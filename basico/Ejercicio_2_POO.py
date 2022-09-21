"""1) Crearemos un nuevo tipo llamado NumeroComplejo. Este tipo tiene un atributo x 
para la coordenada en x e y para la coordenada en y. 
Representa un número complejo de la forma (x, y)."""

class Numero_Complejo:
   
    def __init__(self, _x, _y): # iniciamos los objetos #se usa self
        
        self.x = _x
        self.y = _y

def imprimir(self):
        print("Coordenadas:",self.x)
        print("Coordenadas:",self.y)

l = Numero_Complejo(3,6)
#Desconectar para ejecutar#
#print(l.x)


"""2 Ahora defina dentro de la clase NumeroComplejo un función imprimir donde muestre los 
valores de x e y."""


class Numero_Complejo:
   
    def __init__(self, _x, _y): # iniciamos los objetos #se usa self
        
        self.x = _x
        self.y = _y

    def imprimir(self):
        print("El valor de x es: " + str(self.x))
        print("El valor de y es: " + str(self.y))
#Desconectar para ejecutar
#numeros = Numero_Complejo(12,89)
#numeros.imprimir()

"""3) Define la función str para la clase NumeroComplejo para poder imprimir usando la función print
"""

# Las funciones que parten y terminan con __ son funciones reservadas.
# Existen varias además de __init__ y __st
class Numero_Complejo:
   
    def __init__(self, _x, _y): # iniciamos los objetos
        
        self.x = _x
        self.y = _y
    
    def imprimir(self):
        print("El valor de x es: " + str(self.x))
        print("El valor de y es: " + str(self.y))
    def __str__(self):
        
        l =  str(self.x) + "," + str(self.y)
        return l
#Desconectar para ejecutar      
#v = Numero_Complejo(6, 9)
#print(v)

"""4) definie una función que compara dos números complejos, ya que si dos objetos distintos 
tienen sus atributos iguales, no se consideran iguales."""

class Numero_Complejo:
   
    def __init__(self, _x, _y): # iniciamos los objetos
        
        self.x = _x
        self.y = _y
    
    def imprimir(self):
        print("El valor de x es: " + str(self.x))
        print("El valor de y es: " + str(self.y))
    def __str__(self):
        
        l =  str(self.x) + "," + str(self.y)
        return l
    
    def comparacion(self, otroO):
        if  self.x==otroO and self.y==otro:
            
            
            return True
        return False
        
        
v1 = Numero_Complejo(6, 9)
v2 = Numero_Complejo(6, 9)
#Desconectar para ejecutar
print(v1==v2)
print(v1.comparacion(v2))

"""5) Realiza un método que sume dos numeros complejos sin modificiar los objetos originales, 
ya que se retorna un nuevo numero NumeroComplejo."""

class Numero_Complejo:
   
    def __init__(self, _x, _y): # iniciamos los objetos
        
        self.x = _x
        self.y = _y
    
    def imprimir(self):
        print("El valor de x es: " + str(self.x))
        print("El valor de y es: " + str(self.y))
    def __str__(self):
        
        l =  str(self.x) + "," + str(self.y)
        return l
    
    def comparacion(self, numeroraro):
        if  self.x==numeroraro.x and self.y==numeroraro.y:
            
            
            return True
        return False
    
    def sumar_Numero_Complejo(self,numeroraro):
        a = self.x + numeroraro.x
        b = self.y + numeroraro.y
        return Numero_Complejo(a,b)

v1 = Numero_Complejo(6, 9)
v2 = Numero_Complejo(6, 7)
#Desconectar par ejecutar

##print(v1==v2)
#print(v1.comparacion(v2))
#l = v1.sumar_Numero_Complejo(v2)
#print(l)

"""6) Crea una clase persona. Sus atributos deben ser su nombre y su edad. Además crea un método cumpleaños, 
que aumente en 1 la edad de la persona."""

class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def aumenta_cumpleanhos(self):
        self.edad += 1
        
    
##Desconectar para ejecutar
#p = Persona("Jose", 10)
#p.aumenta_cumpleanhos()
#print(p.edad)

"""7) Para la clase anterior definir el método str. Debe retornar al menos el nombre de la persona."""

class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def aumenta_cumpleanhos(self):
        self.edad += 1
#Desconectar para ejecutar
#p = Persona("Jose", 10)
#p.aumenta_cumpleanhos()
#print(p.edad)

"""8) Extender la clase persona agregando un atributo saldo y un método transferencia(self, persona2, monto).
 El saldo representa el dinero que tiene la persona. El método transferencia hace que la Persona que llama 
 el método le transfiera la cantidad monto al objeto persona2. 
Si no tiene el dinero suficiente no se ejecuta la acción."""
class Persona:
    
    def __init__(self, nombre, edad, saldo, monto):
        self.nombre = nombre
        self.edad = edad
        self.monto = monto
        self.saldo = saldo

    def aumenta_cumpleanhos(self):
        self.edad += 1

    #p = Persona("Jose", 10, 8)
    #p.aumenta_cumpleanhos()
    #print(p.edad)
    
    def metodo_transferir(self, persona2, monto):

        if self.saldo>=monto:
            persona2.saldo -= monto
            print("transfere el monto")
        else:
            print("No se transfere el monto")

    def __str__(self):

        return "Persona: " + self.nombre

p = Persona("Sandra", 10, 30,9)
p2 = Persona("D.Joana", 20, 80,80)
#p2.metodo_transfererir(p, 7) # No acepta
p2.metodo_transferir(p, 70)
print("Saldo de p2: ")
print(p2.saldo)
print("Saldo de p1: ")
print(p.saldo)

    