try:
    f = open('text.txt', 'r')
    print f.read()
finally:
    if f:
        f.close()

with open('text.txt', 'r') as f:
    print f.read()

with open('text.txt', 'r') as f:
    for line in f.readlines():
        print line.strip()
