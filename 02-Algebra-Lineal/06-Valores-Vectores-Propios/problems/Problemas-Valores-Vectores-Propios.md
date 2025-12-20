<!--
content_type: problems
topic: Valores y Vectores Propios
difficulty: graduated
---
-->

# Problemas: Valores y Vectores Propios

---

## 6.1 Eigenvalores y Eigenvectores Básicos

### Problema 1
Verificar que $v = (1, 2)^T$ es eigenvector de $A = \begin{pmatrix} 3 & 1 \\ 2 & 2 \end{pmatrix}$ y encontrar el eigenvalor asociado.

### Problema 2
Encontrar los eigenvalores de:
a) $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$
b) $B = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$
c) $C = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$

### Problema 3
Para cada matriz del problema 2, encontrar los eigenvectores asociados a cada eigenvalor.

### Problema 4
Encontrar eigenvalores y eigenvectores de:
$$A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$$

### Problema 5
Si $\lambda$ es eigenvalor de $A$, demostrar que $\lambda^2$ es eigenvalor de $A^2$.

---

## 6.2 Polinomio Característico

### Problema 6
Escribir el polinomio característico de:
a) $\begin{pmatrix} a & b \\ b & a \end{pmatrix}$
b) $\begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$

### Problema 7
Encontrar los eigenvalores de $A = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 1 \end{pmatrix}$.

### Problema 8
Si $A$ tiene eigenvalores $2, 3, 5$, encontrar:
a) $\det(A)$
b) $\text{tr}(A)$
c) Eigenvalores de $A^{-1}$
d) Eigenvalores de $A + 2I$

### Problema 9
Sea $A$ una matriz $3 \times 3$ con $\text{tr}(A) = 6$, $\det(A) = 8$, y eigenvalores $\lambda, 2, 2$. Encontrar $\lambda$.

### Problema 10
Demostrar que si $A^2 = I$, los eigenvalores de $A$ solo pueden ser $\pm 1$.

---

## 6.3 Espacios Propios y Multiplicidades

### Problema 11
Para $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$:
a) Encontrar eigenvalores y sus multiplicidades algebraicas
b) Encontrar las multiplicidades geométricas
c) ¿Es diagonalizable?

### Problema 12
Encontrar una base para cada espacio propio de:
$$A = \begin{pmatrix} 5 & -1 \\ 1 & 3 \end{pmatrix}$$

### Problema 13
Para $A = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 2 & 0 \\ 1 & 1 & 2 \end{pmatrix}$:
a) Encontrar eigenvalores
b) Calcular $m_a$ y $m_g$ para cada uno
c) ¿Es diagonalizable?

### Problema 14
Encontrar todos los valores de $k$ para los cuales la matriz es diagonalizable:
$$A = \begin{pmatrix} k & 1 \\ 0 & k \end{pmatrix}$$

---

## 6.4 Diagonalización

### Problema 15
Diagonalizar (si es posible):
a) $A = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$
b) $B = \begin{pmatrix} 1 & -1 \\ 1 & 3 \end{pmatrix}$
c) $C = \begin{pmatrix} 4 & 6 \\ -3 & -5 \end{pmatrix}$

### Problema 16
Sea $A = \begin{pmatrix} 0 & 0 & -2 \\ 1 & 2 & 1 \\ 1 & 0 & 3 \end{pmatrix}$.
a) Encontrar eigenvalores
b) Diagonalizar $A$

### Problema 17
Diagonalizar ortogonalmente la matriz simétrica:
$$A = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$$

### Problema 18
Diagonalizar ortogonalmente:
$$A = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 5 \end{pmatrix}$$

---

## 6.5 Potencias de Matrices

### Problema 19
Usando diagonalización, calcular $A^{10}$ donde:
$$A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$$

### Problema 20
Calcular $A^n$ para:
$$A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$$

### Problema 21
Si $A = \begin{pmatrix} 5 & -2 \\ 3 & 0 \end{pmatrix}$, expresar $A^{-1}$ en términos de $A$ usando Cayley-Hamilton.

---

## Aplicaciones

### Problema 22 (Sistemas Dinámicos)
La población de conejos ($C$) y zorros ($Z$) evoluciona según:
$$\begin{pmatrix} C_{n+1} \\ Z_{n+1} \end{pmatrix} = \begin{pmatrix} 1.1 & -0.4 \\ 0.1 & 0.6 \end{pmatrix} \begin{pmatrix} C_n \\ Z_n \end{pmatrix}$$

a) Encontrar eigenvalores
b) ¿Las poblaciones crecen, decrecen o se estabilizan a largo plazo?

### Problema 23 (Cadenas de Markov)
El clima en una ciudad puede ser soleado (S) o lluvioso (L). La matriz de transición es:
$$P = \begin{pmatrix} 0.8 & 0.4 \\ 0.2 & 0.6 \end{pmatrix}$$

Encontrar la distribución de clima a largo plazo.

### Problema 24 (Fibonacci)
La sucesión de Fibonacci satisface $F_n = F_{n-1} + F_{n-2}$.
a) Expresar como sistema matricial
b) Usar diagonalización para encontrar fórmula cerrada de $F_n$

### Problema 25 (Forma Cuadrática)
Clasificar la cónica $5x^2 + 4xy + 2y^2 = 1$ usando eigenvalores.

### Problema 26 (Google PageRank)
Simplificación: 3 páginas web con matriz de enlaces:
$$G = \begin{pmatrix} 0 & 1/2 & 1 \\ 1/2 & 0 & 0 \\ 1/2 & 1/2 & 0 \end{pmatrix}$$

Encontrar el ranking de páginas (eigenvector de $\lambda = 1$).

### Problema 27 (Matrices Definidas Positivas)
Determinar si las siguientes matrices son definidas positivas:
a) $\begin{pmatrix} 4 & 2 \\ 2 & 3 \end{pmatrix}$
b) $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$

### Problema 28 (Cayley-Hamilton)
Verificar el teorema de Cayley-Hamilton para $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.
