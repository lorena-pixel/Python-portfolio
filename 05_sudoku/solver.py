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