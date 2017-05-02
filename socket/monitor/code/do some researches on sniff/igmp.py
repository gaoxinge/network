import socket
import struct
import ctypes
from ip import IP

class IGMP(ctypes.Structure):
    _fields_ = [
        ('type',          ctypes.c_ubyte, 4),
        ('version',       ctypes.c_ubyte, 4),
        ('unused',        ctypes.c_ubyte),
        ('checksum',      ctypes.c_ushort),
        ('group_address', ctypes.c_ulong)
        ]

    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        self.group_address = socket.inet_ntoa(struct.pack('<L', self.group_address))

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind((socket.gethostbyname_ex(socket.gethostname())[2][0], 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    try:
        while True:
            raw_buffer = s.recvfrom(65565)[0]
            ip_header = IP(raw_buffer[0:20])
            if ip_header.protocol == 'IGMP':
                offset = ip_header.ihl * 4
                igmp_header = ICMP(raw_buffer[offset:offset + 9])
                print 'version: %d, type: %d, unused: %d, checksum: %d, group_address: %s'\
                % (igmp_header.version, igmp_header.type, igmp_header.unused, igmp_header.checksum, igmp_header.group_address)
                print
    except KeyboardInterrupt:
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
