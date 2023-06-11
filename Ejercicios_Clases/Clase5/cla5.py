import os
from multiprocessing import Process, Queue

def multiplicar_elemento(matriz1, matriz2, fila, columna, resultado_fifo):
    resultado = matriz1[fila][0] * matriz2[0][columna] + matriz1[fila][1] * matriz2[1][columna]
    resultado_fifo.put((fila, columna, resultado))

if __name__ == "__main__":
    matriz1 = [[1, 2], [3, 4]]
    matriz2 = [[5, 6], [7, 8]]
    resultado_fifo = Queue()

    processes = []
    for fila in range(2):
        for columna in range(2):
            p = Process(target=multiplicar_elemento, args=(matriz1, matriz2, fila, columna, resultado_fifo))
            p.start()
            processes.append(p)

    for p in processes:
        p.join()

    resultado_final = [[0, 0], [0, 0]]
    while not resultado_fifo.empty():
        fila, columna, resultado = resultado_fifo.get()
        resultado_final[fila][columna] = resultado

    for fila in resultado_final:
        print(fila)
