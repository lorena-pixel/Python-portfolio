import tkinter as tk
from tkinter import messagebox
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


class ComprobadorWeb:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Comprobador de Conectividad Web")
        self.ventana.geometry("500x300")

        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = tk.Label(
            self.ventana,
            text="Comprobador de Conectividad Web",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=20)

        self.entrada_url = tk.Entry(
            self.ventana,
            width=45,
            font=("Arial", 12)
        )
        self.entrada_url.pack(pady=10)
        self.entrada_url.insert(0, "https://www.google.com")

        boton = tk.Button(
            self.ventana,
            text="Comprobar sitio web",
            command=self.comprobar_web
        )
        boton.pack(pady=10)

        self.resultado = tk.Label(
            self.ventana,
            text="",
            font=("Arial", 12),
            wraplength=450
        )
        self.resultado.pack(pady=20)

    def comprobar_web(self):
        url = self.entrada_url.get().strip()

        if not url:
            messagebox.showwarning("Aviso", "Introduce una URL.")
            return

        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url

        try:
            respuesta = urlopen(url, timeout=5)
            codigo = respuesta.getcode()

            if codigo == 200:
                self.resultado.config(
                    text=f"✅ El sitio está funcionando correctamente.\nCódigo HTTP: {codigo}",
                    fg="green"
                )
            else:
                self.resultado.config(
                    text=f"⚠️ El sitio responde, pero con código HTTP: {codigo}",
                    fg="orange"
                )

        except HTTPError as error:
            self.resultado.config(
                text=f"❌ Error HTTP: {error.code}",
                fg="red"
            )

        except URLError:
            self.resultado.config(
                text="❌ No se pudo conectar con el sitio web.",
                fg="red"
            )

        except Exception as error:
            self.resultado.config(
                text=f"❌ Error inesperado: {error}",
                fg="red"
            )


if __name__ == "__main__":
    ventana = tk.Tk()
    app = ComprobadorWeb(ventana)
    ventana.mainloop()