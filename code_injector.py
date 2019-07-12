#!/usr/bin/env python

#doesn't actually work in python3 currently, errors about str being returned instead of bytes-like object

import netfilterqueue
import scapy.all as scapy
import subprocess

def set_iptables(): #automate setting IPtables for testing on localhost
    print("\n[+] Setting up IPTables\n")
    subprocess.call(["iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    subprocess.call(["iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    
def restore_iptables():
    print("\n[+] Flushing IPTables\n")
    subprocess.call(["iptables", "--flush"])
    
def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet
    
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+] HTTP Request outbound found")
            print("===================================")
            print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 80: #if this exists, packet is HTTP response inbound
            print("[+] HTTP Response Inbound found:")
            print("===================================")
            print(scapy_packet.show())
            
            #want to first show the packet contents to see what fields to modify
            #using this you see that the Raw layer contains following:
            #Accept-Encoding: gzip, deflate
            #HTML is compressed with gzip then sent to client from server

    packet.accept() #forward packets to target, connectivity seems normal

try:
    while True:
        set_iptables()
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
except KeyboardInterrupt:
    print("\n[+] Stopping file download interceptor")
    restore_iptables()
