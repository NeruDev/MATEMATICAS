<!--
HUMANO:
Soluciones representativas de [integral definida](../../..](../../../glossary.md)#integral-definida).

IA:
Desarrollo paso a paso de problemas selectos.

---
content_type: solutions
format: step_by_step
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Soluciones de Integral Definida

---

## Problema 2
**Enunciado:** $\displaystyle\int_1^4 \sqrt{x} \, dx$

**Solución:**
$$\int_1^4 x^{1/2} \, dx = \left.\frac{x^{3/2}}{3/2}\right|_1^4 = \frac{2}{3}\left[x^{3/2}\right]_1^4$$

$$= \frac{2}{3}(4^{3/2} - 1^{3/2}) = \frac{2}{3}(8 - 1) = \frac{14}{3}$$

---

## Problema 8
**Enunciado:** $\displaystyle\int_1^2 \frac{x^3 + 1}{x^2} \, dx$

**Solución:**
Simplificamos:
$$\frac{x^3 + 1}{x^2} = x + x^{-2}$$

$$\int_1^2 \left(x + x^{-2}\right)dx = \left[\frac{x^2}{2} - \frac{1}{x}\right]_1^2$$

$$= \left(\frac{4}{2} - \frac{1}{2}\right) - \left(\frac{1}{2} - 1\right) = \frac{3}{2} - \left(-\frac{1}{2}\right) = 2$$

---

## Problema 14
**Enunciado:** Hallar $\displaystyle\frac{d}{dx}\int_0^{x^2} \cos t \, dt$

**Solución:**
Aplicamos la regla de Leibniz. Sea $u = x^2$:
$$\frac{d}{dx}\int_0^{x^2} \cos t \, dt = \cos(x^2) \cdot \frac{d}{dx}(x^2) = \cos(x^2) \cdot 2x = 2x\cos(x^2)$$

---

## Problema 16
**Enunciado:** Hallar $\displaystyle\frac{d}{dx}\int_{\sqrt{x}}^{x} t^3 \, dt$

**Solución:**
Aplicamos la fórmula para ambos [límites](../../..](../../../glossary.md)#limites) variables:
$$\frac{d}{dx}\int_{h(x)}^{g(x)} f(t)\,dt = f(g(x))g'(x) - f(h(x))h'(x)$$

Con $f(t) = t^3$, $g(x) = x$, $h(x) = \sqrt{x}$:

$$= x^3 \cdot 1 - (\sqrt{x})^3 \cdot \frac{1}{2\sqrt{x}}$$

$$= x^3 - x^{3/2} \cdot \frac{1}{2}x^{-1/2} = x^3 - \frac{x}{2}$$

---

## Problema 22
**Enunciado:** $\displaystyle\int_0^4 \frac{x}{\sqrt{x^2+9}} \, dx$

**Solución:**
Sea $u = x^2 + 9 \Rightarrow du = 2x\,dx \Rightarrow x\,dx = \frac{1}{2}du$

**Cambio de [límites](../../..](../../../glossary.md)#limites):**
- $x = 0 \Rightarrow u = 9$
- $x = 4 \Rightarrow u = 25$

$$\int_9^{25} \frac{1}{2\sqrt{u}} \, du = \frac{1}{2}\int_9^{25} u^{-1/2}\,du = \frac{1}{2}\left[2u^{1/2}\right]_9^{25}$$

$$= \left[\sqrt{u}\right]_9^{25} = 5 - 3 = 2$$

---

## Problema 24
**Enunciado:** $\displaystyle\int_1^e \frac{\ln x}{x} \, dx$

**Solución:**
Sea $u = \ln x \Rightarrow du = \frac{1}{x}dx$

**Cambio de límites:**
- $x = 1 \Rightarrow u = 0$
- $x = e \Rightarrow u = 1$

$$\int_0^1 u\,du = \left.\frac{u^2}{2}\right|_0^1 = \frac{1}{2}$$

---

## Problema 32
**Enunciado:** $\displaystyle\int_{-2}^{2} (x^3 + x^2) \, dx$

**Solución:**
Separamos en parte impar y par:
- $x^3$ es impar $\Rightarrow \int_{-2}^2 x^3\,dx = 0$
- $x^2$ es par $\Rightarrow \int_{-2}^2 x^2\,dx = 2\int_0^2 x^2\,dx$

$$\int_{-2}^{2} (x^3 + x^2)\,dx = 0 + 2\int_0^2 x^2\,dx = 2\left.\frac{x^3}{3}\right|_0^2 = 2 \cdot \frac{8}{3} = \frac{16}{3}$$

---

## Problema 37
**Enunciado:** Calcular el área entre $y = x^2$ y $y = x$ para $0 \leq x \leq 1$.

**Solución:**
En $[0,1]$: $x \geq x^2$, así que $x$ está arriba.

$$\text{Área} = \int_0^1 (x - x^2)\,dx = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1$$

$$= \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$$

---

## Problema 40
**Enunciado:** Calcular $\displaystyle\int_0^1 |2x - 1| \, dx$

**Solución:**
$|2x - 1| = 0$ cuando $x = \frac{1}{2}$.

- Para $x < \frac{1}{2}$: $|2x-1| = 1 - 2x$
- Para $x > \frac{1}{2}$: $|2x-1| = 2x - 1$

$$\int_0^1 |2x-1|\,dx = \int_0^{1/2} (1-2x)\,dx + \int_{1/2}^1 (2x-1)\,dx$$

$$= \left[x - x^2\right]_0^{1/2} + \left[x^2 - x\right]_{1/2}^1$$

$$= \left(\frac{1}{2} - \frac{1}{4}\right) - 0 + \left(1-1\right) - \left(\frac{1}{4} - \frac{1}{2}\right)$$

$$= \frac{1}{4} + 0 - \left(-\frac{1}{4}\right) = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}$$

---

## Problema 41
**Enunciado:** Si $\displaystyle\int_0^a x^2 \, dx = 8$, hallar $a$.

**Solución:**
$$\int_0^a x^2\,dx = \left.\frac{x^3}{3}\right|_0^a = \frac{a^3}{3} = 8$$

$$a^3 = 24 \Rightarrow a = \sqrt[3]{24} = 2\sqrt[3]{3}$$
