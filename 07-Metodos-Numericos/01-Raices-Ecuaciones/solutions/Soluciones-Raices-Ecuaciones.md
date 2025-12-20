<!--
content_type: solutions
topic: Raíces de Ecuaciones
---
-->

# Soluciones: Raíces de Ecuaciones

*Soluciones seleccionadas que ilustran los métodos principales.*

---

## Solución Problema 1 (Bisección)

**Encontrar la raíz de $f(x) = x^3 - x - 1$ en $[1, 2]$ con $\varepsilon = 0.01$**

**Verificar:** $f(1) = -1 < 0$, $f(2) = 5 > 0$ ✓

| $n$ | $a$ | $b$ | $c = \frac{a+b}{2}$ | $f(c)$ | $b-a$ |
|-----|-----|-----|---------------------|--------|-------|
| 1 | 1.0 | 2.0 | 1.5 | 0.875 | 1.0 |
| 2 | 1.0 | 1.5 | 1.25 | -0.297 | 0.5 |
| 3 | 1.25 | 1.5 | 1.375 | 0.225 | 0.25 |
| 4 | 1.25 | 1.375 | 1.3125 | -0.051 | 0.125 |
| 5 | 1.3125 | 1.375 | 1.3438 | 0.083 | 0.0625 |
| 6 | 1.3125 | 1.3438 | 1.3281 | 0.015 | 0.0313 |
| 7 | 1.3125 | 1.3281 | 1.3203 | -0.018 | 0.0156 |

Como $b - a = 0.0156 < 2(0.01)$, terminamos.

$$\boxed{x^* \approx 1.3203}$$

---

## Solución Problema 2 (Iteraciones de bisección)

**¿Iteraciones para $[0, 4]$ con precisión $10^{-6}$?**

Después de $n$ iteraciones: $|x_n - x^*| \leq \frac{b-a}{2^n}$

Necesitamos: $\frac{4}{2^n} < 10^{-6}$

$$2^n > 4 \times 10^6$$
$$n > \log_2(4 \times 10^6) = \log_2(4) + 6\log_2(10) \approx 2 + 19.93 = 21.93$$

$$\boxed{n = 22 \text{ iteraciones}}$$

---

## Solución Problema 5 (Newton-Raphson para $\sqrt{5}$)

**Resolver $x^2 - 5 = 0$ con $x_0 = 2$**

$f(x) = x^2 - 5$, $f'(x) = 2x$

Fórmula: $x_{n+1} = x_n - \frac{x_n^2 - 5}{2x_n} = \frac{x_n^2 + 5}{2x_n} = \frac{1}{2}\left(x_n + \frac{5}{x_n}\right)$

| $n$ | $x_n$ | $x_n^2$ | $x_{n+1}$ | Error |
|-----|-------|---------|-----------|-------|
| 0 | 2.0 | 4.0 | 2.25 | - |
| 1 | 2.25 | 5.0625 | 2.236111 | 0.0139 |
| 2 | 2.236111 | 4.99999 | 2.2360679779 | 0.000043 |
| 3 | 2.2360679779 | 5.0 | 2.2360679775 | $4 \times 10^{-10}$ |

$$\boxed{\sqrt{5} \approx 2.2360679775}$$

La convergencia es cuadrática: el número de dígitos correctos se duplica en cada iteración.

---

## Solución Problema 6 (Newton para $x^3 - 2x - 5$)

$f(x) = x^3 - 2x - 5$, $f'(x) = 3x^2 - 2$, $x_0 = 2$

$f(2) = 8 - 4 - 5 = -1$, $f'(2) = 12 - 2 = 10$

| $n$ | $x_n$ | $f(x_n)$ | $f'(x_n)$ | $x_{n+1}$ |
|-----|-------|----------|-----------|-----------|
| 0 | 2.0 | -1.0 | 10.0 | 2.1 |
| 1 | 2.1 | 0.061 | 11.23 | 2.09457 |
| 2 | 2.09457 | 0.00015 | 11.16 | 2.09455 |

$$\boxed{x^* \approx 2.09455}$$

---

## Solución Problema 10 (Secante)

**Resolver $x^3 + x - 1 = 0$ con $x_0 = 0$, $x_1 = 1$**

$f(x) = x^3 + x - 1$

$f(0) = -1$, $f(1) = 1$

Fórmula: $x_{n+1} = x_n - f(x_n)\frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}$

| $n$ | $x_{n-1}$ | $x_n$ | $f(x_n)$ | $x_{n+1}$ |
|-----|-----------|-------|----------|-----------|
| 2 | 0 | 1 | 1 | 0.5 |
| 3 | 1 | 0.5 | -0.375 | 0.6364 |
| 4 | 0.5 | 0.6364 | -0.1058 | 0.6901 |
| 5 | 0.6364 | 0.6901 | 0.0188 | 0.6822 |
| 6 | 0.6901 | 0.6822 | -0.0012 | 0.6823 |

$$\boxed{x^* \approx 0.6823}$$

---

## Solución Problema 13 (Punto Fijo)

**Para $x^3 - x - 1 = 0$, proponer funciones $g(x)$**

**Opción 1:** $x = x^3 - 1 \Rightarrow g_1(x) = x^3 - 1$
- $g_1'(x) = 3x^2$
- En $x^* \approx 1.32$: $|g_1'(1.32)| = 5.23 > 1$ ❌ **Diverge**

