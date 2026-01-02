<!--
::METADATA::
type: method
topic_id: al-03-sistemas-lineales
file_id: AL-03-Metodos-Sistemas-Lineales
status: stable
audience: student
last_updated: 2024-12-29
-->

# Métodos para Sistemas de Ecuaciones Lineales

> **Objetivo:** Dominar la resolución de sistemas de ecuaciones lineales con algoritmos detallados, cálculos intermedios y ejemplos clásicos paso a paso.

---

## Método 1: Eliminación Gaussiana

### Cuándo Usar
- Cualquier sistema de ecuaciones lineales
- Método estándar y sistemático

### Objetivo
Transformar el sistema a **forma escalonada por filas (REF)** y resolver por **[sustitución](../../../glossary.md#sustitucion) hacia atrás**.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Escribir [matriz](../../../glossary.md#matriz) aumentada | $(A \mid b)$ |
| 2 | Encontrar pivote | Primer elemento no nulo en columna |
| 3 | Hacer ceros debajo del pivote | $R_i - \frac{a_{i1}}{a_{11}}R_1 \to R_i$ |
| 4 | Repetir para cada columna | Avanzar a la siguiente columna |
| 5 | [Sustitución](../../../glossary.md#sustitucion) hacia atrás | Resolver desde la última ecuación |

### Ejemplo Detallado

**Problema:** Resolver el sistema:
$$\begin{cases} x + 2y + z = 9 \\ 2x + 5y + 3z = 22 \\ 3x + 6y + 4z = 28 \end{cases}$$

**Paso 1:** Escribimos la [matriz](../../../glossary.md#matriz) aumentada:
$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 9 \\ 2 & 5 & 3 & 22 \\ 3 & 6 & 4 & 28 \end{array}\right)$$

**Paso 2:** Hacemos ceros en la columna 1 debajo del pivote:

$R_2 - 2R_1 \to R_2$:
$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 9 \\ 0 & 1 & 1 & 4 \\ 3 & 6 & 4 & 28 \end{array}\right)$$

$R_3 - 3R_1 \to R_3$:
$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 9 \\ 0 & 1 & 1 & 4 \\ 0 & 0 & 1 & 1 \end{array}\right)$$

**Paso 3:** El sistema en forma escalonada es:
$$\begin{cases} x + 2y + z = 9 \\ y + z = 4 \\ z = 1 \end{cases}$$

**Paso 4:** Sustitución hacia atrás:
- De la ecuación 3: $z = 1$
- De la ecuación 2: $y + 1 = 4 \implies y = 3$
- De la ecuación 1: $x + 2(3) + 1 = 9 \implies x = 2$

**Resultado:**
$$\boxed{x = 2, \quad y = 3, \quad z = 1}$$

**Verificación:** $2 + 6 + 1 = 9$ ✓, $4 + 15 + 3 = 22$ ✓, $6 + 18 + 4 = 28$ ✓

---

## Método 2: Gauss-Jordan (Reducción a RREF)

### Cuándo Usar
- Cuando se desea la solución directa sin sustitución hacia atrás
- Para encontrar la inversa de una matriz

### Objetivo
Transformar a **forma escalonada reducida (RREF)**: todos los pivotes son 1 y tienen ceros arriba y abajo.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Aplicar eliminación gaussiana | Obtener REF |
| 2 | Hacer pivotes = 1 | Dividir cada fila por su pivote |
| 3 | Hacer ceros arriba de cada pivote | Eliminación hacia arriba |
| 4 | Leer solución directamente | Cada variable = valor en columna aumentada |

### Ejemplo Detallado

**Problema:** Resolver usando Gauss-Jordan:
$$\begin{cases} x + y - z = 2 \\ 2x - y + z = 1 \\ x - 2y + 2z = -1 \end{cases}$$

**Paso 1:** Matriz aumentada:
$$\left(\begin{array}{ccc|c} 1 & 1 & -1 & 2 \\ 2 & -1 & 1 & 1 \\ 1 & -2 & 2 & -1 \end{array}\right)$$

