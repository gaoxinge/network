import threading
import socket
import struct
import ctypes
from netaddr import IPNetwork, IPAddress

host = ''
subnet = '/24'
message = 'hello'

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

def udp_sender(subnet, message):
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for ip in IPNetwork(subnet):
        try:
            sender.sendto(message, ('%s' % ip, 65212))
        except:
            pass

def main():
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sniffer.bind((host, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    
    t = threading.Thread(target = udp_sender, args = (subnet, message))
    t.start()

    while 1:
        raw_buffer = sniffer.recvfrom(65565)[0]

        ip_header = struct.unpack('!BBHHHBBH4s4s', raw_buffer[0:20])
        version_length = ip_header[0]
        length = version_length & 0xF
        source_addr = socket.inet_ntoa(ip_header[8])
        
        ip_length = length * 4 
        icmp_header = ICMP(raw_buffer[ip_length:ip_length + 4])
        if icmp_header.code == 3 and icmp_header.type == 3 and IPAddress(source_addr) in IPNetwork(subnet) and raw_buffer[len(raw_buffer) - len(message):] == message:
            print 'host up:' + str(source_addr)

main()
