<!--
::METADATA::
type: method
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Métodos: Transformaciones Lineales

> Guía completa de métodos con algoritmos detallados, tablas de procedimientos y ejemplos paso a paso.

---

## Método 1: Verificar si una Función es Transformación Lineal

**Cuándo Usar:** Para determinar si una [función](../../../glossary.md#funcion) $T: V \to W$ preserva la estructura de [espacio vectorial](../../../glossary.md#espacio-vectorial).

**Definición:** $T$ es lineal si y solo si cumple:
1. $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ (aditividad)
2. $T(c\mathbf{v}) = cT(\mathbf{v})$ (homogeneidad)

**Equivalente:** $T(c_1\mathbf{u} + c_2\mathbf{v}) = c_1T(\mathbf{u}) + c_2T(\mathbf{v})$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar $T(\mathbf{0})$ | Si $T(\mathbf{0}) \neq \mathbf{0}$, no es lineal |
| 2 | Tomar vectores genéricos | $\mathbf{u} = (x_1, y_1, \ldots)$, $\mathbf{v} = (x_2, y_2, \ldots)$ |
| 3 | Calcular $T(\mathbf{u} + \mathbf{v})$ | Aplicar la fórmula de $T$ a la suma |
| 4 | Calcular $T(\mathbf{u}) + T(\mathbf{v})$ | Sumar las imágenes individuales |
| 5 | Comparar | Si coinciden, verificar homogeneidad |
| 6 | Verificar $T(c\mathbf{v}) = cT(\mathbf{v})$ | Para escalar arbitrario $c$ |

### Ejemplo Detallado: Transformación Lineal

**Problema:** ¿Es $T: \mathbb{R}^3 \to \mathbb{R}^2$ definida por $T(x, y, z) = (2x - y + z, x + 3y)$ una [transformación lineal](../../../glossary.md#transformacion-lineal)?

---

**Paso 1: Verificar $T(\mathbf{0})$**

$$T(0, 0, 0) = (2(0) - 0 + 0, 0 + 3(0)) = (0, 0) \checkmark$$

---

**Paso 2: Verificar aditividad**

Sean $\mathbf{u} = (x_1, y_1, z_1)$ y $\mathbf{v} = (x_2, y_2, z_2)$.

**Calcular $T(\mathbf{u} + \mathbf{v})$:**
$$\mathbf{u} + \mathbf{v} = (x_1 + x_2, y_1 + y_2, z_1 + z_2)$$

$$T(\mathbf{u} + \mathbf{v}) = (2(x_1+x_2) - (y_1+y_2) + (z_1+z_2), (x_1+x_2) + 3(y_1+y_2))$$

$$= (2x_1 + 2x_2 - y_1 - y_2 + z_1 + z_2, x_1 + x_2 + 3y_1 + 3y_2)$$

**Calcular $T(\mathbf{u}) + T(\mathbf{v})$:**
$$T(\mathbf{u}) = (2x_1 - y_1 + z_1, x_1 + 3y_1)$$
$$T(\mathbf{v}) = (2x_2 - y_2 + z_2, x_2 + 3y_2)$$

$$T(\mathbf{u}) + T(\mathbf{v}) = (2x_1 - y_1 + z_1 + 2x_2 - y_2 + z_2, x_1 + 3y_1 + x_2 + 3y_2)$$

$$= (2x_1 + 2x_2 - y_1 - y_2 + z_1 + z_2, x_1 + x_2 + 3y_1 + 3y_2)$$

**Comparación:** $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ ✓

---

**Paso 3: Verificar homogeneidad**

Sea $c \in \mathbb{R}$ y $\mathbf{v} = (x, y, z)$.

$$T(c\mathbf{v}) = T(cx, cy, cz) = (2(cx) - (cy) + (cz), (cx) + 3(cy))$$

$$= (2cx - cy + cz, cx + 3cy) = c(2x - y + z, x + 3y) = cT(\mathbf{v}) \checkmark$$

---

**Conclusión:**

$$\boxed{T \text{ es una [transformación lineal](../../../glossary.md#transformacion-lineal)}}$$

---

### Ejemplo: Transformación NO Lineal

**Problema:** ¿Es $T: \mathbb{R}^2 \to \mathbb{R}^2$ definida por $T(x, y) = (x + 1, y^2)$ lineal?

---

**Paso 1: Verificar $T(\mathbf{0})$**

$$T(0, 0) = (0 + 1, 0^2) = (1, 0) \neq (0, 0)$$

$$\boxed{T \text{ NO es lineal (falla en el [vector](../../../glossary.md#vector) cero)}}$$

---

### Ejemplo: Otra Transformación NO Lineal

**Problema:** ¿Es $T(x, y) = (xy, x + y)$ lineal?

**Verificación de aditividad:**

$$T(1, 0) + T(0, 1) = (0, 1) + (0, 1) = (0, 2)$$

$$T(1, 0) + (0, 1)) = T(1, 1) = (1 \cdot 1, 1 + 1) = (1, 2)$$

$$(0, 2) \neq (1, 2)$$

$$\boxed{T \text{ NO es lineal (falla aditividad)}}$$

---

## Método 2: Encontrar el Núcleo de una Transformación

**Cuándo Usar:** Para hallar todos los vectores que $T$ envía al [vector](../../../glossary.md#vector) cero.

**Definición:** $\ker(T) = \{\mathbf{v} \in V : T(\mathbf{v}) = \mathbf{0}\}$

**Propiedades:**
- $\ker(T)$ es [subespacio](../../../glossary.md#subespacio) de $V$
- $\dim(\ker(T)) =$ nulidad de $T$
- $T$ inyectiva $\Leftrightarrow \ker(T) = \{\mathbf{0}\}$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Plantear ecuación | $T(\mathbf{v}) = \mathbf{0}$ |
| 2 | Escribir sistema | Igualar cada componente a cero |
| 3 | Formar [matriz](../../../glossary.md#matriz) aumentada | Coeficientes del sistema |
| 4 | Reducir a RREF | Gauss-Jordan |
| 5 | Parametrizar | Expresar en [función](../../../glossary.md#funcion) de variables libres |
| 6 | Extraer [base](../../../glossary.md#base) | Vectores que multiplican parámetros |

### Ejemplo Detallado

**Problema:** Encontrar $\ker(T)$ y su [base](../../../glossary.md#base) para $T: \mathbb{R}^4 \to \mathbb{R}^3$ definida por:
$$T(x_1, x_2, x_3, x_4) = (x_1 + x_2 - x_3, 2x_1 + x_2 + x_4, x_1 - x_3 + x_4)$$

---

**Paso 1: Plantear $T(\mathbf{v}) = \mathbf{0}$**

$$\begin{cases}
x_1 + x_2 - x_3 = 0 \\
2x_1 + x_2 + x_4 = 0 \\
x_1 - x_3 + x_4 = 0
\end{cases}$$

---

**Paso 2: Formar [matriz](../../../glossary.md#matriz) aumentada**

$$\left(\begin{array}{cccc|c}
1 & 1 & -1 & 0 & 0 \\
2 & 1 & 0 & 1 & 0 \\
1 & 0 & -1 & 1 & 0
\end{array}\right)$$

---

**Paso 3: Reducir a RREF**

$R_2 \leftarrow R_2 - 2R_1$:
$$\left(\begin{array}{cccc|c}
1 & 1 & -1 & 0 & 0 \\
0 & -1 & 2 & 1 & 0 \\
1 & 0 & -1 & 1 & 0
\end{array}\right)$$

$R_3 \leftarrow R_3 - R_1$:
$$\left(\begin{array}{cccc|c}
1 & 1 & -1 & 0 & 0 \\
0 & -1 & 2 & 1 & 0 \\
0 & -1 & 0 & 1 & 0
\end{array}\right)$$

$R_3 \leftarrow R_3 - R_2$:
$$\left(\begin{array}{cccc|c}
1 & 1 & -1 & 0 & 0 \\
0 & -1 & 2 & 1 & 0 \\
0 & 0 & -2 & 0 & 0
\end{array}\right)$$

$R_3 \leftarrow -\frac{1}{2}R_3$, $R_2 \leftarrow -R_2$:
$$\left(\begin{array}{cccc|c}
1 & 1 & -1 & 0 & 0 \\
0 & 1 & -2 & -1 & 0 \\
0 & 0 & 1 & 0 & 0
\end{array}\right)$$

$R_2 \leftarrow R_2 + 2R_3$, $R_1 \leftarrow R_1 + R_3$:
$$\left(\begin{array}{cccc|c}
1 & 1 & 0 & 0 & 0 \\
0 & 1 & 0 & -1 & 0 \\
0 & 0 & 1 & 0 & 0
\end{array}\right)$$

$R_1 \leftarrow R_1 - R_2$:
$$\left(\begin{array}{cccc|c}
1 & 0 & 0 & 1 & 0 \\
0 & 1 & 0 & -1 & 0 \\
0 & 0 & 1 & 0 & 0
\end{array}\right)$$

---

**Paso 4: Identificar variables**

- Variables ligadas: $x_1, x_2, x_3$
- Variable libre: $x_4 = t$

**Expresar solución:**
- $x_1 = -t$
- $x_2 = t$
- $x_3 = 0$
- $x_4 = t$

$$\mathbf{v} = \begin{pmatrix} -t \\ t \\ 0 \\ t \end{pmatrix} = t\begin{pmatrix} -1 \\ 1 \\ 0 \\ 1 \end{pmatrix}$$

---

**Paso 5: Conclusión**

$$\boxed{\ker(T) = \text{span}\left\{\begin{pmatrix} -1 \\ 1 \\ 0 \\ 1 \end{pmatrix}\right\}}$$

**Base de $\ker(T)$:** $\{(-1, 1, 0, 1)\}$

**Nulidad:** $\text{nul}(T) = \dim(\ker(T)) = 1$

---

**Verificación:**
$$T(-1, 1, 0, 1) = (-1 + 1 - 0, 2(-1) + 1 + 1, -1 - 0 + 1) = (0, 0, 0) \checkmark$$

---

## Método 3: Encontrar la Imagen de una Transformación

**Cuándo Usar:** Para hallar el conjunto de todos los vectores que son imagen de algún vector del [dominio](../../../glossary.md#dominio).

**Definición:** $\text{Im}(T) = \{T(\mathbf{v}) : \mathbf{v} \in V\} = \{w \in W : \exists v \in V, T(v) = w\}$

**Propiedades:**
- $\text{Im}(T)$ es [subespacio](../../../glossary.md#subespacio) de $W$
- $\dim(\text{Im}(T)) =$ rango de $T$
- $T$ sobreyectiva $\Leftrightarrow \text{Im}(T) = W$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar base del [dominio](../../../glossary.md#dominio) | Generalmente la base estándar |
| 2 | Calcular imágenes | Aplicar $T$ a cada vector base |
| 3 | Formar matriz | Imágenes como columnas |
| 4 | Reducir a REF | Para identificar pivotes |
| 5 | Seleccionar base | Imágenes originales correspondientes a pivotes |

### Ejemplo Detallado

**Problema:** Encontrar $\text{Im}(T)$ y su base para $T: \mathbb{R}^3 \to \mathbb{R}^3$ definida por:
$$T(x, y, z) = (x + y, x + y + z, 2x + 2y + z)$$

---

**Paso 1: Calcular $T$ sobre la base estándar**

$$T(\mathbf{e}_1) = T(1, 0, 0) = (1, 1, 2)$$
$$T(\mathbf{e}_2) = T(0, 1, 0) = (1, 1, 2)$$
$$T(\mathbf{e}_3) = T(0, 0, 1) = (0, 1, 1)$$

---

**Paso 2: Formar matriz con imágenes como columnas**

$$A = \begin{pmatrix}
1 & 1 & 0 \\
1 & 1 & 1 \\
2 & 2 & 1
\end{pmatrix}$$

---

**Paso 3: Reducir a forma escalonada**

$R_2 \leftarrow R_2 - R_1$, $R_3 \leftarrow R_3 - 2R_1$:
$$\begin{pmatrix}
1 & 1 & 0 \\
0 & 0 & 1 \\
0 & 0 & 1
\end{pmatrix}$$

$R_3 \leftarrow R_3 - R_2$:
$$\begin{pmatrix}
1 & 1 & 0 \\
0 & 0 & 1 \\
0 & 0 & 0
\end{pmatrix}$$

---

**Paso 4: Identificar columnas pivote**

- Pivote en columna 1 → corresponde a $T(\mathbf{e}_1) = (1, 1, 2)$
- Pivote en columna 3 → corresponde a $T(\mathbf{e}_3) = (0, 1, 1)$
- Columna 2 no tiene pivote → $T(\mathbf{e}_2)$ es redundante

---

**Paso 5: Conclusión**

$$\boxed{\text{Im}(T) = \text{span}\{(1, 1, 2), (0, 1, 1)\}}$$

**Base de $\text{Im}(T)$:** $\{(1, 1, 2), (0, 1, 1)\}$

**Rango:** $\text{rango}(T) = \dim(\text{Im}(T)) = 2$

---

**Verificación del Teorema Rango-Nulidad:**

$$\text{rango}(T) + \text{nul}(T) = \dim(V)$$

Calculamos $\ker(T)$: $(x+y, x+y+z, 2x+2y+z) = (0,0,0)$
- $x + y = 0 \Rightarrow y = -x$
- $x + y + z = 0 \Rightarrow z = 0$

$\ker(T) = \{(t, -t, 0) : t \in \mathbb{R}\}$, así que $\text{nul}(T) = 1$

$$2 + 1 = 3 = \dim(\mathbb{R}^3) \checkmark$$

---

## Método 4: Construir la Matriz de una Transformación

**Cuándo Usar:** Para representar $T: V \to W$ como una matriz respecto a bases dadas.

**Fórmula:** Si $\mathcal{B} = \{\mathbf{v}_1, \ldots, \mathbf{v}_n\}$ es base de $V$ y $\mathcal{C}$ es base de $W$:
$$[T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix} | & | & & | \\ [T(\mathbf{v}_1)]_{\mathcal{C}} & [T(\mathbf{v}_2)]_{\mathcal{C}} & \cdots & [T(\mathbf{v}_n)]_{\mathcal{C}} \\ | & | & & | \end{pmatrix}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar bases | $\mathcal{B}$ del dominio, $\mathcal{C}$ del [codominio](../../../glossary.md#codominio) |
| 2 | Calcular imágenes | $T(\mathbf{v}_i)$ para cada $\mathbf{v}_i \in \mathcal{B}$ |
| 3 | Expresar en base $\mathcal{C}$ | Escribir $T(\mathbf{v}_i)$ como combinación de vectores de $\mathcal{C}$ |
| 4 | Formar columnas | Coeficientes como columnas de la matriz |

### Ejemplo 1: Bases Estándar

**Problema:** Encontrar $[T]$ para $T: \mathbb{R}^2 \to \mathbb{R}^3$ donde $T(x, y) = (x + 2y, 3x - y, x)$.

---

**Paso 1: Base estándar de $\mathbb{R}^2$:** $\{\mathbf{e}_1 = (1,0), \mathbf{e}_2 = (0,1)\}$

---

**Paso 2: Calcular imágenes**

$$T(\mathbf{e}_1) = T(1, 0) = (1 + 0, 3 - 0, 1) = (1, 3, 1)$$
$$T(\mathbf{e}_2) = T(0, 1) = (0 + 2, 0 - 1, 0) = (2, -1, 0)$$

---

**Paso 3: En base estándar de $\mathbb{R}^3$, las coordenadas son las mismas**

$$[T(\mathbf{e}_1)]_{\mathcal{E}} = \begin{pmatrix} 1 \\ 3 \\ 1 \end{pmatrix}, \quad [T(\mathbf{e}_2)]_{\mathcal{E}} = \begin{pmatrix} 2 \\ -1 \\ 0 \end{pmatrix}$$

---

**Paso 4: Formar matriz**

$$\boxed{[T] = \begin{pmatrix} 1 & 2 \\ 3 & -1 \\ 1 & 0 \end{pmatrix}}$$

---

**Verificación:** $T(2, 3) = (2 + 6, 6 - 3, 2) = (8, 3, 2)$

$$[T] \begin{pmatrix} 2 \\ 3 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 3 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 2 \\ 3 \end{pmatrix} = \begin{pmatrix} 2 + 6 \\ 6 - 3 \\ 2 + 0 \end{pmatrix} = \begin{pmatrix} 8 \\ 3 \\ 2 \end{pmatrix} \checkmark$$

---

### Ejemplo 2: Bases No Estándar

**Problema:** Encontrar $[T]_{\mathcal{B}}^{\mathcal{B}}$ para $T: \mathbb{R}^2 \to \mathbb{R}^2$ donde $T(x, y) = (x + y, 2x)$ con base:
$$\mathcal{B} = \{\mathbf{v}_1 = (1, 1), \mathbf{v}_2 = (1, 0)\}$$

---

**Paso 1: Calcular $T(\mathbf{v}_1)$**

$$T(1, 1) = (1 + 1, 2 \cdot 1) = (2, 2)$$

Expresar $(2, 2)$ en base $\mathcal{B}$:
$$a(1, 1) + b(1, 0) = (2, 2)$$
$$\begin{cases} a + b = 2 \\ a = 2 \end{cases} \Rightarrow a = 2, b = 0$$

$$[T(\mathbf{v}_1)]_{\mathcal{B}} = \begin{pmatrix} 2 \\ 0 \end{pmatrix}$$

---

**Paso 2: Calcular $T(\mathbf{v}_2)$**

$$T(1, 0) = (1 + 0, 2 \cdot 1) = (1, 2)$$

Expresar $(1, 2)$ en base $\mathcal{B}$:
$$a(1, 1) + b(1, 0) = (1, 2)$$
$$\begin{cases} a + b = 1 \\ a = 2 \end{cases} \Rightarrow a = 2, b = -1$$

$$[T(\mathbf{v}_2)]_{\mathcal{B}} = \begin{pmatrix} 2 \\ -1 \end{pmatrix}$$

---

**Paso 3: Formar matriz**

$$\boxed{[T]_{\mathcal{B}}^{\mathcal{B}} = \begin{pmatrix} 2 & 2 \\ 0 & -1 \end{pmatrix}}$$

---

## Método 5: Usar la Matriz para Calcular Imágenes

**Cuándo Usar:** Para calcular $T(\mathbf{v})$ eficientemente usando la representación matricial.

**Fórmula:** 
$$[T(\mathbf{v})]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} \cdot [\mathbf{v}]_{\mathcal{B}}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Obtener coordenadas | Escribir $[\mathbf{v}]_{\mathcal{B}}$ |
| 2 | Multiplicar | $[T]_{\mathcal{B}}^{\mathcal{C}} \cdot [\mathbf{v}]_{\mathcal{B}}$ |
| 3 | Interpretar | El resultado son coordenadas en base $\mathcal{C}$ |
| 4 | Reconstruir (si [necesario](../../../glossary.md#necesario)) | Convertir a forma estándar |

### Ejemplo Detallado

**Problema:** Dada $[T]_{\mathcal{B}}^{\mathcal{C}}$ donde $\mathcal{B} = \{(1, 1), (1, -1)\}$ y $\mathcal{C}$ es la base estándar:

$$[T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix} 3 & 1 \\ 2 & -1 \end{pmatrix}$$

Calcular $T(4, 2)$.

---

**Paso 1: Expresar $(4, 2)$ en base $\mathcal{B}$**

$$a(1, 1) + b(1, -1) = (4, 2)$$

Sistema:
$$\begin{cases} a + b = 4 \\ a - b = 2 \end{cases}$$

Sumando: $2a = 6 \Rightarrow a = 3$
Restando: $2b = 2 \Rightarrow b = 1$

$$[(4, 2)]_{\mathcal{B}} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}$$

---

**Paso 2: Multiplicar**

$$[T(4, 2)]_{\mathcal{C}} = \begin{pmatrix} 3 & 1 \\ 2 & -1 \end{pmatrix} \begin{pmatrix} 3 \\ 1 \end{pmatrix} = \begin{pmatrix} 9 + 1 \\ 6 - 1 \end{pmatrix} = \begin{pmatrix} 10 \\ 5 \end{pmatrix}$$

---

**Paso 3: Interpretar**

Como $\mathcal{C}$ es la base estándar, las coordenadas son el vector mismo.

$$\boxed{T(4, 2) = (10, 5)}$$

---

## Método 6: Encontrar la Matriz de Composición

**Cuándo Usar:** Para encontrar la matriz que representa la [composición](../../../glossary.md#composicion) $S \circ T$.

**Fórmula:** 
$$[S \circ T]_{\mathcal{B}}^{\mathcal{D}} = [S]_{\mathcal{C}}^{\mathcal{D}} \cdot [T]_{\mathcal{B}}^{\mathcal{C}}$$

**Nota:** El [orden](../../../glossary.md#orden) de multiplicación es inverso al orden de aplicación.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar espacios | $T: U \to V$, $S: V \to W$ |
| 2 | Calcular $[T]$ | Matriz de $T$ |
| 3 | Calcular $[S]$ | Matriz de $S$ |
| 4 | Multiplicar | $[S \circ T] = [S] \cdot [T]$ |
| 5 | Verificar dimensiones | $(m \times p)(p \times n) = m \times n$ |

### Ejemplo Detallado

**Problema:** Sean $T: \mathbb{R}^3 \to \mathbb{R}^2$ y $S: \mathbb{R}^2 \to \mathbb{R}^2$ definidas por:
$$T(x, y, z) = (x + y, y + z), \quad S(u, v) = (2u - v, 3v)$$

Encontrar $[S \circ T]$ y la fórmula de $(S \circ T)(x, y, z)$.

---

**Paso 1: Calcular $[T]$**

$$T(1, 0, 0) = (1, 0), \quad T(0, 1, 0) = (1, 1), \quad T(0, 0, 1) = (0, 1)$$

$$[T] = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$

---

**Paso 2: Calcular $[S]$**

$$S(1, 0) = (2, 0), \quad S(0, 1) = (-1, 3)$$

$$[S] = \begin{pmatrix} 2 & -1 \\ 0 & 3 \end{pmatrix}$$

---

**Paso 3: Calcular $[S \circ T] = [S][T]$**

$$[S \circ T] = \begin{pmatrix} 2 & -1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$

$$= \begin{pmatrix} 2(1) + (-1)(0) & 2(1) + (-1)(1) & 2(0) + (-1)(1) \\ 0(1) + 3(0) & 0(1) + 3(1) & 0(0) + 3(1) \end{pmatrix}$$

$$= \begin{pmatrix} 2 & 1 & -1 \\ 0 & 3 & 3 \end{pmatrix}$$

---

**Paso 4: Fórmula de $S \circ T$**

$$\boxed{(S \circ T)(x, y, z) = (2x + y - z, 3y + 3z)}$$

---

**Verificación directa:**

$$T(x, y, z) = (x + y, y + z)$$
$$S(x + y, y + z) = (2(x+y) - (y+z), 3(y+z)) = (2x + y - z, 3y + 3z) \checkmark$$

---

## Método 7: Determinar si T es Inyectiva/Sobreyectiva

**Cuándo Usar:** Para clasificar las propiedades de una transformación lineal.

**Definiciones:**
- **Inyectiva (uno a uno):** $T(\mathbf{u}) = T(\mathbf{v}) \Rightarrow \mathbf{u} = \mathbf{v}$
- **Sobreyectiva (sobre):** Para todo $\mathbf{w} \in W$, existe $\mathbf{v} \in V$ [tal que](../../../glossary.md#tal-que) $T(\mathbf{v}) = \mathbf{w}$
- **Biyectiva ([isomorfismo](../../../glossary.md#isomorfismo)):** Inyectiva y sobreyectiva

### Criterios Algebraicos

| Propiedad | Condición Equivalente |
|-----------|----------------------|
| Inyectiva | $\ker(T) = \{\mathbf{0}\}$ |
| Inyectiva | $\text{nul}(T) = 0$ |
| Inyectiva | $\text{rango}([T]) = \dim(V)$ |
| Sobreyectiva | $\text{Im}(T) = W$ |
| Sobreyectiva | $\text{rango}(T) = \dim(W)$ |
| Biyectiva | $\dim(V) = \dim(W)$ y cualquiera de las anteriores |

### Ejemplo Detallado

**Problema:** Clasificar $T: \mathbb{R}^3 \to \mathbb{R}^3$ definida por:
$$T(x, y, z) = (x + y, y + z, x + z)$$

---

**Paso 1: Construir la matriz**

$$[T] = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$$

---

**Paso 2: Calcular el rango (reducir a REF)**

$R_3 \leftarrow R_3 - R_1$:
$$\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & -1 & 1 \end{pmatrix}$$

$R_3 \leftarrow R_3 + R_2$:
$$\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix}$$

**Rango = 3** (tres pivotes)

---

**Paso 3: Analizar**

- $\text{rango}(T) = 3 = \dim(\mathbb{R}^3)$ → **Sobreyectiva** ✓
- $\text{nul}(T) = 3 - 3 = 0$ → **Inyectiva** ✓

---

**Conclusión:**

$$\boxed{T \text{ es un [isomorfismo](../../../glossary.md#isomorfismo) (biyectiva)}}$$

---

**Encontrar $T^{-1}$:**

Como $T$ es biyectiva, $T^{-1}$ existe y $[T^{-1}] = [T]^{-1}$.

Calculamos $[T]^{-1}$ por Gauss-Jordan:

$$\left(\begin{array}{ccc|ccc}
1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 & 0 & 1
\end{array}\right) \rightarrow \cdots \rightarrow \left(\begin{array}{ccc|ccc}
1 & 0 & 0 & 1/2 & -1/2 & 1/2 \\
0 & 1 & 0 & 1/2 & 1/2 & -1/2 \\
0 & 0 & 1 & -1/2 & 1/2 & 1/2
\end{array}\right)$$

$$[T^{-1}] = \frac{1}{2}\begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix}$$

$$\boxed{T^{-1}(x, y, z) = \frac{1}{2}(x - y + z, x + y - z, -x + y + z)}$$

---

## Método 8: Cambiar la Matriz a una Nueva Base

**Cuándo Usar:** Para encontrar la representación matricial de $T$ en una base diferente.

**Fórmula:** Si $T: V \to V$ (endomorfismo) y cambiamos de base $\mathcal{B}$ a $\mathcal{B}'$:
$$[T]_{\mathcal{B}'} = P^{-1} [T]_{\mathcal{B}} P$$

donde $P = P_{\mathcal{B}' \to \mathcal{B}}$ es la matriz de cambio de base.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Formar $P$ | Columnas = vectores de $\mathcal{B}'$ expresados en $\mathcal{B}$ |
| 2 | Calcular $P^{-1}$ | Por Gauss-Jordan o fórmula 2×2 |
| 3 | Multiplicar | $P^{-1} [T]_{\mathcal{B}} P$ |
| 4 | Simplificar | Reducir la expresión final |

### Ejemplo Detallado

**Problema:** Dada $T: \mathbb{R}^2 \to \mathbb{R}^2$ con $[T]_{\mathcal{E}} = \begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix}$ (base estándar), encontrar $[T]_{\mathcal{B}}$ donde:
$$\mathcal{B} = \{(1, 1), (1, -1)\}$$

---

**Paso 1: Formar matriz $P$**

Los vectores de $\mathcal{B}$ expresados en la base estándar son ellos mismos:

$$P = P_{\mathcal{B} \to \mathcal{E}} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

---

**Paso 2: Calcular $P^{-1}$**

Para matriz 2×2: $P^{-1} = \frac{1}{\det(P)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$

$$\det(P) = (1)(-1) - (1)(1) = -2$$

$$P^{-1} = \frac{1}{-2} \begin{pmatrix} -1 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 1/2 & 1/2 \\ 1/2 & -1/2 \end{pmatrix}$$

---

**Paso 3: Calcular $[T]_{\mathcal{B}} = P^{-1} [T]_{\mathcal{E}} P$**

Primero $[T]_{\mathcal{E}} P$:
$$\begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \begin{pmatrix} 4+2 & 4-2 \\ 1+3 & 1-3 \end{pmatrix} = \begin{pmatrix} 6 & 2 \\ 4 & -2 \end{pmatrix}$$

Luego $P^{-1}([T]_{\mathcal{E}} P)$:
$$\begin{pmatrix} 1/2 & 1/2 \\ 1/2 & -1/2 \end{pmatrix} \begin{pmatrix} 6 & 2 \\ 4 & -2 \end{pmatrix} = \begin{pmatrix} 3+2 & 1-1 \\ 3-2 & 1+1 \end{pmatrix} = \begin{pmatrix} 5 & 0 \\ 1 & 2 \end{pmatrix}$$

---

**Conclusión:**

$$\boxed{[T]_{\mathcal{B}} = \begin{pmatrix} 5 & 0 \\ 1 & 2 \end{pmatrix}}$$

---

**Verificación:** Los eigenvalores deben ser iguales.

$\det([T]_{\mathcal{E}} - \lambda I) = (4-\lambda)(3-\lambda) - 2 = \lambda^2 - 7\lambda + 10 = (\lambda - 5)(\lambda - 2)$

$\det([T]_{\mathcal{B}} - \lambda I) = (5-\lambda)(2-\lambda) - 0 = \lambda^2 - 7\lambda + 10 = (\lambda - 5)(\lambda - 2)$

Eigenvalores: $\lambda_1 = 5$, $\lambda_2 = 2$ ✓

---

## Método 9: Verificar si T es Isomorfismo

**Cuándo Usar:** Para determinar si dos [espacios vectoriales](../../../glossary.md#espacios-vectoriales) son estructuralmente idénticos.

**Definición:** $T: V \to W$ es isomorfismo si es:
1. Transformación lineal
2. Biyectiva (inyectiva y sobreyectiva)

**Consecuencia:** Si existe isomorfismo entre $V$ y $W$, entonces $\dim(V) = \dim(W)$.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar [linealidad](../../../glossary.md#linealidad) | $T(\mathbf{u}+\mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$, $T(c\mathbf{v}) = cT(\mathbf{v})$ |
| 2 | Construir matriz | $[T]$ respecto a bases elegidas |
| 3 | Calcular [determinante](../../../glossary.md#determinante) | Si bases son iguales en [dimensión](../../../glossary.md#dimension) |
| 4 | Analizar | $\det([T]) \neq 0 \Leftrightarrow$ isomorfismo |

### Ejemplo Detallado

**Problema:** ¿Es $T: P_2 \to \mathbb{R}^3$ definida por $T(a + bx + cx^2) = (a, a+b, a+b+c)$ un isomorfismo?

---

**Paso 1: Verificar [linealidad](../../../glossary.md#linealidad)**

Sean $p(x) = a_1 + b_1x + c_1x^2$ y $q(x) = a_2 + b_2x + c_2x^2$.

$$T(p + q) = T((a_1+a_2) + (b_1+b_2)x + (c_1+c_2)x^2)$$
$$= (a_1+a_2, (a_1+a_2)+(b_1+b_2), (a_1+a_2)+(b_1+b_2)+(c_1+c_2))$$

$$T(p) + T(q) = (a_1, a_1+b_1, a_1+b_1+c_1) + (a_2, a_2+b_2, a_2+b_2+c_2)$$
$$= (a_1+a_2, a_1+a_2+b_1+b_2, a_1+a_2+b_1+b_2+c_1+c_2)$$

Coinciden ✓ (homogeneidad similar)

---

**Paso 2: Construir matriz**

Base de $P_2$: $\{1, x, x^2\}$

$$T(1) = (1, 1, 1), \quad T(x) = (0, 1, 1), \quad T(x^2) = (0, 0, 1)$$

$$[T] = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix}$$

---

**Paso 3: Calcular [determinante](../../../glossary.md#determinante)**

$$\det([T]) = 1 \cdot \det\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = 1 \cdot (1 - 0) = 1 \neq 0$$

---

**Conclusión:**

$$\boxed{T \text{ es un isomorfismo, } P_2 \cong \mathbb{R}^3}$$

---

## Método 10: Encontrar la Transformación Inversa

**Cuándo Usar:** Cuando $T$ es isomorfismo y necesitamos encontrar $T^{-1}$.

**Fórmula:** $[T^{-1}] = [T]^{-1}$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar invertibilidad | $\det([T]) \neq 0$ |
| 2 | Calcular $[T]^{-1}$ | Por Gauss-Jordan |
| 3 | Escribir fórmula | Interpretar columnas como imágenes |

### Ejemplo Detallado

**Problema:** Encontrar $T^{-1}$ para $T: \mathbb{R}^2 \to \mathbb{R}^2$ donde $T(x, y) = (2x + y, x + y)$.

---

**Paso 1: Verificar invertibilidad**

$$[T] = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \quad \det([T]) = 2 - 1 = 1 \neq 0 \checkmark$$

---

**Paso 2: Calcular $[T]^{-1}$**

$$[T]^{-1} = \frac{1}{1} \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$$

---

**Paso 3: Escribir fórmula de $T^{-1}$**

$$T^{-1}(u, v) = (1 \cdot u + (-1) \cdot v, (-1) \cdot u + 2 \cdot v) = (u - v, -u + 2v)$$

$$\boxed{T^{-1}(u, v) = (u - v, 2v - u)}$$

---

**Verificación:**

$$T \circ T^{-1}(u, v) = T(u - v, 2v - u)$$
$$= (2(u-v) + (2v-u), (u-v) + (2v-u))$$
$$= (2u - 2v + 2v - u, u - v + 2v - u) = (u, v) \checkmark$$

---

## Método 11: Teorema Rango-Nulidad para Transformaciones

**Cuándo Usar:** Para relacionar dimensiones del núcleo e imagen con la [dimensión](../../../glossary.md#dimension) del dominio.

**Teorema:** Para $T: V \to W$ lineal:
$$\dim(\ker(T)) + \dim(\text{Im}(T)) = \dim(V)$$
$$\text{nul}(T) + \text{rango}(T) = \dim(V)$$

### Aplicaciones

| Situación | Consecuencia |
|-----------|--------------|
| $\text{nul}(T) = 0$ | $\text{rango}(T) = \dim(V)$, $T$ inyectiva |
| $\text{rango}(T) = \dim(W)$ | $T$ sobreyectiva |
| $\dim(V) = \dim(W)$ | Inyectiva $\Leftrightarrow$ Sobreyectiva $\Leftrightarrow$ Isomorfismo |
| $\dim(V) > \dim(W)$ | $T$ nunca puede ser inyectiva |
| $\dim(V) < \dim(W)$ | $T$ nunca puede ser sobreyectiva |

### Ejemplo Detallado

**Problema:** Sea $T: \mathbb{R}^4 \to \mathbb{R}^3$ con $\text{rango}(T) = 2$. ¿Puede $T$ ser inyectiva? ¿Sobreyectiva?

---

**Por Rango-Nulidad:**

$$\text{nul}(T) = \dim(\mathbb{R}^4) - \text{rango}(T) = 4 - 2 = 2$$

---

**Análisis de inyectividad:**

$\text{nul}(T) = 2 \neq 0$, por lo tanto $\ker(T) \neq \{\mathbf{0}\}$.

$$\boxed{T \text{ NO es inyectiva}}$$

---

**Análisis de sobreyectividad:**

$\text{rango}(T) = 2 \neq 3 = \dim(\mathbb{R}^3)$, por lo tanto $\text{Im}(T) \neq \mathbb{R}^3$.

$$\boxed{T \text{ NO es sobreyectiva}}$$

---

## Resumen de Fórmulas

| Concepto | Fórmula/Criterio |
|----------|------------------|
| Linealidad | $T(\alpha\mathbf{u} + \beta\mathbf{v}) = \alpha T(\mathbf{u}) + \beta T(\mathbf{v})$ |
| Núcleo | $\ker(T) = \{\mathbf{v} : T(\mathbf{v}) = \mathbf{0}\}$ |
| Imagen | $\text{Im}(T) = \{T(\mathbf{v}) : \mathbf{v} \in V\}$ |
| Matriz de $T$ | Columnas = $[T(\mathbf{v}_i)]_{\mathcal{C}}$ |
| [Composición](../../../glossary.md#composicion) | $[S \circ T] = [S][T]$ |
| Cambio de base | $[T]_{\mathcal{B}'} = P^{-1}[T]_{\mathcal{B}}P$ |
| Rango-Nulidad | $\text{nul}(T) + \text{rango}(T) = \dim(V)$ |
| Inyectiva | $\ker(T) = \{\mathbf{0}\}$ |
| Sobreyectiva | $\text{Im}(T) = W$ |
| Isomorfismo | Lineal + Biyectiva |
| Inversa | $[T^{-1}] = [T]^{-1}$ |

---

## Errores Comunes

| Error | Corrección |
|-------|------------|
| Confundir $[S \circ T]$ con $[T][S]$ | El [orden](../../../glossary.md#orden) es $[S][T]$ (primero $T$, luego $S$) |
| Olvidar verificar $T(\mathbf{0}) = \mathbf{0}$ | Siempre es el primer paso para verificar linealidad |
| Usar columnas reducidas para base de Im | Usar columnas **originales** correspondientes a pivotes |
| Confundir $P$ con $P^{-1}$ | $P_{\mathcal{B}' \to \mathcal{B}}$ lleva coordenadas de $\mathcal{B}'$ a $\mathcal{B}$ |
| Asumir que $\dim(V) = \dim(W)$ implica isomorfismo | Falta verificar que $T$ sea biyectiva |
| Confundir rango de $T$ con rango de $[T]$ | Son iguales: $\text{rango}(T) = \text{rango}([T])$ |
