__author__ = 'Zero'
#-*- coding:utf-8 -*-
import ftplib
import sys

print (sys.getdefaultencoding())
print(sys.getfilesystemencoding())

lftp = ftplib.FTP('192.168.168.92')
#很重要 不然获取的中文路径或文件名是乱码
lftp.encoding = 'utf-8'

lftp.login()
contentList = lftp.nlst()
for item in contentList:
    print(item)


#from ftplib import FTP
#
#encode=['UTF-8','gbk','GB2312','GB18030','Big5','HZ']
#def logFTP(code):
#    ftp=FTP('192.168.168.92')
#    try:
#        ftp.login()
#        ftp.encoding=code
#        lst=ftp.nlst()
#        for s in lst:
#            print(s)
#    except(UnicodeDecodeError):
#        pass
#    finally:
#        print(code)
#        t=input('Is this?:')
#        ftp.quit()
#
#for enc in encode:
#    logFTP(enc)
