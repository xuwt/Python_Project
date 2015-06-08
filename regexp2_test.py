# -*- coding:utf-8 -*-

#导入re模块
import re

#将正则表达式编译成Pattern对象，注意hello前面的r的意思是‘原生字符串’
pattern = re.compile(r'hello')

#使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.match(pattern,'hello')
result2 = re.match(pattern,'helloo xuwt!')
result3 = re.match(pattern,'helo xuwt!')
result4 = re.match(pattern,'hello xuwt!')

if result1:
	print result1.group()
else:
	print 'result1匹配失败'

if result2:
	print result2.group()
else:
	print 'result2匹配失败'

if result3:
	print result3.group()
else:
	print 'result3匹配失败'

if result4:
	print result4.group()
else:
	print 'result4匹配失败'