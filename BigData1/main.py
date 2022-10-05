from fastapi import FastAPI, status, HTTPException
import pandas as pd 
import json
import csv
import os
from pydantic import BaseModel


# Creamos nuestra primera aplicación FastAPI:
#app = FastAPI()

# doy la ruta donde se encuentra el dataset:
#MEDIA_ROOT = "iris.csv"

 MEDIA_ROOT = "/ettyqueiroz/Documentos/Datascience/iris.csv"

#Método GET a la url "/test/"
# llamaremos a nuestra aplicación (<app name> + <método permitido>)
@app.get("/test/")
async def test_1():
  #return "Bienvenido a FastAPI"
  # @app.get("/iris/")
  async def iris(response: Response):
    try:
        # Crear el dataframe con la información de iris
        # df = pd.read_csv(MEDIA_ROOT)
        #print(df)
        # lo transformamos a json para poder gestionarlo desde el front:
        data = df.to_json(orient="index")
        # cargar la información con formato Json:
        data = json.loads(data)
       # return data
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        #return "404 NOT FOUND"

