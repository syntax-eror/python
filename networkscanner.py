#!/usr/bin/env python

#network scanner from StationX Learn Python course

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request # / appends arp_request to broadcast
	answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
	
	clients_list = []
	
	for element in answered_list:
	    client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
		clients_list.append(client_dict)
	return clients_list
	
def print_result(results_list):
    print("\nIP\t\t\tMAC Address\n----------------------")
	for client in results_list:
	    print(client["ip"] + "\t\t" + client["mac])
		
target_ip = raw_input("Enter IP subnet to scan, include subnet mask in /xx notation: ")
scan_result = scan(target_ip)
print_result(scan_result)
