__author__ = 'ZeroCode'

from http.cookiejar import CookieJar
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor
from urllib.request import build_opener
from urllib.request import Request
import urllib.error


class LSimulateLogIn:
    "模拟登陆类"
    def __init__(self, request_url, login_data, headers):
        self.request_url = request_url  #通过抓包得到的请求地址
        self.login_data = login_data
        self.headers = headers

        post_data = urlencode(self.login_data).encode()
        cookies = CookieJar() #初始化一个CookieJar来处理Cookie

        #实例化一个全局的opener
        self.opener = build_opener(HTTPCookieProcessor(cookies))
        req = Request(self.request_url, post_data, self.headers)
        self.opener.open(req)

    def RequestContent(self, access_url):
        "访问access_url地址，获取html信息"
        try:
            result = self.opener.open(access_url)
        except urllib.error.HTTPError as e:
            print('错误码' + str(e.code))
            return None
        except urllib.error.URLError as e:
            print('请求错误' + e.reason)
            return None

        try:
            content = result.read().decode()
        except IOError as e:
            print('读写异常')
            return None
        except Exception as e:
            print('其他异常')
            return None

        return content

    def RequestBuffer(self, access_url):
        "访问access_url地址，获取二进制数据"
        try:
            result = self.opener.open(access_url)
        except urllib.error.HTTPError as e:
            print('错误码' + str(e.code))
            return None
        except urllib.error.URLError as e:
            print('请求错误' + e.reason)
            return None

        try:
            buffer = result.read()
        except IOError as e:
            print('读写异常')
            return None
        except Exception as e:
            print('其他异常')
            return None

        return buffer



if __name__ == '__main__':
    auth_url = 'http://hkbici.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'

    # 登陆用户名和密码
    data = {'fastloginfield':'*****',
            'username':'*****',
            'password':'******',
            'quickforward':'yes',
            'handlekey':'ls'}

    # 发送头信息
    headers = {'Host':"hkbici.com",
           'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0'}

    login = LSimulateLogIn(auth_url, data, headers)
    content = login.RequestContent('http://hkbici.com/forum-18-1.html')

    print(content)