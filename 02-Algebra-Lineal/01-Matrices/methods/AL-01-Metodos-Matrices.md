<!--
::METADATA::
type: method
topic_id: al-01-matrices
file_id: AL-01-Metodos-Matrices
status: stable
audience: student
last_updated: 2024-12-29
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Métodos de Cálculo con Matrices

> **Objetivo:** Dominar las operaciones matriciales con algoritmos detallados, cálculos intermedios y ejemplos clásicos paso a paso.

---

## Método 1: Suma y Resta de Matrices

### Cuándo Usar
- Combinar dos matrices de las **mismas dimensiones**

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar dimensiones | Deben ser iguales: $m \times n$ |
| 2 | Sumar/restar elemento a elemento | $(A \pm B)_{ij} = a_{ij} \pm b_{ij}$ |

### Ejemplo Detallado

**Problema:** Calcular $A + B$ donde:
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}, \quad B = \begin{pmatrix} 7 & 8 & 9 \\ 10 & 11 & 12 \end{pmatrix}$$

**Paso 1:** Verificamos dimensiones: $A$ es $2 \times 3$, $B$ es $2 \times 3$ ✓

**Paso 2:** Sumamos elemento a elemento:
$$A + B = \begin{pmatrix} 1+7 & 2+8 & 3+9 \\ 4+10 & 5+11 & 6+12 \end{pmatrix} = \boxed{\begin{pmatrix} 8 & 10 & 12 \\ 14 & 16 & 18 \end{pmatrix}}$$

---

## Método 2: Multiplicación por Escalar

