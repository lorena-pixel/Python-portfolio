import tkinter as tk
from tkinter import filedialog, messagebox


class EditorTexto:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Editor de Texto")
        self.ventana.geometry("800x600")

        self.ruta_archivo = None

        self.crear_menu()

        self.area_texto = tk.Text(
            self.ventana,
            wrap="word",
            font=("Arial", 12),
            undo=True
        )
        self.area_texto.pack(expand=True, fill="both")

    def crear_menu(self):
        barra_menu = tk.Menu(self.ventana)
        self.ventana.config(menu=barra_menu)

        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

        menu_archivo.add_command(label="Nuevo", command=self.nuevo_archivo)
        menu_archivo.add_command(label="Abrir", command=self.abrir_archivo)
        menu_archivo.add_command(label="Guardar", command=self.guardar_archivo)
        menu_archivo.add_command(label="Guardar como", command=self.guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.ventana.quit)

    def nuevo_archivo(self):
        self.area_texto.delete("1.0", tk.END)
        self.ruta_archivo = None
        self.ventana.title("Editor de Texto - Nuevo archivo")

    def abrir_archivo(self):
        ruta = filedialog.askopenfilename(
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Todos los archivos", "*.*")
            ]
        )

        if ruta:
            with open(ruta, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

            self.area_texto.delete("1.0", tk.END)
            self.area_texto.insert(tk.END, contenido)

            self.ruta_archivo = ruta
            self.ventana.title(f"Editor de Texto - {ruta}")

    def guardar_archivo(self):
        if self.ruta_archivo:
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                contenido = self.area_texto.get("1.0", tk.END)
                archivo.write(contenido)

            messagebox.showinfo("Guardado", "Archivo guardado correctamente.")
        else:
            self.guardar_como()

    def guardar_como(self):
        ruta = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Todos los archivos", "*.*")
            ]
        )

        if ruta:
            with open(ruta, "w", encoding="utf-8") as archivo:
                contenido = self.area_texto.get("1.0", tk.END)
                archivo.write(contenido)

            self.ruta_archivo = ruta
            self.ventana.title(f"Editor de Texto - {ruta}")
            messagebox.showinfo("Guardado", "Archivo guardado correctamente.")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = EditorTexto(ventana)
    ventana.mainloop()