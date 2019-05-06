#!/usr/bin/env python

#Python 2 version of packet sniffer from LEHAPFS course

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet.show) #packet.show will give field of packet

sniff("eth0")
