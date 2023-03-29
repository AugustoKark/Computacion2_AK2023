#!/usr/bin/env python3

#Realizar un programa que implemente fork junto con el parseo de argumentos.
# Deberá realizar relizar un fork si -f aparece entre las opciones al ejecutar el programa. 
#El proceso padre deberá calcular la raiz cuadrada positiva de un numero y el hijo la raiz negativa.
import os
import sys
import getopt
number=0

opts,args = getopt.getopt(sys.argv[1:], 'f,n:', ['fork','number='])
for opt, arg in opts:
    if opt in ['-n', '--number']:
        
        
        number = int(arg)
        if number>=0:
            print('el numero asignado es %d' % number)
        else:
            print('el numero asignado es negativo')
            sys.exit(1)
            


        
for opt, arg in opts:
    if opt in ['-f', '--fork']:
        ret = os.fork()
        if ret > 0:

            raiz_padre= number**(1/2)
            print('Soy el padre (PID: %d)-----(PPID %d)' % (os.getpid(), os.getppid()))
            print('La raiz cuadrada positiva de %d es %d' % (number, raiz_padre))
        if ret == 0:
            raiz_hijo= (number**(1/2))*-1
            print('Soy el hijo (PID: %d) ------ -----(PPID %d)' % (os.getpid(), os.getppid()))
            print('La raiz cuadrada negativa de %d es %d' % (number, raiz_hijo))


        
        
