<!--
::METADATA::
type: cheat-sheet
topic_id: al-05-transformaciones-lineales
file_id: AL-05-Resumen-Formulas
status: stable
audience: student
-->

> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Resumen de Fórmulas: Transformaciones Lineales

## Definición

$T: V \to W$ es **[transformación lineal](../../glossary.md#subespacio) de $V$
- **Nulidad**: $\text{nul}(T) = \dim(\ker(T))$

## Imagen (Rango)

$$\text{Im}(T) = \{T(\vec{v}) : \vec{v} \in V\} = \{w \in W : \exists \vec{v} \in V, T(\vec{v}) = w\}$$

- $\text{Im}(T)$ es [subespacio](../../glossary.md#base) de $V$ y $\mathcal{C}$ es base de $W$:

$$[T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix} | & | & & | \\ [T(\vec{v}_1)]_{\mathcal{C}} & [T(\vec{v}_2)]_{\mathcal{C}} & \cdots & [T(\vec{v}_n)]_{\mathcal{C}} \\ | & | & & | \end{pmatrix}$$

### Relación fundamental
$$[T(\vec{v})]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} [\vec{v}]_{\mathcal{B}}$$

## Composición de transformaciones

Si $T: V \to W$ y $S: W \to U$:
$$(S \circ T)(\vec{v}) = S(T(\vec{v}))$$

### Matriz de la composición
$$[S \circ T] = [S][T]$$

## Transformación inversa

Si $T: V \to W$ es [isomorfismo](../../glossary.md#isomorfismo):
$$T^{-1}: W \to V$$
$$T^{-1}(T(\vec{v})) = \vec{v}$$

### Matriz de la inversa
$$[T^{-1}] = [T]^{-1}$$

## Cambio de base

Si $T: V \to V$ y cambiamos de [base](../../glossary.md#base) $\mathcal{B}$ a $\mathcal{B}'$:

$$[T]_{\mathcal{B}'} = P^{-1}[T]_{\mathcal{B}}P$$

donde $P = P_{\mathcal{B}' \to \mathcal{B}}$ es la [matriz](../../glossary.md#tal-que):
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
