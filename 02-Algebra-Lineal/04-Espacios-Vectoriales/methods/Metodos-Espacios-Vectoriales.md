<!--
content_type: methods
topic: Espacios Vectoriales
---
-->

# Métodos: Espacios Vectoriales

---

## Método 1: Verificar si un Conjunto es Subespacio

**Objetivo:** Determinar si $W \subseteq V$ es subespacio vectorial.

### Pasos

1. **Verificar no vacío:** Comprobar que $\mathbf{0} \in W$
2. **Verificar cerradura bajo suma:** Si $u, v \in W$, verificar que $u + v \in W$
3. **Verificar cerradura escalar:** Si $v \in W$ y $c \in \mathbb{F}$, verificar que $cv \in W$

### Ejemplo

¿Es $W = \{(x, y, z) \in \mathbb{R}^3 : x + 2y - z = 0\}$ subespacio?

**Paso 1:** $\mathbf{0} = (0,0,0)$: $0 + 2(0) - 0 = 0$ ✓

**Paso 2:** Sean $u = (x_1, y_1, z_1)$, $v = (x_2, y_2, z_2) \in W$
- $u + v = (x_1+x_2, y_1+y_2, z_1+z_2)$
- $(x_1+x_2) + 2(y_1+y_2) - (z_1+z_2) = (x_1+2y_1-z_1) + (x_2+2y_2-z_2) = 0 + 0 = 0$ ✓

**Paso 3:** Sea $v = (x, y, z) \in W$, $c \in \mathbb{R}$
- $cv = (cx, cy, cz)$
- $cx + 2(cy) - cz = c(x + 2y - z) = c(0) = 0$ ✓

**Conclusión:** $W$ **es subespacio**.

---

## Método 2: Determinar Independencia Lineal

**Objetivo:** Verificar si $\{v_1, v_2, ..., v_k\}$ es LI.

### Pasos

1. Formar la ecuación $c_1v_1 + c_2v_2 + ... + c_kv_k = \mathbf{0}$
2. Escribir como sistema de ecuaciones o matriz aumentada
3. Reducir a forma escalonada
4. **Si solo hay solución trivial** $(c_i = 0)$ → **LI**
5. **Si hay soluciones no triviales** → **LD**

### Ejemplo

¿Son $v_1 = (1, 2, 3)$, $v_2 = (4, 5, 6)$, $v_3 = (2, 1, 0)$ LI?

$$\begin{pmatrix} 1 & 4 & 2 & | & 0 \\ 2 & 5 & 1 & | & 0 \\ 3 & 6 & 0 & | & 0 \end{pmatrix}$$

Reduciendo:
$$\rightarrow \begin{pmatrix} 1 & 4 & 2 \\ 0 & -3 & -3 \\ 0 & 0 & 0 \end{pmatrix}$$

Hay columna sin pivote → variable libre → **LD**

---

## Método 3: Encontrar Base del Span

**Objetivo:** Hallar una base de $\text{span}\{v_1, ..., v_k\}$.

### Pasos

1. Formar matriz $A$ con los vectores como **filas**
2. Reducir a forma escalonada REF
3. Las filas no nulas de la matriz **original** correspondientes a pivotes forman base

### Ejemplo

Encontrar base de $\text{span}\{(1,2,1), (2,4,2), (1,1,0)\}$

$$A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 1 & 0 \end{pmatrix} \rightarrow \begin{pmatrix} 1 & 2 & 1 \\ 0 & 0 & 0 \\ 0 & -1 & -1 \end{pmatrix} \rightarrow \begin{pmatrix} 1 & 2 & 1 \\ 0 & -1 & -1 \\ 0 & 0 & 0 \end{pmatrix}$$

Pivotes en filas 1 y 3 (después de reordenar): 

**Base:** $\{(1, 2, 1), (1, 1, 0)\}$

---

## Método 4: Encontrar Base del Espacio Nulo

**Objetivo:** Hallar base de $\text{Nul}(A) = \{x : Ax = \mathbf{0}\}$.

### Pasos

1. Reducir $A$ a RREF
2. Identificar variables libres y ligadas
3. Expresar variables ligadas en términos de las libres
4. Escribir la solución general parametrizada
5. Los vectores que acompañan a cada parámetro forman la base

### Ejemplo

Encontrar base de $\text{Nul}(A)$ donde $A = \begin{pmatrix} 1 & 2 & 1 & 0 \\ 2 & 4 & 0 & 2 \end{pmatrix}$

RREF:
$$\begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & -1 \end{pmatrix}$$

Variables libres: $x_2 = s$, $x_4 = t$
Variables ligadas: $x_1 = -2s - t$, $x_3 = t$

$$x = \begin{pmatrix} -2s - t \\ s \\ t \\ t \end{pmatrix} = s\begin{pmatrix} -2 \\ 1 \\ 0 \\ 0 \end{pmatrix} + t\begin{pmatrix} -1 \\ 0 \\ 1 \\ 1 \end{pmatrix}$$

