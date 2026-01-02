<!--
::METADATA::
type: problem_set
topic_id: al-04-espacios-vectoriales
file_id: AL-04-Problemas
status: stable
audience: student
-->

# Problemas: Espacios Vectoriales

> Colección de problemas graduados por dificultad para [espacios vectoriales](../../../glossary.md#espacios-vectoriales).

---

## 4.1 Axiomas y Definición

### [Prob-01] Verificación de axiomas en R² ⭐

Verificar los axiomas de [espacio vectorial](../../../glossary.md#espacio-vectorial) para $\mathbb{R}^2$ con las operaciones usuales.

📁 **Solución:** [solutions/prob-01/](../solutions/prob-01/)

---

### [Prob-02] Espacio vectorial con operaciones no usuales ⭐⭐

Sea $V = \{(x, y) : x, y > 0\}$ con operaciones:
- $(x_1, y_1) \oplus (x_2, y_2) = (x_1 x_2, y_1 y_2)$
- $c \odot (x, y) = (x^c, y^c)$

Verificar si es [espacio vectorial](../../../glossary.md#espacio-vectorial) sobre $\mathbb{R}$.

📁 **Solución:** [solutions/prob-02/](../solutions/prob-02/)

---

### [Prob-03] Vectores con coordenadas enteras ⭐

¿Es $\mathbb{Z}^n$ (vectores con coordenadas enteras) un espacio vectorial sobre $\mathbb{R}$? Justificar.

📁 **Solución:** [solutions/prob-03/](../solutions/prob-03/)

---

## 4.2 Subespacios

### [Prob-04] Identificación de subespacios en R³ ⭐⭐

Determinar si los siguientes son subespacios de $\mathbb{R}^3$:

a) $W_1 = \{(x, y, z) : x + y + z = 0\}$

b) $W_2 = \{(x, y, z) : x + y + z = 1\}$

c) $W_3 = \{(x, y, z) : xy = 0\}$

d) $W_4 = \{(x, y, z) : x = 2y\}$

📁 **Solución:** [solutions/prob-04/](../solutions/prob-04/)

---

### [Prob-05] Matrices simétricas como subespacio ⭐

