
"""1) Crea el siguiente programa: Una clase de nombre Librería,
Inicia los siguientes atributos: nombre, sección, editorial y año
    Crea una segunda clase con nombre Rosalia que herede la clase librería,
    En esta clase Rosalia, crea una función \"result\" cuyo resultado sea los 
    datos de los libros, declara los Objetos siguientes:
libro1 --> Oceanarium, Ciencia, Impedimenta, 2021),
libro2 --> 33 Botones, Novela negra, Atlantis, 2022
libro3 --> Venganza en Compostela, Historia, Universo de letras, 2022"""
  


class Libreria:
    def __init__(self, nombre, sección, editorial,año):
        self.nombre =nombre
        self.sección =sección
        self.editorial= editorial
        self.año = año

class Rosalia(Libreria):
    def imprimir (self):

        print("el nombre del libro es:", self.nombre)
        print("la seccion del libro es:", self.sección)
        print("el editorial del libro es:", self.editorial)
        print("el año del libro es:", self.año)
        """nombredelaclase.nombredelafunicon"""
        
libro1 = Rosalia("Oceanarium", "Ciencia", "Impedimenta", 2021)
libro2 = Rosalia("Botones", "Novela negra" , "Atlantis", 2022 )
libro3 = Rosalia("Venganza Compostela", "Historia", "Universo letras", 2022)

print(libro1.imprimir())

"""2) Crea otra libraría de nombre MiLibro, que corresponde a una nueva clase, define una función de nombre misLibros,
 cuyo resultado sea los datos de los libros:
 libro4 --> Mi primera Novela, Novela, Bruño, 2019 
 libro5 --> Gatos, Literatura, Listado, 2018 """


"""class  MiLibro:
    def mislibros(self:
       # return 
#libro4 = MiLibro ("Mi primera Novela", "Novela", "Bruño", 2019)
libro5 = Milibro("Gatos", "literatura","Listado", 2018)"""


"""Realiza la media de los años de los libros 4 y 5"""

#def media (lista):
   # return sum(lista)/len(lista)##


"""5) Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva 
clase CuantaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además 
del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto 
por ciento.Construye los siguientes métodos para la clase:""

Un constructor.
En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
Además la retirada de dinero sólo se podrá hacer si el titular es válido.
El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
Piensa los métodos heredados de la clase madre que hay que reescribir."""

"""class CuentaJoven():
    def __init__(self, titular, cantidad, bonificación, edad):
        self.titular = titular
        self.cantidad = cantidad
        self.bonificación = bonificación
        self.edad=edad
   
    def metodo_esTitularValido(CuentaJoven):
        if self.edad > 25 == True:
            
            print( self.edad, "Es mayor que 25 años")
        
        else:
            
            print(self.edad, "Es menos que 25 años")
"""

     