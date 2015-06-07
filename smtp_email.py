# -*- coding:utf-8 -*-

##smtp发送邮件
from email.mime.text import MIMEText
msg = MIMEText('hello,send by Python ...' ,'plain','utf-8')

#输入emil地址和口令：
from_addr = raw_input('From:')
password = raw_input('Password:')

#输入smtp服务器地址：
smtp_server = raw_input('SMTP server:')
#输入收件人地址：
to_addr = raw_input('To:')


import smtplib
#smtp协议默认端口是25
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()


###完整的发送email
from email import encoders
from email.header improt Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smptlib

def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr(( \ 
		Header(name,'utf-8'),encode(), \ 
		addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input('From:')
password = raw_input('Password:')
to_addr = raw_input('To:')
smtp_server = raw_input('SMTP server:')

msg = MIMEText('hello,send by Python...','plain','utf-8')
msg['From'] = _format_addr(u'Python爱好者 <%s> ' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s> ' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候......','utf-8').encode()
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

#html邮件
msg = MIMEText('<html>','html','utf-8')

#添加附件
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……','utf-8').encode()
#邮件正文MIMIText：
msg.attach(MIMEText('send with file ...','plain','utf-8'))
#添加附件就是加上一个MIMTBase，从本id读取一个图片：
with open('test.png','rb') as f:
	#设置附件的MIME和文件名，这里是png类型：
	mime = MIMEBase('image','png',filename = 'test.png')
	#加上必要的头信息：
	mime.add_header('Content-Disposition','attachment',filename = 'test.png')
	mime.add_header('Content-ID','<0>')
	mime.add_header('X-Attachment-Id','0')
	#把附件的内容读进来：
	mime.set_payload(f.read())
	#用base64编码：
	encoders.encode_base64(mime)
	#添加到MIMEMultipart：
	msg.attach(mime)

##创建安全连接
#gmail的smtp端口是587
smtp_server ='smtp.gmail.com'
smtp_port = 587
server = smptlib.SMTP(smtp_server,smtp_port)
server.starttls()
#剩下的代码和上面的都一样了
server.set_debuglevel(1)


