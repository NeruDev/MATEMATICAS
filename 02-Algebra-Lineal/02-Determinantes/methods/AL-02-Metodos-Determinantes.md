<!--
::METADATA::
type: method
topic_id: al-02-determinantes
file_id: AL-02-Metodos-Determinantes
status: stable
audience: student
last_updated: 2024-12-29
-->

# Métodos de Cálculo de Determinantes

> **Objetivo:** Dominar el cálculo de determinantes con algoritmos detallados, cálculos intermedios y ejemplos clásicos paso a paso.

---

## Método 1: Fórmula Directa $2 \times 2$

### Cuándo Usar
- Matrices de tamaño $2 \times 2$
- Cálculo inmediato

### Fórmula
$$\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$

### Regla Mnemotécnica
**Diagonal principal** menos **diagonal secundaria**

### Ejemplo Detallado

**Problema:** Calcular $\det(A)$ donde $A = \begin{pmatrix} 5 & 3 \\ 2 & 4 \end{pmatrix}$

**Solución:**
$$\det(A) = 5(4) - 3(2) = 20 - 6 = \boxed{14}$$

---

## Método 2: Regla de Sarrus ($3 \times 3$)

### Cuándo Usar
- **Solo** para matrices $3 \times 3$
- Método visual y rápido

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Escribir la matriz | Copiar las dos primeras columnas a la derecha |
| 2 | Diagonales descendentes | Sumar productos (→) |
| 3 | Diagonales ascendentes | Restar productos (←) |

### Diagrama Visual
```
| a  b  c | a  b
| d  e  f | d  e
| g  h  i | g  h

(+): aei + bfg + cdh
(-): ceg + afh + bdi

det = (+) - (-)
```

### Ejemplo Detallado

**Problema:** Calcular el determinante de $A = \begin{pmatrix} 2 & 1 & 3 \\ 4 & -1 & 2 \\ 1 & 5 & 1 \end{pmatrix}$

**Paso 1:** Copiamos las dos primeras columnas:
```
| 2   1   3 | 2   1
| 4  -1   2 | 4  -1
| 1   5   1 | 1   5
```

**Paso 2:** Diagonales descendentes (suma):
$$\begin{aligned}
&(2)(-1)(1) = -2 \\
&(1)(2)(1) = 2 \\
&(3)(4)(5) = 60
\end{aligned}$$
Suma: $-2 + 2 + 60 = 60$

**Paso 3:** Diagonales ascendentes (resta):
$$\begin{aligned}
&(3)(-1)(1) = -3 \\
&(2)(2)(5) = 20 \\
&(1)(4)(1) = 4
\end{aligned}$$
Suma: $-3 + 20 + 4 = 21$

**Paso 4:** Restamos:
$$\det(A) = 60 - 21 = \boxed{39}$$

---

## Método 3: Expansión por Cofactores

### Cuándo Usar
- Matrices de cualquier tamaño $n \times n$
- Especialmente eficiente cuando hay **muchos ceros** en una fila o columna

### Fórmulas

**Por fila $i$:**
$$\det(A) = \sum_{j=1}^{n} a_{ij} C_{ij}$$

**Por columna $j$:**
$$\det(A) = \sum_{i=1}^{n} a_{ij} C_{ij}$$

donde el **cofactor** es:
$$C_{ij} = (-1)^{i+j} M_{ij}$$

y $M_{ij}$ es el **menor** (determinante de la submatriz sin fila $i$ y columna $j$).

### Patrón de Signos
$$\begin{pmatrix} + & - & + & - & \cdots \\ - & + & - & + & \cdots \\ + & - & + & - & \cdots \\ \vdots & \vdots & \vdots & \vdots & \ddots \end{pmatrix}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Elegir fila o columna | Preferir la que tenga más ceros |
| 2 | Para cada elemento $a_{ij}$ | Calcular su cofactor $C_{ij}$ |
| 3 | Multiplicar y sumar | $\det = \sum a_{ij} C_{ij}$ |

### Ejemplo Detallado

**Problema:** Calcular el determinante de $A = \begin{pmatrix} 2 & 0 & 1 & 0 \\ 3 & 1 & 2 & 0 \\ 1 & 0 & 4 & 0 \\ 2 & 1 & 0 & 3 \end{pmatrix}$

