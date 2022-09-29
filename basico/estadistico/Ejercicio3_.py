# EJERCICIO 1

"""
    En 2007-2008, la altura promedio de un jugador de baloncesto profesional fue de 2,00 metros 
    con una desviación estándar de 0,02 metros. 
    Harrison Barnes es un jugador de baloncesto que mide 2,03 metros. ¿Qué porcentaje de jugadores 
    son más altos que Barnes?
"""

µ = 2
s = 0.02 
x = 2.03

def Zscore( µ, s, x):
    return round((x - µ )/ s,2)

#print(Zscore (2, 0.02,2.03))

# Nos vamos a la tabla y cojemos la probailidad para 1,5 = 0,9332 = 93,32% mas altos que Barney

Zscore= 1,5
masaltos= (1 - 0.9332)*100

#print(masaltos) 



µ = 0,78
s = 0.08
x = 3.0

Z = 2.3 


def altura_barney(Zscore, s, μ):
    return (Zscore * s) + μ
#print(altura_barney)

# EJERCICIO 2

# Chris Paul mide 1,83 metros. ¿Qué proporción de jugadores de baloncesto se encuentran entre las alturas de Paul y Barnes?



µ = 2
s = 0.02 
x = 1.83

def Zscore( µ, s, x):
    return round((x - µ )/ s , 2)

#print (Zscore (2, 0.02,1.83))

#el valor es -8,5 corresponde al 0% porque Z es < -4 por lo tanto es un outlier el 93% esta entre ellos 

#Ejercicio 3 
"""
    El 92 % de los candidatos obtuvo una puntuación tan buena o peor que la de Steve.
    Si el puntuación promedio fue 55 con una desviación estándar de 6 puntos, ¿cuál fue el puntuación de Steve?
"""

µ = 55
s = 6
porcentaje = 0,92

#sabiendo el porcentaje podemos saber la z 

Zscore = 1.41

def puntos_Steve(Zscore, s, μ):
    return (Zscore * s) + μ

print("Los puntos de Steve son:", puntos_Steve((Zscore, s, μ)))