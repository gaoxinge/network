try:
    fh = open('testfile', 'r')
    try:
        fh.write('qwer')
    finally:
        print 'close'
        fh.close()
except IOError:
    print 'error'

print 1
