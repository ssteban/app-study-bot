from fastapi import APIRouter, HTTPException
from app.models.models import ChatRequest
from app.service.message import send_message

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío")

    try:
        response = send_message(request.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el mensaje: {str(e)}")
