<!--
---
content_type: problem_set
topic_id: ed-04-transformada-laplace
file_id: ED-04-Problemas
created: 2025-12-20
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Problemas: Transformada de Laplace

---

## 4.1 Transformadas Básicas

### [Prob-01] Transformadas de funciones elementales ⭐

Calcular la [transformada de Laplace](../../../glossary.md#transformada-de-laplace):

a) $f(t) = 5$

b) $f(t) = t^3$

c) $f(t) = e^{-4t}$

d) $f(t) = \sin 5t$

e) $f(t) = \cos 2t$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-01)

---

### [Prob-02] Transformadas de combinaciones lineales ⭐

Calcular $\mathcal{L}\{f\}$:

a) $f(t) = 3t^2 - 2t + 1$

b) $f(t) = 4e^{2t} - 3e^{-t}$

c) $f(t) = 2\cos 3t + 5\sin 3t$

d) $f(t) = \cosh 2t - \sinh 2t$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-02)

---

## 4.2 Primera Traslación (en $s$)

### [Prob-03] Propiedad de traslación en s ⭐⭐

Calcular usando la propiedad de traslación en $s$:

a) $\mathcal{L}\{e^{3t}t^2\}$

b) $\mathcal{L}\{e^{-2t}\sin 4t\}$

c) $\mathcal{L}\{e^{t}\cos 3t\}$

d) $\mathcal{L}\{e^{-t}(t^2 + 2t)\}$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-03)

---

### [Prob-04] Traslación con combinaciones ⭐⭐

Calcular:

a) $\mathcal{L}\{e^{2t}(3\cos 5t - 4\sin 5t)\}$

b) $\mathcal{L}\{te^{-3t}\sin 2t\}$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-04)

---

## 4.3 Transformadas de Derivadas

### [Prob-05] Transformada de derivadas ⭐⭐

Si $\mathcal{L}\{f(t)\} = F(s)$, expresar en términos de $F(s)$ y condiciones iniciales:

a) $\mathcal{L}\{f'(t)\}$ con $f(0) = 2$

b) $\mathcal{L}\{f''(t)\}$ con $f(0) = 1$, $f'(0) = -3$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-05)

---

### [Prob-06] Multiplicación por t ⭐⭐

Usar la propiedad de multiplicación por $t$:

a) $\mathcal{L}\{t\sin 2t\}$

b) $\mathcal{L}\{t\cos t\}$

c) $\mathcal{L}\{t^2 e^{-t}\}$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-06)

---

## 4.4 Transformada Inversa

### [Prob-07] Transformada inversa básica ⭐

Calcular la transformada inversa:

a) $F(s) = \frac{3}{s^4}$

b) $F(s) = \frac{2}{s-5}$

c) $F(s) = \frac{4}{s^2+16}$

d) $F(s) = \frac{s}{s^2+9}$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-07)

---

### [Prob-08] Fracciones parciales simples ⭐⭐

Usar [fracciones parciales](../../../glossary.md#fracciones-parciales):

a) $F(s) = \frac{1}{s(s-2)}$

b) $F(s) = \frac{s+3}{(s-1)(s+2)}$

c) $F(s) = \frac{2s-1}{s^2-4}$

d) $F(s) = \frac{s}{(s+1)(s^2+1)}$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-08)

---

### [Prob-09] Fracciones parciales con factores repetidos ⭐⭐

Calcular (factores repetidos):

a) $F(s) = \frac{1}{s^2(s+1)}$

b) $F(s) = \frac{s}{(s-1)^2}$

c) $F(s) = \frac{2s+3}{(s+1)^3}$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-09)

---

### [Prob-10] Completar el cuadrado ⭐⭐

Completar el cuadrado:

a) $F(s) = \frac{1}{s^2+2s+5}$

b) $F(s) = \frac{s+1}{s^2+4s+8}$

c) $F(s) = \frac{2s-3}{s^2-6s+13}$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-10)

---

## 4.5 Resolver PVI

### [Prob-11] PVI de primer orden ⭐⭐

Resolver usando [transformada de Laplace](../../../glossary.md#transformada-de-laplace):

a) $y' + 2y = 0$, $y(0) = 3$

b) $y' - y = e^{2t}$, $y(0) = 1$

c) $y' + 3y = \sin t$, $y(0) = 0$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-11)

---

### [Prob-12] PVI de segundo orden homogéneo ⭐⭐

Resolver:

a) $y'' + 4y = 0$, $y(0) = 1$, $y'(0) = 0$

b) $y'' - y = 0$, $y(0) = 0$, $y'(0) = 2$

c) $y'' + 2y' + y = 0$, $y(0) = 1$, $y'(0) = 1$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-12)

---

### [Prob-13] PVI de segundo orden no homogéneo ⭐⭐

