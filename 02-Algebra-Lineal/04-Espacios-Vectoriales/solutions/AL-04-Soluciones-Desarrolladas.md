<!--
::METADATA::
type: solution
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Soluciones: Espacios Vectoriales

---

## Problema 4a
**Enunciado:** ¿Es $W_1 = \{(x, y, z) : x + y + z = 0\}$ [subespacio](../../..](../../../glossary.md)#subespacio) de $\mathbb{R}^3$?

**Solución:**

1. **[Vector](../../..](../../../glossary.md)#vector) cero:** $(0,0,0)$: $0 + 0 + 0 = 0$ ✓

2. **Cerradura suma:** Sean $u = (x_1, y_1, z_1)$, $v = (x_2, y_2, z_2) \in W_1$
   - $u + v = (x_1+x_2, y_1+y_2, z_1+z_2)$
   - $(x_1+x_2) + (y_1+y_2) + (z_1+z_2) = (x_1+y_1+z_1) + (x_2+y_2+z_2) = 0 + 0 = 0$ ✓

3. **Cerradura escalar:** Sea $v = (x,y,z) \in W_1$, $c \in \mathbb{R}$
   - $cv = (cx, cy, cz)$
   - $cx + cy + cz = c(x+y+z) = c(0) = 0$ ✓

**$W_1$ es [subespacio](../../..](../../../glossary.md)#subespacio)** ✓

---

## Problema 4b
**Enunciado:** ¿Es $W_2 = \{(x, y, z) : x + y + z = 1\}$ subespacio?

**Solución:**

$\mathbf{0} = (0,0,0)$: $0 + 0 + 0 = 0 \neq 1$

**$W_2$ NO es subespacio** (no contiene el [vector](../../..](../../../glossary.md)#vector) cero)

---

## Problema 9
**Enunciado:** ¿Es $v = (1, 2, 3)$ [combinación lineal](../../..](../../../glossary.md)#combinacion-lineal) de $u_1 = (1, 0, 1)$ y $u_2 = (0, 1, 1)$?

**Solución:**

Buscamos $c_1, c_2$ tales que $c_1(1,0,1) + c_2(0,1,1) = (1,2,3)$

Sistema:
$$\begin{cases} c_1 = 1 \\ c_2 = 2 \\ c_1 + c_2 = 3 \end{cases}$$

De las primeras dos: $c_1 = 1$, $c_2 = 2$
Verificación: $1 + 2 = 3$ ✓

**Sí**, $v = 1 \cdot u_1 + 2 \cdot u_2$

---

## Problema 14a
**Enunciado:** ¿Son $(1, 2)$, $(3, 6)$ LI o LD?

**Solución:**

$(3, 6) = 3(1, 2)$

**Son LD** (uno es múltiplo del otro)

---

## Problema 14c
**Enunciado:** ¿Son $(1, 1, 0)$, $(0, 1, 1)$, $(1, 0, 1)$ LI o LD?

**Solución:**

$$\begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$

$\det = 1(1-0) - 0 + 1(1-0) = 1 + 1 = 2 \neq 0$

**Son LI** ([determinante](../../..](../../../glossary.md)#determinante) no nulo)

---

## Problema 19a
**Enunciado:** Encontrar [base](../../..](../../../glossary.md)#base) y [dimensión](../../..](../../../glossary.md)#dimension) de $W = \{(x, y, z) : x - 2y + z = 0\}$

**Solución:**

De $x - 2y + z = 0$: $x = 2y - z$

Parametrizando con $y = s$, $z = t$:
$$(x, y, z) = (2s - t, s, t) = s(2, 1, 0) + t(-1, 0, 1)$$

**[Base](../../..](../../../glossary.md)#base):** $\{(2, 1, 0), (-1, 0, 1)\}$

**[Dimensión](../../..](../../../glossary.md)#dimension):** $2$

---

## Problema 20
**Enunciado:** Encontrar base para matrices simétricas $2 \times 2$.

**Solución:**

Una [matriz simétrica](../../..](../../../glossary.md)#matriz-simetrica) $2 \times 2$ tiene la forma:
$$A = \begin{pmatrix} a & b \\ b & c \end{pmatrix} = a\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + b\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} + c\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$$

**Base:** $\left\{\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}\right\}$

