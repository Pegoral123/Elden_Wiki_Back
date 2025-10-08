from fastapi import APIRouter, HTTPException
import requests  # Corrigido: Importação do módulo requests

router = APIRouter(prefix="/bosses", tags=["Bosses"])

@router.get("/")
def get_bosses():
    url = "https://eldenring.fanapis.com/api/bosses"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        data = resposta.json()
        return data
    else:
        raise HTTPException(status_code=500, detail="Erro ao buscar os dados dos bosses")  

@router.get("/{boss_name}")
def get_boss_by_name(boss_name: str):
    bosses = [
        {
            "id": 1,
            "name": "Margit, o Caído",
            "location": "Castelo Stormveil, Limgrave",
            "description": (
                "Margit é um chefe opcional que serve como guardião da entrada do Castelo Stormveil. "
                "Ele é um inimigo formidável que testa as habilidades dos jogadores logo no início do jogo."
            ),
            "Saúde": 4174,
            "Defesa": 103,
            "Postura": 80,
            "Resistencia": "Dano Sagrado",
            "Fraqueza": "Corte",
            "Recompensa": "Bolsa de Talismã"
            
        },
        {
            "id": 2,
            "name": "Godrick, o Enxertado",
            "location": "Castelo Stormveil, Limgrave",
            "description": (
                "Godrick é o primeiro grande chefe do jogo e um dos portadores de Grandes Runas. "
                "Ele é um descendente degenerado da linhagem dourada de Marika, obcecado por poder a ponto de enxertar membros de outros guerreiros em si mesmo."
            ),
            "Saúde": 6.080,
            "Defesa": 105,
            "Postura": 105,
            "Resistencia": "Dano Sagrado",
            "Fraqueza": "Padrão, Corte, Golpear e Perfurar",
            "Recompensa": "A Grande Runa de Godrick"
        },
        {
            "id": 3,
            "name": "Radahn, o Flagelo Estelar",
            "location": "Caelid",
            "description": (
                "Radahn é um dos mais poderosos e temidos chefes de Elden Ring, conhecido por sua habilidade em combate "
                "e por ser um dos portadores de Grandes Runas."
            ),
            "Saúde": 9.572,
            "Defesa": 113,
            "Postura": 200,
            "Resistencia": "Dano Sagrado, Dormir",
            "Fraqueza": "Perfurar, Podridão Escarlate",
            "Recompensa": "A Grande Runa de Radahn"
        },
    ]

    for boss in bosses:
        if boss["name"].lower() == boss_name.lower() or str(boss["id"]) == boss_name:
            return boss

    # Retorna um erro 404 se o boss não for encontrado
    raise HTTPException(status_code=404, detail="Boss não encontrado")