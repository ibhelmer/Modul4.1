#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 00:21:56 2019

@author: pi
"""

import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 1123
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
   data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
   print ("received message:", data)
