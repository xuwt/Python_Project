# -*- coding:utf-8 -*-
# 创建文本文件

import os 
# ls代编当前系统下的行为分隔符，window下是\r\n
#unix及类Unix系统下为\n
ls = os.linesep

#获取文件名，文件若是已经存在则要求输入新名字
while True:
	fname = raw_input("Filename:")
	if os.path.exists(fname):
		print 'Error:' + fname + 'already exists'
	else:
		break

#从用户获取文本
all = [] 
print "\n Enter lines ('.' to quit) \n"

while True:
	entry = raw_input('>')
	if entry == '.':
		break
	else:
		all.append(entry)
#创建文件并写入
fobj = open(fname,'w')
#强大的列表解析
fobj.writelines(['%s%s' % (x,ls) for x in all])
#别忘记关闭文件
fobj.close()
print 'Done'