#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ���� CGI ����ģ�� 
import cgi, cgitb 

# ���� FieldStorage��ʵ�� 
form = cgi.FieldStorage() 

# �����ֶ�����
if form.getvalue('dropdown'):
   dropdown_value = form.getvalue('dropdown')
else:
   dropdown_value = "û������"

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>����̳� CGI ����ʵ��</title>"
print "</head>"
print "<body>"
print "<h2> ѡ�е�ѡ���ǣ�%s</h2>" % dropdown_value
print "</body>"
print "</html>"