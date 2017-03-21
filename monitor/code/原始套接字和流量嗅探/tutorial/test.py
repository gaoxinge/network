import socket

host = ''
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
sniffer.bind((host, 0))
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
print sniffer.recvfrom(65565)
sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
