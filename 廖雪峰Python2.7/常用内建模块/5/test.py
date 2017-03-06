import itertools

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
    print n

cs = itertools.cycle('ABC')
#for c in cs:
#    print c

ns = itertools.repeat('A', 10)
for n in ns:
    print n
