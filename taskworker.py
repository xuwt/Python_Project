# -*- coding:utf-8 -*-

import time,sys,Queue
from multiprocessing.managers import BaseManager

#创建类似的QueueManger：
class QueueManger(BaseManager):
	pass


#由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字：
QueueManger.register('get_task_queue')
QueueManger.register('get_result_queue')

#连接到服务器，也就是运行taskmanager.py的机器：
server_addr = '127.0.0.1'
print('Connect to server %s ...' % server_addr)

#端口和验证码注意保持与taskmanager.py设置的完全一致：
m = QueueManger(address = (server_addr,5000),authkey = 'abc')

#从网络连接：
m.connect()
#获取queue的对象
task = m.get_task_queue
result = m.get_result_queue

#从task队列取任务，并把结果写入result队列：
for i in range(10):
	try:
		n = task.get(timeout = 1)
		print('run task %d * %d ...' % (n , n))
		r = '%d * %d = %d' % (n , n , n * n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty.')
#处理结束：
print('worker exit.')


