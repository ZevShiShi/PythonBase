#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename:save_file.py

import cgi
import os
import cgitb

cgitb.enable()

form = cgi.FieldStorage()

# 获取文件表单
file_item = form['filename']

# 检测文件是否上传
if file_item.filename:
    # 设置文件路径 获取路径最后的文件名称
    fn = os.path.basename(file_item.filename)
    open('~/' + fn, 'w').write(file_item.filename)
    message = '文件"' + fn + '"上传成功'
else:
    message = '文件没有上传'

print("Content-type:text/html;charset=utf-8")
print('')
print('<html>')
print('<head>')
print("<title>菜鸟教程 CGI 测试实例</title>")
print('</head>')
print('<body>')
print('<p>%s</p>' % message)
print('</body>')
print('</html>')
