#!/usr/bin/env python3
import sys
#este programa se ejecuta de la siguiente manera:
#python3 ejercicio1.py 5

def main():
    impar=1
    lst=[]
    impares = sys.argv[1]
    for i in range(0, int(impares)):
        lst.append(impar)
        
        impar += 2
    print(lst)

if __name__ == "__main__":
    main()
    