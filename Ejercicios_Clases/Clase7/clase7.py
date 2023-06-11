''' Memoria Compartida

Etapa 1
Escribir un programa que reciba por argumento la opción -f acompañada de un path_file
El programa deberá crear un segmento de memoria compartida y generar dos hijos H1 y H2.
H1 deberá leer desde sdtin lo que ingrese el usuario, línea por línea, enviando una señal USR1 al padre en cada línea leida.
Una vez ingresada una línea, el proceso padre leerá la memoria compartida y mostrará la línea leida por pantalla y enviará una señal USR1 a H2.
Al recibir la señal USR1, H2 leerá la línea desde la memoria compartida y la escribirá en mayúsculas en el archivo recibido como argumento.

Etapa 2
Cuando el usuario introduzca "bye" en la terminal, H1 enviará al padre la señal USR2 y terminará.
Al recibir la señal USR2, el padre, la enviará a H2 que también terminará.
El padre esperará a ambos hijos y terminará también. '''

import getopt
import sys
import mmap
import signal

import os
# mmap=mmap.mmap(-1, 1024, mmap.MAP_ANONYMOUS | mmap.MAP_SHARED)
mmap=mmap.mmap(-1, 1024)

def hijo1():
    input=os.read(sys.stdin,1024)
    if input!='bye':
        mmap.write(input)
        mmap.seek(0)
        os.kill(os.getppid(), signal.SIGUSR1)
    else:
        os.kill(os.getppid(), signal.SIGUSR2)

def padre():
    mmap.seek(0)
    print(mmap.readline())
    mmap.seek(0)
    os.kill(os.getpid(), signal.SIGUSR2)

def hijo2():
    mmap.seek(0)
    mmap.write(mmap.readline().upper())
    mmap.seek(0)
    # os.kill(os.getppid(), signal.SIGUSR2)




signal.signal(signal.SIGUSR1, padre())  
signal.signal(signal.SIGUSR2, hijo2())     

(opciones, argumentos) = getopt.getopt(sys.argv[1:], 'f:', ['file='])
if not opciones:
        print('Falta argumento -f')
        sys.exit(2)

for opcion, argumento in opciones:
            if opcion not in ('-f', '--file'):
                print('Opción no válida')
                sys.exit(2)
            if opcion in ('-f', '--file'):
                try:
                    with open(argumento,'r') as  f:
                        print('El archivo existe')
                        rt1=os.fork()
                        if rt1!=0:
                            #padre

                            rt2=os.fork()

                            if rt2==0:
                                signal.signal(signal.SIGUSR1, hijo2())
                                signal.pause()
                                f.write(mmap)
                            
                            if rt2!=0:
                                try:
                                    while True:
                                        os.wait()
                                except ChildProcessError:
                                    exit()
                            
                        if rt1==0:
                            #hijo1
                            hijo1()
                            os._exit(0)      
                except:
                    print('El archivo no existe')
                    sys.exit(2)