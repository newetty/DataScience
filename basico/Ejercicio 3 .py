#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# Ejercicio 1
# Dada una lista de nombre "listado" y con valores: 10,20,30,40,50

# In[2]:


listado = [10,20,30,40,50]


# 1)
# Crea un pequeño programa capaz de conseguir el orden inverso de los números de "listado"

# In[3]:


listado.reverse()
listado


# In[4]:


# imprime nuevamente el listado para tenerlo "a mano"
# 10-20-30-40-50 (tengo)
# 50-40-30-20-10 (lo que busco)


# In[5]:


# necesitas instalar con:
# pip install numpy
import numpy as np


# In[6]:


pip install numpy


# In[2]:


import numpy as np

list(np.arange(5))



# In[3]:


type(list(np.arange(5))[0])


# In[4]:


np.arange(5).tolist()


# In[5]:


type(np.arange(5).tolist()[0])


# In[6]:


rango_indices = np.arange(1,len(listado)+1,1).tolist()
rango_indices


# In[7]:


listado_inverso = []

for indice in rango_indices:
    listado_inverso.append(listado(-indice)                                                
  


# Ejercicio 2
# Programa que coge por teclado 5 números y los almacena en una lista
# Nota:
# debería estar en la misma celda
# Hazlo como puedas, discurre cómo sería..

# In[2]:


import numpy as np


# In[3]:


a= np.arange(1,6,1) #(star=1, stop=6, step=1)
a


# In[ ]:


# entrada por teclao de 5 números
listado_teclado = []
for i in a:
    entrada = int(input("Escribe un numero entero"))
    listado_teclado.append(entrada)
    

print("\n")
listado_teclado



    


# Ejercicio 3
# Programa que coge por teclado una frase y es capaz de decir cuántas vocales hay
# Nota: asume que son letras minúsculas sin tildes.
# 1)

# Entrada de texto por teclado

# In[2]:


frase = input("escribe una frase")
frase


# Hazlo si puedes de varias formas
# forma 1: contar vocales en palabra/frase

# In[4]:


#contar vocales 
# += anñade un valor automaticamente
# vocales
contador_vocales = 0 # contador a 0
vocales = ["a", "e", "i", "o", "u"]
for letra in frase:
    if letra in vocales:
        contador_vocales+=1
contador_vocales


# In[ ]:


# entrada por teclado de una frase y conta las vocales que haya.

teclado_frase = []
for i in a: 
    


# Tablas de multiplicar:
# Haz algo tal que:
# 1) Pregunta al usuario que tabla quiere multiplicar: <1 al 10>
# 2) Muestra los resultados de esta forma:
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 2 x 10 = 20

# In[20]:


tabla = int(input("Elija de que número quiere las Tablas de multiplicar: <1 a 10>:.."))
tabla



# In[21]:


import numpy as np


# In[22]:


numeros= np.arange(1,11,1)
numeros


# In[23]:


for numero in numeros:
    print(tabla, " x ", numero, " = ", tabla*numero)


# In[ ]:




