import easyocr
import logging

# Usamos únicamente Español e Inglés para maximizar la precisión y velocidad del modelo.
idiomas_comunes = ['es', 'en']

reader = easyocr.Reader(idiomas_comunes, gpu=False) 

def procesar_imagen_chat(ruta_imagen):
    try:
        # mag_ratio=1.5 hace un "upscale" de la imagen, mejorando mucho la lectura de textos pequeños o borrosos.
        result = reader.readtext(
            ruta_imagen, 
            mag_ratio=1.5,        # Aumenta el tamaño de la imagen temporalmente para mejor precisión
            text_threshold=0.6    # Ligeramente más permisivo con lo que considera "texto"
        )
        
        # Guardamos los textos cuya confianza sea mayor al 40%
        texto_final = " ".join([text for (bbox, text, confidence) in result if confidence > 0.40])
        return texto_final.lower()
    except Exception as e:
        logging.error(f"Error procesando imagen para OCR: {str(e)}")
        return ""
