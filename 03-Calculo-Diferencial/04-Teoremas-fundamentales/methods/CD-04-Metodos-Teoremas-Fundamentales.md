<!--
HUMANO:
Métodos para teoremas fundamentales.

IA:
Cada método tiene: cuándo usar, pasos, ejemplo.

---
content_type: methods
expected_output:
  default: markdown
audience: self-study
---
-->

# Métodos de Teoremas Fundamentales

---

## Método 1: Aplicar Teorema de Rolle

### Cuándo Usar
- Demostrar que una ecuación tiene raíz donde la derivada es cero
- Garantizar existencia de punto crítico

### Pasos
1. Verificar que $f$ es continua en $[a, b]$
2. Verificar que $f$ es diferenciable en $(a, b)$
3. Verificar que $f(a) = f(b)$
4. Concluir: existe $c \in (a, b)$ con $f'(c) = 0$

### Ejemplo
Demostrar que $f(x) = x^3 - x$ tiene un punto crítico en $(-1, 1)$.

$f(-1) = -1 + 1 = 0$, $f(1) = 1 - 1 = 0$
$f$ es polinomio (continua y diferenciable)
Por Rolle, existe $c \in (-1, 1)$ con $f'(c) = 0$.

---

## Método 2: Aplicar Teorema del Valor Medio

### Cuándo Usar
- Relacionar valor de función con su derivada
- Demostrar desigualdades
- Problemas de velocidad media vs. instantánea

### Pasos
1. Verificar continuidad en $[a, b]$ y diferenciabilidad en $(a, b)$
2. Aplicar: existe $c$ tal que $f'(c) = \frac{f(b) - f(a)}{b - a}$
3. Usar para obtener la conclusión deseada

### Ejemplo
Demostrar que $\lvert \sin a - \sin b \rvert \leq \lvert a - b \rvert$.

Por TVM: $\frac{\sin a - \sin b}{a - b} = \cos c$ para algún $c$.
Como $\lvert \cos c \rvert \leq 1$:
$\lvert \sin a - \sin b \rvert \leq \lvert a - b \rvert$

---

## Método 3: L'Hôpital para $\frac{0}{0}$

### Cuándo Usar
- Límite que da $\frac{0}{0}$ por sustitución directa

### Pasos
1. Verificar que $\lim f(x) = 0$ y $\lim g(x) = 0$
2. Calcular $\lim \frac{f'(x)}{g'(x)}$
3. Si este límite existe, es igual al original

### Ejemplo
$$\lim_{x \to 0} \frac{\sin x - x}{x^3}$$

$\frac{0}{0}$ → $\lim_{x \to 0} \frac{\cos x - 1}{3x^2}$ = $\frac{0}{0}$
→ $\lim_{x \to 0} \frac{-\sin x}{6x}$ = $\frac{0}{0}$
→ $\lim_{x \to 0} \frac{-\cos x}{6} = -\frac{1}{6}$

---

## Método 4: L'Hôpital para $\frac{\infty}{\infty}$

### Cuándo Usar
- Límite que da $\frac{\infty}{\infty}$

### Pasos
1. Verificar forma $\frac{\pm\infty}{\pm\infty}$
2. Aplicar L'Hôpital
3. Repetir si es necesario

### Ejemplo
$$\lim_{x \to \infty} \frac{\ln x}{x}$$

$\frac{\infty}{\infty}$ → $\lim_{x \to \infty} \frac{1/x}{1} = 0$

---

## Método 5: Forma $0 \cdot \infty$

### Cuándo Usar
- Límite de producto donde uno tiende a 0 y otro a infinito

### Pasos
1. Reescribir como $\frac{f}{1/g}$ o $\frac{g}{1/f}$
2. Aplicar L'Hôpital

### Ejemplo
$$\lim_{x \to 0^+} x \ln x$$

$= \lim_{x \to 0^+} \frac{\ln x}{1/x}$ = $\frac{-\infty}{\infty}$
$= \lim_{x \to 0^+} \frac{1/x}{-1/x^2} = \lim_{x \to 0^+} (-x) = 0$

---

## Método 6: Forma $\infty - \infty$

### Cuándo Usar
- Diferencia de dos expresiones que tienden a infinito

### Pasos
1. Combinar en una fracción común, o
2. Racionalizar, o
3. Factorizar término dominante

### Ejemplo
$$\lim_{x \to \infty} (x - \sqrt{x^2 + 1})$$

$= \lim_{x \to \infty} \frac{x^2 - (x^2+1)}{x + \sqrt{x^2+1}} = \lim_{x \to \infty} \frac{-1}{x + \sqrt{x^2+1}} = 0$

---

## Método 7: Formas $0^0$, $1^\infty$, $\infty^0$

### Cuándo Usar
- Límites de la forma $f(x)^{g(x)}$

### Pasos
1. Sea $y = f(x)^{g(x)}$
2. Calcular $\ln y = g(x) \ln f(x)$
3. Evaluar $\lim \ln y$ (usar L'Hôpital si necesario)
4. Si $\lim \ln y = L$, entonces $\lim y = e^L$

### Ejemplo ($1^\infty$)
$$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x$$

$\ln y = x \ln\left(1 + \frac{1}{x}\right) = \frac{\ln(1 + 1/x)}{1/x}$

Por L'Hôpital: $\lim = \frac{-\frac{1}{x^2} \cdot \frac{1}{1+1/x}}{-1/x^2} = \frac{1}{1+1/x} \to 1$

Por tanto, $y \to e^1 = e$

---

## Método 8: Polinomio de Taylor

### Cuándo Usar
- Aproximar funciones cerca de un punto
- Evaluar límites difíciles

### Pasos
1. Calcular $f(a)$, $f'(a)$, $f''(a)$, ...
2. Construir $P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k$

### Ejemplo
Taylor de $e^x$ alrededor de $a = 0$ hasta grado 3:

$f(x) = e^x$: $f(0) = 1$, $f'(0) = 1$, $f''(0) = 1$, $f'''(0) = 1$

$P_3(x) = 1 + x + \frac{x^2}{2} + \frac{x^3}{6}$

---

## Método 9: Estimación del Error de Taylor

### Cuándo Usar
- Saber qué tan buena es una aproximación

### Fórmula
$$\lvert R_n(x) \rvert \leq \frac{M}{(n+1)!}\lvert x - a \rvert^{n+1}$$

donde $M = \max \lvert f^{(n+1)}(t) \rvert$ para $t$ entre $a$ y $x$.

### Ejemplo
Error al aproximar $e^{0.1}$ con $P_2(x)$:

$\lvert R_2(0.1) \rvert \leq \frac{e^{0.1}}{3!}(0.1)^3 < \frac{1.2}{6}(0.001) = 0.0002$

---

## Método 10: Series de Maclaurin Conocidas

### Cuándo Usar
- Evaluar límites usando expansiones
- Aproximaciones rápidas

### Expansiones Útiles
- $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$
- $\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$
- $\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$
- $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$

### Ejemplo
$$\lim_{x \to 0} \frac{e^x - 1 - x}{x^2}$$

$e^x = 1 + x + \frac{x^2}{2} + O(x^3)$

$\frac{e^x - 1 - x}{x^2} = \frac{\frac{x^2}{2} + O(x^3)}{x^2} = \frac{1}{2} + O(x) \to \frac{1}{2}$
