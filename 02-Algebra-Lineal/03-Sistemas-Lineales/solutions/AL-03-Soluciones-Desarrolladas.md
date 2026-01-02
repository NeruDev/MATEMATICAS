<!--
::METADATA::
type: solution
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Soluciones de Sistemas de Ecuaciones Lineales

---

## Problema 2
**Enunciado:** Resolver $\begin{cases} x + y = 5 \\ 2x - y = 4 \end{cases}$

**Solución:**
$$\left(\begin{array}{cc|c} 1 & 1 & 5 \\ 2 & -1 & 4 \end{array}\right)$$

$R_2 \leftarrow R_2 - 2R_1$:
$$\left(\begin{array}{cc|c} 1 & 1 & 5 \\ 0 & -3 & -6 \end{array}\right)$$

De fila 2: $-3y = -6 \Rightarrow y = 2$
De fila 1: $x + 2 = 5 \Rightarrow x = 3$

**Solución:** $x = 3$, $y = 2$

---

## Problema 3
**Enunciado:** Resolver el sistema $3 \times 3$.

**Solución:**
$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 6 \\ 2 & 1 & -1 & 1 \\ 1 & -1 & 2 & 5 \end{array}\right)$$

$R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - R_1$:
$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 6 \\ 0 & -3 & -3 & -11 \\ 0 & -3 & 1 & -1 \end{array}\right)$$

$R_3 \leftarrow R_3 - R_2$:
$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 6 \\ 0 & -3 & -3 & -11 \\ 0 & 0 & 4 & 10 \end{array}\right)$$

[Sustitución](../../../glossary.md#sustitucion) hacia atrás:
- $4z = 10 \Rightarrow z = 5/2$
- $-3y - 3(5/2) = -11 \Rightarrow y = 7/6$
- $x + 2(7/6) + 5/2 = 6 \Rightarrow x = 5/3$

**Solución:** $x = 5/3$, $y = 7/6$, $z = 5/2$

---

## Problema 9
**Enunciado:** Clasificar $\begin{cases} x + y = 2 \\ 2x + 2y = 4 \end{cases}$

**Solución:**
$$\left(\begin{array}{cc|c} 1 & 1 & 2 \\ 2 & 2 & 4 \end{array}\right) \rightarrow \left(\begin{array}{cc|c} 1 & 1 & 2 \\ 0 & 0 & 0 \end{array}\right)$$

$\text{rango}(A) = 1$, $\text{rango}(A|b) = 1$, $n = 2$

Como $\text{rango}(A) = \text{rango}(A|b) < n$: **Compatible indeterminado** (infinitas soluciones).

Solución: $x = 2 - t$, $y = t$ para $t \in \mathbb{R}$

---

## Problema 10
**Enunciado:** Clasificar $\begin{cases} x + y = 2 \\ x + y = 3 \end{cases}$

**Solución:**
$$\left(\begin{array}{cc|c} 1 & 1 & 2 \\ 1 & 1 & 3 \end{array}\right) \rightarrow \left(\begin{array}{cc|c} 1 & 1 & 2 \\ 0 & 0 & 1 \end{array}\right)$$

La fila $[0 \, 0 \, | \, 1]$ indica $0 = 1$, contradicción.

$\text{rango}(A) = 1$, $\text{rango}(A|b) = 2$

Como $\text{rango}(A) < \text{rango}(A|b)$: **Incompatible** (sin solución).

---

## Problema 11
**Enunciado:** ¿Para qué $k$ hay infinitas soluciones?

**Solución:**
$$\left(\begin{array}{cc|c} 1 & k & 1 \\ 2 & 2 & 2 \end{array}\right) \rightarrow \left(\begin{array}{cc|c} 1 & k & 1 \\ 0 & 2-2k & 0 \end{array}\right)$$

Para infinitas soluciones: la segunda fila debe ser toda ceros.
$2 - 2k = 0 \Rightarrow k = 1$

**Respuesta:** $k = 1$

---

## Problema 14
**Enunciado:** Hallar el rango de $A$.

**Solución:**
$$\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 1 & 1 \end{pmatrix}$$

$R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - R_1$:
$$\begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & -1 & -2 \end{pmatrix}$$

Intercambiamos $R_2 \leftrightarrow R_3$:
$$\begin{pmatrix} 1 & 2 & 3 \\ 0 & -1 & -2 \\ 0 & 0 & 0 \end{pmatrix}$$

Hay 2 pivotes.

**$\text{rango}(A) = 2$**

---

## Problema 17
**Enunciado:** Resolver $Ax = 0$ donde $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$.

**Solución:**
$$\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \rightarrow \begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix}$$

$x_1 + 2x_2 = 0$
$x_2 = t$ (libre)
$x_1 = -2t$

**Solución:** $x = t\begin{pmatrix} -2 \\ 1 \end{pmatrix}$, $t \in \mathbb{R}$

---

## Problema 22
**Enunciado:** Hallar parábola por $(1,2)$, $(2,3)$, $(3,6)$.

**Solución:**
$y = ax^2 + bx + c$ debe pasar por cada punto:

$$\begin{cases} a + b + c = 2 \\ 4a + 2b + c = 3 \\ 9a + 3b + c = 6 \end{cases}$$

$$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 4 & 2 & 1 & 3 \\ 9 & 3 & 1 & 6 \end{array}\right)$$

$R_2 \leftarrow R_2 - 4R_1$, $R_3 \leftarrow R_3 - 9R_1$:
$$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 0 & -2 & -3 & -5 \\ 0 & -6 & -8 & -12 \end{array}\right)$$

$R_3 \leftarrow R_3 - 3R_2$:
$$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 0 & -2 & -3 & -5 \\ 0 & 0 & 1 & 3 \end{array}\right)$$

De fila 3: $c = 3$
De fila 2: $-2b - 9 = -5 \Rightarrow b = -2$
De fila 1: $a - 2 + 3 = 2 \Rightarrow a = 1$

**Parábola:** $y = x^2 - 2x + 3$