**Paso 1:** Elegimos la **columna 4** (tiene tres ceros):
$$\det(A) = a_{14}C_{14} + a_{24}C_{24} + a_{34}C_{34} + a_{44}C_{44}$$
$$= 0 \cdot C_{14} + 0 \cdot C_{24} + 0 \cdot C_{34} + 3 \cdot C_{44}$$
$$= 3 \cdot C_{44}$$

**Paso 2:** Calculamos $C_{44}$:
$$C_{44} = (-1)^{4+4} M_{44} = (+1) \begin{vmatrix} 2 & 0 & 1 \\ 3 & 1 & 2 \\ 1 & 0 & 4 \end{vmatrix}$$

**Paso 3:** Expandimos por columna 2 (dos ceros):
$$M_{44} = 0 - 1 \cdot \begin{vmatrix} 2 & 1 \\ 1 & 4 \end{vmatrix} + 0 = -1(8-1) = -7$$

**Resultado:**
$$\det(A) = 3 \cdot (-7) = \boxed{-21}$$

---

## Método 4: Reducción a Forma Triangular

### Cuándo Usar
- Matrices grandes
- Método más eficiente computacionalmente

### Propiedad Clave
Para una matriz triangular (superior o inferior):
$$\det(A) = \prod_{i=1}^{n} a_{ii} = a_{11} \cdot a_{22} \cdot \ldots \cdot a_{nn}$$

### Efecto de las Operaciones de Fila

| Operación | Efecto en $\det$ |
|-----------|------------------|
| $R_i \leftrightarrow R_j$ | Cambia signo: $\det \to -\det$ |
| $kR_i \to R_i$ | Multiplica: $\det \to k \cdot \det$ |
| $R_i + kR_j \to R_i$ | **No cambia**: $\det \to \det$ |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Hacer ceros debajo de cada pivote | Usar $R_i + kR_j \to R_i$ |
| 2 | Registrar cambios de signo | Por cada intercambio de filas |
| 3 | Multiplicar diagonal | Y ajustar signo si hubo intercambios |

### Ejemplo Detallado

**Problema:** Calcular el determinante de $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 5 & 3 \\ 1 & 0 & 8 \end{pmatrix}$

**Paso 1:** $R_2 - 2R_1 \to R_2$ y $R_3 - R_1 \to R_3$:
$$\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & -3 \\ 0 & -2 & 5 \end{pmatrix}$$

**Paso 2:** $R_3 + 2R_2 \to R_3$:
$$\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & -3 \\ 0 & 0 & -1 \end{pmatrix}$$

**Paso 3:** Multiplicamos la diagonal:
$$\det(A) = 1 \cdot 1 \cdot (-1) = \boxed{-1}$$

> **Verificación por Sarrus:** 
> $(+): 1(5)(8) + 2(3)(1) + 3(2)(0) = 40 + 6 + 0 = 46$
> $(−): 3(5)(1) + 2(2)(8) + 1(3)(0) = 15 + 32 + 0 = 47$
> $\det = 46 - 47 = -1$ ✓

---

## Método 5: Propiedades para Simplificar

### Cuándo Usar
- Detectar determinante cero rápidamente
- Simplificar cálculos antes de expandir

### Propiedades Clave

| Condición | Resultado |
|-----------|-----------|
| Fila/columna de ceros | $\det = 0$ |
| Dos filas/columnas iguales | $\det = 0$ |
| Dos filas/columnas proporcionales | $\det = 0$ |
| Matriz triangular | $\det =$ producto de diagonal |
| $\det(AB) = \det(A) \cdot \det(B)$ | Producto de determinantes |
| $\det(A^T) = \det(A)$ | Transpuesta |
| $\det(kA) = k^n \det(A)$ | Para matriz $n \times n$ |
| $\det(A^{-1}) = \frac{1}{\det(A)}$ | Inversa |

### Ejemplo: Detectar det = 0

**Problema:** Sin calcular, determinar si $\det(A) = 0$:
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 5 & 7 & 9 \end{pmatrix}$$

**Observación:** Fila 3 = Fila 1 + Fila 2:
$$\begin{pmatrix} 5 & 7 & 9 \end{pmatrix} = \begin{pmatrix} 1 & 2 & 3 \end{pmatrix} + \begin{pmatrix} 4 & 5 & 6 \end{pmatrix}$$

**Resultado:** $\det(A) = \boxed{0}$ (las filas son linealmente dependientes)

---

## Método 6: Factor Común en Fila/Columna

### Cuándo Usar
- Simplificar antes de calcular
- Reducir números grandes

