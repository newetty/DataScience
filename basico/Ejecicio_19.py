# Ejercicio 19 - funcion inversa de una cadena 

def invert_text(text):
    if len(text)== 0:

        return(text)

    else:
        return invert_text[1:] + text[0]
    text = "luciana"
 
def inversa2(cadena):
    return cadena[::-1]

resultado = inversa2("Hola mundo2")
print(resultado)




"""
#Ejercicio 2 -  Definir una funcion es_palindromos() que reconoce palindromos (es decir, 
# palabras que tienen el mismo aspecto escritas invertidas), 
# ejemplo: es_palindromo ("radar") tendria que devolver True.

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
    
   #3- Definir una funcion superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en comun o devuelva False de lo
#contrario. Escribir la funcion usando el bucle for anidado.
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