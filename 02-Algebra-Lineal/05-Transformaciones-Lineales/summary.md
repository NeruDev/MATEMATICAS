# Resumen: Transformaciones Lineales

## Definición

$T: V \to W$ es **transformación lineal** si:

$$T(u + v) = T(u) + T(v) \quad \text{y} \quad T(cv) = cT(v)$$

Equivalentemente: $T(au + bv) = aT(u) + bT(v)$

## Núcleo (Kernel)

$$\ker(T) = \{v \in V : T(v) = \mathbf{0}\}$$

- $\ker(T)$ es subespacio de $V$
- **Nulidad:** $\text{nul}(T) = \dim(\ker(T))$
- $T$ es inyectiva $\Leftrightarrow \ker(T) = \{\mathbf{0}\}$

## Imagen (Rango)

$$\text{Im}(T) = \{T(v) : v \in V\} = \{w \in W : \exists v, T(v) = w\}$$

- $\text{Im}(T)$ es subespacio de $W$
- **Rango:** $\text{rango}(T) = \dim(\text{Im}(T))$
- $T$ es sobreyectiva $\Leftrightarrow \text{Im}(T) = W$

## Teorema del Rango-Nulidad

$$\dim(V) = \dim(\ker(T)) + \dim(\text{Im}(T))$$
$$n = \text{nul}(T) + \text{rango}(T)$$

## Matriz de una Transformación

Si $\mathcal{B} = \{v_1, ..., v_n\}$ es base de $V$ y $\mathcal{C}$ base de $W$:

$$[T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix} | & | & & | \\ [T(v_1)]_{\mathcal{C}} & [T(v_2)]_{\mathcal{C}} & \cdots & [T(v_n)]_{\mathcal{C}} \\ | & | & & | \end{pmatrix}$$

**Relación fundamental:**
$$[T(v)]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} \cdot [v]_{\mathcal{B}}$$

## Composición

$$[S \circ T]_{\mathcal{B}}^{\mathcal{D}} = [S]_{\mathcal{C}}^{\mathcal{D}} \cdot [T]_{\mathcal{B}}^{\mathcal{C}}$$

## Cambio de Base

$$[T]_{\mathcal{B}'}^{\mathcal{B}'} = P^{-1} [T]_{\mathcal{B}}^{\mathcal{B}} P$$

donde $P = P_{\mathcal{B}' \to \mathcal{B}}$

## Matrices Similares

$A$ y $B$ son **similares** si existe $P$ invertible tal que:
$$B = P^{-1}AP$$

Matrices similares representan la misma transformación en diferentes bases.

## Isomorfismo

$T$ es **isomorfismo** si es biyectiva (inyectiva y sobreyectiva).

$$V \cong W \Leftrightarrow \dim(V) = \dim(W)$$
