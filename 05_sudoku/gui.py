import tkinter as tk
from tkinter import messagebox
import random
from copy import deepcopy
from solver import resolver, es_valido


SUDOKUS = [
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ],
    [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0],
    ],
    [
        [0, 2, 0, 6, 0, 8, 0, 0, 0],
        [5, 8, 0, 0, 0, 9, 7, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [3, 7, 0, 0, 0, 0, 5, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 8, 0, 0, 0, 0, 1, 3],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 9, 8, 0, 0, 0, 3, 6],
        [0, 0, 0, 3, 0, 6, 0, 9, 0],
    ],
]


class SudokuGUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Resolutor de Sudoku")
        self.entradas = []
        self.tablero_inicial = []

        self.crear_tablero()
        self.crear_botones()
        self.nuevo_sudoku()

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
                    padx=(4 if columna % 3 == 0 else 1),
                    pady=(4 if fila % 3 == 0 else 1)
                )
                fila_entradas.append(entrada)

            self.entradas.append(fila_entradas)

    def crear_botones(self):
        marco_botones = tk.Frame(self.ventana)
        marco_botones.pack(pady=10)

        tk.Button(marco_botones, text="Resolver", command=self.resolver_sudoku).grid(row=0, column=0, padx=5)
        tk.Button(marco_botones, text="Comprobar", command=self.comprobar_sudoku).grid(row=0, column=1, padx=5)
        tk.Button(marco_botones, text="Nuevo Sudoku", command=self.nuevo_sudoku).grid(row=0, column=2, padx=5)
        tk.Button(marco_botones, text="Limpiar", command=self.limpiar_respuestas).grid(row=0, column=3, padx=5)

    def nuevo_sudoku(self):
        self.tablero_inicial = deepcopy(random.choice(SUDOKUS))

        for fila in range(9):
            for columna in range(9):
                entrada = self.entradas[fila][columna]
                entrada.config(state="normal")
                entrada.delete(0, tk.END)

                valor = self.tablero_inicial[fila][columna]

                if valor != 0:
                    entrada.insert(0, str(valor))
                    entrada.config(state="disabled", disabledforeground="black", disabledbackground="#e6e6e6")
                else:
                    entrada.config(bg="white")

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
                entrada = self.entradas[fila][columna]
                entrada.config(state="normal")
                entrada.delete(0, tk.END)
                entrada.insert(0, str(tablero[fila][columna]))

                if self.tablero_inicial[fila][columna] != 0:
                    entrada.config(state="disabled", disabledforeground="black", disabledbackground="#e6e6e6")
                else:
                    entrada.config(bg="#d7f7d7")

    def resolver_sudoku(self):
        tablero = self.obtener_tablero()

        if tablero is None:
            return

        solucion = deepcopy(tablero)

        if resolver(solucion):
            self.mostrar_tablero(solucion)
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
                entrada = self.entradas[fila][columna]

                if self.tablero_inicial[fila][columna] != 0:
                    continue

                valor = tablero[fila][columna]
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

    def limpiar_respuestas(self):
        for fila in range(9):
            for columna in range(9):
                if self.tablero_inicial[fila][columna] == 0:
                    entrada = self.entradas[fila][columna]
                    entrada.delete(0, tk.END)
                    entrada.config(bg="white")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = SudokuGUI(ventana)
    ventana.mainloop()