from newspaper import Article
from gtts import gTTS


def texto_a_voz(url):
    try:
        articulo = Article(url, language="es")
        articulo.download()
        articulo.parse()

        titulo = articulo.title
        texto = articulo.text

        print(f"Título: {titulo}")
        print(f"Longitud del texto: {len(texto)} caracteres")

        if len(texto) < 100:
            print("❌ No se pudo obtener suficiente texto del artículo.")
            print("Prueba con otra URL más sencilla, como un blog o una noticia sin bloqueo.")
            return

        voz = gTTS(text=texto, lang="es")
        voz.save("articulo.mp3")

        print("✅ Archivo 'articulo.mp3' creado correctamente.")

    except Exception as error:
        print("❌ Ha ocurrido un error:")
        print(error)


def main():
    print("=== Conversor de artículos a voz ===")
    url = input("Introduce la URL del artículo: ")
    texto_a_voz(url)


if __name__ == "__main__":
    main()