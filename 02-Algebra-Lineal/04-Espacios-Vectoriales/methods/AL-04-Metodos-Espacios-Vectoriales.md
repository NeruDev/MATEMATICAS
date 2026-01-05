<!--
::METADATA::
type: method
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Métodos: Espacios Vectoriales

> Guía completa de métodos con algoritmos detallados, tablas de procedimientos y ejemplos paso a paso.

---

## Método 1: Verificar si un Conjunto es Subespacio

**Cuándo Usar:** Para determinar si un subconjunto $W$ de un [espacio vectorial](../../../glossary.md#espacio-vectorial) $V$ es a su vez un espacio vectorial.

**Teorema:** $W \subseteq V$ es [subespacio](../../../glossary.md#subespacio) si y solo si cumple las tres propiedades.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar no vacío | Comprobar que $\mathbf{0} \in W$ |
| 2 | Cerradura bajo suma | Si $u, v \in W$, verificar $u + v \in W$ |
| 3 | Cerradura escalar | Si $v \in W$, $c \in \mathbb{F}$, verificar $cv \in W$ |
| 4 | Concluir | Si pasa los 3 → [subespacio](../../../glossary.md#subespacio) |

### Ejemplo Detallado

**Problema:** Determinar si $W = \{(x, y, z) \in \mathbb{R}^3 : 2x - y + 3z = 0\}$ es subespacio de $\mathbb{R}^3$.

---

**Paso 1: Verificar que el [vector](../../../glossary.md#vector) cero pertenece a $W$**

**Paso 2: Verificar cerradura bajo la suma**

Sean $\mathbf{u} = (x_1, y_1, z_1)$ y $\mathbf{v} = (x_2, y_2, z_2)$ vectores en $W$.

Por definición de $W$:
- $2x_1 - y_1 + 3z_1 = 0$
- $2x_2 - y_2 + 3z_2 = 0$

La suma es:
$$\mathbf{u} + \mathbf{v} = (x_1 + x_2, y_1 + y_2, z_1 + z_2)$$

Verificamos si pertenece a $W$:
$$2(x_1 + x_2) - (y_1 + y_2) + 3(z_1 + z_2)$$
$$= (2x_1 - y_1 + 3z_1) + (2x_2 - y_2 + 3z_2)$$
$$= 0 + 0 = 0 \checkmark$$

La suma **sí pertenece** a $W$.

---

**Paso 3: Verificar cerradura bajo multiplicación escalar**

Sea $\mathbf{v} = (x, y, z) \in W$ y $c \in \mathbb{R}$.

Por definición: $2x - y + 3z = 0$

El producto escalar es:
$$c\mathbf{v} = (cx, cy, cz)$$

Verificamos:
$$2(cx) - (cy) + 3(cz) = c(2x - y + 3z) = c(0) = 0 \checkmark$$

El producto escalar **sí pertenece** a $W$.

---

**Conclusión:**

$$\boxed{W \text{ es subespacio de } \mathbb{R}^3}$$

---

### Contraejemplo: Conjunto que NO es Subespacio

**Problema:** ¿Es $W = \{(x, y) \in \mathbb{R}^2 : xy \geq 0\}$ subespacio?

**Paso 1:** $(0,0) \in W$ pues $0 \cdot 0 = 0 \geq 0$ ✓

**Paso 2 (Falla):** 
- $(1, 1) \in W$ pues $1 \cdot 1 = 1 \geq 0$ ✓
- $(-1, 1) \in W$ pues $(-1)(1) = -1 \not\geq 0$ ... en realidad NO

Tomemos: $(2, 0) \in W$ y $(0, -1) \in W$
- $(2, 0): 2 \cdot 0 = 0 \geq 0$ ✓
- $(0, -1): 0 \cdot (-1) = 0 \geq 0$ ✓
- Suma: $(2, -1): 2 \cdot (-1) = -2 \not\geq 0$ ✗

$$\boxed{W \text{ NO es subespacio}}$$

---

## Método 2: Determinar Independencia Lineal

**Cuándo Usar:** Para verificar si un conjunto de vectores $\{v_1, v_2, \ldots, v_k\}$ es linealmente independiente (LI) o linealmente dependiente (LD).

**Definición:** 
- **LI:** $c_1v_1 + c_2v_2 + \cdots + c_kv_k = \mathbf{0}$ solo tiene la solución [trivial](../../../glossary.md#trivial) ($c_i = 0$ para todo $i$).
- **LD:** Existe al menos una combinación no [trivial](../../../glossary.md#trivial) que da el vector cero.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Plantear ecuación | $c_1v_1 + c_2v_2 + \cdots + c_kv_k = \mathbf{0}$ |
| 2 | Formar [matriz](../../../glossary.md#matriz) | Vectores como columnas |
| 3 | Reducir a RREF | Operaciones de fila |
| 4 | Analizar soluciones | Solo trivial → LI; no triviales → LD |

### Ejemplo Detallado

**Problema:** Determinar si los vectores $v_1 = (1, 2, 1)$, $v_2 = (2, 3, 0)$, $v_3 = (0, 1, 2)$ son LI o LD.

---

**Paso 1: Plantear la ecuación**

$c_1(1, 2, 1) + c_2(2, 3, 0) + c_3(0, 1, 2) = (0, 0, 0)$

---

**Paso 2: Formar [matriz](../../../glossary.md#matriz) aumentada**
\end{array}\right)$$

---

**Paso 3: Reducir a forma escalonada**

$R_2 \leftarrow R_2 - 2R_1$:
$$\left(\begin{array}{ccc|c}
1 & 2 & 0 & 0 \\
0 & -1 & 1 & 0 \\
1 & 0 & 2 & 0
\end{array}\right)$$

$R_3 \leftarrow R_3 - R_1$:
$$\left(\begin{array}{ccc|c}
1 & 2 & 0 & 0 \\
0 & -1 & 1 & 0 \\
0 & -2 & 2 & 0
\end{array}\right)$$

$R_3 \leftarrow R_3 - 2R_2$:
$$\left(\begin{array}{ccc|c}
1 & 2 & 0 & 0 \\
0 & -1 & 1 & 0 \\
0 & 0 & 0 & 0
\end{array}\right)$$

---

**Paso 4: Análisis**

- Rango de la matriz = 2 (dos pivotes)
- Número de vectores = 3
- Hay variable libre ($c_3$ es libre)

De la fila 2: $-c_2 + c_3 = 0 \Rightarrow c_2 = c_3$

Si $c_3 = 1$: $c_2 = 1$

De la fila 1: $c_1 + 2c_2 = 0 \Rightarrow c_1 = -2$

**Combinación no trivial:** $-2v_1 + v_2 + v_3 = \mathbf{0}$

**Verificación:**
$$-2(1,2,1) + (2,3,0) + (0,1,2) = (-2+2+0, -4+3+1, -2+0+2) = (0,0,0) \checkmark$$

$$\boxed{\text{Los vectores son LD con relación: } v_3 = 2v_1 - v_2}$$

---

## Método 3: Encontrar Base del Espacio Generado (Span)

**Cuándo Usar:** Para hallar una [base](../../../glossary.md#base) del espacio generado por un conjunto de vectores, eliminando vectores redundantes.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Formar matriz | Vectores como **filas** |
| 2 | Reducir a REF | Operaciones elementales de fila |
| 3 | Identificar pivotes | Filas con pivotes corresponden a vectores [base](../../../glossary.md#base) |
| 4 | Concluir | Número de pivotes = [dimensión](../../../glossary.md#dimension) del span |

### Ejemplo Detallado

**Resultado:** La [dimensión](../../../glossary.md#dimension) del span es igual al número de pivotes: $\dim(\text{span}) = 2$

**Fórmula:** $\text{Nul}(A) = \{\mathbf{x} \in \mathbb{R}^n : A\mathbf{x} = \mathbf{0}\}$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Reducir a RREF | Llevar $A$ a forma escalonada reducida |
| 2 | Identificar variables | Libres (sin pivote) y ligadas (con pivote) |
| 3 | Parametrizar | Expresar ligadas en [función](../../../glossary.md#funcion) de las libres |
| 4 | Escribir [solución general](../../../glossary.md#solucion-general) | Como combinación lineal de vectores base |

### Ejemplo Detallado

**Paso 4: Escribir la solución [general](../../../glossary.md#solucion-general)**

**Paso 5: Conclusión**

$$\boxed{\text{Base de Nul}(A) = \left\{ \begin{pmatrix} -2 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} -1 \\ 0 \\ -1 \\ 1 \end{pmatrix} \right\}}$$

**Verificación:** $A \cdot (-2, 1, 0, 0)^T$:
$$\begin{pmatrix} 1(−2)+2(1)+0(0)+1(0) \\ 2(−2)+4(1)+1(0)+3(0) \\ 1(−2)+2(1)+1(0)+2(0) \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \checkmark$$

**Nulidad:** $\dim(\text{Nul}(A)) = 2$

---

## Método 5: Encontrar Base del Espacio Columna

**Cuándo Usar:** Para hallar una base del espacio generado por las columnas de una matriz $A$.

**Relación:** $\text{Col}(A) = \text{span}\{\text{columnas de } A\}$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Reducir a REF | Operaciones de fila sobre $A$ |
| 2 | Identificar pivotes | Columnas que contienen pivotes |
| 3 | Seleccionar columnas | Usar columnas **ORIGINALES** (no las reducidas) |

### Ejemplo Detallado

**Problema:** Encontrar base de $\text{Col}(A)$ para:
$$A = \begin{pmatrix}
1 & 3 & 5 & 2 \\
2 & 6 & 10 & 4 \\
1 & 1 & 2 & 1
\end{pmatrix}$$

---

**Paso 1: Reducir a forma escalonada**

$R_2 \leftarrow R_2 - 2R_1$:
$$\begin{pmatrix}
1 & 3 & 5 & 2 \\
0 & 0 & 0 & 0 \\
1 & 1 & 2 & 1
\end{pmatrix}$$

$R_3 \leftarrow R_3 - R_1$:
$$\begin{pmatrix}
1 & 3 & 5 & 2 \\
0 & 0 & 0 & 0 \\
0 & -2 & -3 & -1
\end{pmatrix}$$

Intercambiar $R_2 \leftrightarrow R_3$:
$$\begin{pmatrix}
1 & 3 & 5 & 2 \\
0 & -2 & -3 & -1 \\
0 & 0 & 0 & 0
\end{pmatrix}$$

---

**Paso 2: Identificar columnas con pivote**

- Pivote en columna **1** (fila 1)
- Pivote en columna **2** (fila 2)

---

**Paso 3: Seleccionar columnas originales**

Las columnas 1 y 2 de la matriz **original** $A$:

$$\mathbf{a}_1 = \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}, \quad \mathbf{a}_2 = \begin{pmatrix} 3 \\ 6 \\ 1 \end{pmatrix}$$

---

**Conclusión:**

$$\boxed{\text{Base de Col}(A) = \left\{ \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}, \begin{pmatrix} 3 \\ 6 \\ 1 \end{pmatrix} \right\}}$$

**Rango de $A$:** $\text{rango}(A) = \dim(\text{Col}(A)) = 2$

---

## Método 6: Calcular Coordenadas en una Base

**Cuándo Usar:** Para expresar un vector $\mathbf{v}$ como [combinación lineal](../../../glossary.md#combinacion-lineal) de los vectores de una base $\mathcal{B}$.

**Definición:** Si $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$ y $\mathbf{v} = c_1\mathbf{b}_1 + \cdots + c_n\mathbf{b}_n$, entonces:
$$[\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} c_1 \\ \vdots \\ c_n \end{pmatrix}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Formar matriz $B$ | Columnas = vectores de la base |
| 2 | Plantear sistema | $B \cdot [\mathbf{v}]_{\mathcal{B}} = \mathbf{v}$ |
| 3 | Resolver | Por Gauss-Jordan o inversión |
| 4 | Escribir coordenadas | $[\mathbf{v}]_{\mathcal{B}} = (c_1, \ldots, c_n)^T$ |

### Ejemplo Detallado

**Problema:** Hallar las coordenadas de $\mathbf{v} = (5, 7, 4)$ en la base:
$$\mathcal{B} = \left\{ \mathbf{b}_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \mathbf{b}_2 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}, \mathbf{b}_3 = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \right\}$$

---

**Paso 1: Formar la matriz aumentada**

$$\left(\begin{array}{ccc|c}
1 & 1 & 0 & 5 \\
1 & 0 & 1 & 7 \\
0 & 1 & 1 & 4
\end{array}\right)$$

---

**Paso 2: Reducir a RREF**

$R_2 \leftarrow R_2 - R_1$:
$$\left(\begin{array}{ccc|c}
1 & 1 & 0 & 5 \\
0 & -1 & 1 & 2 \\
0 & 1 & 1 & 4
\end{array}\right)$$

$R_3 \leftarrow R_3 + R_2$:
$$\left(\begin{array}{ccc|c}
1 & 1 & 0 & 5 \\
0 & -1 & 1 & 2 \\
0 & 0 & 2 & 6
\end{array}\right)$$

$R_3 \leftarrow \frac{1}{2}R_3$:
$$\left(\begin{array}{ccc|c}
1 & 1 & 0 & 5 \\
0 & -1 & 1 & 2 \\
0 & 0 & 1 & 3
\end{array}\right)$$

$R_2 \leftarrow R_2 - R_3$:
$$\left(\begin{array}{ccc|c}
1 & 1 & 0 & 5 \\
0 & -1 & 0 & -1 \\
0 & 0 & 1 & 3
\end{array}\right)$$

$R_2 \leftarrow -R_2$:
$$\left(\begin{array}{ccc|c}
1 & 1 & 0 & 5 \\
0 & 1 & 0 & 1 \\
0 & 0 & 1 & 3
\end{array}\right)$$

$R_1 \leftarrow R_1 - R_2$:
$$\left(\begin{array}{ccc|c}
1 & 0 & 0 & 4 \\
0 & 1 & 0 & 1 \\
0 & 0 & 1 & 3
\end{array}\right)$$

---

**Paso 3: Leer solución**

$$c_1 = 4, \quad c_2 = 1, \quad c_3 = 3$$

---

**Verificación:**

$$4\mathbf{b}_1 + 1\mathbf{b}_2 + 3\mathbf{b}_3 = 4\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} + 3\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$$

$$= \begin{pmatrix} 4 \\ 4 \\ 0 \end{pmatrix} + \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} + \begin{pmatrix} 0 \\ 3 \\ 3 \end{pmatrix} = \begin{pmatrix} 5 \\ 7 \\ 4 \end{pmatrix} \checkmark$$

$$\boxed{[\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} 4 \\ 1 \\ 3 \end{pmatrix}}$$

---

## Método 7: Calcular Matriz de Cambio de Base

**Cuándo Usar:** Para convertir coordenadas de una base $\mathcal{B}$ a otra base $\mathcal{B}'$.

**Fórmula:** Si $[\mathbf{v}]_{\mathcal{B}} = \mathbf{x}$ y $[\mathbf{v}]_{\mathcal{B}'} = \mathbf{y}$, entonces:
$$\mathbf{y} = P_{\mathcal{B} \to \mathcal{B}'} \cdot \mathbf{x}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Formar matriz | $(B' \mid B)$ donde columnas son vectores de cada base |
| 2 | Reducir | Aplicar Gauss-Jordan hasta $(I \mid P)$ |
| 3 | Extraer | $P = P_{\mathcal{B} \to \mathcal{B}'}$ es la parte derecha |

### Ejemplo Detallado

**Problema:** Encontrar la matriz de cambio de base de $\mathcal{B}$ a $\mathcal{B}'$ donde:
$$\mathcal{B} = \{(1, 0), (0, 1)\} \text{ (estándar)}, \quad \mathcal{B}' = \{(2, 1), (1, 1)\}$$

---

**Paso 1: Formar matriz aumentada $(B' \mid B)$**

$$\left(\begin{array}{cc|cc}
2 & 1 & 1 & 0 \\
1 & 1 & 0 & 1
\end{array}\right)$$

---

**Paso 2: Reducir a $(I \mid P)$**

$R_1 \leftrightarrow R_2$:
$$\left(\begin{array}{cc|cc}
1 & 1 & 0 & 1 \\
2 & 1 & 1 & 0
\end{array}\right)$$

$R_2 \leftarrow R_2 - 2R_1$:
$$\left(\begin{array}{cc|cc}
1 & 1 & 0 & 1 \\
0 & -1 & 1 & -2
\end{array}\right)$$

$R_2 \leftarrow -R_2$:
$$\left(\begin{array}{cc|cc}
1 & 1 & 0 & 1 \\
0 & 1 & -1 & 2
\end{array}\right)$$

$R_1 \leftarrow R_1 - R_2$:
$$\left(\begin{array}{cc|cc}
1 & 0 & 1 & -1 \\
0 & 1 & -1 & 2
\end{array}\right)$$

---

**Paso 3: Extraer la matriz**

$$\boxed{P_{\mathcal{B} \to \mathcal{B}'} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}}$$

---

**Verificación:** Si $\mathbf{v} = (3, 2)$, entonces $[\mathbf{v}]_{\mathcal{B}} = (3, 2)^T$ (base estándar).

$$[\mathbf{v}]_{\mathcal{B}'} = P \cdot [\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 3 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

Comprobación: $1 \cdot (2,1) + 1 \cdot (1,1) = (2+1, 1+1) = (3, 2)$ ✓

---

## Método 8: Extender Conjunto LI a Base

**Cuándo Usar:** Cuando tienes un conjunto linealmente independiente y necesitas completarlo para formar una base del espacio.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar LI | Confirmar que el conjunto dado es LI |
| 2 | Calcular [dimensión](../../../glossary.md#independencia-lineal) | $c_1v_1 + \cdots + c_nv_n = \mathbf{0} \Rightarrow$ todos $c_i = 0$ |
| Dimensión | Número de vectores en cualquier base |
| Rango | $= \dim(\text{Col}(A)) = \dim(\text{Row}(A))$ |
| Nulidad | $= \dim(\text{Nul}(A)) =$ número de variables libres |
| Rango-Nulidad | $\text{rango}(A) + \text{nulidad}(A) = n$ |
| Cambio de base | $[\mathbf{v}]_{\mathcal{B}'} = P_{\mathcal{B} \to \mathcal{B}'} [\mathbf{v}]_{\mathcal{B}}$ |
| Suma directa | $V = W_1 \oplus W_2 \Leftrightarrow V = W_1 + W_2$ y $W_1 \cap W_2 = \{\mathbf{0}\}$ |
| Coordenadas | $[\mathbf{v}]_{\mathcal{B}} = B^{-1}\mathbf{v}$ donde $B$ tiene vectores base como columnas |

---

## Errores Comunes

| Error | Corrección |
|-------|------------|
| Usar filas reducidas para base de $\text{Col}(A)$ | Usar columnas **originales** correspondientes a pivotes |
| Confundir suma directa con suma | Verificar también que $W_1 \cap W_2 = \{\mathbf{0}\}$ |
| Olvidar verificar $\mathbf{0} \in W$ | Siempre es el primer paso al verificar subespacio |
| Confundir LI con generadores | LI: solo solución trivial; generadores: todo vector es combinación |
| Invertir orden en cambio de base | $P_{\mathcal{B} \to \mathcal{B}'}$ transforma **de** $\mathcal{B}$ **a** $\mathcal{B}'$ |
