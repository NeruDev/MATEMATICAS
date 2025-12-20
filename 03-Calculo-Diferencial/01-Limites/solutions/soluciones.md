<!--
HUMANO:
Soluciones con contexto teórico y desarrollo paso a paso.

IA:
Cada solución incluye: contexto → desarrollo → verificación.

---
content_type: solutions
expected_output:
  default: markdown
audience: self-study
---
-->

# Soluciones de Límites

> **Formato:** Contexto teórico → Desarrollo paso a paso → Verificación

---

## 1.2 Límites Laterales

### Solución 1.2.1
**Contexto:** El valor absoluto cambia de comportamiento en $x = 0$.

**Desarrollo:**
- $\lim_{x \to 0^+} \frac{\lvert x \rvert}{x} = \lim_{x \to 0^+} \frac{x}{x} = 1$ (para $x > 0$, $\lvert x \rvert = x$)
- $\lim_{x \to 0^-} \frac{\lvert x \rvert}{x} = \lim_{x \to 0^-} \frac{-x}{x} = -1$ (para $x < 0$, $\lvert x \rvert = -x$)

**Respuesta:** Por la derecha: $1$, por la izquierda: $-1$. El límite $\lim_{x \to 0}$ no existe.

### Solución 1.2.2
**Contexto:** Función definida por partes, evaluar en el punto de cambio.

**Desarrollo:**
- $\lim_{x \to 1^-} g(x) = \lim_{x \to 1^-} x^2 = 1^2 = 1$
- $\lim_{x \to 1^+} g(x) = \lim_{x \to 1^+} (2x-1) = 2(1)-1 = 1$

**Respuesta:** Ambos límites laterales son $1$, por lo que $\lim_{x \to 1} g(x) = 1$.

---

## 1.4 Técnicas de Evaluación

### Solución 1.4.1
**Contexto:** Forma $\frac{0}{0}$, usar factorización de diferencia de cuadrados.

**Desarrollo:**
$$\lim_{x \to 5} \frac{x^2 - 25}{x - 5} = \lim_{x \to 5} \frac{(x-5)(x+5)}{x-5} = \lim_{x \to 5} (x+5) = 10$$

### Solución 1.4.5
**Contexto:** Forma $\frac{0}{0}$ con radical, usar racionalización.

**Desarrollo:**
$$\lim_{x \to 4} \frac{\sqrt{x} - 2}{x - 4} = \lim_{x \to 4} \frac{(\sqrt{x}-2)(\sqrt{x}+2)}{(x-4)(\sqrt{x}+2)} = \lim_{x \to 4} \frac{x-4}{(x-4)(\sqrt{x}+2)}$$
$$= \lim_{x \to 4} \frac{1}{\sqrt{x}+2} = \frac{1}{2+2} = \frac{1}{4}$$

### Solución 1.4.9
**Contexto:** Esta es la definición de derivada de $f(x) = x^3$ en $x = 2$.

**Desarrollo:**
Expandir $(2+h)^3 = 8 + 12h + 6h^2 + h^3$
$$\lim_{h \to 0} \frac{8 + 12h + 6h^2 + h^3 - 8}{h} = \lim_{h \to 0} \frac{12h + 6h^2 + h^3}{h}$$
$$= \lim_{h \to 0} (12 + 6h + h^2) = 12$$

---

## 1.5 Límites Trigonométricos

### Solución 1.5.1
**Contexto:** Usar $\lim_{u \to 0} \frac{\sin u}{u} = 1$ con $u = 5x$.

**Desarrollo:**
$$\lim_{x \to 0} \frac{\sin 5x}{x} = \lim_{x \to 0} \frac{\sin 5x}{5x} \cdot 5 = 1 \cdot 5 = 5$$

### Solución 1.5.3
**Contexto:** Expresar ambos senos en términos de sus argumentos.

**Desarrollo:**
$$\lim_{x \to 0} \frac{\sin 3x}{\sin 5x} = \lim_{x \to 0} \frac{\sin 3x}{3x} \cdot \frac{5x}{\sin 5x} \cdot \frac{3x}{5x} = 1 \cdot 1 \cdot \frac{3}{5} = \frac{3}{5}$$

### Solución 1.5.5
**Contexto:** Usar la identidad $1 - \cos x = 2\sin^2(x/2)$ o el límite fundamental.

**Desarrollo:**
$$\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \lim_{x \to 0} \frac{2\sin^2(x/2)}{x^2} = \lim_{x \to 0} \frac{2\sin^2(x/2)}{4(x/2)^2} = \frac{2}{4} \cdot 1 = \frac{1}{2}$$

---

## 1.6 Límites al Infinito

### Solución 1.6.1
**Contexto:** Grados iguales en numerador y denominador, el límite es el cociente de coeficientes.

**Desarrollo:**
$$\lim_{x \to \infty} \frac{3x + 2}{x - 1} = \lim_{x \to \infty} \frac{3 + \frac{2}{x}}{1 - \frac{1}{x}} = \frac{3 + 0}{1 - 0} = 3$$

### Solución 1.6.6
**Contexto:** Forma $\infty - \infty$, usar racionalización.

