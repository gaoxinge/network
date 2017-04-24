from tornado import httputil

h = httputil.HTTPHeaders({'content-type': 'text/html'})
print h
print list(h.keys())
print h['Content-Type']
h.add('Set-Cookie', 'A=B')
h.add('Set-Cookie', 'C=D')
print h
print list(h.keys())
print h['set-cookie']
print h.get_list('set-cookie')
for k, v in h.get_all():
    print '%s: %s' % (k, v)