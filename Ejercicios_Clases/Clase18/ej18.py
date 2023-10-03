from concurrent.futures import ProcessPoolExecutor
import os


prime_numbers = []

def prime_test(num):
    print('num: ', num, ' --- PID: ', os.getpid(), '  ')
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("Ingrese el número a evaluar: "))
print('PID PADRE: ', os.getpid())
# Crear un ThreadPoolExecutor con, por ejemplo, 4 hilos
with ProcessPoolExecutor(max_workers=4) as executor:

    # Enviar tareas para su ejecución concurrente
    futures = [executor.submit(prime_test, i) for i in range(1, abs(num))]
            
    for i, future in enumerate(futures):
        if future.result() is True:
            prime_numbers.append(i + 1)

# print(f"\nNúmeros primos:", prime_numbers, "hasta ", num)
print(f"El número primo inmediatamente inferior a", num, "es:", max(prime_numbers))