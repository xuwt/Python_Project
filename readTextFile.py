# -*- coding:utf-8 -*-

import os

#获取文件名，文件不存在就退出
while True:
	fname = raw_input("Enter filename:")
	if os.path.exists(fname):
		break
	else:
		exit()

#打开文件并读取

try:
	fobj = open(fname , 'r')
except IOError, e:	
	print '*** file open error:' , e
else:
	#显示文本内容
	for eachline in fobj:
		print eachline,
	fobj.close()
exit()