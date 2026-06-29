import tkinter as tk
from tkinter import messagebox
import datetime
import random
import webbrowser


ARCHIVO_LINKS = "youtube_links.txt"


class RelojDespertador:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Reloj Despertador")
        self.ventana.geometry("500x350")

        self.alarma_activada = False
        self.hora_alarma = ""

        self.crear_interfaz()
        self.actualizar_reloj()

    def crear_interfaz(self):
        self.reloj_label = tk.Label(
            self.ventana,
            text="",
            font=("Arial", 28, "bold")
        )
        self.reloj_label.pack(pady=20)

        tk.Label(
            self.ventana,
            text="Hora de alarma (HH:MM):",
            font=("Arial", 12)
        ).pack()

        self.entrada_hora = tk.Entry(
            self.ventana,
            font=("Arial", 14),
            justify="center"
        )
        self.entrada_hora.pack(pady=10)
        self.entrada_hora.insert(0, "08:00")

        tk.Button(
            self.ventana,
            text="Activar alarma",
            command=self.activar_alarma
        ).pack(pady=5)

        tk.Button(
            self.ventana,
            text="Desactivar alarma",
            command=self.desactivar_alarma
        ).pack(pady=5)

        self.estado_label = tk.Label(
            self.ventana,
            text="Alarma desactivada",
            font=("Arial", 12)
        )
        self.estado_label.pack(pady=15)

    def actualizar_reloj(self):
        ahora = datetime.datetime.now()
        hora_actual = ahora.strftime("%H:%M:%S")
        hora_actual_sin_segundos = ahora.strftime("%H:%M")

        self.reloj_label.config(text=hora_actual)

        if self.alarma_activada and hora_actual_sin_segundos == self.hora_alarma:
            self.alarma_activada = False
            self.reproducir_video()
            self.estado_label.config(text="Alarma ejecutada")

        self.ventana.after(1000, self.actualizar_reloj)

    def activar_alarma(self):
        hora = self.entrada_hora.get().strip()

        try:
            datetime.datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Formato incorrecto. Usa HH:MM, por ejemplo 08:30.")
            return

        self.hora_alarma = hora
        self.alarma_activada = True
        self.estado_label.config(text=f"Alarma activada para las {hora}")

    def desactivar_alarma(self):
        self.alarma_activada = False
        self.estado_label.config(text="Alarma desactivada")

    def reproducir_video(self):
        try:
            with open(ARCHIVO_LINKS, "r", encoding="utf-8") as archivo:
                enlaces = [linea.strip() for linea in archivo if linea.strip()]

            if not enlaces:
                messagebox.showwarning("Aviso", "No hay enlaces en youtube_links.txt.")
                return

            enlace = random.choice(enlaces)
            webbrowser.open(enlace)

        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo youtube_links.txt.")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = RelojDespertador(ventana)
    ventana.mainloop()