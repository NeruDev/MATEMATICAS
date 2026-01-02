<!--
::METADATA::
type: cheatsheet
topic_id: ed-01-[edo](../../glossary.md#orden)
file_id: ED-01-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Resumen rápido — EDO de Primer Orden

## Forma general

$$\frac{dy}{dx} = f(x, y) \quad \text{o} \quad F\left(x, y, \frac{dy}{dx}\right) = 0$$

---

## Ecuaciones Separables

**Forma:** $\frac{dy}{dx} = f(x) \cdot g(y)$

**Solución:**
$$\int \frac{dy}{g(y)} = \int f(x)\,dx + C$$

---

## Ecuaciones Lineales de Primer Orden

**Forma estándar:** $\frac{dy}{dx} + P(x)y = Q(x)$

**[Factor integrante](../../glossary.md#solucion-general):**
$$y = \frac{1}{\mu(x)}\left[\int \mu(x) Q(x)\,dx + C\right]$$

---

## Ecuaciones Exactas

**Forma:** $M(x,y)\,dx + N(x,y)\,dy = 0$

**Condición de exactitud:**
$$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$$

**Solución:** Encontrar $F(x,y)$ [tal que](../../glossary.md#factor-integrante) |
|------|-------------------|
| $\frac{1}{N}\left(\frac{\partial M}{\partial y} - \frac{\partial N}{\partial x}\right) = f(x)$ | $\mu = e^{\int f(x)\,dx}$ |
| $\frac{1}{M}\left(\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y}\right) = g(y)$ | $\mu = e^{\int g(y)\,dy}$ |

---

## Ecuación de Bernoulli

**Forma:** $\frac{dy}{dx} + P(x)y = Q(x)y^n$, donde $n \neq 0, 1$

**[Sustitución](../../glossary.md#edo) lineal resultante:**
$$\frac{dv}{dx} + (1-n)P(x)v = (1-n)Q(x)$$

---

## Ecuaciones Homogéneas

**Forma:** $\frac{dy}{dx} = f\left(\frac{y}{x}\right)$

**[Sustitución](../../glossary.md#orden).
Para desarrollo completo: [theory/ED-01-Teoria-EDO-Primer-Orden.md](theory/ED-01-Teoria-EDO-Primer-Orden.md)
file_id: ED-01-Resumen-Formulas
-->
