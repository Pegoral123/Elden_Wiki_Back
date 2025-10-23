
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from routes import auth, bosses, locations


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(locations.router)
app.include_router(bosses.router)
app.include_router(auth.router)

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




