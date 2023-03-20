#!/usr/bin/env python3
"""Modules"""

import scapy.all as scapy
import optparse

def get_input():
    """Get IP CLI"""
    parser = optparse.OptionParser()
    parser.add_option("--ip", dest="ip",
                      help="IP address/range to scan")
    (options, arguments) = parser.parse_args()
    if not options.ip:
        parser.error("[-] Please specify ip or ip range, use --help")
    return options

def scan(ip):
    """Scan Network For Connected Devices"""
    arp_request = scapy.ARP(pdst=ip)
    broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    client_list=[]
    for element in answered_list: 
        client_dictionary = {"IP" : element[1].psrc, "MAC" : element[1].hwsrc }
        client_list.append(client_dictionary)
    return client_list

def results(results_list):
    """Results of IP Scan"""
    for client in results_list:
        print(client["IP"], client["MAC"])

options = get_input()
scan_result = scan(options.ip)
results(scan_result)