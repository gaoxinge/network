#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ����ģ��
import os
import Cookie

print "Content-type: text/html"
print

print """
<html>
<head>
<meta charset="utf-8">
<title>����̳�(runoob.com)</title>
</head>
<body>
<h1>��ȡcookie��Ϣ</h1>
"""

if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    c=Cookie.SimpleCookie()
    c.load(cookie_string)

    try:
        data=c['name'].value
        print "cookie data: "+data+"<br>"
    except KeyError:
        print "cookie û�����û����ѹ�ȥ<br>"
print """
</body>
</html>

"""