import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# EJERCICIO 1

"""Dada estos valores: 15 16 17 16 21 22 15 16 15 17 16 22 14 13 14 14 15 15 14 15 16 10 19 15 15 22 24 25 15 16#
# 2) ¿Cuál es el número que más se repite?
# 3) ¿Qué pasa si cambiamos a tamaño de barra 5?
# 4) ¿Qué pasa si cambiamos a tamaño de barra 20?
# 5) ¿Qué parece indicar el sesgo en la distribución?
# 1) Realiza un Histograma con tamaño de barra 2.
# realizar un histagrama:"""
#opcion 1 


plt.hist(df.y, bins=10,
color="green",
histtype="bar",
rwidth= 0.25)

numbers = (31,10,85,25,4,83,32,43,66,18,93,6,42,27,21,42,53,32,85,32,42,58,67,17,4,5)
y_pos = np.arange(len(numbers))
performance = 3 + 10 * np.random.rand(len(numbers))
error = np.random.rand(len(numbers))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=numbers)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('frecuencia')
ax.set_title('Numbers today')

plt.show()