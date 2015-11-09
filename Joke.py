__author__ = 'ZeroCode'

import urllib.request
import re

def GetJoke():
    data = urllib.request.urlopen("http://neihanshequ.com/")
    content = data.read().decode()
    print(content)
    JokePattern = re.compile("<h1 class=\"title\">\s*<p>.*</p>\s*</h1>")
    JokeList = JokePattern.findall(content)
    for it in JokeList:
        subPattern = re.compile(r'<h1 class="title">\s*<p>|</p>\s*</h1>')
        print(subPattern.sub('', it))

if '__main__' == __name__:
    GetJoke()