**Base:** $\left\{\begin{pmatrix} -2 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} -1 \\ 0 \\ 1 \\ 1 \end{pmatrix}\right\}$

---

## Método 5: Encontrar Base del Espacio Columna

**Objetivo:** Hallar base de $\text{Col}(A)$.

### Pasos

1. Reducir $A$ a forma escalonada REF
2. Identificar las columnas con pivote
3. Las columnas **originales** correspondientes forman la base

### Ejemplo

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 5 \\ 2 & 5 & 8 \end{pmatrix}$$

REF:
$$\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{pmatrix}$$

Pivotes en columnas 1 y 2.

**Base de $\text{Col}(A)$:** $\left\{\begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix}, \begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix}\right\}$

---

## Método 6: Calcular Coordenadas en una Base

**Objetivo:** Encontrar $[v]_{\mathcal{B}}$ dado $v$ y base $\mathcal{B} = \{b_1, ..., b_n\}$.

### Pasos

1. Plantear $v = c_1 b_1 + c_2 b_2 + ... + c_n b_n$
2. Formar sistema de ecuaciones
3. Resolver para $c_1, c_2, ..., c_n$
4. $[v]_{\mathcal{B}} = (c_1, c_2, ..., c_n)^T$

### Método Matricial (en $\mathbb{R}^n$)

1. Formar matriz $B$ con vectores de base como columnas
2. Resolver $B \cdot [v]_{\mathcal{B}} = v$
3. $[v]_{\mathcal{B}} = B^{-1} v$

### Ejemplo

$\mathcal{B} = \{(1, 1), (1, -1)\}$, $v = (5, 1)$

$$\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \end{pmatrix} = \begin{pmatrix} 5 \\ 1 \end{pmatrix}$$

Resolviendo: $c_1 = 3$, $c_2 = 2$

**$[v]_{\mathcal{B}} = \begin{pmatrix} 3 \\ 2 \end{pmatrix}$**

---

## Método 7: Calcular Matriz de Cambio de Base

**Objetivo:** Encontrar $P_{\mathcal{B} \to \mathcal{B}'}$.

### Pasos (Método de la Matriz Aumentada)

1. Sea $\mathcal{B} = \{v_1, ..., v_n\}$ y $\mathcal{B}' = \{w_1, ..., w_n\}$
2. Formar la matriz aumentada $(B' | B)$
3. Reducir a $(I | P)$ usando operaciones de fila
4. $P = P_{\mathcal{B} \to \mathcal{B}'}$

### Ejemplo

$\mathcal{B} = \{(1, 0), (0, 1)\}$ (estándar), $\mathcal{B}' = \{(1, 1), (1, -1)\}$

$$\left(\begin{array}{cc|cc} 1 & 1 & 1 & 0 \\ 1 & -1 & 0 & 1 \end{array}\right)$$

$R_2 \leftarrow R_2 - R_1$:
$$\left(\begin{array}{cc|cc} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \end{array}\right)$$

$R_2 \leftarrow -\frac{1}{2}R_2$:
$$\left(\begin{array}{cc|cc} 1 & 1 & 1 & 0 \\ 0 & 1 & 1/2 & -1/2 \end{array}\right)$$

$R_1 \leftarrow R_1 - R_2$:
$$\left(\begin{array}{cc|cc} 1 & 0 & 1/2 & 1/2 \\ 0 & 1 & 1/2 & -1/2 \end{array}\right)$$

**$P_{\mathcal{B} \to \mathcal{B}'} = \begin{pmatrix} 1/2 & 1/2 \\ 1/2 & -1/2 \end{pmatrix}$**

---

## Método 8: Extender a una Base

**Objetivo:** Dado un conjunto LI $S$, extenderlo a una base de $V$.

### Pasos

1. Partir del conjunto LI dado $S = \{v_1, ..., v_k\}$
2. Tomar vectores de la base estándar $\{e_1, ..., e_n\}$
3. Añadir $e_i$ a $S$ si mantiene independencia lineal
4. Repetir hasta tener $n$ vectores

### Ejemplo

Extender $S = \{(1, 1, 0)\}$ a base de $\mathbb{R}^3$.

Probamos $e_1 = (1, 0, 0)$:
$$\begin{pmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 0 \end{pmatrix}$$ 
No, porque $\text{rango} = 2$ pero solo en las primeras 2 filas.

Probamos $e_2 = (0, 1, 0)$: Similar análisis.

Probamos $e_3 = (0, 0, 1)$:
$\{(1,1,0), (0,0,1)\}$ son LI.

Añadimos $e_1 = (1, 0, 0)$:
$\{(1,1,0), (0,0,1), (1,0,0)\}$ son LI.

**Base extendida:** $\{(1,1,0), (0,0,1), (1,0,0)\}$
