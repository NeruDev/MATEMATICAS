<!--
::METADATA::
type: solution
status: active
-->

# Soluciones: Interpolación

*Soluciones seleccionadas que ilustran los métodos principales.*

---

## Solución Problema 1 (Lagrange)

**Encontrar [polinomio](../../../glossary.md#polinomio) para $(0, 1)$, $(1, 0)$, $(2, 1)$**

**Paso 1:** Calcular polinomios [base](../../../glossary.md#base):

$$L_0(x) = \frac{(x-1)(x-2)}{(0-1)(0-2)} = \frac{(x-1)(x-2)}{2}$$

$$L_1(x) = \frac{(x-0)(x-2)}{(1-0)(1-2)} = \frac{x(x-2)}{-1} = -x(x-2)$$

$$L_2(x) = \frac{(x-0)(x-1)}{(2-0)(2-1)} = \frac{x(x-1)}{2}$$

**Paso 2:** Construir polinomio:

$$P(x) = 1 \cdot L_0(x) + 0 \cdot L_1(x) + 1 \cdot L_2(x)$$

$$= \frac{(x-1)(x-2)}{2} + \frac{x(x-1)}{2}$$

$$= \frac{(x-1)(x-2) + x(x-1)}{2} = \frac{(x-1)(x-2+x)}{2} = \frac{(x-1)(2x-2)}{2}$$

$$= (x-1)^2$$

$$\boxed{P(x) = x^2 - 2x + 1}$$

**Verificación:** $P(0) = 1$ ✓, $P(1) = 0$ ✓, $P(2) = 1$ ✓

---

## Solución Problema 5 (Diferencias Divididas)

**Puntos:** $(0, -1)$, $(1, 1)$, $(3, 7)$, $(4, 13)$

**Tabla de [diferencias divididas](../../../glossary.md#diferencias-divididas):**

| $x_i$ | $f[x_i]$ | $f[x_i, x_{i+1}]$ | $f[x_i, x_{i+1}, x_{i+2}]$ | $f[...]$ |
|-------|----------|-------------------|----------------------------|----------|
| 0 | -1 | | | |
| 1 | 1 | $\frac{1-(-1)}{1-0} = 2$ | | |
| 3 | 7 | $\frac{7-1}{3-1} = 3$ | $\frac{3-2}{3-0} = \frac{1}{3}$ | |
| 4 | 13 | $\frac{13-7}{4-3} = 6$ | $\frac{6-3}{4-1} = 1$ | $\frac{1-\frac{1}{3}}{4-0} = \frac{1}{6}$ |

**Coeficientes:** $a_0 = -1$, $a_1 = 2$, $a_2 = \frac{1}{3}$, $a_3 = \frac{1}{6}$

**Polinomio de Newton:**
$$P(x) = -1 + 2(x-0) + \frac{1}{3}(x-0)(x-1) + \frac{1}{6}(x-0)(x-1)(x-3)$$

Expandiendo:
$$\boxed{P(x) = \frac{1}{6}x^3 - \frac{1}{3}x^2 + \frac{13}{6}x - 1}$$

---

## Solución Problema 6 (Diferencias de $x^3$)

**a)** $f[0, 1] = \frac{1^3 - 0^3}{1 - 0} = \frac{1}{1} = \boxed{1}$

**b)** 
$f[1, 2] = \frac{8 - 1}{1} = 7$

$f[0, 1, 2] = \frac{f[1,2] - f[0,1]}{2-0} = \frac{7 - 1}{2} = \boxed{3}$

**c)**
$f[2, 3] = \frac{27 - 8}{1} = 19$

$f[1, 2, 3] = \frac{19 - 7}{2} = 6$

$f[0, 1, 2, 3] = \frac{f[1,2,3] - f[0,1,2]}{3-0} = \frac{6 - 3}{3} = \boxed{1}$

**Observación:** Para $f(x) = x^n$, $f[x_0, ..., x_n] = 1$ (coeficiente principal).

---

## Solución Problema 9 (Newton Progresivo)

**Datos:** $y = 1, 1, 2, 6, 24$ con $h = 1$

**Tabla de diferencias finitas:**

| $x$ | $y$ | $\Delta y$ | $\Delta^2 y$ | $\Delta^3 y$ | $\Delta^4 y$ |
|-----|-----|------------|--------------|--------------|--------------|
| 0 | 1 | | | | |
| 1 | 1 | 0 | | | |
| 2 | 2 | 1 | 1 | | |
| 3 | 6 | 4 | 3 | 2 | |
| 4 | 24 | 18 | 14 | 11 | 9 |

**Coeficientes:** $\Delta^0 y_0 = 1$, $\Delta y_0 = 0$, $\Delta^2 y_0 = 1$, $\Delta^3 y_0 = 2$, $\Delta^4 y_0 = 9$

**Polinomio:** Con $s = x - 0 = x$:

$$P(x) = 1 + \binom{x}{1}(0) + \binom{x}{2}(1) + \binom{x}{3}(2) + \binom{x}{4}(9)$$

$$= 1 + \frac{x(x-1)}{2} + \frac{x(x-1)(x-2)}{3} + \frac{9x(x-1)(x-2)(x-3)}{24}$$

Simplificando:
$$\boxed{P(x) = \frac{3x^4 - 10x^3 + 15x^2 - 8x + 8}{8}}$$

---

## Solución Problema 12 (Error de Interpolación)

