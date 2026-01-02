<!--
::METADATA::
type: cheat-sheet
topic_id: al-04-espacios-vectoriales
file_id: AL-04-Resumen-Formulas
status: stable
audience: student
-->
# Resumen de Fórmulas: Espacios Vectoriales

## Axiomas de espacio vectorial

Un conjunto $V$ con operaciones $+$ y $\cdot$ es [espacio vectorial](../../glossary.md#espacio-vectorial) si:

### Suma
1. $\vec{u} + \vec{v} = \vec{v} + \vec{u}$ (conmutativa)
2. $(\vec{u} + \vec{v}) + \vec{w} = \vec{u} + (\vec{v} + \vec{w})$ (asociativa)
3. Existe $\vec{0}$ [tal que](../../glossary.md#tal-que) $\vec{v} + \vec{0} = \vec{v}$ (neutro)
4. Existe $-\vec{v}$ [tal que](../../glossary.md#tal-que) $\vec{v} + (-\vec{v}) = \vec{0}$ (inverso)

### Producto por escalar
5. $c(\vec{u} + \vec{v}) = c\vec{u} + c\vec{v}$
6. $(c + d)\vec{v} = c\vec{v} + d\vec{v}$
7. $c(d\vec{v}) = (cd)\vec{v}$
8. $1 \cdot \vec{v} = \vec{v}$

## Criterio de subespacio

$W \subseteq V$ es [subespacio](../../glossary.md#subespacio) si:
1. $\vec{0} \in W$
2. $\vec{u}, \vec{v} \in W \Rightarrow \vec{u} + \vec{v} \in W$ (cerrado bajo suma)
3. $\vec{v} \in W, c \in \mathbb{R} \Rightarrow c\vec{v} \in W$ (cerrado bajo escalar)

**Equivalente**: $W \neq \emptyset$ y $\forall \vec{u}, \vec{v} \in W, \forall c, d \in \mathbb{R}: c\vec{u} + d\vec{v} \in W$

## Combinación lineal

$$\vec{v} = c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_n\vec{v}_n = \sum_{i=1}^{n} c_i\vec{v}_i$$

## Span (espacio generado)

$$\text{span}\{\vec{v}_1, \ldots, \vec{v}_n\} = \{c_1\vec{v}_1 + \cdots + c_n\vec{v}_n : c_i \in \mathbb{R}\}$$

## Independencia lineal

$\{\vec{v}_1, \ldots, \vec{v}_n\}$ es **linealmente independiente** si:
$$c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_n\vec{v}_n = \vec{0} \Rightarrow c_1 = c_2 = \cdots = c_n = 0$$

### Criterios prácticos
- En $\mathbb{R}^n$: formar [matriz](../../glossary.md#matriz) y verificar $\det \neq 0$ (si es cuadrada)
- Calcular rango de la [matriz](../../glossary.md#matriz) formada por los vectores

## Base

$\mathcal{B} = \{\vec{v}_1, \ldots, \vec{v}_n\}$ es **[base](../../glossary.md#base)** de $V$ si:
1. $\mathcal{B}$ es linealmente independiente
2. $\text{span}(\mathcal{B}) = V$

### Base canónica de $\mathbb{R}^n$
$$\mathcal{E} = \{\vec{e}_1, \vec{e}_2, \ldots, \vec{e}_n\}$$

donde $\vec{e}_i$ tiene 1 en posición $i$ y 0 en las demás.

## Dimensión

$$\dim(V) = \text{número de vectores en cualquier [base](../../glossary.md#base) de } V$$

### Dimensiones importantes
- $\dim(\mathbb{R}^n) = n$
- $\dim(M_{m \times n}) = mn$
- $\dim(P_n) = n + 1$ (polinomios de grado $\leq n$)

## Coordenadas

Si $\mathcal{B} = \{\vec{v}_1, \ldots, \vec{v}_n\}$ es base y $\vec{v} = c_1\vec{v}_1 + \cdots + c_n\vec{v}_n$:

$$[\vec{v}]_{\mathcal{B}} = \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{pmatrix}$$

## Cambio de base

$$[\vec{v}]_{\mathcal{B}'} = P_{\mathcal{B} \to \mathcal{B}'} [\vec{v}]_{\mathcal{B}}$$

### Matriz de cambio de base
$$P_{\mathcal{B} \to \mathcal{B}'} = \left( [\vec{b}_1]_{\mathcal{B}'} \mid [\vec{b}_2]_{\mathcal{B}'} \mid \cdots \mid [\vec{b}_n]_{\mathcal{B}'} \right)$$

### Propiedad
$$P_{\mathcal{B}' \to \mathcal{B}} = \left(P_{\mathcal{B} \to \mathcal{B}'}\right)^{-1}$$

## Teoremas importantes

### Teorema de la dimensión para subespacios
Si $W$ es [subespacio](../../glossary.md#subespacio) de $V$:
$$\dim(W) \leq \dim(V)$$

### Suma de subespacios
$$\dim(U + W) = \dim(U) + \dim(W) - \dim(U \cap W)$$

### Suma directa
$V = U \oplus W$ si:
- $V = U + W$
- $U \cap W = \{\vec{0}\}$

En tal caso: $\dim(V) = \dim(U) + \dim(W)$
