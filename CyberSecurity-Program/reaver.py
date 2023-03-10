import subprocess
"""Modules"""

def reaver(adapter): 
    """reaver scan"""
    channel = input("[+] input channel: ")
    wifi_mac = input("[+] Input wifi mac address: ")
    interface = adapter
    subprocess.call(['reaver', '--bssid', wifi_mac,'--channel', channel, '--interface', interface '-vvv', '--no-associate'])