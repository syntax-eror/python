#!/usr/bin/env python3

import scapy.all as scapy
from scapy_http import http #need scapy_http installed
#pip install scapy_http
#pip3 install scapy_http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter="port 21")
    #, filter=    filters can be tcp, udp, etc. or specify port by doing port 80
    
def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest): #haslayer - scapy method
        print(packet)
    
sniff("eth0")
