try:
    fh = open('testfile', 'r')
    fh.write('qwer')
except IOError, RuntimeError:
    print 'error'
else:
    print 'success'
    fh.close()
    

def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print 'not int', Argument

temp_convert('qwer')

try:
    fh = open('testfile', 'r')
except:
    pass
else:
    print 'success'
    fh.close()
