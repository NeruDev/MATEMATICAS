<!--
::METADATA::
type: cheatsheet
topic_id: ci-05-integrales-impropias
file_id: CI-05-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Resumen rápido — Integrales Impropias

## Tipo I: Límites infinitos

### Límite superior infinito

$$\int_a^\infty f(x)\,dx = \lim_{t\to\infty} \int_a^t f(x)\,dx$$

### Límite inferior infinito

$$\int_{-\infty}^b f(x)\,dx = \lim_{t\to-\infty} \int_t^b f(x)\,dx$$

### Ambos límites infinitos

$$\int_{-\infty}^\infty f(x)\,dx = \int_{-\infty}^c f(x)\,dx + \int_c^\infty f(x)\,dx$$

**Nota:** Ambas integrales deben converger independientemente.

## Tipo II: Discontinuidades

### Discontinuidad en $a$ (límite inferior)

$$\int_a^b f(x)\,dx = \lim_{t\to a^+} \int_t^b f(x)\,dx$$

### Discontinuidad en $b$ (límite superior)

$$\int_a^b f(x)\,dx = \lim_{t\to b^-} \int_a^t f(x)\,dx$$

### Discontinuidad en $c \in (a,b)$

$$\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx$$

**Nota:** Ambas integrales deben converger independientemente.

## Integrales p (Referencia fundamental)

### En $[1, \infty)$

$$\int_1^\infty \frac{1}{x^p}\,dx = \begin{cases} \dfrac{1}{p-1} & \text{si } p > 1 \text{ (converge)} \\ \text{diverge} & \text{si } p \leq 1 \end{cases}$$

### En $(0, 1]$

$$\int_0^1 \frac{1}{x^p}\,dx = \begin{cases} \dfrac{1}{1-p} & \text{si } p < 1 \text{ (converge)} \\ \text{diverge} & \text{si } p \geq 1 \end{cases}$$

## Criterios de convergencia

### Criterio de comparación directa

Si $0 \leq f(x) \leq g(x)$ para todo $x \geq a$:

| Si... | Entonces... |
|-------|-------------|
| $\int_a^\infty g(x)\,dx$ converge | $\int_a^\infty f(x)\,dx$ converge |
| $\int_a^\infty f(x)\,dx$ diverge | $\int_a^\infty g(x)\,dx$ diverge |

### Criterio de comparación por límite

Si $f(x), g(x) > 0$ y $\lim_{x\to\infty} \dfrac{f(x)}{g(x)} = L$:

| Valor de $L$ | Conclusión |
|--------------|------------|
| $0 < L < \infty$ | Ambas convergen o ambas divergen |
| $L = 0$ | Si $\int g$ converge, entonces $\int f$ converge |
| $L = \infty$ | Si $\int g$ diverge, entonces $\int f$ diverge |

## Integrales impropias notables

| Integral | Valor | Condición |
|----------|-------|-----------|
| $\int_0^\infty e^{-x}\,dx$ | $1$ | Converge |
| $\int_0^\infty e^{-ax}\,dx$ | $\dfrac{1}{a}$ | $a > 0$ |
| $\int_0^\infty x^n e^{-x}\,dx$ | $n!$ | $n \in \mathbb{N}$ |
| $\int_0^\infty e^{-x^2}\,dx$ | $\dfrac{\sqrt{\pi}}{2}$ | Integral de Gauss |
| $\int_{-\infty}^\infty e^{-x^2}\,dx$ | $\sqrt{\pi}$ | Integral gaussiana |
| $\int_1^\infty \dfrac{1}{x^2}\,dx$ | $1$ | Converge |
| $\int_1^\infty \dfrac{1}{x}\,dx$ | $\infty$ | Diverge |

## Comportamiento asintótico

Para determinar [convergencia](../../glossary.md#integrales-impropias).
Para desarrollo completo: [theory/CI-05-Teoria-Integrales-Impropias.md](theory/CI-05-Teoria-Integrales-Impropias.md)
file_id: CI-05-Resumen-Formulas
-->
