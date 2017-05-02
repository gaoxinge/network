import socket

class PromiscuousSocket(object):
    def __init__(self):
        HOST = socket.gethostbyname(socket.gethostname())
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, 0))
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        self.s = s

    def __enter__(self):
        return self.s

    def __exit__(self, *args, **kwargs):
        self.s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

def printPacket(package, showPort, showRawData):
    dataIndex = 0
    headerIndex = 1
    ipAddressIndex = 0
    portIndex = 1

    print('IP:', package[headerIndex][ipAddressIndex])
    if(showPort):
        print('Port:', package[headerIndex][portIndex])
    if(showRawData):
        print('Data:', package[dataIndex])

    print

def sniffer(count, bufferSize = 65565, showPort = False, showRawData = False):
    with PromiscuousSocket() as s:
        for i in range(count):
            package = s.recvfrom(bufferSize)
            printPacket(package, showPort, showRawData)

sniffer(count = 10, showPort = True, showRawData = True)

