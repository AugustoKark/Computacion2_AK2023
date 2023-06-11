'''FIFOS

1- Escribir un programa que realice la multiplicación de dos matrices de 2x2. 
Cada elemento deberá calcularse en un proceso distinto devolviendo el resultado en una fifo indicando el indice del elemento. 
El padre deberá leer en la fifo y mostrar el resultado final.
'''

# import os
# import time


# def hijo(matriz1, matriz2, fila, columna, pipe):
#     print('Mi índice es', fila, columna)
#     # print('Mi matriz1 es', matriz1)
#     # print('Mi matriz2 es', matriz2)
#     resultado = matriz1[fila][0] * matriz2[0][columna] + matriz1[fila][1] * matriz2[1][columna]
#     print('Mi resultado es', resultado)
    
#     pipeout = os.open(pipe, os.O_WRONLY)
#     os.write(pipeout, str((fila,columna,resultado)).encode())  # Se debe codificar el resultado antes de escribirlo en el pipe
#     os.close(pipeout)  # Cerrar el descriptor de archivo

# def padre(pipe):
#     resultado = [[0, 0], [0, 0]]  # Inicializar matriz resultado
    
#     for i in range(2):
#         for j in range(2):
            
#             pipein = os.open(pipe, os.O_RDONLY)
#             valor = os.read(pipein, 100)
#             os.close(pipein)
#             valor = int(valor.decode())
#             resultado[i][j] = valor
    
    
   
    
#     print('Resultado:')
#     for fila in resultado:
#         print(fila)

# matriz1 = [[1, 2], [3, 4]]
# matriz2 = [[5, 6], [7, 8]]

# pipe = "/tmp/pfifo"
# if not os.path.exists(pipe):
#     os.mkfifo(pipe)

# rt = os.fork()
# if rt == 0:
#     hijo(matriz1, matriz2, 0, 0, pipe)
#     #exit()
# else:
#     rt = os.fork()
#     if rt == 0:
#         hijo(matriz1, matriz2, 0, 1, pipe)
#         #exit()
#     else:
#         rt = os.fork()
#         if rt == 0:
#             hijo(matriz1, matriz2, 1, 0, pipe)
#             #exit()
#         else:
#             rt = os.fork()
#             if rt == 0:
#                 hijo(matriz1, matriz2, 1, 1, pipe)
#                 #exit()
#             else:
#                 time.sleep(1)
#                 padre(pipe)
#                 #exit()

    
# import os
# import time


# def hijo(matriz1, matriz2, fila, columna):
#     print('Mi índice es', fila, columna)
#     resultado = matriz1[fila][0] * matriz2[0][columna] + matriz1[fila][1] * matriz2[1][columna]
#     print('Mi resultado es', resultado)

#     pipeout = os.open(pipe, os.O_WRONLY)
#     os.write(pipeout, str((fila)).encode())
#     os.write(pipeout, str((columna)).encode())
#     os.write(pipeout, str((resultado)).encode())
#     os.close(pipeout)


    

# def padre():
#     resultado = [[0, 0], [0, 0]]  # Inicializar matriz resultado
    
#     for i in range(2):
#         for j in range(2):
#             pipein = os.open(pipe, os.O_RDONLY)
#             valor = os.read(pipein, 100)
#             os.close(pipein)
#             valor = eval(valor.decode())
#             fila, columna, resultado_hijo = eval(valor)
#             resultado[fila][columna] = resultado_hijo
    
#     print('Resultado:')
#     for fila in resultado:
#         print(fila)

# matriz1 = [[1, 2], [3, 4]]
# matriz2 = [[5, 6], [7, 8]]

# pipe = "/tmp/pfifo"
# if not os.path.exists(pipe):
#     os.mkfifo(pipe)

# rt = os.fork()
# if rt == 0:
#     hijo(matriz1, matriz2, 0, 0)
#     #exit()
# else:
#     rt = os.fork()
#     if rt == 0:
#         hijo(matriz1, matriz2, 0, 1)
#         #exit()
#     else:
#         rt = os.fork()
#         if rt == 0:
#             hijo(matriz1, matriz2, 1, 0)
#             #exit()
#         else:
#             rt = os.fork()
#             if rt == 0:
#                 hijo(matriz1, matriz2, 1, 1)
#                 #exit()
#             else:
#                 time.sleep(1)
#                 # os.waitpid(-1, 0)  # Esperar a que todos los procesos hijo terminen
#                 padre()
#                 exit()

import os
import time

def hijo(matriz1, matriz2, fila, columna, pipe):
    print('Mi índice es', fila, columna)
    resultado = matriz1[fila][0] * matriz2[0][columna] + matriz1[fila][1] * matriz2[1][columna]
    print('Mi resultado es', resultado)

    data = f"{fila},{columna},{resultado},$"
    pipeout = os.open(pipe, os.O_WRONLY)
    os.write(pipeout, str(data).encode())
    os.close(pipeout)


def padre(pipe):
    resultado = [[0, 0], [0, 0]]  # Inicializar matriz resultado

    for i in range(4):
       
            pipein = os.open(pipe, os.O_RDONLY)
            data = os.read(pipein, 100).decode()
            os.close(pipein)
            for i in range(len(data)):
                if data[i] == '$':
                    pass
                else:
                    fila= data[i]
                    columna= data[i+1]
                    resultado_hijo= data[i+2]
                    resultado[fila][columna] = resultado_hijo
                    print(resultado)

    #         fila, columna, resultado_hijo= data.split(',')
    #         fila = int(fila)
    #         columna = int(columna)
    #         resultado_hijo = int(resultado_hijo)

    #         resultado[fila][columna] = resultado_hijo

    # print('Resultado:')
    # for fila in resultado:
    #     print(fila)


matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]

pipe = "/tmp/pfifo"
if not os.path.exists(pipe):
    os.mkfifo(pipe)

rt = os.fork()
if rt == 0:
    hijo(matriz1, matriz2, 0, 0, pipe)
    exit()
else:
    rt = os.fork()
    if rt == 0:
        hijo(matriz1, matriz2, 0, 1, pipe)
        exit()
    else:
        rt = os.fork()
        if rt == 0:
            hijo(matriz1, matriz2, 1, 0, pipe)
            exit()
        else:
            rt = os.fork()
            if rt == 0:
                hijo(matriz1, matriz2, 1, 1, pipe)
                exit()
            else:
                time.sleep(1)
                padre(pipe)


