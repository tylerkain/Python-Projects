''' modules'''
import subprocess
import optparse


def get_input():
    """Get user input"""
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="interface to change")
    parser.add_option("-m", "--mac", dest="new_mac",
                      help="new mac address for interface")
    (options, args) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify interface, use --help")
    elif not options.mac:
        parser.error("[-] Please specify mac, use --help")
    return options


def change_mac(interface, mac):
    '''MAC Changer Function '''
    print(f'changing {interface} to {mac}')
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])
    subprocess.call(['ifconfig', interface, 'up'])


options = get_input()
change_mac(options.interface, options.mac)
