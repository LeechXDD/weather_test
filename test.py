# -*- coding: cp936 -*-
import re
import urllib2
import json
from StringIO import StringIO
import gzip


cityname = raw_input(u'������ĸ����е�������\n')
url = "http://wthrcdn.etouch.cn/weather_mini?city=%s"%cityname
content = urllib2.urlopen(url).read()
buf = StringIO(content)
f = gzip.GzipFile(fileobj=buf)
data = f.read()
data = json.loads(data)
result =data['data']

print u'�������֣� '+ result['city']
print u'����عˣ�'+result['yesterday']['type']
print u'����: '+result['yesterday']['fx']+ ' '+ u'����'+ result['yesterday']['fl']
print u'δ��Ԥ��'
for w in result['forecast']:
    print w['date']+": "+w['type']

print u'��ܰ��ʾ�� '+result['ganmao']