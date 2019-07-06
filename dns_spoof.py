#!/usr/bin/env python3

#iptables -I FORWARD -j NFQUEUE --queue-num 0
#iptables --flush - delete rules set up

import netfilterqueue
#need to have module installed - pip3 install netfilterqueue
#apt-get install build-essential python-dev libnetfilter-queue-dev if errors

def process_packet(packet):
    print(packet)
    packet.drop() #drop packets, connectivity cut
    packet.accept() #forward packets to target, connectivity seems normal


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet) #invoke bind method of NetfilterQueue
#0 - queue number used in iptables
#process packet is a callback function that will be run on each packet
queue.run

#all packets received will be put in the queue that was set up
#on target computer, connectiivty will be interrupted as each packet is being held


