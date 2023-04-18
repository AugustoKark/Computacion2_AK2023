#!/usr/bin/env python3
import getopt
import sys
#este programa se ejecuta de la siguiente manera:
#python3 ejercicio2.py "hola" "3"

def main():
    text=sys.argv[1]
    x=int(sys.argv[2])

    list=text*(x)
    print(list)
  
  

if __name__ == "__main__":
    main()
    

  
