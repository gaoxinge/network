import socket
import select
import Queue

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 8888))
s.listen(5)

rlists = [s]
wlists = []
msg_que = {}
timeout = 10

while True:
    rs, ws, es = select.select(rlists, wlists, rlists, timeout)
    
    if not (rs or ws or es):
        print 'timeout...'
        continue
        
    for r in rs:
        if r is s:
            conn, addr = r.accept()
            print 'connect by', addr
            conn.setblocking(False)
            rlists.append(conn)
            msg_que[conn] = Queue.Queue()
        else:
            data = r.recv(1024)
            if data:
                print data
                msg_que[r].put(data)
                if r not in wlists:
                    wlists.append(r)
            else:
                if r in wlists:
                    wlists.remove(r)
                rlists.remove(r)
                r.close()
                del msg_que[r]
                
    for r in ws:
        try:
            msg = msg_que[r].get_nowait()
        except Queue.Empty:
            print 'msg empty'
            wlists.remove(r)
        else:
            r.send(msg)
            
    for r in es:
        print 'except', s.getpeername()
        if r in rlists:
            rlists.remove(r)
        if r in wlists:
            wlists.remove(r)
        r.close()
        del msg_que[r]
        
        