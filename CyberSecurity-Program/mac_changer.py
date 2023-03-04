''' modules'''
import subprocess
import optparse
import re


def get_input():
    """Get input"""
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="interface to change")
    parser.add_option("-m", "--mac", dest="mac",
                      help="new mac address for interface")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify interface, use --help")
    elif not options.mac:
        parser.error("[-] Please specify mac, use --help")
    return options


def change_mac(interface, mac):
    '''Mac changer function '''
    print(f'changing {interface} to {mac}')
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])
    subprocess.call(['ifconfig', interface, 'up'])


def check_output():
    """check output of interface"""
    result = subprocess.check_output(["ifconfig", options.interface])
    output = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result )
    return output


options = get_input()
change_mac(options.interface, options.mac)
check_output()
