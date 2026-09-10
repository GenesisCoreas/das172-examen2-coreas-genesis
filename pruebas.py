from funciones import validar_matrices, calcular_ocupacion


# CASO 1: matrices validas
cargas = [
    [50, 100],
    [75, 120]
]

capacidades = [
    [100, 100],
    [100, 100]
]

assert validar_matrices(cargas, capacidades) == True


# CASO 2: carga negativa
cargas_invalidas = [
    [-10, 50],
    [20, 30]
]

assert validar_matrices(cargas_invalidas, capacidades) == False


# CASO 3: capacidad igual a cero
capacidades_invalidas = [
    [100, 0],
    [100, 100]
]

assert validar_matrices(cargas, capacidades_invalidas) == False


# CASO 4: calcular ocupacion y detectar sobrecarga
ocupacion, sobrecargas = calcular_ocupacion(cargas, capacidades)

assert ocupacion[0][0] == 50.0
assert ocupacion[0][1] == 100.0
assert (1, 1) in sobrecargas


print("Todas las pruebas de validacion y ocupacion pasaron correctamente.")

from funciones import evaluar_balance, buscar_submatriz_critica


# CASO 5: balance lateral aprobado
cargas_balanceadas = [
    [50, 20, 20, 50],
    [40, 30, 30, 40]
]

pesos_filas, desbalance, balanceado = evaluar_balance(
    cargas_balanceadas,
    10
)

assert pesos_filas == [140, 140]
assert desbalance == 0
assert balanceado == True


# CASO 6: balance lateral rechazado
cargas_desbalanceadas = [
    [100, 100, 10, 10],
    [100, 100, 10, 10]
]

pesos_filas, desbalance, balanceado = evaluar_balance(
    cargas_desbalanceadas,
    50
)

assert desbalance > 50
assert balanceado == False


# CASO 7: submatriz critica
matriz_ocupacion = [
    [10, 20, 30],
    [40, 90, 100],
    [50, 110, 120]
]

submatriz = buscar_submatriz_critica(
    matriz_ocupacion,
    2,
    2
)

assert submatriz == [
    [90, 100],
    [110, 120]
]


print("Todas las pruebas de balance y submatriz critica pasaron correctamente.")

# CASO 8: matriz minima 2x2 valida
cargas_minimas = [
    [10, 20],
    [30, 40]
]

capacidades_minimas = [
    [100, 100],
    [100, 100]
]

assert validar_matrices(cargas_minimas, capacidades_minimas) == True


# CASO 9: dimensiones no coincidentes
cargas_dimensiones = [
    [10, 20],
    [30, 40]
]

capacidades_dimensiones = [
    [100, 100, 100],
    [100, 100, 100]
]

assert validar_matrices(cargas_dimensiones, capacidades_dimensiones) == False


# CASO 10: columnas impares, columna central ignorada en balance
cargas_impares = [
    [50, 999, 50],
    [30, 999, 30]
]

pesos_filas, desbalance, balanceado = evaluar_balance(
    cargas_impares,
    0
)

assert desbalance == 0
assert balanceado == True


print("Todas las pruebas de casos limite pasaron correctamente.")