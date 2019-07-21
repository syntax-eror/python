#!/usr/bin/env python3

#adapted from packet_sniffer_python3.py
#This WON'T actually work in python3 currently
#Need to run as python 2, http layer support is different now that scapy_http is deprecated

import scapy.all as scapy

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
    
def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        print(packet.show())        
    
sniff("eth0")
