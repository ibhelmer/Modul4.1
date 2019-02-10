#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 00:03:40 2019

@author: Ib Helmer Nielsen
"""
#!/usr/bin/env python3

import socket
import time

HOST = '0.0.0.0'  
PORT = 1234       # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            recvStr =data.decode()
            cmdStr = 'TIME'
            timenow=time.strftime("%c")
            if recvStr==cmdStr :
                conn.sendall(bytes(timenow,'utf-8'))
            else:
                conn.sendall(data)
            if not data:
                break

