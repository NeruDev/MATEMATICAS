<!--
::METADATA::
type: cheatsheet
topic_id: fun-06-geometria-analitica
file_id: FUN-06-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

---

# Resumen rápido — Geometría Analítica

## Fórmulas básicas

**Distancia entre dos puntos:**
$$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$$

**Punto medio:**
$$M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$$

**Pendiente de una recta:**
$$m = \frac{y_2-y_1}{x_2-x_1}$$

## Ecuaciones de la recta

| Forma | Ecuación |
|-------|----------|
| Punto-pendiente | $y - y_1 = m(x - x_1)$ |
| Pendiente-ordenada | $y = mx + b$ |
| General | $Ax + By + C = 0$ |

**Paralelas:** $m_1 = m_2$
**Perpendiculares:** $m_1 \cdot m_2 = -1$

**Distancia punto-recta:**
$$d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}$$

## Circunferencia

**Canónica:** $(x-h)^2 + (y-k)^2 = r^2$
- Centro: $(h, k)$
- Radio: $r$

**General:** $x^2 + y^2 + Dx + Ey + F = 0$
- Centro: $\left(-\frac{D}{2}, -\frac{E}{2}\right)$
- Radio: $r = \sqrt{\frac{D^2+E^2}{4} - F}$

## Parábola

| Orientación | Ecuación | Foco | Directriz |
|-------------|----------|------|-----------|
| Vertical ↑ | $(x-h)^2 = 4p(y-k)$ | $(h, k+p)$ | $y = k-p$ |
| Vertical ↓ | $(x-h)^2 = -4p(y-k)$ | $(h, k-p)$ | $y = k+p$ |
| Horizontal → | $(y-k)^2 = 4p(x-h)$ | $(h+p, k)$ | $x = h-p$ |
| Horizontal ← | $(y-k)^2 = -4p(x-h)$ | $(h-p, k)$ | $x = h+p$ |

## Elipse

$$\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1$$

- Centro: $(h, k)$
- Semieje mayor: $a$ (si $a > b$)
- Semieje [menor](../..](../../glossary.md)#menor): $b$
- Distancia focal: $c = \sqrt{a^2 - b^2}$
- Excentricidad: $e = \frac{c}{a}$ (donde $0 < e < 1$)

## Hipérbola

$$\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1$$ (horizontal)

- Centro: $(h, k)$
- Distancia focal: $c = \sqrt{a^2 + b^2}$
- Asíntotas: $y - k = \pm\frac{b}{a}(x - h)$
- Excentricidad: $e = \frac{c}{a}$ (donde $e > 1$)

---

<!--
IA: Fórmulas de geometría analítica para repaso rápido.
file_id: FUN-06-Resumen-Formulas
-->
