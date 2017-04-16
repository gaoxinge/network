import requests

response = requests.get('https://raw.githubusercontent.com/im-iron-man/python/master/im2text/1.png')
with open('1.png', 'wb') as f:
    f.write(response.content)
    
response = requests.get('https://raw.githubusercontent.com/im-iron-man/python/master/im2text/1.png', stream=True)
with open('2.png', 'wb') as f:
    for _ in response.iter_content(chunk_size=1024):
        if _:
            f.write(_)