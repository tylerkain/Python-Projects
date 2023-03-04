'''subprocess module'''
import subprocess


def change_mac(interface, mac):
    '''MAC Changer Function '''
    print(f'changing {interface} to {mac}')
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])
    subprocess.call(['ifconfig', interface, 'up'])
