<!--
::METADATA::
type: cheatsheet
topic_id: ed-02-[edo](../../glossary.md#edo)-segundo-[orden](../../glossary.md#orden)
file_id: ED-02-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

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

| Discriminante | Raíces | [Solución general](../../glossary.md#solucion-general) |
|---------------|--------|------------------|
| $\Delta > 0$ | $r_1, r_2$ reales distintas | $y = C_1 e^{r_1 x} + C_2 e^{r_2 x}$ |
| $\Delta = 0$ | $r$ real repetida | $y = (C_1 + C_2 x)e^{rx}$ |
| $\Delta < 0$ | $\alpha \pm \beta i$ | $y = e^{\alpha x}(C_1 \cos\beta x + C_2 \sin\beta x)$ |

---

## Ecuación No Homogénea

$$ay'' + by' + cy = g(x)$$

**[Solución general](../../glossary.md#solucion-general):** $y = y_h + y_p$

---

## Método de Coeficientes Indeterminados

| $g(x)$ | Propuesta $y_p$ |
|--------|-----------------|
| $P_n(x)$ ([polinomio](../../glossary.md#polinomio) grado $n$) | $x^s(A_n x^n + \cdots + A_1 x + A_0)$ |
| $e^{\alpha x}$ | $x^s A e^{\alpha x}$ |
| $\cos\beta x$ o $\sin\beta x$ | $x^s(A\cos\beta x + B\sin\beta x)$ |
| $e^{\alpha x}\cos\beta x$ | $x^s e^{\alpha x}(A\cos\beta x + B\sin\beta x)$ |
| $P_n(x)e^{\alpha x}$ | $x^s e^{\alpha x}(A_n x^n + \cdots + A_0)$ |

**Nota:** $s$ = número de veces que la parte de $g(x)$ aparece en $y_h$ (0, 1 o 2)

---

## Método de Variación de Parámetros

Para $y'' + P(x)y' + Q(x)y = g(x)$, con solución homogénea $y_h = C_1 y_1 + C_2 y_2$:

**[Solución particular](../../glossary.md#solucion-particular):**
$$y_p = u_1(x) y_1(x) + u_2(x) y_2(x)$$

**[Wronskiano](../../glossary.md#wronskiano):**
$$W = \begin{vmatrix} y_1 & y_2 \\ y_1' & y_2' \end{vmatrix} = y_1 y_2' - y_2 y_1'$$

**Fórmulas:**
$$u_1 = -\int \frac{y_2 \cdot g(x)}{W}\,dx, \quad u_2 = \int \frac{y_1 \cdot g(x)}{W}\,dx$$

---

## Ecuación de Cauchy-Euler

$$ax^2 y'' + bxy' + cy = 0$$

**[Sustitución](../../glossary.md#sustitucion):** $y = x^m$ o $x = e^t$

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
IA: Hoja de referencia rápida para [EDO](../../glossary.md#edo) de Segundo [Orden](../../glossary.md#orden).
Para desarrollo completo: theory/ED-02-Teoria-EDO-Segundo-Orden.md
file_id: ED-02-Resumen-Formulas
-->
