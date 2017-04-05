import requests
import re
import random

class Download(object):
    
    def __init__(self):
        self.ips = []
        response = requests.get('http://haoip.cc/tiqu.htm')
        results = re.findall(r'r/>(.*?)<b', response.text, re.S)
        for result in results:
            t = re.sub('\n', '', result)
            self.ips.append(t.strip().__str__())
        
    def get(self, url, on=False, timeout=3, num_retries=6):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        headers = {'User-Agent': user_agent}
        
        if not on:
            try:
                response = requests.get(url, headers=headers, timeout=timeout)
            except:
                if num_retries > 0:
                    response = self.get(url, False, timeout, num_retries-1)
                else:
                    response = self.get(url, True, timeout, 1)
        else:
            try:
                ip = str(random.choice(self.ips))
                proxy = {'http': ip}
                response = requests.get(url, headers=headers, proxies=proxy, timeout=timeout)
            except:
                if num_retries > 0:
                    response = self.get(url, True, timeout, num_retries-1)
                else:
                    response = None
                    
        return response
        
if __name__ == '__main__':
    download = Download()
    response = download.get('https://www.baidu.com/', on=True)
    print 'baidu' in response.text
    response = download.get('https://www.baidu.com/')
    print 'baidu' in response.text
            
        
