f = open('text3.txt', 'w')
f.write('qwer')
f.close()

with open('text3.txt', 'w') as f:
    f.write('qwer qewr')
