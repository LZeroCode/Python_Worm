__author__ = 'Zero'

import  smtplib
from email.mime.text import MIMEText
lsmtp = smtplib.SMTP('smtp.163.com')

try:
    lsmtp.login('**********@163.com', '**********')
except( smtplib.SMTPHeloError, smtplib.SMTPAuthenticationError, smtplib.SMTPException):
    print('Erro')

content = 'testttt'
msg = MIMEText('<html><h1>你好</h1></html>','html','utf-8')
msg['Subject'] = content
lsmtp.sendmail('***********@163.com', '*********@qq.com', str(msg))
lsmtp.quit()

