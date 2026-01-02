<!--
::METADATA::
type: solution
status: active
-->

# Soluciones: Transformaciones Lineales

---

## Problema 1a
**Enunciado:** ¿Es $T(x, y) = (2x + y, x - 3y)$ lineal?

**Solución:**

**Paso 1:** $T(0, 0) = (0, 0)$ ✓

**Paso 2 (Aditividad):** Sean $u = (x_1, y_1)$, $v = (x_2, y_2)$
- $T(u + v) = (2(x_1+x_2) + (y_1+y_2), (x_1+x_2) - 3(y_1+y_2))$
- $T(u) + T(v) = (2x_1 + y_1 + 2x_2 + y_2, x_1 - 3y_1 + x_2 - 3y_2)$

Son iguales ✓

**Paso 3 (Homogeneidad):** $T(cv) = (2cx + cy, cx - 3cy) = c(2x + y, x - 3y) = cT(v)$ ✓

**$T$ es lineal** ✓

---

## Problema 1b
**Enunciado:** ¿Es $T(x, y) = (x^2, y)$ lineal?

**Solución:**

Verificamos aditividad:
- $T((1,0) + (1,0)) = T(2,0) = (4, 0)$
- $T(1,0) + T(1,0) = (1, 0) + (1, 0) = (2, 0)$

$(4, 0) \neq (2, 0)$

**$T$ NO es lineal** ✗

---

## Problema 6
**Enunciado:** $T(x, y, z) = (x - y, y - z)$. Hallar núcleo e imagen.

**Solución:**

**a) Núcleo:**
$T(x, y, z) = (0, 0)$:
$$\begin{cases} x - y = 0 \\ y - z = 0 \end{cases}$$

De aquí: $x = y = z$. Sea $x = t$:
$$\ker(T) = \{(t, t, t) : t \in \mathbb{R}\} = \text{span}\{(1, 1, 1)\}$$

**[Base](../../../glossary.md#base) de $\ker(T)$:** $\{(1, 1, 1)\}$, **nulidad = 1**

**b) Imagen:**
- $T(1, 0, 0) = (1, 0)$
- $T(0, 1, 0) = (-1, 1)$
- $T(0, 0, 1) = (0, -1)$

[Matriz](../../../glossary.md#matriz): $\begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \end{pmatrix}$ ya está en forma escalonada.

**[Base](../../../glossary.md#base) de $\text{Im}(T)$:** $\{(1, 0), (-1, 1)\}$ o equivalente $\{(1, 0), (0, 1)\}$

**$\text{Im}(T) = \mathbb{R}^2$**, **rango = 2**

**c) Verificación:** $\dim(\mathbb{R}^3) = 3 = 1 + 2$ ✓

---

## Problema 11a
**Enunciado:** [Matriz](../../../glossary.md#matriz) de $T(x, y) = (3x - y, 2x + 4y)$

**Solución:**

- $T(e_1) = T(1, 0) = (3, 2)$
- $T(e_2) = T(0, 1) = (-1, 4)$

$$[T] = \begin{pmatrix} 3 & -1 \\ 2 & 4 \end{pmatrix}$$

---

## Problema 13
**Enunciado:** Matriz de rotación de $45°$

**Solución:**

$$R_{45°} = \begin{pmatrix} \cos 45° & -\sin 45° \\ \sin 45° & \cos 45° \end{pmatrix} = \begin{pmatrix} \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \end{pmatrix}$$

---

## Problema 16
**Enunciado:** $T(x, y) = (x + y, x - y)$ en base $\mathcal{B} = \{(1, 1), (1, -1)\}$

**Solución:**

- $T(1, 1) = (2, 0)$
- $T(1, -1) = (0, 2)$

Expresamos en base $\mathcal{B}$:
- $(2, 0) = a(1,1) + b(1,-1) \Rightarrow a + b = 2, a - b = 0 \Rightarrow a = b = 1$
  
  $[T(1,1)]_{\mathcal{B}} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$... 

Espera, revisemos: $(2, 0) = 1(1, 1) + 1(1, -1) = (2, 0)$ ✓

- $(0, 2) = a(1,1) + b(1,-1) \Rightarrow a + b = 0, a - b = 2 \Rightarrow a = 1, b = -1$
  
  $[T(1,-1)]_{\mathcal{B}} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$

$$[T]_{\mathcal{B}} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

---

## Problema 17
**Enunciado:** $T(x, y) = (x + y, 2y)$, $S(x, y) = (x - y, x)$

**Solución:**

$$[T] = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}, \quad [S] = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix}$$

**a)** $[S \circ T] = [S][T] = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$

**b)** $[T \circ S] = [T][S] = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ 2 & 0 \end{pmatrix}$

**c)** No son iguales: $[S \circ T] \neq [T \circ S]$

---

## Problema 18
**Enunciado:** $[T] = \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix}$

**Solución:**

**a)** $\det(T) = 4 - 3 = 1 \neq 0$, **$T$ es invertible** ✓

**b)** $[T^{-1}] = \frac{1}{1}\begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix}$

**c)** $[T][T^{-1}] = \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix}\begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ ✓

---

## Problema 21
**Enunciado:** $[T]_{\mathcal{E}} = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$, base $\mathcal{B} = \{(1, 1), (1, 0)\}$

**Solución:**

$P_{\mathcal{B} \to \mathcal{E}} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$

$P^{-1} = \begin{pmatrix} 0 & 1 \\ 1 & -1 \end{pmatrix}$

$$[T]_{\mathcal{B}} = P^{-1}[T]_{\mathcal{E}}P = \begin{pmatrix} 0 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$$

$$= \begin{pmatrix} 0 & 2 \\ 3 & -1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 2 & 3 \end{pmatrix}$$

---

## Problema 22
**Enunciado:** ¿Son $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ y $B = I$ similares?

**Solución:**

Matrices similares tienen el mismo [determinante](../../../glossary.md#determinante) y [traza](../../../glossary.md#traza).

- $\det(A) = 1$, $\det(B) = 1$ ✓
- $\text{tr}(A) = 2$, $\text{tr}(B) = 2$ ✓

Pero $A \neq I$, y si fueran similares: $A = P^{-1}IP = P^{-1}P = I$

Contradicción. **No son similares.**

(Alternativamente: $A$ no es diagonalizable porque $(A - I)^2 = 0$ pero $A \neq I$)

---

## Problema 26
**Enunciado:** Base $\mathcal{B} = \{(1, 1), (-1, 1)\}$, $[p]_{\mathcal{B}} = (3, 2)^T$

**Solución:**

$$p = 3(1, 1) + 2(-1, 1) = (3, 3) + (-2, 2) = (1, 5)$$

**Posición en coordenadas estándar:** $(1, 5)$

---

## Problema 27
**Enunciado:** Migración entre ciudades

**Solución:**

Sea $x = (a, b)^T$ donde $a$ = población de $A$, $b$ = población de $B$.

Después de un año:
- Nueva población de $A$: $0.90a + 0.05b$
- Nueva población de $B$: $0.10a + 0.95b$

$$[T] = \begin{pmatrix} 0.90 & 0.05 \\ 0.10 & 0.95 \end{pmatrix}$$

Esta es una **matriz de Markov** (columnas suman 1).
