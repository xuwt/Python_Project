# -*- coding:utf-8 -*-

age = 20
if age >= 18:
	print 'your age is' ,age 
	print 'adult'

age = 3
if age >= 18:
	print 'your age is',age 
	print 'adult'
else:
	print 'your age is' ,age 
	print 'teenager'

age = 3
if age >= 18:
	print 'adult'
elif age >=6:
	print 'teenager'
else:
	print 'kid'
x ='wi '
if x:
	print 'True'

#循环
names = ['Michael' , 'Bob' ,'Tracy']
for name in names:
	print name 

sum = 0
for x in [1,2,3,4,5,6,7,8]:
	sum = sum + x 
print sum 

print range(5)

sum = 0
for x in range(101):
	sum = sum + x 
print sum 

#while
sum = 0
n = 99
while n > 0:
	sum = sum + n 
	n = n -2 
print sum 

