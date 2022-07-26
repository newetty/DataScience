# Ejercicio 19 - funcion inversa de una cadena 

from ast import While
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



"""
#Ejercicio 2 -  Definir una función es_palindromo() que reconoce palíndromos (es decir, 
# palabras que tienen el mismo aspecto escritas invertidas), 
# ejemplo: es_palindromo ("radar") tendría que devolver True.

"""

def es_palindromo(palabra):
    i = 0 
    while i <= len(palabra) / 2:
        if palabra[i] != palabra[-i - 1]:
            return False
        i += 1
    return True

# or 

def es_palindromo(escrita): 

    normal = 0 
    detras_para_adelante = len(normal) -1

    if not escrita[normal] == escrita[detras_para_adelante]:
        return False

    else:
            return True
    print(es_palindromo('cruel'))
    print(es_palindromo('ana'))


    """""
    
   #3- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo
#contrario. Escribir la función usando el bucle for anidado.
    """

list1 = ['a', 'e', 'i', 'o', 'u']
list2 = ['b', 'c', 'd', 'e', 'o']

def superposicion (list1, list2):
    for n in list1:
        for p in list2:
            if n == p:
                return True
    return False
print(superposicion(list1, list2))