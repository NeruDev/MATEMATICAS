<!--
content_type: methods
topic: Valores y Vectores Propios
---
-->

# Métodos: Valores y Vectores Propios

---

## Método 1: Encontrar Eigenvalores (Matriz 2×2)

**Objetivo:** Hallar los eigenvalores de $A$ ($2 \times 2$).

### Pasos

1. Calcular $\text{tr}(A) = a + d$
2. Calcular $\det(A) = ad - bc$
3. Resolver $\lambda^2 - \text{tr}(A)\lambda + \det(A) = 0$

### Fórmula Directa

$$\lambda = \frac{\text{tr}(A) \pm \sqrt{\text{tr}(A)^2 - 4\det(A)}}{2}$$

### Ejemplo

$A = \begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix}$

- $\text{tr}(A) = 4 + 3 = 7$
- $\det(A) = 12 - 2 = 10$

$\lambda^2 - 7\lambda + 10 = 0$
$(\lambda - 5)(\lambda - 2) = 0$

**Eigenvalores:** $\lambda_1 = 5$, $\lambda_2 = 2$

---

## Método 2: Encontrar Eigenvalores (Matriz 3×3)

**Objetivo:** Hallar los eigenvalores de $A$ ($3 \times 3$).

### Pasos

1. Formar $A - \lambda I$
2. Calcular $\det(A - \lambda I) = 0$ (polinomio cúbico)
3. Buscar raíces racionales probando divisores del término independiente
4. Una vez encontrada una raíz, factorizar y resolver el cuadrático restante

### Ejemplo

$A = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$ (triangular)

Para matrices triangulares: **eigenvalores = elementos de la diagonal**

**Eigenvalores:** $\lambda_1 = 2$ (doble), $\lambda_2 = 3$

---

## Método 3: Encontrar Eigenvectores

**Objetivo:** Dado $\lambda$, encontrar los eigenvectores asociados.

### Pasos

1. Formar la matriz $A - \lambda I$
2. Resolver el sistema $(A - \lambda I)v = \mathbf{0}$
3. Encontrar base del espacio nulo
4. Los vectores de la base son eigenvectores

### Ejemplo

$A = \begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix}$, $\lambda_1 = 5$

$A - 5I = \begin{pmatrix} -1 & 2 \\ 1 & -2 \end{pmatrix}$

Sistema: $-x + 2y = 0 \Rightarrow x = 2y$

Sea $y = 1$: $v_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$

Para $\lambda_2 = 2$:
$A - 2I = \begin{pmatrix} 2 & 2 \\ 1 & 1 \end{pmatrix}$

Sistema: $x + y = 0 \Rightarrow x = -y$

Sea $y = 1$: $v_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$

---

## Método 4: Verificar Diagonalizabilidad

**Objetivo:** Determinar si $A$ es diagonalizable.

### Pasos

1. Encontrar todos los eigenvalores y sus multiplicidades algebraicas
2. Para cada eigenvalor, calcular $m_g(\lambda) = \dim(\ker(A - \lambda I))$
3. Si $m_g(\lambda) = m_a(\lambda)$ para todos, **es diagonalizable**
4. Si algún $m_g(\lambda) < m_a(\lambda)$, **no es diagonalizable**

### Atajo

Si $A$ tiene $n$ eigenvalores **distintos**, es diagonalizable automáticamente.

### Ejemplo

$A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$

$\lambda = 2$ con $m_a(2) = 2$

$A - 2I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $\text{nulidad} = 1$

$m_g(2) = 1 < 2 = m_a(2)$

**No es diagonalizable**

---

## Método 5: Diagonalizar una Matriz

**Objetivo:** Encontrar $P$ y $D$ tales que $A = PDP^{-1}$.

### Pasos

1. Encontrar todos los eigenvalores $\lambda_1, ..., \lambda_n$
2. Para cada $\lambda_i$, encontrar una base de $E_{\lambda_i}$
3. Formar $P$ con todos los eigenvectores como columnas
4. Formar $D$ con los eigenvalores correspondientes en la diagonal
5. Verificar: $AP = PD$

