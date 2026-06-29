import tkinter as tk
from tkinter import messagebox
from solver import resolver, es_valido


class SudokuGUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Resolutor de Sudoku")
        self.entradas = []

        self.crear_tablero()
        self.crear_botones()

    def crear_tablero(self):
        marco = tk.Frame(self.ventana)
        marco.pack(pady=10)

        for fila in range(9):
            fila_entradas = []

            for columna in range(9):
                entrada = tk.Entry(
                    marco,
                    width=3,
                    font=("Arial", 20),
                    justify="center"
                )
                entrada.grid(
                    row=fila,
                    column=columna,
                    padx=(3 if columna % 3 == 0 else 1),
                    pady=(3 if fila % 3 == 0 else 1)
                )
                fila_entradas.append(entrada)

            self.entradas.append(fila_entradas)

    def crear_botones(self):
        marco_botones = tk.Frame(self.ventana)
        marco_botones.pack(pady=10)

        tk.Button(marco_botones, text="Resolver", command=self.resolver_sudoku).grid(row=0, column=0, padx=5)
        tk.Button(marco_botones, text="Comprobar", command=self.comprobar_sudoku).grid(row=0, column=1, padx=5)
        tk.Button(marco_botones, text="Limpiar", command=self.limpiar).grid(row=0, column=2, padx=5)

    def obtener_tablero(self):
        tablero = []

        for fila in range(9):
            fila_valores = []

            for columna in range(9):
                valor = self.entradas[fila][columna].get()

                if valor == "":
                    fila_valores.append(0)
                elif valor.isdigit() and 1 <= int(valor) <= 9:
                    fila_valores.append(int(valor))
                else:
                    messagebox.showerror("Error", "Solo puedes introducir números del 1 al 9.")
                    return None

            tablero.append(fila_valores)

        return tablero

    def mostrar_tablero(self, tablero):
        for fila in range(9):
            for columna in range(9):
                self.entradas[fila][columna].delete(0, tk.END)
                self.entradas[fila][columna].insert(0, str(tablero[fila][columna]))
                self.entradas[fila][columna].config(bg="white")

    def resolver_sudoku(self):
        tablero = self.obtener_tablero()

        if tablero is None:
            return

        if resolver(tablero):
            self.mostrar_tablero(tablero)
            messagebox.showinfo("Sudoku", "Sudoku resuelto correctamente.")
        else:
            messagebox.showerror("Sudoku", "No se encontró solución.")

    def comprobar_sudoku(self):
        tablero = self.obtener_tablero()

        if tablero is None:
            return

        hay_errores = False

        for fila in range(9):
            for columna in range(9):
                valor = tablero[fila][columna]
                entrada = self.entradas[fila][columna]

                entrada.config(bg="white")

                if valor != 0:
                    tablero[fila][columna] = 0

                    if es_valido(tablero, valor, (fila, columna)):
                        entrada.config(bg="#c8f7c5")
                    else:
                        entrada.config(bg="#f7c5c5")
                        hay_errores = True

                    tablero[fila][columna] = valor

        if hay_errores:
            messagebox.showwarning("Comprobación", "Hay números incorrectos.")
        else:
            messagebox.showinfo("Comprobación", "Los números introducidos son válidos.")

    def limpiar(self):
        for fila in range(9):
            for columna in range(9):
                self.entradas[fila][columna].delete(0, tk.END)
                self.entradas[fila][columna].config(bg="white")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = SudokuGUI(ventana)
    ventana.mainloop()