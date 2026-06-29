import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


RUTA_CSV = "data/netflix_titles.csv"


class RecomendadorNetflix:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Recomendador Netflix")
        self.ventana.geometry("850x600")

        self.datos = self.cargar_datos()
        self.crear_interfaz()

    def cargar_datos(self):
        datos = pd.read_csv(RUTA_CSV)

        columnas = [
            "Title",
            "Director",
            "Cast",
            "Production Country",
            "Genres",
            "Description",
            "Rating",
            "Duration",
            "Imdb Score",
            "Content Type"
        ]

        for columna in columnas:
            datos[columna] = datos[columna].fillna("")

        datos["title_lower"] = datos["Title"].str.lower()

        datos["caracteristicas"] = (
            datos["Director"] + " " +
            datos["Cast"] + " " +
            datos["Production Country"] + " " +
            datos["Genres"] + " " +
            datos["Description"]
        )

        vectorizador = CountVectorizer(stop_words="english")
        self.matriz = vectorizador.fit_transform(datos["caracteristicas"])

        return datos

    def crear_interfaz(self):
        titulo = tk.Label(
            self.ventana,
            text="🎬 Recomendador Netflix",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=15)

        descripcion = tk.Label(
            self.ventana,
            text="Introduce una película o serie y obtén recomendaciones similares.",
            font=("Arial", 12)
        )
        descripcion.pack()

        self.entrada = tk.Entry(
            self.ventana,
            width=50,
            font=("Arial", 14)
        )
        self.entrada.pack(pady=15)

        boton = tk.Button(
            self.ventana,
            text="Buscar recomendaciones",
            font=("Arial", 12),
            command=self.buscar_recomendaciones
        )
        boton.pack(pady=5)

        contenedor = tk.Frame(self.ventana)
        contenedor.pack(fill="both", expand=True, padx=20, pady=15)

        self.lista = tk.Listbox(
            contenedor,
            width=35,
            height=15,
            font=("Arial", 11)
        )
        self.lista.pack(side="left", fill="y")
        self.lista.bind("<<ListboxSelect>>", self.mostrar_detalles)

        self.detalles = tk.Text(
            contenedor,
            width=60,
            height=15,
            font=("Arial", 11),
            wrap="word"
        )
        self.detalles.pack(side="right", fill="both", expand=True, padx=10)

    def buscar_recomendaciones(self):
        titulo = self.entrada.get().lower().strip()

        if not titulo:
            messagebox.showwarning("Aviso", "Introduce un título.")
            return

        self.lista.delete(0, tk.END)
        self.detalles.delete("1.0", tk.END)

        if titulo not in self.datos["title_lower"].values:
            coincidencias = self.datos[
                self.datos["title_lower"].str.contains(titulo, case=False, na=False)
            ]

            if coincidencias.empty:
                messagebox.showinfo("Sin resultados", "No se encontró ningún título parecido.")
                return

            self.detalles.insert(
                tk.END,
                "No se encontró el título exacto.\nQuizá buscabas alguno de estos:\n\n"
            )

            for nombre in coincidencias["Title"].head(10):
                self.lista.insert(tk.END, nombre)

            return

        indice = self.datos[self.datos["title_lower"] == titulo].index[0]

        similitud = cosine_similarity(self.matriz[indice], self.matriz).flatten()
        indices = similitud.argsort()[::-1][1:6]

        for indice_recomendado in indices:
            self.lista.insert(tk.END, self.datos.iloc[indice_recomendado]["Title"])

        self.detalles.insert(
            tk.END,
            f"Recomendaciones similares a: {self.datos.iloc[indice]['Title']}\n\n"
            "Selecciona una recomendación para ver sus detalles."
        )

    def mostrar_detalles(self, evento):
        seleccion = self.lista.curselection()

        if not seleccion:
            return

        titulo = self.lista.get(seleccion[0])
        fila = self.datos[self.datos["Title"] == titulo].iloc[0]

        texto = (
            f"Título: {fila['Title']}\n\n"
            f"Tipo: {fila['Content Type']}\n"
            f"Géneros: {fila['Genres']}\n"
            f"País: {fila['Production Country']}\n"
            f"Duración: {fila['Duration']}\n"
            f"Rating: {fila['Rating']}\n"
            f"IMDb: {fila['Imdb Score']}\n\n"
            f"Director: {fila['Director']}\n\n"
            f"Descripción:\n{fila['Description']}"
        )

        self.detalles.delete("1.0", tk.END)
        self.detalles.insert(tk.END, texto)


if __name__ == "__main__":
    ventana = tk.Tk()
    app = RecomendadorNetflix(ventana)
    ventana.mainloop()