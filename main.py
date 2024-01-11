from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import requests
import re

# activar entorno: venv\Scripts\activate.bat

app = FastAPI()

templates = Jinja2Templates(directory="frontend/templates")
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/obtenerdatos")
async def obtenerdatos():
    url_django = 'http://192.168.31.120:8500/what_map/'
    response = requests.get(url_django)
    datos_django = response.json()
    return datos_django

#funcion para limpiar los datos
def names_clean(json_data):
    for item in json_data:
        name = item["name"]
        words = name.split('_')[0]
        item["name"] = words.capitalize()
    return json_data

@app.get("/f", response_class=HTMLResponse)
async def obtenerdatos(request: Request):
    url_django = 'http://192.168.31.120:8500/what_map/'
    response = requests.get(url_django) #obtiene los datos
    datos_django = names_clean(response.json()) #limpia los datos
    return templates.TemplateResponse("index2.html", {"request": request, "datos_django": datos_django})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9090)
