# EJERCICIO 1

# Calcula la Z score para los siguientes casos:

# 1) µ = 54, s= 12, x = 68

def Zscore( µ, s, x):
    return round((x - µ )/ s)
µ  = 54 
s= 12
x = 68

#print(Zscore)



# 2) µ= 25, s = 3.5, x = 20

µ  = 25
s= 3.5
x = 20
Zscore = round((20-25)/3.5, 2)

#print(Zscore(µ, s, x))

# 3) µ = 0.01, s = 0.002, x = 0.01
Zscore = round((0.01-0.01)/0.002, 2)
#print (Zscore)

# EJERCICIO 2

"""
    El GPA promedio de los estudiantes en una escuela de secundaria local es 3.2 con una desviación estándar de 0.3.
    Jenny tiene GPA de 2.8 ¿A cuántas desviaciones estándar de la media está el GPA de Jenny?
"""
µ = 3.2
s = 0.3
x = 2.8 

#print("GPA de Jenny:", (Zscore(3.2, 0.3,2.8))



# EJERCICIO 3

"""
    Jenny está tratando de demostrarles a sus padres que le va mejor en la escuela que a su prima.
    Su prima asiste a una escuela de secundaria diferente donde el GPA promedio es 3.4 con una desviación estándar de 0.2.
    El prima de Jenny tiene un GPA de 3.0.¿se está desempeñando Jenny mejor que su prima según los puntajes estándar?
"""
µ = 3.4
s = 0.3
x = 3.0


#print("GPA de prima:", (Zscore(µ, s, x))

# EJERCICIO 4

"""
    La puntuación de Kyle en una prueba de matemáticas reciente fue de 2.3 desviaciones estándar de la 
    puntuación media del 78%.
    Si la desviación estándar de los puntajes de la prueba fue del 8%. ¿Qué puntaje obtuvo kyle en su prueba?
"""
µ = 0,78
s = 0.08
x = 3.0

Z = 2.3 
def calculo_x (Z, s, µ):
    return(Z * s) + µ