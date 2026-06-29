import tkinter as tk
from tkinter import messagebox
import random
import time


FRASES = [
    "Python es un lenguaje muy utilizado en desarrollo web",
    "La practica constante mejora la velocidad de escritura",
    "GitHub permite mostrar proyectos de programacion",
    "Aprender a programar requiere paciencia y constancia",
    "Las interfaces graficas hacen los programas mas visuales"
]


class PruebaEscritura:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Prueba de Escritura Veloz")
        self.ventana.geometry("700x400")

        self.frase_actual = ""
        self.tiempo_inicio = None

        self.titulo = tk.Label(
            ventana,
            text="Prueba de Escritura Veloz",
            font=("Arial", 20, "bold")
        )
        self.titulo.pack(pady=15)

        self.frase_label = tk.Label(
            ventana,
            text="Pulsa 'Nueva frase' para empezar",
            font=("Arial", 14),
            wraplength=650
        )
        self.frase_label.pack(pady=20)

        self.entrada = tk.Entry(ventana, font=("Arial", 14), width=60)
        self.entrada.pack(pady=10)

        self.boton_nueva = tk.Button(
            ventana,
            text="Nueva frase",
            command=self.nueva_frase
        )
        self.boton_nueva.pack(pady=5)

        self.boton_comprobar = tk.Button(
            ventana,
            text="Comprobar",
            command=self.comprobar_resultado
        )
        self.boton_comprobar.pack(pady=5)

        self.resultado_label = tk.Label(
            ventana,
            text="",
            font=("Arial", 12)
        )
        self.resultado_label.pack(pady=20)

    def nueva_frase(self):
        self.frase_actual = random.choice(FRASES)
        self.frase_label.config(text=self.frase_actual)
        self.entrada.delete(0, tk.END)
        self.resultado_label.config(text="")
        self.tiempo_inicio = time.time()
        self.entrada.focus()

    def comprobar_resultado(self):
        if self.tiempo_inicio is None:
            messagebox.showwarning("Aviso", "Primero pulsa 'Nueva frase'.")
            return

        texto_usuario = self.entrada.get()
        tiempo_final = time.time()
        tiempo_total = tiempo_final - self.tiempo_inicio

        palabras = len(texto_usuario.split())
        palabras_por_minuto = round((palabras / tiempo_total) * 60, 2)

        precision = self.calcular_precision(self.frase_actual, texto_usuario)

        self.resultado_label.config(
            text=(
                f"Tiempo: {tiempo_total:.2f} segundos\n"
                f"Velocidad: {palabras_por_minuto} palabras por minuto\n"
                f"Precisión: {precision}%"
            )
        )

    def calcular_precision(self, frase_original, frase_usuario):
        caracteres_correctos = 0
        longitud = max(len(frase_original), len(frase_usuario))

        if longitud == 0:
            return 0

        for original, escrito in zip(frase_original, frase_usuario):
            if original == escrito:
                caracteres_correctos += 1

        precision = (caracteres_correctos / longitud) * 100
        return round(precision, 2)


if __name__ == "__main__":
    ventana = tk.Tk()
    app = PruebaEscritura(ventana)
    ventana.mainloop()