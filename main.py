from funciones import (
    validar_matrices,
    calcular_ocupacion,
    evaluar_balance,
    buscar_submatriz_critica
)

cargas = [
    [80, 120, 60, 90],
    [70, 110, 50, 100],
    [60, 90, 80, 120]
]

capacidades = [
    [100, 100, 100, 100],
    [100, 100, 100, 100],
    [100, 100, 100, 100]
]

tolerancia = 20

print("===== AEROCARGO MATRIX =====")

if validar_matrices(cargas, capacidades):
    print("\nMatrices validas.")

    ocupacion, sobrecargas = calcular_ocupacion(
        cargas,
        capacidades
    )

    print("\nMatriz de ocupacion (%):")
    for fila in ocupacion:
        print(fila)

    print("\nCeldas con sobrecarga:")
    print(sobrecargas)

    pesos_filas, desbalance, balanceado = evaluar_balance(
        cargas,
        tolerancia
    )

    print("\nPesos por fila:")
    print(pesos_filas)

    print("\nDesbalance lateral:")
    print(desbalance)

    print("\nEstado del balance:")
    if balanceado:
        print("Balance aceptable.")
    else:
        print("Balance fuera de tolerancia.")

    submatriz_critica = buscar_submatriz_critica(
        ocupacion,
        2,
        2
    )

    print("\nSubmatriz critica 2x2:")
    for fila in submatriz_critica:
        print(fila)

    print("\n===== RESUMEN DEL ANALISIS =====")
    print("Total de celdas con sobrecarga:", len(sobrecargas))
    print("Desbalance lateral:", desbalance)

    if balanceado:
        print("Resultado final: Carga balanceada.")
    else:
        print("Resultado final: Carga fuera de balance.")

    print("Submatriz critica:")
    for fila in submatriz_critica:
        print(fila)

else:
    print("\nMatrices invalidas.")