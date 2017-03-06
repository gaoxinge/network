#coding=utf-8  
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  

smtp = smtplib.SMTP()  
smtp.connect('smtp.***.com')  
smtp.login('username', 'password') 
 
msg = MIMEText('大家关好窗户', 'plain', 'utf-8')
msg['Subject'] = Header('放假通知', 'utf-8')  
msg['From'] = 'send email address'    
msg['To'] = 'receive email address'
smtp.sendmail('send email address', 'receive email address', msg.as_string())

smtp.quit()  