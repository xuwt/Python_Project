# -*- coding:utf-8 -*-
#错误异常
import logging

try:
	print 'try ……'
	r = 10 / 0
	print 'result:' , r 	
except ZeroDivisionError, e:
	print 'except:' , e
finally:
	print 'finally . . .'
print 'END'

####
try:
	print 'try ……'
	r = 10 / int('a')
	print 'result:' , r 	
except ValueError,e:
	print 'ValueError:',e
except ZeroDivisionError, e:
	print 'except:' , e
finally:
	print 'finally . . .'
print 'END'

#####
try:
	print 'try ……'
	r = 10 / 2
	print 'result:' , r 	
except ValueError,e:
	print 'ValueError:',e
except ZeroDivisionError, e:
	print 'except:' , e
else:
	print 'no error!'
finally:
	print 'finally . . .'
print 'END'
####
def foo(s):
	return 10/int(s)
def bar(s):
	return foo(s) * 2
def main():
	try:
		bar('0')
	except e:
		print 'Error!'
	finally:
		print 'finally ...'
main()

###logging
def foo(s):
	return 10/int(s)
def bar(s):
	return foo(s) * 2
def main():
	try:
		bar('0')
	except StandarError,e:
		logging.exception(e)
main()
print 'end'