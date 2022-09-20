#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as py


# Ejercicio 1
# a) Declara la variable "test" como una lista con los siguientes componentes: 25, 8, 32, 20, 1. Usa las formas que conozcas para crearla y
# el uso de type para asegurarte de que es una lista.

# In[31]:


test= [25,8,32,20,1]


# In[32]:


test


# In[33]:


type(test)


# In[34]:


test = list((25,8,32,20,1))
test


# b) Apendiza un valor de valor 20, 32, 25, 32

# In[35]:


test.append(20)
test


# In[36]:


test.append(32)
test


# In[37]:


test.append(25)
test


# In[38]:


test.append(32)
test



# In[39]:


Lista = [20, 32, 25, 32]
for Listas in Lista:
    test.append(Lista)
test


# c) Elimina el valor 8 de la lista

# In[40]:


test.remove(test[1])


# In[41]:


test


# d) Elimina los duplicados que haya en la lista test

# In[42]:


# Eliminar valores duplicados y colocarlos

test = list(set(test))
test


# In[ ]:




