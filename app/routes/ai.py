from fastapi import APIRouter, HTTPException, Body, UploadFile, File
from app.models.models import ChatRequest
from app.service.message import send_message
from app.utils.ocr import procesar_imagen_chat

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


@router.post("/chat/image")
async def chat_image(message: str = Body(...), file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        text_ocr = procesar_imagen_chat(image_bytes)
        response = send_message(message + "\n\nContenido extraído de la imagen: \n\n" + text_ocr)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el mensaje: {str(e)}")