import json

d = dict(name = 'Bob', age = 20, score = 88)
print json.dumps(d)

f = open('json.txt', 'wb')
json.dump(d, f)
f.close()
