<!--
HUMANO:
Soluciones para teoremas fundamentales.

IA:
Soluciones representativas con desarrollo completo.

---
content_type: solutions
expected_output:
  default: detailed steps
---
-->

# Soluciones de Teoremas Fundamentales

---

## Teorema de Rolle

### Problema 1
**Verificar Rolle para $f(x) = x^2 - 4x + 3$ en $[1, 3]$.**

**Verificación de hipótesis:**
- $f$ es [polinomio](../../../glossary.md#polinomio) → continua en $[1, 3]$ ✓
- $f$ es [polinomio](../../../glossary.md#polinomio) → diferenciable en $(1, 3)$ ✓
- $f(1) = 1 - 4 + 3 = 0$, $f(3) = 9 - 12 + 3 = 0$ → $f(1) = f(3)$ ✓

**Encontrar $c$:**
$f'(x) = 2x - 4 = 0$
$x = 2$

$c = 2 \in (1, 3)$ ✓

---

### Problema 5
**Probar que $x^3 + x - 1 = 0$ tiene exactamente una raíz real.**

**Existencia:**
Sea $f(x) = x^3 + x - 1$
- $f(0) = -1 < 0$
- $f(1) = 1 > 0$

Por Bolzano, existe al menos una raíz en $(0, 1)$.

**Unicidad:**
$f'(x) = 3x^2 + 1 > 0$ para todo $x$

$f$ es estrictamente creciente, por lo que puede cruzar el eje $x$ a lo sumo una vez.

∴ Existe exactamente una raíz real.

---

## Teorema del Valor Medio

### Problema 15
**Probar que $\lvert \cos a - \cos b \rvert \leq \lvert a - b \rvert$.**

Por el TVM aplicado a $f(x) = \cos x$ en $[a, b]$ (o $[b, a]$):

Existe $c$ entre $a$ y $b$ [tal que](../../../glossary.md#tal-que):
$$\frac{\cos b - \cos a}{b - a} = f'(c) = -\sin c$$

Por tanto:
$$\lvert \cos b - \cos a \rvert = \lvert -\sin c \rvert \cdot \lvert b - a \rvert$$

Como $\lvert \sin c \rvert \leq 1$:
$$\lvert \cos a - \cos b \rvert \leq \lvert a - b \rvert$$ ∎

---

### Problema 17
**Auto que recorre 120 km en 1 hora.**

Sea $s(t)$ la posición del auto, con $s(0) = 0$ y $s(1) = 120$.

Por el TVM, existe $c \in (0, 1)$ [tal que](../../../glossary.md#tal-que):
$$s'(c) = \frac{s(1) - s(0)}{1 - 0} = \frac{120 - 0}{1} = 120 \text{ km/h}$$

∴ En el instante $t = c$, la velocidad instantánea fue exactamente 120 km/h. ∎

---

## Regla de L'Hôpital

### Problema 33
$$\lim_{x \to 0} \frac{x - \sin x}{x^3}$$

**Verificación:** $\frac{0 - 0}{0} = \frac{0}{0}$ ✓

**Primera aplicación:**
$$\lim_{x \to 0} \frac{1 - \cos x}{3x^2} = \frac{0}{0}$$

**Segunda aplicación:**
$$\lim_{x \to 0} \frac{\sin x}{6x} = \frac{0}{0}$$

**Tercera aplicación:**
$$\lim_{x \to 0} \frac{\cos x}{6} = \frac{1}{6}$$

---

### Problema 52
$$\lim_{x \to 0} \left(\frac{1}{\sin x} - \frac{1}{x}\right)$$

**Forma $\infty - \infty$** → combinar fracciones:

$$= \lim_{x \to 0} \frac{x - \sin x}{x \sin x}$$

**Forma $\frac{0}{0}$:**
$$= \lim_{x \to 0} \frac{1 - \cos x}{\sin x + x \cos x} = \frac{0}{0}$$

$$= \lim_{x \to 0} \frac{\sin x}{\cos x + \cos x - x \sin x} = \frac{0}{2} = 0$$

---

### Problema 56
$$\lim_{x \to 0^+} x^x$$

**Forma $0^0$** → usar logaritmo.

Sea $y = x^x$, entonces $\ln y = x \ln x$.

$$\lim_{x \to 0^+} x \ln x = \lim_{x \to 0^+} \frac{\ln x}{1/x}$$

**Forma $\frac{-\infty}{\infty}$:**
$$= \lim_{x \to 0^+} \frac{1/x}{-1/x^2} = \lim_{x \to 0^+} (-x) = 0$$

∴ $\lim_{x \to 0^+} \ln y = 0$, por tanto $\lim_{x \to 0^+} y = e^0 = 1$

---

### Problema 61
$$\lim_{x \to 0} (\cos x)^{1/x^2}$$

**Forma $1^\infty$** → usar logaritmo.

Sea $y = (\cos x)^{1/x^2}$, entonces $\ln y = \frac{\ln(\cos x)}{x^2}$.

$$\lim_{x \to 0} \frac{\ln(\cos x)}{x^2} = \frac{0}{0}$$

Por L'Hôpital:
$$= \lim_{x \to 0} \frac{-\tan x}{2x} = \frac{0}{0}$$

$$= \lim_{x \to 0} \frac{-\sec^2 x}{2} = -\frac{1}{2}$$

∴ $\lim y = e^{-1/2} = \frac{1}{\sqrt{e}}$

---

## Taylor y Series

### Problema 66
**Polinomio de Taylor de grado 3 de $e^x$ en $x = 0$.**

| $n$ | $f^{(n)}(x)$ | $f^{(n)}(0)$ |
|-----|--------------|--------------|
| 0 | $e^x$ | 1 |
| 1 | $e^x$ | 1 |
| 2 | $e^x$ | 1 |
| 3 | $e^x$ | 1 |

$$P_3(x) = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} = 1 + x + \frac{x^2}{2} + \frac{x^3}{6}$$

---

### Problema 73
**Aproximar $e^{0.1}$ con $P_2(x)$ y estimar error.**

$P_2(x) = 1 + x + \frac{x^2}{2}$

$P_2(0.1) = 1 + 0.1 + \frac{0.01}{2} = 1.105$

**Error de Lagrange:**
$$R_2(x) = \frac{f'''(c)}{3!}x^3 = \frac{e^c}{6}x^3$$

donde $c \in (0, 0.1)$.

Como $e^c < e^{0.1} < e^1 < 3$:
$$\lvert R_2(0.1) \rvert < \frac{3}{6}(0.1)^3 = 0.0005$$

Valor real: $e^{0.1} \approx 1.10517...$
Error real: $\approx 0.00017$

---

### Problema 76
$$\lim_{x \to 0} \frac{e^x - 1 - x - \frac{x^2}{2}}{x^3}$$

Usando la serie de Maclaurin de $e^x$:
$$e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} + \cdots$$

$$e^x - 1 - x - \frac{x^2}{2} = \frac{x^3}{6} + \frac{x^4}{24} + \cdots$$

$$\frac{e^x - 1 - x - \frac{x^2}{2}}{x^3} = \frac{1}{6} + \frac{x}{24} + \cdots \to \frac{1}{6}$$

---

### Problema 79
$$\lim_{x \to 0} \frac{e^{\sin x} - e^x}{x^3}$$

**Expansiones:**
$\sin x = x - \frac{x^3}{6} + O(x^5)$

$e^{\sin x} = e^{x - x^3/6 + O(x^5)}$

Usando $e^u = 1 + u + \frac{u^2}{2} + O(u^3)$ con $u = \sin x$:

$e^{\sin x} = 1 + \left(x - \frac{x^3}{6}\right) + \frac{x^2}{2} + O(x^3)$

$= 1 + x + \frac{x^2}{2} - \frac{x^3}{6} + O(x^3)$

$e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + O(x^4)$

$$e^{\sin x} - e^x = -\frac{x^3}{6} - \frac{x^3}{6} + O(x^4) = -\frac{x^3}{3} + O(x^4)$$

$$\lim_{x \to 0} \frac{e^{\sin x} - e^x}{x^3} = -\frac{1}{3}$$
