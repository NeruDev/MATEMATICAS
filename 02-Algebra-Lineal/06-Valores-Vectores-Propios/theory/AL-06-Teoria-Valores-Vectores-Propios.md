<!--
content_type: theory
topic: Valores y Vectores Propios
---
-->

# Teoría de Valores y Vectores Propios

---

## 6.1 Definición de Valores y Vectores Propios

### Definiciones Fundamentales

Sea $A$ una matriz $n \times n$ (o $T: V \to V$ una transformación lineal).

> **Definición:** Un escalar $\lambda$ es **valor propio** (eigenvalor) de $A$ si existe un vector no nulo $v$ tal que:
> $$Av = \lambda v$$

> **Definición:** El vector $v \neq \mathbf{0}$ que satisface $Av = \lambda v$ se llama **vector propio** (eigenvector) asociado a $\lambda$.

### Interpretación Geométrica

$v$ es eigenvector de $A$ si $Av$ es paralelo a $v$:
- La transformación $A$ solo **escala** al vector $v$ por el factor $\lambda$
- Si $\lambda > 0$: mismo sentido
- Si $\lambda < 0$: sentido opuesto
- Si $\lambda = 0$: $v \in \ker(A)$

### Ejemplo Introductorio

Sea $A = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$

Verificar que $v = (1, 0)$ es eigenvector:
$$Av = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \end{pmatrix} = 3\begin{pmatrix} 1 \\ 0 \end{pmatrix}$$

Por lo tanto, $\lambda = 3$ es valor propio con eigenvector $(1, 0)$.

### Propiedades Básicas

1. Si $v$ es eigenvector asociado a $\lambda$, entonces $cv$ también (para $c \neq 0$)
2. Si $v_1, v_2$ son eigenvectores del **mismo** $\lambda$, entonces $v_1 + v_2$ también lo es (si $\neq \mathbf{0}$)
3. Eigenvectores de **diferentes** eigenvalores son linealmente independientes

### Ecuación Característica

De $Av = \lambda v$ obtenemos:
$$Av - \lambda v = \mathbf{0}$$
$$(A - \lambda I)v = \mathbf{0}$$

Para que exista $v \neq \mathbf{0}$, necesitamos que $(A - \lambda I)$ sea singular:

> **Ecuación Característica:**
> $$\det(A - \lambda I) = 0$$

---

## 6.2 Polinomio Característico

### Definición

El **polinomio característico** de $A$ es:
$$p(\lambda) = \det(A - \lambda I)$$

Es un polinomio de grado $n$ en $\lambda$.

### Para Matrices $2 \times 2$

Si $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$:

$$p(\lambda) = \det\begin{pmatrix} a - \lambda & b \\ c & d - \lambda \end{pmatrix} = (a-\lambda)(d-\lambda) - bc$$

$$p(\lambda) = \lambda^2 - (a + d)\lambda + (ad - bc)$$

$$\boxed{p(\lambda) = \lambda^2 - \text{tr}(A)\lambda + \det(A)}$$

### Para Matrices $3 \times 3$

$$p(\lambda) = -\lambda^3 + \text{tr}(A)\lambda^2 - (\text{suma de menores } 2\times 2)\lambda + \det(A)$$

### Propiedades del Polinomio Característico

> **Teorema:** Para una matriz $n \times n$ con eigenvalores $\lambda_1, ..., \lambda_n$ (contando multiplicidad):
> 1. $\lambda_1 + \lambda_2 + ... + \lambda_n = \text{tr}(A)$
> 2. $\lambda_1 \cdot \lambda_2 \cdots \lambda_n = \det(A)$

### Eigenvalores de Matrices Especiales

| Tipo de Matriz | Eigenvalores |
|----------------|--------------|
| Diagonal | Los elementos de la diagonal |
| Triangular | Los elementos de la diagonal |
| $A^k$ | $\lambda_1^k, ..., \lambda_n^k$ |
| $A^{-1}$ (si existe) | $1/\lambda_1, ..., 1/\lambda_n$ |
| $A + cI$ | $\lambda_1 + c, ..., \lambda_n + c$ |
| $cA$ | $c\lambda_1, ..., c\lambda_n$ |

---

## 6.3 Espacios Propios

### Definición

El **espacio propio** (eigenespacio) asociado al eigenvalor $\lambda$ es:

$$E_\lambda = \ker(A - \lambda I) = \{v \in \mathbb{R}^n : Av = \lambda v\}$$

> **Teorema:** $E_\lambda$ es un subespacio vectorial de $\mathbb{R}^n$.

### Multiplicidad Algebraica y Geométrica

**Multiplicidad algebraica** $m_a(\lambda)$: 
- Número de veces que $\lambda$ aparece como raíz de $p(\lambda)$
- Es el exponente de $(\lambda - \lambda_i)$ en la factorización de $p(\lambda)$

**Multiplicidad geométrica** $m_g(\lambda)$:
- Dimensión del espacio propio: $m_g(\lambda) = \dim(E_\lambda)$
- Número máximo de eigenvectores LI asociados a $\lambda$

> **Teorema Fundamental:**
> $$1 \leq m_g(\lambda) \leq m_a(\lambda)$$

