<!--
::METADATA::
type: cheatsheet
topic_id: ed-02-[edo](../../glossary.md#orden)
file_id: ED-02-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Resumen rápido — EDO de Segundo Orden

## Forma general

$$a\frac{d^2y}{dx^2} + b\frac{dy}{dx} + cy = g(x)$$

---

## Ecuación Homogénea con Coeficientes Constantes

$$ay'' + by' + cy = 0$$

### Ecuación característica

$$ar^2 + br + c = 0 \quad \Rightarrow \quad r = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

### Solución según discriminante

| Discriminante | Raíces | [Solución general](../../glossary.md#solucion-general):** $y = y_h + y_p$

---

## Método de Coeficientes Indeterminados

| $g(x)$ | Propuesta $y_p$ |
|--------|-----------------|
| $P_n(x)$ ([polinomio](../../glossary.md#solucion-particular):**
$$y_p = u_1(x) y_1(x) + u_2(x) y_2(x)$$

**[Wronskiano](../../glossary.md#sustitucion):** $y = x^m$ o $x = e^t$

**Ecuación auxiliar:**
$$am(m-1) + bm + c = 0 \quad \Rightarrow \quad am^2 + (b-a)m + c = 0$$

| Raíces | Solución |
|--------|----------|
| $m_1 \neq m_2$ reales | $y = C_1 x^{m_1} + C_2 x^{m_2}$ |
| $m$ repetida | $y = (C_1 + C_2 \ln x)x^m$ |
| $\alpha \pm \beta i$ | $y = x^\alpha[C_1 \cos(\beta \ln x) + C_2 \sin(\beta \ln x)]$ |

---

## Reducción de Orden

Si se conoce $y_1$, buscar $y_2 = v(x) \cdot y_1(x)$:

$$v = \int \frac{e^{-\int P(x)\,dx}}{y_1^2}\,dx$$

---

## Aplicaciones: Oscilador Armónico

$$my'' + cy' + ky = F(t)$$

| Caso | Condición | Comportamiento |
|------|-----------|----------------|
| Subamortiguado | $c^2 < 4mk$ | Oscilaciones decrecientes |
| Críticamente amortiguado | $c^2 = 4mk$ | Sin oscilación, retorno rápido |
| Sobreamortiguado | $c^2 > 4mk$ | Sin oscilación, retorno lento |
| No amortiguado | $c = 0$ | Oscilación permanente |

**Frecuencia natural:** $\omega_0 = \sqrt{\frac{k}{m}}$

**Frecuencia amortiguada:** $\omega_d = \sqrt{\omega_0^2 - \left(\frac{c}{2m}\right)^2}$

---

<!--
IA: Hoja de referencia rápida para [EDO](../../glossary.md#orden).
Para desarrollo completo: [theory/ED-02-Teoria-EDO-Segundo-Orden.md](theory/ED-02-Teoria-EDO-Segundo-Orden.md)
file_id: ED-02-Resumen-Formulas
-->
