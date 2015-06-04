# -*- coding:utf-8 -*-

import time,threading

#新线程执行的代码：
def loop():
	print 'trhead %s is running ...' % threading.current_thread().name
	n = 0
	while n < 5:
		n = n + 1
		print 'thread %s >>> %s' % (threading.current_thread().name , n)
		time.sleep(1)
	print 'thread %s ended ...' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target = loop , name = 'LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name


import time,threading

#假定这是你的银行存款：
balance = 0
lock = threading.Lock()


def change_it(n):
	#先存后取，结果应该为0：
	global balance
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for i in range(100000):
		#先获取锁：
		lock.acquire()
		try:
			#放心改：
			change_it(n)
		finally:
			#改完释放锁
			lock.release()
		

t1 = threading.Thread(target = run_thread , args = (5,))
t2 = threading.Thread(target = run_thread , args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance

#死循环线程
'''
import threading,multiprocessing
def loop():
	x = 0
	while True:
		x = x ^ 1
for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target = loop)
	t.start()
'''

