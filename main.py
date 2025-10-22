
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from router import locais_router, bosses_router, data_router


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(locais_router.router)
app.include_router(bosses_router.router)
app.include_router(data_router.router)

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