### Cuándo Usar
- Escalar todos los elementos de una [matriz](../../../glossary.md#matriz) por un factor constante

### Fórmula
$$(kA)_{ij} = k \cdot a_{ij}$$

### Ejemplo Detallado

**Problema:** Calcular $3A$ donde $A = \begin{pmatrix} 1 & -2 \\ 4 & 5 \end{pmatrix}$

**Solución:**
$$3A = 3 \begin{pmatrix} 1 & -2 \\ 4 & 5 \end{pmatrix} = \begin{pmatrix} 3(1) & 3(-2) \\ 3(4) & 3(5) \end{pmatrix} = \boxed{\begin{pmatrix} 3 & -6 \\ 12 & 15 \end{pmatrix}}$$

---

## Método 3: Multiplicación de Matrices (Fila × Columna)

### Cuándo Usar
- [Composición](../../../glossary.md#composicion) de [transformaciones lineales](../../../glossary.md#transformaciones-lineales)
- Sistemas de ecuaciones
- Cambios de [base](../../../glossary.md#base)

### Requisito
Columnas de $A$ = Filas de $B$: $(m \times n) \cdot (n \times p) = (m \times p)$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar dimensiones | $A_{m \times n}$, $B_{n \times p}$ → resultado $m \times p$ |
| 2 | Para cada posición $(i,j)$ | Multiplicar fila $i$ de $A$ por columna $j$ de $B$ |
| 3 | Sumar productos | $(AB)_{ij} = \sum_{k=1}^n a_{ik} b_{kj}$ |

### Ejemplo Detallado

**Problema:** Calcular $AB$ donde:
$$A = \begin{pmatrix} 2 & 3 & 1 \\ 4 & 0 & 2 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 2 \\ 0 & 1 \\ 3 & 0 \end{pmatrix}$$

**Paso 1:** Verificamos dimensiones: $A_{2 \times 3} \cdot B_{3 \times 2} = C_{2 \times 2}$ ✓

**Paso 2:** Calculamos cada elemento:

**Elemento $(1,1)$:** Fila 1 de $A$ × Columna 1 de $B$
$$c_{11} = 2(1) + 3(0) + 1(3) = 2 + 0 + 3 = 5$$

**Elemento $(1,2)$:** Fila 1 de $A$ × Columna 2 de $B$
$$c_{12} = 2(2) + 3(1) + 1(0) = 4 + 3 + 0 = 7$$

**Elemento $(2,1)$:** Fila 2 de $A$ × Columna 1 de $B$
$$c_{21} = 4(1) + 0(0) + 2(3) = 4 + 0 + 6 = 10$$

**Elemento $(2,2)$:** Fila 2 de $A$ × Columna 2 de $B$
$$c_{22} = 4(2) + 0(1) + 2(0) = 8 + 0 + 0 = 8$$

**Resultado:**
$$AB = \boxed{\begin{pmatrix} 5 & 7 \\ 10 & 8 \end{pmatrix}}$$

> **Nota:** En general, $AB \neq BA$. La multiplicación de matrices **NO** es conmutativa.

---

## Método 4: Transpuesta de una Matriz

### Cuándo Usar
- Intercambiar filas por columnas
- Verificar simetría ($A = A^T$)
- Calcular $(AB)^T = B^T A^T$

### Fórmula
$$(A^T)_{ij} = a_{ji}$$

### Propiedades

| Propiedad | Fórmula |
|-----------|---------|
| Doble [transpuesta](../../../glossary.md#transpuesta) | $(A^T)^T = A$ |
| Suma | $(A + B)^T = A^T + B^T$ |
| Escalar | $(kA)^T = kA^T$ |
| Producto | $(AB)^T = B^T A^T$ |

### Ejemplo Detallado

**Problema:** Encontrar $A^T$ para $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$

**Solución:** La fila $i$ se convierte en columna $i$:

$$A^T = \boxed{\begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}}$$

**Verificación de dimensiones:** $A_{2 \times 3} \rightarrow A^T_{3 \times 2}$ ✓

---

## Método 5: Inversa de Matriz $2 \times 2$ (Fórmula Directa)

### Cuándo Usar
- Matrices pequeñas $2 \times 2$
- Cálculo rápido cuando $\det(A) \neq 0$

### Fórmula
$$A^{-1} = \frac{1}{\det(A)}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \quad \text{donde } A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Calcular [determinante](../../../glossary.md#determinante) | $\det(A) = ad - bc$ |
| 2 | Verificar invertibilidad | Si $\det = 0$, no existe inversa |
| 3 | Intercambiar diagonal principal | $a \leftrightarrow d$ |
| 4 | Cambiar signo diagonal secundaria | $b \to -b$, $c \to -c$ |
| 5 | Dividir entre [determinante](../../../glossary.md#determinante) | Multiplicar por $\frac{1}{\det(A)}$ |

### Ejemplo Detallado

**Problema:** Encontrar la inversa de $A = \begin{pmatrix} 4 & 3 \\ 2 & 1 \end{pmatrix}$

**Paso 1:** Calculamos el determinante:
$$\det(A) = 4(1) - 3(2) = 4 - 6 = -2$$

**Paso 2:** Como $\det(A) = -2 \neq 0$, la inversa existe.

**Paso 3-4:** Formamos la [matriz](../../../glossary.md#matriz) adjunta:
$$\text{adj}(A) = \begin{pmatrix} 1 & -3 \\ -2 & 4 \end{pmatrix}$$

**Paso 5:** Dividimos entre el determinante:
$$A^{-1} = \frac{1}{-2}\begin{pmatrix} 1 & -3 \\ -2 & 4 \end{pmatrix} = \boxed{\begin{pmatrix} -1/2 & 3/2 \\ 1 & -2 \end{pmatrix}}$$

**Verificación:** $AA^{-1} = I$
$$\begin{pmatrix} 4 & 3 \\ 2 & 1 \end{pmatrix}\begin{pmatrix} -1/2 & 3/2 \\ 1 & -2 \end{pmatrix} = \begin{pmatrix} -2+3 & 6-6 \\ -1+1 & 3-2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$ ✓

---

## Método 6: Inversa por Gauss-Jordan

### Cuándo Usar
- Matrices de cualquier tamaño $n \times n$
- Método sistemático y general

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Formar matriz aumentada | $(A \mid I_n)$ |
| 2 | Aplicar operaciones elementales | Intercambiar filas, multiplicar por escalar, sumar múltiplos |
| 3 | Reducir a forma escalonada reducida | RREF en el lado izquierdo |
| 4 | Leer la inversa | Si $(I_n \mid B)$, entonces $B = A^{-1}$ |

### Operaciones Elementales de Fila

| Operación | Notación | Descripción |
|-----------|----------|-------------|
| Intercambio | $R_i \leftrightarrow R_j$ | Intercambiar filas $i$ y $j$ |
| Escalamiento | $kR_i \to R_i$ | Multiplicar fila $i$ por $k \neq 0$ |
| Reemplazo | $R_i + kR_j \to R_i$ | Sumar $k$ veces la fila $j$ a la fila $i$ |

### Ejemplo Detallado

**Problema:** Encontrar la inversa de $A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 5 & 3 \\ 1 & 3 & 2 \end{pmatrix}$

**Paso 1:** Formamos $(A \mid I)$:
$$\left(\begin{array}{ccc|ccc} 1 & 2 & 1 & 1 & 0 & 0 \\ 2 & 5 & 3 & 0 & 1 & 0 \\ 1 & 3 & 2 & 0 & 0 & 1 \end{array}\right)$$

**Paso 2:** $R_2 - 2R_1 \to R_2$ y $R_3 - R_1 \to R_3$:
$$\left(\begin{array}{ccc|ccc} 1 & 2 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & -2 & 1 & 0 \\ 0 & 1 & 1 & -1 & 0 & 1 \end{array}\right)$$

**Paso 3:** $R_3 - R_2 \to R_3$:
$$\left(\begin{array}{ccc|ccc} 1 & 2 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & -2 & 1 & 0 \\ 0 & 0 & 0 & 1 & -1 & 1 \end{array}\right)$$

**Observación:** La tercera fila del lado izquierdo es $[0 \; 0 \; 0]$, lo que significa que $\det(A) = 0$.

**Resultado:** La matriz $A$ **no es invertible**.

---

### Ejemplo donde SÍ existe inversa

**Problema:** Encontrar la inversa de $A = \begin{pmatrix} 1 & 2 \\ 3 & 7 \end{pmatrix}$

**Paso 1:** Formamos $(A \mid I)$:
$$\left(\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 3 & 7 & 0 & 1 \end{array}\right)$$

**Paso 2:** $R_2 - 3R_1 \to R_2$:
$$\left(\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & 1 & -3 & 1 \end{array}\right)$$

**Paso 3:** $R_1 - 2R_2 \to R_1$:
$$\left(\begin{array}{cc|cc} 1 & 0 & 7 & -2 \\ 0 & 1 & -3 & 1 \end{array}\right)$$

**Resultado:**
$$A^{-1} = \boxed{\begin{pmatrix} 7 & -2 \\ -3 & 1 \end{pmatrix}}$$

**Verificación:** $\det(A) = 1(7) - 2(3) = 1 \neq 0$ ✓

---

## Método 7: Rango de una Matriz

### Cuándo Usar
- Determinar la [dimensión](../../../glossary.md#dimension) del espacio columna
- Verificar [independencia lineal](../../../glossary.md#independencia-lineal)
- Analizar sistemas de ecuaciones

### Definición
El **rango** de $A$ es el número de pivotes (filas no nulas) en su forma escalonada.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Reducir a forma escalonada | Usar eliminación gaussiana |
| 2 | Contar filas con pivote | Filas no nulas |

### Ejemplo Detallado

**Problema:** Encontrar el rango de $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 3 & 4 \end{pmatrix}$

**Paso 1:** Reducimos:

$R_2 - 2R_1 \to R_2$ y $R_3 - R_1 \to R_3$:
$$\begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$

Intercambiamos $R_2 \leftrightarrow R_3$:
$$\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$

**Paso 2:** Contamos filas no nulas: **2 pivotes**

**Resultado:** $\text{rango}(A) = \boxed{2}$

**Interpretación:** Las filas de $A$ son linealmente dependientes (la fila 2 es el doble de la fila 1).

---

## Método 8: Potencias de Matrices

### Cuándo Usar
- Calcular $A^n$ para $n$ grande
- Modelos de Markov, series de tiempo discretas

### Métodos

**Para potencias pequeñas:** Multiplicar sucesivamente $A^2 = A \cdot A$, $A^3 = A^2 \cdot A$, etc.

**Para matrices diagonalizables:** Si $A = PDP^{-1}$ donde $D$ es diagonal:
$$A^n = PD^nP^{-1}$$

### Ejemplo Detallado

**Problema:** Calcular $A^3$ donde $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$

**Paso 1:** Calculamos $A^2$:
$$A^2 = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$$

**Paso 2:** Calculamos $A^3 = A^2 \cdot A$:
$$A^3 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}$$

**Resultado:**
$$A^3 = \boxed{\begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}}$$

> **Patrón observado:** Para esta matriz triangular, $A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$

---

## Método 9: Tipos Especiales de Matrices

### Matrices Simétricas ($A = A^T$)

**Verificación:** Comparar elemento $(i,j)$ con elemento $(j,i)$

**Ejemplo:** $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 5 \\ 3 & 5 & 6 \end{pmatrix}$ es simétrica porque $a_{12} = a_{21} = 2$, etc.

### Matrices Ortogonales ($A^T A = I$)

**Propiedad:** $A^{-1} = A^T$

**Verificación:** Las columnas forman un conjunto ortonormal.

**Ejemplo:**
$$A = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$
es ortogonal (matriz de rotación).

### Matrices Idempotentes ($A^2 = A$)

**Ejemplo:** Las matrices de proyección son idempotentes.

---

## Método 10: Matriz de Cofactores y Adjunta

### Cuándo Usar
- Calcular inversas de matrices $n \times n$
- Fórmula $A^{-1} = \frac{1}{\det(A)}\text{adj}(A)$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Calcular menores $M_{ij}$ | Determinante de submatriz sin fila $i$ y columna $j$ |
| 2 | Calcular cofactores | $C_{ij} = (-1)^{i+j} M_{ij}$ |
| 3 | Formar matriz de cofactores | Colocar $C_{ij}$ en posición $(i,j)$ |
| 4 | Transponer | $\text{adj}(A) = C^T$ |

### Patrón de Signos
$$\begin{pmatrix} + & - & + & \cdots \\ - & + & - & \cdots \\ + & - & + & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}$$

### Ejemplo Detallado

**Problema:** Encontrar $\text{adj}(A)$ para $A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 1 & 0 & 6 \end{pmatrix}$

**Paso 1-2:** Calculamos cada [cofactor](../../../glossary.md#cofactor):

$$C_{11} = (+1)\begin{vmatrix} 4 & 5 \\ 0 & 6 \end{vmatrix} = 24$$

$$C_{12} = (-1)\begin{vmatrix} 0 & 5 \\ 1 & 6 \end{vmatrix} = -(-5) = 5$$

$$C_{13} = (+1)\begin{vmatrix} 0 & 4 \\ 1 & 0 \end{vmatrix} = -4$$

$$C_{21} = (-1)\begin{vmatrix} 2 & 3 \\ 0 & 6 \end{vmatrix} = -12$$

$$C_{22} = (+1)\begin{vmatrix} 1 & 3 \\ 1 & 6 \end{vmatrix} = 3$$

$$C_{23} = (-1)\begin{vmatrix} 1 & 2 \\ 1 & 0 \end{vmatrix} = -(-2) = 2$$

$$C_{31} = (+1)\begin{vmatrix} 2 & 3 \\ 4 & 5 \end{vmatrix} = -2$$

$$C_{32} = (-1)\begin{vmatrix} 1 & 3 \\ 0 & 5 \end{vmatrix} = -5$$

$$C_{33} = (+1)\begin{vmatrix} 1 & 2 \\ 0 & 4 \end{vmatrix} = 4$$

**Paso 3:** Matriz de cofactores:
$$C = \begin{pmatrix} 24 & 5 & -4 \\ -12 & 3 & 2 \\ -2 & -5 & 4 \end{pmatrix}$$

**Paso 4:** Transponemos:
$$\text{adj}(A) = \boxed{\begin{pmatrix} 24 & -12 & -2 \\ 5 & 3 & -5 \\ -4 & 2 & 4 \end{pmatrix}}$$

---

## Método 11: Verificar si una Matriz es Invertible

### Criterios Equivalentes
Una matriz $A$ de $n \times n$ es invertible si y solo si:

| Criterio | Condición |
|----------|-----------|
| Determinante | $\det(A) \neq 0$ |
| Rango | $\text{rango}(A) = n$ |
| Núcleo | $\ker(A) = \{0\}$ (solo solución [trivial](../../../glossary.md#trivial) para $Ax = 0$) |
| Columnas | Son linealmente independientes |
| Filas | Son linealmente independientes |
| RREF | Se puede reducir a $I_n$ |

### Ejemplo Detallado

**Problema:** ¿Es $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$ invertible?

**Método 1 (Determinante):**
$$\det(A) = 1(45-48) - 2(36-42) + 3(32-35) = -3 + 12 - 9 = 0$$

**Resultado:** Como $\det(A) = 0$, la matriz **NO es invertible**.

**Verificación alternativa (Dependencia):** Notamos que Fila 3 = 2(Fila 2) - Fila 1:
$$\begin{pmatrix} 7 & 8 & 9 \end{pmatrix} = 2\begin{pmatrix} 4 & 5 & 6 \end{pmatrix} - \begin{pmatrix} 1 & 2 & 3 \end{pmatrix}$$ ✓
