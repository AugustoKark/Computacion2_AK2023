import math
import threading



def calcular_termino(n, x):
    termino = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    return termino

def calcular_hilo(n, x, resultados):
    termino = calcular_termino(n, x)
    resultados.append(termino)

def calculo_final(resultados):
    suma = sum(resultados)
    return suma

def suma_hilos(resultados_hilos):
    suma_total = sum(resultados_hilos)
    return suma_total

def main():
    x = 1.5
    num_terminos = 12


    resultados = []
    resultados_hilos = []
   

    hilos = []
    for n in range(num_terminos):
        hilo = threading.Thread(target=calcular_hilo, args=(n, x, resultados))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()
        resultados_hilos.append(sum(resultados))

    hilo_suma = threading.Thread(target=suma_hilos, args=(resultados_hilos,))
    hilo_suma.start()
    hilo_suma.join()

    suma = calculo_final(resultados)
    valor_referencia = math.sin(x)

    print("Suma de términos calculados por cada hilo:", resultados_hilos)
    print("Suma total de los términos calculados:", suma)
    print("Valor de referencia:", valor_referencia)
    print("Diferencia con el valor de referencia:",abs( suma - valor_referencia))



if __name__ == "__main__":
    main()


