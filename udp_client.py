#!/usr/bin/env python3

import socket

target_host = "127.0.0.1"
target_port = 9998

# create socket object newsock
# AF_INET = use IPv4 addr/hostname, SOCK.DGRAM = UDP client
newsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send info over connectin
newsock.sendto(b"TEST",(target_host,target_port))

# receive data in response
data, addr = newsock.recvfrom(4096)

print(data.decode())
newsock.close()