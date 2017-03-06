import codecs

f = open('text2.txt', 'rb')
print f.read().decode('gbk')
f.close()


with codecs.open('text2.txt', 'r', 'gbk') as f:
    print f.read()
    
