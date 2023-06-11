# Ejercicios

# 1 - Escribir un programa que genere dos hilos utilizando threading.
# Uno de los hilos debera leer desde stdin el texto ingresado por el usuario y deberá escribirlo en una cola de mensajes (queue).
# El segundo hilo deberá leer desde la queue el contenido y encriptará dicho texto utilizando el algoritmo ROT13 y lo almacenará en una cola de mensajes (queue).
# El primer hilo deberá leer dicho mensaje de la cola y lo mostrará por pantalla.

# ROT13

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# N O P Q R S T U V W X Y Z A B C D E F G H I J K L M

# gato (claro)->(rot13) tngb

import threading
import queue
import sys
import time

def encrypt_rot13():
    text= q1.get()
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
            
    q2.put(encrypted_text)

def leer():
        texto = input("Ingrese un texto: ")
        q1.put(texto)

t1= threading.Thread(target=leer)

q1= queue.Queue()
q2= queue.Queue()
t1.start()
t1.join()
encrypt_rot13()
time.sleep(1)

print(q2.get())





