from app.service.init_AI import client
from app.service.promt import STUDY_ASSISTANT_PROMPT


def send_message(user_message: str) -> str:
    """
    Envía un mensaje del usuario al modelo de Groq y retorna la respuesta completa.

    Args:
        user_message: El texto enviado por el usuario desde el endpoint.

    Returns:
        La respuesta generada por el modelo como string.
    """
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": STUDY_ASSISTANT_PROMPT
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        temperature=0.7,
        max_completion_tokens=2048,
        top_p=1,
        stream=False,
        stop=None
    )

    return completion.choices[0].message.content
