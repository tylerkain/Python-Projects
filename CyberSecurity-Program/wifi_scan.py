#!/usr/bin/env python
"""Modules"""
import subprocess

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

monitor_mode(adapter)
check_wps(adapter)   