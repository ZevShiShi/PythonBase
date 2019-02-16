#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename:cgi0.py

import os

print("Content-type:text/html")
print('')
print('<html>')
print('<head>')
print('<title>Hello</title>')
print("<meta charset=\"utf-8\">")
print('</head>')
print('<body>')
print("<b>环境变量</b><br>")
print("<ul>")
for key in os.environ.keys():
    print("<li><span style='color:green'>%30s </span> : %s </li>" % (key, os.environ[key]))
print("</ul>")
print('</body>')
print('</html>')
print('')
print('<html>')
print('<head>')
print('<title>Hello</title>')
print('</head>')
print('</html>')
