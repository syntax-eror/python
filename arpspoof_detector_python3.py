#!/usr/bin/env python3

#adapted from packet_sniffer_python3.py
#This WON'T actually work in python3 currently
#Need to run as python 2, http layer support is different now that scapy_http is deprecated

import scapy.all as scapy

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request #append arp_request to broadcast and store as new variable arp_request_broadcast
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
    
def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        real_mac = get_mac(packet[scapy.ARP].psrc)
        response_mac = packet[scapy.ARP].hwsrc
        #use packet.show to show which fields you need to get the above responses
        #psrc is in the ARP layer, etc
        if real_mac != response_mac:
            print("!! Possible ARP spoof detected, ARP MAC does not equal what it should!!")
        print(packet.show())        
    
sniff("eth0")
