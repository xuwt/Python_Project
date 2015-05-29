# -*- coding:utf-8 -*-

#dict
d = {'mickael':95,'bob':75,'tracy':85}
print d 
d['admin'] = 67
print d 
print 'tome' in d
print d.get('bob')

#get 默认值
print d.get('xuwt','02')

d.pop('bob')
print d 

# set
s = set([1,2,3])
print s 
s.add(4)
print s 
s.remove(3)
print s

s1 = set([1,2,3])
s2 = set([2,3,4])
print s1 & s2
print s1 | s2

a = ['c','b','a']
a.sort()
print a 

a = 'abc'
a.replace('a', 'A')
print a 

b = a.replace('a','A')
print b 
print a 