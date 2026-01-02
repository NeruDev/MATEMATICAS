<!--
::METADATA::
type: cheat-sheet
topic_id: al-02-[determinantes](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md#determinante) de la submatriz que resulta de eliminar fila $i$ y columna $j$.

### Cofactor $C_{ij}$
$$C_{ij} = (-1)^{i+j} M_{ij}$$

**Patrón de signos**:
$$\begin{pmatrix} + & - & + & \cdots \\ - & + & - & \cdots \\ + & - & + & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}$$

## Expansión por cofactores (Laplace)

### Por fila $i$
$$\det(A) = \sum_{j=1}^{n} a_{ij} C_{ij}$$

### Por columna $j$
$$\det(A) = \sum_{i=1}^{n} a_{ij} C_{ij}$$

**💡 Consejo**: Expandir por la fila o columna con más ceros.

## Propiedades fundamentales

| Propiedad | Efecto en det |
|-----------|---------------|
| Intercambiar dos filas | Cambia signo |
| Multiplicar fila por $k$ | Multiplica det por $k$ |
| Sumar múltiplo de fila a otra | No cambia |
| Fila de ceros | $\det = 0$ |
| Dos filas iguales | $\det = 0$ |
| [Matriz](../../glossary.md#matriz) $n \times n$
- $\det(I) = 1$

## Matriz adjunta

$$\text{adj}(A) = [C_{ji}] = \text{(matriz de cofactores)}^T$$

### Inversa por adjunta
$$A^{-1} = \frac{1}{\det(A)} \text{adj}(A)$$

## Regla de Cramer

Para el sistema $Ax = b$ con $\det(A) \neq 0$:

$$x_i = \frac{\det(A_i)}{\det(A)}$$

donde $A_i$ es la matriz $A$ con la columna $i$ reemplazada por $b$.

## Criterios importantes

| Condición | Resultado |
|-----------|-----------|
| $\det(A) \neq 0$ | $A$ es invertible |
| $\det(A) = 0$ | $A$ es singular (no invertible) |
| $\det(A) \neq 0$ | Sistema $Ax = b$ tiene solución única |

## Aplicaciones geométricas

- **Área del paralelogramo** con lados $\vec{u}, \vec{v}$ en $\mathbb{R}^2$:
$$\text{Área} = |\det[\vec{u}, \vec{v}]|$$

- **Volumen del paralelepípedo** con aristas $\vec{u}, \vec{v}, \vec{w}$ en $\mathbb{R}^3$:
$$\text{Volumen} = |\det[\vec{u}, \vec{v}, \vec{w}]|$$
