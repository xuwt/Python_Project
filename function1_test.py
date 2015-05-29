# -*- coding:utf-8 -*-

print abs(1000)
print abs(-20)
print cmp(1,2)

print int('123')

print float('12.34')
print unicode(100)
print bool(1)

a = abs
print a(-1)

def my_abs(x):
	if not isinstance(x, (int,float)):
		print 'bad operand type'
	if x >= 0:
		return x 
	else:
		return -x 
print my_abs(-2354)
my_abs('a')

def nop():
	pass

import math

def move(x,y,step,angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)

	return nx,ny 

x , y = move(100,100,60,math.pi / 6)
print x ,y 

r = move (100,100,60,math.pi/6)
print r 
