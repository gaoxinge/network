import socket
import os
import signal
import time, threading
def SendDataToServer(sock):
    while True:
        put = str(raw_input())
        sock.send(put)

def ReceiveData(sock):
    while True:
        try:
            data = sock.recv(1024)
            time.sleep(1)
        except:
            print "Server Down!"
            os._exit(0)
        else:
            if data:
                print "RECEIVE:",data

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 8008))
    send_tick = threading.Thread(target=SendDataToServer, args=(s,))
    rec_tick = threading.Thread(target=ReceiveData, args=(s,))
    send_tick.start()
    rec_tick.start()