import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# EJERCICIO 1

"""Dada estos valores: 15 16 17 16 21 22 15 16 15 17 16 22 14 13 14 14 15 15 14 15 16 10 19 15 15 22 24 25 15 16#



# 
# 1) Realiza un Histograma con tamaño de barra 2.
# realizar un histagrama:"""
#opcion 1 

df = pd.DataFrame({"x": [31,10,85,25,4,83,32,43,66,18,93,
                        6,42,27,21,42,53,32,85,32,42,58,67,17,4,5]})

##plt.hist(df, bins=2,
#color="green",
##histtype="bar",
#rwidth= 0.25)
#plt.show()

# opcion 2 

#y_pos = np.arange(len(df))
#performance = 3 + 10 * np.random.rand(len(df))
#error = np.random.rand(len(df))

#ax.barh(y_pos, performance, xerr=error, align='center')
#ax.set_yticks(y_pos, labels=df)
##ax.invert_yaxis()  # labels read top-to-bottom
#ax.set_xlabel('frecuencia')
#ax.set_title('Numbers today')
#plt.show()#

# 2) ¿Cuál es el número que más se repite?
"""sesgo positivo hacia la derecha"""

# 3) ¿Qué pasa si cambiamos a tamaño de barra 5?
df = pd.DataFrame({"x": [31,10,85,25,4,83,32,43,66,18,93,6,42,27,
                        21,42,53,32,85,32,42,58,67,17,4,5]})
                    
plt.hist(df, bins=5, # modificando solo el número de barras
        color="green",
        histtype="bar",
        rwidth= 0.75)
# cuadrícula
plt.grid(True)
# Etiqueta del eje de la X
plt.xlabel("Edad")
# Etiqueta del eje de la Y
plt.ylabel("Frecuencia")
# titulo:
plt.title("Mi segundo Histograma")
# Mostrar el gráfico:
#plt.show()

#histograma(df,5)

# 4) ¿Qué pasa si cambiamos a tamaño de barra 20?
##histograma(df,20)

#5) ¿Qué parece indicar el sesgo en la distribución?#
df = pd.DataFrame({"x": [31,10,85,25,4,83,32,43,66,18,93,6,42,27,
                        21,42,53,32,85,32,42,58,67,17,4,5]})

def scatterPlot(df):
    plt.scatter(df, label="años", marker="+", s=200)
    plt.grid(True)
    plt.xlabel("eje X")
    plt.ylabel("Eje y")
    plt.title("nube de puntos")
    plt.legend()
    plt.show()

