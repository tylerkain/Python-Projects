import socket
from IPy import IP

class PortScan:
    banners = []
    open_ports = []

    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num

    def scan(self):
        for port in range(1, self.port_num+1):
            self.scan_port(port)

    def check_ip(self):
        try:
            IP(self.target)
            return self.target
        except ValueError:
            return socket.gethostbyname(self.target)

    def scan_port(self, port):
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(2)
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
            except:
                self.banners.append(' ')
            sock.close()
        except:
            pass

    def save_open_ports(self, output_file):
        with open(output_file, 'w') as file:
            for port in self.open_ports:
                file.write(f"Open port: {port}\n")

def main():
    targets_ip = input('[+] * Enter Target To Scan For Vulnerable Open Ports: ')
    port_number = int(input('[+] * Enter Amount Of Ports You Want To Scan (500 - first 500 ports): '))
    output_file = input('[+] * Enter the output file path to save open ports: ')
    print('\n')

    target = PortScan(targets_ip, port_number)
    target.scan()
    target.save_open_ports(output_file)

if __name__ == "__main__":
    main()
