import getopt
import os
import sys
import getopt
import time
import signal

### Requerimientos
#Escriba un programa que abra un archvo de texto pasado por argumento utilizando el modificador -f.
#* El programa deberá generar tantos procesos hijos como líneas tenga el archivo de texto.
#* El programa deberá enviarle, vía pipes (os.pipe()), cada línea del archivo a un hijo.
#* Cada hijo deberá invertir el orden de las letras de la línea recibida, y se lo enviará al proceso padre nuevamente, también usando os.pipe().
#* El proceso padre deberá esperar a que terminen todos los hijos, y mostrará por pantalla las líneas invertidas que recibió por pipe.
#* Debe manejar los errores.

 #creo el primer pipe 
rI, wI = os.pipe()  # ENTRADA
#creo el segundo pipe
rO, wO = os.pipe() # SALIDA

class padre():
        def escribir(self,wI,linea):
            #print('Este es el pid del padre ',os.getpid())
            for i in linea:
                linea1 = bytes(i, 'utf-8')
                #print(linea1)
                os.write(wI,linea1)
            
      
        def leer(self,rO,longaleer):
           # print('Este es el pid del padre ',os.getpid())
            texto=os.read(rO,longaleer)
            print(texto.decode())
            
class hijo():
        def transformar(self,inn,out,longitud):
            #print('Este es el pid del hijo ',os.getpid())
            #print('Este es el pid del hijo ',os.getpid())
            linn=''
            caracter=os.read(rI,longitud)
            caracter1=caracter.decode()
            linn=caracter1[::-1].replace("'", "")
            lout=bytes(str(linn), 'utf-8')
            os.write(wO,lout)
            
        def matar(self,pid):
            os.kill(pid, signal.SIGTERM)
                       
                     

hijo= hijo()
padre= padre()


try:
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
                            lineas = f.readlines()
                            numero_de_lineas = len(lineas)
                            longitud = 0
                            
                        padre.escribir(wI,lineas)    #escribo en el pipe  
                        time.sleep(3)  
                        for k in range(numero_de_lineas):
                                longitud = len(lineas[k])
                                pid = os.fork()
                                if pid == -1:
                                    print('Error al crear proceso hijo')
                                    sys.exit(1)
                                if pid == 0:
                                    hijo.transformar(rI,wO,longitud)
                                    time.sleep(3)
                                

                                    
                                #elif pid > 0: # código para el proceso padre
                                #    time.sleep(3)
                                #    os.kill(pid, signal.SIGTERM)
                                    
                                    

                        
                        for m in range(numero_de_lineas):
                            longaleer=len(lineas[m])
                            padre.leer(rO,longaleer)
                        sys.exit()
                    except FileNotFoundError:
                        print('No se encontró el archivo')
                        sys.exit(2)
except getopt.GetoptError:
    print('Error al leer los argumentos.')
    sys.exit(2)



            
                            
                        

                        
                    