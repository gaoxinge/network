import struct

print struct.pack('>I', 10240099)
print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')

f = open('test.bmp', 'rb')
s = f.read(30)
print struct.unpack('<ccIIIIIIHH', s)
