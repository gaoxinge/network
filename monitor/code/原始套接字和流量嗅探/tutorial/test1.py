import socket
import struct
import ctypes

host = ''

class IP(ctypes.Structure):
    _fields_ = [
        ('ihl',          ctypes.c_ubyte, 4),
        ('version',      ctypes.c_ubyte, 4),
        ('tos',          ctypes.c_ubyte),
        ('len',          ctypes.c_ushort),
        ('id',           ctypes.c_ushort),
        ('offset',       ctypes.c_ushort),
        ('ttl',          ctypes.c_ubyte),
        ('protocol_num', ctypes.c_ubyte),
        ('sum',          ctypes.c_ushort),
        ('src',          ctypes.c_ulong),
        ('dst',          ctypes.c_ulong)
        ]

    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        self.protocol_map = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}
        self.src_address = socket.inet_ntoa(struct.pack('<L', self.src))
        self.dst_address = socket.inet_ntoa(struct.pack('<L', self.dst))
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
sniffer.bind((host, 0))
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

try:
    while True:
        raw_buffer = sniffer.recvfrom(65565)[0]
        ip_header = IP(raw_buffer[0:20])
        print 'Protocol:%s %s -> %s' % (ip_header.protocol, ip_header.src_address, ip_header.dst_address)
except KeyboardInterrupt:
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
