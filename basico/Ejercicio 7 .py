#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# Ejercicio 1
# Dado: "np.arange(2,10)"
# sigue los siguientes pasos:
# 1)
# Escribe esa instrucción y asígnaselo a la variable "a"

# In[6]:


a = np.arange(2,10)


# In[7]:


a


# 2)
# ¿Es equivalente a "np.arange(2,10,1)"?

# In[8]:


b = np.arange(2,10,1)
b


# In[9]:


a==b


# 3)
# se pide quedarse con aquellos números menores de 5.
# hazlo con numpy si puedes para la variable "a"

# In[12]:


menores5 =[]
for i in b:
    if i< 5:
        menores5.append(i)
menores5


# In[13]:


# imprimo "a" nuevamente
a


# 4)
# hazlo pasando esa información (de "a") a una lista
# 

# In[14]:


a.tolist()


# In[15]:


listado= a.tolist()


# In[ ]:





# In[17]:


listado


# 5)
# en base a los resultados..
# ¿Es posible recorrer 1 a 1 un array de numpy?

# In[ ]:


for i in a:
    if i 


# 6)
# Haz el mismo proceso programando una sola línea (toma "a" como referencia)

# In[18]:


# en una sola línea..
[numero for numero in a if numero<5]


# In[19]:


listado2 = [numero for numero in a if numero<5]
listado2


# Ejercicio 2
# Para estos valores (v de valores por abreviar):
# v1 = 4
# v2 = 5
# v3 = 7
# v4 = 8
# El objetivo será calcular la media de estos valores
# Para ello sigue los siguientes pasos:
# 1)
# imprime los valores de esas variables v1,v2,v3,v4

# In[24]:


#valores
v1 = 4
v2 = 5
v3 = 7
v4 = 8
v1,v2,v3,v4


# 2)
# Descomenta las 2 líneas siguientes para aprender..
# que es posible asignar varios valores en la misma línea
# Y la asignación de valores a variables se hace de forma consecutiva.

# Ejercicio 3
# Factorial de un número
# Nota:
# El Factorial de 5, por ejemplo:
# 5! = 5 4 3 2 1 = 120
# y el de 3:
# 3! = 3 2 1 = 6
# y así para todos..
# PASOS A SEGUIR Y COSAS A TENER EN CUENTA
# Pide por teclado el número del cual quieres calcular el factorial.
# Para que no sea muy grande te recomendamos:
# 3,4 o 5 (para hacer las pruebas)
# si ya no lo recuerdas o nunca lo viste, no te preocupes..
# 3! es: 3 2 1 = 6
# 4! es: 4 3 2 * 1 = 24
# 5! es: 5 4 3 2 1 = 120
# (esto es lo que se pide, en esencia)

# In[25]:


numero=int(input("Factorial de (3, 4 5 escribe es ...."))
numero


# In[ ]:




