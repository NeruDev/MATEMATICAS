<!--
HUMANO:
Problemas de límites organizados por subtema.

IA:
No incluyas soluciones aquí. Las soluciones están en solutions/soluciones.md.

---
content_type: problem_set
expected_output:
  default: markdown
audience: self-study
difficulty_levels: básico, intermedio, avanzado
---
-->

# Problemas de Límites

> **Instrucciones:** Evalúa cada límite. Indica si no existe y por qué.

---

## 1.1 Concepto de Límite

### Problema 1.1.1 ⭐
Usa la gráfica de $f(x)$ para estimar:
Si $f(x) = \begin{cases} x+1 & x < 2 \\ 5 & x = 2 \\ 4-x & x > 2 \end{cases}$, evalúa $\lim_{x \to 2} f(x)$.

### Problema 1.1.2 ⭐
Evalúa $\lim_{x \to 3} (2x + 5)$ usando la definición intuitiva.

### Problema 1.1.3 ⭐⭐
Usando la definición épsilon-delta, demuestra que $\lim_{x \to 4} (3x - 7) = 5$.

### Problema 1.1.4 ⭐⭐⭐
Demuestra que $\lim_{x \to 2} x^2 = 4$ usando la definición formal.

---

## 1.2 Límites Laterales

### Problema 1.2.1 ⭐
Evalúa los límites laterales: $\lim_{x \to 0^+} \frac{\lvert x \rvert}{x}$ y $\lim_{x \to 0^-} \frac{\lvert x \rvert}{x}$

### Problema 1.2.2 ⭐
Para $g(x) = \begin{cases} x^2 & x \leq 1 \\ 2x-1 & x > 1 \end{cases}$, evalúa $\lim_{x \to 1^-} g(x)$ y $\lim_{x \to 1^+} g(x)$.

### Problema 1.2.3 ⭐⭐
¿Existe $\lim_{x \to 3} f(x)$ si $f(x) = \begin{cases} x+2 & x < 3 \\ 8-x & x \geq 3 \end{cases}$?

### Problema 1.2.4 ⭐⭐
Evalúa $\lim_{x \to 2} \frac{x^2 - 4}{\lvert x - 2 \rvert}$

### Problema 1.2.5 ⭐⭐⭐
Para $f(x) = \lfloor x \rfloor$ (función piso), evalúa $\lim_{x \to 3^-} f(x)$ y $\lim_{x \to 3^+} f(x)$.

---

## 1.3 Propiedades de los Límites

### Problema 1.3.1 ⭐
Si $\lim_{x \to 4} f(x) = 3$ y $\lim_{x \to 4} g(x) = -2$, calcula $\lim_{x \to 4} [5f(x) - 2g(x)]$.

### Problema 1.3.2 ⭐
Evalúa $\lim_{x \to 2} \sqrt{x^2 + 5}$

### Problema 1.3.3 ⭐⭐
Si $\lim_{x \to a} f(x) = 4$ y $\lim_{x \to a} g(x) = 0$, ¿qué se puede concluir sobre $\lim_{x \to a} f(x) \cdot g(x)$?

### Problema 1.3.4 ⭐⭐⭐
Usa el teorema del emparedado para evaluar $\lim_{x \to 0} x^2 \cos\left(\frac{1}{x}\right)$.

---

## 1.4 Técnicas de Evaluación

### Problema 1.4.1 ⭐
$\lim_{x \to 5} \frac{x^2 - 25}{x - 5}$

### Problema 1.4.2 ⭐
$\lim_{x \to -2} \frac{x^2 + 5x + 6}{x + 2}$

### Problema 1.4.3 ⭐
$\lim_{x \to 3} \frac{x^2 - 9}{x^2 - 5x + 6}$

### Problema 1.4.4 ⭐⭐
$\lim_{x \to 1} \frac{x^3 - 1}{x - 1}$