### Ejemplo Completo

$A = \begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix}$

Eigenvalores: $\lambda_1 = 5$, $\lambda_2 = 2$
Eigenvectores: $v_1 = (2, 1)^T$, $v_2 = (-1, 1)^T$

$$P = \begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix}, \quad D = \begin{pmatrix} 5 & 0 \\ 0 & 2 \end{pmatrix}$$

Verificación: $A = PDP^{-1}$

---

## Método 6: Calcular Potencias de Matrices

**Objetivo:** Calcular $A^k$ usando diagonalización.

### Pasos

1. Diagonalizar: $A = PDP^{-1}$
2. Calcular $D^k$ (elevar cada elemento diagonal a la $k$)
3. Calcular $A^k = PD^kP^{-1}$

### Ejemplo

$A = \begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix}$, calcular $A^3$

Ya tenemos: $P = \begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix}$, $D = \begin{pmatrix} 5 & 0 \\ 0 & 2 \end{pmatrix}$

$P^{-1} = \frac{1}{3}\begin{pmatrix} 1 & 1 \\ -1 & 2 \end{pmatrix}$

$D^3 = \begin{pmatrix} 125 & 0 \\ 0 & 8 \end{pmatrix}$

$$A^3 = PD^3P^{-1} = \begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 125 & 0 \\ 0 & 8 \end{pmatrix}\frac{1}{3}\begin{pmatrix} 1 & 1 \\ -1 & 2 \end{pmatrix}$$

$$= \frac{1}{3}\begin{pmatrix} 250 & -8 \\ 125 & 8 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ -1 & 2 \end{pmatrix} = \frac{1}{3}\begin{pmatrix} 258 & 234 \\ 117 & 141 \end{pmatrix} = \begin{pmatrix} 86 & 78 \\ 39 & 47 \end{pmatrix}$$

---

## Método 7: Diagonalización Ortogonal (Matrices Simétricas)

**Objetivo:** Para $A = A^T$, encontrar $Q$ ortogonal tal que $Q^TAQ = D$.

### Pasos

1. Verificar que $A$ es simétrica
2. Encontrar eigenvalores (serán reales)
3. Encontrar eigenvectores
4. **Ortonormalizar** eigenvectores del mismo eigenespacio (Gram-Schmidt)
5. Formar $Q$ con eigenvectores ortonormales como columnas
6. $D$ tendrá eigenvalores en la diagonal

### Ejemplo

$A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$

$p(\lambda) = \lambda^2 - 4\lambda + 3 = (\lambda - 3)(\lambda - 1)$

$\lambda_1 = 3$: $v_1 = (1, 1)^T$, normalizado: $\frac{1}{\sqrt{2}}(1, 1)^T$

$\lambda_2 = 1$: $v_2 = (1, -1)^T$, normalizado: $\frac{1}{\sqrt{2}}(1, -1)^T$

$$Q = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \quad D = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$$

Verificar: $Q^T = Q^{-1}$ ✓

---

## Método 8: Encontrar Estado Estacionario (Cadenas de Markov)

**Objetivo:** Para una matriz de Markov $P$, encontrar el estado estacionario.

### Pasos

1. Resolver $(P - I)x = \mathbf{0}$
2. Encontrar eigenvector $v$ asociado a $\lambda = 1$
3. Normalizar: $x = \frac{v}{\|v\|_1}$ donde $\|v\|_1 = |v_1| + |v_2| + ...$

### Ejemplo

$P = \begin{pmatrix} 0.7 & 0.2 \\ 0.3 & 0.8 \end{pmatrix}$

$P - I = \begin{pmatrix} -0.3 & 0.2 \\ 0.3 & -0.2 \end{pmatrix}$

Sistema: $-0.3x + 0.2y = 0 \Rightarrow y = 1.5x$

Eigenvector: $v = (1, 1.5)^T = (2, 3)^T$

Normalizado: $x = \frac{1}{5}(2, 3)^T = (0.4, 0.6)^T$

**Estado estacionario:** $(0.4, 0.6)$
