# -*- coding:utf-8 -*-


##服务器

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口：
s.bind(('127.0.0.1',9999))

print 'Bind UDP on 9999 ...' 
while True:
	#接收数据
	data,addr = s.recvfrom(1024)
	print 'Received from %s:%s.' % addr
	s.sendto('Hello,%s!' % data , addr)

###客户端

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in ['Michael','Tracy','Sarah']:
	#发送数据
	s.sendto(data,('127.0.0.1',9999))
	#接收数据
	print s.recv(1024)
s.close()
