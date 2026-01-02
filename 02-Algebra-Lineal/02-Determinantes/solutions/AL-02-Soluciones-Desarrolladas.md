<!--
::METADATA::
type: solution
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Soluciones de Determinantes

---

## Problema 1
**Enunciado:** $\begin{vmatrix} 2 & 3 \\ 1 & 4 \end{vmatrix}$

**Solución:**
$$\det = 2(4) - 3(1) = 8 - 3 = 5$$

---

## Problema 4
**Enunciado:** $\begin{vmatrix} 2 & 0 & 1 \\ 3 & 1 & 2 \\ 1 & 0 & 4 \end{vmatrix}$

**Solución:**
Expandiendo por columna 2 (tiene dos ceros):

$$= 0 \cdot C_{12} + 1 \cdot C_{22} + 0 \cdot C_{32}$$

$$C_{22} = (+1)\begin{vmatrix} 2 & 1 \\ 1 & 4 \end{vmatrix} = 8 - 1 = 7$$

$$\det = 7$$

---

## Problema 9
**Enunciado:** Si $\det(A) = 2$ y $A$ es $3 \times 3$, hallar $\det(3A)$.

**Solución:**
$$\det(cA) = c^n \det(A)$$

$$\det(3A) = 3^3 \cdot 2 = 27 \cdot 2 = 54$$

---

## Problema 10
**Enunciado:** Calcular $\begin{vmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 1 & 1 \end{vmatrix}$ sin expandir.

**Solución:**
Observamos que la fila 2 es el doble de la fila 1:
$$\begin{pmatrix} 2 & 4 & 6 \end{pmatrix} = 2 \cdot \begin{pmatrix} 1 & 2 & 3 \end{pmatrix}$$

Como hay dos filas proporcionales, $\det = 0$.

---

## Problema 15
**Enunciado:** Calcular por expansión de la primera fila:
$$\begin{vmatrix} 2 & 1 & 3 \\ 0 & 4 & 1 \\ 5 & 2 & 0 \end{vmatrix}$$

**Solución:**
$$= 2 \cdot C_{11} + 1 \cdot C_{12} + 3 \cdot C_{13}$$

$$C_{11} = (+1)\begin{vmatrix} 4 & 1 \\ 2 & 0 \end{vmatrix} = 0 - 2 = -2$$

$$C_{12} = (-1)\begin{vmatrix} 0 & 1 \\ 5 & 0 \end{vmatrix} = -(0 - 5) = 5$$

$$C_{13} = (+1)\begin{vmatrix} 0 & 4 \\ 5 & 2 \end{vmatrix} = 0 - 20 = -20$$

$$\det = 2(-2) + 1(5) + 3(-20) = -4 + 5 - 60 = -59$$

---

## Problema 17
**Enunciado:** $\begin{vmatrix} 1 & 2 & 3 & 4 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 1 \end{vmatrix}$

**Solución:**
Es una [matriz](../../../glossary.md#matriz) triangular superior. El [determinante](../../../glossary.md#determinante) es el producto de la diagonal:

$$\det = 1 \cdot 1 \cdot 1 \cdot 1 = 1$$

---

## Problema 18
**Enunciado:** Hallar $\text{adj}(A)$ para $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$.

**Solución:**
Cofactores:
- $C_{11} = 3$
- $C_{12} = -5$
- $C_{21} = -1$
- $C_{22} = 2$

[Matriz](../../../glossary.md#matriz) de cofactores: $C = \begin{pmatrix} 3 & -5 \\ -1 & 2 \end{pmatrix}$

$$\text{adj}(A) = C^T = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$$

---

## Problema 22
**Enunciado:** Resolver por Cramer: $\begin{cases} 2x + y = 5 \\ x + 3y = 5 \end{cases}$

**Solución:**
$$A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}, \quad b = \begin{pmatrix} 5 \\ 5 \end{pmatrix}$$

$$\det(A) = 6 - 1 = 5$$

$$x = \frac{\begin{vmatrix} 5 & 1 \\ 5 & 3 \end{vmatrix}}{5} = \frac{15 - 5}{5} = 2$$

$$y = \frac{\begin{vmatrix} 2 & 5 \\ 1 & 5 \end{vmatrix}}{5} = \frac{10 - 5}{5} = 1$$

**Solución:** $x = 2$, $y = 1$

---

## Problema 24
**Enunciado:** Resolver por Cramer el sistema $3 \times 3$.

**Solución:**
$$A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & 1 \\ 2 & 1 & -1 \end{pmatrix}, \quad b = \begin{pmatrix} 6 \\ 2 \\ 1 \end{pmatrix}$$

$\det(A) = 1(1-1) - 1(-1-2) + 1(1+2) = 0 + 3 + 3 = 6$

$$x = \frac{\begin{vmatrix} 6 & 1 & 1 \\ 2 & -1 & 1 \\ 1 & 1 & -1 \end{vmatrix}}{6} = \frac{6}{6} = 1$$

$$y = \frac{\begin{vmatrix} 1 & 6 & 1 \\ 1 & 2 & 1 \\ 2 & 1 & -1 \end{vmatrix}}{6} = \frac{12}{6} = 2$$

$$z = \frac{\begin{vmatrix} 1 & 1 & 6 \\ 1 & -1 & 2 \\ 2 & 1 & 1 \end{vmatrix}}{6} = \frac{18}{6} = 3$$

**Solución:** $x = 1$, $y = 2$, $z = 3$

---

## Problema 25
**Enunciado:** ¿Para qué valor de $k$ no hay solución única?

**Solución:**
$$\det(A) = \begin{vmatrix} k & 1 \\ 2 & k \end{vmatrix} = k^2 - 2$$

No hay solución única cuando $\det(A) = 0$:
$$k^2 - 2 = 0 \Rightarrow k = \pm\sqrt{2}$$

---

## Problema 27
**Enunciado:** Si $\det(A) = 5$, hallar $\det(A^3)$.

**Solución:**
$$\det(A^3) = \det(A \cdot A \cdot A) = \det(A)^3 = 5^3 = 125$$
