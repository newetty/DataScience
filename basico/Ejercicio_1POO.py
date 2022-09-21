
"""1) Crea el siguiente programa: Una clase de nombre Librería,
Inicia los siguientes atributos: nombre, sección, editorial y año
    Crea una segunda clase con nombre Rosalia que herede la clase librería,
    En esta clase Rosalia, crea una función \"result\" cuyo resultado sea los 
    datos de los libros, declara los Objetos siguientes:
libro1 --> Oceanarium, Ciencia, Impedimenta, 2021),
libro2 --> 33 Botones, Novela negra, Atlantis, 2022
libro3 --> Venganza en Compostela, Historia, Universo de letras, 2022"""
  


from typing_extensions import Self


class Libreria:
    def __init__(self, nombre, sección, editorial,año):
        self.nombre =nombre
        self.sección =sección
        self.editorial = editorial
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

#print(libro1.imprimir())
#print((libro2.imprimir()))
print((libro3.imprimir()))

"""2) Crea otra libraría de nombre MiLibro, que corresponde a una nueva clase, define una función de nombre misLibros,
 cuyo resultado sea los datos de los libros:
 libro4 --> Mi primera Novela, Novela, Bruño, 2019 
 libro5 --> Gatos, Literatura, Listado, 2018 """


 """class  MiLibro:
    def mislibros(self):
       print()
libro4 = MiLibro ("Mi primera Novela", "Novela", "Bruño", 2019)
libro5 = Milibro("Gatos", "literatura","Listado", 2018)"""


"""Realiza la media de los años de los libros 4 y 5"""

#def media (lista):
   # return sum(lista)/len(lista)##

"""3) Crea una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.
mostrar(): Muestra los datos de la persona.
esMayorDeEdad(): Devuelve un valor indicando si es mayor de edad."""

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
    def mostrar(self):
        return f"El usuario  {self.nombre}  que tiene de edad {self.edad} con dni {self.dni}"
    def esMayorDeEdad(self):
        return self.edad >= 18
    

persona1= Persona("Juan Garcias", 65, "457778999-T")
persona2= Persona("Luis Guerra", 45, "38999000-p")
    
    

"""4) Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular 
(que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad 
es opcional. Construye los siguientes métodos para la clase:
class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad =cantidad
        
    def metodo_constructor(self):
        print("los datos pueden estar vacios", self.titular)
        print("los datos puede estar vacios",self.cantidad)
    def ingresar(self, ingreso):
        if ingreso>0:
            self.cantidad = self.cantidad + ingreso #se le añade la cantidad
        
    def retirada(self,retirada):  
        if retirada>0:
            self.cantidad = self. cantidad - ingreso
        if self.cantidad<0:
            return f"ATENCIO la cuenta esta en numeros rojos: {self.cantidad}"
        
titular1 = Cuenta("José Luis")

titular1.Cuenta
Un constructor, donde los datos pueden estar vacíos.
El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
 rojos si es saldo negativo.
"""
class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad =cantidad
    
    def metodo_constructor(self):
        print("Titular de la cuenta:", self.titular)
        print("los datos puede estar vacios",self.cantidad)

    def ingresar(self, ingreso):
        if ingreso>0:
            self.cantidad = self.cantidad + ingreso #se le añade la cantidad
        
    def retirada(self,retirada):  
        if retirada>0:
            self.cantidad = self. cantidad - ingreso
        if self.cantidad<0:
            return f"ATENCIO la cuenta esta en numeros rojos: {self.cantidad}"
        
titular1= Cuenta("José Luis")

titular1.metodo_constructor(40)

titular1.ingresar(40)

titular1.retirada(-10)
titular1.metodo_constructor()











"""5) Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva 
clase CuantaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además 
del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto 
por ciento.Construye los siguientes métodos para la clase:""

Un constructor.
En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
Además la retirada de dinero sólo se podrá hacer si el titular es válido.
El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
Piensa los métodos heredados de la clase madre que hay que reescribir."""

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificación=0, edad):
        super().__init__{titular, cantidad}
        self.bonificación = bonificación
        self.edad=edad
     def metodo_constructor(self):
        print("Titular de la cuenta:", self.titular)
        print("los datos puede estar vacios",self.cantidad)
   
    def metodo_esTitularValido(CuentaJoven):
        if self.edad > 25 == True:
            
            print(self.edad, "Es mayor que 25 años")
        
        else:
            
            print(self.edad, "Es menos que 25 años")


    elif cantidad > 0:
super().retirar(cantidad)

titular2 = CuentaJoven("Pedro Alonso", 30)
titular3 = CuentaJoven("Lorena García", 20, 200, 5)

titular2.metodo_constructor()
titular2.ingresar(100)
titular2.metodo_constructor()
titular3.ingresar(1000)
titular3.metodo_constructor()
