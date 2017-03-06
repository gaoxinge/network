fo = open('foo.txt', 'r')
print 'name:', fo.name
print 'closed or not:', fo.closed
print 'access mode:', fo.mode
print 'sapce:', fo.softspace
fo.close()
print 'name:', fo.name
print 'closed or not:', fo.closed
print 'access mode:', fo.mode
print 'sapce:', fo.softspace
print 

fo = open('foo.txt','w')
fo.write('qwer qewrqwerqewrqwerqwe\nqwerqwerqwerqwer\nqwerqwerqwerqwerqwer\nqwerqweqwerqwer\nqwerqweeqwr')
fo.close()

fo = open('foo.txt', 'r')
str = fo.read(10)
print str
print fo.tell()
fo.seek(0,0)
str = fo.read(10)
print str
print fo.tell()
fo.close()
