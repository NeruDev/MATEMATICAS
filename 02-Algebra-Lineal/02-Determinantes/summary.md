# Resumen: Determinantes

---

## Fórmulas Directas

### Determinante $2 \times 2$
$$\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$

### Determinante $3 \times 3$ (Regla de Sarrus)
$$\det\begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix} = aei + bfg + cdh - ceg - bdi - afh$$

---

## Propiedades

1. $\det(I) = 1$
2. $\det(A^T) = \det(A)$
3. $\det(AB) = \det(A)\det(B)$
4. $\det(A^{-1}) = \frac{1}{\det(A)}$
5. $\det(cA) = c^n \det(A)$ para $A$ de $n \times n$

### Operaciones de Fila
- Intercambiar filas: cambia signo
- Multiplicar fila por $k$: multiplica det por $k$
- Sumar múltiplo de fila a otra: no cambia det

---

## Cofactores y Adjunta

**Menor:** $M_{ij}$ = det de submatriz eliminando fila $i$, columna $j$

**Cofactor:** $C_{ij} = (-1)^{i+j} M_{ij}$

**Adjunta:** $\text{adj}(A) = (C_{ij})^T$

**Inversa:** $A^{-1} = \frac{1}{\det(A)}\text{adj}(A)$

---

## Regla de Cramer

Para $Ax = b$ con $\det(A) \neq 0$:
$$x_i = \frac{\det(A_i)}{\det(A)}$$

donde $A_i$ = $A$ con columna $i$ reemplazada por $b$.
