# DAS172 - Examen 2

Proyecto desarrollado en Python para trabajar con matrices y realizar diferentes operaciones, validaciones y análisis sobre ellas.

## Archivos del proyecto

- `funciones.py`: contiene las funciones utilizadas para realizar operaciones y validaciones con matrices.
- `main.py`: ejecuta las principales funciones del programa y muestra sus resultados.
- `pruebas.py`: contiene pruebas para comprobar el funcionamiento correcto de las funciones.
- `requirements.txt`: archivo de dependencias del proyecto.

## Funcionalidades

El proyecto incluye funciones para:

- Validar matrices de cargas y capacidades.
- Calcular porcentajes de ocupación y detectar sobrecargas.
- Evaluar el balance de una matriz de cargas.
- Extraer submatrices.
- Buscar una submatriz crítica.
- Sumar matrices.
- Multiplicar matrices.
- Multiplicar una matriz por un escalar.
- Transponer matrices.
- Obtener la diagonal principal y secundaria.
- Sumar filas y columnas.
- Calcular la suma total de una matriz.
- Encontrar el valor máximo y mínimo.
- Calcular el promedio de los elementos.
- Validar si una matriz es cuadrada.
- Validar dimensiones para multiplicación.
- Verificar matrices identidad.
- Verificar matrices triangulares superiores e inferiores.
- Verificar matrices diagonales.
- Verificar matrices simétricas.
- Realizar operaciones adicionales de búsqueda y conteo de elementos.

## Ejecución

Para ejecutar el programa principal:

```bash
python main.py
```

Para ejecutar las pruebas:

```bash
python pruebas.py
```

## Ejemplo

Para una matriz:

```python
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

El programa puede obtener, entre otros resultados:

```text
Diagonal principal: [1, 5, 9]
Diagonal secundaria: [3, 5, 7]
Suma total: 45
Máximo: 9
Mínimo: 1
Promedio: 5.0
```

## Pruebas

El archivo `pruebas.py` verifica diferentes casos relacionados con:

- Validación de matrices.
- Cálculo de ocupación.
- Evaluación de balance.
- Extracción y búsqueda de submatrices.
- Operaciones básicas con matrices.
- Casos límite.

Las pruebas pueden ejecutarse utilizando:

```bash
python pruebas.py
```

Si todas las pruebas se ejecutan correctamente, el programa mostrará mensajes indicando que las pruebas pasaron satisfactoriamente.

## Autor

Genesis Coreas