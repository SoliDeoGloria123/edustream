from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="public")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

if __name__ == "__main__":
    print("🚀 Iniciando servidor en http://localhost:8001")
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)