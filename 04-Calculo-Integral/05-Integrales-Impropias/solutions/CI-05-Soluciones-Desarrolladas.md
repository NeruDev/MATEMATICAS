<!--
HUMANO:
Soluciones de [integrales impropias](../../../glossary.md#integrales-impropias).

IA:
Soluciones detalladas de problemas representativos.

---
content_type: solutions
format: step_by_step
---
-->

# Soluciones de Integrales Impropias

---

## Problema 2
**Enunciado:** $\displaystyle\int_0^{\infty} e^{-x}\,dx$

**Solución:**
$$\int_0^{\infty} e^{-x}\,dx = \lim_{t \to \infty} \int_0^t e^{-x}\,dx = \lim_{t \to \infty} [-e^{-x}]_0^t$$

$$= \lim_{t \to \infty} (-e^{-t} + e^0) = 0 + 1 = 1$$

**Converge a 1.**

---

## Problema 6
**Enunciado:** $\displaystyle\int_0^{\infty} xe^{-x}\,dx$

**Solución:**
Usamos [integración por partes](../../../glossary.md#integración-por-partes): $u = x$, $dv = e^{-x}dx$

$$\int xe^{-x}\,dx = -xe^{-x} + \int e^{-x}\,dx = -xe^{-x} - e^{-x} = -(x+1)e^{-x}$$

$$\int_0^{\infty} xe^{-x}\,dx = \lim_{t \to \infty} [-(x+1)e^{-x}]_0^t$$

$$= \lim_{t \to \infty} \left[-(t+1)e^{-t} + 1\right]$$

Por L'Hôpital: $\lim_{t \to \infty} \frac{t+1}{e^t} = 0$

$$= 0 + 1 = 1$$

**Converge a 1.**

---

## Problema 9
**Enunciado:** $\displaystyle\int_{-\infty}^{\infty} \frac{1}{1+x^2}\,dx$

**Solución:**
Dividimos en dos partes:
$$= \int_{-\infty}^{0} \frac{dx}{1+x^2} + \int_0^{\infty} \frac{dx}{1+x^2}$$

$$= \lim_{s \to -\infty} [\arctan x]_s^0 + \lim_{t \to \infty} [\arctan x]_0^t$$

$$= (0 - (-\frac{\pi}{2})) + (\frac{\pi}{2} - 0) = \frac{\pi}{2} + \frac{\pi}{2} = \pi$$

**Converge a $\pi$.**

---

## Problema 12
**Enunciado:** $\displaystyle\int_1^{\infty} \frac{\ln x}{x^2}\,dx$

**Solución:**
Integración por partes: $u = \ln x$, $dv = x^{-2}dx$

$$du = \frac{1}{x}dx, \quad v = -\frac{1}{x}$$

$$\int \frac{\ln x}{x^2}\,dx = -\frac{\ln x}{x} + \int \frac{1}{x^2}\,dx = -\frac{\ln x}{x} - \frac{1}{x}$$

$$\int_1^{\infty} \frac{\ln x}{x^2}\,dx = \lim_{t \to \infty} \left[-\frac{\ln x + 1}{x}\right]_1^t$$

$$= \lim_{t \to \infty} \left(-\frac{\ln t + 1}{t}\right) - (-1) = 0 + 1 = 1$$

(Por L'Hôpital: $\lim_{t \to \infty} \frac{\ln t + 1}{t} = \lim_{t \to \infty} \frac{1/t}{1} = 0$)

**Converge a 1.**

---

## Problema 14
**Enunciado:** $\displaystyle\int_0^1 \frac{1}{\sqrt{x}}\,dx$

**Solución:**
Discontinuidad en $x = 0$ (Tipo II):

$$\int_0^1 x^{-1/2}\,dx = \lim_{t \to 0^+} \int_t^1 x^{-1/2}\,dx = \lim_{t \to 0^+} [2\sqrt{x}]_t^1$$

$$= \lim_{t \to 0^+} (2 - 2\sqrt{t}) = 2 - 0 = 2$$

**Converge a 2.**

---

## Problema 17
**Enunciado:** $\displaystyle\int_0^1 \frac{1}{x}\,dx$

**Solución:**
$$\int_0^1 \frac{1}{x}\,dx = \lim_{t \to 0^+} \int_t^1 \frac{1}{x}\,dx = \lim_{t \to 0^+} [\ln x]_t^1$$

$$= \lim_{t \to 0^+} (0 - \ln t) = \lim_{t \to 0^+} (-\ln t) = +\infty$$

**Diverge.**

---

## Problema 21
**Enunciado:** $\displaystyle\int_0^3 \frac{1}{(x-1)^{2/3}}\,dx$

**Solución:**
Discontinuidad en $x = 1$ (interior). Dividimos:

$$= \int_0^1 \frac{dx}{(x-1)^{2/3}} + \int_1^3 \frac{dx}{(x-1)^{2/3}}$$

**Primera integral:**
$$\lim_{t \to 1^-} \int_0^t (x-1)^{-2/3}\,dx = \lim_{t \to 1^-} [3(x-1)^{1/3}]_0^t$$
$$= \lim_{t \to 1^-} (3(t-1)^{1/3} - 3(-1)^{1/3}) = 0 - 3(-1) = 3$$

**Segunda integral:**
$$\lim_{s \to 1^+} \int_s^3 (x-1)^{-2/3}\,dx = \lim_{s \to 1^+} [3(x-1)^{1/3}]_s^3$$
$$= 3(2)^{1/3} - 0 = 3\sqrt[3]{2}$$

**Total:** $3 + 3\sqrt[3]{2} = 3(1 + \sqrt[3]{2})$

---

## Problema 24
**Enunciado:** Determinar [convergencia](../../../glossary.md#convergencia) de $\displaystyle\int_1^{\infty} \frac{1}{\sqrt{x^3+1}}\,dx$

**Solución:**
Para $x$ grande: $\sqrt{x^3+1} \approx x^{3/2}$

Comparación por [límite](../../../glossary.md#límite) con $g(x) = \frac{1}{x^{3/2}}$:

$$\lim_{x \to \infty} \frac{1/\sqrt{x^3+1}}{1/x^{3/2}} = \lim_{x \to \infty} \frac{x^{3/2}}{\sqrt{x^3+1}} = \lim_{x \to \infty} \sqrt{\frac{x^3}{x^3+1}} = 1$$

Como $\int_1^{\infty} \frac{1}{x^{3/2}}\,dx$ converge ($p = 3/2 > 1$), la integral **converge**.

---

## Problema 25
**Enunciado:** $\displaystyle\int_2^{\infty} \frac{1}{x\ln x}\,dx$

**Solución:**
Sea $u = \ln x$, $du = \frac{1}{x}dx$

Cuando $x = 2$: $u = \ln 2$; cuando $x \to \infty$: $u \to \infty$

$$\int_2^{\infty} \frac{dx}{x\ln x} = \int_{\ln 2}^{\infty} \frac{du}{u} = \lim_{t \to \infty} [\ln u]_{\ln 2}^t = \infty$$

**Diverge.**

---

## Problema 36
**Enunciado:** $\displaystyle\int_0^{\infty} \frac{1}{\sqrt{x}(1+x)}\,dx$

**Solución:**
Esta integral tiene problemas tanto en $x = 0$ (Tipo II) como en $x = \infty$ (Tipo I).

Dividimos en $x = 1$:
$$= \int_0^1 \frac{dx}{\sqrt{x}(1+x)} + \int_1^{\infty} \frac{dx}{\sqrt{x}(1+x)}$$

Sea $u = \sqrt{x}$, entonces $x = u^2$, $dx = 2u\,du$:

$$\int \frac{dx}{\sqrt{x}(1+x)} = \int \frac{2u\,du}{u(1+u^2)} = 2\int \frac{du}{1+u^2} = 2\arctan u = 2\arctan\sqrt{x}$$

$$\int_0^{\infty} \frac{dx}{\sqrt{x}(1+x)} = \lim_{t \to \infty} [2\arctan\sqrt{x}]_0^t = 2 \cdot \frac{\pi}{2} - 0 = \pi$$

**Converge a $\pi$.**

---

## Problema 40
**Enunciado:** Evaluar $\displaystyle\int_0^1 x^p \ln x\,dx$ para $p > -1$.

**Solución:**
Integración por partes: $u = \ln x$, $dv = x^p dx$

$$du = \frac{1}{x}dx, \quad v = \frac{x^{p+1}}{p+1}$$

$$\int x^p \ln x\,dx = \frac{x^{p+1}\ln x}{p+1} - \frac{1}{p+1}\int x^p\,dx = \frac{x^{p+1}\ln x}{p+1} - \frac{x^{p+1}}{(p+1)^2}$$

$$\int_0^1 x^p \ln x\,dx = \left[\frac{x^{p+1}\ln x}{p+1} - \frac{x^{p+1}}{(p+1)^2}\right]_0^1$$

En $x = 1$: $\frac{0}{p+1} - \frac{1}{(p+1)^2} = -\frac{1}{(p+1)^2}$

En $x \to 0^+$: $\lim_{x \to 0^+} x^{p+1}\ln x = 0$ para $p > -1$ (por L'Hôpital)

$$= -\frac{1}{(p+1)^2} - 0 = -\frac{1}{(p+1)^2}$$
