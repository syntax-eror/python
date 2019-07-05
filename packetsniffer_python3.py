#!/usr/bin/env python3

import scapy.all as scapy
from scapy_http import http #need scapy_http installed
#scapy_http is now deprecated, and scapy has native support for HTTP: https://github.com/invernizzi/scapy-http
#need to find way to implement
#pip install scapy_http
#pip3 install scapy_http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter="port 21")
    #prn = pass to a function for each packet
    #, filter=    filters can be tcp, udp, etc. or specify port by doing port 80
    # http://biot.com/capstats/bpf.html - filters you can use
    
def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest): #haslayer - scapy method
        print(packet)
    
sniff("eth0")
