import pandas as pd

"""Ejercicio 1
Dado el siguiente listado: ["Python", "Matlab", "R", "VBA", "Julia", "C++"].
Modifica con un algoritmo ese listado.
Cuando encuentre Python debe poner un 1
y cuando encuentre otro lenguaje de programacion, un 0
es un simple ejemplo de modificación de valores en una lista"""

listado = ["Python", "Matlab", "R", "VBA", "Julia", "C++"]
for i in range(len(listado)): #crea un iterable con los elementos de la lista(considerando su longitud)
    if listado[i]=="Python":  #doy un valor para elemento del listado en la posicion Python
        listado[i]=1            #asigno que listado na posicion i (Python) es igual a 1 
    else:
        listado[i]=0
#Desconectar par ejecutar·
#   print(listado)

"""Ejercicio 2"""
L = [10, None, 8, 5, None, 20]
"""2.2) Susitituir por -1 el valor None usando bucles y listas"""
for i in range(0, len(L)):
    if L[i]== None:
        L[i]= -1
    #print(L)
for i in range(len(L)):
    if L[i]== None:
        L[i]= -1
#Desconectar para ejecutar
    #print(L)
"""2.3) Creamos un dataframe con los valores de la lista y modificamos los "NaN" por un valor de -1 (Valores nulos, suma, etc..)"""

lista = [10, None, 8, 5, None, 20]
#print(lista)

df = pd.DataFrame(lista)
#print(df)
lista = [10, None, 8, 5, None, 20]
df = pd.DataFrame(lista)
df = df.fillna(-1)
#Desconectar para ejecutar
#print(df)

"""2.4) Vuelve a escribir el listado con falta de valores (inicial), y sustituye por la media."""

L = [10, None, 8, 5, None, 20]

df = pd.DataFrame(lista)
#Desconectar para ejecutar
#df = df.mean()
#print(df)
#df= df.fillna(10.75)
#Desconectar para ejecutar
#print(df)
"""2.5) Apendiza la columna con estos valores"""
listado3 = [10, 20, 50, 30, 20, 0]
#print(listado3)


df["listado3"] = listado3
# Desconectar para ejecutar
#print(df)
#2.6) Elimina la columna L

df = df.drop(["listado3"], axis=1)
#Desconectar para ejecutar 
#print(df)

"""Ejercicio 3
Crear un listado con los siguientes numeros: 10, 20, 30, 40 (nombra la lista con nombre: "listado")"""

listado=[10, 20, 30, 40]


#1) Crea el listado e imprimelo:

#print(listado)

#2) Apendiza el valor 50 ( si es posible)

listado.append(50)
#Desconectar para ejecutar
#print(listado)
#3) Modifica (si es posible) el valor 10 por 100

for elemento in range(len(listado)):
    if listado[elemento]==10:
        listado[elemento] = 100
#Desconectar para ejecutar
 #       print(listado)
"""Ejercicio 4
Da una lista de nombre "Temperatura" con valores: 10, 20, 30, 40, 50"""

Temperatura=[10,20,30,40,50]
#Desconectar para ejecutar
#print(Temperatura)
"""2) En este "Temperatura". 
¿Cuál es el elemento en la posición (index) 1?"""

#Deconectar para ejecutar
Temperatura[1]
#print(Temperatura[1])


"""3) ¿Y en la posición (index) 0?"""

#Desconectar para ejecutar
#Temperatura [0]
#print(Temperatura[0])

"4) ¿Y en la posición (index) -1?"
#Desconectar par ejecutar
Temperatura [-1]
#print(Temperatura [-1])


