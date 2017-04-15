import re
import requests

username = ''
email    = ''
password = ''

pattern = re.compile(r'fkey":"(.*?)\"')
response = requests.get('https://math.stackexchange.com/users/login')
result = re.findall(pattern, response.text)

data = {
    'fkey':              result[0],
    'ssrc':              '',
    'email':             email,
    'password':          password,
    'oauth_version':     '',
    'oauth_server':      '',
    'openid_username':   '',
    'openid_identifier': '',
}

response = requests.post('https://math.stackexchange.com/users/login', data=data)
print username in response.text