import subprocess
import argparse
import re
import random


class MacChanger:
    def __init__(self):
        self.interface = None
        self.mac = None

    def get_input(self):
        """Get input"""
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--interface", help="specify interface to change")
        args = parser.parse_args()

        if not args.interface:
            parser.error("[-] Please specify interface. Use --help for more information.")
        self.interface = args.interface
        self.mac = self.generate_random_mac()

    def generate_random_mac(self):
        """Generate a random MAC address"""
        mac = [random.randint(0x00, 0xff) for _ in range(6)]
        mac_str = ':'.join(map(lambda x: f'{x:02x}', mac))
        return mac_str

    def change_mac(self):
        '''Mac changer function'''
        print(f'Changing {self.interface} to {self.mac}')

        subprocess.call(['ifconfig', self.interface, 'down'])
        subprocess.call(['ifconfig', self.interface, 'hw', 'ether', self.mac])
        subprocess.call(['ifconfig', self.interface, 'up'])

    def check_output(self):
        """Check output of interface"""
        result = subprocess.check_output(["ifconfig", self.interface], encoding='utf8')
        output = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result)

        if output:
            print(output.group(0))
        else:
            print("No MAC address found.")

    def run(self):
        self.get_input()
        self.change_mac()
        self.check_output()


if __name__ == "__main__":
    mac_changer = MacChanger()
    mac_changer.run()
