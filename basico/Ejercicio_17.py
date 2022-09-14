#Ejercicio 1
#Crea la clase "matematicas" y dentro de esa clase crea las funciones suma y resta, en dichas funciones nos deberán devolver el resultado
#de la suma y de la resta, siguiendo los siguientes pasos#:  matematicas:

class Matematicas:
    
    def funcion_suma(x):
        y = x + 17
        return y 
    def funcion_resta(x):
        y = x - 10
        return y

print ("Estamos dentro de la clase de matematicas")    
print("Suma 5:", Matematicas.funcion_suma(10)) 
print("Suma 5:", Matematicas.funcion_resta(10)) 
    Matematicas.funcion_resta(9)


#Ejercicio 2

#Crea dos clases una llamala "libros" y otra clase "materias". A la clase libros declara una función con nombre "tipos" y dentro de clase materias declara una función con nombre "asignaturas". A la función tipos retorne el valor name = "Data Science" y la función asignaturas retorne nombre = "Big Data"


class libros:
    def funcion_tipos():
        name = "Data Science"
        return (name)

class materias(libros):
    def funcion_asignatura():
        nombre = "Big Data"
        return(nombre)

print("Resultados de clase libro, funcion tipos: " , libros.funcion_tipos())


print("Resultados de clase libro, funcion tipos: " , libros.funcion_asignatura())
