"""1 Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo:
generar_n_caracteres(5, "x") debería devolver "xxxxx" """

def generar_n_caracteres(s, letra):
    return s*letra

s = int(input("Ingrese numero:"))
letra = (input("Ingrese letra"))

print (generar_n_caracteres (s, letra))