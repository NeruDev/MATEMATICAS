<!--
::METADATA::
type: solution
topic_id: cv-01-vectores-espacio
file_id: prob-25-solucion
problem_ref: Prob-25
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Triple Producto Escalar mediante Determinante

## Problema

Calcular el triple producto escalar $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})$ donde:
- $\mathbf{u} = \langle 1, 2, 3 \rangle$
- $\mathbf{v} = \langle 2, -1, 1 \rangle$
- $\mathbf{w} = \langle 3, 1, -2 \rangle$

---

## Conceptos clave

**Triple producto escalar:**
$$\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = \begin{vmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{vmatrix}$$

**Expansión por cofactores (primera fila):**
$$\det(A) = a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13}$$

**Interpretación geométrica:**
El valor absoluto del triple producto escalar representa el volumen del paralelepípedo formado por los tres vectores.

---

## Solución

### Paso 1: Plantear el determinante 3×3

$$\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = \begin{vmatrix} 1 & 2 & 3 \\ 2 & -1 & 1 \\ 3 & 1 & -2 \end{vmatrix}$$

### Paso 2: Expansión por cofactores de la primera fila

$$= 1 \cdot C_{11} + 2 \cdot C_{12} + 3 \cdot C_{13}$$

Donde los cofactores son:

$$C_{11} = (+1) \begin{vmatrix} -1 & 1 \\ 1 & -2 \end{vmatrix}$$

$$C_{12} = (-1) \begin{vmatrix} 2 & 1 \\ 3 & -2 \end{vmatrix}$$

$$C_{13} = (+1) \begin{vmatrix} 2 & -1 \\ 3 & 1 \end{vmatrix}$$

### Paso 3: Calcular cada menor 2×2

**[Menor](../../../..](../../../../glossary.md)#menor) $M_{11}$:**
$$\begin{vmatrix} -1 & 1 \\ 1 & -2 \end{vmatrix} = (-1)(-2) - (1)(1) = 2 - 1 = 1$$

**[Menor](../../../..](../../../../glossary.md)#menor) $M_{12}$:**
$$\begin{vmatrix} 2 & 1 \\ 3 & -2 \end{vmatrix} = (2)(-2) - (1)(3) = -4 - 3 = -7$$

**Menor $M_{13}$:**
$$\begin{vmatrix} 2 & -1 \\ 3 & 1 \end{vmatrix} = (2)(1) - (-1)(3) = 2 + 3 = 5$$

### Paso 4: Calcular los cofactores

$$C_{11} = (+1)(1) = 1$$

$$C_{12} = (-1)(-7) = 7$$

$$C_{13} = (+1)(5) = 5$$

### Paso 5: Calcular el determinante final

$$\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = 1(1) + 2(7) + 3(5)$$

$$= 1 + 14 + 15$$

$$= 30$$

---

## Respuesta Final

$$\boxed{\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = 30}$$

---

## Interpretación Geométrica

El triple producto escalar $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = 30$ tiene las siguientes interpretaciones:

1. **Volumen del paralelepípedo:** El volumen del paralelepípedo formado por $\mathbf{u}$, $\mathbf{v}$ y $\mathbf{w}$ es:
   $$V = |\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})| = |30| = 30 \text{ unidades cúbicas}$$

2. **Orientación:** Como el resultado es positivo ($30 > 0$), los vectores forman un sistema **dextrógiro** (regla de la mano derecha).

3. **Coplanaridad:** Si el triple producto escalar fuera cero, los vectores serían coplanares. Como $30 \neq 0$, los vectores **no son coplanares** y definen un paralelepípedo de volumen no nulo.

---

## Verificación: Método Alternativo

Calculemos primero $\mathbf{v} \times \mathbf{w}$ y luego el producto punto:

$$\mathbf{v} \times \mathbf{w} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 2 & -1 & 1 \\ 3 & 1 & -2 \end{vmatrix}$$

$$= \mathbf{i}[(-1)(-2) - (1)(1)] - \mathbf{j}[(2)(-2) - (1)(3)] + \mathbf{k}[(2)(1) - (-1)(3)]$$

$$= \mathbf{i}[2 - 1] - \mathbf{j}[-4 - 3] + \mathbf{k}[2 + 3]$$

$$= \mathbf{i}(1) - \mathbf{j}(-7) + \mathbf{k}(5)$$

$$= \langle 1, 7, 5 \rangle$$

Ahora calculamos el producto punto:

$$\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = \langle 1, 2, 3 \rangle \cdot \langle 1, 7, 5 \rangle$$

$$= (1)(1) + (2)(7) + (3)(5)$$

$$= 1 + 14 + 15 = 30 \checkmark$$
