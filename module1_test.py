# -*- coding:utf-8 -*-

# 模块别名
try:
	import cStringIO as StringIO
except ImportError: #导入失败会捕获到ImportError
	import StringIO

try:
	import json #python >= 2.6
except ImportError:
	import simplejson as json # python <= 2.5

#private函数
def _private_1(name):
	return 'Hello,%s' % name 
def _private_2(name):
	return 'Hi,%s' % name

def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)