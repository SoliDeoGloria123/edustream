"""
Archivo índice de rutas existentes en la API
"""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from SRC.backend.routes.course_routes import router as course_routes
from SRC.backend.routes.lesson_routes import router as lesson_routes
from SRC.backend.routes.user_routes import router as user_routes

app = FastAPI()

# Manejo global de errores
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
	return JSONResponse(
		status_code=500,
		content={
			"success": False,
			"message": str(exc)
		}
	)

app.include_router(course_routes)
app.include_router(lesson_routes)
app.include_router(user_routes)
