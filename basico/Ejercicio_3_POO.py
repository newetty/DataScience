"""Escribir un programa que pregunte al usuario su edad y 
muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

from mailbox import NoSuchMailboxError

#desconectar para ejecutar#
#edad = int(input("Tu edad es?:"))
#for i in range(edad):
#    print("Has cumplido" + str(i+1) + "años")


"""""Desarrolla el siguiente ejercicios de POO:
Alumnos -> Es la clase.
init -> Es el método init
nombre, edad, asignatura y nota son las propiedades
Instanciamos..
los posibles alumnos (alumno1, alumno2, alumno3..) --> son los "objetos"
y el.init los inicializa"""

class Alumnos:
    
    def __init__(self, nombre, edad, asignatura, nota):
        self.nombre = nombre
        self.edad = edad
        self.asignatura = asignatura
        self.nota = nota


alumno1 = Alumnos("Joao", 67, "Fisica", 8)
alumno2 = Alumnos("Felipe", 37, "Mandarim" , 9)
alumno3 = Alumnos("Luana", 45, "Matematicas", 10)
alumno4 = Alumnos("Toni", 27, "Geografia", 5)

"""A continuación muestra la edad del alumno 2 y el alumno 3 y sus"""

print(alumno2.edad)
print(alumno2.edad)
