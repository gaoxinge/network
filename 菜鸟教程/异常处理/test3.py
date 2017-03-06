def mye(level):
    if level < 1:
        raise Exception('Invalid level!', level)

try:
    mye(0)
except 'Invalid level!':
    print 1
else:
    print 2
