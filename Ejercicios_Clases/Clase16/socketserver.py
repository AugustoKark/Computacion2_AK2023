# #!/usr/bin/python3
# ## EJERCICIOS ##
# # 1 - Realizar un programa que implemente un servido TCP o UDP usando socketserver.
# # El servidor puede ser un servidor de mayúsculas, un codificador en rot13 o cualquier otra tarea simple.
# # Se debe implementar concurrencia usanfo forking o threading.

# # ROT13

# # A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# # N O P Q R S T U V W X Y Z A B C D E F G H I J K L M

# # gato (claro)->(rot13) tngb



# #!/usr/bin/python3
# import socket
# import signal
# import threading
# import sys
# import socketserver

# def encrypt_rot13(sock, addr):
#     while True:
#         try:
#             msg = sock.recv(1024)
#             encrypted_text = ""
#             text= msg.decode()
#             if msg == b'exit\r\n':
#                 print('Cerrando conexión con %s' % str(addr))
#                 break
#             for char in text:
#                 if char.isalpha():
#                     if char.islower():
#                         encrypted_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
#                     else:
#                         encrypted_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
#                     encrypted_text += encrypted_char
#                 else:
#                     encrypted_text += char
                
#             sock.send(("Mensaje en Rot13: " + encrypted_text).encode())
#             print(encrypted_text)
            

#             # print("Mensaje recibido: %s" % (msg.decode().upper()))
#             # print(msg)
#         except KeyboardInterrupt:
#             break
#     sock.close()

# def signal_handler(sig, frame):
#     print('Se presionó Ctrl+C. Cerrando el servidor...')

#     for thread in hilo_eliminar:
#         thread.join()
#     serversocket.close()
#     sys.exit(0)

# hilo_eliminar = []
# signal.signal(signal.SIGINT, signal_handler)
# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# host = "127.0.0.1"
# port = int(50002)

# serversocket.bind((host, port))
# serversocket.listen(5)

# while True:
#         cliente = serversocket.accept()
#         clientsocket, addr = cliente
#         print("Conexión entrante desde %s" % str(addr))
#         thread = threading.Thread(target=encrypt_rot13, args=(clientsocket, addr))
#         hilo_eliminar.append(thread)
#         thread.start()
    