**Desarrollo:**
$$\lim_{x \to \infty} (\sqrt{x^2 + x} - x) = \lim_{x \to \infty} \frac{(\sqrt{x^2+x}-x)(\sqrt{x^2+x}+x)}{\sqrt{x^2+x}+x}$$
$$= \lim_{x \to \infty} \frac{x^2+x-x^2}{\sqrt{x^2+x}+x} = \lim_{x \to \infty} \frac{x}{\sqrt{x^2+x}+x}$$

Dividiendo entre $x$ (con $x > 0$):
$$= \lim_{x \to \infty} \frac{1}{\sqrt{1+\frac{1}{x}}+1} = \frac{1}{1+1} = \frac{1}{2}$$

### Solución 1.6.10
**Contexto:** Este es el límite que define el número $e$.

**Desarrollo:**
$$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e \approx 2.71828...$$

Este límite fundamental define la constante de Euler $e$.

---

## 1.7 Límites Infinitos

### Solución 1.7.1
**Contexto:** Cuando $x \to 3^+$, el denominador es positivo pequeño.

**Desarrollo:**
Cuando $x > 3$ y $x \to 3$: $(x - 3) \to 0^+$

$$\lim_{x \to 3^+} \frac{1}{x-3} = \frac{1}{0^+} = +\infty$$

### Solución 1.7.6
**Contexto:** Análisis completo de asíntotas.

**Desarrollo:**
$f(x) = \frac{x^2-1}{x^2-4} = \frac{(x-1)(x+1)}{(x-2)(x+2)}$

**Asíntotas verticales:** $x = 2$ y $x = -2$ (donde el denominador es 0)

**Asíntota horizontal:** 
$$\lim_{x \to \pm\infty} \frac{x^2-1}{x^2-4} = \frac{1}{1} = 1$$

Por lo tanto, $y = 1$ es asíntota horizontal.

---

## 1.8 Continuidad

### Solución 1.8.1
**Contexto:** Verificar las tres condiciones de continuidad.

**Desarrollo:**
$f(x) = \frac{x^2-1}{x-1} = \frac{(x-1)(x+1)}{x-1} = x + 1$ para $x \neq 1$

1. ¿$f(1)$ está definida? No, hay división por cero
2. $\lim_{x \to 1} f(x) = \lim_{x \to 1} (x+1) = 2$

**Respuesta:** Discontinuidad **removible** en $x = 1$. Se puede definir $f(1) = 2$ para hacerla continua.

### Solución 1.8.2
**Contexto:** Para continuidad, los límites laterales deben ser iguales al valor de la función.

**Desarrollo:**
En $x = 2$:
- $\lim_{x \to 2^-} x^2 = 4$
- $\lim_{x \to 2^+} kx = 2k$
- $f(2) = 2^2 = 4$

Para continuidad: $4 = 2k$, entonces $k = 2$.

---

## 1.9 Teorema del Valor Intermedio

### Solución 1.9.1
**Contexto:** Usar TVI para demostrar existencia de raíz.

**Desarrollo:**
Sea $f(x) = x^3 - x - 1$

$f$ es continua en $[1, 2]$ (polinomio)

- $f(1) = 1 - 1 - 1 = -1 < 0$
- $f(2) = 8 - 2 - 1 = 5 > 0$

Como $f(1) < 0 < f(2)$ y $f$ es continua, por el TVI existe $c \in (1, 2)$ tal que $f(c) = 0$.

### Solución 1.9.2
**Contexto:** Reformular como búsqueda de raíz.

**Desarrollo:**
Sea $f(x) = \cos x - x$

$f$ es continua en $[0, 1]$

- $f(0) = \cos 0 - 0 = 1 > 0$
- $f(1) = \cos 1 - 1 \approx 0.54 - 1 = -0.46 < 0$

Por TVI, existe $c \in (0, 1)$ donde $\cos c = c$.

---

## Problemas de Síntesis

### Solución 1.S.3
**Contexto:** La suma es $\frac{1 + 2 + \cdots + n}{n^2} = \frac{n(n+1)/2}{n^2}$.

**Desarrollo:**
$$\lim_{n \to \infty} \frac{1 + 2 + \cdots + n}{n^2} = \lim_{n \to \infty} \frac{n(n+1)}{2n^2} = \lim_{n \to \infty} \frac{n+1}{2n} = \frac{1}{2}$$

### Solución 1.S.5
**Contexto:** Demostrar que los límites laterales no existen de forma tradicional.

**Desarrollo:**
Cuando $x \to 0$, $\frac{1}{x} \to \pm\infty$, y $\sin$ oscila entre $-1$ y $1$ infinitamente.

Tomemos dos sucesiones que tienden a 0:
- $x_n = \frac{1}{n\pi}$: $\sin(n\pi) = 0$ para todo $n$
- $y_n = \frac{1}{\frac{\pi}{2} + 2n\pi}$: $\sin(\frac{\pi}{2} + 2n\pi) = 1$ para todo $n$

Como las sucesiones convergen al mismo límite (0) pero $f(x_n) \to 0$ y $f(y_n) \to 1$, el límite no existe.
