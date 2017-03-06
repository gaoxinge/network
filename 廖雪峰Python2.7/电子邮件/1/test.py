#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtp_server = 'smtp.***.com'
from_addr = 'send email address'
password = 'password'
to_addr = 'receive email address'

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8')  
msg['From'] = from_addr  
msg['To'] = to_addr
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
