
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from routes import auth, bosses, locations


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")



app.include_router(locations.router)
app.include_router(bosses.router)
app.include_router(auth.router)

origins = [
    "http://localhost:5173",  # A origem do seu app Vue
    "http://127.0.0.1:5173", 
    "http://localhost:8080",# Adicione variações se necessário
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*", "Authorization"],
)

@app.get("/")
def raiz_root():
    return {"Bem-vindo à ELDEN WIKI!"}




