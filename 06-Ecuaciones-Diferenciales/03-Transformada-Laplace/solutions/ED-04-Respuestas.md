<!--
::METADATA::
type: answer-key
topic_id: ed-04-transformada-laplace
file_id: ED-04-Respuestas
status: stable
audience: student
total_problems: 24
solved_detailed: 0
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Respuestas Rápidas - Transformada de Laplace

> **Leyenda:** ✅ Solución desarrollada | ➖ Solo respuesta

## Tabla de Respuestas

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-01] | a) $\frac{5}{s}$; b) $\frac{6}{s^4}$; c) $\frac{1}{s+4}$; d) $\frac{5}{s^2+25}$; e) $\frac{s}{s^2+4}$ | ➖ |
| [Prob-02] | a) $\frac{6}{s^3} - \frac{2}{s^2} + \frac{1}{s}$; b) $\frac{4}{s-2} - \frac{3}{s+1}$; c) $\frac{2s + 15}{s^2+9}$; d) $\frac{1}{s-2}$ | ➖ |
| [Prob-03] | a) $\frac{2}{(s-3)^3}$; b) $\frac{4}{(s+2)^2+16}$; c) $\frac{s-1}{(s-1)^2+9}$; d) $\frac{2}{(s+1)^3} + \frac{2}{(s+1)^2}$ | ➖ |
| [Prob-04] | a) $\frac{3(s-2) - 20}{(s-2)^2+25}$; b) $\frac{4(s+3)}{[(s+3)^2+4]^2}$ | ➖ |
| [Prob-05] | a) $sF(s) - 2$; b) $s^2F(s) - s + 3$ | ➖ |
| [Prob-06] | a) $\frac{4s}{(s^2+4)^2}$; b) $\frac{s^2-1}{(s^2+1)^2}$; c) $\frac{2}{(s+1)^3}$ | ➖ |
| [Prob-07] | a) $\frac{t^3}{2}$; b) $2e^{5t}$; c) $\sin 4t$; d) $\cos 3t$ | ➖ |
| [Prob-08] | a) $\frac{1}{2}(e^{2t} - 1)$; b) $\frac{4}{3}e^{-2t} - \frac{1}{3}e^{t}$; c) $e^{2t} - e^{-2t}$; d) $\frac{1}{2}e^{-t} + \frac{1}{2}\cos t - \frac{1}{2}\sin t$ | ➖ |
| [Prob-09] | a) $t - 1 + e^{-t}$; b) $(t + 1)e^t$; c) $(t^2 + t - \frac{1}{2})e^{-t}$ | ➖ |
| [Prob-10] | a) $\frac{1}{2}e^{-t}\sin 2t$; b) $e^{-2t}(\cos 2t + \frac{3}{2}\sin 2t)$; c) $e^{3t}(\cos 2t - \frac{9}{4}\sin 2t)$ | ➖ |
| [Prob-11] | a) $y = 3e^{-2t}$; b) $y = \frac{4}{3}e^{2t} - \frac{1}{3}e^{-t}$; c) $y = \frac{1}{10}(\sin t - 3\cos t) + \frac{3}{10}e^{-3t}$ | ➖ |
| [Prob-12] | a) $y = \cos 2t$; b) $y = \sinh t = \frac{e^t - e^{-t}}{2}$; c) $y = (1 + 2t)e^{-t}$ | ➖ |
| [Prob-13] | a) $y = \frac{t}{4}\sin 2t$; b) $y = te^t$; c) $y = t + \cos t$ | ➖ |
| [Prob-14] | a) $y = \frac{t}{4}e^{-t}\sin 2t$; b) $y = \frac{1}{2}(e^t - e^{-t}) = \sinh t$ | ➖ |
| [Prob-15] | a) $f(t) = 2u(t-3)$; b) $f(t) = t - (t-2)u(t-2) - 2u(t-2) = t - 2(t-2)u(t-2)$; c) $f(t) = 1 - u(t-1) + u(t-2)$ | ➖ |
| [Prob-16] | a) $\frac{e^{-2s}}{s}$; b) $\frac{e^{-s}}{s^2}$; c) $\frac{e^{-3s}}{s+1}$; d) $\frac{e^{-\pi s}}{s^2+1}$ | ➖ |
| [Prob-17] | a) $u(t-2)$; b) $(t-1)u(t-1)$; c) $\cos(t-\pi)u(t-\pi) = -\cos t \cdot u(t-\pi)$ | ➖ |
| [Prob-18] | a) $y = e^{-(t-1)}u(t-1)$; b) $y = \frac{1}{2}\sin 2(t-\pi)u(t-\pi)$; c) $y = te^{-t}$ | ➖ |
| [Prob-19] | a) $t - 1 + e^{-t}$ (por [convolución](../../../glossary.md#convolucion)); b) $e^{2t} - e^t$ | ➖ |
| [Prob-20] | $y = \int_0^t f(\tau)\sin(t-\tau)\,d\tau = (f * \sin)(t)$ | ➖ |
| [Prob-21] | $q(t) = 0.1(1 - e^{-t})$ C | ➖ |
| [Prob-22] | $i(t) = 10te^{-t}$ A | ➖ |
| [Prob-23] | $x(t) = \frac{3}{2}\sin 2(t-2) \cdot u(t-2)$ m | ➖ |
| [Prob-24] | $Y(s) = \frac{w_0}{EI \cdot s^5}(1 - e^{-Ls/2})$ | ➖ |

---

## Fórmulas Clave

### Transformadas Básicas

| $f(t)$ | $F(s) = \mathcal{L}\{f\}$ |
|:-------|:--------------------------|
| $1$ | $\frac{1}{s}$ |
| $t^n$ | $\frac{n!}{s^{n+1}}$ |
| $e^{at}$ | $\frac{1}{s-a}$ |
| $\sin bt$ | $\frac{b}{s^2+b^2}$ |
| $\cos bt$ | $\frac{s}{s^2+b^2}$ |
| $u(t-a)$ | $\frac{e^{-as}}{s}$ |
| $\delta(t-a)$ | $e^{-as}$ |

### Propiedades

| Propiedad | Fórmula |
|:----------|:--------|
| [Linealidad](../../../glossary.md#derivada) | $\mathcal{L}\{f'\} = sF(s) - f(0)$ |
| Multiplicación por $t$ | $\mathcal{L}\{tf\} = -F'(s)$ |
| [Convolución](../problems/ED-04-Problemas.md)
