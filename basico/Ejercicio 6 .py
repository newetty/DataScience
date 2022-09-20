#!/usr/bin/env python
# coding: utf-8

""" Ejercicio 1  Mínimo de una lista de números (lista de nombre "listado")
 30, 20, 10, 50, 40
"""" 1) Escribe el listado e ímprimelo"""
 

# In[23]:


listado = [30, 20, 10, 50, 40]


# In[24]:


listado


# 2) Prueba con min(listado)

# In[25]:


min(listado)


# 3) Realiza lo mismo pero con bucles y condicionales
# 

# In[26]:


for i in (30,20,10,50,40):
    print(i)


# In[27]:


maximo=-1000
for numero in listado:
    if numero>maximo:
        
        maximo=minimo
minimo


# In[28]:


maximo = -min(listado)-1
for numero in listado:
    if numero>maximo:
        maximo=numero
maximo



# Ejercicio 3
# Ordena de menor a mayor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")
# Pista: si quieres almacena esos números en una lista de nombre: "listado_ascendente"
# 1) Escribe el listado e ímprimelo

# In[38]:


listado = [30,20,10,50,40]


# In[39]:


listado


# In[40]:


listado.sort(reverse=False)
listado


# #Realiza lo mismo pero con bucles y condicionales
# 
# 

# In[6]:


# aqui el algoritmo
listado_ascendente=[] # listado vacío
while(len(listado)>0):# mientras que tenemos números en listado->longitud(listado) d
    listado_ascendente.append(min(listado))# apendizas el mínimo
 
    listado.remove(min(listado)) # le borras del listado original
listado_ascendente


# In[ ]:





# Ejercicio 4
# Ordena de mayor a menor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")
# 1) Escribe el listado e ímprimelo

# Ejercicio 4
# Ordena de mayor a menor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")
# 1) Escribe el listado e ímprimelo

# In[16]:


listado = [30,20,10,50,40]


# In[17]:


listado


# 2) Prueba a usar sort()

# In[18]:


listado.sort(reverse=True)
listado


# 3) Realiza lo mismo pero con bucles y condicionales
# 

# In[19]:


# me creo una copia para no perder la información
listado_copia = listado.copy()
listado_copia


# In[21]:


# aqui programa el algoritmo
listado_descendente=[]
while(len(listado)>0):
    listado_descendente.append(max(listado))
    listado.remove(max(listado))
listado_descendente


# Ejercicio 5
# Escribe el código necesario en Python para:
# almacenar con una lista de nombre "módulos" las siguientes materias de un programa de Ciencia de Datos:
# Big Data, Python, Algoritmos, Machine Learning, Deep Learning, NLP.
# 1)

# In[62]:


import pandas as pd


# In[63]:


módulos=["Big Data", "Python", "Algoritmos", "Machine Learning", "Deep Learning","NLP"]
módulos


# In[64]:


for módulo in módulos:
    print(módulo)


# 2)
# dentro de ese grupo de materias, existen unas materias que son básicas en todos los programas.
# y que forman la base de conocimientos iniciales para afrontar con éxito el resto de un programa.
# Las mismas son: Python y Algoritmos (aunque en la práctica hay más cosas)
# Se pide almacenar las mismas en un listado secundario, de nombre: "esenciales" (por ejemplo)
# Imprime ese listado al terminar de almacenarlos

# In[65]:


esenciales = ["Python", "Algoritmos"]
esenciales


# In[66]:


for esence in esenciales:
    print(esence)


# In[67]:


esenciales = []
for módulo in módulos:
    if (módulo=="Python") or (módulo=="Algoritmos"):
        esenciales.append(módulo) # adiciona a esenciales vacio Python y Algoritmos 


# In[68]:


esenciales


# 3)
# Crea un DataFrame, de nombre df con esa información en base a la siguiente relación de módulos y horas de clase
# módulos:
# Big Data, Python, Algoritmos, Machine Learning, Deep Learning, NLP
# horas:
# 25, 15, 5, 15, 5, 10

# In[73]:


módulos= ["Big Data", "Python", "Algoritmos", "Machine Learning", "Deep Learning","NLP"]
horas = [25, 15, 5, 15, 5, 10]
módulos


# In[74]:


horas


# In[75]:


df = pd.DataFrame({"módulos": módulos, "horas": horas})
df


# #De ese DataFrame, selecciona solamente la columna "horas" e imprímela

# In[78]:


df_horas=df["horas"]


# In[79]:


df_horas


# In[80]:


df[["horas"]]


# In[82]:


df.horas


# 5) Muestra el gráfico (plot) para la columna "horas"

# In[83]:


df.horas.plot(kind="bar")


# In[84]:


df_dedicacion_20 = df[df["horas"]>=20]
df_dedicacion_20


# 7)
# De ese DataFrame, selecciona solamente aquellas materias que tienen menos de 10 horas de dedicación

# In[85]:


df_dedicacion_10 = df[df["horas"]<=10]


# In[86]:


df_dedicacion_10


# 8)
# De ese DataFrame, selecciona solamente (si fuera posible) aquellas materias que tienen mas de 26 horas de dedicación

# In[87]:


df.módulos


# In[88]:


df_dedicacion_20 = df[df["horas"]>=26]
df_dedicacion_20


# 9)
# Apendiza, (si puedes), una nueva columna llamada "docente" con el instructor encargado de la materia.
# Y cuyos nombres serán: Enrique, Susana, Juan, Ana, Laura, Patricia

# In[93]:


df["docente"] = ["Enrique", "Susana", "Juan", "Ana", "Laura", "Patricia"]


# In[95]:


df["docente"] = ["Enrique", "Susana", "Juan", "Ana", "Laura", "Patricia"]
df

