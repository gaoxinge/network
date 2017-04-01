from cgi import parse_qs, escape

QUERY_STRING = 'age=10&hobbies=software&hobbies=tunning'
d = parse_qs(QUERY_STRING)
print d.get('age', [''])[0]
print d.get('hobbies', [])
print d.get('name', ['unkown'])
print 10 * '*'
print escape('<script>alert(123);</script>')