import subprocess
import argparse
import re


def get_input():
    """Get input"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", help="specify interface to change")
    parser.add_argument("-m", "--mac", help="specify new MAC address for interface")
    args = parser.parse_args()

    if not args.interface:
        parser.error("[-] Please specify interface. Use --help for more information.")
    elif not args.mac:
        parser.error("[-] Please specify MAC address. Use --help for more information.")

    return args


def change_mac(interface, mac):
    '''Mac changer function'''
    print(f'Changing {interface} to {mac}')

    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])
    subprocess.call(['ifconfig', interface, 'up'])


def check_output(interface):
    """Check output of interface"""
    result = subprocess.check_output(["ifconfig", interface], encoding='utf8')
    output = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result)

    if output:
        print(output.group(0))
    else:
        print("No MAC address found.")


def main():
    options = get_input()
    change_mac(options.interface, options.mac)
    check_output(options.interface)


if __name__ == "__main__":
    main()
