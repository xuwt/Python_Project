# -*- coding:utf-8 -*-

#sqlite
#导入sqlite驱动：
import sqlite3
#连接到SQLite数据库
#数据库文件是test.db
#如果文件不存在，会自动在当前目录创建：
conn = sqlite3.connect('test.db')
#创建一个Cursor：
cursor = conn.cursor()
#执行一条sql语句，创建user表：
cursor.execute('create table user (id varchar(20) primary key, \
	name varchar(20))')
#继续执行一条sql语句，插入一条记录：
cursor.execute('insert into user (id,name) values (\'1\',\'Michael\')')
#通过rowcount获取插入的行数：
print cursor.rowcount
#关闭Cursor:
cursor.close()
#提交事务
conn.commit()
#关闭Connection
conn.close()


conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#执行查询语句：
cursor.execute('select * from user where id = ?', '1')
#获得查询结果：
values = cursor.fetchall()
print values
cursor.close()
conn.close()