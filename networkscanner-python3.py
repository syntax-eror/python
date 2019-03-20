#!/usr/bin/env python3

import scapy.all as scapy

#def scan(ip):
    #arp_request = scapy.ARP(pdst = ip) #pdst is a field that needs to be set to tell where the-
    #ARP packet should be directed
    #the specific field can be found using scapy.ls; scapy.ls(scapy.ARP())
    #arp_request.show() #module in scapy to show detail of packet
    #arp_request.pdst = ip - another way to set the pdst
    #print(arp_request.summary())
    #broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") #create Ethernet object called Broadcast
    #that has the dst field set to broadcast address
    #broadcast.show()
    #print(broadcast.sumary())
    #scapy.ls(scapy.ARP()) #scapy module to return list of fields use in scapy.ARP
    #using this, you see that pdst is the field you want to set
    #scapy.arping(ip)
    #scapy.ls(scapy.Ether())
    #arp_request_broadcast = broadcast/arp_request #/ is a scapy method to append;
    #this appends arp_request to the end of broadcast to create a new variable
    #print(arp_request_broadcast.summary())
    #arp_request_broadcast.show()
    #answered, unanswered = scapy.srp(arp_request_broadcast, timeout = 1) - scapy.srp returns a couple of two lists
    #-this stores them in these two variables
    #-timeout used to exit if no response is received, otherwise it will continue running
    print(answered.summary()) #summary is a scapy method that will list the info stored in answered variable
    print(unanswered.summary())
    
#scan("10.0.2.1")

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    #answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout = 1)
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0] #only return element 0 from list;
    #since scapy.srp returns two lists, this lets it know to only return the first element in a 0-indexed list
    #print(answered_list.summary())
    
    print("IP\t\t\tMAC Address")
    
    for element in answered_list: #this for loop breaks the list out into each element
        #print(element)
        #print(element[1]) #second part of list is the raw packet info
        #print(element[1].show()) #to show all fields in packet
        #print("answered list is type: ", type(answered_list))
        print(element[1].psrc) #print source IP
        print(element[1].hwsrc) #print source MAC
        print("------------------------------")
    
scan("10.0.2.1/24")
    
