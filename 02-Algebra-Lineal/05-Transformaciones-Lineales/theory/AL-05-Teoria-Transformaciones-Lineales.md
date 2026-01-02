<!--
::METADATA::
type: theory
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Teoría de Transformaciones Lineales

---

## 5.1 Definición de Transformación Lineal

### Definición Formal

Sean $V$ y $W$ [espacios vectoriales](../../../glossary.md#espacios-vectoriales) sobre el mismo campo $\mathbb{F}$. Una [función](../../../glossary.md#funcion) $T: V \to W$ es una **[transformación lineal](../../../glossary.md#transformacion-lineal)** si satisface:

1. **Aditividad:** $T(u + v) = T(u) + T(v)$ para todo $u, v \in V$
2. **Homogeneidad:** $T(cv) = cT(v)$ para todo $c \in \mathbb{F}$, $v \in V$

Equivalentemente, $T$ es lineal si:
$$T(au + bv) = aT(u) + bT(v)$$
para todo $a, b \in \mathbb{F}$ y $u, v \in V$.

### Propiedades Inmediatas

> **Teorema:** Si $T: V \to W$ es lineal, entonces:
> 1. $T(\mathbf{0}_V) = \mathbf{0}_W$
> 2. $T(-v) = -T(v)$
> 3. $T(c_1v_1 + ... + c_nv_n) = c_1T(v_1) + ... + c_nT(v_n)$

### Ejemplos Fundamentales

**1. Transformación cero**
$$T: V \to W, \quad T(v) = \mathbf{0}$$

**2. Transformación identidad**
$$I: V \to V, \quad I(v) = v$$

**3. Multiplicación por [matriz](../../../glossary.md#matriz)**
$$T: \mathbb{R}^n \to \mathbb{R}^m, \quad T(x) = Ax$$
donde $A$ es [matriz](../../../glossary.md#matriz) $m \times n$.

**4. Derivación**
$$D: P_n \to P_{n-1}, \quad D(p(x)) = p'(x)$$

**5. Integración definida**
$$T: C[0,1] \to \mathbb{R}, \quad T(f) = \int_0^1 f(x)\,dx$$

**6. Rotación en $\mathbb{R}^2$**
$$R_\theta: \mathbb{R}^2 \to \mathbb{R}^2, \quad R_\theta(x, y) = (x\cos\theta - y\sin\theta, x\sin\theta + y\cos\theta)$$

### Verificación de Linealidad

Para verificar que $T$ es lineal:
1. Comprobar $T(\mathbf{0}) = \mathbf{0}$ ([necesario](../../../glossary.md#necesario) pero no [suficiente](../../../glossary.md#suficiente))
2. Verificar $T(u + v) = T(u) + T(v)$
3. Verificar $T(cv) = cT(v)$

**Contraejemplo:** $T(x) = x + 1$ no es lineal porque $T(0) = 1 \neq 0$.

### Determinación por una Base

> **Teorema Fundamental:** Una [transformación lineal](../../../glossary.md#transformacion-lineal) $T: V \to W$ queda completamente determinada por sus valores en una [base](../../../glossary.md#base) de $V$.

Si $\mathcal{B} = \{v_1, ..., v_n\}$ es [base](../../../glossary.md#base) de $V$ y conocemos $T(v_1), ..., T(v_n)$, entonces para cualquier $v = c_1v_1 + ... + c_nv_n$:
$$T(v) = c_1T(v_1) + ... + c_nT(v_n)$$

---

## 5.2 Núcleo e Imagen

### Núcleo (Kernel)

El **núcleo** de $T: V \to W$ es:
$$\ker(T) = \{v \in V : T(v) = \mathbf{0}_W\}$$

> **Teorema:** $\ker(T)$ es [subespacio](../../../glossary.md#subespacio) de $V$.

**Demostración:**
1. $T(\mathbf{0}) = \mathbf{0}$, así que $\mathbf{0} \in \ker(T)$
2. Si $u, v \in \ker(T)$: $T(u+v) = T(u) + T(v) = \mathbf{0} + \mathbf{0} = \mathbf{0}$
3. Si $v \in \ker(T)$, $c \in \mathbb{F}$: $T(cv) = cT(v) = c\mathbf{0} = \mathbf{0}$

**Nulidad:** $\text{nul}(T) = \dim(\ker(T))$

### Imagen (Rango)

La **imagen** de $T: V \to W$ es:
$$\text{Im}(T) = \{T(v) : v \in V\} = \{w \in W : \exists v \in V, T(v) = w\}$$

> **Teorema:** $\text{Im}(T)$ es [subespacio](../../../glossary.md#subespacio) de $W$.

Si $\{v_1, ..., v_n\}$ es base de $V$:
$$\text{Im}(T) = \text{span}\{T(v_1), ..., T(v_n)\}$$

**Rango:** $\text{rango}(T) = \dim(\text{Im}(T))$

### Teorema del Rango-Nulidad

> **Teorema:** Si $T: V \to W$ es lineal y $V$ tiene [dimensión](../../../glossary.md#dimension) finita:
> $$\dim(V) = \dim(\ker(T)) + \dim(\text{Im}(T))$$
> Es decir: $n = \text{nul}(T) + \text{rango}(T)$

### Inyectividad y Sobreyectividad

| Propiedad | Definición | Criterio |
|-----------|------------|----------|
| **Inyectiva** (1-1) | $T(u) = T(v) \Rightarrow u = v$ | $\ker(T) = \{\mathbf{0}\}$ |
| **Sobreyectiva** (sobre) | $\forall w \in W, \exists v: T(v) = w$ | $\text{Im}(T) = W$ |
| **Biyectiva** | Inyectiva y sobreyectiva | Ambos criterios |

> **Corolario:** Si $\dim(V) = \dim(W)$, entonces:
> $$T \text{ inyectiva} \Leftrightarrow T \text{ sobreyectiva} \Leftrightarrow T \text{ biyectiva}$$

---

## 5.3 Matriz de una Transformación Lineal

### Definición

Sea $T: V \to W$ lineal, $\mathcal{B} = \{v_1, ..., v_n\}$ base de $V$, $\mathcal{C} = \{w_1, ..., w_m\}$ base de $W$.

La **matriz de $T$ respecto a $\mathcal{B}$ y $\mathcal{C}$** es la matriz $m \times n$:

$$[T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix} | & | & & | \\ [T(v_1)]_{\mathcal{C}} & [T(v_2)]_{\mathcal{C}} & \cdots & [T(v_n)]_{\mathcal{C}} \\ | & | & & | \end{pmatrix}$$

Es decir, la columna $j$ es el [vector](../../../glossary.md#vector) de coordenadas de $T(v_j)$ en la base $\mathcal{C}$.

### Relación Fundamental

$$[T(v)]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} \cdot [v]_{\mathcal{B}}$$

Esto permite calcular la imagen de cualquier [vector](../../../glossary.md#vector) usando multiplicación matricial.

### Caso de Bases Estándar

Si $V = \mathbb{R}^n$, $W = \mathbb{R}^m$ con bases estándar, la matriz de $T$ es simplemente la matriz $A$ [tal que](../../../glossary.md#tal-que) $T(x) = Ax$.

### Ejemplo

Sea $T: \mathbb{R}^2 \to \mathbb{R}^2$ definida por $T(x, y) = (2x + y, x - y)$.

Con bases estándar:
- $T(e_1) = T(1, 0) = (2, 1)$
- $T(e_2) = T(0, 1) = (1, -1)$

$$[T] = \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}$$

### Propiedades

| Propiedad | Relación Matricial |
|-----------|-------------------|
| $T$ inyectiva | $\text{Nul}([T]) = \{\mathbf{0}\}$ |
| $T$ sobreyectiva | $\text{rango}([T]) = \dim(W)$ |
| $\text{rango}(T)$ | $\text{rango}([T])$ (rango de la matriz) |
| $\text{nul}(T)$ | $\text{nulidad}([T])$ |

---

## 5.4 Composición e Inversa

### Composición de Transformaciones

Si $T: U \to V$ y $S: V \to W$ son lineales, entonces $S \circ T: U \to W$ es lineal.

$$[S \circ T]_{\mathcal{B}}^{\mathcal{D}} = [S]_{\mathcal{C}}^{\mathcal{D}} \cdot [T]_{\mathcal{B}}^{\mathcal{C}}$$

**Nota:** El [orden](../../../glossary.md#orden) de multiplicación es inverso al de [composición](../../../glossary.md#composicion).

### Transformación Inversa

Si $T: V \to W$ es biyectiva, existe $T^{-1}: W \to V$ [tal que](../../../glossary.md#tal-que):
- $T^{-1} \circ T = I_V$
- $T \circ T^{-1} = I_W$

> **Teorema:** $T^{-1}$ es también lineal.

$$[T^{-1}]_{\mathcal{C}}^{\mathcal{B}} = \left([T]_{\mathcal{B}}^{\mathcal{C}}\right)^{-1}$$

### Isomorfismo

Una transformación lineal biyectiva se llama **[isomorfismo](../../../glossary.md#isomorfismo)**.

Si existe un [isomorfismo](../../../glossary.md#isomorfismo) $T: V \to W$, decimos que $V$ y $W$ son **isomorfos**: $V \cong W$.

> **Teorema:** Dos [espacios vectoriales](../../../glossary.md#espacios-vectoriales) de [dimensión](../../../glossary.md#dimension) finita son isomorfos si y solo si tienen la misma dimensión.
> $$V \cong W \Leftrightarrow \dim(V) = \dim(W)$$

### Automorfismos

Un isomorfismo de $V$ en sí mismo se llama **automorfismo**.

El conjunto de automorfismos de $V$ forma un grupo bajo [composición](../../../glossary.md#composicion): $\text{GL}(V)$.

---

## 5.5 Cambio de Base en Transformaciones

### Matriz de Transformación en Diferentes Bases

Sea $T: V \to V$ lineal y $\mathcal{B}, \mathcal{B}'$ dos bases de $V$.

Si $P = P_{\mathcal{B}' \to \mathcal{B}}$ es la matriz de cambio de base, entonces:

$$[T]_{\mathcal{B}'} = P^{-1} [T]_{\mathcal{B}} P$$

### Matrices Similares

Dos matrices $A$ y $B$ son **similares** si existe $P$ invertible tal que:
$$B = P^{-1}AP$$

> **Teorema:** Dos matrices son similares si y solo si representan la misma transformación lineal en diferentes bases.

### Propiedades Invariantes bajo Similitud

Las siguientes propiedades son iguales para matrices similares:
- [Determinante](../../../glossary.md#determinante): $\det(A) = \det(B)$
- [Traza](../../../glossary.md#traza): $\text{tr}(A) = \text{tr}(B)$
- Rango: $\text{rango}(A) = \text{rango}(B)$
- Valores propios
- [Polinomio característico](../../../glossary.md#polinomio-caracteristico)

### Diagonalización (Adelanto)

Encontrar una base $\mathcal{B}'$ tal que $[T]_{\mathcal{B}'}$ sea diagonal es el problema de **[diagonalización](../../../glossary.md#diagonalizacion)**, que se estudia con [valores y vectores propios](../../../glossary.md#valores-y-vectores-propios).

### Diagrama Conmutativo

```
       T
V ──────────► V
│             │
│[·]_B        │[·]_B'
▼             ▼
F^n ────────► F^n
     [T]_B

       T
V ──────────► V
│             │
│[·]_B'       │[·]_B'
▼             ▼
F^n ────────► F^n
    [T]_B'
```

La relación $[T]_{\mathcal{B}'} = P^{-1}[T]_{\mathcal{B}}P$ expresa que el diagrama conmuta.

---

## Transformaciones Lineales Importantes

### Reflexiones

**Reflexión respecto al eje $x$:**
$$T(x, y) = (x, -y), \quad [T] = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**Reflexión respecto a la recta $y = x$:**
$$T(x, y) = (y, x), \quad [T] = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

### Rotaciones

**Rotación de ángulo $\theta$:**
$$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

### Proyecciones

**Proyección sobre el eje $x$:**
$$T(x, y) = (x, 0), \quad [T] = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$$

### Escalamientos

**Escalamiento:**
$$T(x, y) = (ax, by), \quad [T] = \begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix}$$

### Shear (Cizallamiento)

**Shear horizontal:**
$$T(x, y) = (x + ky, y), \quad [T] = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$$