### Fórmula
Si una fila tiene factor común $k$:
$$\det\begin{pmatrix} ka_1 & ka_2 & ka_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{pmatrix} = k \cdot \det\begin{pmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{pmatrix}$$

### Ejemplo Detallado

**Problema:** Calcular $\det\begin{pmatrix} 6 & 12 & 18 \\ 1 & 2 & 1 \\ 2 & 1 & 3 \end{pmatrix}$

**Paso 1:** Sacamos factor 6 de la fila 1:
$$= 6 \cdot \det\begin{pmatrix} 1 & 2 & 3 \\ 1 & 2 & 1 \\ 2 & 1 & 3 \end{pmatrix}$$

**Paso 2:** Calculamos el determinante simplificado (Sarrus):
$$(+): 1(2)(3) + 2(1)(2) + 3(1)(1) = 6 + 4 + 3 = 13$$
$$(−): 3(2)(2) + 2(1)(3) + 1(1)(1) = 12 + 6 + 1 = 19$$
$$\det = 13 - 19 = -6$$

**Resultado:**
$$\det(A) = 6 \cdot (-6) = \boxed{-36}$$

---

## Método 7: Regla de Cramer

### Cuándo Usar
- Resolver sistemas $n \times n$ con $\det(A) \neq 0$
- Encontrar una variable específica sin resolver todo el sistema

### Fórmula
Para el sistema $Ax = b$:
$$x_i = \frac{\det(A_i)}{\det(A)}$$

donde $A_i$ es la matriz $A$ con la columna $i$ reemplazada por $b$.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Calcular $\det(A)$ | Verificar que $\det(A) \neq 0$ |
| 2 | Para cada variable $x_i$ | Formar $A_i$ reemplazando columna $i$ |
| 3 | Calcular $\det(A_i)$ | Para cada variable |
| 4 | Dividir | $x_i = \frac{\det(A_i)}{\det(A)}$ |

### Ejemplo Detallado

**Problema:** Resolver el sistema usando Cramer:
$$\begin{cases} 2x + y - z = 3 \\ x - y + 2z = 1 \\ 3x + 2y + z = 4 \end{cases}$$

**Paso 1:** Matriz de coeficientes y vector de términos independientes:
$$A = \begin{pmatrix} 2 & 1 & -1 \\ 1 & -1 & 2 \\ 3 & 2 & 1 \end{pmatrix}, \quad b = \begin{pmatrix} 3 \\ 1 \\ 4 \end{pmatrix}$$

**Paso 2:** Calculamos $\det(A)$ (por Sarrus):
$$(+): 2(-1)(1) + 1(2)(3) + (-1)(1)(2) = -2 + 6 - 2 = 2$$
$$(−): (-1)(-1)(3) + 1(1)(1) + 2(2)(2) = 3 + 1 + 8 = 12$$
$$\det(A) = 2 - 12 = -10$$

**Paso 3:** Calculamos $\det(A_x)$ (reemplazar columna 1 por $b$):
$$A_x = \begin{pmatrix} 3 & 1 & -1 \\ 1 & -1 & 2 \\ 4 & 2 & 1 \end{pmatrix}$$

$$(+): 3(-1)(1) + 1(2)(4) + (-1)(1)(2) = -3 + 8 - 2 = 3$$
$$(−): (-1)(-1)(4) + 1(1)(1) + 3(2)(2) = 4 + 1 + 12 = 17$$
$$\det(A_x) = 3 - 17 = -14$$

**Paso 4:** Calculamos $\det(A_y)$ (reemplazar columna 2):
$$A_y = \begin{pmatrix} 2 & 3 & -1 \\ 1 & 1 & 2 \\ 3 & 4 & 1 \end{pmatrix}$$

$$(+): 2(1)(1) + 3(2)(3) + (-1)(1)(4) = 2 + 18 - 4 = 16$$
$$(−): (-1)(1)(3) + 3(1)(1) + 2(2)(4) = -3 + 3 + 16 = 16$$
$$\det(A_y) = 16 - 16 = 0$$

**Paso 5:** Calculamos $\det(A_z)$ (reemplazar columna 3):
$$A_z = \begin{pmatrix} 2 & 1 & 3 \\ 1 & -1 & 1 \\ 3 & 2 & 4 \end{pmatrix}$$

$$(+): 2(-1)(4) + 1(1)(3) + 3(1)(2) = -8 + 3 + 6 = 1$$
$$(−): 3(-1)(3) + 1(1)(4) + 2(1)(2) = -9 + 4 + 4 = -1$$
$$\det(A_z) = 1 - (-1) = 2$$

**Paso 6:** Calculamos las soluciones:
$$x = \frac{-14}{-10} = \frac{7}{5}, \quad y = \frac{0}{-10} = 0, \quad z = \frac{2}{-10} = -\frac{1}{5}$$

**Resultado:**
$$\boxed{x = \frac{7}{5}, \quad y = 0, \quad z = -\frac{1}{5}}$$

---

## Método 8: Determinante de Matrices Especiales

### Matriz Diagonal
$$\det\begin{pmatrix} d_1 & 0 & 0 \\ 0 & d_2 & 0 \\ 0 & 0 & d_3 \end{pmatrix} = d_1 \cdot d_2 \cdot d_3$$

### Matriz Triangular (Superior o Inferior)
$$\det = \text{producto de la diagonal}$$

### Matriz por Bloques
$$\det\begin{pmatrix} A & B \\ 0 & D \end{pmatrix} = \det(A) \cdot \det(D)$$

### Ejemplo Detallado

**Problema:** Calcular $\det\begin{pmatrix} 3 & 1 & 4 & 1 \\ 0 & 5 & 9 & 2 \\ 0 & 0 & 6 & 5 \\ 0 & 0 & 0 & 4 \end{pmatrix}$

**Solución:** Es una matriz triangular superior.

$$\det = 3 \cdot 5 \cdot 6 \cdot 4 = \boxed{360}$$

---

## Método 9: Determinante y Área/Volumen

### Cuándo Usar
- Geometría: calcular áreas y volúmenes
- Verificar coplanaridad o colinealidad

### Fórmulas Geométricas

**Área de paralelogramo** (vectores $\vec{u}$, $\vec{v}$ en $\mathbb{R}^2$):
$$A = |\det\begin{pmatrix} u_1 & v_1 \\ u_2 & v_2 \end{pmatrix}|$$

**Área de triángulo** con vértices $(x_1,y_1)$, $(x_2,y_2)$, $(x_3,y_3)$:
$$A = \frac{1}{2}\left|\det\begin{pmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{pmatrix}\right|$$

**Volumen de paralelepípedo** (vectores $\vec{u}$, $\vec{v}$, $\vec{w}$):
$$V = |\det\begin{pmatrix} u_1 & v_1 & w_1 \\ u_2 & v_2 & w_2 \\ u_3 & v_3 & w_3 \end{pmatrix}|$$

### Ejemplo Detallado

**Problema:** Encontrar el área del triángulo con vértices $(1, 2)$, $(4, 6)$, $(2, 8)$

**Paso 1:** Formamos la matriz:
$$A = \frac{1}{2}\left|\det\begin{pmatrix} 1 & 2 & 1 \\ 4 & 6 & 1 \\ 2 & 8 & 1 \end{pmatrix}\right|$$

**Paso 2:** Calculamos el determinante (Sarrus):
$$(+): 1(6)(1) + 2(1)(2) + 1(4)(8) = 6 + 4 + 32 = 42$$
$$(−): 1(6)(2) + 2(4)(1) + 1(1)(8) = 12 + 8 + 8 = 28$$
$$\det = 42 - 28 = 14$$

**Paso 3:** Área:
$$A = \frac{1}{2}|14| = \boxed{7 \text{ unidades}^2}$$

---

## Método 10: Determinante de Vandermonde

### Cuándo Usar
- Matrices con estructura especial de potencias
- Interpolación polinomial

### Fórmula
$$\det\begin{pmatrix} 1 & x_1 & x_1^2 \\ 1 & x_2 & x_2^2 \\ 1 & x_3 & x_3^2 \end{pmatrix} = (x_2 - x_1)(x_3 - x_1)(x_3 - x_2)$$

### Fórmula General ($n \times n$)
$$\det(V) = \prod_{1 \leq i < j \leq n} (x_j - x_i)$$

### Ejemplo Detallado

**Problema:** Calcular $\det\begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 4 \\ 1 & 3 & 9 \end{pmatrix}$

**Identificación:** Es una matriz de Vandermonde con $x_1 = 1$, $x_2 = 2$, $x_3 = 3$.

**Aplicamos la fórmula:**
$$\det = (x_2 - x_1)(x_3 - x_1)(x_3 - x_2)$$
$$= (2 - 1)(3 - 1)(3 - 2)$$
$$= (1)(2)(1) = \boxed{2}$$
