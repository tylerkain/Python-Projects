#!/usr/bin/env python3
"""Modules"""

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan('192.168.4.1')