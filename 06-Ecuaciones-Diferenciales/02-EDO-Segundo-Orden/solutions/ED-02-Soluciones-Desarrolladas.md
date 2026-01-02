<!--
::METADATA::
type: solution
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Soluciones: EDO de Segundo Orden

---

## Problema 1a
**Ecuación:** $y'' - 5y' + 6y = 0$

**Solución:**
$r^2 - 5r + 6 = 0$

$(r-2)(r-3) = 0 \Rightarrow r = 2, 3$

**$y = C_1 e^{2x} + C_2 e^{3x}$**

---

## Problema 2
**PVI:** $y'' - 3y' + 2y = 0$, $y(0) = 1$, $y'(0) = 0$

**Solución:**
$r^2 - 3r + 2 = 0 \Rightarrow r = 1, 2$

$y = C_1 e^x + C_2 e^{2x}$

$y(0) = C_1 + C_2 = 1$

$y' = C_1 e^x + 2C_2 e^{2x}$

$y'(0) = C_1 + 2C_2 = 0$

Restando: $C_2 = -1$, $C_1 = 2$

**$y = 2e^x - e^{2x}$**

---

## Problema 3a
**Ecuación:** $y'' - 4y' + 4y = 0$

**Solución:**
$r^2 - 4r + 4 = 0$

$(r-2)^2 = 0 \Rightarrow r = 2$ (doble)

**$y = (C_1 + C_2 x)e^{2x}$**

---

## Problema 5b
**Ecuación:** $y'' + 2y' + 5y = 0$

**Solución:**
$r^2 + 2r + 5 = 0$

$r = \frac{-2 \pm \sqrt{4-20}}{2} = \frac{-2 \pm 4i}{2} = -1 \pm 2i$

$\alpha = -1$, $\beta = 2$

**$y = e^{-x}(C_1 \cos 2x + C_2 \sin 2x)$**

---

## Problema 6
**PVI:** $y'' + 4y' + 8y = 0$, $y(0) = 1$, $y'(0) = 0$

**Solución:**
$r^2 + 4r + 8 = 0$

$r = \frac{-4 \pm \sqrt{16-32}}{2} = -2 \pm 2i$

$y = e^{-2x}(C_1 \cos 2x + C_2 \sin 2x)$

$y(0) = C_1 = 1$

$y' = e^{-2x}[(-2C_1 - 2C_2)\cos 2x + (-2C_2 + 2C_1)\sin 2x]$

$y'(0) = -2C_1 - 2C_2 = 0 \Rightarrow C_2 = -1$

**$y = e^{-2x}(\cos 2x - \sin 2x)$**

---

## Problema 9a
**Ecuación:** $y'' - 2y' + y = e^x$ (con duplicación)

**Solución:**
Homogénea: $r^2 - 2r + 1 = 0 \Rightarrow r = 1$ (doble)

$y_h = (C_1 + C_2 x)e^x$

$y_p = Ax^2 e^x$ (multiplicar por $x^2$ por doble duplicación)

$y_p' = A(2x + x^2)e^x$

$y_p'' = A(2 + 4x + x^2)e^x$

Sustituyendo:
$A(2 + 4x + x^2)e^x - 2A(2x + x^2)e^x + Ax^2 e^x = e^x$

$Ae^x[2 + 4x + x^2 - 4x - 2x^2 + x^2] = e^x$

$2A = 1 \Rightarrow A = \frac{1}{2}$

**$y = (C_1 + C_2 x)e^x + \frac{x^2}{2}e^x$**

---

## Problema 12a
**Ecuación:** $y'' + y = \sec x$ (Variación de parámetros)

**Solución:**
$y_h = C_1 \cos x + C_2 \sin x$

$y_1 = \cos x$, $y_2 = \sin x$

$W = \cos x \cdot \cos x - \sin x(-\sin x) = 1$

$u_1' = -\sin x \cdot \sec x = -\tan x$

$u_1 = \ln|\cos x|$

$u_2' = \cos x \cdot \sec x = 1$

$u_2 = x$

$y_p = \cos x \ln|\cos x| + x\sin x$

