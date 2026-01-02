<!--
::METADATA::
type: problem_set
topic_id: al-01-matrices
file_id: AL-01-Problemas
status: stable
audience: student
problem_count: 32
difficulty_distribution: {basico: 14, intermedio: 12, avanzado: 6}
-->

# Problemas de Matrices

> **Instrucciones:** Resuelve cada problema. Las soluciones se encuentran en `solutions/prob-XX/`.

---

## 1.1-1.2 Definición y Tipos

### [Prob-01] Elementos y dimensiones de una matriz ⭐

Dada $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$, determinar: (a) dimensiones, (b) $a_{12}$, (c) $a_{23}$.

> 📁 Solución: `solutions/prob-01/`

### [Prob-02] Identificación de tipos de matrices ⭐

Identificar el tipo de cada [matriz](../../../glossary.md#matriz):
   - $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$
   - $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix}$
   - $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$

> 📁 Solución: `solutions/prob-02/`

### [Prob-03] Matriz identidad ⭐

Escribir la [matriz identidad](../../../glossary.md#matriz-identidad) $I_4$.

> 📁 Solución: `solutions/prob-03/`

---

## 1.3 Operaciones Básicas

### [Prob-04] Suma de matrices ⭐

Calcular $A + B$ donde $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ y $B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$.

> 📁 Solución: `solutions/prob-04/`

### [Prob-05] Combinación lineal de matrices ⭐

Calcular $3A - 2B$ con las matrices del problema anterior.

> 📁 Solución: `solutions/prob-05/`

### [Prob-06] Producto escalar-matriz ⭐

Si $A = \begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix}$, hallar $2A$.

> 📁 Solución: `solutions/prob-06/`

### [Prob-07] Ecuación matricial lineal ⭐⭐

Resolver para $X$: $2X + A = B$ donde $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, $B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$.

> 📁 Solución: `solutions/prob-07/`

### [Prob-08] Sistema de ecuaciones matriciales ⭐⭐

Si $A + B = \begin{pmatrix} 5 & 3 \\ 2 & 7 \end{pmatrix}$ y $A - B = \begin{pmatrix} 1 & 1 \\ 0 & 3 \end{pmatrix}$, hallar $A$ y $B$.

> 📁 Solución: `solutions/prob-08/`

---

## 1.4 Multiplicación de Matrices

### [Prob-09] Producto de matrices 2×2 ⭐

Calcular $AB$ donde $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ y $B = \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix}$.

> 📁 Solución: `solutions/prob-09/`

### [Prob-10] No conmutatividad del producto ⭐

Calcular $BA$ con las matrices del problema anterior. ¿Es igual a $AB$?

> 📁 Solución: `solutions/prob-10/`

### [Prob-11] Producto fila por columna ⭐

Calcular $\begin{pmatrix} 1 & 2 & 3 \end{pmatrix} \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}$.

> 📁 Solución: `solutions/prob-11/`

### [Prob-12] Producto columna por fila ⭐

Calcular $\begin{pmatrix} 1 \\ 2 \end{pmatrix} \begin{pmatrix} 3 & 4 \end{pmatrix}$.

> 📁 Solución: `solutions/prob-12/`

### [Prob-13] Potencias de matrices ⭐⭐

Si $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$, calcular $A^2$ y $A^3$.

> 📁 Solución: `solutions/prob-13/`

### [Prob-14] Propiedad de la identidad ⭐⭐

Verificar que $AI = IA = A$ para $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.

> 📁 Solución: `solutions/prob-14/`

### [Prob-15] Producto de matrices rectangulares ⭐⭐

Calcular $\begin{pmatrix} 1 & 0 & 2 \\ 3 & 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \\ 4 & 0 \end{pmatrix}$.

> 📁 Solución: `solutions/prob-15/`

### [Prob-16] Matrices idempotentes ⭐⭐⭐

Si $A^2 = A$, demostrar que $(I - A)^2 = I - A$.

> 📁 Solución: `solutions/prob-16/`

### [Prob-17] Matrices que conmutan ⭐⭐⭐

Encontrar todas las matrices $2 \times 2$ que conmutan con $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

> 📁 Solución: `solutions/prob-17/`

---

## 1.5 Transpuesta

### [Prob-18] Transpuesta básica ⭐

Hallar $A^T$ para $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$.

> 📁 Solución: `solutions/prob-18/`

### [Prob-19] Doble transpuesta ⭐

Verificar que $(A^T)^T = A$ para $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix}$.

> 📁 Solución: `solutions/prob-19/`

### [Prob-20] Clasificación de matrices simétricas ⭐

Determinar si cada matriz es simétrica, antisimétrica o ninguna:
   - $\begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}$
   - $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$
   - $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$

> 📁 Solución: `solutions/prob-20/`

### [Prob-21] Transpuesta del producto ⭐⭐

Verificar que $(AB)^T = B^T A^T$ para $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, $B = \begin{pmatrix} 0 & 1 \\ 2 & 3 \end{pmatrix}$.

> 📁 Solución: `solutions/prob-21/`

### [Prob-22] Simetría de A + Aᵀ ⭐⭐

Demostrar que $A + A^T$ es simétrica para cualquier [matriz cuadrada](../../../glossary.md#matriz-cuadrada) $A$.

> 📁 Solución: `solutions/prob-22/`

### [Prob-23] Descomposición simétrica-antisimétrica ⭐⭐

Expresar $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ como suma de [matriz simétrica](../../../glossary.md#matriz-simétrica) y antisimétrica.

> 📁 Solución: `solutions/prob-23/`

---

## 1.6 Matriz Inversa

### [Prob-24] Inversa por fórmula 2×2 ⭐

Hallar la inversa de $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$.

> 📁 Solución: `solutions/prob-24/`

### [Prob-25] Inversa con determinante no unitario ⭐

Hallar la inversa de $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.

> 📁 Solución: `solutions/prob-25/`

### [Prob-26] Verificación de inversa ⭐

Verificar que $AA^{-1} = I$ para el resultado del problema anterior.

> 📁 Solución: `solutions/prob-26/`

### [Prob-27] Matriz singular ⭐⭐

Determinar si existe la inversa: $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$.

> 📁 Solución: `solutions/prob-27/`

### [Prob-28] Inversa por Gauss-Jordan 3×3 ⭐⭐

Usar Gauss-Jordan para encontrar la inversa de $A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{pmatrix}$.

> 📁 Solución: `solutions/prob-28/`

### [Prob-29] Sistema matricial AX = B ⭐⭐

Si $A$ es invertible, resolver $AX = B$ donde $B = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ y $A = \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix}$.

> 📁 Solución: `solutions/prob-29/`

### [Prob-30] Demostración AB = I implica BA = I ⭐⭐⭐

Demostrar que si $AB = I$, entonces $BA = I$ (para matrices cuadradas).

> 📁 Solución: `solutions/prob-30/`

### [Prob-31] Matrices involutivas ⭐⭐⭐

Si $A^2 = I$, demostrar que $A$ es su propia inversa.

> 📁 Solución: `solutions/prob-31/`

### [Prob-32] Inversa paramétrica ⭐⭐⭐

Encontrar la inversa de $\begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix}$.

> 📁 Solución: `solutions/prob-32/`
