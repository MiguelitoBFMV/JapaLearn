from google.cloud import translate_v2 as translate

def translate_text(texto_esp):

    translate_client = translate.Client()


    texto_jap = translate_client.translate(
        values = texto_esp,
        target_language="ja",
        source_language="es"
    )

    return texto_jap['translatedText']