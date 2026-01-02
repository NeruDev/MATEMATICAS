<!--
::METADATA::
type: solution
topic_id: cv-03-funciones-vectoriales
file_id: prob-33-solucion
problem_ref: Prob-33
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Marco TNB de la hélice

## Problema
Para $\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle$, encuentra los vectores $\mathbf{T}$, $\mathbf{N}$ y $\mathbf{B}$.

---

## Conceptos clave

| [Vector](../../../../glossary.md#vector) | Fórmula |
|--------|---------|
| **Tangente** | $\mathbf{T} = \frac{\mathbf{r}'}{\lVert \mathbf{r}' \rVert}$ |
| **Normal** | $\mathbf{N} = \frac{\mathbf{T}'}{\lVert \mathbf{T}' \rVert}$ |
| **Binormal** | $\mathbf{B} = \mathbf{T} \times \mathbf{N}$ |

---

## Solución

### Paso 1: Calcular r'(t) y su magnitud
$$\mathbf{r}'(t) = \langle -\sin t, \cos t, 1 \rangle$$

$$\lVert \mathbf{r}'(t) \rVert = \sqrt{\sin^2 t + \cos^2 t + 1} = \sqrt{2}$$

### Paso 2: Vector tangente unitario T
$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\lVert \mathbf{r}'(t) \rVert} = \frac{1}{\sqrt{2}}\langle -\sin t, \cos t, 1 \rangle$$

### Paso 3: Calcular T'(t) y su magnitud
$$\mathbf{T}'(t) = \frac{1}{\sqrt{2}}\langle -\cos t, -\sin t, 0 \rangle$$

$$\lVert \mathbf{T}'(t) \rVert = \frac{1}{\sqrt{2}}\sqrt{\cos^2 t + \sin^2 t + 0} = \frac{1}{\sqrt{2}}$$

### Paso 4: Vector normal principal N
$$\mathbf{N}(t) = \frac{\mathbf{T}'(t)}{\lVert \mathbf{T}'(t) \rVert} = \frac{\frac{1}{\sqrt{2}}\langle -\cos t, -\sin t, 0 \rangle}{\frac{1}{\sqrt{2}}}$$

$$\mathbf{N}(t) = \langle -\cos t, -\sin t, 0 \rangle$$

### Paso 5: Vector binormal B = T × N
$$\mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t) = \frac{1}{\sqrt{2}}\begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -\sin t & \cos t & 1 \\ -\cos t & -\sin t & 0 \end{vmatrix}$$

$$= \frac{1}{\sqrt{2}}\left[\mathbf{i}(0 - (-\sin t)) - \mathbf{j}(0 - (-\cos t)) + \mathbf{k}(\sin^2 t + \cos^2 t)\right]$$

$$= \frac{1}{\sqrt{2}}\langle \sin t, -\cos t, 1 \rangle$$

---

## Respuesta Final

$$\boxed{\mathbf{T}(t) = \frac{1}{\sqrt{2}}\langle -\sin t, \cos t, 1 \rangle}$$

$$\boxed{\mathbf{N}(t) = \langle -\cos t, -\sin t, 0 \rangle}$$

$$\boxed{\mathbf{B}(t) = \frac{1}{\sqrt{2}}\langle \sin t, -\cos t, 1 \rangle}$$

---

## Verificación de ortogonalidad

**T · N:**
$$\frac{1}{\sqrt{2}}(-\sin t)(-\cos t) + \frac{1}{\sqrt{2}}(\cos t)(-\sin t) + \frac{1}{\sqrt{2}}(1)(0) = 0 \checkmark$$

**T · B:**
$$\frac{1}{2}(-\sin t \cdot \sin t) + \frac{1}{2}(\cos t \cdot (-\cos t)) + \frac{1}{2}(1)(1) = \frac{1}{2}(-\sin^2 t - \cos^2 t + 1) = 0 \checkmark$$

**N · B:**
$$\frac{1}{\sqrt{2}}(-\cos t \cdot \sin t) + \frac{1}{\sqrt{2}}(-\sin t \cdot (-\cos t)) + 0 = 0 \checkmark$$

Los tres vectores son mutuamente ortogonales ✓
