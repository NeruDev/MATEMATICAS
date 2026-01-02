<!--
::METADATA::
type: solution
topic_id: cv-03-funciones-vectoriales
file_id: prob-38-solucion
problem_ref: Prob-38
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../glossary.md)

---

# Solución: Componentes tangencial y normal de la aceleración

## Problema
Para el movimiento $\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle$:
a) Calcula $\mathbf{v}(t)$ y $\mathbf{a}(t)$
b) Encuentra las componentes $a_T$ y $a_N$

---

## Conceptos clave

| Componente | Fórmula |
|------------|---------|
| **Tangencial** | $a_T = \frac{\mathbf{v} \cdot \mathbf{a}}{\lVert \mathbf{v} \rVert}$ |
| **Normal** | $a_N = \frac{\lVert \mathbf{v} \times \mathbf{a} \rVert}{\lVert \mathbf{v} \rVert}$ |

---

## Solución

### Parte a): Velocidad y aceleración

**Velocidad:**
$$\mathbf{v}(t) = \mathbf{r}'(t) = \langle -\sin t, \cos t, 1 \rangle$$

**Aceleración:**
$$\mathbf{a}(t) = \mathbf{r}''(t) = \langle -\cos t, -\sin t, 0 \rangle$$

### Parte b): Componentes de la aceleración

#### Paso 1: Calcular ||v||
$$\lVert \mathbf{v} \rVert = \sqrt{\sin^2 t + \cos^2 t + 1} = \sqrt{2}$$

#### Paso 2: Calcular v · a
$$\mathbf{v} \cdot \mathbf{a} = (-\sin t)(-\cos t) + (\cos t)(-\sin t) + (1)(0)$$
$$= \sin t \cos t - \sin t \cos t + 0 = 0$$

#### Paso 3: Componente tangencial
$$a_T = \frac{\mathbf{v} \cdot \mathbf{a}}{\lVert \mathbf{v} \rVert} = \frac{0}{\sqrt{2}} = 0$$

#### Paso 4: Calcular v × a
$$\mathbf{v} \times \mathbf{a} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -\sin t & \cos t & 1 \\ -\cos t & -\sin t & 0 \end{vmatrix}$$

$$= \mathbf{i}(\cos t \cdot 0 - 1 \cdot (-\sin t)) - \mathbf{j}((-\sin t) \cdot 0 - 1 \cdot (-\cos t)) + \mathbf{k}((-\sin t)(-\sin t) - (\cos t)(-\cos t))$$

$$= \langle \sin t, -\cos t, \sin^2 t + \cos^2 t \rangle = \langle \sin t, -\cos t, 1 \rangle$$

#### Paso 5: Calcular ||v × a||
$$\lVert \mathbf{v} \times \mathbf{a} \rVert = \sqrt{\sin^2 t + \cos^2 t + 1} = \sqrt{2}$$

#### Paso 6: Componente normal
$$a_N = \frac{\lVert \mathbf{v} \times \mathbf{a} \rVert}{\lVert \mathbf{v} \rVert} = \frac{\sqrt{2}}{\sqrt{2}} = 1$$

---

## Respuesta Final

$$\boxed{\mathbf{v}(t) = \langle -\sin t, \cos t, 1 \rangle}$$
$$\boxed{\mathbf{a}(t) = \langle -\cos t, -\sin t, 0 \rangle}$$
$$\boxed{a_T = 0, \quad a_N = 1}$$

---

## Interpretación física
- **$a_T = 0$**: La rapidez es constante ($\lVert\mathbf{v}\rVert = \sqrt{2}$ no cambia).
- **$a_N = 1$**: Toda la aceleración es centrípeta, cambiando solo la dirección del movimiento.

Esto es característico del **movimiento circular uniforme** en la proyección al plano $xy$, combinado con movimiento rectilíneo uniforme en $z$.
