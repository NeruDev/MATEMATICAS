<!--
---
content_type: problem_set
topic_id: mn-01-raices-ecuaciones
file_id: MN-01-Problemas
title: Problemas - [Raíces de Ecuaciones](../../../glossary.md#raices-de-ecuaciones)
description: Colección de problemas sobre [métodos numéricos](../../../glossary.md#metodos-numericos) para encontrar raíces
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Problemas: Raíces de Ecuaciones

---

## Sección 1: Método de Bisección

### [Prob-01] Bisección para polinomio cúbico ⭐
Usar el [método de bisección](../../../glossary.md#metodo-de-biseccion) para encontrar la raíz de $f(x) = x^3 - x - 1$ en $[1, 2]$ con tolerancia $\varepsilon = 0.01$.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-01)

---

### [Prob-02] Número de iteraciones en bisección ⭐
¿Cuántas iteraciones de bisección se necesitan para encontrar una raíz en $[0, 4]$ con precisión de $10^{-6}$?

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-02)

---

### [Prob-03] Ecuación trascendente con bisección ⭐
Aplicar bisección para resolver $\cos(x) = x$ en $[0, 1]$. Realizar 5 iteraciones.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-03)

---

### [Prob-04] Raíz de función exponencial ⭐
Encontrar la raíz positiva de $x - e^{-x} = 0$ usando bisección en $[0, 1]$.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-04)

---

## Sección 2: Método de Newton-Raphson

### [Prob-05] Cálculo de raíz cuadrada ⭐
Usar Newton-Raphson para encontrar $\sqrt{5}$ (resolver $x^2 - 5 = 0$) partiendo de $x_0 = 2$. Realizar 4 iteraciones.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-05)

---

### [Prob-06] Newton-Raphson con criterio de paro ⭐⭐
Aplicar Newton-Raphson a $f(x) = x^3 - 2x - 5$ con $x_0 = 2$. Calcular hasta que $|x_{n+1} - x_n| < 0.001$.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-06)

---

### [Prob-07] Raíz de logaritmo natural ⭐
Encontrar la raíz de $\ln(x) - 1 = 0$ usando Newton-Raphson con $x_0 = 3$.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-07)

---

### [Prob-08] Análisis de fallo en Newton-Raphson ⭐⭐
¿Por qué Newton-Raphson falla si se aplica a $f(x) = x^{1/3}$ con $x_0 = 0.1$? Analizar gráficamente.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-08)

---

### [Prob-09] Raíces múltiples y Newton modificado ⭐⭐⭐
Para $f(x) = x^2 - 2x + 1 = (x-1)^2$, la raíz $x = 1$ es doble. Aplicar Newton estándar y Newton modificado con $m = 2$. Comparar [convergencia](../../../glossary.md#convergencia).

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-09)

---

## Sección 3: Método de la Secante

### [Prob-10] Secante para polinomio cúbico ⭐⭐
Usar el método de la secante para resolver $x^3 + x - 1 = 0$ con $x_0 = 0$, $x_1 = 1$. Realizar 5 iteraciones.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-10)

---

### [Prob-11] Comparación Newton vs Secante ⭐⭐
Comparar la [convergencia](../../../glossary.md#convergencia) de Newton-Raphson y Secante para $f(x) = x - e^{-x}$ con valores iniciales apropiados.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-11)

---

### [Prob-12] Secante para función tangente ⭐⭐
Aplicar secante a $\tan(x) - x = 0$ cerca de $x = 4.5$ usando $x_0 = 4$, $x_1 = 5$.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-12)

---

## Sección 4: Método de Punto Fijo

### [Prob-13] Diseño de funciones de iteración ⭐⭐
Para $f(x) = x^3 - x - 1 = 0$, proponer tres funciones $g(x)$ diferentes. Analizar cuál converge.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-13)

---

### [Prob-14] Punto fijo con función seno ⭐
Resolver $x = 2\sin(x)$ usando punto fijo con $x_0 = 2$.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-14)

---

### [Prob-15] Demostración de convergencia de punto fijo ⭐⭐
Demostrar que $g(x) = e^{-x}$ converge para resolver $e^{-x} - x = 0$ en $[0, 1]$.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-15)

---

### [Prob-16] Análisis comparativo de funciones de iteración ⭐⭐⭐
La ecuación $x^3 = 2$ se puede resolver como:
- $g_1(x) = \sqrt[3]{2}$ ([trivial](../../../glossary.md#trivial))
- $g_2(x) = 2/x^2$
- $g_3(x) = \frac{2x + 2/x^2}{3}$ (Newton para $x^3 - 2$)

Analizar convergencia de $g_2$ y $g_3$.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-16)

---

## Sección 5: Análisis de Convergencia

### [Prob-17] Derivación de fórmula para raíz cuadrada ⭐⭐
Para $f(x) = x^2 - a$, demostrar que Newton-Raphson da:
$$x_{n+1} = \frac{1}{2}\left(x_n + \frac{a}{x_n}\right)$$

y verificar que la convergencia es cuadrática.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-17)

