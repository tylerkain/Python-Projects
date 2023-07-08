import nmap
import argparse


class ScanNetworkTool:
    def __init__(self, ip, output, scan_arguments):
        self.ip = ip
        self.output = output
        self.scan_arguments = scan_arguments

    def scan_network(self):
        nm = nmap.PortScanner()
        print("Running nmap scan with arguments:", self.scan_arguments)
        nm.scan(self.ip, arguments=self.scan_arguments)

        results = {}

        for idx, host in enumerate(nm.all_hosts(), 1):
            print(f"Scanning host {idx}/{len(nm.all_hosts())} - IP: {host}")
            host_details = {
                "IP": host,
                "Open Ports": [],
                "Device": "",
                "OS": "",
                "Service Versions": {},
            }

            if 'tcp' in nm[host]:  # Check if 'tcp' key exists in the dictionary
                for port in nm[host]['tcp'].keys():
                    if nm[host]['tcp'][port]['state'] == 'open':
                        host_details["Open Ports"].append(port)

            if 'vendor' in nm[host]:
                host_details["Device"] = nm[host]['vendor']

            if 'osmatch' in nm[host]:
                host_details["OS"] = nm[host]['osmatch'][0]['name']

            if 'tcp' in nm[host] and 'script' in nm[host]['tcp']:
                for port in nm[host]['tcp'].keys():
                    if nm[host]['tcp'][port]['state'] == 'open':
                        script_output = nm[host]['tcp'][port]['script']
                        if script_output:
                            host_details["Service Versions"][port] = script_output

            results[host] = host_details

        return results

    def save_results(self, results_dict):
        """Save results to a text file"""
        with open(self.output, 'w') as file:
            for host, details in results_dict.items():
                file.write(f"Host: {host}\n")
                file.write(f"IP: {details['IP']}\n")
                file.write(f"Open Ports: {details['Open Ports']}\n")
                file.write(f"Device: {details['Device']}\n")
                file.write(f"OS: {details['OS']}\n")
                file.write("Service Versions:\n")
                for port, service_version in details['Service Versions'].items():
                    file.write(f"Port: {port}, Service Version: {service_version}\n")
                file.write("\n")

    def run_network_scanner(self):
        scan_result = self.scan_network()
        if scan_result:
            self.save_results(scan_result)
            print("Scan results saved to", self.output)
        else:
            print("No scan results found.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="IP address/range to scan")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--scan", help="Additional nmap scan arguments")
    args = parser.parse_args()

    if not args.ip:
        parser.error("[-] Please specify IP or IP range. Use --help for more information.")

    tool = ScanNetworkTool(args.ip, args.output, args.scan)
    tool.run_network_scanner()


if __name__ == "__main__":
    main()
