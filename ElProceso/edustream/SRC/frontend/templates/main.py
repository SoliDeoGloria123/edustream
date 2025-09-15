from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="../static"), name="static")
templates = Jinja2Templates(directory="public")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/registro")
async def registro(request: Request):
    return templates.TemplateResponse("registro.html", {"request": request})

@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

if __name__ == "__main__":
    print("🚀 Iniciando servidor en http://localhost:8001")
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)