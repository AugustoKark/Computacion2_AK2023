import os 
import time

fdr , fdw = os.pipe()

time.sleep(20)

pid = os.fork()

#HIJO 
if pid == 0:
    os.close(fdw)
    while  True:
        leido = os.read(fdr, 2024) #leo del pipe.
        if len(leido)==0:
            break
        os.write(1,leido.upper())
    exit()
#PADRE
os.close(fdr)
while True:
    leido = os.read(0,2024) #leer sobre la pantalla con bloques de a 2024 bytes
    if len(leido)==0: # si en el buffer no hay nada, termina
        break
    os.write(fdw,leido) # escribo en el pipe       