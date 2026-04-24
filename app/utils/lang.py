from langdetect import detect, LangDetectException

_COMMON_WORDS: dict[str, list[str]] = {
    "Spanish": [
        "hola", "buenas", "buenos días", "buenas tardes", "buenas noches",
        "¿cómo estás?", "como estas", "qué tal", "que tal", "gracias",
        "por favor", "sí", "no", "ayuda", "ayúdame", "ayudame",
        "necesito", "quiero", "tengo", "puedes", "dime", "explícame",
        "explícame", "explica", "muéstrame", "eres", "estoy",
    ],
    "English": [
        "hello", "hi", "hey", "good morning", "good afternoon", "good evening",
        "good night", "how are you", "thanks", "thank you", "please",
        "yes", "no", "help", "help me", "i need", "i want", "i have",
        "can you", "tell me", "explain", "show me", "you are", "i am",
    ],
    "French": [
        "bonjour", "salut", "bonsoir", "bonne nuit", "comment ça va",
        "merci", "s'il vous plaît", "oui", "non", "aide", "aidez-moi",
    ],
    "Portuguese": [
        "olá", "ola", "bom dia", "boa tarde", "boa noite",
        "como vai", "obrigado", "obrigada", "por favor", "sim", "não",
    ],
    "German": [
        "hallo", "guten morgen", "guten tag", "guten abend", "gute nacht",
        "wie geht es", "danke", "bitte", "ja", "nein",
    ],
    "Italian": [
        "ciao", "buongiorno", "buonasera", "buonanotte", "come stai",
        "grazie", "per favore", "sì", "no",
    ],
}

# Mapeo del código ISO de langdetect al nombre completo del idioma
_LANG_CODE_MAP: dict[str, str] = {
    "es": "Spanish",
    "en": "English",
    "fr": "French",
    "pt": "Portuguese",
    "de": "German",
    "it": "Italian",
    "nl": "Dutch",
    "ru": "Russian",
    "zh-cn": "Chinese (Simplified)",
    "zh-tw": "Chinese (Traditional)",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
}


def get_response_language(text: str) -> str:
    """
    Detecta el idioma del mensaje del usuario y devuelve su nombre completo.
    Prioridad:
      1. Petición explícita del usuario ("answer in English", "responde en español", etc.)
      2. Diccionario de palabras cortas comunes (evita errores de langdetect con textos cortos)
      3. langdetect como fallback para textos más largos
    """
    lower = text.strip().lower()

    # 1. Petición explícita del usuario
    explicit_map = {
        "Spanish":    ["in spanish", "en español", "en espanol"],
        "English":    ["in english", "en inglés", "en ingles"],
        "French":     ["in french", "en francés", "en frances", "en français"],
        "Portuguese": ["in portuguese", "en portugués"],
        "German":     ["in german", "en alemán", "en aleman", "auf deutsch"],
        "Italian":    ["in italian", "en italiano", "in italiano"],
    }
    for lang, phrases in explicit_map.items():
        if any(phrase in lower for phrase in phrases):
            return lang

    # 2. Diccionario de palabras cortas comunes
    for lang, words in _COMMON_WORDS.items():
        if any(lower == w or lower.startswith(w + " ") or lower.endswith(" " + w) for w in words):
            return lang

    # 3. langdetect como fallback (puede ser impreciso con textos muy cortos)
    try:
        code = detect(text)
        return _LANG_CODE_MAP.get(code, code)
    except LangDetectException:
        return "Spanish"  # Fallback seguro si la detección falla por completo
