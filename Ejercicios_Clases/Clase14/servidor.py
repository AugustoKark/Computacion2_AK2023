## EJERCICIO ##

# Escribir un programa que implemente un socket pasivo que gestione de forma serializada distintas conecciones entrantes.

# Debe atender nuevas conexiones de forma indefinida.

# NOTA: cuando decimos serializado decimo que atiende una conexión y recibe una nueva conección una vez que esa conexión se cerró

import socket
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 50010))
s.listen(2)  # Lo hace pasivo y le dice que solo puede tener 2 conexiones

print('Esperando conexiones...')
while True:
    ready_sockets, _, _ = select.select([s], [], [], 15)

    if ready_sockets:
        conn, address = s.accept()
        print(f"Cliente conectado desde {address}")

        while True:
            data = conn.recv(1024)
            print(data.decode('utf-8'))
            if data.decode('utf-8') == 'bye':
                conn.close()
                break

        print("Cerrando la conexión con el cliente.")
    else:
        print("Tiempo de espera agotado, cerrando el servidor.")
        break

s.close()


