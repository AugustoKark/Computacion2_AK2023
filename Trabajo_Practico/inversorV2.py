import getopt
import sys
import os

#este programa se ejecuta de la siguiente manera:
#python3 inversor3.py -f texto.txt
#A diferencia del otro programa, en este se ejecutan alternadamente padre e hijo,
#  y no se espera a que todos los hijos terminen para que el padre termine
print('Este ejercicio es una alternativa')
print('El padre no espera a que todos los hijos se ejecuten, sinó que despues de la ejecución de cada hijo, el padre se ejecuta.')
print('El padre se ejecuta tantas veces como hijos se crean')
def main():
    
    (opciones, argumentos) = getopt.getopt(sys.argv[1:], 'f:', ['file='])
  
    for opcion, argumento in opciones:
        if opcion in ('-f', '--file'):
            with open('texto.txt','r') as f:
                lineas = f.readlines()
                numero_de_lineas = len(lineas)
                mensajes = []
                for iter in range(numero_de_lineas):
                    r, w = os.pipe()
                    pid = os.fork()

                    if pid == 0:
                        #print('Soy el hijo y mi pid es: ', os.getpid())
                        
                        # Este es el hijo
                        linea_renglon = lineas[iter]
                        texto_al_reves = linea_renglon[::-1]
                        os.close(r)  # El proceso hijo no necesita leer de la tubería
                        w = os.fdopen(w, 'w')
                        mensaje = texto_al_reves
                        w.write(mensaje)
                        w.close()
                        sys.exit(0)

                    else:
                        #print('Soy el padre y mi pid es: ', os.getpid())
                        # Este es el proceso padre
                        os.close(w)  # El proceso padre no necesita escribir en la tubería
                        r = os.fdopen(r)
                        mensaje = r.read()
                        r.close()
                        mensajes.append(mensaje)
                        os.waitpid(pid, 0)  # Esperar a que el proceso hijo termine

            for mensaje in mensajes:
                if mensaje.strip()!= "":
                    print(mensaje)

        else:
            print('Hubo algún error')

if __name__ == '__main__':
    main()