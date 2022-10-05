from fastapi import FastAPI, status, HTTPException
import pandas as pd 
import json
import csv
import os
from pydantic import BaseModel


# Creamos nuestra primera aplicación FastAPI:
app = FastAPI()

# doy la ruta donde se encuentra el dataset:
#MEDIA_ROOT = "iris.csv"
MEDIA_ROOT = "/home/isabel/FEI_projects/DataScience/media/iris.csv"

#Método GET a la url "/test/"
# llamaremos a nuestra aplicación (<app name> + <método permitido>)
@app.get("/test/")
async def test_1():
    return "Bienvenido a FastAPI"




