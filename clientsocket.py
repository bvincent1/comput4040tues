#!/usr/bin/env python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("129.128.41.35",12345))

request = "GET / HTTP/1.0\n\n"

s.sendall(request)

done = False
while not done:
	part = s.recv(2048)
	if (part):
		print part
	else:
		done = True


