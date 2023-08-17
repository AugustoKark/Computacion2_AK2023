import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50010))

s.sendall(b'Coneccion establecida')
while True:
    data = input('Ingrese un mensaje: ')
    s.sendall(data.encode('utf-8'))

    if str(data) == 'bye':
        break

s.close()
