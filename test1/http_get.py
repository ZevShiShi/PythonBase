#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename:http_get.py
# Get请求
# 将文件放入/Library/WebServer/CGI-Executables目录下
# http://localhost/cgi-bin/cgi1.py?name=菜鸟教程&url=http://www.runoob.com

# CGI处理模块
import cgi, cgitb

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('name')
site_url = form.getvalue('url')

print("Content-type:text/html")
print('')
print('<html>')
print('<head>')
print("<title>菜鸟教程 CGI 测试实例</title>")
print("<meta charset=\"utf-8\">")
print('</head>')
print('<body>')
print("<h2>%s官网：%s</h2>" % (site_name, site_url))
print('</body>')
print('</html>')

