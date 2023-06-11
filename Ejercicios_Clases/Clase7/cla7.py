import getopt
import sys
import mmap
import signal
import os

mmap = mmap.mmap(-1, 1024)

global texto

def hijo1():
    while True:
        input = sys.stdin.readline().strip()
        if input != 'bye':
            mmap.write(input.encode())
            mmap.seek(0)

            os.kill(os.getppid(), signal.SIGUSR1)
        else:
            os.kill(os.getppid(), signal.SIGUSR2)
            break

def padre(signum, frame):
    mmap.seek(0)
    line = mmap.readline().decode().strip()
    print(line,"soy el padre")
    mmap.seek(0)
    os.kill(h2_pid, signal.SIGUSR1)

def hijo2(signum, frame):
    mmap.seek(0)
    line = mmap.readline().decode().strip()
    mmap.seek(0)
    mmap.write(line.upper().encode())
    mmap.seek(0)
    print(line.upper(),"soy el hijo 2")
    # os.kill(ppid, signal.SIGUSR1)
    texto=line.upper()

signal.signal(signal.SIGUSR1, padre)
signal.signal(signal.SIGUSR2, hijo2)

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
            
            with open(argumento, 'r+') as f:
                print('El archivo existe')
                # mmap.write(f.read().encode())
                # mmap.seek(0)
                ppid = os.getpid()
                h1_pid = os.fork()

                if h1_pid != 0:
                    h2_pid = os.fork()
                    

                    if h2_pid == 0:
                        signal.signal(signal.SIGUSR1, signal.SIG_IGN)
                        signal.pause()

                    if h2_pid != 0:
                        while True:
                            try:
                                pid, status = os.waitpid(h1_pid, 0)
                                if pid == h1_pid:
                                    os.kill(h2_pid, signal.SIGUSR2)
                                    os.waitpid(h2_pid, 0)
                                    break
                            except ChildProcessError:
                                break

                if h1_pid == 0:
                    # Hijo 1
                    while True:
                        hijo1()
                        os._exit(0)
                linea = mmap.readline().decode().strip()
                print(linea,'soy el padre desde aqui')
                f.write(linea)

        except FileNotFoundError:
            print('El archivo no existe')
            sys.exit(2)
