#!/usr/bin/python3
import socket, sys
import signal
import multiprocessing 

def mp_server(c):    
    while True:
        try:
            sock, addr = c
            msg = sock.recv(1024)
            print("Mensaje recibido: %s" % msg.decode().upper())
            if msg == b'exit\r\n':
                print('Cerrando conexion con %s' % str(addr))
                break
        except KeyboardInterrupt:
            break
    sock.close()

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    for child in mp_eliminar:
        child.join()
    serversocket.close()
    sys.exit(0)

mp_eliminar = []


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

# Crear un socket que acepte conexiones IPv4 e IPv6
serversocket = socket.socket(socket.AF_INET6 if socket.has_ipv6 else socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = "::" if socket.has_ipv6 else "0.0.0.0"  # Escuchar en todas las interfaces
port = int(50002)

serversocket.bind((host, port))
serversocket.listen(5)

while True:
    cliente = serversocket.accept()
    clientsocket, addr = cliente
    print("Got a connection from %s" % str(addr))
    child = multiprocessing.Process(target=mp_server, args=(cliente,))
    mp_eliminar.append(child)
    child.start()
    clientsocket.close()
