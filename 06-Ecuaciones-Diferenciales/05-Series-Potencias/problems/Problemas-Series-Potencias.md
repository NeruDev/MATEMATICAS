<!--
content_type: problems
topic: Series de Potencias para EDO
---
-->

# Problemas: Series de Potencias para EDO

---

## 5.1 Repaso de Series

**Problema 1.** Encontrar el radio de convergencia:

a) $\sum_{n=0}^{\infty} \frac{x^n}{n!}$

b) $\sum_{n=0}^{\infty} n! x^n$

c) $\sum_{n=1}^{\infty} \frac{x^n}{n}$

d) $\sum_{n=0}^{\infty} \frac{(x-2)^n}{3^n}$

**Problema 2.** Expresar como serie de potencias centrada en $x = 0$:

a) $\frac{1}{1+x}$

b) $e^{-x^2}$

c) $\ln(1+x)$

---

## 5.2 Puntos Ordinarios

**Problema 3.** Clasificar $x = 0$ como punto ordinario o singular:

a) $y'' + xy' + y = 0$

b) $xy'' + y' + y = 0$

c) $(x^2-1)y'' + xy' + y = 0$

d) $x^2y'' + xy' + (x^2-1)y = 0$

**Problema 4.** Resolver en serie de potencias alrededor de $x = 0$:

a) $y'' + y = 0$

b) $y'' - y = 0$

c) $y' - y = 0$

**Problema 5.** Encontrar la solución en serie hasta el término $x^5$:

a) $y'' - xy = 0$ (ecuación de Airy)

b) $y'' - 2xy' + 2y = 0$ (Hermite con $n = 1$)

c) $(1-x^2)y'' - 2xy' + 2y = 0$ (Legendre con $n = 1$)

**Problema 6.** Resolver el PVI en serie:

a) $y'' + xy' + y = 0$, $y(0) = 1$, $y'(0) = 0$

b) $y'' - x^2y = 0$, $y(0) = 0$, $y'(0) = 1$

**Problema 7.** Encontrar la relación de recurrencia:

a) $y'' + x^2y = 0$

b) $(1+x^2)y'' + 2xy' - 2y = 0$

---

## 5.3 Puntos Singulares Regulares

**Problema 8.** Clasificar el punto $x = 0$ como singular regular o irregular:

a) $x^2y'' + xy' + (x^2-1)y = 0$

b) $x^3y'' + xy' + y = 0$

c) $xy'' + y' + xy = 0$

d) $x^2y'' + (x + x^2)y' + y = 0$

**Problema 9.** Encontrar la ecuación indicial y sus raíces:

a) $2xy'' + y' - y = 0$

b) $x^2y'' + xy' + (x^2 - \frac{1}{4})y = 0$

c) $xy'' + y = 0$

d) $x^2y'' - xy' + y = 0$

**Problema 10.** Determinar qué caso de Frobenius aplica (1, 2 o 3):

a) $xy'' + y' + y = 0$ (raíces: $0, 0$)

b) $x^2y'' + xy' + (x^2-4)y = 0$ (raíces: $2, -2$)

c) $2x^2y'' + 3xy' - (1+x)y = 0$ (raíces: $1, -\frac{1}{2}$)

---

## 5.4 Método de Frobenius

**Problema 11.** Usar el método de Frobenius para encontrar una solución:

a) $2xy'' + y' + y = 0$

b) $xy'' + y' - y = 0$

c) $x^2y'' + xy' + (x^2 - 1)y = 0$ (Bessel, $\nu = 1$)

**Problema 12.** Encontrar los primeros cuatro términos no nulos de cada solución:

a) $x^2y'' - xy' + (1-x)y = 0$

b) $xy'' + (1-x)y' - y = 0$

**Problema 13.** Resolver cerca de $x = 0$:

a) $xy'' + 2y' + xy = 0$

b) $x^2y'' + x(x-1)y' + y = 0$

---

## 5.5 Ecuaciones Especiales

**Problema 14.** Verificar que las siguientes son soluciones:

a) $y = J_0(x) = 1 - \frac{x^2}{4} + \frac{x^4}{64} - ...$ satisface $x^2y'' + xy' + x^2y = 0$

b) $y = P_2(x) = \frac{1}{2}(3x^2 - 1)$ satisface $(1-x^2)y'' - 2xy' + 6y = 0$

**Problema 15.** Ecuación de Bessel:

a) Encontrar la ecuación indicial para $x^2y'' + xy' + (x^2 - \nu^2)y = 0$

b) Para $\nu = 0$, encontrar los primeros cuatro términos de $J_0(x)$

c) Para $\nu = 1$, encontrar los primeros tres términos de $J_1(x)$

**Problema 16.** Ecuación de Legendre:

a) Verificar que $(1-x^2)y'' - 2xy' + n(n+1)y = 0$ tiene $x = 0$ como punto ordinario

b) Para $n = 2$, encontrar $P_2(x)$

c) Verificar la ortogonalidad: $\int_{-1}^{1} P_1(x)P_2(x)\,dx = 0$

---

## 5.6 Aplicaciones

**Problema 17.** (Ecuación de Airy) La ecuación $y'' - xy = 0$ aparece en óptica y mecánica cuántica.

a) Verificar que $x = 0$ es punto ordinario

b) Encontrar la solución en serie hasta $x^6$

c) Usar las condiciones $y(0) = 1$, $y'(0) = 0$ para encontrar $\text{Ai}(x)$

**Problema 18.** (Oscilador cuántico) La ecuación de Schrödinger para el oscilador armónico da:

$\psi'' + (2E - x^2)\psi = 0$

Para $E = \frac{1}{2}$:

a) Encontrar una solución en serie

b) Verificar que $\psi = e^{-x^2/2}$ es solución

**Problema 19.** (Conducción de calor en cilindro) La distribución de temperatura satisface:

$r^2\frac{d^2T}{dr^2} + r\frac{dT}{dr} + \lambda^2 r^2 T = 0$

a) Identificar esta como ecuación de Bessel

b) ¿Cuál es la solución acotada en $r = 0$?

**Problema 20.** (Potencial electrostático) El potencial cerca de una esfera satisface:

$(1-x^2)\frac{d^2V}{dx^2} - 2x\frac{dV}{dx} + n(n+1)V = 0$

donde $x = \cos\theta$.

a) Identificar como ecuación de Legendre

b) Para $n = 3$, encontrar $P_3(x)$
