#!/usr/bin/python
# -*- coding: UTF-8 -*-

# HTTP ͷ��
print "Content-Disposition: attachment; filename=\"foo.txt\"";
print
# ���ļ�
fo = open("foo.txt", "rb")

str = fo.read();
print str

# �ر��ļ�
fo.close()