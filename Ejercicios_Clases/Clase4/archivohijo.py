import sys
import os
import time
print('Este es el proceso hijo y su PID es: ', os.getpid())




for line in sys.stdin:
    contador = len(line.split())
    resultado = f"La linea tiene {contador} palabras.\n"
    time.sleep(1)
    sys.stdout.write(resultado)

    

sys.stdin.close()