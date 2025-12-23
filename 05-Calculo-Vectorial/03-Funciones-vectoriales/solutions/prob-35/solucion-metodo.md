<!--
::METADATA::
type: solution
topic_id: cv-03-funciones-vectoriales
file_id: prob-35-solucion
problem_ref: Prob-35
status: stable
audience: student
-->

# Solución: Torsión de la hélice

## Problema
Encuentra la torsión de la hélice $\mathbf{r}(t) = \langle 3\cos t, 3\sin t, 4t \rangle$.

---

## Conceptos clave

**Fórmula de torsión:**
$$\tau = \frac{(\mathbf{r}' \times \mathbf{r}'') \cdot \mathbf{r}'''}{\lVert \mathbf{r}' \times \mathbf{r}'' \rVert^2}$$

---

## Solución

### Paso 1: Calcular las derivadas
$$\mathbf{r}'(t) = \langle -3\sin t, 3\cos t, 4 \rangle$$

$$\mathbf{r}''(t) = \langle -3\cos t, -3\sin t, 0 \rangle$$

$$\mathbf{r}'''(t) = \langle 3\sin t, -3\cos t, 0 \rangle$$

### Paso 2: Calcular r' × r''
$$\mathbf{r}' \times \mathbf{r}'' = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -3\sin t & 3\cos t & 4 \\ -3\cos t & -3\sin t & 0 \end{vmatrix}$$

$$= \mathbf{i}(3\cos t \cdot 0 - 4 \cdot (-3\sin t)) - \mathbf{j}((-3\sin t) \cdot 0 - 4 \cdot (-3\cos t)) + \mathbf{k}((-3\sin t)(-3\sin t) - (3\cos t)(-3\cos t))$$

$$= \mathbf{i}(12\sin t) - \mathbf{j}(12\cos t) + \mathbf{k}(9\sin^2 t + 9\cos^2 t)$$

$$= \langle 12\sin t, -12\cos t, 9 \rangle$$

### Paso 3: Calcular ||r' × r''||²
$$\lVert \mathbf{r}' \times \mathbf{r}'' \rVert^2 = (12\sin t)^2 + (-12\cos t)^2 + 9^2$$
$$= 144\sin^2 t + 144\cos^2 t + 81 = 144 + 81 = 225$$

### Paso 4: Calcular (r' × r'') · r'''
$$(\mathbf{r}' \times \mathbf{r}'') \cdot \mathbf{r}''' = \langle 12\sin t, -12\cos t, 9 \rangle \cdot \langle 3\sin t, -3\cos t, 0 \rangle$$

$$= 12\sin t \cdot 3\sin t + (-12\cos t)(-3\cos t) + 9 \cdot 0$$

$$= 36\sin^2 t + 36\cos^2 t = 36$$

### Paso 5: Aplicar la fórmula de torsión
$$\tau = \frac{36}{225} = \frac{4}{25}$$

---

## Respuesta Final
$$\boxed{\tau = \frac{4}{25}}$$

La torsión es **constante** (característica de las hélices).

---

## Verificación
Para una hélice general $\mathbf{r}(t) = \langle a\cos t, a\sin t, bt \rangle$:
$$\tau = \frac{b}{a^2 + b^2}$$

Con $a = 3$ y $b = 4$: $\tau = \frac{4}{9 + 16} = \frac{4}{25}$ ✓

---

## Nota
La torsión positiva indica que la hélice gira en sentido antihorario (dextrógira) cuando se ve desde arriba.
