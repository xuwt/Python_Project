# -*- coding:utf-8 -*-
#默认参数
def power(x):
	return x * x 

print power(14)

def powers(x , n):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x 
	return s 

print powers(5,3)

def defaultPower(x,n = 2):
	s = 1
	while n > 0:
		n = n -1
		s = s * x 
	return s 

print defaultPower(25)
print defaultPower(24,3)

def enroll(name,gender):
	print 'name',name
	print 'gender',gender
enroll('Sarah',"F")

def enroll2(name,gender,age = 6,city = 'Beijing'):
	print 'name:',name
	print 'gender' ,gender
	print 'age:',age 
	print 'city:', city

enroll2('sarah','f')

enroll2('Bob',"M",7)
enroll2('Adam','M',city = 'tianjin')

def add_end(L = []):
	L.append('END')
	return L 

print add_end(['1','2','3'])

def add_none(L = None):
	if L is None:
		L = []
	L.append("end")
	return L 

print add_none()

#可变参数
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n 
	return sum 

print calc([1,2,3])
print calc(range(8))
#上面的calc是不可变
def cal(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n 
	return sum 
print cal()

nums = [1,2,3]
print cal(*nums)
#关键字参数
def person(name,age,**kw):
	print 'name',name,'age',age,'other',kw
person('mick',30)

person('bob',33,city = 'beijing')
person('adm',20,gender = 'M',job = 'Engineer')

def func(a,b,c = 0, *args, **kw):
	print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw

func(1,2)
func(1,2,c = 3)
func(1,2,3,'a','b')
func(1,2,3,'a','b',x = 99)

args = (1,2,3,4)
kw = {'x':45}
func(*args,**kw)
