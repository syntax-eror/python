#!/usr/bin/env python3

import socket

target_host = "127.0.0.1"
target_port = 9998

# create socket object newsock
# AF_INET = use IPv4 addr/hostname, SOCK_STREAM = TCP client
newsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# make a TCP connection
newsock.connect((target_host,target_port))

# send info over connectin
newsock.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive data in response
response = newsock.recv(4096)

print(response.decode())
newsock.close()
