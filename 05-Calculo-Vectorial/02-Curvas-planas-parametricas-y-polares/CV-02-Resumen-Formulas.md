<!--
::METADATA::
type: cheatsheet
topic_id: cv-02-curvas-parametricas-polares
file_id: CV-02-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->

# Resumen rápido — Curvas paramétricas y coordenadas polares

## Ecuaciones paramétricas

| Concepto | Fórmula |
|----------|---------|
| **Curva** | $x = x(t),\; y = y(t),\; t \in [a,b]$ |
| **Pendiente** | $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$ (si $dx/dt \neq 0$) |
| **Segunda derivada** | $\frac{d^2y}{dx^2} = \frac{d}{dt}\left(\frac{dy}{dx}\right) \cdot \frac{1}{dx/dt}$ |

## Tangentes paramétricas

- **Tangente horizontal:** $dy/dt = 0$ y $dx/dt \neq 0$
- **Tangente vertical:** $dx/dt = 0$ y $dy/dt \neq 0$
- **Punto singular:** $dx/dt = 0$ y $dy/dt = 0$ (requiere análisis adicional)

## Longitud de arco paramétrico

$$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\, dt$$

## Área bajo curva paramétrica

$$A = \int_a^b y(t)\, x'(t)\, dt \quad \text{(o } -\int_a^b x(t)\, y'(t)\, dt \text{)}$$

## Coordenadas polares

| Conversión | Fórmula |
|------------|---------|
| **Polar → Cartesiana** | $x = r\cos\theta,\; y = r\sin\theta$ |
| **Cartesiana → Polar** | $r = \sqrt{x^2+y^2},\; \theta = \arctan(y/x)$ |

## Curvas polares clásicas

| Curva | Ecuación |
|-------|----------|
| Círculo | $r = a$ |
| Cardioide | $r = a(1 + \cos\theta)$ |
| Rosa de $n$ pétalos | $r = a\cos(n\theta)$ o $r = a\sin(n\theta)$ |
| Lemniscata | $r^2 = a^2\cos(2\theta)$ |
| Espiral de Arquímedes | $r = a\theta$ |
| Limaçon | $r = a + b\cos\theta$ |

## Derivada en polares

$$\frac{dy}{dx} = \frac{\frac{dr}{d\theta}\sin\theta + r\cos\theta}{\frac{dr}{d\theta}\cos\theta - r\sin\theta}$$

## Área en coordenadas polares

| Concepto | Fórmula |
|----------|---------|
| **Área encerrada** | $A = \frac{1}{2}\int_\alpha^\beta r(\theta)^2\, d\theta$ |
| **Área entre curvas** | $A = \frac{1}{2}\int_\alpha^\beta \left[r_{\text{ext}}^2 - r_{\text{int}}^2\right] d\theta$ |

## Longitud de arco en polares

$$L = \int_\alpha^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\, d\theta$$

## Criterios rápidos

| Condición | Significado |
|-----------|-------------|
| $r(\theta) = r(-\theta)$ | Simetría respecto al eje polar |
| $r(\theta) = r(\pi - \theta)$ | Simetría respecto a $\theta = \pi/2$ |
| $r(\theta) = -r(\theta + \pi)$ | Simetría respecto al polo |

---

<!--
IA: Usa este resumen para respuestas breves.
Para desarrollo completo, consulta theory/CV-02-Teoria-Curvas.md
file_id: CV-02-Resumen-Formulas
-->