**Paso 2:** $R_2 - 2R_1 \to R_2$ y $R_3 - R_1 \to R_3$:
$$\left(\begin{array}{ccc|c} 1 & 1 & -1 & 2 \\ 0 & -3 & 3 & -3 \\ 0 & -3 & 3 & -3 \end{array}\right)$$

**Paso 3:** $R_3 - R_2 \to R_3$:
$$\left(\begin{array}{ccc|c} 1 & 1 & -1 & 2 \\ 0 & -3 & 3 & -3 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

**Paso 4:** $-\frac{1}{3}R_2 \to R_2$:
$$\left(\begin{array}{ccc|c} 1 & 1 & -1 & 2 \\ 0 & 1 & -1 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

**Paso 5:** $R_1 - R_2 \to R_1$:
$$\left(\begin{array}{ccc|c} 1 & 0 & 0 & 1 \\ 0 & 1 & -1 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

**Paso 6:** Interpretamos el resultado:
- Variables básicas (con pivote): $x$, $y$
- Variable libre (sin pivote): $z = t$

**Solución paramétrica:**
$$x = 1, \quad y = 1 + t, \quad z = t$$

O en forma vectorial:
$$\boxed{\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + t\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}, \quad t \in \mathbb{R}}$$

---

## Método 3: Clasificación de Sistemas

### Cuándo Usar
- Determinar si el sistema tiene solución única, infinitas o ninguna

### Criterio del Rango

Sea $A$ la matriz de coeficientes, $(A|b)$ la matriz aumentada, y $n$ el número de variables.

| Condición | Tipo de Sistema |
|-----------|-----------------|
| $\text{rango}(A) < \text{rango}(A|b)$ | **Incompatible** (sin solución) |
| $\text{rango}(A) = \text{rango}(A|b) = n$ | **Compatible determinado** (solución única) |
| $\text{rango}(A) = \text{rango}(A|b) < n$ | **Compatible indeterminado** (infinitas soluciones) |

### Identificación por RREF

| Patrón en RREF | Tipo |
|----------------|------|
| Fila $[0 \; 0 \; \cdots \; 0 \mid c]$ con $c \neq 0$ | Sin solución |
| Cada columna tiene pivote | Solución única |
| Columnas sin pivote | Variables libres → infinitas soluciones |

### Ejemplo Detallado: Sistema Incompatible

**Problema:** Clasificar el sistema:
$$\begin{cases} x + y + z = 1 \\ x + y + z = 2 \\ 2x + 2y + 2z = 5 \end{cases}$$

**Paso 1:** Matriz aumentada:
$$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 2 \\ 2 & 2 & 2 & 5 \end{array}\right)$$

**Paso 2:** $R_2 - R_1 \to R_2$ y $R_3 - 2R_1 \to R_3$:
$$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 3 \end{array}\right)$$

**Paso 3:** La fila 2 es $[0 \; 0 \; 0 \mid 1]$, que representa $0 = 1$ (contradicción).

**Resultado:** El sistema es **incompatible** (no tiene solución).

**Verificación de rangos:** $\text{rango}(A) = 1$, $\text{rango}(A|b) = 2$

---

## Método 4: Sistemas con Infinitas Soluciones

