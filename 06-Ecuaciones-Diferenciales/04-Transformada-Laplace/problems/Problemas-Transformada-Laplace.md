<!--
content_type: problems
topic: Transformada de Laplace
---
-->

# Problemas: Transformada de Laplace

---

## 4.1 Transformadas Básicas

**Problema 1.** Calcular la transformada de Laplace:

a) $f(t) = 5$

b) $f(t) = t^3$

c) $f(t) = e^{-4t}$

d) $f(t) = \sin 5t$

e) $f(t) = \cos 2t$

**Problema 2.** Calcular $\mathcal{L}\{f\}$:

a) $f(t) = 3t^2 - 2t + 1$

b) $f(t) = 4e^{2t} - 3e^{-t}$

c) $f(t) = 2\cos 3t + 5\sin 3t$

d) $f(t) = \cosh 2t - \sinh 2t$

---

## 4.2 Primera Traslación (en $s$)

**Problema 3.** Calcular usando la propiedad de traslación en $s$:

a) $\mathcal{L}\{e^{3t}t^2\}$

b) $\mathcal{L}\{e^{-2t}\sin 4t\}$

c) $\mathcal{L}\{e^{t}\cos 3t\}$

d) $\mathcal{L}\{e^{-t}(t^2 + 2t)\}$

**Problema 4.** Calcular:

a) $\mathcal{L}\{e^{2t}(3\cos 5t - 4\sin 5t)\}$

b) $\mathcal{L}\{te^{-3t}\sin 2t\}$

---

## 4.3 Transformadas de Derivadas

**Problema 5.** Si $\mathcal{L}\{f(t)\} = F(s)$, expresar en términos de $F(s)$ y condiciones iniciales:

a) $\mathcal{L}\{f'(t)\}$ con $f(0) = 2$

b) $\mathcal{L}\{f''(t)\}$ con $f(0) = 1$, $f'(0) = -3$

**Problema 6.** Usar la propiedad de multiplicación por $t$:

a) $\mathcal{L}\{t\sin 2t\}$

b) $\mathcal{L}\{t\cos t\}$

c) $\mathcal{L}\{t^2 e^{-t}\}$

---

## 4.4 Transformada Inversa

**Problema 7.** Calcular la transformada inversa:

a) $F(s) = \frac{3}{s^4}$

b) $F(s) = \frac{2}{s-5}$

c) $F(s) = \frac{4}{s^2+16}$

d) $F(s) = \frac{s}{s^2+9}$

**Problema 8.** Usar fracciones parciales:

a) $F(s) = \frac{1}{s(s-2)}$

b) $F(s) = \frac{s+3}{(s-1)(s+2)}$

c) $F(s) = \frac{2s-1}{s^2-4}$

d) $F(s) = \frac{s}{(s+1)(s^2+1)}$

**Problema 9.** Calcular (factores repetidos):

a) $F(s) = \frac{1}{s^2(s+1)}$

b) $F(s) = \frac{s}{(s-1)^2}$

c) $F(s) = \frac{2s+3}{(s+1)^3}$

**Problema 10.** Completar el cuadrado:

a) $F(s) = \frac{1}{s^2+2s+5}$

b) $F(s) = \frac{s+1}{s^2+4s+8}$

c) $F(s) = \frac{2s-3}{s^2-6s+13}$

---

## 4.5 Resolver PVI

**Problema 11.** Resolver usando transformada de Laplace:

a) $y' + 2y = 0$, $y(0) = 3$

b) $y' - y = e^{2t}$, $y(0) = 1$

c) $y' + 3y = \sin t$, $y(0) = 0$

**Problema 12.** Resolver:

a) $y'' + 4y = 0$, $y(0) = 1$, $y'(0) = 0$

b) $y'' - y = 0$, $y(0) = 0$, $y'(0) = 2$

c) $y'' + 2y' + y = 0$, $y(0) = 1$, $y'(0) = 1$