---

### [Prob-18] Orden de convergencia experimental ⭐⭐
Calcular el [orden de convergencia](../../../glossary.md#orden-de-convergencia) experimental para bisección aplicada a $x^3 - 2 = 0$ en $[1, 2]$.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-18)

---

### [Prob-19] Índice de eficiencia de métodos ⭐⭐⭐
¿Cuál es el índice de eficiencia de Newton-Raphson vs Secante? Interpretar.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-19)

---

## Sección 6: Problemas Aplicados

### [Prob-20] Deflexión de viga (Ingeniería Civil) ⭐⭐
La deflexión de una viga está dada por:
$$f(x) = x^4 - 20x^3 + 100x^2 - 150$$
Encontrar el punto donde la deflexión es cero en $[0, 10]$.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-20)

---

### [Prob-21] Tasa Interna de Retorno (Economía) ⭐⭐⭐
Calcular la Tasa Interna de Retorno de un proyecto con:
- Inversión inicial: $1000
- Flujo año 1: $500
- Flujo año 2: $600
- Flujo año 3: $300

Resolver: $-1000 + \frac{500}{1+r} + \frac{600}{(1+r)^2} + \frac{300}{(1+r)^3} = 0$

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-21)

---

### [Prob-22] Movimiento de partícula (Física) ⭐⭐
La posición de una partícula es $x(t) = t^3 - 6t^2 + 9t - 4$. ¿En qué instantes $t > 0$ la partícula está en el origen?

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-22)

---

### [Prob-23] Equilibrio químico (Química) ⭐⭐⭐
En una reacción química, el equilibrio satisface:
$$\frac{x^2}{(1-x)(2-x)} = 4$$
Encontrar $x$ en $(0, 1)$.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-23)

---

### [Prob-24] Frecuencia de resonancia RLC (Ingeniería Eléctrica) ⭐⭐
En un circuito RLC, la frecuencia de [resonancia](../../../glossary.md#resonancia) satisface:
$$\omega^3 - 2\omega - 5 = 0$$
Encontrar $\omega > 0$.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-24)

---

## Sección 7: Problemas de Implementación

### [Prob-25] Implementación de bisección ⭐⭐
Implementar el [método de bisección](../../../glossary.md#metodo-de-biseccion) en Python/MATLAB y probar con $\sin(x) - x/2 = 0$ en $[\pi/2, \pi]$.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-25)

---

### [Prob-26] Newton-Raphson con detección de divergencia ⭐⭐
Implementar Newton-Raphson con un [límite](../../../glossary.md#limite) de iteraciones y detectar [divergencia](../../../glossary.md#divergencia).

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-26)

---

### [Prob-27] Selector automático de método ⭐⭐⭐
Crear una [función](../../../glossary.md#funcion) que elija automáticamente entre bisección y Newton según la disponibilidad de $f'$.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-27)

---

### [Prob-28] Método de Steffensen ⭐⭐⭐
Implementar el método de Steffensen (aceleración de Aitken para punto fijo):
$$x_{n+1} = x_n - \frac{[g(x_n) - x_n]^2}{g(g(x_n)) - 2g(x_n) + x_n}$$

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-28)

---

## Sección 8: Problemas Teóricos

### [Prob-29] Demostración de convergencia cuadrática de Newton ⭐⭐⭐
Demostrar que si $f''$ es continua y $f'(x^*) \neq 0$, entonces Newton-Raphson tiene convergencia cuadrática.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-29)

---

### [Prob-30] Orden de convergencia del método de la secante ⭐⭐⭐
Demostrar que el método de la secante tiene [orden](../../../glossary.md#orden) de convergencia $\phi = \frac{1+\sqrt{5}}{2}$.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-30)

---

### [Prob-31] Teorema de convergencia de punto fijo ⭐⭐⭐
Para punto fijo, demostrar que si $|g'(x)| \leq L < 1$ en $[a,b]$ y $g([a,b]) \subseteq [a,b]$, entonces el método converge.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-31)

---

### [Prob-32] Comportamiento cíclico de Newton-Raphson ⭐⭐⭐
Analizar qué sucede con Newton-Raphson aplicado a $f(x) = x^3 - 2x + 2$ partiendo de $x_0 = 0$.

> 📂 **Solución:** [📎 Ver Respuesta](../solutions/MN-01-Respuestas.md#prob-32)
