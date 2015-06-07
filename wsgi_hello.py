# -*- coding:utf-8 -*-

##web_hello

def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	return '<h1>Hello,Web! %s </h1>' % (environ['PATH_INFO'][1:] or 'web')