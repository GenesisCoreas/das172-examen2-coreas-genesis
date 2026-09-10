from funciones import *


A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]


print("Matriz A:")
print(A)

print("\nMatriz B:")
print(B)


print("\nSuma de matrices:")
print(sumar_matrices(A, B))


print("\nMultiplicación de matrices:")
print(multiplicar_matrices(A, B))


print("\nMultiplicación por escalar:")
print(multiplicar_por_escalar(A, 2))


print("\nMatriz transpuesta:")
print(transponer_matriz(A))


print("\nDiagonal principal:")
print(obtener_diagonal_principal(A))


print("\nDiagonal secundaria:")
print(obtener_diagonal_secundaria(A))


print("\nSuma total:")
print(sumar_matriz(A))


print("\nMáximo:")
print(encontrar_maximo(A))


print("\nMínimo:")
print(encontrar_minimo(A))


print("\nPromedio:")
print(calcular_promedio(A))


print("\nEs cuadrada:")
print(es_matriz_cuadrada(A))


print("\nEs simétrica:")
print(es_matriz_simetrica(A))


print("\nSubmatriz crítica:")
print(buscar_submatriz_critica(A, 2, 2))