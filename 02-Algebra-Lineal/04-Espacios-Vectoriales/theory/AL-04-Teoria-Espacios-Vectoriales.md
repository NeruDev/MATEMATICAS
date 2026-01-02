<!--
::METADATA::
type: theory
status: active
-->

# Teoría de Espacios Vectoriales

---

## 4.1 Definición de Espacio Vectorial

### Definición Formal

Un **[espacio vectorial](../../../glossary.md#espacio-vectorial)** $V$ sobre un campo $\mathbb{F}$ (usualmente $\mathbb{R}$ o $\mathbb{C}$) es un conjunto no vacío con dos operaciones:

1. **Suma vectorial:** $+: V \times V \to V$
2. **Multiplicación escalar:** $\cdot: \mathbb{F} \times V \to V$

que satisfacen los siguientes **axiomas** para todo $u, v, w \in V$ y $a, b \in \mathbb{F}$:

### Axiomas de la Suma

| Axioma | Nombre | Expresión |
|--------|--------|-----------|
| A1 | Cerradura | $u + v \in V$ |
| A2 | Asociatividad | $(u + v) + w = u + (v + w)$ |
| A3 | Conmutatividad | $u + v = v + u$ |
| A4 | Elemento neutro | $\exists \mathbf{0} \in V : v + \mathbf{0} = v$ |
| A5 | Inverso aditivo | $\exists (-v) \in V : v + (-v) = \mathbf{0}$ |

### Axiomas de la Multiplicación Escalar

| Axioma | Nombre | Expresión |
|--------|--------|-----------|
| M1 | Cerradura | $a \cdot v \in V$ |
| M2 | Asociatividad | $a(bv) = (ab)v$ |
| M3 | Identidad | $1 \cdot v = v$ |
| M4 | Distributividad (escalar) | $a(u + v) = au + av$ |
| M5 | Distributividad ([vector](../../../glossary.md#vector)) | $(a + b)v = av + bv$ |

### Ejemplos Fundamentales

**1. $\mathbb{R}^n$ (Espacio Euclidiano)**
$$\mathbb{R}^n = \{(x_1, x_2, ..., x_n) : x_i \in \mathbb{R}\}$$

Con operaciones componente a componente.

**2. $M_{m \times n}(\mathbb{R})$ (Espacio de Matrices)**

Matrices $m \times n$ con suma y multiplicación escalar usuales.

**3. $P_n(x)$ (Polinomios de grado $\leq n$)**
$$P_n(x) = \{a_0 + a_1x + ... + a_nx^n : a_i \in \mathbb{R}\}$$

**4. $C[a,b]$ (Funciones Continuas)**

Funciones continuas en $[a,b]$ con suma y multiplicación escalar puntuales.

### Propiedades Derivadas

> **Teorema:** En todo espacio vectorial:
> 1. El vector cero $\mathbf{0}$ es único
> 2. El inverso aditivo $-v$ es único para cada $v$
> 3. $0 \cdot v = \mathbf{0}$
> 4. $a \cdot \mathbf{0} = \mathbf{0}$
> 5. $(-1) \cdot v = -v$
> 6. $av = \mathbf{0} \Rightarrow a = 0$ o $v = \mathbf{0}$

---

## 4.2 Subespacios Vectoriales

### Definición

Sea $V$ un espacio vectorial sobre $\mathbb{F}$. Un subconjunto $W \subseteq V$ es **[subespacio](../../../glossary.md#subespacio) vectorial** si $W$ es también un espacio vectorial con las mismas operaciones.

### Criterio del Subespacio (Forma Práctica)

> **Teorema:** $W \subseteq V$ es subespacio si y solo si:
> 1. $\mathbf{0} \in W$ (contiene el vector cero)
> 2. $u, v \in W \Rightarrow u + v \in W$ (cerrado bajo suma)
> 3. $v \in W, c \in \mathbb{F} \Rightarrow cv \in W$ (cerrado bajo multiplicación escalar)

**Equivalentemente:** $W$ es subespacio si $au + bv \in W$ para todo $u, v \in W$ y $a, b \in \mathbb{F}$.

### Ejemplos de Subespacios

**En $\mathbb{R}^3$:**
- Rectas por el origen: $W = \{t\mathbf{v} : t \in \mathbb{R}\}$
- Planos por el origen: $W = \{s\mathbf{u} + t\mathbf{v} : s, t \in \mathbb{R}\}$
- $\{\mathbf{0}\}$ (subespacio [trivial](../../../glossary.md#trivial))
- $\mathbb{R}^3$ mismo

**No son subespacios:**
- Rectas que no pasan por el origen
- El primer cuadrante $\{(x, y) : x \geq 0, y \geq 0\}$

### Subespacios Importantes

**1. Espacio Nulo (Kernel)**
$$\text{Nul}(A) = \{x \in \mathbb{R}^n : Ax = \mathbf{0}\}$$

**2. Espacio Columna**
$$\text{Col}(A) = \text{span}\{\text{columnas de } A\}$$

**3. Espacio Fila**
$$\text{Row}(A) = \text{span}\{\text{filas de } A\}$$

### Intersección y Suma de Subespacios

> **Teorema:** Si $W_1$ y $W_2$ son subespacios de $V$, entonces:
> - $W_1 \cap W_2$ es subespacio
> - $W_1 + W_2 = \{w_1 + w_2 : w_1 \in W_1, w_2 \in W_2\}$ es subespacio

---

## 4.3 Combinaciones Lineales y Generadores

### Combinación Lineal

Una **[combinación lineal](../../../glossary.md#combinación-lineal)** de vectores $v_1, v_2, ..., v_k$ es:
$$c_1v_1 + c_2v_2 + ... + c_kv_k$$
donde $c_i \in \mathbb{F}$ son escalares.

### Espacio Generado (Span)

El **span** de un conjunto de vectores es el conjunto de todas sus combinaciones lineales:

$$\text{span}\{v_1, ..., v_k\} = \{c_1v_1 + ... + c_kv_k : c_i \in \mathbb{F}\}$$

> **Teorema:** $\text{span}\{v_1, ..., v_k\}$ es siempre un subespacio vectorial.

### Ejemplos

**En $\mathbb{R}^3$:**
- $\text{span}\{(1,0,0)\} = $ eje $x$
- $\text{span}\{(1,0,0), (0,1,0)\} = $ plano $xy$
- $\text{span}\{(1,0,0), (2,0,0)\} = $ eje $x$ (vectores colineales)

### Conjunto Generador

Un conjunto $S = \{v_1, ..., v_k\}$ **genera** a $V$ si:
$$V = \text{span}\{v_1, ..., v_k\}$$

Es decir, todo vector de $V$ puede escribirse como combinación lineal de $S$.

---

## 4.4 Independencia Lineal

### Definición

Un conjunto de vectores $\{v_1, v_2, ..., v_k\}$ es **linealmente independiente (LI)** si:
$$c_1v_1 + c_2v_2 + ... + c_kv_k = \mathbf{0} \Rightarrow c_1 = c_2 = ... = c_k = 0$$

Es decir, la única forma de obtener el vector cero es con todos los coeficientes iguales a cero.

### Dependencia Lineal

Un conjunto es **linealmente dependiente (LD)** si NO es linealmente independiente, es decir, existen escalares $c_i$ no todos cero tales que:
$$c_1v_1 + c_2v_2 + ... + c_kv_k = \mathbf{0}$$

### Criterios Prácticos

> **Teorema:** $\{v_1, ..., v_k\}$ es LD si y solo si algún $v_i$ es combinación lineal de los demás.

> **Criterio Matricial:** Los vectores columna de $A$ son LI si y solo si el sistema $Ax = \mathbf{0}$ tiene solo la solución trivial.

### Propiedades

1. El conjunto $\{\mathbf{0}\}$ es siempre LD
2. Un solo vector $\{v\}$ es LI si y solo si $v \neq \mathbf{0}$
3. Si un subconjunto es LD, el conjunto completo es LD
4. Si un conjunto es LI, todo subconjunto es LI
5. En $\mathbb{R}^n$, más de $n$ vectores son siempre LD

### Determinación de Independencia

Para vectores en $\mathbb{R}^n$:
1. Formar la [matriz](../../../glossary.md#matriz) con vectores como columnas
2. Reducir a forma escalonada
3. Son LI si cada columna tiene pivote

---

## 4.5 Bases y Dimensión

### Definición de Base

Una **[base](../../../glossary.md#base)** de un espacio vectorial $V$ es un conjunto $\mathcal{B} = \{v_1, ..., v_n\}$ que:
1. Es **linealmente independiente**
2. **Genera** a $V$

> **Teorema:** Todo vector $v \in V$ se escribe de manera **única** como combinación lineal de una base.

### Bases Estándar

| Espacio | Base Estándar | Notación |
|---------|---------------|----------|
| $\mathbb{R}^2$ | $\{(1,0), (0,1)\}$ | $\{e_1, e_2\}$ |
| $\mathbb{R}^3$ | $\{(1,0,0), (0,1,0), (0,0,1)\}$ | $\{e_1, e_2, e_3\}$ |
| $\mathbb{R}^n$ | $\{e_1, e_2, ..., e_n\}$ | $e_i$ tiene 1 en posición $i$ |
| $P_2(x)$ | $\{1, x, x^2\}$ | Monomios |
| $M_{2\times 2}$ | $\{E_{11}, E_{12}, E_{21}, E_{22}\}$ | $E_{ij}$ tiene 1 en $(i,j)$ |

### Dimensión

> **Teorema de la [Dimensión](../../../glossary.md#dimensión):** Todas las bases de un espacio vectorial finito-dimensional tienen el mismo número de elementos.

La **dimensión** de $V$ es el número de vectores en cualquier base:
$$\dim(V) = n$$

### Ejemplos de Dimensiones

| Espacio | Dimensión |
|---------|-----------|
| $\mathbb{R}^n$ | $n$ |
| $P_n(x)$ | $n + 1$ |
| $M_{m \times n}(\mathbb{R})$ | $mn$ |
| $\{\mathbf{0}\}$ | $0$ |

### Teoremas Fundamentales

> **Teorema 1:** Si $\dim(V) = n$:
> - Todo conjunto LI tiene $\leq n$ vectores
> - Todo conjunto generador tiene $\geq n$ vectores
> - $n$ vectores LI forman base
> - $n$ vectores que generan a $V$ forman base

> **Teorema 2 (Dimensión de Subespacios):** Si $W$ es subespacio de $V$:
> $$\dim(W) \leq \dim(V)$$
> con igualdad si y solo si $W = V$.

### Cómo Encontrar una Base

**Para $\text{span}\{v_1, ..., v_k\}$:**
1. Formar matriz con vectores como filas
2. Reducir a forma escalonada
3. Los vectores correspondientes a filas con pivote forman base

**Para soluciones de $Ax = 0$:**
1. Reducir $A$ a RREF
2. Expresar variables ligadas en términos de libres
3. Los vectores obtenidos al dar valores a variables libres forman base de $\text{Nul}(A)$

---

## 4.6 Coordenadas y Cambio de Base

### Vector de Coordenadas

Sea $\mathcal{B} = \{v_1, v_2, ..., v_n\}$ una base ordenada de $V$.

Si $v = c_1v_1 + c_2v_2 + ... + c_nv_n$, el **vector de coordenadas** de $v$ respecto a $\mathcal{B}$ es:

$$[v]_{\mathcal{B}} = \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{pmatrix}$$

### Ejemplo

En $\mathbb{R}^2$ con $\mathcal{B} = \{(1,1), (1,-1)\}$:

Si $v = (3, 1)$, encontrar $[v]_{\mathcal{B}}$:
$$v = c_1(1,1) + c_2(1,-1) = (c_1 + c_2, c_1 - c_2)$$

Sistema: $c_1 + c_2 = 3$, $c_1 - c_2 = 1$ → $c_1 = 2$, $c_2 = 1$

$$[v]_{\mathcal{B}} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$$

### Matriz de Cambio de Base

Sean $\mathcal{B} = \{v_1, ..., v_n\}$ y $\mathcal{B}' = \{w_1, ..., w_n\}$ dos bases de $V$.

La **matriz de cambio de base** de $\mathcal{B}$ a $\mathcal{B}'$ es:

$$P_{\mathcal{B} \to \mathcal{B}'} = \begin{pmatrix} | & | & & | \\ [v_1]_{\mathcal{B}'} & [v_2]_{\mathcal{B}'} & \cdots & [v_n]_{\mathcal{B}'} \\ | & | & & | \end{pmatrix}$$

### Fórmula de Cambio

$$[v]_{\mathcal{B}'} = P_{\mathcal{B} \to \mathcal{B}'} \cdot [v]_{\mathcal{B}}$$

### Propiedades

1. $P_{\mathcal{B} \to \mathcal{B}'}$ es siempre invertible
2. $P_{\mathcal{B}' \to \mathcal{B}} = \left(P_{\mathcal{B} \to \mathcal{B}'}\right)^{-1}$
3. $P_{\mathcal{B} \to \mathcal{B}''} = P_{\mathcal{B}' \to \mathcal{B}''} \cdot P_{\mathcal{B} \to \mathcal{B}'}$

### Cálculo Práctico (en $\mathbb{R}^n$)

Para encontrar $P_{\mathcal{B} \to \mathcal{B}'}$:
1. Formar la matriz $(B' | B)$ donde $B'$ y $B$ son las matrices de las bases
2. Reducir a $(I | P)$
3. $P = P_{\mathcal{B} \to \mathcal{B}'}$

### Fórmulas de Dimensión

**Suma de subespacios:**
$$\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$$

**Teorema del Rango-Nulidad:**
$$\dim(\text{Nul}(A)) + \dim(\text{Col}(A)) = n$$

donde $A$ es $m \times n$.
