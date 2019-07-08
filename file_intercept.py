#!/usr/bin/env python

#doesn't actually work in python3 currently, errors about str being returned instead of bytes-like object

#iptables -I FORWARD -j NFQUEUE --queue-num 0
#iptables --flush - delete rules set up
#iptables -I OUTPUT -j NFQUEUE --queue-num 0
#set up for your own computer


import netfilterqueue
#need to have module installed - pip3 install netfilterqueue
#apt-get install build-essential python-dev libnetfilter-queue-dev if errors
import scapy.all as scapy
import subprocess

def set_iptables():
    print("\n[+] Setting up IPTables\n")
    #python3 code:
    #subprocess.run(["iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    #subprocess.run(["iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    #python2 code:
    subprocess.call(["iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    subprocess.call(["iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    
def restore_iptables():
    print("\n[+] Flushing IPTables\n")
    #subprocess.run(["iptables", "--flush"])
    subprocess.call(["iptables", "--flush"])

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload()) #store packet as a variable;
    #wrapped in scapy layer that lets you access layers of packet using scapy;
    #then able to modify
    if scapy_packet.haslayer(scapy.Raw): #http request is in the Raw layer in scapy
        if scapy_packet[scapy.TCP].dport == 80: #if this exists, packet is HTTP request outbound
            print("\nHTTP Request outbound found:\n")
            print(scapy_packet.show())
            if ".exe" in scapy_packet[scapy.Raw].load:
                print("EXE found")
                print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport = 80: #if this exists, packet is HTTP response inbound
            print("\nHTTP Response inbound found:\n")
            print(scapy_packet.show())
            
        #print(scapy_packet.show()) #print out any packet with a RAW layer;
        #this will show packets that have HTTP requests, so it can be narrowed
        #down to what fields are being looked for to find file download requests
        #only works for http

    packet.accept() #forward packets to target, connectivity seems normal

try:
    while True:
        set_iptables()
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, process_packet) #invoke bind method of NetfilterQueue
        #0 - queue number used in iptables
        #process packet is a callback function that will be run on each packet
        queue.run
except KeyboardInterrupt:
    print("\n[+] Stopping DNS Spoof")
    restore_iptables()
#all packets received will be put in the queue that was set up
#on target computer, connectivity will be interrupted as each packet is being held
