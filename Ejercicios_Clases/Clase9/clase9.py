#1 - Realizar un programa que busque los numeros primos menores a 100. Hacerlo usando al menos dos estrategias de Pool.
import multiprocessing

def es_primo(numero):
    if numero < 2:
        return True
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return False

    return True
    

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    primos = pool.map(es_primo, range(1, 100))
    # print(primos)
    lista = []
    pool.close()
    pool.join()
    for i in range (len(primos)):
        if primos[i]==True:
            lista.append(i+1)

    print(lista)

            
    