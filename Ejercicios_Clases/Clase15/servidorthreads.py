#!/usr/bin/python3
import socket
import signal
import threading
import sys

def mp_server(sock, addr):
    while True:
        try:
            msg = sock.recv(1024)
            print("Mensaje recibido: %s" % (msg.decode().upper()))
            # print(msg)
            if msg == b'exit\r\n':
                print('Cerrando conexión con %s' % str(addr))
                break
        except KeyboardInterrupt:
            break
    sock.close()

def signal_handler(sig, frame):
    print('Se presionó Ctrl+C. Cerrando el servidor...')

    for thread in hilo_eliminar:
        thread.join()
    serversocket.close()
    sys.exit(0)

hilo_eliminar = []
signal.signal(signal.SIGINT, signal_handler)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = "127.0.0.1"
port = int(50002)

serversocket.bind((host, port))
serversocket.listen(5)

while True:
        cliente = serversocket.accept()
        clientsocket, addr = cliente
        print("Conexión entrante desde %s" % str(addr))
        thread = threading.Thread(target=mp_server, args=(clientsocket, addr))
        hilo_eliminar.append(thread)
        thread.start()
    
