#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ���� CGI ����ģ�� 
import cgi, cgitb 

# ���� FieldStorage��ʵ�� 
form = cgi.FieldStorage() 

# �����ֶ�����
if form.getvalue('site'):
   site = form.getvalue('site')
else:
   site = "�ύ����Ϊ��"

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>����̳� CGI ����ʵ��</title>"
print "</head>"
print "<body>"
print "<h2> ѡ�е���վ�� %s</h2>" % site
print "</body>"
print "</html>"