import re
import requests

pattern = re.compile(r'cid=(.*?)&')
response = requests.get('http://www.bilibili.com/video/av7388172/')
result = re.findall(pattern, response.text)

pattern = re.compile(r'<d .*?>(.*?)<')
response = requests.get('http://comment.bilibili.com/%s.xml' % result[0])
results = re.findall(pattern, response.text)

for _ in results:
    print _

