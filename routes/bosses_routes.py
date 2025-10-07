from fastapi import APIRouter
from fastapi import FastAPI, HTTPException

router = APIRouter(prefix="/bosses", tags=["Bosses"])

@router.get("/bosses")
def get_bosses():
    url = "https://eldenring.fanapis.com/api/bosses"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        data = resposta.json()
        return data
    else:
        return {"erro": "ao buscar os dados dos bosses"}
    
@router.get("/bosses/{boss_name}")
def get_boss_by_name(boss_name: str):
    bosses = [
        {
            "id": 1,
            "name": "Margit, o Caído",
            "location": "Castelo Stormveil, Limgrave",
            "description": "Margit é um chefe opcional que serve como guardião da entrada do Castelo Stormveil. Ele é um inimigo formidável que testa as habilidades dos jogadores logo no início do jogo.",
        },
        {
            "id": 2,
            "name": "Godrick, o Enxertado",
            "location": "Castelo Stormveil, Limgrave",
            "description": "Godrick é o primeiro grande chefe do jogo e um dos portadores de Grandes Runas. Ele é um descendente degenerado da linhagem dourada de Marika, obcecado por poder a ponto de enxertar membros de outros guerreiros em si mesmo.",
        },
        {
            "id": 3,
            "name": "Radahn, o Flagelo Estelar",
            "location": "Caelid",
            "description": "Radahn é um dos mais poderosos e temidos chefes de Elden Ring, conhecido por sua habilidade em combate e por ser um dos portadores de Grandes Runas.",
        },
    ]

    for boss in bosses:
        if boss["name"].lower() == boss_name.lower() or str(boss["id"]) == boss_name:
            return boss

    # Retorna um erro 404 se o boss não for encontrado
    raise HTTPException(status_code=404, detail="Boss não encontrado")