#!/usr/bin/env python

import socket
import os

s_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_in.bind(("0.0.0.0",12345))

s_in.listen(5)

while True:
	(client, addr) = s_in.accept()
	print str(addr)
	
	cpid = os.fork()
	
	if cpid != 0:
		continue
	else:
		s_out = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s_out.connect(("www.google.ca", 80))
		
		done = False
		while not done:
				s_in.setblocking(0)
				
				try:
					part = s_in.recv(2048)
				except IOError:
					if exception.errno == 11:
						part = None
					else:
						raise 
				
				if (part):
					s_out.sendall(part)					
				s_out.setblocking(0)
				
				try:	
					part = s_out.recv(2048)
				except IOError:
					if exception.errno == 11:
						part = None
					else:
						raise
				
				if (part):
					s_in.sendall(part)
				else:
					done = True

