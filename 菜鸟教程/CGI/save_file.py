#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# ��ȡ�ļ���
fileitem = form['filename']

# ����ļ��Ƿ��ϴ�
if fileitem.filename:
   # �����ļ�·�� 
   fn = os.path.basename(fileitem.filename)
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())

   message = '�ļ� "' + fn + '" �ϴ��ɹ�'
   
else:
   message = '�ļ�û���ϴ�'
   
print """\
Content-Type: text/html\n
<html>
<head>
<meta charset="utf-8">
<title>����̳�(runoob.com)</title>
</head>
<body>
   <p>%s</p>
</body>
</html>
""" % (message,)