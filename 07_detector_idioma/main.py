import tkinter as tk
from tkinter import messagebox
from langdetect import detect, detect_langs


IDIOMAS = {
    "es": "Español",
    "en": "Inglés",
    "fr": "Francés",
    "de": "Alemán",
    "it": "Italiano",
    "pt": "Portugués",
    "ca": "Catalán",
    "gl": "Gallego",
    "nl": "Neerlandés",
    "ru": "Ruso",
    "ja": "Japonés",
    "ko": "Coreano",
    "zh-cn": "Chino simplificado",
    "zh-tw": "Chino tradicional",
    "ar": "Árabe",
    "tr": "Turco",
    "pl": "Polaco",
    "ro": "Rumano",
    "sv": "Sueco",
    "da": "Danés",
    "fi": "Finés",
    "no": "Noruego",
    "tr": "Turco",
}


class DetectorIdioma:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Detector de Idioma")
        self.ventana.geometry("600x400")

        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = tk.Label(
            self.ventana,
            text="Detector de Idioma",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=15)

        self.area_texto = tk.Text(
            self.ventana,
            height=8,
            width=60,
            font=("Arial", 12)
        )
        self.area_texto.pack(pady=10)

        boton = tk.Button(
            self.ventana,
            text="Detectar idioma",
            command=self.detectar_idioma
        )
        boton.pack(pady=10)

        self.resultado = tk.Label(
            self.ventana,
            text="",
            font=("Arial", 13),
            wraplength=550
        )
        self.resultado.pack(pady=15)

    def detectar_idioma(self):
        texto = self.area_texto.get("1.0", tk.END).strip()

        if not texto:
            messagebox.showwarning("Aviso", "Introduce un texto.")
            return

        if len(texto.split()) < 3:
            messagebox.showwarning(
                "Texto demasiado corto",
                "Introduce al menos 3 palabras para detectar el idioma con mayor precisión."
            )
            return

        try:
            codigo = detect(texto)
            probabilidades = detect_langs(texto)

            idioma = IDIOMAS.get(codigo, f"Idioma no registrado en la lista ({codigo})")
            confianza = round(probabilidades[0].prob * 100, 2)

            self.resultado.config(
                text=(
                    f"Idioma detectado: {idioma}\n"
                    f"Código: {codigo}\n"
                    f"Confianza aproximada: {confianza}%"
                )
            )

        except Exception as error:
            messagebox.showerror("Error", f"No se pudo detectar el idioma.\n{error}")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = DetectorIdioma(ventana)
    ventana.mainloop()