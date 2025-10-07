import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import locais_routes, bosses_routes


app = FastAPI()

app.include_router(locais_routes.router)
app.include_router(bosses_routes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou especifique ["http://localhost:8080"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def raiz_root():
    return {"Bem-vindo à ELDEN WIKI!"}




