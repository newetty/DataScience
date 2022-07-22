# Ejercicio 19 - funcion inversa de una cadena 

from cgitb import text
from operator import inv, invert
from plistlib import InvalidFileException
from re import I

def invert_cadena(text):          #función inversa para una cadena : text
    salida = ''                   #designamos signo cadena vacia
    i = len[text]                 #cantidad total de caracters que tiene el texto 
    while i > 0:                  #ciclo while preguntamos se elvalor i es >0 
       salida += i [text[-1]]         #si se cumple concatenamos a la variable salida el contenido de text en la posicion que indique el indice
       i  -= 1                    # reducimos en una unidad el contenido de la variable indice
    return salida

lenguaje = 'ovlop'
print(invert_cadena(lenguaje))

print(invert_cadena('polvo'))


#Ejercicio 2 -  Definir una función es_palindromo() que reconoce palíndromos (es decir, 
# palabras que tienen el mismo aspecto escritas invertidas), 
# ejemplo: es_palindromo ("radar") tendría que devolver True.
