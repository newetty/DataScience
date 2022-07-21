from operator import invert


1) Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"


def función inversa(palabra):

    rev = []
	letras = list(palabra)
	for i in range(len(letras)-1, -1, -1):
		rev.append(letras[i])

	cadena = "".join(rev)
	print "Del revés: ",cadena

    


2) Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen 
el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True.

3) Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 
1 miembro en común o devuelva 
False de lo contrario. Escribir la función usando el bucle for anidado.


