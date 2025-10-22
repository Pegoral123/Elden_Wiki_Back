# firebase_config.py
import os
from firebase_admin import credentials, initialize_app, auth
from dotenv import load_dotenv

load_dotenv()

SERVICE_ACCOUNT_PATH = os.path.join(os.path.dirname(__file__), "data", "serviceAccountKey.json")

def init_firebase():
    # inicializa apenas uma vez
    try:
        cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
        initialize_app(cred)
        print("Firebase Admin inicializado")
    except Exception as e:
        # em dev pode imprimir; em produção usar logging
        print("Erro ao inicializar Firebase Admin:", e)

def create_user(email: str, password: str):
    return auth.create_user(email=email, password=password)

def verify_id_token(id_token: str):
    return auth.verify_id_token(id_token)