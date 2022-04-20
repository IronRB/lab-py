from typing import Optional

from fastapi import FastAPI

import requests
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/countries")
def get_countries(pagination_size: int, pagination_key: int):
    API_url = "https://restcountries.com/v3.1/all"
    response = requests.get(API_url, verify=False)
    responseJSON = response.json()
    ordenado = sorted(responseJSON, key=lambda x: x["name"]["common"])
    return {"totalRegisters":len(responseJSON),
        "data": ordenado[slice(pagination_key, pagination_size,1)]
    }

@app.get("/countries/{item_id}")
def get_country(item_id: int):
    API_url = "https://restcountries.com/v3.1/all"
    response = requests.get(API_url, verify=False)
    responseJSON = response.json()
    ordenado = sorted(responseJSON, key=lambda x: x["name"]["common"])         
    return {"idRegisters":item_id,
        "data": ordenado[item_id]
    }    
 
