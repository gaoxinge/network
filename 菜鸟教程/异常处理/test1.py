try:
    fh = open('testfile', 'r')
    fh.write('qwer')
finally:
    print 'error'

print 1
