"""Crearemos un nuevo tipo llamado NumeroComplejo. Este tipo tiene un atributo x 
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
print(l.x)


"""2 Ahora defina dentro de la clase NumeroComplejo un función imprimir donde muestre los 
valores de x e y."""


class Numero_Complejo:
   
    def __init__(self, _x, _y): # iniciamos los objetos #se usa self
        
        self.x = _x
        self.y = _y

def imprimir(self):
    print("El valor de x es: " + str(self.x))
    print("El valor de y es: " + str(self.y))

numeros=Numero_Complejo(12,89)
numeros.imprimir()