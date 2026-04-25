from pydantic import BaseModel


class user_login(BaseModel):
    username: str
    contrasena: str

class user_register(BaseModel):
    username: str
    email: str
    tipo_usuario: str
    contrasena: str


class ChatRequest(BaseModel):
    message: str


