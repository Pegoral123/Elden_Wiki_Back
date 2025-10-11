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

@router.get("/limgrave_boss")
def get_limgrave_boss():
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
            "Recompensa": "Bolsa de Talismã",
            "image": "http://localhost:8000/static/margit_foto.jpg"
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
            "Recompensa": "A Grande Runa de Godrick",
            "image": "http://localhost:8000/static/godrick_foto.jpg" 
        },
        
    ]
    if not bosses:
        raise HTTPException(status_code=404, detail="Nenhum boss encontrado em Limgrave")
    return bosses


@router.get("/caelid_boss")
def get_caelid_boss():
    bosses = [
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
    return bosses

