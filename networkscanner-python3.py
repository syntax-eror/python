#!/usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    arp_request.show() #module in scapy to show detail of packet
    #arp_request.pdst = ip - another way to set the pdst
    #print(arp_request.summary())
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") #create Ethernet object called Broadcast
    #that has the dst field set to broadcast address
    broadcast.show()
    print(broadcast.sumary())
    #scapy.ls(scapy.ARP()) #scapy module to return list of fields use in scapy.ARP
    #using this, you see that pdst is the field you want to set
    #scapy.arping(ip)
    #scapy.ls(scapy.Ether())
    arp_request_broadcast = broadcast/arp_request #/ is a scapy method to append;
    #this appends arp_request to the end of broadcast to create a new variable
    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()
    
scan("10.0.2.1")
