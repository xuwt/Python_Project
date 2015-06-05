# -*- coding:utf-8 -*-

#  Collections
#namedtuple
p = (1,2)
print p

from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print p.x ,p.y
print isinstance(p, Point)
print isinstance(p, tuple)

Circle = namedtuple('Circle',['x','y','z'])

#deque
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print q

#defaultdict
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print dd['key1']
print dd['key2']

#orderedDict
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print d

od = OrderedDict([('a',1),('b',2),('c',3)])
print od

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print od.keys()

from collections import OrderedDict
class LastUpdateOrderedDict(OrderedDict):
	def __init__(self,capacity):
		super(LastUpdateOrderedDict,self).__init__()
		self._capacity = capacity
	def __setitem__(self,key,value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last = False)
			print 'remove:',last
		if containsKey:
			del self[key]
			print 'set:',(key,value)
		else:
			print 'add:',(key,value)
		OrderedDict.__setitem__(self,key,value)

#Counter
from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
print c


#Base64
import base64
print base64.b64encode('binary\x00String')
print base64.b64decode('YmluYXJ5AFN0cmluZw==')
print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64decode('abcd--__')

#struct
n = 10240099
b1 = chr((n & 0xff000000) >> 24)
b2 = chr((n & 0xff0000) >> 16)
b3 = chr((n & 0xff00) >> 8)
b4 = chr((n & 0xff))
s = b1 + b2 + b3 + b4
print s

import struct
print struct.pack('>I',10240099)
print struct.unpack('>IH','\xf0\xf0\xf0\xf0\x80\x80')


import struct
def bmpck(picx):
	with open(picx,'rb') as p:
		pp = struct.unpack('<ccIIIIIIHH',p.read(30))
		if pp[0] == 'B':
			if pp[1] == 'M':
				print "%s is a window bitmap" % picx
				print "This bitmap width: %s high: %s,and colorMode is %s!" \
				% (pp[6],pp[7],pp[9])
			elif pp[1] == 'A':
				print "%s is a OS/2 bitmap" % picx
				print "This bitmap width: %s high: %s,and colorMode is %s!" \
				% (pp[6],pp[7],pp[9])
			else:
				print "This file not a bitmap"

#hashlib
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()

#itertools
'''
import itertools
natuals = itertools.count(1)
for n in natuals:
	print n
cs = itertools.cycle('ABC')
for c in cs:
	print c
ns = itertools.repeat('A',10)
for n in ns:
	print n
'''
import itertools
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10,natuals)
for n in ns:
	print n
for c in itertools.chain('ABC','XYZ'):
	print c
for key,group in itertools.groupby('AAABBBCCAAA'):
	print key,list(group)

for key,group in itertools.groupby('AaaBBbcCAAa',lambda c: c.upper()):
	print key,list(group)

for x in itertools.imap(lambda x,y: x * y , [10,20,30],itertools.count(1)):
	print x

r = map(lambda x: x*x,[1,2,3])
print r 

r = itertools.imap(lambda x:x*x,itertools.count(1))
for n in itertools.takewhile(lambda x:x<100,r):
	print n
##ifilter