### Cuándo Usar
- $\text{rango}(A) = \text{rango}(A|b) < n$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Reducir a RREF | Identificar pivotes |
| 2 | Identificar variables básicas | Columnas con pivote |
| 3 | Identificar variables libres | Columnas sin pivote |
| 4 | Asignar parámetros | A cada variable libre |
| 5 | Despejar variables básicas | En términos de parámetros |
| 6 | Escribir solución vectorial | [Solución particular](../../../glossary.md#solucion-particular) + combinación de vectores |

### Ejemplo Detallado

**Problema:** Resolver:
$$\begin{cases} x_1 + 2x_2 - x_3 + x_4 = 3 \\ 2x_1 + 4x_2 + x_3 - 2x_4 = 1 \\ x_1 + 2x_2 + 2x_3 - 3x_4 = -2 \end{cases}$$

**Paso 1:** Matriz aumentada y reducción:
$$\left(\begin{array}{cccc|c} 1 & 2 & -1 & 1 & 3 \\ 2 & 4 & 1 & -2 & 1 \\ 1 & 2 & 2 & -3 & -2 \end{array}\right)$$

$R_2 - 2R_1 \to R_2$, $R_3 - R_1 \to R_3$:
$$\left(\begin{array}{cccc|c} 1 & 2 & -1 & 1 & 3 \\ 0 & 0 & 3 & -4 & -5 \\ 0 & 0 & 3 & -4 & -5 \end{array}\right)$$

$R_3 - R_2 \to R_3$:
$$\left(\begin{array}{cccc|c} 1 & 2 & -1 & 1 & 3 \\ 0 & 0 & 3 & -4 & -5 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right)$$

$\frac{1}{3}R_2 \to R_2$:
$$\left(\begin{array}{cccc|c} 1 & 2 & -1 & 1 & 3 \\ 0 & 0 & 1 & -\frac{4}{3} & -\frac{5}{3} \\ 0 & 0 & 0 & 0 & 0 \end{array}\right)$$

$R_1 + R_2 \to R_1$:
$$\left(\begin{array}{cccc|c} 1 & 2 & 0 & -\frac{1}{3} & \frac{4}{3} \\ 0 & 0 & 1 & -\frac{4}{3} & -\frac{5}{3} \\ 0 & 0 & 0 & 0 & 0 \end{array}\right)$$

**Paso 2-3:** Identificamos:
- Variables básicas (pivotes en columnas 1 y 3): $x_1$, $x_3$
- Variables libres (sin pivote en columnas 2 y 4): $x_2$, $x_4$

**Paso 4:** Asignamos parámetros: $x_2 = s$, $x_4 = t$

**Paso 5:** Despejamos:
$$x_3 = -\frac{5}{3} + \frac{4}{3}t$$
$$x_1 = \frac{4}{3} - 2s + \frac{1}{3}t$$

**Paso 6:** Solución vectorial:
$$\boxed{\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} = \begin{pmatrix} 4/3 \\ 0 \\ -5/3 \\ 0 \end{pmatrix} + s\begin{pmatrix} -2 \\ 1 \\ 0 \\ 0 \end{pmatrix} + t\begin{pmatrix} 1/3 \\ 0 \\ 4/3 \\ 1 \end{pmatrix}}$$

---

## Método 5: Sistemas Homogéneos ($Ax = 0$)

