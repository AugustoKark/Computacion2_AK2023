import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 50010))
s.listen(2)  # Lo hace pasivo y le dice que solo puede tener 2 conexiones
s.settimeout(30)  

print('Esperando conexiones...')
try:
    while True:
        conn, address = s.accept()
        print(f"Cliente conectado desde {address}")
        try:
            while True:
                data = conn.recv(1024)
                print(data.decode('utf-8'))
                if data.decode('utf-8') == 'bye':
                    conn.close()
                    break
            
        finally:
            print("Cerrando la conexión con el cliente.")
except socket.timeout:
    print("Tiempo de espera agotado, cerrando el servidor.")
finally:
    s.close()
