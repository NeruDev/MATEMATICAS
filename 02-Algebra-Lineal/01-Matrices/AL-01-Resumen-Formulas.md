<!--
::METADATA::
type: cheat-sheet
topic_id: al-01-matrices
file_id: AL-01-Resumen-Formulas
status: stable
audience: student
-->

> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Resumen de Fórmulas: Matrices

## Notación

- [Matriz](../../glossary.md#matriz) $A$ de tamaño $m \times n$: $A = [a_{ij}]$ donde $i = 1, \ldots, m$ y $j = 1, \ldots, n$
- Elemento en fila $i$, columna $j$: $a_{ij}$ o $(A)_{ij}$

## Tipos especiales de matrices

| Tipo | Condición |
|------|-----------|
| **Cuadrada** | $m = n$ |
| **Diagonal** | $a_{ij} = 0$ si $i \neq j$ |
| **Identidad** $I_n$ | Diagonal con $a_{ii} = 1$ |
| **Triangular superior** | $a_{ij} = 0$ si $i > j$ |
| **Triangular inferior** | $a_{ij} = 0$ si $i < j$ |
| **Simétrica** | $A = A^T$ |
| **Antisimétrica** | $A = -A^T$ |
| **Nula** $O$ | Todos $a_{ij} = 0$ |

## Operaciones básicas

### Suma y resta
$$A \pm B = [a_{ij} \pm b_{ij}]$$

*Requisito*: $A$ y $B$ del mismo tamaño.

### Producto por escalar
$$kA = [k \cdot a_{ij}]$$

### Producto de matrices
Si $A$ es $m \times n$ y $B$ es $n \times p$, entonces $C = AB$ es $m \times p$:

$$c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$$

**⚠️ En general**: $AB \neq BA$

## Transpuesta

$$A^T = [a_{ji}]$$

### Propiedades de la transpuesta
- $(A^T)^T = A$
- $(A + B)^T = A^T + B^T$
- $(kA)^T = kA^T$
- $(AB)^T = B^T A^T$

## Matriz inversa

Si $A$ es cuadrada e invertible:
$$A \cdot A^{-1} = A^{-1} \cdot A = I$$

### Inversa de matriz 2×2

$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \Rightarrow A^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

*Condición*: $\det(A) = ad - bc \neq 0$

### Propiedades de la inversa
- $(A^{-1})^{-1} = A$
- $(AB)^{-1} = B^{-1}A^{-1}$
- $(A^T)^{-1} = (A^{-1})^T$
- $(kA)^{-1} = \frac{1}{k}A^{-1}$

## Propiedades del producto

- **Asociatividad**: $(AB)C = A(BC)$
- **Distributividad**: $A(B + C) = AB + AC$
- **Elemento neutro**: $AI = IA = A$
- **Escalar**: $k(AB) = (kA)B = A(kB)$

## Verificación rápida

| Para verificar | Comprobar |
|----------------|-----------|
| Suma válida | Mismas dimensiones |
| Producto $AB$ válido | Columnas de $A$ = Filas de $B$ |
| Inversa válida | $AA^{-1} = I$ |
| Simetría | $A = A^T$ |
