# -*- coding:utf-8 -*-

#导入mysql驱动：
import mysql.connector
#注意把password设为你的root口令
conn = mysql.connector.connect(user = 'root',password = 'password',\
	database = 'test',use_unicode = True)
cursor = conn.cursor()

#创建user表：
cursor.execute('create table user ( id varchar(20) primary key,name varchar(20))')
#插入一行记录，注意mysql的占位符是%s：
curosr.execute('insert into user(id,name) values (%s,%s)',['1','Michael'])
print curosr.rowcount

#提交事务
conn.commit()
curosr.close()


#运行查询
curosr = conn.curosr()
curosr.execute('select * from user where id = %s','1')
values = vursor.fetchall()
print values
#关闭Cursor和Connection
curosr.close()
conn.close()