**$y = C_1 \cos x + C_2 \sin x + \cos x \ln|\cos x| + x\sin x$**

---

## Problema 15a
**Ecuación:** $x^2y'' - 2xy' - 4y = 0$ (Cauchy-Euler)

**Solución:**
Ecuación auxiliar: $m(m-1) - 2m - 4 = 0$

$m^2 - 3m - 4 = 0$

$(m-4)(m+1) = 0 \Rightarrow m = 4, -1$

**$y = C_1 x^4 + C_2 x^{-1}$**

---

## Problema 16a
**Ecuación:** $x^2y'' + xy' + 4y = 0$ (Raíces complejas)

**Solución:**
$m(m-1) + m + 4 = 0$

$m^2 + 4 = 0 \Rightarrow m = \pm 2i$

$\alpha = 0$, $\beta = 2$

**$y = C_1 \cos(2\ln x) + C_2 \sin(2\ln x)$**

---

## Problema 20
**Sistema masa-resorte sin amortiguamiento**

$m = 2$ kg, $k = 18$ N/m

a) $2\ddot{x} + 18x = 0$ → $\ddot{x} + 9x = 0$

b) $r^2 + 9 = 0 \Rightarrow r = \pm 3i$

$x = C_1\cos 3t + C_2\sin 3t$

$x(0) = 0.1$: $C_1 = 0.1$

$\dot{x} = -3C_1\sin 3t + 3C_2\cos 3t$

$\dot{x}(0) = 0$: $C_2 = 0$

**$x(t) = 0.1\cos 3t$ m**

c) $\omega = 3$ rad/s, $f = \frac{3}{2\pi} \approx 0.477$ Hz, $T = \frac{2\pi}{3} \approx 2.09$ s

---

## Problema 21
**Sistema amortiguado:** $m = 1$, $c = 2$, $k = 5$

a) $\ddot{x} + 2\dot{x} + 5x = 0$

$\omega_0 = \sqrt{5}$, $\zeta = \frac{2}{2\sqrt{5}} = \frac{1}{\sqrt{5}} \approx 0.447 < 1$

**Subamortiguado**

b) $r^2 + 2r + 5 = 0 \Rightarrow r = -1 \pm 2i$

$x = e^{-t}(C_1\cos 2t + C_2\sin 2t)$

$x(0) = 1$: $C_1 = 1$

$\dot{x} = e^{-t}[(-C_1 - 2C_2)\cos 2t + (-C_2 + 2C_1)\sin 2t]$

$\dot{x}(0) = -C_1 - 2C_2 = 0 \Rightarrow C_2 = -\frac{1}{2}$

**$x(t) = e^{-t}(\cos 2t - \frac{1}{2}\sin 2t)$**

c) $\omega_d = 2$ rad/s

---

## Problema 25
**Circuito RLC:** $L = 1$ H, $R = 6$ Ω, $C = 1/9$ F

a) $\frac{d^2q}{dt^2} + 6\frac{dq}{dt} + 9q = 0$

b) $r^2 + 6r + 9 = 0 \Rightarrow r = -3$ (doble)

**Críticamente amortiguado**

c) $q = (C_1 + C_2 t)e^{-3t}$

$q(0) = C_1 = 1$

$\dot{q} = (C_2 - 3C_1 - 3C_2 t)e^{-3t}$

$i(0) = C_2 - 3 = 0 \Rightarrow C_2 = 3$

**$q(t) = (1 + 3t)e^{-3t}$ C**

---

## Problema 29b
**Encontrar [EDO](../../../glossary.md#edo) con solución:** $y = e^{2x}(C_1\cos 3x + C_2\sin 3x)$

**Solución:**
Las raíces son $r = 2 \pm 3i$

Ecuación característica: $(r - 2 - 3i)(r - 2 + 3i) = 0$

$[(r-2) - 3i][(r-2) + 3i] = (r-2)^2 + 9 = 0$

$r^2 - 4r + 4 + 9 = 0$

$r^2 - 4r + 13 = 0$

**$y'' - 4y' + 13y = 0$**
