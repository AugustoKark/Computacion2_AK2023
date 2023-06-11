# Ejercicio

# 1 - Escribir un programa que reciba un mensaje desde otro proceso usando fifo (pipes con nombre). 
# El proceso receptor deberá lanzar tantos hilos como líneas tenga el mensaje y deberá enviar cada línea a los hilos secundarios. 
# Cada hilo secundario deberá calcular la cantidad de caracteres de su línea y COMPROBAR la cuenta de la línea anterior.

import threading
import multiprocessing
import os


pipe1, pipe2 = multiprocessing.Pipe()



def emisor():
    mensaje= "Hola mundo\nsi River gana la copa\nme tatuo el escudo"
    pipe1.send(mensaje)


def receptor():
    # print("El PID del proceso es: ", os.getpid())
    mensaje= pipe2.recv()
    # print(mensaje)
    lineas= mensaje.split("\n")
    for linea in lineas:
        hilo= threading.Thread(target=contar, args=(linea,))
        hilo.start()
        hilo.join()

def contar(linea):
    print("La linea es: ", linea)
    print("La cantidad de caracteres es: ", len(linea))
    # print("El PID del hilo es: ", os.getpid())
    # print("El PID del padre es: ", os.getppid())
    # print("El nombre del hilo es: ", threading.current_thread().name)

p1= multiprocessing.Process(target=emisor())
p1.start()
p1.join()
receptor()

   
