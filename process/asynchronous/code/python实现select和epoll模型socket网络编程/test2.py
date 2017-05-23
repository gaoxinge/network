import select
import socket
import Queue
import time
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 9999))
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setblocking(False)
server.listen(10)

inputs = [server]
outputs = []
message_queues = {}

while inputs:
    print 'waiting for next event'
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    
    if not (readable or writable or exceptional):
        print 'Time out !'
        break
        
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            print 'connection from', client_address
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = Queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                print 'received', data, 'from', s.getpeername()
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                print 'closing', client_address
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]
                
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except Queue.Empty:
            print '', s.getpeername, 'queue empty'
            outputs.remove(s)
        else:
            print 'sending', next_msg, 'to', s.getpeername()
            os.popen('sleep 5').read()
            s.send(next_msg)
            
    for s in exceptional:
        print 'exception condition on', s.getpeername()
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]