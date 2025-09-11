from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

def CORS(app: FastAPI) -> FastAPI:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
   )

CORS(app)