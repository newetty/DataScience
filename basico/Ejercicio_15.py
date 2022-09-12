#1- Crea una lista de nombre "concursantes" que contenga los seguientes valores: "Juan", "Pedro", "Andrea", "Luis",
#"Lara", "Jose", "Estefania" ##

concursantes = ["Juan", "Pedro", "Andrea", "Luis", "Lara", "Jose", "Estefania"]


#2- Crea una lisa de nombre "resultados" que contenga los seguintes valores: 20, 30, 50, 20, 10, 5, 60, 40 #

resultados = [20, 30, 50, 20, 10, 5, 60, 40]

#3- Crea un dicionario con los concursantes y los resultados#

data = {"Concursantes": concursantes; "Resultados" : resultados}

data2 = dict(zip(concursante, resultados))
data2

#3 Crea un dataframe vacio y apendiza los concursantes y los resultados mediante el empleo de un bucle for#

df = pd.DataFrame(data, columns= ["Concursante", "Resultados"])

df.nuevo = []
for elemento in data.items():
    df.append(elemento)
df
