#!/usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)
    
scan("10.0.2.1")
