<!--
::METADATA::
type: solution
topic_id: cv-03-funciones-vectoriales
file_id: prob-41-solucion
problem_ref: Prob-41
status: stable
audience: student
-->

# Solución: Movimiento de proyectil

## Problema
Un proyectil se lanza con velocidad inicial $\mathbf{v}_0 = \langle 50, 50\sqrt{3} \rangle$ m/s. Con $g = 10$ m/s²:
a) Encuentra la ecuación de posición
b) ¿Cuál es la altura máxima?
c) ¿Cuál es el alcance horizontal?

---

## Conceptos clave

**Ecuaciones del movimiento:**
$$\mathbf{a}(t) = \langle 0, -g \rangle$$
$$\mathbf{v}(t) = \mathbf{v}_0 + \mathbf{a}t = \langle v_{0x}, v_{0y} - gt \rangle$$
$$\mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v}_0 t + \frac{1}{2}\mathbf{a}t^2$$

---

## Solución

### Datos iniciales
- $v_{0x} = 50$ m/s
- $v_{0y} = 50\sqrt{3}$ m/s
- $g = 10$ m/s²
- $\mathbf{r}_0 = \langle 0, 0 \rangle$ (lanzamiento desde el origen)

### Parte a): Ecuación de posición

$$\mathbf{r}(t) = \langle v_{0x}t, v_{0y}t - \frac{1}{2}gt^2 \rangle$$

$$\mathbf{r}(t) = \langle 50t, 50\sqrt{3}t - 5t^2 \rangle$$

En forma escalar:
$$x(t) = 50t$$
$$y(t) = 50\sqrt{3}t - 5t^2$$

### Parte b): Altura máxima

La altura máxima ocurre cuando $v_y = 0$:
$$v_y(t) = v_{0y} - gt = 50\sqrt{3} - 10t = 0$$
$$t_{max} = 5\sqrt{3} \text{ s}$$

Sustituyendo en $y(t)$:
$$y_{max} = 50\sqrt{3}(5\sqrt{3}) - 5(5\sqrt{3})^2$$
$$= 50 \cdot 3 \cdot 5 - 5 \cdot 75$$
$$= 750 - 375 = 375 \text{ m}$$

### Parte c): Alcance horizontal

El proyectil toca el suelo cuando $y(t) = 0$:
$$50\sqrt{3}t - 5t^2 = 0$$
$$5t(10\sqrt{3} - t) = 0$$
$$t = 0 \text{ (inicial) o } t = 10\sqrt{3} \text{ s (aterrizaje)}$$

El alcance es:
$$x_{alcance} = 50 \cdot 10\sqrt{3} = 500\sqrt{3} \approx 866 \text{ m}$$

---

## Respuesta Final

$$\boxed{\mathbf{r}(t) = \langle 50t, 50\sqrt{3}t - 5t^2 \rangle \text{ m}}$$

$$\boxed{h_{max} = 375 \text{ m}}$$

$$\boxed{R = 500\sqrt{3} \approx 866 \text{ m}}$$

---

## Verificación

**Ángulo de lanzamiento:**
$$\tan\theta = \frac{v_{0y}}{v_{0x}} = \frac{50\sqrt{3}}{50} = \sqrt{3} \Rightarrow \theta = 60°$$

**Fórmulas clásicas:**
$$h_{max} = \frac{v_0^2 \sin^2\theta}{2g} = \frac{(100)^2 \cdot ({\sqrt{3}/2})^2}{2 \cdot 10} = \frac{10000 \cdot 0.75}{20} = 375 \text{ m} \checkmark$$

$$R = \frac{v_0^2 \sin(2\theta)}{g} = \frac{10000 \cdot \sin 120°}{10} = 1000 \cdot \frac{\sqrt{3}}{2} = 500\sqrt{3} \text{ m} \checkmark$$