**Dimensión:** $3$

---

## Problema 21
**Enunciado:** Encontrar base y dimensión de $\text{Nul}(A)$ donde $A = \begin{pmatrix} 1 & 2 & -1 & 3 \\ 2 & 4 & -2 & 6 \end{pmatrix}$

**Solución:**

RREF:
$$\begin{pmatrix} 1 & 2 & -1 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

Variables libres: $x_2 = r$, $x_3 = s$, $x_4 = t$
Variable ligada: $x_1 = -2r + s - 3t$

$$x = \begin{pmatrix} -2r + s - 3t \\ r \\ s \\ t \end{pmatrix} = r\begin{pmatrix} -2 \\ 1 \\ 0 \\ 0 \end{pmatrix} + s\begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \end{pmatrix} + t\begin{pmatrix} -3 \\ 0 \\ 0 \\ 1 \end{pmatrix}$$

**Base:** $\left\{\begin{pmatrix} -2 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} -3 \\ 0 \\ 0 \\ 1 \end{pmatrix}\right\}$

**Dimensión:** $3$ (nulidad)

---

## Problema 25a
**Enunciado:** Con $\mathcal{B} = \{(1, 1), (1, -1)\}$, encontrar $[v]_{\mathcal{B}}$ para $v = (4, 2)$.

**Solución:**

$v = c_1(1,1) + c_2(1,-1)$

Sistema:
$$\begin{cases} c_1 + c_2 = 4 \\ c_1 - c_2 = 2 \end{cases}$$

Sumando: $2c_1 = 6 \Rightarrow c_1 = 3$
Restando: $2c_2 = 2 \Rightarrow c_2 = 1$

**$[v]_{\mathcal{B}} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}$**

---

## Problema 27
**Enunciado:** Encontrar $P_{\mathcal{B} \to \mathcal{B}'}$ de $\mathcal{B} = \{e_1, e_2\}$ a $\mathcal{B}' = \{(1, 1), (2, 1)\}$.

**Solución:**

Necesitamos expresar $e_1, e_2$ en términos de $\mathcal{B}'$:

Para $e_1 = (1, 0)$: $(1,0) = c_1(1,1) + c_2(2,1)$
- $c_1 + 2c_2 = 1$
- $c_1 + c_2 = 0$

Restando: $c_2 = 1$, entonces $c_1 = -1$

$[e_1]_{\mathcal{B}'} = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$

Para $e_2 = (0, 1)$: $(0,1) = c_1(1,1) + c_2(2,1)$
- $c_1 + 2c_2 = 0$
- $c_1 + c_2 = 1$

Restando: $c_2 = -1$, entonces $c_1 = 2$

$[e_2]_{\mathcal{B}'} = \begin{pmatrix} 2 \\ -1 \end{pmatrix}$

**$P_{\mathcal{B} \to \mathcal{B}'} = \begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix}$**

---

## Problema 28
**Enunciado:** Si $[v]_{\mathcal{B}} = \begin{pmatrix} 3 \\ -2 \end{pmatrix}$ y $P_{\mathcal{B} \to \mathcal{B}'} = \begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix}$, encontrar $[v]_{\mathcal{B}'}$.

**Solución:**

$$[v]_{\mathcal{B}'} = P_{\mathcal{B} \to \mathcal{B}'} \cdot [v]_{\mathcal{B}} = \begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix} \begin{pmatrix} 3 \\ -2 \end{pmatrix}$$

$$= \begin{pmatrix} 2(3) + 1(-2) \\ -1(3) + 3(-2) \end{pmatrix} = \begin{pmatrix} 6 - 2 \\ -3 - 6 \end{pmatrix} = \begin{pmatrix} 4 \\ -9 \end{pmatrix}$$

**$[v]_{\mathcal{B}'} = \begin{pmatrix} 4 \\ -9 \end{pmatrix}$**
