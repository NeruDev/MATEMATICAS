<!--
::METADATA::
type: solution
topic_id: cd-01-limites
file_id: prob-24-solucion-metodo
problem_ref: [Prob-24]
method: limite-trigonometrico-fundamental
status: stable
audience: student
-->

# Solución: Límite seno fundamental

**Método aplicado:** [Límite](../../../../glossary.md#límite) trigonométrico fundamental $\lim_{u \to 0} \frac{\sin u}{u} = 1$

**Paso 1: Reescribir usando el límite fundamental**
Hacemos $u = 5x$. Cuando $x \to 0$, también $u \to 0$.

$$\lim_{x \to 0} \frac{\sin 5x}{x}$$

**Paso 2: Multiplicar y dividir para obtener la forma estándar**
$$= \lim_{x \to 0} \frac{\sin 5x}{5x} \cdot 5$$

**Paso 3: Aplicar el límite fundamental**
$$= 5 \cdot \lim_{x \to 0} \frac{\sin 5x}{5x} = 5 \cdot 1 = 5$$

**Respuesta:**

$$\lim_{x \to 0} \frac{\sin 5x}{x} = 5$$
