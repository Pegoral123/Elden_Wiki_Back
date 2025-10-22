from fastapi import APIRouter, HTTPException
import requests  

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

        {
            "id": 3,
            "name": "Cavaleiro Cão de Caça Darriwil",
            "location": "Cão Desamparado Evergaol",
            "description": (
                "O Cavaleiro Cão de Caça é um chefe opcional em Elden Ring, mas bastante conhecido pelos novatos por dropar a arma Presa do Cão de Caça, uma das favoritas de muitos por sua versatilidade e excelente Cinza de Guerra. Ele também faz parte da linha de missões do Blaidd, então é recomendado falar com ele antes de enfrentar o chefe para receber sua ajuda na luta. "
            ),
            "Saúde": 1.450,
            "Defesa": 103.9,
            "Postura": 66,
            "Resistencia": "Ataque Padrão",
            "Fraqueza": "Raio",
            "Recompensa": "Presa do Cão de Caça",
            "image": "http://localhost:8000/static/caoCaca_foto.jpg"
        },
        
        
    ]
    if not bosses:
        raise HTTPException(status_code=404, detail="Nenhum boss encontrado em Limgrave")
    return bosses


@router.get("/caelid_boss")
def get_caelid_boss():
    bosses = [
        {
            "id": 1,
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
            "Recompensa": "A Grande Runa de Radahn",
            "image": "http://localhost:8000/static/radahn_foto.jpg"
        },
        {
            "id": 2,
            "name": "Comandante O'Neil",
            "location": "Pântano de Aeonia",
            "description": (
                "O Comandante O’Neil é um Grande Chefe Inimigo em Elden Ring, encontrado no coração da região tomada pela Podridão Escarlate."
            ),
            "Saúde": 9.210,
            "Defesa": 111,
            "Postura": 90,
            "Resistencia": "Barra, IMUNE A PODRIDÃO ESCARLATE",
            "Fraqueza": "Perfurar",
            "Recompensa": "Estandarte do comandate Agulha de ouro sem liga",
            "image": "http://localhost:8000/static/comandanteONeil_foto.jpg"
        },
        {
            "id": 3,
            "name": "Ekzykes em decomposição",
            "location": "Caelid Highway South",
            "description": (
                "Ekzykes, o Vingador da Comunhão do Dragão, é uma figura trágica e aterradora no mundo de Elden Ring. Antigo cavaleiro da Comunhão do Dragão, Ekzykes foi um dos poucos humanos que ousaram buscar o poder ancestral dos dragões antigos."
            ),
            "Saúde": 23.731,
            "Defesa": 114,
            "Postura": 120,
            "Resistencia": "Podridão Escarlate e Veneno",
            "Fraqueza": "Fraco para todos tipos de dano",
            "Recompensa": "Coração do Dragão",
            "image": "http://localhost:8000/static/ekzykes_foto.jpg"
        },
        
        
    ]
    return bosses

