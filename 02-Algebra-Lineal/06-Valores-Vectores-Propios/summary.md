# Resumen: Valores y Vectores Propios

## Definiciones

**Valor propio (eigenvalor):** $\lambda$ es valor propio de $A$ si:
$$Av = \lambda v$$
para algún $v \neq \mathbf{0}$.

**Vector propio (eigenvector):** $v \neq \mathbf{0}$ tal que $Av = \lambda v$.

## Ecuación Característica

$$\det(A - \lambda I) = 0$$

## Polinomio Característico

$$p(\lambda) = \det(A - \lambda I)$$

Para $n = 2$:
$$p(\lambda) = \lambda^2 - \text{tr}(A)\lambda + \det(A)$$

## Propiedades

| Propiedad | Fórmula |
|-----------|--------|
| Suma de valores propios | $\lambda_1 + ... + \lambda_n = \text{tr}(A)$ |
| Producto de valores propios | $\lambda_1 \cdots \lambda_n = \det(A)$ |
| VP de $A^k$ | $\lambda^k$ |
| VP de $A^{-1}$ | $1/\lambda$ |
| VP de $A - cI$ | $\lambda - c$ |

## Espacios Propios

$$E_\lambda = \ker(A - \lambda I) = \{v : Av = \lambda v\}$$

**Multiplicidad algebraica:** $m_a(\lambda)$ = exponente de $(\lambda - \lambda_i)$ en $p(\lambda)$

**Multiplicidad geométrica:** $m_g(\lambda) = \dim(E_\lambda)$

$$1 \leq m_g(\lambda) \leq m_a(\lambda)$$

## Diagonalización

$A$ es **diagonalizable** si existe $P$ invertible tal que:
$$P^{-1}AP = D = \begin{pmatrix} \lambda_1 & & \\ & \ddots & \\ & & \lambda_n \end{pmatrix}$$

**Criterio:** $A$ es diagonalizable $\Leftrightarrow$ tiene $n$ eigenvectores LI.

Equivalentemente: $m_g(\lambda) = m_a(\lambda)$ para todo $\lambda$.

## Potencias de Matrices

Si $A = PDP^{-1}$:
$$A^k = PD^kP^{-1}$$

donde $D^k = \begin{pmatrix} \lambda_1^k & & \\ & \ddots & \\ & & \lambda_n^k \end{pmatrix}$

## Teorema de Cayley-Hamilton

Toda matriz satisface su polinomio característico:
$$p(A) = 0$$
