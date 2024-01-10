from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
#import requests

# activar entorno: venv\Scripts\activate.bat

app = FastAPI()

templates = Jinja2Templates(directory="frontend/templates")
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Inicio de pagina
# @app.get("/")
# def index():
#     return 'hello'

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )
# @app.get("/obtenerdatos")
# async def obtenerdatos():
#     url_django = 
#     response = requests.get(url_django)
#     datos_django = response.json()
#     return datos_django
# @app.get("/get_json") 
# async def enviar_json():
#     data = {
#         "map_type": 2,
#     }
#     url_django = "http://127.0.0.1:8000/api/set_map_type/"
#     response = requests.post(url_django, json=data)

#     if response.status_code == 200:
#         return{"mensaje": "XDDDDDDD"}
#     else:
#         return{"mensaje": ":("}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9090)
