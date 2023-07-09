import subprocess
import re
import random


class MacChanger:
    def __init__(self, interface):
        self.interface = interface
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
        self.change_mac()
        self.check_output()


if __name__ == "__main__":
    interface = input("Enter the interface to change: ")
    mac_changer = MacChanger(interface)
    mac_changer.run()