Resolver:

a) $y'' + 4y = \sin 2t$, $y(0) = 0$, $y'(0) = 0$

b) $y'' - 3y' + 2y = e^t$, $y(0) = 0$, $y'(0) = 0$

c) $y'' + y = t$, $y(0) = 1$, $y'(0) = 0$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-13)

---

### [Prob-14] PVI avanzados ⭐⭐⭐

Resolver:

a) $y'' + 2y' + 5y = e^{-t}\sin 2t$, $y(0) = 0$, $y'(0) = 0$

b) $y''' - y' = 0$, $y(0) = 0$, $y'(0) = 1$, $y''(0) = 0$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-14)

---

## 4.6 Funciones Escalón

### [Prob-15] Expresión con función escalón ⭐⭐

Escribir usando la [función](../../../glossary.md#funcion) escalón unitario:

a) $f(t) = \begin{cases} 0, & t < 3 \\ 2, & t \geq 3 \end{cases}$

b) $f(t) = \begin{cases} t, & 0 \leq t < 2 \\ 4-t, & t \geq 2 \end{cases}$

c) $f(t) = \begin{cases} 1, & 0 \leq t < 1 \\ 0, & 1 \leq t < 2 \\ 1, & t \geq 2 \end{cases}$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-15)

---

### [Prob-16] Transformada de función escalón ⭐⭐

Calcular la transformada:

a) $\mathcal{L}\{u(t-2)\}$

b) $\mathcal{L}\{(t-1)u(t-1)\}$

c) $\mathcal{L}\{e^{-(t-3)}u(t-3)\}$

d) $\mathcal{L}\{\sin(t-\pi)u(t-\pi)\}$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-16)

---

### [Prob-17] Transformada inversa con exponencial ⭐⭐

Calcular la transformada inversa:

a) $F(s) = \frac{e^{-2s}}{s}$

b) $F(s) = \frac{e^{-s}}{s^2}$

c) $F(s) = \frac{se^{-\pi s}}{s^2+1}$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-17)

---

## 4.7 Función Delta de Dirac

### [Prob-18] Ecuaciones con delta de Dirac ⭐⭐⭐

Resolver:

a) $y' + y = \delta(t-1)$, $y(0) = 0$

b) $y'' + 4y = \delta(t-\pi)$, $y(0) = 0$, $y'(0) = 0$

c) $y'' + 2y' + y = \delta(t)$, $y(0) = 0$, $y'(0) = 0$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-18)

---

## 4.8 Convolución

### [Prob-19] Transformada inversa por convolución ⭐⭐⭐

Calcular usando [convolución](../../../glossary.md#convolucion):

a) $\mathcal{L}^{-1}\left\{\frac{1}{s^2(s-1)}\right\}$

b) $\mathcal{L}^{-1}\left\{\frac{1}{(s-1)(s-2)}\right\}$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-19)

---

### [Prob-20] Teorema de convolución ⭐⭐⭐

Usar el teorema de [convolución](../../../glossary.md#convolucion) para resolver:

$y'' + y = f(t)$, $y(0) = 0$, $y'(0) = 0$

donde la solución es $(f * \sin)(t)$

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-20)

---

## 4.9 Aplicaciones

### [Prob-21] Circuito RC ⭐⭐

En un circuito RC con $R = 100$ Ω, $C = 0.01$ F:
$$R\frac{dq}{dt} + \frac{q}{C} = E(t)$$

Si $E(t) = 10$ V constante y $q(0) = 0$, encontrar $q(t)$.

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-21)

---

### [Prob-22] Circuito RLC ⭐⭐⭐

Con $L = 1$ H, $R = 2$ Ω, $C = 0.5$ F y $E = 10u(t)$ V:
$$L\frac{d^2i}{dt^2} + R\frac{di}{dt} + \frac{i}{C} = \frac{dE}{dt}$$

Resolver con $i(0) = 0$, $i'(0) = 10$.

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-22)

---

### [Prob-23] Sistema masa-resorte con impulso ⭐⭐⭐

Un sistema con $m = 1$ kg, $k = 4$ N/m recibe un impulso en $t = 2$ s:
$$\ddot{x} + 4x = 3\delta(t-2)$$

Resolver con $x(0) = 0$, $\dot{x}(0) = 0$.

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-23)

---

### [Prob-24] Deflexión de viga ⭐⭐⭐

La deflexión $y(x)$ de una viga satisface:
$$EI\frac{d^4y}{dx^4} = w(x)$$

Si $w(x) = w_0[u(x) - u(x-L/2)]$ y las condiciones son $y(0) = y'(0) = 0$, encontrar $Y(s)$.

> **Solución:** Ver [📎 Ver Respuesta](../solutions/ED-04-Respuestas.md#prob-24)
