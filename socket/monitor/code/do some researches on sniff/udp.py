import socket
import ctypes
from ip import IP

class UDP(ctypes.Structure):
    _fields_ = [
        ('src_port', ctypes.c_ushort),
        ('dst_port', ctypes.c_ushort),
        ('offset',   ctypes.c_ushort),
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
            if ip_header.protocol == 'UDP':
                offset = ip_header.ihl * 4
                udp_header = UDP(raw_buffer[offset:offset + 8])
                print 'source port: %d, destination port: %d, data offset: %d, checksum: %d'\
                % (udp_header.src_port, udp_header.dst_port, udp_header.offset, udp_header.checksum)
                offset = offset + udp_header.offset * 4
                data = raw_buffer[offset:]
                if data: print repr(data)
                print
    except KeyboardInterrupt:
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
