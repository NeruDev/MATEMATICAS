<!--
content_type: methods
topic: Transformaciones Lineales
---
-->

# Métodos: Transformaciones Lineales

---

## Método 1: Verificar si una Función es Transformación Lineal

**Objetivo:** Determinar si $T: V \to W$ es lineal.

### Pasos

1. **Verificar $T(\mathbf{0}) = \mathbf{0}$** (si falla, no es lineal)
2. **Verificar aditividad:** $T(u + v) = T(u) + T(v)$
3. **Verificar homogeneidad:** $T(cv) = cT(v)$

### Ejemplo

¿Es $T: \mathbb{R}^2 \to \mathbb{R}^2$, $T(x, y) = (2x - y, x + 3y)$ lineal?

**Paso 1:** $T(0, 0) = (0, 0)$ ✓

**Paso 2:** Sean $u = (x_1, y_1)$, $v = (x_2, y_2)$
- $T(u + v) = T(x_1 + x_2, y_1 + y_2) = (2(x_1+x_2) - (y_1+y_2), (x_1+x_2) + 3(y_1+y_2))$
- $T(u) + T(v) = (2x_1 - y_1, x_1 + 3y_1) + (2x_2 - y_2, x_2 + 3y_2)$
- Coinciden ✓

**Paso 3:** $T(cv) = T(cx, cy) = (2cx - cy, cx + 3cy) = c(2x - y, x + 3y) = cT(v)$ ✓

**Conclusión:** $T$ es lineal.

---

## Método 2: Encontrar el Núcleo de una Transformación

**Objetivo:** Hallar $\ker(T)$ y su base.

### Pasos

1. Plantear $T(v) = \mathbf{0}$
2. Resolver el sistema de ecuaciones resultante
3. Expresar la solución en forma paramétrica
4. Los vectores parámetro forman base de $\ker(T)$

### Ejemplo

$T: \mathbb{R}^3 \to \mathbb{R}^2$, $T(x, y, z) = (x + y, y + z)$

Resolver $T(x, y, z) = (0, 0)$:
$$\begin{cases} x + y = 0 \\ y + z = 0 \end{cases}$$

De ecuación 1: $x = -y$
De ecuación 2: $z = -y$

Sea $y = t$: $(x, y, z) = (-t, t, -t) = t(-1, 1, -1)$

**Base de $\ker(T)$:** $\{(-1, 1, -1)\}$

**$\text{nul}(T) = 1$**

---

## Método 3: Encontrar la Imagen de una Transformación

**Objetivo:** Hallar $\text{Im}(T)$ y su base.

### Pasos

1. Aplicar $T$ a los vectores de una base de $V$
2. Formar la matriz con estos vectores como columnas
3. Reducir a forma escalonada
4. Los vectores originales correspondientes a pivotes forman base de $\text{Im}(T)$

### Ejemplo

$T: \mathbb{R}^3 \to \mathbb{R}^2$, $T(x, y, z) = (x + y, 2x + 2y)$

Base estándar de $\mathbb{R}^3$:
- $T(1, 0, 0) = (1, 2)$
- $T(0, 1, 0) = (1, 2)$
- $T(0, 0, 1) = (0, 0)$

Matriz: $\begin{pmatrix} 1 & 1 & 0 \\ 2 & 2 & 0 \end{pmatrix} \to \begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}$

Pivote en columna 1.

**Base de $\text{Im}(T)$:** $\{(1, 2)\}$

**$\text{rango}(T) = 1$**

---

## Método 4: Construir la Matriz de una Transformación

**Objetivo:** Hallar $[T]_{\mathcal{B}}^{\mathcal{C}}$.

### Pasos

1. Aplicar $T$ a cada vector de la base $\mathcal{B}$ de $V$
2. Expresar cada $T(v_i)$ como combinación lineal de la base $\mathcal{C}$ de $W$
3. Los coeficientes forman las columnas de la matriz

### Ejemplo (Bases Estándar)

$T: \mathbb{R}^2 \to \mathbb{R}^3$, $T(x, y) = (x + y, 2x, y)$

- $T(e_1) = T(1, 0) = (1, 2, 0)$
- $T(e_2) = T(0, 1) = (1, 0, 1)$

$$[T] = \begin{pmatrix} 1 & 1 \\ 2 & 0 \\ 0 & 1 \end{pmatrix}$$

### Ejemplo (Bases No Estándar)

$T: \mathbb{R}^2 \to \mathbb{R}^2$, $T(x, y) = (x + y, x - y)$

$\mathcal{B} = \{(1, 1), (1, -1)\}$