¿Es $W = \{A \in M_{2\times 2} : A^T = A\}$ (matrices simétricas) [subespacio](../../../glossary.md#subespacio) de $M_{2\times 2}$?

📁 **Solución:** [solutions/prob-05/](../solutions/prob-05/)

---

### [Prob-06] Polinomios con raíz en cero ⭐

¿Es $W = \{p(x) \in P_3 : p(0) = 0\}$ [subespacio](../../../glossary.md#subespacio) de $P_3$?

📁 **Solución:** [solutions/prob-06/](../solutions/prob-06/)

---

### [Prob-07] Espacio nulo como subespacio ⭐⭐

Sea $A$ una [matriz](../../../glossary.md#matriz) $m \times n$. Demostrar que $\text{Nul}(A)$ es subespacio de $\mathbb{R}^n$.

📁 **Solución:** [solutions/prob-07/](../solutions/prob-07/)

---

### [Prob-08] Bola unitaria como subespacio ⭐

Determinar si $W = \{(x, y, z) : x^2 + y^2 + z^2 \leq 1\}$ es subespacio de $\mathbb{R}^3$.

📁 **Solución:** [solutions/prob-08/](../solutions/prob-08/)

---

## 4.3 Combinaciones Lineales y Span

### [Prob-09] Verificar combinación lineal ⭐

¿Es $v = (1, 2, 3)$ [combinación lineal](../../../glossary.md#combinacion-lineal) de $u_1 = (1, 0, 1)$ y $u_2 = (0, 1, 1)$?

📁 **Solución:** [solutions/prob-09/](../solutions/prob-09/)

---

### [Prob-10] Expresar como combinación lineal ⭐

Escribir $(7, 4, 5)$ como [combinación lineal](../../../glossary.md#combinacion-lineal) de $(1, 1, 1)$, $(1, 1, 0)$, $(1, 0, 0)$.

📁 **Solución:** [solutions/prob-10/](../solutions/prob-10/)

---

### [Prob-11] Interpretación geométrica del span ⭐

Determinar $\text{span}\{(1, 2), (2, 4)\}$ geométricamente.

📁 **Solución:** [solutions/prob-11/](../solutions/prob-11/)

---

### [Prob-12] Span y generación de R³ ⭐⭐

¿Es $\mathbb{R}^3 = \text{span}\{(1, 0, 0), (1, 1, 0), (1, 1, 1)\}$?

📁 **Solución:** [solutions/prob-12/](../solutions/prob-12/)

---

### [Prob-13] Span en espacio de polinomios ⭐⭐

Encontrar $\text{span}\{1 + x, x + x^2, 1 + x^2\}$ en $P_2$.

📁 **Solución:** [solutions/prob-13/](../solutions/prob-13/)

---

## 4.4 Independencia Lineal

### [Prob-14] Determinar independencia lineal ⭐

Determinar si son LI o LD:

a) $(1, 2)$, $(3, 6)$

b) $(1, 0, 0)$, $(0, 1, 0)$, $(0, 0, 1)$

c) $(1, 1, 0)$, $(0, 1, 1)$, $(1, 0, 1)$

📁 **Solución:** [solutions/prob-14/](../solutions/prob-14/)

---

### [Prob-15] Independencia lineal de matrices base ⭐

¿Son las matrices $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$, $\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ LI?

📁 **Solución:** [solutions/prob-15/](../solutions/prob-15/)

---

### [Prob-16] Dependencia lineal parametrizada ⭐⭐

Determinar para qué valores de $k$ los vectores $(1, k, 0)$, $(0, 1, k)$, $(k, 0, 1)$ son LD.

📁 **Solución:** [solutions/prob-16/](../solutions/prob-16/)

---

### [Prob-17] Preservación de independencia lineal ⭐⭐⭐

Demostrar que si $\{v_1, v_2, v_3\}$ es LI, entonces $\{v_1, v_1 + v_2, v_1 + v_2 + v_3\}$ también es LI.

📁 **Solución:** [solutions/prob-17/](../solutions/prob-17/)

---

### [Prob-18] Independencia en espacio de funciones ⭐⭐

¿Son $1$, $\sin^2(x)$, $\cos^2(x)$ LI en el espacio de funciones continuas?

📁 **Solución:** [solutions/prob-18/](../solutions/prob-18/)

---

## 4.5 Bases y Dimensión

### [Prob-19] Base y dimensión de subespacios ⭐⭐

Encontrar una [base](../../../glossary.md#base) y la [dimensión](../../../glossary.md#dimension) de:

a) $W = \{(x, y, z) : x - 2y + z = 0\}$

b) $W = \{(x, y, z, w) : x + y = 0, z + w = 0\}$

📁 **Solución:** [solutions/prob-19/](../solutions/prob-19/)

---

### [Prob-20] Base de matrices simétricas ⭐⭐

Encontrar una [base](../../../glossary.md#base) para el espacio de matrices simétricas $2 \times 2$. ¿Cuál es su [dimensión](../../../glossary.md#dimension)?

📁 **Solución:** [solutions/prob-20/](../solutions/prob-20/)

---

### [Prob-21] Base del espacio nulo ⭐⭐

Encontrar base y dimensión de $\text{Nul}(A)$ donde:

$$A = \begin{pmatrix} 1 & 2 & -1 & 3 \\ 2 & 4 & -2 & 6 \end{pmatrix}$$

📁 **Solución:** [solutions/prob-21/](../solutions/prob-21/)

---

### [Prob-22] Base del espacio columna ⭐⭐

Encontrar base de $\text{Col}(A)$ donde:

$$A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 3 \end{pmatrix}$$

📁 **Solución:** [solutions/prob-22/](../solutions/prob-22/)

---

### [Prob-23] Extensión de base ⭐

Si $\dim(V) = 5$ y $W$ es subespacio con $\dim(W) = 3$, ¿cuántos vectores se necesitan para extender una base de $W$ a una base de $V$?

📁 **Solución:** [solutions/prob-23/](../solutions/prob-23/)

---

### [Prob-24] Dimensión del espacio de polinomios ⭐

Determinar la dimensión de $P_n(x)$ y dar una base.

📁 **Solución:** [solutions/prob-24/](../solutions/prob-24/)

---

## 4.6 Coordenadas y Cambio de Base

### [Prob-25] Coordenadas respecto a base ordenada ⭐⭐

Sea $\mathcal{B} = \{(1, 1), (1, -1)\}$ base de $\mathbb{R}^2$. Encontrar $[v]_{\mathcal{B}}$ para:

a) $v = (4, 2)$

b) $v = (1, 0)$

