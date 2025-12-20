<!--
content_type: solutions
format: step_by_step
---
-->

# Soluciones de Matrices

---

## Problema 4
**Enunciado:** Calcular $A + B$ donde $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, $B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$.

**Solución:**
$$A + B = \begin{pmatrix} 1+5 & 2+6 \\ 3+7 & 4+8 \end{pmatrix} = \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix}$$

---

## Problema 9
**Enunciado:** Calcular $AB$ donde $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, $B = \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix}$.

**Solución:**
- $(AB)_{11} = 1(2) + 2(1) = 4$
- $(AB)_{12} = 1(0) + 2(3) = 6$
- $(AB)_{21} = 3(2) + 4(1) = 10$
- $(AB)_{22} = 3(0) + 4(3) = 12$

$$AB = \begin{pmatrix} 4 & 6 \\ 10 & 12 \end{pmatrix}$$

---

## Problema 10
**Enunciado:** Calcular $BA$ y comparar con $AB$.

**Solución:**
$$BA = \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$$

- $(BA)_{11} = 2(1) + 0(3) = 2$
- $(BA)_{12} = 2(2) + 0(4) = 4$
- $(BA)_{21} = 1(1) + 3(3) = 10$
- $(BA)_{22} = 1(2) + 3(4) = 14$

$$BA = \begin{pmatrix} 2 & 4 \\ 10 & 14 \end{pmatrix}$$

**Conclusión:** $AB \neq BA$. La multiplicación de matrices no es conmutativa.

---

## Problema 13
**Enunciado:** Si $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$, calcular $A^2$ y $A^3$.

**Solución:**
$$A^2 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$$

$$A^3 = A^2 \cdot A = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 6 \\ 0 & 1 \end{pmatrix}$$

**Patrón:** $A^n = \begin{pmatrix} 1 & 2n \\ 0 & 1 \end{pmatrix}$

---

## Problema 23
**Enunciado:** Expresar $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ como suma de simétrica y antisimétrica.

**Solución:**
Parte simétrica: $S = \frac{1}{2}(A + A^T)$

$$A^T = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$$

$$S = \frac{1}{2}\begin{pmatrix} 2 & 5 \\ 5 & 8 \end{pmatrix} = \begin{pmatrix} 1 & 5/2 \\ 5/2 & 4 \end{pmatrix}$$

Parte antisimétrica: $K = \frac{1}{2}(A - A^T)$

$$K = \frac{1}{2}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -1/2 \\ 1/2 & 0 \end{pmatrix}$$

**Verificación:** $S + K = A$ ✓

---

## Problema 24
**Enunciado:** Hallar la inversa de $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$.

**Solución:**
$\det(A) = 2(3) - 1(5) = 6 - 5 = 1$

$$A^{-1} = \frac{1}{1}\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$$

**Verificación:**
$$AA^{-1} = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$$ ✓

---

## Problema 27
**Enunciado:** Determinar si existe la inversa de $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$.

**Solución:**
$\det(A) = 1(4) - 2(2) = 4 - 4 = 0$

Como $\det(A) = 0$, la matriz **no es invertible** (es singular).

Nota: La segunda fila es el doble de la primera, lo que significa que las filas son linealmente dependientes.

---

## Problema 28
**Enunciado:** Usar Gauss-Jordan para encontrar la inversa de $A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{pmatrix}$.

**Solución:**

$$\left(\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 0 & 0 & 1 \end{array}\right)$$

$R_3 \leftarrow R_3 - R_1$:
$$\left(\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 1 & -1 & -1 & 0 & 1 \end{array}\right)$$

$R_3 \leftarrow R_3 - R_2$:
$$\left(\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & -2 & -1 & -1 & 1 \end{array}\right)$$

$R_3 \leftarrow -\frac{1}{2}R_3$:
$$\left(\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & 1/2 & 1/2 & -1/2 \end{array}\right)$$

$R_1 \leftarrow R_1 - R_3$, $R_2 \leftarrow R_2 - R_3$:
$$\left(\begin{array}{ccc|ccc} 1 & 0 & 0 & 1/2 & -1/2 & 1/2 \\ 0 & 1 & 0 & -1/2 & 1/2 & 1/2 \\ 0 & 0 & 1 & 1/2 & 1/2 & -1/2 \end{array}\right)$$

$$A^{-1} = \frac{1}{2}\begin{pmatrix} 1 & -1 & 1 \\ -1 & 1 & 1 \\ 1 & 1 & -1 \end{pmatrix}$$

---

## Problema 32
**Enunciado:** Encontrar la inversa de $\begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix}$.

**Solución:**
$\det = 1(1) - a(0) = 1 \neq 0$

$$\begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix}^{-1} = \frac{1}{1}\begin{pmatrix} 1 & -a \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -a \\ 0 & 1 \end{pmatrix}$$

**Verificación:**
$$\begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & -a \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$ ✓
