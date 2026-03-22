from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.post("/login")
def login(usuario: str, senha: str):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))

    user = cursor.fetchone()
    conn.close()

    if user:
        return {"msg": "login ok"}

    return {"msg": "usuario ou senha errados"}
