<!--
::METADATA::
type: solution
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Soluciones: Transformada de Laplace

---

## Problema 1

a) $\mathcal{L}\{5\} = \frac{5}{s}$

b) $\mathcal{L}\{t^3\} = \frac{3!}{s^4} = \frac{6}{s^4}$

c) $\mathcal{L}\{e^{-4t}\} = \frac{1}{s+4}$

d) $\mathcal{L}\{\sin 5t\} = \frac{5}{s^2+25}$

e) $\mathcal{L}\{\cos 2t\} = \frac{s}{s^2+4}$

---

## Problema 2a
$\mathcal{L}\{3t^2 - 2t + 1\} = 3 \cdot \frac{2}{s^3} - 2 \cdot \frac{1}{s^2} + \frac{1}{s} = \frac{6}{s^3} - \frac{2}{s^2} + \frac{1}{s}$

---

## Problema 3a
$\mathcal{L}\{e^{3t}t^2\}$

$\mathcal{L}\{t^2\} = \frac{2}{s^3}$

Traslación $s \to s-3$:

$$\mathcal{L}\{e^{3t}t^2\} = \frac{2}{(s-3)^3}$$

---

## Problema 3b
$\mathcal{L}\{e^{-2t}\sin 4t\}$

$\mathcal{L}\{\sin 4t\} = \frac{4}{s^2+16}$

Traslación $s \to s+2$:

$$\mathcal{L}\{e^{-2t}\sin 4t\} = \frac{4}{(s+2)^2+16}$$

---

## Problema 6a
$\mathcal{L}\{t\sin 2t\}$

$\mathcal{L}\{\sin 2t\} = \frac{2}{s^2+4}$

$\mathcal{L}\{tf(t)\} = -F'(s)$

$F'(s) = -\frac{2 \cdot 2s}{(s^2+4)^2} = -\frac{4s}{(s^2+4)^2}$

$$\mathcal{L}\{t\sin 2t\} = \frac{4s}{(s^2+4)^2}$$

---

## Problema 8b
$F(s) = \frac{s+3}{(s-1)(s+2)}$

[Fracciones parciales](../../../glossary.md#fracciones-parciales):
$\frac{s+3}{(s-1)(s+2)} = \frac{A}{s-1} + \frac{B}{s+2}$

$s+3 = A(s+2) + B(s-1)$

$s = 1$: $4 = 3A \Rightarrow A = \frac{4}{3}$

$s = -2$: $1 = -3B \Rightarrow B = -\frac{1}{3}$

$$\mathcal{L}^{-1} = \frac{4}{3}e^t - \frac{1}{3}e^{-2t}$$

---

## Problema 9a
$F(s) = \frac{1}{s^2(s+1)}$

$\frac{1}{s^2(s+1)} = \frac{A}{s} + \frac{B}{s^2} + \frac{C}{s+1}$

$1 = As(s+1) + B(s+1) + Cs^2$

$s = 0$: $1 = B$

$s = -1$: $1 = C$

$s = 1$: $1 = 2A + 2B + C = 2A + 3 \Rightarrow A = -1$

$$\mathcal{L}^{-1} = -1 + t + e^{-t}$$

---

## Problema 10a
$F(s) = \frac{1}{s^2+2s+5}$

Completar cuadrado: $s^2+2s+5 = (s+1)^2 + 4$

$\frac{1}{(s+1)^2+4} = \frac{1}{2} \cdot \frac{2}{(s+1)^2+4}$

$$\mathcal{L}^{-1} = \frac{1}{2}e^{-t}\sin 2t$$

---

## Problema 11a
$y' + 2y = 0$, $y(0) = 3$

$sY - 3 + 2Y = 0$

$Y(s+2) = 3$

$Y = \frac{3}{s+2}$

$$y(t) = 3e^{-2t}$$

---

## Problema 12a
$y'' + 4y = 0$, $y(0) = 1$, $y'(0) = 0$

$s^2Y - s + 4Y = 0$

$Y(s^2+4) = s$

$Y = \frac{s}{s^2+4}$

$$y(t) = \cos 2t$$

---

## Problema 13a
$y'' + 4y = \sin 2t$, $y(0) = 0$, $y'(0) = 0$

$s^2Y + 4Y = \frac{2}{s^2+4}$

$Y = \frac{2}{(s^2+4)^2}$

Usando tabla: $\mathcal{L}^{-1}\left\{\frac{2b^3}{(s^2+b^2)^2}\right\} = \sin bt - bt\cos bt$

Con $b = 2$: $\frac{2 \cdot 8}{(s^2+4)^2} \to \sin 2t - 2t\cos 2t$

$Y = \frac{2}{(s^2+4)^2} = \frac{1}{8} \cdot \frac{16}{(s^2+4)^2}$

$$y(t) = \frac{1}{8}(\sin 2t - 2t\cos 2t)$$

---

## Problema 13b
$y'' - 3y' + 2y = e^t$, $y(0) = 0$, $y'(0) = 0$

$s^2Y - 3sY + 2Y = \frac{1}{s-1}$

$Y(s^2-3s+2) = \frac{1}{s-1}$

$Y = \frac{1}{(s-1)(s-1)(s-2)} = \frac{1}{(s-1)^2(s-2)}$

[Fracciones parciales](../../../glossary.md#fracciones-parciales):
$\frac{A}{s-1} + \frac{B}{(s-1)^2} + \frac{C}{s-2}$

$A = 1$, $B = -1$, $C = -1$

$$y(t) = e^t - te^t - e^{2t}$$

---

## Problema 16b
$\mathcal{L}\{(t-1)u(t-1)\}$

Por segunda traslación con $f(t) = t$:

$$\mathcal{L}\{(t-1)u(t-1)\} = e^{-s}\mathcal{L}\{t\} = \frac{e^{-s}}{s^2}$$

---

## Problema 18a
$y' + y = \delta(t-1)$, $y(0) = 0$

$sY + Y = e^{-s}$

$Y = \frac{e^{-s}}{s+1}$

$$y(t) = u(t-1)e^{-(t-1)}$$

---

## Problema 21
**Circuito RC:** $100\frac{dq}{dt} + 100q = 10$

$\frac{dq}{dt} + q = 0.1$

$sQ + Q = \frac{0.1}{s}$

$Q = \frac{0.1}{s(s+1)} = 0.1\left(\frac{1}{s} - \frac{1}{s+1}\right)$

$$q(t) = 0.1(1 - e^{-t}) \text{ C}$$

---

## Problema 23
$\ddot{x} + 4x = 3\delta(t-2)$, $x(0) = 0$, $\dot{x}(0) = 0$

$s^2X + 4X = 3e^{-2s}$

$X = \frac{3e^{-2s}}{s^2+4}$

$\mathcal{L}^{-1}\left\{\frac{3}{s^2+4}\right\} = \frac{3}{2}\sin 2t$

Por segunda traslación:

$$x(t) = \frac{3}{2}u(t-2)\sin 2(t-2)$$

El sistema permanece en reposo hasta $t = 2$, luego oscila.
