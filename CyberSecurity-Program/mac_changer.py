import subprocess


def change_mac():
    subprocess.call('ifconfig', shell=True)
    interface = input('[+] Wireless adapter to change: ')
    mac = input ('[+] New MAC address:  ')
    subprocess.call(f'ifconfig {interface} down', shell=True)
    subprocess.call(f'ifconfig {interface} hw ether {mac}', shell=True)
    print(f'changing {interface} to {mac}')
    subprocess.call(f'ifconfig {interface} up')

