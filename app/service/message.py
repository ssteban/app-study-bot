from app.service.init_AI import client
from app.service.promt import STUDY_ASSISTANT_PROMPT
from app.utils.lang import get_response_language


def send_message(user_message: str) -> str:
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": STUDY_ASSISTANT_PROMPT + f"""

                    LANGUAGE RULE:
                    Reply only in {get_response_language(user_message)}.
                """
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        temperature=0.4,
        max_completion_tokens=2048,
        top_p=1,
        stream=False,
        stop=None
    )

    return completion.choices[0].message.content


