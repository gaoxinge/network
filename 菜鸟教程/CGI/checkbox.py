#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ���� CGI ����ģ�� 
import cgi, cgitb 

# ���� FieldStorage��ʵ�� 
form = cgi.FieldStorage() 

# �����ֶ�����
if form.getvalue('google'):
   google_flag = "��"
else:
   google_flag = "��"

if form.getvalue('runoob'):
   runoob_flag = "��"
else:
   runoob_flag = "��"

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>����̳� CGI ����ʵ��</title>"
print "</head>"
print "<body>"
print "<h2> ����̳��Ƿ�ѡ���� : %s</h2>" % runoob_flag
print "<h2> Google �Ƿ�ѡ���� : %s</h2>" % google_flag
print "</body>"
print "</html>"