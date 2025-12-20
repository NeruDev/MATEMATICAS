# Resumen: Espacios Vectoriales

## Axiomas de Espacio Vectorial

Sea $V$ un conjunto con operaciones $+$ y $\cdot$:

| Propiedad | Suma | Multiplicación Escalar |
|-----------|------|------------------------|
| Cerradura | $u + v \in V$ | $c \cdot v \in V$ |
| Asociatividad | $(u+v)+w = u+(v+w)$ | $a(bv) = (ab)v$ |
| Conmutatividad | $u + v = v + u$ | — |
| Elemento neutro | $v + 0 = v$ | $1 \cdot v = v$ |
| Inverso | $v + (-v) = 0$ | — |
| Distributividad | — | $a(u+v) = au + av$ |
| | | $(a+b)v = av + bv$ |

## Subespacio Vectorial

$W \subseteq V$ es subespacio si:
1. $\mathbf{0} \in W$
2. $u, v \in W \Rightarrow u + v \in W$
3. $v \in W, c \in \mathbb{F} \Rightarrow cv \in W$

## Combinación Lineal y Span

$$\text{span}\{v_1, ..., v_k\} = \{c_1v_1 + ... + c_kv_k : c_i \in \mathbb{F}\}$$

## Independencia Lineal

$\{v_1, ..., v_k\}$ es **linealmente independiente** si:
$$c_1v_1 + ... + c_kv_k = 0 \Rightarrow c_1 = ... = c_k = 0$$

## Base y Dimensión

- **Base:** Conjunto linealmente independiente que genera $V$
- **Dimensión:** $\dim(V)$ = número de vectores en cualquier base

### Bases estándar

| Espacio | Base estándar | Dimensión |
|---------|---------------|----------|
| $\mathbb{R}^n$ | $\{e_1, ..., e_n\}$ | $n$ |
| $P_n(x)$ | $\{1, x, x^2, ..., x^n\}$ | $n+1$ |
| $M_{m \times n}$ | $\{E_{ij}\}$ | $mn$ |

## Coordenadas

Si $\mathcal{B} = \{v_1, ..., v_n\}$ es base y $v = c_1v_1 + ... + c_nv_n$:

$$[v]_{\mathcal{B}} = \begin{pmatrix} c_1 \\ \vdots \\ c_n \end{pmatrix}$$

## Cambio de Base

$$[v]_{\mathcal{B}'} = P_{\mathcal{B} \to \mathcal{B}'} \cdot [v]_{\mathcal{B}}$$

$$P_{\mathcal{B} \to \mathcal{B}'} = \left([v_1]_{\mathcal{B}'} \mid ... \mid [v_n]_{\mathcal{B}'}\right)$$

## Fórmulas de Dimensión

$$\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$$

$$\dim(V) = \dim(\ker(T)) + \dim(\text{Im}(T))$$
