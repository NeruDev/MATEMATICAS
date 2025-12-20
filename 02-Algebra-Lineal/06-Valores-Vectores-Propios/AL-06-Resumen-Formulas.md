<!--
::METADATA::
type: cheat-sheet
topic_id: al-06-valores-vectores-propios
file_id: AL-06-Resumen-Formulas
status: stable
audience: student
-->
# Resumen de Fórmulas: Valores y Vectores Propios

## Definiciones fundamentales

### Valor propio (eigenvalor)
$\lambda$ es **valor propio** de $A$ si existe $\vec{v} \neq \vec{0}$ tal que:
$$A\vec{v} = \lambda\vec{v}$$

### Vector propio (eigenvector)
$\vec{v} \neq \vec{0}$ es **vector propio** asociado a $\lambda$ si:
$$A\vec{v} = \lambda\vec{v}$$

### Ecuación característica
$$\det(A - \lambda I) = 0$$

## Polinomio característico

$$p(\lambda) = \det(A - \lambda I)$$

Para matriz $n \times n$: polinomio de grado $n$.

### Caso 2×2
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

$$p(\lambda) = \lambda^2 - (a+d)\lambda + (ad-bc)$$
$$p(\lambda) = \lambda^2 - \text{tr}(A)\lambda + \det(A)$$

### Fórmulas útiles
- **Traza**: $\text{tr}(A) = \sum \lambda_i$ (suma de valores propios)
- **Determinante**: $\det(A) = \prod \lambda_i$ (producto de valores propios)

## Espacio propio (eigenespacio)

$$E_\lambda = \ker(A - \lambda I) = \{\vec{v} : A\vec{v} = \lambda\vec{v}\}$$

### Para calcular $E_\lambda$:
Resolver el sistema homogéneo:
$$(A - \lambda I)\vec{v} = \vec{0}$$

## Multiplicidades

### Multiplicidad algebraica $m_a(\lambda)$
Multiplicidad de $\lambda$ como raíz de $p(\lambda)$.

### Multiplicidad geométrica $m_g(\lambda)$
$$m_g(\lambda) = \dim(E_\lambda)$$

### Relación fundamental
$$1 \leq m_g(\lambda) \leq m_a(\lambda)$$

## Diagonalización

### Matriz diagonalizable
$A$ es **diagonalizable** si existe $P$ invertible tal que:
$$A = PDP^{-1}$$

donde $D$ es diagonal.

### Construcción
- $D$: valores propios en la diagonal
- $P$: columnas son los vectores propios correspondientes

$$P = \begin{pmatrix} | & | & & | \\ \vec{v}_1 & \vec{v}_2 & \cdots & \vec{v}_n \\ | & | & & | \end{pmatrix}, \quad D = \begin{pmatrix} \lambda_1 & 0 & \cdots & 0 \\ 0 & \lambda_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_n \end{pmatrix}$$

### Criterios de diagonalización

$A$ ($n \times n$) es diagonalizable si y solo si:
1. $A$ tiene $n$ vectores propios linealmente independientes
2. $m_g(\lambda) = m_a(\lambda)$ para todo $\lambda$
3. La suma de dimensiones de espacios propios es $n$

### Casos garantizados
- $n$ valores propios distintos $\Rightarrow$ diagonalizable
- Matriz simétrica real $\Rightarrow$ diagonalizable (con valores propios reales)

## Potencias de matrices

Si $A = PDP^{-1}$:
$$A^k = PD^kP^{-1}$$

donde:
$$D^k = \begin{pmatrix} \lambda_1^k & 0 & \cdots & 0 \\ 0 & \lambda_2^k & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_n^k \end{pmatrix}$$

## Propiedades de valores propios

| Operación | Valores propios |
|-----------|-----------------|
| $A$ | $\lambda$ |
| $A^k$ | $\lambda^k$ |
| $A^{-1}$ | $\frac{1}{\lambda}$ |
| $A + cI$ | $\lambda + c$ |
| $cA$ | $c\lambda$ |
| $A^T$ | $\lambda$ (mismos) |

## Matrices similares

Si $B = P^{-1}AP$:
- Mismo polinomio característico
- Mismos valores propios
- Misma traza y determinante
- Si $\vec{v}$ es eigenvector de $A$, entonces $P^{-1}\vec{v}$ es eigenvector de $B$

## Teorema de Cayley-Hamilton

Toda matriz satisface su propia ecuación característica:
$$p(A) = 0$$

Si $p(\lambda) = \lambda^2 - 5\lambda + 6$, entonces $A^2 - 5A + 6I = O$.

## Aplicaciones

### Sistemas dinámicos discretos
$$\vec{x}_{k+1} = A\vec{x}_k \Rightarrow \vec{x}_k = A^k\vec{x}_0$$

### Cadenas de Markov
Estado estacionario: eigenvector de $\lambda = 1$.

### Sistemas de EDO lineales
$$\vec{x}'(t) = A\vec{x}(t)$$
Solución: $\vec{x}(t) = c_1 e^{\lambda_1 t}\vec{v}_1 + c_2 e^{\lambda_2 t}\vec{v}_2 + \cdots$