### Ejemplo

$$A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$$

$p(\lambda) = (2 - \lambda)^2$, entonces $\lambda = 2$ con $m_a(2) = 2$.

$A - 2I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$

$\ker(A - 2I) = \text{span}\{(1, 0)\}$, entonces $m_g(2) = 1$.

Aquí $m_g(2) < m_a(2)$.

### Eigenvectores de Diferentes Eigenvalores

> **Teorema:** Si $v_1, ..., v_k$ son eigenvectores correspondientes a eigenvalores **distintos** $\lambda_1, ..., \lambda_k$, entonces $\{v_1, ..., v_k\}$ es linealmente independiente.

---

## 6.4 Diagonalización

### Definición

Una matriz $A$ es **diagonalizable** si existe una matriz invertible $P$ tal que:
$$P^{-1}AP = D$$
donde $D$ es diagonal.

Equivalentemente: $A = PDP^{-1}$

### Construcción de P y D

Si $A$ es diagonalizable:
- Las **columnas de $P$** son eigenvectores de $A$
- Los **elementos de la diagonal de $D$** son los eigenvalores correspondientes

$$P = \begin{pmatrix} | & | & & | \\ v_1 & v_2 & \cdots & v_n \\ | & | & & | \end{pmatrix}, \quad D = \begin{pmatrix} \lambda_1 & 0 & \cdots & 0 \\ 0 & \lambda_2 & \cdots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_n \end{pmatrix}$$

### Criterios de Diagonalizabilidad

> **Teorema:** $A$ ($n \times n$) es diagonalizable si y solo si tiene $n$ eigenvectores linealmente independientes.

> **Corolario 1:** Si $A$ tiene $n$ eigenvalores distintos, entonces $A$ es diagonalizable.

> **Corolario 2:** $A$ es diagonalizable si y solo si $m_g(\lambda) = m_a(\lambda)$ para todo eigenvalor $\lambda$.

### Matrices NO Diagonalizables

Una matriz **no es diagonalizable** si:
- $m_g(\lambda) < m_a(\lambda)$ para algún eigenvalor

**Ejemplo clásico:** $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ tiene $\lambda = 0$ (doble), pero $\dim(E_0) = 1$.

### Matrices Reales con Eigenvalores Complejos

Una matriz real puede tener eigenvalores complejos (conjugados).

Ejemplo: $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ (rotación 90°)

$p(\lambda) = \lambda^2 + 1$, entonces $\lambda = \pm i$.

**No es diagonalizable sobre $\mathbb{R}$**, pero sí sobre $\mathbb{C}$.

---

## 6.5 Aplicaciones

### Potencias de Matrices

Si $A = PDP^{-1}$, entonces:
$$A^k = PD^kP^{-1}$$

donde $D^k = \begin{pmatrix} \lambda_1^k & 0 & \cdots \\ 0 & \lambda_2^k & \cdots \\ \vdots & & \ddots \end{pmatrix}$

**Utilidad:** Calcular $A^{100}$ se reduce a calcular $\lambda^{100}$.

### Sistemas de Ecuaciones Diferenciales

El sistema $\mathbf{x}'(t) = A\mathbf{x}(t)$ tiene solución:
$$\mathbf{x}(t) = e^{At}\mathbf{x}(0)$$

Si $A = PDP^{-1}$:
$$e^{At} = Pe^{Dt}P^{-1}$$

donde $e^{Dt} = \begin{pmatrix} e^{\lambda_1 t} & 0 & \cdots \\ 0 & e^{\lambda_2 t} & \cdots \\ \vdots & & \ddots \end{pmatrix}$

### Cadenas de Markov

Una **matriz de Markov** $P$ satisface:
- Todas las entradas son $\geq 0$
- Las columnas suman 1

> **Teorema:** Toda matriz de Markov tiene $\lambda = 1$ como eigenvalor.

El **estado estacionario** es el eigenvector correspondiente a $\lambda = 1$ (normalizado).

### Análisis de Componentes Principales (PCA)

Para datos con matriz de covarianza $\Sigma$:
- Los eigenvalores dan la varianza en cada dirección principal
- Los eigenvectores dan las direcciones principales

### Teorema de Cayley-Hamilton

> **Teorema:** Toda matriz $A$ satisface su propio polinomio característico:
> $$p(A) = A^n - c_{n-1}A^{n-1} - ... - c_1A - c_0I = O$$

**Utilidad:** Permite expresar $A^{-1}$ y potencias altas de $A$ en términos de potencias menores.

---

## Teoremas Importantes

### Teorema Espectral (Matrices Simétricas)

> **Teorema:** Si $A$ es matriz real simétrica ($A^T = A$):
> 1. Todos los eigenvalores son reales
> 2. Eigenvectores de diferentes eigenvalores son ortogonales
> 3. $A$ es **ortogonalmente diagonalizable**: existe $Q$ ortogonal ($Q^TQ = I$) tal que $Q^TAQ = D$

### Matrices Definidas Positivas

Una matriz simétrica $A$ es **definida positiva** si todos sus eigenvalores son positivos.

Equivalentemente: $x^TAx > 0$ para todo $x \neq \mathbf{0}$.
