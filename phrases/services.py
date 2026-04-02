from google.cloud import translate_v2 as translate

def translate_text(texto_esp):
    try:
        translate_client = translate.Client()
        return translate_client.translate(
            values = texto_esp,
            target_language="ja",
            source_language="es"
        )['translatedText']

    except Exception as e:
        print("Error en traducción:", e)
        return None