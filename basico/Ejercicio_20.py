"""1 Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo:
generar_n_caracteres(5, "x") debería devolver "xxxxx" """

def generar_n_caracteres(s, letra):
    return s*letra

#s = int(input("Ingrese numero:"))
#letra = (input("Ingrese letra"))


#Desconectar para ejecutar
#print (generar_n_caracteres (s, letra))#

"""2) 2) Definir un diagrama procedimiento() que tome una lista de números enteros e imprima un diagrama en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:"""

def procedimiento (lista): #llamamento para la lista
    for i in lista:
        print(i * "x")
#Desconectar para ejecutar
#procedimiento([4,7,9])

"""3) Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga."""
def mas_larga(lista):
    mas_larga = ""
    for i in lista:
        if len(i)>len(mas_larga):
            mas_larga = i 
    return mas_larga
#Desconetar para ejecutar#
#print(mas_larga(["coche", "tortuga", "bici"]))#

"""4) Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n
caracteres."""

def filtras_palabras(lista,n):
    for i in lista:
        if len(i)>n:
            print(i)
#Deconectar para ejecutar
#filtras_palabras(["coche", "limpiar", "musica"], 4)

"""6) Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20."""

def mayores_vinte(tupla):
    cont = 0
    for i in tupla:
        if i > 20:
            cont += 1
        
#print("son", cont, "las personas con mas de 20 años")
#Desconecctar para ejecutar
#mayores_vinte((18,27,32,45,56,78,88,9,10,12))

or

def mayores(tup):
    cont = 0
for i in tup:
    if i > 20:
        cont += 1
print("Hay", cont, "numeros mayores a 20")
mayores ((15, 20, 16, 31, 40, 50, 11, 13, 48, 60))