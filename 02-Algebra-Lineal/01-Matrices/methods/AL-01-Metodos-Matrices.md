<!--
::METADATA::
type: method
topic_id: al-01-matrices
file_id: AL-01-Metodos-Matrices
status: stable
audience: student
last_updated: 2024-12-23
-->

# Métodos de Cálculo con Matrices

---

## Método 1: Suma y Resta de Matrices

**Requisito:** Mismas dimensiones.

**Pasos:**
1. Verificar que las dimensiones coincidan.
2. Sumar/restar elemento a elemento.

**Ejemplo:**
$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix}$$

---

## Método 2: Multiplicación por Escalar

**Pasos:**
1. Multiplicar cada elemento por el escalar.

**Ejemplo:**
$$3 \cdot \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 3 & 6 \\ 9 & 12 \end{pmatrix}$$

---

## Método 3: Multiplicación de Matrices (Fila × Columna)

**Requisito:** Columnas de $A$ = Filas de $B$.

**Pasos:**
1. Verificar dimensiones: $(m \times n) \cdot (n \times p) = (m \times p)$
2. Para cada elemento $(i,j)$: multiplicar fila $i$ de $A$ por columna $j$ de $B$
3. Sumar los productos.

**Ejemplo:**
$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$$

- $(1,1)$: $1(5) + 2(7) = 19$
- $(1,2)$: $1(6) + 2(8) = 22$
- $(2,1)$: $3(5) + 4(7) = 43$
- $(2,2)$: $3(6) + 4(8) = 50$

$$= \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$$

---

## Método 4: Transpuesta

**Pasos:**
1. Intercambiar filas por columnas.
2. La fila $i$ se convierte en columna $i$.

**Ejemplo:**
$$\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}^T = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$$

---

## Método 5: Inversa de Matriz $2 \times 2$

**Fórmula:**
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

**Pasos:**
1. Calcular determinante: $\det = ad - bc$
2. Si $\det = 0$: no existe inversa.
3. Intercambiar elementos de la diagonal principal.
4. Cambiar signo de la diagonal secundaria.
5. Dividir todo entre el determinante.

**Ejemplo:**
$$A = \begin{pmatrix} 4 & 3 \\ 2 & 1 \end{pmatrix}$$

1. $\det = 4(1) - 3(2) = -2$
2. $A^{-1} = \frac{1}{-2}\begin{pmatrix} 1 & -3 \\ -2 & 4 \end{pmatrix} = \begin{pmatrix} -1/2 & 3/2 \\ 1 & -2 \end{pmatrix}$

---

## Método 6: Inversa por Gauss-Jordan

**Pasos:**
1. Escribir $(A | I)$
2. Aplicar operaciones elementales de fila:
   - Intercambiar filas
   - Multiplicar fila por escalar no nulo
   - Sumar múltiplo de una fila a otra
3. Reducir hasta obtener $(I | A^{-1})$

**Ejemplo:** Encontrar inversa de $A = \begin{pmatrix} 1 & 2 \\ 3 & 7 \end{pmatrix}$

$$\left(\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 3 & 7 & 0 & 1 \end{array}\right)$$

$R_2 \leftarrow R_2 - 3R_1$:
$$\left(\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & 1 & -3 & 1 \end{array}\right)$$

$R_1 \leftarrow R_1 - 2R_2$:
$$\left(\begin{array}{cc|cc} 1 & 0 & 7 & -2 \\ 0 & 1 & -3 & 1 \end{array}\right)$$

$$A^{-1} = \begin{pmatrix} 7 & -2 \\ -3 & 1 \end{pmatrix}$$

---

## Método 7: Verificar si una Matriz es Invertible

**Criterios:**
1. $\det(A) \neq 0$
2. Las filas son linealmente independientes
3. Las columnas son linealmente independientes
4. $\text{rango}(A) = n$ (para $n \times n$)

---

## Método 8: Potencias de Matrices

**Para potencias pequeñas:** Multiplicar sucesivamente.

**Para diagonalizables:** Si $A = PDP^{-1}$ donde $D$ es diagonal:
$$A^n = PD^nP^{-1}$$

**Ejemplo:** $A^2$
$$A^2 = A \cdot A$$

Calcular directamente multiplicando.
