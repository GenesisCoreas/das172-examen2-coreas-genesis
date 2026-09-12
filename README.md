# DAS172 - Examen 2

Proyecto desarrollado en Python para analizar la distribución de carga de una aeronave mediante matrices. El sistema permite validar los datos de carga y capacidad, calcular el porcentaje de ocupación de cada celda, identificar sobrecargas, evaluar el balance lateral y localizar una submatriz crítica que represente una zona de alta concentración de carga.

La solución utiliza programación modular, separando las funciones de procesamiento, la ejecución principal del programa y las pruebas de validación.

La correcta distribución de la carga es importante para la seguridad de la aeronave, ya que cada sección del piso posee una capacidad máxima de carga. Una sobrecarga puede comprometer la integridad estructural del fuselaje. Además, la distribución del peso debe mantenerse equilibrada entre los lados izquierdo y derecho de la aeronave para conservar condiciones adecuadas de balance y maniobrabilidad durante el vuelo.

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

## Arquitectura modular

El proyecto está organizado utilizando programación modular, separando las funciones de procesamiento, la ejecución principal y las pruebas de validación.

```text
  AeroCargo-Matrix
                           |
             -----------------------------
             |                           |
        funciones.py                  main.py
             |                           |
     Procesamiento y              Ejecución principal
   análisis de matrices           del programa
             |
        pruebas.py
             |
     Validación y pruebas
```

### Flujo de datos

```text
cargas + capacidades
        |
        v
validar_matrices()
        |
        v
calcular_ocupacion()
        |
        +--------------------+
        |                    |
        v                    v
evaluar_balance()   buscar_submatriz_critica()
        |                    |
        +---------+----------+
                  |
                  v
           resultados finales
```

`main.py` proporciona las matrices de cargas y capacidades a las funciones de `funciones.py`. Cada función procesa los parámetros recibidos y devuelve sus resultados sin modificar las matrices originales. Estos resultados son utilizados por el programa principal para mostrar el análisis final de la distribución de carga.

## Decisiones técnicas

Se utilizó programación modular para separar las responsabilidades del sistema. Las funciones relacionadas con el procesamiento y análisis de matrices se encuentran en `funciones.py`, mientras que `main.py` contiene el flujo principal del programa y utiliza dichas funciones para realizar el análisis de carga de la aeronave.

Las matrices fueron representadas mediante listas bidimensionales de Python, permitiendo acceder a cada posición mediante índices de fila y columna. Esta representación facilita operaciones como la validación de cargas y capacidades, el cálculo de ocupación, la evaluación del balance lateral y la búsqueda de submatrices críticas.

El archivo `pruebas.py` se mantiene separado del programa principal para verificar el funcionamiento de las funciones mediante diferentes casos de prueba, incluyendo casos válidos, casos límite y matrices irregulares.

## Datos de entrada

El análisis utiliza dos matrices principales:

- `cargas`: representa la carga asignada a cada sección de la aeronave.
- `capacidades`: representa la capacidad máxima permitida para cada una de esas posiciones.

Ambas matrices deben tener las mismas dimensiones, contar con al menos dos filas y dos columnas, no contener cargas negativas y poseer capacidades mayores que cero.

También se utiliza una tolerancia para determinar si la diferencia de carga entre los lados izquierdo y derecho se encuentra dentro de un rango aceptable.

## Ejecución

Para ejecutar el programa principal, ubíquese en la carpeta del proyecto desde la terminal y utilice:

```bash
python main.py
```

El programa ejecutará el flujo principal de AeroCargo-Matrix y mostrará:

- La validación de las matrices de cargas y capacidades.
- La matriz de ocupación expresada en porcentaje.
- Las coordenadas de las celdas con sobrecarga.
- El peso total de cada fila.
- El valor del desbalance lateral.
- El estado del balance de acuerdo con la tolerancia establecida.
- La submatriz crítica 2x2.
- Un resumen final del análisis.

Para ejecutar las pruebas del proyecto, utilice:

```bash
python pruebas.py
```

## Resultados del análisis

Al ejecutar el programa, AeroCargo-Matrix presenta los resultados principales del análisis de carga:

- La matriz de ocupación muestra el porcentaje utilizado de la capacidad de cada posición.
- Las celdas con sobrecarga indican las coordenadas donde la ocupación supera el 100 %.
- Los pesos por fila representan la suma de las cargas correspondientes a cada fila de la matriz.
- El desbalance lateral representa la diferencia absoluta entre la carga del lado izquierdo y el lado derecho.
- El estado del balance indica si el desbalance se encuentra dentro o fuera de la tolerancia establecida.
- La submatriz crítica 2x2 identifica la región con el mayor promedio de carga.
- El resumen final reúne la cantidad de sobrecargas, el desbalance lateral y el resultado general del análisis.

## Ejemplo

El programa utiliza una matriz de cargas como la siguiente:

```python
cargas = [
    [80, 120, 60, 90],
    [70, 110, 50, 100],
    [60, 90, 80, 120]
]
```
La matriz de capacidades utilizada es:

```python
capacidades = [
    [100, 100, 100, 100],
    [100, 100, 100, 100],
    [100, 100, 100, 100]
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

### Resultado del ejemplo

Al ejecutar el programa con estos datos se obtiene:

```text
Matriz de ocupación (%):
[80.0, 120.0, 60.0, 90.0]
[70.0, 110.0, 50.0, 100.0]
[60.0, 90.0, 80.0, 120.0]

Celdas con sobrecarga:
[(0, 1), (1, 1), (2, 3)]

Pesos por fila:
[350, 330, 350]

Desbalance lateral:
30

Estado del balance:
Balance fuera de tolerancia.

Submatriz crítica 2x2:
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