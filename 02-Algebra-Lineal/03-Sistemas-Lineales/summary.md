# Resumen: Sistemas de Ecuaciones Lineales

---

## Forma Matricial

$$Ax = b$$

$$\begin{pmatrix} a_{11} & \cdots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \cdots & a_{mn} \end{pmatrix} \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} = \begin{pmatrix} b_1 \\ \vdots \\ b_m \end{pmatrix}$$

**Matriz aumentada:** $(A | b)$

---

## Operaciones Elementales de Fila

1. Intercambiar filas: $R_i \leftrightarrow R_j$
2. Multiplicar fila por escalar: $R_i \leftarrow kR_i$ $(k \neq 0)$
3. Sumar múltiplo: $R_i \leftarrow R_i + kR_j$

---

## Forma Escalonada

**REF (Row Echelon Form):**
- Filas de ceros al fondo
- Pivote a la derecha del pivote superior
- Ceros debajo de cada pivote

**RREF (Reduced REF):**
- Pivotes = 1
- Ceros arriba y abajo de cada pivote

---

## Clasificación de Soluciones

| Condición | Tipo | Solución |
|-----------|------|----------|
| $\text{rango}(A) = \text{rango}(A|b) = n$ | Compatible determinado | Única |
| $\text{rango}(A) = \text{rango}(A|b) < n$ | Compatible indeterminado | Infinitas |
| $\text{rango}(A) < \text{rango}(A|b)$ | Incompatible | Ninguna |

---

## Rango

$\text{rango}(A)$ = número de pivotes = número de filas no nulas en REF

---

## Sistemas Homogéneos

$Ax = 0$ siempre tiene solución ($x = 0$).

Solución no trivial existe $\Leftrightarrow \text{rango}(A) < n$
