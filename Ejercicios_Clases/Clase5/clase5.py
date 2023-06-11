'''FIFOS

1- Escribir un programa que realice la multiplicación de dos matrices de 2x2. 
Cada elemento deberá calcularse en un proceso distinto devolviendo el resultado en una fifo indicando el indice del elemento. 
El padre deberá leer en la fifo y mostrar el resultado final.
'''
#A veces tira error, pero funciona

import os
import time


def hijo(matriz1, matriz2, fila, columna, pipe):
    # time.sleep(1)
    # look.acquire()
    print('Mi índice es', fila, columna)
    resultado = matriz1[fila][0] * matriz2[0][columna] + matriz1[fila][1] * matriz2[1][columna]
    print('Mi resultado es', resultado)

    data = f"{fila},{columna},{resultado},"
    pipeout = os.open(pipe, os.O_WRONLY)
    os.write(pipeout, str(data).encode())
    os.close(pipeout)
    # look.release()


def padre(pipe):
    time.sleep(1)
    cte=0
    resultado_padre=[[0, 0], [0, 0]]

    

    pipein = os.open(pipe, os.O_RDONLY)
    data = os.read(pipein, 100).decode()
    data=data.split(",")
    print(data)
    os.close(pipein)
    for i in range(4):
            
            fila= int(data[cte])
            columna= int(data[cte+1])
            resultado_hijo= int(data[cte+2])
            resultado_padre[fila][columna] = resultado_hijo
            cte+=3
    print(resultado_padre)


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
                time.sleep(6)
                padre(pipe)




#Resultado :
# Mi índice es 0 1
# Mi resultado es 22
# Mi índice es 1 0
# Mi resultado es 43
# Mi índice es 1 1
# Mi resultado es 50
# Mi índice es 0 0
# Mi resultado es 19
# ['1', '1', '50', '0', '0', '19', '0', '1', '22', '1', '0', '43', '']
# [[19, 22], [43, 50]]


