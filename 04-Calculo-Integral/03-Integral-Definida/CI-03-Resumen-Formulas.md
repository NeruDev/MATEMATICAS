<!--
::METADATA::
type: cheatsheet
topic_id: ci-03-integral-definida
file_id: CI-03-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Resumen rápido — Integral Definida

## Definición (Suma de Riemann)

$$\int_a^b f(x)\,dx = \lim_{n\to\infty} \sum_{i=1}^{n} f(x_i^*) \Delta x$$

donde $\Delta x = \dfrac{b-a}{n}$ y $x_i^* \in [x_{i-1}, x_i]$

## Teorema Fundamental del Cálculo

### Parte 1 (TFC-1): Derivada de la función integral

$$\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$$

**Forma general ([regla de la cadena](../../glossary.md#regla-de-la-cadena)):**

$$\frac{d}{dx}\int_{g(x)}^{h(x)} f(t)\,dt = f(h(x)) \cdot h'(x) - f(g(x)) \cdot g'(x)$$

### Parte 2 (TFC-2): Evaluación de integrales

$$\int_a^b f(x)\,dx = F(b) - F(a) = \left[F(x)\right]_a^b$$

donde $F'(x) = f(x)$

## Propiedades de la integral definida

### Propiedades básicas

| Propiedad | Fórmula |
|-----------|---------|
| [Límites](../../glossary.md#limites) | $\int_a^b f(x)\,dx = -\int_b^a f(x)\,dx$ |
| Constante | $\int_a^b c\,dx = c(b-a)$ |
| [Linealidad](../../glossary.md#linealidad) | $\int_a^b [cf(x) + dg(x)]\,dx = c\int_a^b f(x)\,dx + d\int_a^b g(x)\,dx$ |

### Propiedad aditiva

$$\int_a^b f(x)\,dx + \int_b^c f(x)\,dx = \int_a^c f(x)\,dx$$

### Propiedades de comparación

Si $f(x) \leq g(x)$ en $[a,b]$:
$$\int_a^b f(x)\,dx \leq \int_a^b g(x)\,dx$$

Si $m \leq f(x) \leq M$ en $[a,b]$:
$$m(b-a) \leq \int_a^b f(x)\,dx \leq M(b-a)$$

## Funciones pares e impares

Sea $f$ continua en $[-a, a]$:

| Tipo | Propiedad | Integral |
|------|-----------|----------|
| Par | $f(-x) = f(x)$ | $\int_{-a}^{a} f(x)\,dx = 2\int_0^a f(x)\,dx$ |
| Impar | $f(-x) = -f(x)$ | $\int_{-a}^{a} f(x)\,dx = 0$ |

## Sustitución en integrales definidas

Si $u = g(x)$, entonces:
$$\int_a^b f(g(x)) \cdot g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du$$

**Importante:** Cambiar los límites de integración a valores de $u$.

## Valor promedio de una función

$$f_{\text{prom}} = \frac{1}{b-a}\int_a^b f(x)\,dx$$

## Teorema del valor medio para integrales

Si $f$ es continua en $[a,b]$, existe $c \in [a,b]$ [tal que](../../glossary.md#integral-definida).
Para desarrollo completo: [theory/CI-03-Teoria-Integral-Definida.md](theory/CI-03-Teoria-Integral-Definida.md)
file_id: CI-03-Resumen-Formulas
-->
