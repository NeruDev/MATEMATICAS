<!--
::METADATA::
type: solution
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Soluciones: EDO de Primer Orden

---

## Problema 4a
**Enunciado:** Resolver $\frac{dy}{dx} = \frac{x^2}{y}$

**Solución:**

Separando: $y\,dy = x^2\,dx$

Integrando: $\frac{y^2}{2} = \frac{x^3}{3} + C$

**Solución:** $y^2 = \frac{2x^3}{3} + C_1$ o $3y^2 - 2x^3 = C$

---

## Problema 5
**Enunciado:** PVI: $\frac{dy}{dx} = \frac{y^2}{x}$, $y(1) = 1$

**Solución:**

Separando: $\frac{dy}{y^2} = \frac{dx}{x}$

Integrando: $-\frac{1}{y} = \ln|x| + C$

Aplicando $y(1) = 1$: $-1 = 0 + C \Rightarrow C = -1$

$-\frac{1}{y} = \ln|x| - 1$

**Solución:** $y = \frac{1}{1 - \ln|x|}$

---

## Problema 8a
**Enunciado:** Resolver $\frac{dy}{dx} + 2y = e^{-x}$

**Solución:**

$P(x) = 2$, $Q(x) = e^{-x}$

$\mu = e^{\int 2dx} = e^{2x}$

$e^{2x}y = \int e^{2x} \cdot e^{-x}dx = \int e^x dx = e^x + C$

**Solución:** $y = e^{-x} + Ce^{-2x}$

---

## Problema 9
**Enunciado:** PVI: $\frac{dy}{dx} + y = e^x$, $y(0) = 1$

**Solución:**

$\mu = e^{\int 1dx} = e^x$

$e^x y = \int e^x \cdot e^x dx = \int e^{2x}dx = \frac{e^{2x}}{2} + C$

$y = \frac{e^x}{2} + Ce^{-x}$

Aplicando $y(0) = 1$: $1 = \frac{1}{2} + C \Rightarrow C = \frac{1}{2}$

**Solución:** $y = \frac{e^x + e^{-x}}{2} = \cosh x$

---

## Problema 12a
**Enunciado:** $(2xy + 3)dx + (x^2 - 1)dy = 0$

**Solución:**

$M = 2xy + 3$, $N = x^2 - 1$

$M_y = 2x$, $N_x = 2x$ ✓ Es exacta

$F = \int (2xy + 3)dx = x^2y + 3x + g(y)$

$\frac{\partial F}{\partial y} = x^2 + g'(y) = x^2 - 1$

$g'(y) = -1 \Rightarrow g(y) = -y$

**Solución:** $x^2y + 3x - y = C$

---

## Problema 15a
**Enunciado:** $(y + 1)dx - xdy = 0$

**Solución:**

$M = y + 1$, $N = -x$

$M_y = 1$, $N_x = -1$, $M_y - N_x = 2$

$\frac{M_y - N_x}{N} = \frac{2}{-x} = -\frac{2}{x}$ (depende solo de $x$)

$\mu = e^{\int -\frac{2}{x}dx} = x^{-2}$

Multiplicando: $\frac{y+1}{x^2}dx - \frac{1}{x}dy = 0$

Verificar: $\tilde{M}_y = \frac{1}{x^2}$, $\tilde{N}_x = \frac{1}{x^2}$ ✓

$F = \int \frac{y+1}{x^2}dx = -\frac{y+1}{x} + g(y)$

$\frac{\partial F}{\partial y} = -\frac{1}{x} + g'(y) = -\frac{1}{x}$

$g'(y) = 0 \Rightarrow g(y) = 0$

**Solución:** $\frac{y+1}{x} = C$ o $y = Cx - 1$

---

## Problema 18a
**Enunciado:** $\frac{dy}{dx} + y = y^2$ (Bernoulli con $n = 2$)

**Solución:**

$v = y^{1-2} = y^{-1}$, $\frac{dv}{dx} = -y^{-2}\frac{dy}{dx}$

Dividiendo por $y^2$: $y^{-2}\frac{dy}{dx} + y^{-1} = 1$

$-\frac{dv}{dx} + v = 1$

$\frac{dv}{dx} - v = -1$ (lineal)

$\mu = e^{-x}$

$e^{-x}v = \int -e^{-x}dx = e^{-x} + C$

$v = 1 + Ce^x$

**Solución:** $y = \frac{1}{1 + Ce^x}$

---

## Problema 21a
**Enunciado:** $\frac{dy}{dx} = \frac{x + y}{x}$ (Homogénea)

**Solución:**

$\frac{dy}{dx} = 1 + \frac{y}{x} = 1 + v$

Con $y = vx$: $v + x\frac{dv}{dx} = 1 + v$

$x\frac{dv}{dx} = 1$

$dv = \frac{dx}{x}$

$v = \ln|x| + C$

$\frac{y}{x} = \ln|x| + C$

**Solución:** $y = x\ln|x| + Cx$

---

## Problema 24
**Enunciado:** Decaimiento radiactivo

**Solución:**

$\frac{dN}{dt} = -kN \Rightarrow N = N_0 e^{-kt}$

$N_0 = 100$, $N(10) = 60$

$60 = 100e^{-10k}$

$e^{-10k} = 0.6 \Rightarrow k = -\frac{\ln 0.6}{10} \approx 0.0511$

$N(25) = 100e^{-0.0511 \cdot 25} = 100e^{-1.278}$

**$N(25) \approx 27.9$ g**

---

## Problema 26
**Enunciado:** Circuito RL: $2\frac{di}{dt} + 4i = 12$, $i(0) = 0$

**Solución:**

$\frac{di}{dt} + 2i = 6$

$\mu = e^{2t}$

$e^{2t}i = \int 6e^{2t}dt = 3e^{2t} + C$

$i = 3 + Ce^{-2t}$

$i(0) = 0$: $0 = 3 + C \Rightarrow C = -3$

**Solución:** $i(t) = 3(1 - e^{-2t})$ A

Corriente estacionaria: $i_\infty = 3$ A

---

## Problema 27
**Enunciado:** Tanque con mezcla

**Solución:**

Sea $S(t)$ = kg de sal en tiempo $t$

Entrada: $3 \cdot 0.2 = 0.6$ kg/min

Salida: $\frac{S}{100} \cdot 3 = 0.03S$ kg/min

$\frac{dS}{dt} = 0.6 - 0.03S$

$\frac{dS}{dt} + 0.03S = 0.6$

$\mu = e^{0.03t}$

$e^{0.03t}S = \int 0.6e^{0.03t}dt = 20e^{0.03t} + C$

$S = 20 + Ce^{-0.03t}$

$S(0) = 10$: $C = -10$

**Solución:** $S(t) = 20 - 10e^{-0.03t}$ kg

Cantidad de equilibrio: $S_\infty = 20$ kg
