## main.py del Frontend
from fastapi import FastAPI, Request 
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="../static"), name="static")
templates = Jinja2Templates(directory="public")
temp = Jinja2Templates(directory="private")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/registro")
async def registro(request: Request):
    return templates.TemplateResponse("registro.html", {"request": request})

@app.post("/registro")
async def registro_post(request: Request):
    return templates.TemplateResponse("registro.html", {"request": request})

@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/dashboard-estudiante")
async def dashboard_student(request: Request):
    return temp.TemplateResponse("student/dashboard.student.html", {"request": request, "panel": request.query_params.get("panel", "inicio"), "user": {"username": "Student"}})

@app.get("/dashboard-estudiante")
async def dashboard_student_post(request: Request):
    return temp.TemplateResponse("student/dashboard.student.html", {"request": request, "panel": request.query_params.get("panel", "inicio"), "user": {"username": "Student"}})

@app.get("/logout")
async def logout(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/dashboard")
async def dashboard_admin(request: Request):
    return temp.TemplateResponse("admin/dashboard.admin.html", {"request": request, "panel": request.query_params.get("panel", "inicio"), "user": {"username": "Admin"}})


if __name__ == "__main__":
    print("🚀 Iniciando servidor en http://localhost:8001")
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)