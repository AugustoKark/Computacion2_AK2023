import os

print('SOY EL PADRE (PID: %d)' % os.getpid())
print('------------------------------------')

#Error al crear el proceso hijo
try:
    ret = os.fork()
except OSError:
    print('Error al crear el proceso hijo')
    
#Proceso padre
ret = os.fork()

if ret > 0:
    print('Soy el padre (PID: %d)-----(PPID %d)' % (os.getpid(), os.getppid()))

elif ret == 0:
    print('Soy el hijo (PID: %d) ------ -----(PPID %d)' % (os.getpid(), os.getppid()))