**Acotar [error de interpolación](../../../glossary.md#error-de-[interpolación](../../../glossary.md#interpolación)) lineal de $e^x$ en $[0, 1]$**

Fórmula del error:
$$|f(x) - P_1(x)| \leq \frac{M_2}{2!}|(x - x_0)(x - x_1)|$$

donde $M_2 = \max_{[0,1]} |f''(x)| = \max_{[0,1]} |e^x| = e$

El máximo de $|(x-0)(x-1)| = |x(x-1)|$ en $[0,1]$ ocurre en $x = 0.5$:
$$|0.5 \cdot (-0.5)| = 0.25$$

**Cota del error:**
$$\boxed{|f(x) - P_1(x)| \leq \frac{e \cdot 0.25}{2} = \frac{e}{8} \approx 0.34}$$

---

## Solución Problema 16 (Spline Cúbico Natural)

**Puntos:** $(0, 0)$, $(1, 1)$, $(2, 0)$

**Paso 1:** $h_0 = h_1 = 1$

**Paso 2:** Sistema para $c_i$ (con $c_0 = c_2 = 0$):

Solo una ecuación para $c_1$:
$$h_0 c_0 + 2(h_0 + h_1)c_1 + h_1 c_2 = 3\left(\frac{y_2 - y_1}{h_1} - \frac{y_1 - y_0}{h_0}\right)$$

$$0 + 4c_1 + 0 = 3\left(\frac{0-1}{1} - \frac{1-0}{1}\right) = 3(-2) = -6$$

$$c_1 = -1.5$$

**Paso 3:** Coeficientes para cada intervalo.

**Intervalo $[0, 1]$:**
- $a_0 = 0$
- $b_0 = \frac{y_1 - y_0}{h_0} - \frac{h_0}{3}(2c_0 + c_1) = 1 - \frac{1}{3}(-1.5) = 1.5$
- $c_0 = 0$
- $d_0 = \frac{c_1 - c_0}{3h_0} = \frac{-1.5}{3} = -0.5$

$$S_0(x) = 0 + 1.5x + 0 - 0.5x^3 = 1.5x - 0.5x^3$$

**Intervalo $[1, 2]$:**
- $a_1 = 1$
- $b_1 = \frac{y_2 - y_1}{h_1} - \frac{h_1}{3}(2c_1 + c_2) = -1 - \frac{1}{3}(-3) = 0$
- $c_1 = -1.5$
- $d_1 = \frac{c_2 - c_1}{3h_1} = \frac{1.5}{3} = 0.5$

$$S_1(x) = 1 + 0(x-1) - 1.5(x-1)^2 + 0.5(x-1)^3$$

**Spline completo:**
$$\boxed{S(x) = \begin{cases} 1.5x - 0.5x^3 & \text{si } 0 \leq x \leq 1 \\ 1 - 1.5(x-1)^2 + 0.5(x-1)^3 & \text{si } 1 \leq x \leq 2 \end{cases}}$$

**Verificación de [continuidad](../../../glossary.md#continuidad) en $x = 1$:**
- $S_0(1) = 1.5 - 0.5 = 1$ ✓
- $S_1(1) = 1$ ✓
- $S_0'(1) = 1.5 - 1.5 = 0$, $S_1'(1) = 0$ ✓
- $S_0''(1) = -3$, $S_1''(1) = -3$ ✓

---

## Solución Problema 20 (Hermite)

**Datos:** $f(0) = 1$, $f'(0) = 2$, $f(1) = 2$, $f'(1) = 0$

**Tabla ampliada** (puntos: $0, 0, 1, 1$):

| $z$ | $f[z]$ | 1er [orden](../../../glossary.md#orden) | 2do orden | 3er orden |
|-----|--------|-----------|-----------|-----------|
| 0 | 1 | | | |
| 0 | 1 | 2 (= $f'(0)$) | | |
| 1 | 2 | $\frac{2-1}{1} = 1$ | $\frac{1-2}{1} = -1$ | |
| 1 | 2 | 0 (= $f'(1)$) | $\frac{0-1}{1} = -1$ | $\frac{-1-(-1)}{1} = 0$ |

**Coeficientes:** $1, 2, -1, 0$

**Polinomio:**
$$H(x) = 1 + 2x + (-1)x \cdot x + 0 \cdot x \cdot x \cdot (x-1)$$
$$= 1 + 2x - x^2$$

$$\boxed{H(x) = -x^2 + 2x + 1}$$

**Verificación:**
- $H(0) = 1$ ✓
- $H'(x) = -2x + 2$, $H'(0) = 2$ ✓
- $H(1) = -1 + 2 + 1 = 2$ ✓
- $H'(1) = -2 + 2 = 0$ ✓

---

## Solución Problema 22 (Densidad del Agua)

**Estimar densidad a 50°C**

**a) Lagrange con puntos 40°C, 60°C, 80°C:**

$(40, 0.9922)$, $(60, 0.9832)$, $(80, 0.9718)$

$$L_0(50) = \frac{(50-60)(50-80)}{(40-60)(40-80)} = \frac{(-10)(-30)}{(-20)(-40)} = \frac{300}{800} = 0.375$$

$$L_1(50) = \frac{(50-40)(50-80)}{(60-40)(60-80)} = \frac{(10)(-30)}{(20)(-20)} = \frac{-300}{-400} = 0.75$$

$$L_2(50) = \frac{(50-40)(50-60)}{(80-40)(80-60)} = \frac{(10)(-10)}{(40)(20)} = \frac{-100}{800} = -0.125$$

$$\rho(50) = 0.9922(0.375) + 0.9832(0.75) + 0.9718(-0.125)$$
$$= 0.3721 + 0.7374 - 0.1215 = 0.9880$$

$$\boxed{\rho(50°C) \approx 0.9880 \text{ g/cm}^3}$$

(Valor real: 0.9881 g/cm³)
