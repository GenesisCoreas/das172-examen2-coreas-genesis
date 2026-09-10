# DAS172 - Examen 2

Proyecto desarrollado en Python para analizar la distribución de carga de una aeronave mediante matrices. El sistema permite validar los datos de carga y capacidad, calcular el porcentaje de ocupación de cada celda, identificar sobrecargas, evaluar el balance lateral y localizar una submatriz crítica que represente una zona de alta concentración de carga.

La solución utiliza programación modular, separando las funciones de procesamiento, la ejecución principal del programa y las pruebas de validación.

## Archivos del proyecto

- `funciones.py`: contiene las funciones modulares utilizadas para validar matrices, calcular ocupación, evaluar balance y buscar la submatriz crítica.
- `main.py`: ejecuta el flujo principal del sistema AeroCargo-Matrix con datos de prueba y muestra los resultados obtenidos.
- `pruebas.py`: contiene pruebas para verificar el funcionamiento correcto de los módulos principales y casos límite.
- `README.md`: contiene la explicación técnica del proyecto, su arquitectura y forma de ejecución.
- `.gitignore`: evita incluir archivos temporales de Python y configuraciones locales.
- `requirements.txt`: archivo de dependencias del proyecto.

## Funcionalidades

El sistema AeroCargo-Matrix permite:

- Validar que las matrices de cargas y capacidades tengan dimensiones compatibles.
- Verificar que las cargas no contengan valores negativos y que las capacidades sean mayores que cero.
- Calcular el porcentaje de ocupación de cada celda.
- Detectar las posiciones que presentan sobrecarga, es decir, ocupaciones mayores al 100 %.
- Calcular el peso total correspondiente a cada fila de la matriz.
- Evaluar el balance lateral de la carga utilizando una tolerancia establecida.
- Extraer submatrices de una matriz principal.
- Buscar una submatriz crítica según el mayor promedio de carga.
- Generar un resumen final con la cantidad de sobrecargas, el desbalance lateral y el estado general de la carga.

Además, `funciones.py` contiene operaciones auxiliares para el manejo y análisis de matrices, utilizadas durante el desarrollo y las pruebas del proyecto.

## Ejecución

Para ejecutar el programa principal, desde la terminal ubicada en la carpeta del proyecto se utiliza:

```bash
python main.py

## Ejemplo

El programa utiliza una matriz de cargas como la siguiente:

```python
cargas = [
    [80, 120, 60, 90],
    [70, 110, 50, 100],
    [60, 90, 80, 120]
]
```

Con capacidades de 100 para cada posición, el sistema obtiene los porcentajes de ocupación e identifica las celdas que superan el 100 % de capacidad.

Para estos datos se detectan tres posiciones con sobrecarga:

```text
[(0, 1), (1, 1), (2, 3)]
```

También se obtiene un desbalance lateral de 30. Con una tolerancia establecida de 20, el resultado indica que la carga se encuentra fuera de balance.

La submatriz crítica 2x2 obtenida es:

```text
[80.0, 120.0]
[70.0, 110.0]
```

## Pruebas

El archivo `pruebas.py` verifica diferentes casos relacionados con:

- Validación de matrices de cargas y capacidades.
- Cálculo de ocupación y detección de sobrecargas.
- Evaluación del balance lateral.
- Extracción y búsqueda de submatrices críticas.
- Validación de casos límite.
- Validación de matrices irregulares.

Las pruebas pueden ejecutarse utilizando:

```bash
python pruebas.py
```

Si todas las pruebas se ejecutan correctamente, el programa mostrará mensajes indicando que las pruebas pasaron satisfactoriamente.

## Autor

Genesis Coreas