#!/usr/bin/env python 
from mac_changer import change_mac
from portscanner import scan
while True: 
 user_selection = input("select program you want to run: \n 1: Change_Mac \n 2: Network_Scan \n")
 if user_selection == '1':
        change_mac()
 elif user_selection == '2':
        targets = input("[*] Enter Targets To Scan(split them by ,): ")
        ports = int(input("[*] Enter How Many Ports You Want To Scan: ")) 
        scan(targets, ports)
