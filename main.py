from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import requests
import re

# activar entorno: venv\Scripts\activate.bat

app = FastAPI()

#ruta para manejar plantillas
templates = Jinja2Templates(directory="frontend/templates")
#ruta para subir los css, img 
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

#inicio pagina de botones
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

#funcion para limpiar los datos
def names_clean(json_data):
    for item in json_data:
        name = item["name"]
        words = name.split('_')[0]
        item["name"] = words.capitalize()
    return json_data

#nueva pagina de botones 
@app.get("/botones", response_class=HTMLResponse)
async def obtenerdatos(request: Request):
    url_django = 'http://192.168.31.120:8500/what_map/'
    response = requests.get(url_django) #obtiene los datos
    datos_django = names_clean(response.json()) #limpia los datos
    return templates.TemplateResponse("botones.html", {"request": request, "datos_django": datos_django})


@app.get("/test/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="hola.html"
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9090)
