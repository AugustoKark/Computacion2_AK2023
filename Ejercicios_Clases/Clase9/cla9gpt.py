import multiprocessing

def es_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

if __name__ == '__main__':
    with multiprocessing.Pool(processes=2) as pool:
        numeros = range(2, 100)
        resultados = pool.map(es_primo, numeros)

    primos = [numero for numero, es_primo in zip(numeros, resultados) if es_primo]
    print("Números primos menores a 100 (estrategia de Pool):", primos)
