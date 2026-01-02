<!--
::METADATA::
type: solution
topic_id: cv-04-limites-varias-variables
file_id: prob-09-solucion
problem_ref: Prob-09
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../glossary.md)

---

# Solución: Demostración de que un Límite No Existe

## Problema

Demostrar que el siguiente [límite](../../../../glossary.md#limite) no existe:

$$\lim_{(x,y) \to (0,0)} \frac{xy}{x^2 + y^2}$$

---

## Conceptos clave

**Criterio de inexistencia de [límite](../../../../glossary.md#limite):** Si al aproximarnos al punto $(a,b)$ por diferentes trayectorias obtenemos valores distintos, entonces el límite no existe.

**Trayectorias comunes a evaluar:**
- Ejes coordenados: $y = 0$, $x = 0$
- Rectas por el origen: $y = mx$
- Parábolas: $y = x^2$, $x = y^2$

---

## Solución

### Paso 1: Análisis por la trayectoria $y = 0$ (eje $x$)

Sustituimos $y = 0$ en la [función](../../../../glossary.md#funcion):

$$f(x, 0) = \frac{x \cdot 0}{x^2 + 0^2} = \frac{0}{x^2} = 0$$

Evaluamos el límite:

$$\lim_{x \to 0} f(x, 0) = \lim_{x \to 0} 0 = 0$$

**Por el eje $x$, el límite es $\mathbf{0}$.**

---

### Paso 2: Análisis por la trayectoria $x = 0$ (eje $y$)

Sustituimos $x = 0$ en la [función](../../../../glossary.md#funcion):

$$f(0, y) = \frac{0 \cdot y}{0^2 + y^2} = \frac{0}{y^2} = 0$$

Evaluamos el límite:

$$\lim_{y \to 0} f(0, y) = \lim_{y \to 0} 0 = 0$$

**Por el eje $y$, el límite es $\mathbf{0}$.**

---

### Paso 3: Análisis por la trayectoria $y = x$

Sustituimos $y = x$ en la función:

$$f(x, x) = \frac{x \cdot x}{x^2 + x^2} = \frac{x^2}{2x^2} = \frac{1}{2}$$

Evaluamos el límite:

$$\lim_{x \to 0} f(x, x) = \lim_{x \to 0} \frac{1}{2} = \frac{1}{2}$$

**Por la recta $y = x$, el límite es $\mathbf{\frac{1}{2}}$.**

---

### Paso 4: Análisis por la trayectoria general $y = mx$

Para confirmar el resultado, evaluamos a lo largo de cualquier recta $y = mx$ donde $m \neq 0$:

$$f(x, mx) = \frac{x \cdot mx}{x^2 + (mx)^2} = \frac{mx^2}{x^2 + m^2x^2} = \frac{mx^2}{x^2(1 + m^2)} = \frac{m}{1 + m^2}$$

Evaluamos el límite:

$$\lim_{x \to 0} f(x, mx) = \frac{m}{1 + m^2}$$

**El límite depende del valor de $m$:**

| Trayectoria | Valor de $m$ | Límite |
|-------------|--------------|--------|
| $y = 0$ | $m = 0$ | $0$ |
| $y = x$ | $m = 1$ | $\frac{1}{2}$ |
| $y = -x$ | $m = -1$ | $-\frac{1}{2}$ |
| $y = 2x$ | $m = 2$ | $\frac{2}{5}$ |

---

### Paso 5: Conclusión

Hemos encontrado que:

- Por $y = 0$: límite $= 0$
- Por $y = x$: límite $= \frac{1}{2}$
- Por $y = -x$: límite $= -\frac{1}{2}$

Como obtenemos **valores diferentes** al aproximarnos al origen por distintas trayectorias, concluimos que el límite no existe.

---

## Respuesta Final

$$\boxed{\text{El límite } \lim_{(x,y) \to (0,0)} \frac{xy}{x^2 + y^2} \text{ no existe}}$$

---

## Verificación

**Verificación geométrica:** La función $f(x,y) = \frac{xy}{x^2+y^2}$ en coordenadas polares es:

$$f(r\cos\theta, r\sin\theta) = \frac{r^2\cos\theta\sin\theta}{r^2} = \cos\theta\sin\theta = \frac{\sin(2\theta)}{2}$$

El valor depende únicamente de $\theta$ (la dirección), no de $r$ (la distancia al origen). Esto confirma que al acercarnos al origen desde diferentes direcciones obtenemos valores distintos, por lo tanto el límite no existe.

**Rango de valores:** Según la dirección $\theta$, el valor oscila entre $-\frac{1}{2}$ y $\frac{1}{2}$.
