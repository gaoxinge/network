import socket
import ctypes
from ip import IP

class ICMP(ctypes.Structure):
    _fields_ = [
        ('type',     ctypes.c_ubyte),
        ('code',     ctypes.c_ubyte),
        ('checksum', ctypes.c_ushort)
        ]

    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        pass

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind((socket.gethostbyname_ex(socket.gethostname())[2][0], 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    try:
        while True:
            raw_buffer = s.recvfrom(65565)[0]
            ip_header = IP(raw_buffer[0:20])
            if ip_header.protocol == 'ICMP':
                offset = ip_header.ihl * 4
                icmp_header = ICMP(raw_buffer[offset:offset + 4])
                print 'type: %d, code: %d, checksum: %d'\
                % (icmp_header.type, icmp_header.code, icmp_header.checksum)
                print
    except KeyboardInterrupt:
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
