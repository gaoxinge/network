import json

# python object to json
data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
text = json.dumps(data)
print text

# json to python object
data = json.loads(text)
for key, value in data[0].items():
    print key, value