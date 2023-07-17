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

import subprocess
import getmac


import subprocess
import getmac
import time


class WifiScan:
    def __init__(self, adapter):
        self.adapter = adapter

    def capture_handshake(self):
        """Capture WPA handshake"""
        print("Capturing handshake")

        # Get the current MAC address
        current_mac = getmac.get_mac_address(interface=self.adapter)
        print("Current MAC address:", current_mac)

        while True:
            try:
                self.run_airodump()
                break
            except subprocess.CalledProcessError as e:
                print("Error: Failed to retrieve BSSIDs:", e)

        # Continue with the rest of the code for selecting BSSID, channel, and running airodump-ng
        bssid_choice = int(input("Select the client BSSID: "))
        selected_bssid = self.bssids[bssid_choice - 1]
        channel = selected_bssid[1]
        client_bssid = selected_bssid[0]
        handshake_file = input("[+] Input handshake file name: ")

    def run_airodump(self):
        """Run airodump-ng with timer"""
        duration = 10
        subprocess.run(['airodump-ng', '--berlin', '--output-format', 'csv', '--write', 'temp', self.adapter],
                       timeout=duration)
    def run_wifi_scan(self):
        self.capture_handshake()


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

    # Execute the desired function after the scan
    print("Scanning complete. Running the next function...")
    # Run the next function here


if __name__ == "__main__":
    main()


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