### Problema 1.4.5 ⭐⭐
$\lim_{x \to 4} \frac{\sqrt{x} - 2}{x - 4}$

### Problema 1.4.6 ⭐⭐
$\lim_{x \to 0} \frac{\sqrt{1+x} - 1}{x}$

### Problema 1.4.7 ⭐⭐
$\lim_{x \to 9} \frac{3 - \sqrt{x}}{9 - x}$

### Problema 1.4.8 ⭐⭐⭐
$\lim_{x \to 0} \frac{\sqrt{1+x} - \sqrt{1-x}}{x}$

### Problema 1.4.9 ⭐⭐⭐
$\lim_{h \to 0} \frac{(2+h)^3 - 8}{h}$

### Problema 1.4.10 ⭐⭐⭐
$\lim_{x \to 1} \frac{x^{1/3} - 1}{x - 1}$

---

## 1.5 Límites Trigonométricos

### Problema 1.5.1 ⭐
$\lim_{x \to 0} \frac{\sin 5x}{x}$

### Problema 1.5.2 ⭐
$\lim_{x \to 0} \frac{\sin x}{3x}$

### Problema 1.5.3 ⭐⭐
$\lim_{x \to 0} \frac{\sin 3x}{\sin 5x}$

### Problema 1.5.4 ⭐⭐
$\lim_{x \to 0} \frac{\tan x}{x}$

### Problema 1.5.5 ⭐⭐
$\lim_{x \to 0} \frac{1 - \cos x}{x^2}$

### Problema 1.5.6 ⭐⭐
$\lim_{x \to 0} \frac{\sin^2 x}{x^2}$

### Problema 1.5.7 ⭐⭐⭐
$\lim_{x \to 0} \frac{x - \sin x}{x^3}$

### Problema 1.5.8 ⭐⭐⭐
$\lim_{x \to 0} \frac{\tan x - \sin x}{x^3}$

### Problema 1.5.9 ⭐⭐⭐
$\lim_{\theta \to 0} \frac{\sin 3\theta}{\theta \cos 2\theta}$

### Problema 1.5.10 ⭐⭐⭐⭐
$\lim_{x \to \pi/4} \frac{\sin x - \cos x}{1 - \tan x}$

---

## 1.6 Límites al Infinito

### Problema 1.6.1 ⭐
$\lim_{x \to \infty} \frac{3x + 2}{x - 1}$

### Problema 1.6.2 ⭐
$\lim_{x \to \infty} \frac{x^2 + 1}{2x^2 - 3}$

### Problema 1.6.3 ⭐
$\lim_{x \to \infty} \frac{5x}{x^2 + 4}$

### Problema 1.6.4 ⭐⭐
$\lim_{x \to \infty} \frac{x^3 - 2x}{3x^2 + x}$

### Problema 1.6.5 ⭐⭐
$\lim_{x \to -\infty} \frac{2x^2 - x}{x^2 + 1}$

### Problema 1.6.6 ⭐⭐
$\lim_{x \to \infty} \left(\sqrt{x^2 + x} - x\right)$

### Problema 1.6.7 ⭐⭐⭐
$\lim_{x \to \infty} \left(\sqrt{x^2 + 2x} - \sqrt{x^2 - 2x}\right)$

### Problema 1.6.8 ⭐⭐⭐
$\lim_{x \to \infty} x\left(\sqrt{x^2+1} - x\right)$

### Problema 1.6.9 ⭐⭐⭐
$\lim_{x \to \infty} \frac{\sin x}{x}$

### Problema 1.6.10 ⭐⭐⭐⭐
$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x$

---

## 1.7 Límites Infinitos

### Problema 1.7.1 ⭐
$\lim_{x \to 3^+} \frac{1}{x-3}$

### Problema 1.7.2 ⭐
$\lim_{x \to 2^-} \frac{1}{(x-2)^2}$

### Problema 1.7.3 ⭐⭐
$\lim_{x \to 0} \frac{1}{x^2}$

