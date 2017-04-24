from tornado import template

t = template.Template('<html>{{ myvalue }}</html>')
print t.generate(myvalue='XXX')
