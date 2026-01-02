<!--
::METADATA::
type: solution
topic_id: cv-03-funciones-vectoriales
file_id: prob-28-solucion
problem_ref: Prob-28
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Curvatura de la hélice

## Problema
Encuentra la curvatura de la hélice $\mathbf{r}(t) = \langle 2\cos t, 2\sin t, t \rangle$.

---

## Conceptos clave

**Fórmula de curvatura:**
$$\kappa = \frac{\lVert \mathbf{r}'(t) \times \mathbf{r}''(t) \rVert}{\lVert \mathbf{r}'(t) \rVert^3}$$

---

## Solución

### Paso 1: Calcular la primera derivada
$$\mathbf{r}'(t) = \langle -2\sin t, 2\cos t, 1 \rangle$$

### Paso 2: Calcular la segunda derivada
$$\mathbf{r}''(t) = \langle -2\cos t, -2\sin t, 0 \rangle$$

### Paso 3: Calcular la magnitud de r'(t)
$$\lVert \mathbf{r}'(t) \rVert = \sqrt{(-2\sin t)^2 + (2\cos t)^2 + 1^2}$$
$$= \sqrt{4\sin^2 t + 4\cos^2 t + 1} = \sqrt{4(\sin^2 t + \cos^2 t) + 1} = \sqrt{4 + 1} = \sqrt{5}$$

### Paso 4: Calcular el producto cruz r' × r''
$$\mathbf{r}'(t) \times \mathbf{r}''(t) = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -2\sin t & 2\cos t & 1 \\ -2\cos t & -2\sin t & 0 \end{vmatrix}$$

Expandiendo:
$$= \mathbf{i}(2\cos t \cdot 0 - 1 \cdot (-2\sin t)) - \mathbf{j}((-2\sin t) \cdot 0 - 1 \cdot (-2\cos t)) + \mathbf{k}((-2\sin t)(-2\sin t) - (2\cos t)(-2\cos t))$$

$$= \mathbf{i}(2\sin t) - \mathbf{j}(2\cos t) + \mathbf{k}(4\sin^2 t + 4\cos^2 t)$$

$$= \langle 2\sin t, -2\cos t, 4 \rangle$$

### Paso 5: Calcular la magnitud del producto cruz
$$\lVert \mathbf{r}'(t) \times \mathbf{r}''(t) \rVert = \sqrt{(2\sin t)^2 + (-2\cos t)^2 + 4^2}$$
$$= \sqrt{4\sin^2 t + 4\cos^2 t + 16} = \sqrt{4 + 16} = \sqrt{20} = 2\sqrt{5}$$

### Paso 6: Aplicar la fórmula de curvatura
$$\kappa = \frac{2\sqrt{5}}{(\sqrt{5})^3} = \frac{2\sqrt{5}}{5\sqrt{5}} = \frac{2}{5}$$

---

## Respuesta Final
$$\boxed{\kappa = \frac{2}{5}}$$

La curvatura es **constante** (no depende de $t$).

---

## Verificación
La curvatura constante es característica de las hélices circulares. Para una hélice general $\mathbf{r}(t) = \langle a\cos t, a\sin t, bt \rangle$:
$$\kappa = \frac{a}{a^2 + b^2}$$

Con $a = 2$ y $b = 1$: $\kappa = \frac{2}{4 + 1} = \frac{2}{5}$ ✓
