import socket
import struct
import ctypes

class IP(ctypes.Structure):
    _fields_ = [
        ('ihl',          ctypes.c_ubyte, 4),
        ('version',      ctypes.c_ubyte, 4),
        ('tos',          ctypes.c_ubyte),
        ('len',          ctypes.c_ushort),
        ('id',           ctypes.c_ushort),
        ('offset1',      ctypes.c_ubyte, 4),
        ('flags',        ctypes.c_ubyte, 4),
        ('offset2',      ctypes.c_ubyte),
        ('ttl',          ctypes.c_ubyte),
        ('protocol_num', ctypes.c_ubyte),
        ('checksum',     ctypes.c_ushort),
        ('src',          ctypes.c_ulong),
        ('dst',          ctypes.c_ulong)
        ]

    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        self.offset = self.offset1 << 8 + self.offset2
        
        self.protocol_map = {1: 'ICMP', 2: 'IGMP', 6: 'TCP', 17: 'UDP'}
        try:    self.protocol = self.protocol_map[self.protocol_num]
        except: self.protocol = str(self.protocol_num)

        self.src_address = socket.inet_ntoa(struct.pack('<L', self.src))
        self.dst_address = socket.inet_ntoa(struct.pack('<L', self.dst))

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind((socket.gethostbyname_ex(socket.gethostname())[2][0], 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    try:
        while True:
            raw_buffer = s.recvfrom(65565)[0]
            ip_header = IP(raw_buffer[0:20])
            print 'version: %d, ihl: %d, tos: %d, total length: %d, identification: %d, flags: %d, offset: %d, time to live: %d, protocol: %s, checksum: %d, source address: %s, destination address: %s'\
            % (ip_header.version, ip_header.ihl, ip_header.tos, ip_header.len, ip_header.id, ip_header.flags,
               ip_header.offset, ip_header.ttl, ip_header.protocol, ip_header.checksum, ip_header.src_address, ip_header.dst_address)
            print
    except KeyboardInterrupt:
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