### Cuándo Usar
- Sistema con todos los términos independientes iguales a cero
- Encontrar el [núcleo (kernel)](../../../glossary.md#nucleo-kernel) de una matriz

### Propiedades
- **Siempre** tiene la solución [trivial](../../../glossary.md#trivial) $x = 0$
- Si $\text{rango}(A) < n$, tiene infinitas soluciones no triviales
- El conjunto solución es un **[subespacio](../../../glossary.md#subespacio) vectorial**

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Reducir $A$ a RREF | Sin columna aumentada |
| 2 | Identificar variables libres | Columnas sin pivote |
| 3 | Encontrar [base](../../../glossary.md#base) del núcleo | Un [vector](../../../glossary.md#vector) por cada variable libre |

### Ejemplo Detallado

**Problema:** Encontrar todas las soluciones de:
$$\begin{cases} x_1 + 2x_2 - x_3 = 0 \\ 2x_1 + 4x_2 + x_3 = 0 \\ 3x_1 + 6x_2 = 0 \end{cases}$$

**Paso 1:** Reducimos:
$$\begin{pmatrix} 1 & 2 & -1 \\ 2 & 4 & 1 \\ 3 & 6 & 0 \end{pmatrix} \xrightarrow{R_2-2R_1, R_3-3R_1} \begin{pmatrix} 1 & 2 & -1 \\ 0 & 0 & 3 \\ 0 & 0 & 3 \end{pmatrix}$$

$$\xrightarrow{R_3-R_2} \begin{pmatrix} 1 & 2 & -1 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{pmatrix} \xrightarrow{\frac{1}{3}R_2} \begin{pmatrix} 1 & 2 & -1 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$

$$\xrightarrow{R_1+R_2} \begin{pmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$

**Paso 2:** Variable libre: $x_2 = t$

**Paso 3:** De la RREF:
$$x_1 = -2t, \quad x_3 = 0$$

**Resultado:** El espacio solución es:
$$\boxed{\ker(A) = \text{span}\left\{\begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}\right\}}$$

[Dimensión](../../../glossary.md#dimension) del núcleo: $\dim(\ker A) = 1$ (una variable libre).

---

## Método 6: Matriz Inversa

### Cuándo Usar
- Sistemas $n \times n$ con $\det(A) \neq 0$
- Resolver múltiples sistemas con la misma matriz $A$

### Fórmula
$$Ax = b \implies x = A^{-1}b$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar que $\det(A) \neq 0$ | Sistema tiene solución única |
| 2 | Calcular $A^{-1}$ | Por Gauss-Jordan o adjunta |
| 3 | Multiplicar | $x = A^{-1}b$ |

### Ejemplo Detallado

**Problema:** Resolver usando la inversa:
$$\begin{cases} 2x + y = 5 \\ x + 3y = 10 \end{cases}$$

**Paso 1:** Verificamos: $\det(A) = 2(3) - 1(1) = 5 \neq 0$ ✓

**Paso 2:** Calculamos $A^{-1}$:
$$A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} \implies A^{-1} = \frac{1}{5}\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}$$

**Paso 3:** Multiplicamos:
$$x = A^{-1}b = \frac{1}{5}\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}\begin{pmatrix} 5 \\ 10 \end{pmatrix} = \frac{1}{5}\begin{pmatrix} 15 - 10 \\ -5 + 20 \end{pmatrix} = \frac{1}{5}\begin{pmatrix} 5 \\ 15 \end{pmatrix} = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$$

**Resultado:**
$$\boxed{x = 1, \quad y = 3}$$

---

## Método 7: Regla de Cramer

### Cuándo Usar
- Sistemas $n \times n$ con $\det(A) \neq 0$
- Calcular una variable específica sin resolver todo el sistema

### Fórmula
$$x_i = \frac{\det(A_i)}{\det(A)}$$

donde $A_i$ tiene la columna $i$ reemplazada por el [vector](../../../glossary.md#vector) $b$.

*Ver Método 7 de [Determinantes](../../../glossary.md#determinantes) para ejemplo detallado.*

---

## Método 8: Factorización LU

### Cuándo Usar
- Resolver múltiples sistemas $Ax = b_i$ con la misma $A$
- Eficiencia computacional

### Idea
Descomponer $A = LU$ donde:
- $L$: matriz triangular inferior con 1's en la diagonal
- $U$: matriz triangular superior

### Algoritmo de Resolución

| Paso | Acción | Sistema |
|------|--------|---------|
| 1 | [Factorizar](../../../glossary.md#factorizar) $A = LU$ | Durante eliminación gaussiana |
| 2 | Resolver $Ly = b$ | Sustitución hacia adelante |
| 3 | Resolver $Ux = y$ | Sustitución hacia atrás |

### Ejemplo Detallado

**Problema:** [Factorizar](../../../glossary.md#factorizar) y resolver:
$$\begin{cases} 2x + y + z = 1 \\ 4x + 3y + 3z = 1 \\ 8x + 7y + 9z = 5 \end{cases}$$

**Paso 1:** Eliminación guardando multiplicadores:

$R_2 - 2R_1 \to R_2$ (multiplicador = 2):
$$\begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 8 & 7 & 9 \end{pmatrix}$$

$R_3 - 4R_1 \to R_3$ (multiplicador = 4):
$$\begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 3 & 5 \end{pmatrix}$$

$R_3 - 3R_2 \to R_3$ (multiplicador = 3):
$$U = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix}$$

Los multiplicadores forman $L$:
$$L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{pmatrix}$$

**Paso 2:** Resolver $Ly = b$:
$$\begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{pmatrix}\begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 5 \end{pmatrix}$$

$y_1 = 1$, $y_2 = 1 - 2(1) = -1$, $y_3 = 5 - 4(1) - 3(-1) = 4$

**Paso 3:** Resolver $Ux = y$:
$$\begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 4 \end{pmatrix}$$

$z = 2$, $y = -1 - 2 = -3$, $x = \frac{1 - (-3) - 2}{2} = 1$

**Resultado:**
$$\boxed{x = 1, \quad y = -3, \quad z = 2}$$

---

## Método 9: Análisis de Sistemas Dependientes de Parámetros

### Cuándo Usar
- Sistemas con parámetros (letras en coeficientes)
- Determinar valores del parámetro para cada tipo de sistema

### Estrategia

| Paso | Acción |
|------|--------|
| 1 | Calcular $\det(A)$ en [función](../../../glossary.md#funcion) del parámetro |
| 2 | Encontrar valores críticos donde $\det = 0$ |
| 3 | Analizar cada caso por separado |

### Ejemplo Detallado

**Problema:** Para qué valores de $k$ el sistema tiene solución única, infinitas o ninguna:
$$\begin{cases} x + y + z = 1 \\ x + 2y + 3z = 1 \\ x + 2y + kz = 1 \end{cases}$$

**Paso 1:** Calculamos el [determinante](../../../glossary.md#determinante):
$$\det(A) = \det\begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 1 & 2 & k \end{pmatrix}$$

Expandiendo por la columna 1:
$$= 1(2k - 6) - 1(k - 2) + 1(3 - 2) = 2k - 6 - k + 2 + 1 = k - 3$$

**Paso 2:** El valor crítico es $k = 3$.

**Caso $k \neq 3$:** $\det(A) \neq 0$ → **Solución única**

**Caso $k = 3$:** Debemos analizar más:
$$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 1 & 2 & 3 & 1 \\ 1 & 2 & 3 & 1 \end{array}\right) \xrightarrow{R_2-R_1, R_3-R_1} \left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 0 \\ 0 & 1 & 2 & 0 \end{array}\right)$$

$R_3 - R_2 \to R_3$:
$$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 0 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

No hay contradicción, $\text{rango}(A) = \text{rango}(A|b) = 2 < 3$ → **Infinitas soluciones**

**Resultado:**
$$\boxed{\begin{cases} k \neq 3: & \text{Solución única} \\ k = 3: & \text{Infinitas soluciones} \end{cases}}$$

---

## Método 10: Verificación de Soluciones

### Cuándo Usar
- Siempre, al final de cualquier método
- Detectar errores de cálculo

### Algoritmo

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Sustituir la solución en cada ecuación | Una por una |
| 2 | Verificar que se cumplan todas las igualdades | LHS = RHS |
| 3 | Si hay parámetros | Verificar con valores específicos |

### Ejemplo

**Solución encontrada:** $x = 2$, $y = 3$, $z = 1$

**Sistema original:**
$$\begin{cases} x + 2y + z = 9 \\ 2x + 5y + 3z = 22 \\ 3x + 6y + 4z = 28 \end{cases}$$

**Verificación:**
- Ecuación 1: $2 + 2(3) + 1 = 2 + 6 + 1 = 9$ ✓
- Ecuación 2: $2(2) + 5(3) + 3(1) = 4 + 15 + 3 = 22$ ✓
- Ecuación 3: $3(2) + 6(3) + 4(1) = 6 + 18 + 4 = 28$ ✓

**Resultado:** La solución es **correcta**.
