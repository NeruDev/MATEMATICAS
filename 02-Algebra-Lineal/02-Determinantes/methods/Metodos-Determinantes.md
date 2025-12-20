<!--
content_type: methods
format: step_by_step
---
-->

# Métodos de Cálculo de Determinantes

---

## Método 1: Fórmula Directa $2 \times 2$

$$\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$

**Ejemplo:**
$$\det\begin{pmatrix} 3 & 2 \\ 1 & 4 \end{pmatrix} = 3(4) - 2(1) = 10$$

---

## Método 2: Regla de Sarrus ($3 \times 3$)

**Pasos:**
1. Copiar las dos primeras columnas a la derecha.
2. Sumar productos de diagonales hacia abajo.
3. Restar productos de diagonales hacia arriba.

**Ejemplo:**
$$\begin{vmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{vmatrix}$$

Diagonales (+): $1·5·9 + 2·6·7 + 3·4·8 = 45 + 84 + 96 = 225$
Diagonales (−): $3·5·7 + 2·4·9 + 1·6·8 = 105 + 72 + 48 = 225$

$\det = 225 - 225 = 0$

---

## Método 3: Expansión por Cofactores

**Pasos:**
1. Elegir fila o columna (preferir la que tenga más ceros).
2. Calcular $\det = \sum a_{ij} C_{ij}$ donde $C_{ij} = (-1)^{i+j} M_{ij}$.

**Ejemplo:** $\begin{vmatrix} 2 & 0 & 1 \\ 3 & 1 & 2 \\ 1 & 0 & 4 \end{vmatrix}$

Expandir por columna 2 (dos ceros):
$$= 0 \cdot C_{12} + 1 \cdot C_{22} + 0 \cdot C_{32} = C_{22}$$

$$C_{22} = (+1)\begin{vmatrix} 2 & 1 \\ 1 & 4 \end{vmatrix} = 8 - 1 = 7$$

---

## Método 4: Reducción a Triangular

**Pasos:**
1. Usar operaciones de fila para obtener forma triangular.
2. Multiplicar elementos de la diagonal.
3. Ajustar signo si se intercambiaron filas.

**Ejemplo:**
$$\begin{vmatrix} 1 & 2 & 3 \\ 2 & 3 & 4 \\ 3 & 5 & 6 \end{vmatrix}$$

$R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - 3R_1$:
$$\begin{vmatrix} 1 & 2 & 3 \\ 0 & -1 & -2 \\ 0 & -1 & -3 \end{vmatrix}$$

$R_3 \leftarrow R_3 - R_2$:
$$\begin{vmatrix} 1 & 2 & 3 \\ 0 & -1 & -2 \\ 0 & 0 & -1 \end{vmatrix} = 1 \cdot (-1) \cdot (-1) = 1$$

---

## Método 5: Matriz Adjunta e Inversa

**Para encontrar $A^{-1}$:**

1. Calcular todos los cofactores $C_{ij}$.
2. Formar matriz de cofactores $C$.
3. Transponer: $\text{adj}(A) = C^T$.
4. Dividir: $A^{-1} = \frac{1}{\det(A)} \text{adj}(A)$.

**Ejemplo:** $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$

$\det(A) = -2$

Cofactores: $C_{11} = 4$, $C_{12} = -3$, $C_{21} = -2$, $C_{22} = 1$

$\text{adj}(A) = \begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix}$

$A^{-1} = \frac{1}{-2}\begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix}$

---

## Método 6: Regla de Cramer

**Para resolver $Ax = b$:**

1. Calcular $\det(A)$.
2. Para cada variable $x_i$, reemplazar columna $i$ de $A$ por $b$.
3. Calcular $x_i = \frac{\det(A_i)}{\det(A)}$.

**Ejemplo:** $\begin{cases} x + 2y = 5 \\ 3x + 4y = 11 \end{cases}$

$\det(A) = 4 - 6 = -2$

$x = \frac{\begin{vmatrix} 5 & 2 \\ 11 & 4 \end{vmatrix}}{-2} = \frac{20 - 22}{-2} = 1$

$y = \frac{\begin{vmatrix} 1 & 5 \\ 3 & 11 \end{vmatrix}}{-2} = \frac{11 - 15}{-2} = 2$

---

## Método 7: Propiedades para Simplificar

**Atajos útiles:**
- Fila/columna de ceros → $\det = 0$
- Filas proporcionales → $\det = 0$
- Matriz triangular → producto de diagonal
- Factor común en fila → se puede sacar

**Ejemplo:**
$$\begin{vmatrix} 2 & 4 & 6 \\ 1 & 3 & 5 \\ 0 & 0 & 7 \end{vmatrix} = 2\begin{vmatrix} 1 & 2 & 3 \\ 1 & 3 & 5 \\ 0 & 0 & 7 \end{vmatrix}$$

Expandir por fila 3: $= 2 \cdot 7 \cdot \begin{vmatrix} 1 & 2 \\ 1 & 3 \end{vmatrix} = 14(1) = 14$
