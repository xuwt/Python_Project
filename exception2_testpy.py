# -*- coding:utf-8 -*-
import logging

###logging
def foo(s):
	return 10/int(s)
def bar(s):
	return foo(s) * 2
def main():
	try:
		bar('0')
	except BaseException,e:
		logging.exception(e)
main()
print 'end'

###
class FooError(BaseException):
	pass
def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' % s)
	return 10 / n 
foo('s')
