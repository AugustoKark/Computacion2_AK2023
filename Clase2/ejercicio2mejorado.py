#!/usr/bin/env python3

#este programa se ejecuta de la siguiente manera:
#python3 ejercicio2mejorado.py -t "hola" -x 3
import getopt
import sys


def main():
    resultado=[]
    (opciones, argumentos) = getopt.getopt(sys.argv[1:], 't:x:', ['text=', 'times='])
  
    for opcion, argumento in opciones:
        if opcion in ('-t', '--text'):
            texto = argumento
        elif opcion in ('-x', '--times'):
            veces = int(argumento)

            resultado = texto * veces

    
    print(resultado)
    

if __name__ == '__main__':
    main()
    