- $T(1, 1) = (2, 0) = 1(1, 1) + 1(1, -1)$
- $T(1, -1) = (0, 2) = 1(1, 1) + (-1)(1, -1)$

$$[T]_{\mathcal{B}}^{\mathcal{B}} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

---

## Método 5: Usar la Matriz para Calcular Imágenes

**Objetivo:** Dado $[T]$ y un vector $v$, calcular $T(v)$.

### Pasos

1. Expresar $v$ en la base del dominio: $[v]_{\mathcal{B}}$
2. Multiplicar: $[T(v)]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} \cdot [v]_{\mathcal{B}}$
3. Reconstruir $T(v)$ en $W$

### Ejemplo

$[T] = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$ (bases estándar), $v = (3, 2)$

$$T(v) = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 3 \\ 2 \end{pmatrix} = \begin{pmatrix} 8 \\ 9 \end{pmatrix}$$

**$T(3, 2) = (8, 9)$**

---

## Método 6: Encontrar la Matriz de Composición

**Objetivo:** Hallar $[S \circ T]$.

### Pasos

1. Calcular $[T]_{\mathcal{B}}^{\mathcal{C}}$ (matriz de $T$)
2. Calcular $[S]_{\mathcal{C}}^{\mathcal{D}}$ (matriz de $S$)
3. Multiplicar: $[S \circ T]_{\mathcal{B}}^{\mathcal{D}} = [S]_{\mathcal{C}}^{\mathcal{D}} \cdot [T]_{\mathcal{B}}^{\mathcal{C}}$

### Ejemplo

$T(x, y) = (x + y, x - y)$, $S(u, v) = (2u, u + v)$

$$[T] = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \quad [S] = \begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix}$$

$$[S \circ T] = \begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \begin{pmatrix} 2 & 2 \\ 2 & 0 \end{pmatrix}$$

---

## Método 7: Determinar si T es Inyectiva/Sobreyectiva

**Objetivo:** Clasificar propiedades de $T$.

### Pasos para Inyectividad

1. Calcular $\ker(T)$
2. $T$ es inyectiva $\Leftrightarrow \ker(T) = \{\mathbf{0}\}$

**Equivalente:** Calcular $[T]$ y verificar que $\text{rango}([T]) = \dim(V)$

### Pasos para Sobreyectividad

1. Calcular $\text{Im}(T)$
2. $T$ es sobreyectiva $\Leftrightarrow \text{Im}(T) = W$

**Equivalente:** Verificar que $\text{rango}([T]) = \dim(W)$

### Ejemplo

$T: \mathbb{R}^3 \to \mathbb{R}^2$, $[T] = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 3 \end{pmatrix}$

RREF: $\begin{pmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$

- $\text{rango}(T) = 2 = \dim(\mathbb{R}^2)$ → **Sobreyectiva** ✓
- $\text{nul}(T) = 3 - 2 = 1 \neq 0$ → **No inyectiva** ✗

---

## Método 8: Cambiar la Matriz a una Nueva Base

**Objetivo:** Dado $[T]_{\mathcal{B}}$, encontrar $[T]_{\mathcal{B}'}$.

### Pasos

1. Calcular la matriz de cambio $P = P_{\mathcal{B}' \to \mathcal{B}}$
2. Calcular $P^{-1}$
3. Aplicar: $[T]_{\mathcal{B}'} = P^{-1} [T]_{\mathcal{B}} P$

### Ejemplo

$[T]_{\mathcal{E}} = \begin{pmatrix} 5 & 3 \\ 3 & 5 \end{pmatrix}$ (base estándar $\mathcal{E}$)

Nueva base $\mathcal{B}' = \{(1, 1), (1, -1)\}$

$P_{\mathcal{B}' \to \mathcal{E}} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$

$P^{-1} = \frac{1}{-2}\begin{pmatrix} -1 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 1/2 & 1/2 \\ 1/2 & -1/2 \end{pmatrix}$

$$[T]_{\mathcal{B}'} = \begin{pmatrix} 1/2 & 1/2 \\ 1/2 & -1/2 \end{pmatrix} \begin{pmatrix} 5 & 3 \\ 3 & 5 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

$$= \begin{pmatrix} 1/2 & 1/2 \\ 1/2 & -1/2 \end{pmatrix} \begin{pmatrix} 8 & 2 \\ 8 & -2 \end{pmatrix} = \begin{pmatrix} 8 & 0 \\ 0 & 2 \end{pmatrix}$$

**$[T]_{\mathcal{B}'} = \begin{pmatrix} 8 & 0 \\ 0 & 2 \end{pmatrix}$** (diagonal!)
