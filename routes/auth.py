from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, EmailStr
import os
import requests
from dotenv import load_dotenv
from firebase_config import init_firebase, create_user, verify_id_token

load_dotenv()
API_KEY = os.getenv("FIREBASE_API_KEY")
init_firebase()

router = APIRouter(prefix="/auth", tags=["Auth"])

class RegisterModel(BaseModel):
    email: EmailStr
    password: str
    name: str

class LoginModel(BaseModel):
    email: EmailStr
    password: str

@router.post("/register")
def register(payload: RegisterModel):
    try:
        user = create_user(email=payload.email, display_name=payload.name, password=payload.password)
        login_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
        login_body = {
            "email": payload.email,
            "password": payload.password,
            "returnSecureToken": True
        }
        login_resp = requests.post(login_url, json=login_body)

        if login_resp.status_code != 200:
            raise HTTPException(status_code=401, detail=login_resp.json())

        token_data = login_resp.json()
        return {
            "uid": user.uid,
            "email": user.email,
            "name": user.display_name,
            "idToken": token_data.get("idToken"),
            "refreshToken": token_data.get("refreshToken"),
            "expiresIn": token_data.get("expiresIn")
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(payload: LoginModel):
    if not API_KEY:
        raise HTTPException(status_code=500, detail="FIREBASE_API_KEY não configurada")
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
    body = {"email": payload.email, "password": payload.password, "returnSecureToken": True}
    resp = requests.post(url, json=body)
    if resp.status_code != 200:
        raise HTTPException(status_code=401, detail=resp.json())
    return resp.json()  # contém idToken, refreshToken, expiresIn, localId (uid)

@router.post("/verify_token")
async def verify_token(request: Request):
    body = await request.json()
    id_token = body.get("idToken")
    if not id_token:
        raise HTTPException(status_code=400, detail="idToken ausente")
    try:
        decoded = verify_id_token(id_token)
        return {"uid": decoded.get("uid"), "email": decoded.get("email")}
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))