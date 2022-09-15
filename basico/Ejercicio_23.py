
"""1) Desarrolla el siguiente ejercicios de POO: Alumnos -> Es la clase. init -> Es el método init
#nombre, edad, asignatura y nota son las propiedades Instanciamos.los posibles alumnos (alumno1, alumno2, alumno3..) --> son los "objetos"
#y el.init los inicializa """  




class Alumnos:

    def __init__(self, nombre, edad, asignatura, nota):
        self.nombre = nombre
        self.edad = edad
        self.asignatura = asignatura
        self.nota = nota


#"""A continuación muestra la edad del alumno 2 y el alumno 3 y sus notas"""


alumno1 = Alumnos("Juan", 30, "matematica", "A")
alumno2 = Alumnos("María", 45, "ciencias", "B")
alumno3 = Alumnos("Carlos", 25, "geografia", "C")

print(alumno2.edad)
print(alumno3.edad)
print(alumno1.nota)
print(alumno2.nota)
print(alumno3.nota)

"""2) Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha
 cumplido (desde 1 hasta su edad)."""
def edad():
    age = int(input("¿Cuántos años tienes? "))#for i in range(age):
   # print("Cumples " + str(i+1) + " años")

#""Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida
#empezando por la última""

#palabra =(input('¿Cual es la palabra?  '))

#if palabra in range(palabra [0, -1, -1]):
   # print('palabra')


#5) Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la
#extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este
#formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.""
#xxx- 
#numero_telefono = int(input("¿Cual es el numero_telefono #xx-xxxxxxxxx-xx?"))
#print('Su umero de telefono' [4:-3])



#6) Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma
#rase pero con la vocal introducida en mayúscula.
def frase():
    frase = input("Ingrese una frase: ")
    vocal = input("Ingrese una vocal minuscula: ")

#print(frase.replace(vocal, vocal.upper()))

 # 4Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número
#de euros y el número de céntimos del precio introducido.#

    def string():
    
    string = input(" Nombre y apellido: ")

 
    i=1
    while i<= 3:
        print(string)
    i+=1

#print("en minusculas: " + nombre.capitalize())
#print("Primeras letras mayusculas: " + nombre.title())
#print("en mayusculas: " + nombre.upper())

#7) Escribir un programa que pregunte por consola el precio de un producto en euros 
# con dos decimales y muestre por pantalla el número
#de euros y el número de céntimos del precio introducido.

def precio_euros ():
    pass

    precio = input("¿Cual es el precio en euros con dos decimales?")


 parte_entero =  (precio[:precio.find('.')] )

    parte_decimal = (precio[precio.find('.')+1:])

    #print("el total es: " + entero + " con: " + decimal + " centavos")")