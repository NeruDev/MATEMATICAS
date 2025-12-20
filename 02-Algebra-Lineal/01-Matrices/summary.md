<!--
content_type: summary
format: formula_sheet
---
-->

# Resumen: Matrices y Operaciones

---

## Notación

Una matriz $A$ de $m \times n$:
$$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix} = (a_{ij})_{m \times n}$$

---

## Tipos de Matrices

| Tipo | Condición |
|------|-----------|
| **Cuadrada** | $m = n$ |
| **Diagonal** | $a_{ij} = 0$ si $i \neq j$ |
| **Identidad** | $I_n$: diagonal con 1's |
| **Triangular superior** | $a_{ij} = 0$ si $i > j$ |
| **Triangular inferior** | $a_{ij} = 0$ si $i < j$ |
| **Simétrica** | $A = A^T$ |
| **Antisimétrica** | $A = -A^T$ |

---

## Operaciones

### Suma
$(A + B)_{ij} = a_{ij} + b_{ij}$

### Escalar
$(cA)_{ij} = c \cdot a_{ij}$

### Producto
$(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$

**Dimensiones:** $(m \times n) \cdot (n \times p) = (m \times p)$

---

## Transpuesta

$(A^T)_{ij} = a_{ji}$

**Propiedades:**
- $(A^T)^T = A$
- $(A + B)^T = A^T + B^T$
- $(cA)^T = cA^T$
- $(AB)^T = B^T A^T$

---

## Matriz Inversa

$AA^{-1} = A^{-1}A = I$

**Para $2 \times 2$:**
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \Rightarrow A^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

**Propiedades:**
- $(A^{-1})^{-1} = A$
- $(AB)^{-1} = B^{-1}A^{-1}$
- $(A^T)^{-1} = (A^{-1})^T$
