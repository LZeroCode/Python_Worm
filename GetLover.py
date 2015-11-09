__author__ = 'ZeroCode'
# coding:utf-8

import SimulateLogIn
import socket

timeout = 1000
socket.setdefaulttimeout(timeout)

#访问的地址
#home_url = 'http://hkbici.com/forum-18-1.html'

#模拟登陆，抓包得到的Request地址
auth_url = 'http://hkbici.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'

# 登陆用户名和密码
data = {'fastloginfield':'*****',
        'username':'*****',
        'password':'***********',
        'quickforward':'yes',
        'handlekey':'ls'}

# 发送头信息
headers = {'Host':"hkbici.com",
           'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0'}

login = SimulateLogIn.LSimulateLogIn(auth_url, data, headers)

pagelimit = 946
for pageindex in range(0, pagelimit):
    home_url = 'http://hkbici.com/forum-18-' + str(pageindex) + '.html'
    realinformation = login.RequestContent(home_url)
    if None == realinformation:
        continue

    #获得图片的地址
    html_index = 0
    thumbnailcharacter = '<div class="c cl">'
    for i in range(0, 32):
        thumbnail_index = realinformation.find(thumbnailcharacter, html_index)
        if thumbnail_index == -1:
            continue

        href_index = realinformation.find('<a href="', thumbnail_index)
        if href_index == -1:
            continue

        html_index = realinformation.find('.html', href_index)
        if html_index == -1:
            continue

        real_html = realinformation[href_index+9 : html_index+5]
        pictureadress = 'http://hkbici.com/' + real_html
        #print(pictureadress)

        pictureinformation = login.RequestContent(pictureadress)
        if None == pictureinformation:
            continue

        #根据图片的地址找到相对应的图片
        findcharacter = '<img id="'
        jpg_index = 0
        for j in range(0, 30):
            findcharacter_index = pictureinformation.find(findcharacter, jpg_index)
            if findcharacter_index == -1:
                continue

            zoomfile_index = pictureinformation.find('zoomfile="', findcharacter_index)
            if zoomfile_index == -1:
                continue

            jpg_index = pictureinformation.find('.jpg"', zoomfile_index)
            if jpg_index == -1:
                continue

            realjpg_adr = pictureinformation[zoomfile_index+10 : jpg_index+4]
            picuture_path = 'http://hkbici.com/' + realjpg_adr
            #print(picuture_path)

            jpgbuffer = login.RequestBuffer(picuture_path)
            if None == jpgbuffer:
                continue

            try:
                filename = realjpg_adr[-26:]
                print('正在获取' + filename + '...')

                filename.replace('/', 'a', len(filename))
                file = open(filename, 'wb')
                file.write(jpgbuffer)
                file.flush()
                file.close()
            except FileNotFoundError as e:
                print("文件错误")
            except FileExistsError as e:
                print('文件已经存在')

    else:
        print(str(pageindex) + '_paget end!')
else:
    print('all end!')

input()