### Problema 1.7.4 ⭐⭐
$\lim_{x \to 1} \frac{x^2}{(x-1)^2}$

### Problema 1.7.5 ⭐⭐
Encuentra las asíntotas verticales de $f(x) = \frac{x}{x^2-4}$.

### Problema 1.7.6 ⭐⭐⭐
Encuentra todas las asíntotas de $f(x) = \frac{x^2 - 1}{x^2 - 4}$.

### Problema 1.7.7 ⭐⭐⭐
$\lim_{x \to 0^+} x \ln x$

---

## 1.8 Continuidad

### Problema 1.8.1 ⭐
¿Es $f(x) = \frac{x^2-1}{x-1}$ continua en $x = 1$? Si no, ¿qué tipo de discontinuidad tiene?

### Problema 1.8.2 ⭐
Encuentra el valor de $k$ para que $f(x) = \begin{cases} x^2 & x \leq 2 \\ kx & x > 2 \end{cases}$ sea continua.

### Problema 1.8.3 ⭐⭐
Determina los puntos de discontinuidad de $f(x) = \frac{1}{x^2 - 5x + 6}$.

### Problema 1.8.4 ⭐⭐
¿Es continua $f(x) = \begin{cases} \frac{\sin x}{x} & x \neq 0 \\ 1 & x = 0 \end{cases}$?

### Problema 1.8.5 ⭐⭐⭐
Encuentra $a$ y $b$ para que $f(x) = \begin{cases} ax+b & x < 1 \\ 3 & x = 1 \\ x^2 + 1 & x > 1 \end{cases}$ sea continua en todo $\mathbb{R}$.

### Problema 1.8.6 ⭐⭐⭐
Clasifica todas las discontinuidades de $f(x) = \frac{\lvert x-2 \rvert}{x-2}$.

---

## 1.9 Teorema del Valor Intermedio

### Problema 1.9.1 ⭐⭐
Demuestra que $x^3 - x - 1 = 0$ tiene al menos una solución en $(1, 2)$.

### Problema 1.9.2 ⭐⭐
Demuestra que la ecuación $\cos x = x$ tiene al menos una solución en $(0, 1)$.

### Problema 1.9.3 ⭐⭐⭐
Demuestra que $e^x = 3 - 2x$ tiene exactamente una solución.

### Problema 1.9.4 ⭐⭐⭐
Usa el TVI para demostrar que $\sqrt{2}$ existe (es decir, que $x^2 = 2$ tiene solución positiva).

### Problema 1.9.5 ⭐⭐⭐⭐
Si $f$ es continua en $[0,1]$ con $f(0) = f(1)$, demuestra que existe $c \in [0, 1/2]$ tal que $f(c) = f(c + 1/2)$.

---

## Problemas de Síntesis

### Problema 1.S.1 ⭐⭐⭐
Evalúa $\lim_{x \to 0} \frac{\sqrt{1+\tan x} - \sqrt{1+\sin x}}{x^3}$

### Problema 1.S.2 ⭐⭐⭐
Si $\lim_{x \to 0} \frac{f(x)}{x} = 1$ y $\lim_{x \to 0} \frac{g(x)}{x^2} = 1$, evalúa $\lim_{x \to 0} \frac{f(x) - g(x)}{x}$.

### Problema 1.S.3 ⭐⭐⭐⭐
Encuentra $\lim_{n \to \infty} \left(\frac{1}{n^2} + \frac{2}{n^2} + \cdots + \frac{n}{n^2}\right)$

### Problema 1.S.4 ⭐⭐⭐⭐
Sea $f(x) = \lim_{n \to \infty} \frac{x^{2n} - 1}{x^{2n} + 1}$. Encuentra el dominio y grafica $f$.

### Problema 1.S.5 ⭐⭐⭐⭐
Demuestra que $\lim_{x \to 0} \sin\frac{1}{x}$ no existe.
