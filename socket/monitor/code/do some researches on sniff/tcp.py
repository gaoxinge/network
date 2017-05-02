import socket
import ctypes
from ip import IP

class TCP(ctypes.Structure):
    _fields_ = [
        ('src_port',       ctypes.c_ushort),
        ('dst_port',       ctypes.c_ushort),
        ('sequence',       ctypes.c_ulong),
        ('acknowledgment', ctypes.c_ulong),
        ('reserved1',      ctypes.c_ubyte, 4),
        ('offset',         ctypes.c_ubyte, 4),
        ('control',        ctypes.c_ubyte, 6),
        ('reserved2',      ctypes.c_ubyte, 2),
        ('window',         ctypes.c_ushort),
        ('checksum',       ctypes.c_ushort),
        ('urgent_pointer', ctypes.c_ushort)
        ]

    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        self.reserved = self.reserved1 << 4 + self.reserved2
        
        self.urg = (self.control & 0b100000) >> 5
        self.ack = (self.control & 0b010000) >> 4
        self.psh = (self.control & 0b001000) >> 3
        self.rst = (self.control & 0b000100) >> 2
        self.syn = (self.control & 0b000010) >> 1
        self.fin = (self.control & 0b000001) >> 0

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind((socket.gethostbyname_ex(socket.gethostname())[2][0], 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    
    try:
        while True:
            raw_buffer = s.recvfrom(65565)[0]
            ip_header = IP(raw_buffer[0:20])
            if ip_header.protocol == 'TCP':
                offset = ip_header.ihl * 4
                tcp_header = TCP(raw_buffer[offset:offset + 20])
                print 'source port: %d, destination port: %d, sequence number: %d, acknowledgment number: %d, data offset: %d, reserved: %d, urgent: %d, acknowledgment: %d, push: %d, reset: %d, synchronization: %d, finish: %d, window: %d, checksum: %d, urgent pointer: %d'\
                % (tcp_header.src_port, tcp_header.dst_port, tcp_header.sequence, tcp_header.acknowledgment, tcp_header.offset, tcp_header.reserved,
                   tcp_header.urg, tcp_header.ack, tcp_header.psh, tcp_header.rst, tcp_header.syn, tcp_header.fin,
                   tcp_header.window, tcp_header.checksum, tcp_header.urgent_pointer)
                offset = offset + tcp_header.offset * 4
                data = raw_buffer[offset:]
                if data: print repr(data)
                print
    except KeyboardInterrupt:
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
