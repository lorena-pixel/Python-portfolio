tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def imprimir_tablero(tablero):
    for fila in range(9):
        if fila % 3 == 0 and fila != 0:
            print("-" * 21)

        for columna in range(9):
            if columna % 3 == 0 and columna != 0:
                print("|", end=" ")

            valor = tablero[fila][columna]
            print(valor if valor != 0 else ".", end=" ")

        print()


def encontrar_vacio(tablero):
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                return fila, columna
    return None


def es_valido(tablero, numero, posicion):
    fila, columna = posicion

    for col in range(9):
        if tablero[fila][col] == numero and col != columna:
            return False

    for fil in range(9):
        if tablero[fil][columna] == numero and fil != fila:
            return False

    caja_x = columna // 3
    caja_y = fila // 3

    for fil in range(caja_y * 3, caja_y * 3 + 3):
        for col in range(caja_x * 3, caja_x * 3 + 3):
            if tablero[fil][col] == numero and (fil, col) != posicion:
                return False

    return True


def resolver(tablero):
    vacio = encontrar_vacio(tablero)

    if not vacio:
        return True

    fila, columna = vacio

    for numero in range(1, 10):
        if es_valido(tablero, numero, (fila, columna)):
            tablero[fila][columna] = numero

            if resolver(tablero):
                return True

            tablero[fila][columna] = 0

    return False


print("Sudoku original:")
imprimir_tablero(tablero)

if resolver(tablero):
    print("\nSudoku resuelto:")
    imprimir_tablero(tablero)
else:
    print("No se encontró solución.")