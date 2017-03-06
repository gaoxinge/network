import os

a = os.path.abspath('.')
b = os.path.join(a, 'text2.py')
c = os.path.split(b)
d = os.path.splitext(b)
print a
print b
print c
print d

os.mkdir('1')
os.rmdir('1')

f = file('text.txt', 'w')
f.close()
os.rename('text.txt', 'text.py')
os.remove('text.py')
