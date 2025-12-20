<!--
content_type: problems
topic: Espacios Vectoriales
difficulty: graduated
---
-->

# Problemas: Espacios Vectoriales

---

## 4.1 Axiomas y Definición

### Problema 1
Verificar los axiomas de espacio vectorial para $\mathbb{R}^2$ con las operaciones usuales.

### Problema 2
Sea $V = \{(x, y) : x, y > 0\}$ con operaciones:
- $(x_1, y_1) \oplus (x_2, y_2) = (x_1 x_2, y_1 y_2)$
- $c \odot (x, y) = (x^c, y^c)$

Verificar si es espacio vectorial sobre $\mathbb{R}$.

### Problema 3
¿Es $\mathbb{Z}^n$ (vectores con coordenadas enteras) un espacio vectorial sobre $\mathbb{R}$? Justificar.

---

## 4.2 Subespacios

### Problema 4
Determinar si los siguientes son subespacios de $\mathbb{R}^3$:
a) $W_1 = \{(x, y, z) : x + y + z = 0\}$
b) $W_2 = \{(x, y, z) : x + y + z = 1\}$
c) $W_3 = \{(x, y, z) : xy = 0\}$
d) $W_4 = \{(x, y, z) : x = 2y\}$

### Problema 5
¿Es $W = \{A \in M_{2\times 2} : A^T = A\}$ (matrices simétricas) subespacio de $M_{2\times 2}$?

### Problema 6
¿Es $W = \{p(x) \in P_3 : p(0) = 0\}$ subespacio de $P_3$?

### Problema 7
Sea $A$ una matriz $m \times n$. Demostrar que $\text{Nul}(A)$ es subespacio de $\mathbb{R}^n$.

### Problema 8
Determinar si $W = \{(x, y, z) : x^2 + y^2 + z^2 \leq 1\}$ es subespacio de $\mathbb{R}^3$.

---

## 4.3 Combinaciones Lineales y Span

### Problema 9
¿Es $v = (1, 2, 3)$ combinación lineal de $u_1 = (1, 0, 1)$ y $u_2 = (0, 1, 1)$?

### Problema 10
Escribir $(7, 4, 5)$ como combinación lineal de $(1, 1, 1)$, $(1, 1, 0)$, $(1, 0, 0)$.

### Problema 11
Determinar $\text{span}\{(1, 2), (2, 4)\}$ geométricamente.

### Problema 12
¿Es $\mathbb{R}^3 = \text{span}\{(1, 0, 0), (1, 1, 0), (1, 1, 1)\}$?

### Problema 13
Encontrar $\text{span}\{1 + x, x + x^2, 1 + x^2\}$ en $P_2$.

---

## 4.4 Independencia Lineal

### Problema 14
Determinar si son LI o LD:
a) $(1, 2)$, $(3, 6)$
b) $(1, 0, 0)$, $(0, 1, 0)$, $(0, 0, 1)$
c) $(1, 1, 0)$, $(0, 1, 1)$, $(1, 0, 1)$

### Problema 15
¿Son las matrices $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$, $\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ LI?

### Problema 16
Determinar para qué valores de $k$ los vectores $(1, k, 0)$, $(0, 1, k)$, $(k, 0, 1)$ son LD.

### Problema 17
Demostrar que si $\{v_1, v_2, v_3\}$ es LI, entonces $\{v_1, v_1 + v_2, v_1 + v_2 + v_3\}$ también es LI.

### Problema 18
¿Son $1$, $\sin^2(x)$, $\cos^2(x)$ LI en el espacio de funciones continuas?

---

## 4.5 Bases y Dimensión

### Problema 19
Encontrar una base y la dimensión de:
a) $W = \{(x, y, z) : x - 2y + z = 0\}$
b) $W = \{(x, y, z, w) : x + y = 0, z + w = 0\}$

### Problema 20
Encontrar una base para el espacio de matrices simétricas $2 \times 2$. ¿Cuál es su dimensión?

### Problema 21
Encontrar base y dimensión de $\text{Nul}(A)$ donde:
$$A = \begin{pmatrix} 1 & 2 & -1 & 3 \\ 2 & 4 & -2 & 6 \end{pmatrix}$$

### Problema 22
Encontrar base de $\text{Col}(A)$ donde:
$$A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 3 \end{pmatrix}$$

### Problema 23
Si $\dim(V) = 5$ y $W$ es subespacio con $\dim(W) = 3$, ¿cuántos vectores se necesitan para extender una base de $W$ a una base de $V$?

### Problema 24
Determinar la dimensión de $P_n(x)$ y dar una base.

---

## 4.6 Coordenadas y Cambio de Base

### Problema 25
Sea $\mathcal{B} = \{(1, 1), (1, -1)\}$ base de $\mathbb{R}^2$. Encontrar $[v]_{\mathcal{B}}$ para:
a) $v = (4, 2)$
b) $v = (1, 0)$

### Problema 26
Sea $\mathcal{B} = \{1, 1+x, 1+x+x^2\}$ base de $P_2$. Encontrar $[p]_{\mathcal{B}}$ para $p(x) = 2 + 3x + x^2$.

### Problema 27
Encontrar la matriz de cambio de base de $\mathcal{B} = \{(1, 0), (0, 1)\}$ a $\mathcal{B}' = \{(1, 1), (2, 1)\}$.

### Problema 28
Si $[v]_{\mathcal{B}} = \begin{pmatrix} 3 \\ -2 \end{pmatrix}$ y $P_{\mathcal{B} \to \mathcal{B}'} = \begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix}$, encontrar $[v]_{\mathcal{B}'}$.

### Problema 29
Sea $\mathcal{B} = \{(1, 0, 0), (1, 1, 0), (1, 1, 1)\}$. Encontrar $P_{\mathcal{E} \to \mathcal{B}}$ donde $\mathcal{E}$ es la base estándar.

---

## Problemas de Aplicación

### Problema 30
En un circuito eléctrico, las corrientes satisfacen ciertas ecuaciones de Kirchhoff. Si las soluciones forman un subespacio de dimensión 2 en $\mathbb{R}^5$, ¿cuántas ecuaciones independientes hay?

### Problema 31
El espacio de soluciones de una ecuación diferencial lineal homogénea de orden $n$ tiene dimensión $n$. Si $y_1 = e^x$ y $y_2 = e^{-x}$ son soluciones de una EDO de orden 2, ¿forman base del espacio solución?

### Problema 32
En compresión de imágenes, una imagen de $m \times n$ píxeles puede verse como vector en $\mathbb{R}^{mn}$. Si queremos representarla con $k < mn$ coeficientes, ¿qué estructura algebraica usamos?
