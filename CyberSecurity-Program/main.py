#!/usr/bin/env python
import mac_changer 
while True:
    user_selection = input("select program you want to run: \n 1: Change_Mac \n 2: Network_Scan \n")
    if user_selection == '1':
           mac_changer.change_mac(interface=mac_changer.options, mac=mac_changer.options)
