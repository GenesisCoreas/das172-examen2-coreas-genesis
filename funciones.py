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

def sumar_matrices(matriz1, matriz2):
    resultado = []

    for i in range(len(matriz1)):
        fila = []

        for j in range(len(matriz1[i])):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)

        resultado.append(fila)

    return resultado

def multiplicar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz2[0])
    resultado = []

    for i in range(filas):
        fila = []

        for j in range(columnas):
            suma = 0

            for k in range(len(matriz2)):
                suma += matriz1[i][k] * matriz2[k][j]

            fila.append(suma)

        resultado.append(fila)

    return resultado

def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    transpuesta = []

    for j in range(columnas):
        fila = []

        for i in range(filas):
            fila.append(matriz[i][j])

        transpuesta.append(fila)

    return transpuesta

def multiplicar_por_escalar(matriz, escalar):
    resultado = []

    for fila in matriz:
        nueva_fila = []

        for elemento in fila:
            nueva_fila.append(elemento * escalar)

        resultado.append(nueva_fila)

    return resultado

def obtener_diagonal_principal(matriz):
    diagonal = []

    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])

    return diagonal

def obtener_diagonal_secundaria(matriz):
    diagonal = []

    n = len(matriz)

    for i in range(n):
        diagonal.append(matriz[i][n - 1 - i])

    return diagonal

def sumar_filas(matriz):
    sumas = []

    for fila in matriz:
        suma = 0

        for elemento in fila:
            suma += elemento

        sumas.append(suma)

    return sumas

def sumar_columnas(matriz):
    sumas = []

    columnas = len(matriz[0])

    for j in range(columnas):
        suma = 0

        for i in range(len(matriz)):
            suma += matriz[i][j]

        sumas.append(suma)

    return sumas

def sumar_matriz(matriz):
    suma_total = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma_total += matriz[i][j]

    return suma_total

def encontrar_maximo(matriz):
    maximo = matriz[0][0]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]

    return maximo

