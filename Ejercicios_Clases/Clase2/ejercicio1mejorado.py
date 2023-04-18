#!/usr/bin/env python3
import getopt
import sys

#este programa se ejecuta de la siguiente manera:
#python3 ejercicio1mejorado.py -n 5

def main():
    #n=''
    lst=[]  
    impar=1
    contador=0
    
    (opts, args) = getopt.getopt(sys.argv[1:], 'n:')
    for opt, arg in opts:
        if opt in ('-n'):
                for arg in range(0, int(arg)):
                    lst.append(impar)
                    impar += 2
                

    print(lst)
    return lst

if __name__ == "__main__":
    main()
    
