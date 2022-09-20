#!/usr/bin/env python
# coding: utf-8

# Ejercicio 1
# 

# Crear un pequeño programa que calcule la multiplicación de 2 números (x, y)
# x = 3, y = 5
# x = 7, y = 3
# a) Con una función (por ejemplo funcion_multiplicar)

# In[9]:


import pandas as pd
import numpy as np


# a) Con una función (por ejemplo funcion_multiplicar)

# In[24]:


def multiplicar(x,y):
    return x*y 


# In[25]:


multiplicar(x,y)


# In[26]:


multiplicar(8,9)


# In[27]:


multiplicar(7,5)


# b) Con la función lambda (Tal vez puedes ir a repasarlo)
# una forma...

# In[30]:


def funcion(x):
    return x + 1


# In[31]:


funcion(x)


# In[32]:


funcion(9)


# In[33]:


(lambda x: x + 1)(3)


# In[34]:


f = lambda x: x + 1
f(3)


# In[35]:


f = lambda x: x + 1
f(6)


# c) Realizarlo con entrada de teclado (input)

# In[39]:


x= int(input("escribe un numero"))
y= int(input("escribe un numero"))
z=x*y
print(z)


# Otra forma sin ser tan repetitivo...

# In[49]:


def funcion_multiplicar():
    x= int(input("escribe un numero..."))
    y= int(input("escribe un numero..."))
    z=x*y
    print(z)


# In[50]:


funcion_multiplicar()


# Ejercicio 2
# 

# -ADado
# un string:
# "Level"
# ¿Es un palíndromo?
# -B-
# ¿Y este string?
# "level"
# Nota: "Es un palíndromo si se invierte el orden del string, el resultado es exactamente el mismo"

# In[87]:


def es_palindromo(x):
    if str(x) == str(x)[::-1]:
        print("Palindrome")
    else:
    
        print("Not Palindrome")


# In[88]:


word=input()
if str(word) == str(word)[::-1]:
    print("Palindrome")
    
else:
        print("Not Palindrome")


# In[96]:


def palindromo(cadena):
    inicio = 0
    fin = len(cadena) - 1
    while cadena[inicio] == cadena[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False


# In[ ]:





# In[97]:


def remover_caracteres_especiales(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace(" ", "")
    cadena = cadena.replace("á", "a")
    cadena = cadena.replace("é", "e")
    cadena = cadena.replace("í", "i")
    cadena = cadena.replace("ó", "o")
    cadena = cadena.replace("ú", "u")
    return cadena


# In[100]:


def esPalindromo(texto):
    return texto == texto[::-1]# invertir la cadena


# In[101]:


esPalindromo(level)


# otra forma de solucionar paso a paso

# In[107]:


A = "Level"



# lista vacia para invertir la lista inicial

A1=[]

                            # el último valor (index -1)
i=-1

                            # revertimos el orden de la lista inicial (A)

while len(A1)<len(A):
    
    A1.append(A[i])
    i-=1                      # i = i-1 ( decremento )
    
A1

# !=  is not equal que 
different = 0 # inicializamos la variable

for i in range (len(A)):
    if len(A)!=len(A1):      #con != ( no es igual que )
        different+=1
        if different == 0:
            
            print("palíndromo")
    else:
        
        print("no un palíndromo")
        print("tenemos", different, "elementos diferentes")



# Ejercicio 3
# Dado 2 strings:
# S1 = "Hi!"
# S2 = "Hello!"
# Imprimir las letras que son comunes

# In[2]:


S1="Hi!"
S2="Hello"
for elemento in S1: #H i
    for letra in S2:
        if elemento == letra:
            print(elemento)
    
    


# In[ ]:




