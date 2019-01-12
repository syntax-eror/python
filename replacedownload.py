#!/usr/bin/env python 
 
#Download replacer from Learn Python and Ethical Hacking 
#from Scratch course 
 
import netfilterqueue 
import scapy.all as scapy 
 
def process_packet(packet): 
    scapy_packet = scapy.IP(packet.get_payload()) 
    if scapy_packet.haslayer(scapy.Raw): 
        if scapy_packet[scapy.TCP].dport ==80: #if dest port is 80, it's an HTTP request outbound 
            #access TCP layer by using .TCP method 
            print("HTTP Request") 
            print(scapy_packet.show()) 
        elif scapy_packet[scapy.TCP].sport == 80:  #if src port is 80, it's an HTTP response inbound 
            print("HTTP Response") 
            print(scapy_packet.show()) 
 
    packet.accept() 
 
queue = netfilterqueue.NetfilterQueue() 
queue.bind(0, process_packet) 
queue.run()
