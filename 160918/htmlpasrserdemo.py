#!/usr/bin/python
# -*- coding: utf-8 -*-
#HTMLParser

#如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下
#来，第二步就是解析该 HTML 页面，看看里面的内容到底是新闻、图片还是视频。

#HTML 本质上是 XML 的子集，但是 HTML 的语法没有 XML 那么严格，
#所以不能用标准的 DOM 或 SAX 来解析 HTML。

#Python 提供了 HTMLParser 来非常方便地解析 HTML
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
	def handle_starttag(self,tag,attrs):
		print('<%s>'%tag)

	def handle_endtag(self,tag):
		print('</%s>' %tag)

	def handle_startendtag(self,tag,attrs):
		print('<%s/>' % tag)
	
	def handle_data(self, data):
		print(data)

	def handle_comment(self, data):
		print('<!--', data, '-->')
	
	def handle_entityref(self, name):
		print('&%s;' % name)

	def handle_charref(self, name):
		print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
 <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

#feed()方法可以多次调用，也就是不一定一次把整个 HTML 字符串都塞进去，可以一部分一部分塞进去。

#特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过 Parser 解析出来。

















