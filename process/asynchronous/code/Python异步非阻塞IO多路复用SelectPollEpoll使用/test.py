import select
import socket
import Queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 8080))
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setblocking(0)
server.listen(10)

inputs = [server]
outputs = []
message_queues = {}
timeout = 20

while True:
    readable, writable, exceptional = select.select(inputs, outputs, inputs, timeout)
    
    if not (readable or writable or exceptional):
        continue
        
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = Queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                print 'receive', data, 'from', s.getpeername()
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                print 'close', client_address
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]
    
    for s in writable:
        try:
            msg = message_queues[s].get_nowait()
        except Queue.Empty:
            print 'connection', s.getpeername()
            outputs.remove(s)
        else:
            print 'send', msg, 'to', s.getpeername()
            s.send(msg)
    
    for s in exceptional:
        print 'except', s.getpeername()
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]