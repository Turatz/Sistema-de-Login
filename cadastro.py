from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.post("/cadastro")
def cadastro(usuario: str, senha: str):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT,
        senha TEXT
    )
    """)

    # verifica se ja existe
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))
    if cursor.fetchone():
        conn.close()
        return {"msg": "usuario ja existe"}

    cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))

    conn.commit()
    conn.close()

    return {"msg": "cadastrado"}
