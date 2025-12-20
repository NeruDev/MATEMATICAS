<!--
content_type: problems
topic: Raíces de Ecuaciones
---
-->

# Problemas: Raíces de Ecuaciones

---

## Sección 1: Método de Bisección

**Problema 1.** Usar el método de bisección para encontrar la raíz de $f(x) = x^3 - x - 1$ en $[1, 2]$ con tolerancia $\varepsilon = 0.01$.

**Problema 2.** ¿Cuántas iteraciones de bisección se necesitan para encontrar una raíz en $[0, 4]$ con precisión de $10^{-6}$?

**Problema 3.** Aplicar bisección para resolver $\cos(x) = x$ en $[0, 1]$. Realizar 5 iteraciones.

**Problema 4.** Encontrar la raíz positiva de $x - e^{-x} = 0$ usando bisección en $[0, 1]$.

---

## Sección 2: Método de Newton-Raphson

**Problema 5.** Usar Newton-Raphson para encontrar $\sqrt{5}$ (resolver $x^2 - 5 = 0$) partiendo de $x_0 = 2$. Realizar 4 iteraciones.

**Problema 6.** Aplicar Newton-Raphson a $f(x) = x^3 - 2x - 5$ con $x_0 = 2$. Calcular hasta que $|x_{n+1} - x_n| < 0.001$.

**Problema 7.** Encontrar la raíz de $\ln(x) - 1 = 0$ usando Newton-Raphson con $x_0 = 3$.

**Problema 8.** ¿Por qué Newton-Raphson falla si se aplica a $f(x) = x^{1/3}$ con $x_0 = 0.1$? Analizar gráficamente.

**Problema 9.** Para $f(x) = x^2 - 2x + 1 = (x-1)^2$, la raíz $x = 1$ es doble. Aplicar Newton estándar y Newton modificado con $m = 2$. Comparar convergencia.

---

## Sección 3: Método de la Secante

**Problema 10.** Usar el método de la secante para resolver $x^3 + x - 1 = 0$ con $x_0 = 0$, $x_1 = 1$. Realizar 5 iteraciones.

**Problema 11.** Comparar la convergencia de Newton-Raphson y Secante para $f(x) = x - e^{-x}$ con valores iniciales apropiados.

**Problema 12.** Aplicar secante a $\tan(x) - x = 0$ cerca de $x = 4.5$ usando $x_0 = 4$, $x_1 = 5$.

---

## Sección 4: Método de Punto Fijo

**Problema 13.** Para $f(x) = x^3 - x - 1 = 0$, proponer tres funciones $g(x)$ diferentes. Analizar cuál converge.

**Problema 14.** Resolver $x = 2\sin(x)$ usando punto fijo con $x_0 = 2$.

**Problema 15.** Demostrar que $g(x) = e^{-x}$ converge para resolver $e^{-x} - x = 0$ en $[0, 1]$.

**Problema 16.** La ecuación $x^3 = 2$ se puede resolver como:
- $g_1(x) = \sqrt[3]{2}$ (trivial)
- $g_2(x) = 2/x^2$
- $g_3(x) = \frac{2x + 2/x^2}{3}$ (Newton para $x^3 - 2$)

Analizar convergencia de $g_2$ y $g_3$.

---

## Sección 5: Análisis de Convergencia

**Problema 17.** Para $f(x) = x^2 - a$, demostrar que Newton-Raphson da:
$$x_{n+1} = \frac{1}{2}\left(x_n + \frac{a}{x_n}\right)$$

y verificar que la convergencia es cuadrática.

**Problema 18.** Calcular el orden de convergencia experimental para bisección aplicada a $x^3 - 2 = 0$ en $[1, 2]$.

**Problema 19.** ¿Cuál es el índice de eficiencia de Newton-Raphson vs Secante? Interpretar.

---

## Sección 6: Problemas Aplicados

**Problema 20.** (Ingeniería civil) La deflexión de una viga está dada por:
$$f(x) = x^4 - 20x^3 + 100x^2 - 150$$
Encontrar el punto donde la deflexión es cero en $[0, 10]$.

**Problema 21.** (Economía - TIR) Calcular la Tasa Interna de Retorno de un proyecto con:
- Inversión inicial: $1000
- Flujo año 1: $500
- Flujo año 2: $600
- Flujo año 3: $300

Resolver: $-1000 + \frac{500}{1+r} + \frac{600}{(1+r)^2} + \frac{300}{(1+r)^3} = 0$

**Problema 22.** (Física) La posición de una partícula es $x(t) = t^3 - 6t^2 + 9t - 4$. ¿En qué instantes $t > 0$ la partícula está en el origen?

**Problema 23.** (Química) En una reacción química, el equilibrio satisface:
$$\frac{x^2}{(1-x)(2-x)} = 4$$
Encontrar $x$ en $(0, 1)$.

**Problema 24.** (Ingeniería eléctrica) En un circuito RLC, la frecuencia de resonancia satisface:
$$\omega^3 - 2\omega - 5 = 0$$
Encontrar $\omega > 0$.

---

## Sección 7: Problemas de Implementación

**Problema 25.** Implementar el método de bisección en Python/MATLAB y probar con $\sin(x) - x/2 = 0$ en $[\pi/2, \pi]$.

**Problema 26.** Implementar Newton-Raphson con un límite de iteraciones y detectar divergencia.

**Problema 27.** Crear una función que elija automáticamente entre bisección y Newton según la disponibilidad de $f'$.

**Problema 28.** Implementar el método de Steffensen (aceleración de Aitken para punto fijo):
$$x_{n+1} = x_n - \frac{[g(x_n) - x_n]^2}{g(g(x_n)) - 2g(x_n) + x_n}$$

---

## Sección 8: Problemas Teóricos

**Problema 29.** Demostrar que si $f''$ es continua y $f'(x^*) \neq 0$, entonces Newton-Raphson tiene convergencia cuadrática.

**Problema 30.** Demostrar que el método de la secante tiene orden de convergencia $\phi = \frac{1+\sqrt{5}}{2}$.

**Problema 31.** Para punto fijo, demostrar que si $|g'(x)| \leq L < 1$ en $[a,b]$ y $g([a,b]) \subseteq [a,b]$, entonces el método converge.

**Problema 32.** Analizar qué sucede con Newton-Raphson aplicado a $f(x) = x^3 - 2x + 2$ partiendo de $x_0 = 0$.
