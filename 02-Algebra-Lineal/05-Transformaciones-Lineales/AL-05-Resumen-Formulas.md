<!--
::METADATA::
type: cheat-sheet
topic_id: al-05-transformaciones-lineales
file_id: AL-05-Resumen-Formulas
status: stable
audience: student
-->

> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

---

# Resumen de Fórmulas: Transformaciones Lineales

## Definición

$T: V \to W$ es **[transformación lineal](../..](../../glossary.md)#transformacion-lineal)** si:
1. $T(\vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v})$ (aditividad)
2. $T(c\vec{v}) = cT(\vec{v})$ (homogeneidad)

**Equivalente**: $T(c\vec{u} + d\vec{v}) = cT(\vec{u}) + dT(\vec{v})$

### Consecuencias inmediatas
- $T(\vec{0}) = \vec{0}$
- $T(-\vec{v}) = -T(\vec{v})$
- $T\left(\sum_{i=1}^n c_i\vec{v}_i\right) = \sum_{i=1}^n c_i T(\vec{v}_i)$

## Núcleo (Kernel)

$$\ker(T) = \{\vec{v} \in V : T(\vec{v}) = \vec{0}\}$$

- $\ker(T)$ es [subespacio](../..](../../glossary.md)#subespacio) de $V$
- **Nulidad**: $\text{nul}(T) = \dim(\ker(T))$

## Imagen (Rango)

$$\text{Im}(T) = \{T(\vec{v}) : \vec{v} \in V\} = \{w \in W : \exists \vec{v} \in V, T(\vec{v}) = w\}$$

- $\text{Im}(T)$ es [subespacio](../..](../../glossary.md)#subespacio) de $W$
- **Rango**: $\text{rang}(T) = \dim(\text{Im}(T))$

## Teorema del rango-nulidad

$$\dim(V) = \text{nul}(T) + \text{rang}(T)$$

$$\dim(V) = \dim(\ker(T)) + \dim(\text{Im}(T))$$

## Clasificación de transformaciones

| Propiedad | Condición | Equivalencia |
|-----------|-----------|--------------|
| **Inyectiva** (1-1) | $T(\vec{u}) = T(\vec{v}) \Rightarrow \vec{u} = \vec{v}$ | $\ker(T) = \{\vec{0}\}$ |
| **Sobreyectiva** (sobre) | $\text{Im}(T) = W$ | $\text{rang}(T) = \dim(W)$ |
| **Isomorfismo** | Inyectiva + Sobreyectiva | $T$ es invertible |

## Matriz de una transformación lineal

Si $\mathcal{B} = \{\vec{v}_1, \ldots, \vec{v}_n\}$ es [base](../..](../../glossary.md)#base) de $V$ y $\mathcal{C}$ es base de $W$:

$$[T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix} | & | & & | \\ [T(\vec{v}_1)]_{\mathcal{C}} & [T(\vec{v}_2)]_{\mathcal{C}} & \cdots & [T(\vec{v}_n)]_{\mathcal{C}} \\ | & | & & | \end{pmatrix}$$

### Relación fundamental
$$[T(\vec{v})]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} [\vec{v}]_{\mathcal{B}}$$

## Composición de transformaciones

Si $T: V \to W$ y $S: W \to U$:
$$(S \circ T)(\vec{v}) = S(T(\vec{v}))$$

### Matriz de la composición
$$[S \circ T] = [S][T]$$

## Transformación inversa

Si $T: V \to W$ es [isomorfismo](../..](../../glossary.md)#isomorfismo):
$$T^{-1}: W \to V$$
$$T^{-1}(T(\vec{v})) = \vec{v}$$

### Matriz de la inversa
$$[T^{-1}] = [T]^{-1}$$

## Cambio de base

Si $T: V \to V$ y cambiamos de [base](../..](../../glossary.md)#base) $\mathcal{B}$ a $\mathcal{B}'$:

$$[T]_{\mathcal{B}'} = P^{-1}[T]_{\mathcal{B}}P$$

donde $P = P_{\mathcal{B}' \to \mathcal{B}}$ es la [matriz](../..](../../glossary.md)#matriz) de cambio de base.

### Matrices similares
$A$ y $B$ son **similares** si existe $P$ invertible [tal que](../..](../../glossary.md)#tal-que):
$$B = P^{-1}AP$$

## Transformaciones importantes en $\mathbb{R}^2$

| Transformación | [Matriz](../../glossary.md#matriz) |
|----------------|--------|
| Rotación ángulo $\theta$ | $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ |
| Reflexión eje $x$ | $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ |
| Reflexión eje $y$ | $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ |
| Escalamiento | $\begin{pmatrix} k_1 & 0 \\ 0 & k_2 \end{pmatrix}$ |
| Proyección sobre eje $x$ | $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ |

## Propiedades de la matriz asociada

Para $T: \mathbb{R}^n \to \mathbb{R}^m$ con matriz $A$:
- $\ker(T) = \text{Nul}(A)$
- $\text{Im}(T) = \text{Col}(A)$
- $\text{nul}(T) = n - \text{rang}(A)$
- $\text{rang}(T) = \text{rang}(A)$
