# -*- coding: cp936 -*-
import re
import urllib2
import json
from StringIO import StringIO
import gzip


cityname = raw_input(u'你想查哪个城市的天气？\n')
url = "http://wthrcdn.etouch.cn/weather_mini?city=%s"%cityname
content = urllib2.urlopen(url).read()
buf = StringIO(content)
f = gzip.GzipFile(fileobj=buf)
data = f.read()
data = json.loads(data)
result =data['data']

print u'城市名字： '+ result['city']
print u'昨天回顾：'+result['yesterday']['type']
print u'风向: '+result['yesterday']['fx']+ ' '+ u'风力'+ result['yesterday']['fl']
print u'未来预测'
for w in result['forecast']:
    print w['date']+": "+w['type']

print u'温馨提示： '+result['ganmao']