import itertools

for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
    print x

r = map(lambda x: x * x, [1, 2, 3])
print r

r = itertools.imap(lambda x: x * x, [1, 2, 3])
print r

r = itertools.imap(lambda x: x*x, itertools.count(1))
for n in itertools.takewhile(lambda x: x < 100, r):
    print n

r = map(lambda x: x * x, itertools.count(1))
