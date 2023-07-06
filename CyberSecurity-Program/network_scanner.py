#!/usr/bin/env python3

import scapy.all as scapy
import argparse


def get_input():
    """Get IP CLI"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="IP address/range to scan")
    args = parser.parse_args()

    if not args.ip:
        parser.error("[-] Please specify IP or IP range. Use --help for more information.")

    return args


def scan(ip):
    """Scan Network For Connected Devices"""
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    client_list = []

    for element in answered_list:
        client_dictionary = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
        client_list.append(client_dictionary)

    return client_list


def print_results(results_list):
    """Print results of IP Scan"""
    for client in results_list:
        print(client["IP"], client["MAC"])


def main():
    options = get_input()
    scan_result = scan(options.ip)
    print_results(scan_result)


if __name__ == "__main__":
    main()
