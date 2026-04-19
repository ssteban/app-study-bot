from fastapi import APIRouter, HTTPException
from app.db.query import user_query
from app.models.models import user_login, user_register
import bcrypt


router = APIRouter()


# Inicio de sesión de usuario
@router.post("/login")
def login(user: user_login):
    query = user_query()
    try:
        result = query.login(user.username, user.contrasena)
    finally:
        query.close()
    if result:
        return {"status": "ok", "message": "Login exitoso"}
    raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")


# Registro de cuenta del usuario
@router.post("/register")
def register(user: user_register):
    query = user_query()
    try:
        password_hash = bcrypt.hashpw(user.contrasena.encode('utf-8'), bcrypt.gensalt())
        result = query.register(user.username, user.email, user.tipo_usuario, password_hash)
    finally:
        query.close()
    if result:
        return {"status": "ok", "message": "Registro exitoso"}
    raise HTTPException(status_code=500, detail="Error al registrar el usuario")