<!--
::METADATA::
type: solution
topic_id: cv-04-multiplicadores-lagrange
file_id: prob-47-solucion
problem_ref: Prob-47
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Multiplicadores de Lagrange

## Problema

Usar el método de multiplicadores de Lagrange para encontrar los valores máximo y mínimo de:

$$f(x,y) = xy$$

sujeto a la restricción:

$$g(x,y) = x^2 + y^2 - 1 = 0$$

(es decir, sobre el círculo unitario $x^2 + y^2 = 1$)

---

## Conceptos clave

**Método de Multiplicadores de Lagrange:**

Para optimizar $f(x,y)$ sujeto a $g(x,y) = 0$, resolvemos el sistema:

$$\nabla f = \lambda \nabla g$$

donde $\lambda$ es el multiplicador de Lagrange.

Esto equivale a:
$$\begin{cases}
\frac{\partial f}{\partial x} = \lambda \frac{\partial g}{\partial x} \\
\frac{\partial f}{\partial y} = \lambda \frac{\partial g}{\partial y} \\
g(x,y) = 0
\end{cases}$$

---

## Solución

### Paso 1: Calcular los gradientes

**Gradiente de $f$:**
$$\nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right) = (y, x)$$

**Gradiente de $g$:**
$$\nabla g = \left( \frac{\partial g}{\partial x}, \frac{\partial g}{\partial y} \right) = (2x, 2y)$$

---

### Paso 2: Plantear el sistema de ecuaciones

De $\nabla f = \lambda \nabla g$:

$$\begin{cases}
y = \lambda \cdot 2x = 2\lambda x \quad \text{...(1)} \\
x = \lambda \cdot 2y = 2\lambda y \quad \text{...(2)} \\
x^2 + y^2 = 1 \quad \text{...(3)}
\end{cases}$$

---

### Paso 3: Resolver el sistema

**Estrategia:** Multiplicamos (1) por $y$ y (2) por $x$:

De (1): $y^2 = 2\lambda xy$

De (2): $x^2 = 2\lambda xy$

Igualando:
$$y^2 = x^2$$

$$y = \pm x$$

---

### Paso 4: Caso $y = x$

Sustituimos en la restricción (3):
$$x^2 + x^2 = 1$$
$$2x^2 = 1$$
$$x^2 = \frac{1}{2}$$
$$x = \pm \frac{1}{\sqrt{2}} = \pm \frac{\sqrt{2}}{2}$$

**Puntos críticos:**
$$P_1 = \left( \frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2} \right), \quad P_2 = \left( -\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2} \right)$$

**Encontrar $\lambda$:** De (1) con $y = x$:
$$x = 2\lambda x \Rightarrow \lambda = \frac{1}{2} \quad (\text{si } x \neq 0)$$

---

### Paso 5: Caso $y = -x$

Sustituimos en la restricción (3):
$$x^2 + (-x)^2 = 1$$
$$2x^2 = 1$$
$$x = \pm \frac{\sqrt{2}}{2}$$

**Puntos críticos:**
$$P_3 = \left( \frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2} \right), \quad P_4 = \left( -\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2} \right)$$

**Encontrar $\lambda$:** De (1) con $y = -x$:
$$-x = 2\lambda x \Rightarrow \lambda = -\frac{1}{2} \quad (\text{si } x \neq 0)$$

---

### Paso 6: Evaluar $f$ en los puntos críticos

**En $P_1 = \left( \frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2} \right)$:**
$$f(P_1) = \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{2}}{2} = \frac{2}{4} = \frac{1}{2}$$

**En $P_2 = \left( -\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2} \right)$:**
$$f(P_2) = \left( -\frac{\sqrt{2}}{2} \right) \cdot \left( -\frac{\sqrt{2}}{2} \right) = \frac{2}{4} = \frac{1}{2}$$

**En $P_3 = \left( \frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2} \right)$:**
$$f(P_3) = \frac{\sqrt{2}}{2} \cdot \left( -\frac{\sqrt{2}}{2} \right) = -\frac{2}{4} = -\frac{1}{2}$$

**En $P_4 = \left( -\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2} \right)$:**
$$f(P_4) = \left( -\frac{\sqrt{2}}{2} \right) \cdot \frac{\sqrt{2}}{2} = -\frac{2}{4} = -\frac{1}{2}$$

---

### Paso 7: Identificar máximos y mínimos

| Punto | Coordenadas | $f(x,y)$ | $\lambda$ |
|-------|-------------|----------|-----------|
| $P_1$ | $\left( \frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2} \right)$ | $\frac{1}{2}$ | $\frac{1}{2}$ |
| $P_2$ | $\left( -\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2} \right)$ | $\frac{1}{2}$ | $\frac{1}{2}$ |
| $P_3$ | $\left( \frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2} \right)$ | $-\frac{1}{2}$ | $-\frac{1}{2}$ |
| $P_4$ | $\left( -\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2} \right)$ | $-\frac{1}{2}$ | $-\frac{1}{2}$ |

---

## Respuesta Final

$$\boxed{\text{Máximo: } f = \frac{1}{2} \text{ en } \left( \pm\frac{\sqrt{2}}{2}, \pm\frac{\sqrt{2}}{2} \right) \text{ con signos iguales}}$$

$$\boxed{\text{Mínimo: } f = -\frac{1}{2} \text{ en } \left( \pm\frac{\sqrt{2}}{2}, \mp\frac{\sqrt{2}}{2} \right) \text{ con signos opuestos}}$$

---

## Verificación

**Verificación paramétrica:**

Parametrizamos el círculo unitario: $x = \cos\theta$, $y = \sin\theta$

$$f(\theta) = \cos\theta \cdot \sin\theta = \frac{1}{2}\sin(2\theta)$$

**Máximo:** $f = \frac{1}{2}$ cuando $\sin(2\theta) = 1$, es decir, $2\theta = \frac{\pi}{2}$, $\theta = \frac{\pi}{4}$
- $x = \cos\frac{\pi}{4} = \frac{\sqrt{2}}{2}$, $y = \sin\frac{\pi}{4} = \frac{\sqrt{2}}{2}$ ✓

**Mínimo:** $f = -\frac{1}{2}$ cuando $\sin(2\theta) = -1$, es decir, $\theta = \frac{3\pi}{4}$
- $x = \cos\frac{3\pi}{4} = -\frac{\sqrt{2}}{2}$, $y = \sin\frac{3\pi}{4} = \frac{\sqrt{2}}{2}$ ✓

**Interpretación del multiplicador $\lambda$:**

El multiplicador $\lambda = \frac{df^*}{dc}$ representa la tasa de cambio del valor óptimo respecto al radio del círculo. Si la restricción fuera $x^2 + y^2 = c$, entonces $\lambda$ indica cuánto cambia el máximo/mínimo por unidad de cambio en $c$.
