def validar_matrices(cargas, capacidades):
    if len(cargas) != len(capacidades):
        return False

    if len(cargas) < 2:
        return False

    for i in range(len(cargas)):

        if len(cargas[i]) != len(capacidades[i]):
            return False

        if len(cargas[i]) < 2:
            return False

        for j in range(len(cargas[i])):

            if cargas[i][j] < 0:
                return False

            if capacidades[i][j] <= 0:
                return False

    return True

def calcular_ocupacion(cargas, capacidades):
    ocupacion = []
    sobrecargas = []

    for i in range(len(cargas)):
        fila_ocupacion = []

        for j in range(len(cargas[i])):

            porcentaje = (cargas[i][j] / capacidades[i][j]) * 100

            fila_ocupacion.append(porcentaje)

            if porcentaje > 100:
                sobrecargas.append((i, j))

        ocupacion.append(fila_ocupacion)

    return ocupacion, sobrecargas

def evaluar_balance(cargas, tolerancia):
    pesos_filas = []

    for fila in cargas:
        pesos_filas.append(sum(fila))

    columnas = len(cargas[0])

    mitad = columnas // 2

    izquierda = 0
    derecha = 0

    for fila in cargas:
        izquierda += sum(fila[:mitad])

        if columnas % 2 == 0:
            derecha += sum(fila[mitad:])
        else:
            derecha += sum(fila[mitad + 1:])

    desbalance = abs(izquierda - derecha)

    balanceado = desbalance <= tolerancia

    return pesos_filas, desbalance, balanceado

def extraer_submatriz(matriz, inicio_fila, inicio_columna, filas, columnas):
    submatriz = []

    for i in range(inicio_fila, inicio_fila + filas):
        fila = []

        for j in range(inicio_columna, inicio_columna + columnas):
            fila.append(matriz[i][j])

        submatriz.append(fila)

    return submatriz

def transformar_matriz(matriz):
    transformada = []

    for fila in matriz:
        nueva_fila = []

        for elemento in fila:
            nueva_fila.append(elemento * 2)

        transformada.append(nueva_fila)

    return transformada

def comparar_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2):
        return False

    for i in range(len(matriz1)):
        if len(matriz1[i]) != len(matriz2[i]):
            return False

        for j in range(len(matriz1[i])):
            if matriz1[i][j] != matriz2[i][j]:
                return False

    return True