**Problema 13.** Resolver:

a) $y'' + 4y = \sin 2t$, $y(0) = 0$, $y'(0) = 0$

b) $y'' - 3y' + 2y = e^t$, $y(0) = 0$, $y'(0) = 0$

c) $y'' + y = t$, $y(0) = 1$, $y'(0) = 0$

**Problema 14.** Resolver:

a) $y'' + 2y' + 5y = e^{-t}\sin 2t$, $y(0) = 0$, $y'(0) = 0$

b) $y''' - y' = 0$, $y(0) = 0$, $y'(0) = 1$, $y''(0) = 0$

---

## 4.6 Funciones Escalón

**Problema 15.** Escribir usando la función escalón unitario:

a) $f(t) = \begin{cases} 0, & t < 3 \\ 2, & t \geq 3 \end{cases}$

b) $f(t) = \begin{cases} t, & 0 \leq t < 2 \\ 4-t, & t \geq 2 \end{cases}$

c) $f(t) = \begin{cases} 1, & 0 \leq t < 1 \\ 0, & 1 \leq t < 2 \\ 1, & t \geq 2 \end{cases}$

**Problema 16.** Calcular la transformada:

a) $\mathcal{L}\{u(t-2)\}$

b) $\mathcal{L}\{(t-1)u(t-1)\}$

c) $\mathcal{L}\{e^{-(t-3)}u(t-3)\}$

d) $\mathcal{L}\{\sin(t-\pi)u(t-\pi)\}$

**Problema 17.** Calcular la transformada inversa:

a) $F(s) = \frac{e^{-2s}}{s}$

b) $F(s) = \frac{e^{-s}}{s^2}$

c) $F(s) = \frac{se^{-\pi s}}{s^2+1}$

---

## 4.7 Función Delta de Dirac

**Problema 18.** Resolver:

a) $y' + y = \delta(t-1)$, $y(0) = 0$

b) $y'' + 4y = \delta(t-\pi)$, $y(0) = 0$, $y'(0) = 0$

c) $y'' + 2y' + y = \delta(t)$, $y(0) = 0$, $y'(0) = 0$

---

## 4.8 Convolución

**Problema 19.** Calcular usando convolución:

a) $\mathcal{L}^{-1}\left\{\frac{1}{s^2(s-1)}\right\}$

b) $\mathcal{L}^{-1}\left\{\frac{1}{(s-1)(s-2)}\right\}$

**Problema 20.** Usar el teorema de convolución para resolver:

$y'' + y = f(t)$, $y(0) = 0$, $y'(0) = 0$

donde la solución es $(f * \sin)(t)$

---

## 4.9 Aplicaciones

**Problema 21.** (Circuito RC) En un circuito RC con $R = 100$ Ω, $C = 0.01$ F:
$$R\frac{dq}{dt} + \frac{q}{C} = E(t)$$

Si $E(t) = 10$ V constante y $q(0) = 0$, encontrar $q(t)$.

**Problema 22.** (Circuito RLC) Con $L = 1$ H, $R = 2$ Ω, $C = 0.5$ F y $E = 10u(t)$ V:
$$L\frac{d^2i}{dt^2} + R\frac{di}{dt} + \frac{i}{C} = \frac{dE}{dt}$$

Resolver con $i(0) = 0$, $i'(0) = 10$.

**Problema 23.** (Sistema masa-resorte) Un sistema con $m = 1$ kg, $k = 4$ N/m recibe un impulso en $t = 2$ s:
$$\ddot{x} + 4x = 3\delta(t-2)$$

Resolver con $x(0) = 0$, $\dot{x}(0) = 0$.

**Problema 24.** (Viga) La deflexión $y(x)$ de una viga satisface:
$$EI\frac{d^4y}{dx^4} = w(x)$$

Si $w(x) = w_0[u(x) - u(x-L/2)]$ y las condiciones son $y(0) = y'(0) = 0$, encontrar $Y(s)$.
