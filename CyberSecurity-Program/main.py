#!/usr/bin/env python
from mac_changer import change_mac
while True:
    user_selection = input("select program you want to run: \n 1: Change_Mac \n 2: Network_Scan \n")
    if user_selection == '1':
        interface = input('[+] Wireless adapter to change: ')
        mac = input('[+] New MAC address:  ')
        change_mac(interface, mac)
