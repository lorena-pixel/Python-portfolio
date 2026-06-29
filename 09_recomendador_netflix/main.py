import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

RUTA_CSV = "data/netflix_titles.csv"


def cargar_datos():
    try:
        return pd.read_csv(RUTA_CSV)
    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
        print("Asegúrate de que está en: data/netflix_titles.csv")
        return None


def limpiar_datos(datos):
    columnas = [
        "Title",
        "Director",
        "Cast",
        "Production Country",
        "Genres",
        "Description"
    ]

    for columna in columnas:
        datos[columna] = datos[columna].fillna("")

    datos["caracteristicas"] = (
        datos["Director"] + " " +
        datos["Cast"] + " " +
        datos["Production Country"] + " " +
        datos["Genres"] + " " +
        datos["Description"]
    )

    return datos


def recomendar(titulo, datos):
    titulo = titulo.lower().strip()

    datos["title_lower"] = datos["Title"].str.lower()

    # Buscar coincidencia exacta
    if titulo in datos["title_lower"].values:

        indice = datos[datos["title_lower"] == titulo].index[0]

        vectorizador = CountVectorizer(stop_words="english")
        matriz = vectorizador.fit_transform(datos["caracteristicas"])

        similitud = cosine_similarity(matriz[indice], matriz).flatten()

        indices = similitud.argsort()[::-1][1:6]

        print(f"\nRecomendaciones similares a: {datos.iloc[indice]['Title']}\n")

        for i, indice_recomendado in enumerate(indices, start=1):
            print(f"{i}. {datos.iloc[indice_recomendado]['Title']}")

    else:

        coincidencias = datos[
            datos["title_lower"].str.contains(titulo, case=False, na=False)
        ]

        if len(coincidencias) > 0:
            print("\nNo se encontró el título exacto.")
            print("Quizá buscabas alguno de estos:\n")

            for titulo in coincidencias["Title"].head(10):
                print("-", titulo)

        else:
            print("No se encontró ningún título parecido.")


def main():
    print("=== Sistema de Recomendación de Netflix ===\n")

    datos = cargar_datos()

    if datos is None:
        return

    datos = limpiar_datos(datos)

    titulo = input("Introduce una película o serie de Netflix: ")

    recomendar(titulo, datos)


if __name__ == "__main__":
    main()