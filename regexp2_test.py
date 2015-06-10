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

###简单的match实例
import re
print '*******'
m = re.match(r'(\w+) (\w+)(.*)','hello world!')
print m.string
print m.pos
print m.groups()


### search方法
#将正则表达式编译成Pattern对象
pattern = re.compile(r'world')
#使用search()查找匹配的子串，不存在能匹配的子串时将
#返回None，这个例子中使用match（）无法成功匹配
search = re.search(pattern,'hello world!')
match = re.match(pattern,'hello world!')
print search,match

if search:
	print search.group()

##  split方法
pattern = re.compile(r'\d+')
print re.split(pattern,'one1two2three3four4')

### findall方法
pattern = re.compile(r'\d+')
print re.findall(pattern,'one1two2three3four4')

### finditer
pattern = re.compile(r'\d+')
iters = re.finditer(pattern,'one1two2three3four4')
print iters
for m in iters:
	print m.group(),

print '\r\n'

### sub
pattern =re.compile(r'(\w+) (\w+)')
s = 'i say,hello world!'

print re.sub(pattern,r'\2 \1',s)

def func(m):
	return m.group(1).title() + ' ' + m.group(2).title()

print re.sub(pattern,func,s)