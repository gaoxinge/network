#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ���� CGI ����ģ�� 
import cgi, cgitb 

# ���� FieldStorage��ʵ�� 
form = cgi.FieldStorage() 

# �����ֶ�����
if form.getvalue('textcontent'):
   text_content = form.getvalue('textcontent')
else:
   text_content = "û������"

print "Content-type:text/html"
print
print "<html>"
print "<head>";
print "<meta charset=\"utf-8\">"
print "<title>����̳� CGI ����ʵ��</title>"
print "</head>"
print "<body>"
print "<h2> ����������ǣ�%s</h2>" % text_content
print "</body>"
print "</html>"