**Opción 2:** $x = \sqrt[3]{x + 1} \Rightarrow g_2(x) = (x+1)^{1/3}$
- $g_2'(x) = \frac{1}{3}(x+1)^{-2/3}$
- En $x^* \approx 1.32$: $|g_2'(1.32)| = 0.24 < 1$ ✓ **Converge**

**Opción 3:** $x = \frac{1}{x^2 - 1}$ (de $x(x^2-1) = 1$) 
- Esta formulación es problemática cerca de $x = 1$

**Verificación de $g_2$:** Con $x_0 = 1$:

| $n$ | $x_n$ | $g_2(x_n)$ |
|-----|-------|------------|
| 0 | 1.0 | 1.2599 |
| 1 | 1.2599 | 1.3122 |
| 2 | 1.3122 | 1.3223 |
| 3 | 1.3223 | 1.3243 |
| 4 | 1.3243 | 1.3247 |

$$\boxed{g_2(x) = (x+1)^{1/3} \text{ converge}}$$

---

## Solución Problema 17 (Newton para $x^2 - a$)

**Demostrar la fórmula y verificar convergencia cuadrática**

$f(x) = x^2 - a$, $f'(x) = 2x$

Newton: $x_{n+1} = x_n - \frac{x_n^2 - a}{2x_n} = \frac{2x_n^2 - x_n^2 + a}{2x_n} = \frac{x_n^2 + a}{2x_n}$

$$\boxed{x_{n+1} = \frac{1}{2}\left(x_n + \frac{a}{x_n}\right)}$$

**Análisis de convergencia:**

Sea $e_n = x_n - \sqrt{a}$. Entonces $x_n = \sqrt{a} + e_n$.

$$x_{n+1} = \frac{1}{2}\left(\sqrt{a} + e_n + \frac{a}{\sqrt{a} + e_n}\right)$$

$$= \frac{1}{2}\left(\sqrt{a} + e_n + \frac{a(\sqrt{a} - e_n)}{a - e_n^2}\right)$$

Para $e_n$ pequeño:
$$x_{n+1} \approx \frac{1}{2}\left(\sqrt{a} + e_n + \sqrt{a} - e_n + \frac{e_n^2}{\sqrt{a}}\right) = \sqrt{a} + \frac{e_n^2}{2\sqrt{a}}$$

Por lo tanto:
$$\boxed{e_{n+1} \approx \frac{e_n^2}{2\sqrt{a}}}$$

Esto demuestra convergencia **cuadrática** ($p = 2$).

---

## Solución Problema 21 (TIR)

**Calcular TIR con flujos: -1000, 500, 600, 300**

$$f(r) = -1000 + \frac{500}{1+r} + \frac{600}{(1+r)^2} + \frac{300}{(1+r)^3} = 0$$

Sea $x = 1 + r$. Multiplicar por $x^3$:
$$-1000x^3 + 500x^2 + 600x + 300 = 0$$

Dividir por -100:
$$10x^3 - 5x^2 - 6x - 3 = 0$$

**Usando Newton con $x_0 = 1.2$ (equivale a $r_0 = 0.2$):**

$f(x) = 10x^3 - 5x^2 - 6x - 3$
$f'(x) = 30x^2 - 10x - 6$

| $n$ | $x_n$ | $f(x_n)$ | $f'(x_n)$ | $x_{n+1}$ |
|-----|-------|----------|-----------|-----------|
| 0 | 1.2 | 1.08 | 25.2 | 1.157 |
| 1 | 1.157 | 0.072 | 22.23 | 1.154 |
| 2 | 1.154 | 0.0003 | 21.96 | 1.154 |

$x^* = 1.154$, por lo tanto $r^* = 0.154$

$$\boxed{TIR \approx 15.4\%}$$

---

## Solución Problema 29 (Convergencia cuadrática de Newton)

**Demostrar convergencia cuadrática**

Por Taylor alrededor de $x^*$:
$$f(x_n) = f(x^*) + f'(x^*)(x_n - x^*) + \frac{f''(\xi_n)}{2}(x_n - x^*)^2$$

Como $f(x^*) = 0$:
$$f(x_n) = f'(x^*)e_n + \frac{f''(\xi_n)}{2}e_n^2$$

donde $e_n = x_n - x^*$.

De Newton: $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$

$$e_{n+1} = x_{n+1} - x^* = x_n - x^* - \frac{f(x_n)}{f'(x_n)}$$

$$= e_n - \frac{f'(x^*)e_n + \frac{f''(\xi_n)}{2}e_n^2}{f'(x_n)}$$

Para $x_n$ cerca de $x^*$: $f'(x_n) \approx f'(x^*)$

$$e_{n+1} \approx e_n - e_n - \frac{f''(\xi_n)}{2f'(x^*)}e_n^2 = -\frac{f''(\xi_n)}{2f'(x^*)}e_n^2$$

Tomando límite:
$$\boxed{\lim_{n\to\infty}\frac{|e_{n+1}|}{|e_n|^2} = \frac{|f''(x^*)|}{2|f'(x^*)|}}$$

Esto confirma **orden de convergencia $p = 2$** (cuadrática).
