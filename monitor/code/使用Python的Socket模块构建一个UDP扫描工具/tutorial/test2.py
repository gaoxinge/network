import netaddr

ip = ''
if ip in netaddr.IPNetwork('/24'):
    print 'OK!'
