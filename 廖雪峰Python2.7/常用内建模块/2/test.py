import base64

print base64.b64encode('binary\x00string')
print base64.b64decode('YmluYXJ5AHN0cmluZw==')

print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.b64decode('abcd++//')

print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64decode('abcd--__')
