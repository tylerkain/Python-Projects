'''subprocess module'''
import subprocess


def change_mac(interface, mac):
    '''MAC Changer Function '''
    subprocess.call(['ifconfig'], shell=True)
    subprocess.call(['ifconfig', interface, 'down'], shell=True)
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac], shell=True)
    print(f'changing {interface} to {mac}')
    subprocess.call(['ifconfig', interface, 'up'], shell=True)
