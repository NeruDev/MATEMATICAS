<!--
::METADATA::
type: solution
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Soluciones: Valores y Vectores Propios

---

## Problema 1
**Enunciado:** Verificar que $v = (1, 2)^T$ es eigenvector de $A = \begin{pmatrix} 3 & 1 \\ 2 & 2 \end{pmatrix}$.

**Solución:**

$$Av = \begin{pmatrix} 3 & 1 \\ 2 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 5 \\ 6 \end{pmatrix}$$

¿Es múltiplo de $v = (1, 2)^T$?

$(5, 6) = \lambda(1, 2)$ implica $\lambda = 5$ de la primera componente.
Verificación: $\lambda \cdot 2 = 10 \neq 6$.

**$v = (1, 2)$ NO es eigenvector de $A$** ✗

Probemos recalculando: $5/1 = 5$, pero $6/2 = 3$. No coinciden.

---

## Problema 2a
**Enunciado:** Eigenvalores de $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$

**Solución:**

$\text{tr}(A) = 7$, $\det(A) = 10 - 4 = 6$

$\lambda^2 - 7\lambda + 6 = 0$
$(\lambda - 6)(\lambda - 1) = 0$

**Eigenvalores:** $\lambda_1 = 6$, $\lambda_2 = 1$

---

## Problema 2c
**Enunciado:** Eigenvalores de $C = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$

**Solución:**

$\text{tr}(C) = 0$, $\det(C) = 0 - (-1) = 1$

$\lambda^2 + 1 = 0$
$\lambda = \pm i$

**Eigenvalores:** $\lambda_1 = i$, $\lambda_2 = -i$ (complejos)

---

## Problema 4
**Enunciado:** Eigenvalores y eigenvectores de $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$

**Solución:**

**Eigenvalores:** ([matriz](../../..](../../../glossary.md)#matriz) triangular)
$\lambda_1 = 1$, $\lambda_2 = 3$

**Eigenvectores:**

Para $\lambda = 1$:
$A - I = \begin{pmatrix} 0 & 2 \\ 0 & 2 \end{pmatrix}$
Sistema: $2y = 0 \Rightarrow y = 0$
$v_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$

Para $\lambda = 3$:
$A - 3I = \begin{pmatrix} -2 & 2 \\ 0 & 0 \end{pmatrix}$
Sistema: $-2x + 2y = 0 \Rightarrow x = y$
$v_2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$

---

## Problema 8
**Enunciado:** $A$ tiene eigenvalores $2, 3, 5$.

**Solución:**

**a)** $\det(A) = 2 \cdot 3 \cdot 5 = 30$

**b)** $\text{tr}(A) = 2 + 3 + 5 = 10$

**c)** Eigenvalores de $A^{-1}$: $\frac{1}{2}, \frac{1}{3}, \frac{1}{5}$

**d)** Eigenvalores de $A + 2I$: $4, 5, 7$

---

## Problema 11
**Enunciado:** $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$

**Solución:**

**a) Eigenvalores:**
$p(\lambda) = (2-\lambda)^2 = 0$
$\lambda = 2$ con $m_a(2) = 2$

**b) [Multiplicidad geométrica](../../..](../../../glossary.md)#multiplicidad-geometrica):**
$A - 2I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$
$\ker(A - 2I) = \text{span}\{(1, 0)^T\}$
$m_g(2) = 1$

**c)** Como $m_g(2) = 1 < 2 = m_a(2)$, **no es diagonalizable**.

---

## Problema 15a
**Enunciado:** Diagonalizar $A = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$

**Solución:**

**Eigenvalores:** $\lambda_1 = 3$, $\lambda_2 = 2$ (diagonal de [matriz](../../..](../../../glossary.md)#matriz) triangular)

**Eigenvectores:**

$\lambda = 3$: $A - 3I = \begin{pmatrix} 0 & 1 \\ 0 & -1 \end{pmatrix}$, $v_1 = (1, 0)^T$

$\lambda = 2$: $A - 2I = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$, $v_2 = (-1, 1)^T$

$$P = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}, \quad D = \begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix}$$

$A = PDP^{-1}$

---

## Problema 17
**Enunciado:** Diagonalizar ortogonalmente $A = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$

**Solución:**

$p(\lambda) = \lambda^2 - 6\lambda + 8 = (\lambda - 4)(\lambda - 2)$

**Eigenvalores:** $\lambda_1 = 4$, $\lambda_2 = 2$

**Eigenvectores:**

$\lambda = 4$: $A - 4I = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}$, $v_1 = (1, 1)^T$

$\lambda = 2$: $A - 2I = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, $v_2 = (1, -1)^T$

**Ortonormalización:**
$q_1 = \frac{1}{\sqrt{2}}(1, 1)^T$
$q_2 = \frac{1}{\sqrt{2}}(1, -1)^T$

$$Q = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \quad D = \begin{pmatrix} 4 & 0 \\ 0 & 2 \end{pmatrix}$$

Verificar: $Q^T = Q^{-1}$ ✓

---

## Problema 19
**Enunciado:** Calcular $A^{10}$ donde $A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$

**Solución:**

Eigenvalores: $\lambda_1 = 1$, $\lambda_2 = 2$

Eigenvectores: $v_1 = (1, 0)^T$, $v_2 = (1, 1)^T$

$P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, $P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$

$D^{10} = \begin{pmatrix} 1 & 0 \\ 0 & 1024 \end{pmatrix}$

$$A^{10} = PD^{10}P^{-1} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & 1024 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$$

$$= \begin{pmatrix} 1 & 1024 \\ 0 & 1024 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1023 \\ 0 & 1024 \end{pmatrix}$$

---

## Problema 23
**Enunciado:** Distribución de clima a largo plazo.

**Solución:**

$P = \begin{pmatrix} 0.8 & 0.4 \\ 0.2 & 0.6 \end{pmatrix}$

Resolver $(P - I)x = 0$:
$\begin{pmatrix} -0.2 & 0.4 \\ 0.2 & -0.4 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$

$-0.2x_1 + 0.4x_2 = 0 \Rightarrow x_1 = 2x_2$

Eigenvector: $(2, 1)^T$

Normalizar (suma = 1): $x = \frac{1}{3}(2, 1)^T = (2/3, 1/3)$

**Estado estacionario:** 
- Soleado: $66.7\%$
- Lluvioso: $33.3\%$

---

## Problema 27
**Enunciado:** ¿Son definidas positivas?

**Solución:**

**a)** $A = \begin{pmatrix} 4 & 2 \\ 2 & 3 \end{pmatrix}$

$p(\lambda) = \lambda^2 - 7\lambda + 8$
$\lambda = \frac{7 \pm \sqrt{17}}{2}$

$\lambda_1 \approx 5.56 > 0$, $\lambda_2 \approx 1.44 > 0$

**Sí es definida positiva** ✓

**b)** $B = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$

$p(\lambda) = \lambda^2 - 2\lambda - 3 = (\lambda - 3)(\lambda + 1)$

$\lambda_1 = 3 > 0$, $\lambda_2 = -1 < 0$

**No es definida positiva** ✗

---

## Problema 28
**Enunciado:** Verificar Cayley-Hamilton para $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$

**Solución:**

$p(\lambda) = \lambda^2 - 5\lambda - 2$

Verificar que $A^2 - 5A - 2I = O$:

$A^2 = \begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix}$

$5A = \begin{pmatrix} 5 & 10 \\ 15 & 20 \end{pmatrix}$

$2I = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$

$A^2 - 5A - 2I = \begin{pmatrix} 7-5-2 & 10-10-0 \\ 15-15-0 & 22-20-2 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$ ✓
