
#1- Escribir un programa en Python que comunique dos procesos. 
# El proceso padre deberá leer un archivo de texto y enviar cada línea del archivo al proceso hijo a través de un pipe. 
# El proceso hijo deberá recibir las líneas del archivo y, por cada una de ellas, contar la cantidad de palabras que contiene y mostrar ese número.
import subprocess
import os
import time


print('Este es el proceso padre y su PID es: ', os.getpid())

# Obtener ruta completa del archivo "archivohijo.py"
ruta_archivo = os.path.expanduser('~/Documentos/Computacion2/Clase4/archivohijo.py')

# Verificar si el archivo existe en la ruta especificada
if not os.path.isfile(ruta_archivo):
    print("El archivo no existe en la ruta especificada:", ruta_archivo)
    exit()

# Abrir proceso secundario
p = subprocess.Popen(['python3', '-u', ruta_archivo], stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd=os.path.expanduser('~/Documentos/Computacion2/Clase4'))

# Leer archivo "archivo.txt" y enviar líneas al proceso secundario
with open('archivo.txt','r' ) as f:
    for line in f:
        p.stdin.write(line.encode())
        p.stdin.flush()
        

        respuesta = p.stdout.readline().decode()
        print(respuesta)

p.stdout.close()    
p.wait()



