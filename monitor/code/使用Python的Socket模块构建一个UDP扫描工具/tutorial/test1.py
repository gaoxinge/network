import socket
import struct
import ctypes

host = ''

class ICMP(ctypes.Structure):
    _fields_ = [
        ('type',         ctypes.c_ubyte),
        ('code',         ctypes.c_ubyte),
        ('checksum',     ctypes.c_ushort)
        ]

    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        pass

def main():
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sniffer.bind((host, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        
    while 1:
        raw_buffer = sniffer.recvfrom(65565)[0]

        ip_header = struct.unpack('!BBHHHBBH4s4s', raw_buffer[0:20])
        version_length = ip_header[0]
        version = version_length >> 4
        length = version_length & 0xF
        ttl = ip_header[5]
        protocol = ip_header[6]
        source_addr = socket.inet_ntoa(ip_header[8])
        destination_addr = socket.inet_ntoa(ip_header[9])
        print 'IP -> Version:' + str(version) + ', Header Length:' + str(length) + \
              ', TTL:' + str(ttl) + ', Protocol:' + str(protocol) + \
              ', Source:' + str(source_addr) + ', Destination:' + str(destination_addr)

        ip_length = length * 4
        icmp_header = ICMP(raw_buffer[ip_length:ip_length + 4])
        print 'ICMP -> Type:' + str(icmp_header.type) + ', Code:' + str(icmp_header.code) + '\n'

main()