📁 **Solución:** [solutions/prob-25/](../solutions/prob-25/)

---

### [Prob-26] Coordenadas en espacio de polinomios ⭐⭐

Sea $\mathcal{B} = \{1, 1+x, 1+x+x^2\}$ base de $P_2$. Encontrar $[p]_{\mathcal{B}}$ para $p(x) = 2 + 3x + x^2$.

📁 **Solución:** [solutions/prob-26/](../solutions/prob-26/)

---

### [Prob-27] Matriz de cambio de base ⭐⭐

Encontrar la [matriz](../../../glossary.md#matriz) de cambio de base de $\mathcal{B} = \{(1, 0), (0, 1)\}$ a $\mathcal{B}' = \{(1, 1), (2, 1)\}$.

📁 **Solución:** [solutions/prob-27/](../solutions/prob-27/)

---

### [Prob-28] Aplicación de matriz de transición ⭐⭐

Si $[v]_{\mathcal{B}} = \begin{pmatrix} 3 \\ -2 \end{pmatrix}$ y $P_{\mathcal{B} \to \mathcal{B}'} = \begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix}$, encontrar $[v]_{\mathcal{B}'}$.

📁 **Solución:** [solutions/prob-28/](../solutions/prob-28/)

---

### [Prob-29] Matriz de transición a base estándar ⭐⭐⭐

Sea $\mathcal{B} = \{(1, 0, 0), (1, 1, 0), (1, 1, 1)\}$. Encontrar $P_{\mathcal{E} \to \mathcal{B}}$ donde $\mathcal{E}$ es la base estándar.

📁 **Solución:** [solutions/prob-29/](../solutions/prob-29/)

---

## 4.7 Problemas de Aplicación

### [Prob-30] Espacios vectoriales en circuitos eléctricos ⭐⭐⭐

En un circuito eléctrico, las corrientes satisfacen ciertas ecuaciones de Kirchhoff. Si las soluciones forman un subespacio de dimensión 2 en $\mathbb{R}^5$, ¿cuántas ecuaciones independientes hay?

📁 **Solución:** [solutions/prob-30/](../solutions/prob-30/)

---

### [Prob-31] Ecuaciones diferenciales y espacios solución ⭐⭐⭐

El espacio de soluciones de una [ecuación diferencial](../../../glossary.md#ecuacion-diferencial) lineal homogénea de [orden](../../../glossary.md#orden) $n$ tiene dimensión $n$. Si $y_1 = e^x$ y $y_2 = e^{-x}$ son soluciones de una [EDO](../../../glossary.md#edo) de orden 2, ¿forman base del espacio solución?

📁 **Solución:** [solutions/prob-31/](../solutions/prob-31/)

---

### [Prob-32] Compresión de imágenes y subespacios ⭐⭐⭐

En compresión de imágenes, una imagen de $m \times n$ píxeles puede verse como [vector](../../../glossary.md#vector) en $\mathbb{R}^{mn}$. Si queremos representarla con $k < mn$ coeficientes, ¿qué estructura algebraica usamos?

📁 **Solución:** [solutions/prob-32/](../solutions/prob-32/)

---

## Resumen de Problemas

| Sección | Problemas | Dificultad |
|---------|-----------|------------|
| 4.1 Axiomas y Definición | Prob-01 a Prob-03 | ⭐ a ⭐⭐ |
| 4.2 Subespacios | Prob-04 a Prob-08 | ⭐ a ⭐⭐ |
| 4.3 Combinaciones Lineales y Span | Prob-09 a Prob-13 | ⭐ a ⭐⭐ |
| 4.4 [Independencia Lineal](../../../glossary.md#independencia-lineal) | Prob-14 a Prob-18 | ⭐ a ⭐⭐⭐ |
| 4.5 Bases y Dimensión | Prob-19 a Prob-24 | ⭐ a ⭐⭐ |
| 4.6 Coordenadas y Cambio de Base | Prob-25 a Prob-29 | ⭐⭐ a ⭐⭐⭐ |
| 4.7 Aplicaciones | Prob-30 a Prob-32 | ⭐⭐⭐ |
