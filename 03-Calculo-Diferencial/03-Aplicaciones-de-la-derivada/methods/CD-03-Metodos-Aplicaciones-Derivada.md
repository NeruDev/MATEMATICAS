<!--
HUMANO:
Métodos para aplicaciones de la derivada.

IA:
Cada método tiene: cuándo usar, pasos, ejemplo.

---
content_type: methods
expected_output:
  default: markdown
audience: self-study
---
-->

# Métodos de Aplicaciones de la Derivada

---

## Método 1: Ecuación de la Recta Tangente

### Cuándo Usar
- Encontrar la recta tangente a una curva en un punto

### Pasos
1. Calcular $f(a)$ (el punto de tangencia)
2. Calcular $f'(a)$ (la pendiente)
3. Usar forma punto-pendiente: $y - f(a) = f'(a)(x - a)$

### Ejemplo
Tangente a $y = x^2$ en $x = 2$:
- $f(2) = 4$
- $f'(x) = 2x$, $f'(2) = 4$
- Tangente: $y - 4 = 4(x - 2)$ → $y = 4x - 4$

---

## Método 2: Razones Relacionadas

### Cuándo Usar
- Problemas donde varias cantidades cambian con el tiempo

### Pasos
1. Identificar todas las variables y sus relaciones
2. Escribir la ecuación que las conecta
3. Derivar implícitamente respecto a $t$
4. Sustituir valores conocidos
5. Resolver para la tasa desconocida

### Ejemplo
Un globo esférico se infla a razón de 3 cm³/s. ¿Qué tan rápido crece el radio cuando $r = 5$ cm?

$V = \frac{4}{3}\pi r^3$, $\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt}$

$3 = 4\pi(25)\frac{dr}{dt}$ → $\frac{dr}{dt} = \frac{3}{100\pi}$ cm/s

---

## Método 3: Extremos Absolutos en Intervalo Cerrado

### Cuándo Usar
- Encontrar máximo/mínimo absoluto en $[a, b]$

### Pasos
1. Encontrar $f'(x)$ y resolver $f'(x) = 0$
2. Listar puntos críticos en $(a, b)$
3. Evaluar $f$ en críticos y en $a$, $b$
4. Comparar valores; el mayor es máximo, el menor es mínimo

### Ejemplo
$f(x) = x^3 - 3x$ en $[-2, 2]$

$f'(x) = 3x^2 - 3 = 0$ → $x = \pm 1$

$f(-2) = -2$, $f(-1) = 2$, $f(1) = -2$, $f(2) = 2$

Máximo: $2$ en $x = -1$ y $x = 2$. Mínimo: $-2$ en $x = -2$ y $x = 1$.

---

## Método 4: Criterio de Primera Derivada

### Cuándo Usar
- Clasificar puntos críticos como máximos, mínimos o ninguno

### Pasos
1. Encontrar puntos críticos
2. Hacer tabla de signos de $f'$ alrededor de cada crítico
3. Aplicar criterio:
   - $+$ a $-$ → máximo
   - $-$ a $+$ → mínimo

### Ejemplo
$f(x) = x^3 - 3x$, $f'(x) = 3(x-1)(x+1)$

| Intervalo | $(-\infty, -1)$ | $(-1, 1)$ | $(1, \infty)$ |
|-----------|-----------------|-----------|---------------|
| $f'(x)$ | $+$ | $-$ | $+$ |

$x = -1$: máximo relativo. $x = 1$: mínimo relativo.

---

## Método 5: Criterio de Segunda Derivada

### Cuándo Usar
- Clasificar puntos críticos cuando $f''$ es fácil de calcular

### Pasos
1. Encontrar $f'(x) = 0$ para puntos críticos
2. Calcular $f''(c)$ para cada crítico $c$
3. Si $f''(c) > 0$: mínimo. Si $f''(c) < 0$: máximo

### Ejemplo
$f(x) = x^4 - 4x^2$

$f'(x) = 4x^3 - 8x = 4x(x^2 - 2) = 0$ → $x = 0, \pm\sqrt{2}$

$f''(x) = 12x^2 - 8$

$f''(0) = -8 < 0$ → máximo
$f''(\pm\sqrt{2}) = 24 - 8 = 16 > 0$ → mínimos

---

## Método 6: Optimización

### Cuándo Usar
- Maximizar/minimizar una cantidad sujeta a restricciones

### Pasos
1. Variables: definir claramente
2. Objetivo: función a optimizar $f(x)$
3. Restricción: ecuación que relaciona variables
4. Eliminar: usar restricción para tener $f$ en una variable
5. Derivar: resolver $f'(x) = 0$
6. Verificar: que sea máximo o mínimo
7. Responder: en contexto del problema

### Ejemplo
Maximizar área de rectángulo con perímetro 20.

Variables: $x$ = base, $y$ = altura
Restricción: $2x + 2y = 20$ → $y = 10 - x$
Objetivo: $A = xy = x(10-x) = 10x - x^2$
$A' = 10 - 2x = 0$ → $x = 5$
$A'' = -2 < 0$ → máximo
Área máxima: $25$ (cuadrado $5 \times 5$)

---

## Método 7: Aproximación Lineal

### Cuándo Usar
- Estimar $f(x)$ cerca de un punto conocido

### Fórmula
$$f(x) \approx f(a) + f'(a)(x - a)$$

### Ejemplo
Estimar $\sqrt{4.1}$

$f(x) = \sqrt{x}$, $a = 4$, $f(4) = 2$, $f'(x) = \frac{1}{2\sqrt{x}}$, $f'(4) = \frac{1}{4}$

$\sqrt{4.1} \approx 2 + \frac{1}{4}(0.1) = 2.025$

(Valor real: $2.0248...$)

---

## Método 8: Análisis Completo de Gráfica

### Cuándo Usar
- Graficar una función con todos sus detalles

### Pasos
1. **Dominio:** ¿dónde está definida?
2. **Intersecciones:** $f(0)$ para eje $y$; resolver $f(x) = 0$ para eje $x$
3. **Simetría:** ¿es $f(-x) = f(x)$ (par) o $f(-x) = -f(x)$ (impar)?
4. **Asíntotas verticales:** donde el denominador es 0
5. **Asíntotas horizontales:** $\lim_{x \to \pm\infty} f(x)$
6. **$f'(x)$:** crecimiento/decrecimiento, extremos
7. **$f''(x)$:** concavidad, puntos de inflexión
8. **Graficar:** unir toda la información

---

## Método 9: Newton-Raphson

### Cuándo Usar
- Aproximar numéricamente raíces de ecuaciones

### Fórmula
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

### Pasos
1. Elegir $x_0$ cercano a la raíz
2. Calcular $x_1, x_2, \ldots$ usando la fórmula
3. Parar cuando $\lvert x_{n+1} - x_n \rvert < \varepsilon$

### Ejemplo
Resolver $x^3 - 2 = 0$ (encontrar $\sqrt[3]{2}$)

$f(x) = x^3 - 2$, $f'(x) = 3x^2$

$x_0 = 1.5$
$x_1 = 1.5 - \frac{1.375}{6.75} = 1.2963$
$x_2 = 1.2599$ (converge a $\sqrt[3]{2} \approx 1.2599$)

---

## Método 10: Determinar Concavidad

### Cuándo Usar
- Analizar la forma de la gráfica

### Pasos
1. Calcular $f''(x)$
2. Resolver $f''(x) = 0$ (candidatos a inflexión)
3. Tabla de signos de $f''$
4. $f'' > 0$: cóncava arriba (∪)
5. $f'' < 0$: cóncava abajo (∩)
6. Cambio de signo: punto de inflexión

---

## Método 11: Encontrar Asíntotas

### Verticales
Buscar donde $f(x) \to \pm\infty$
- Para $\frac{P(x)}{Q(x)}$: resolver $Q(x) = 0$

### Horizontales
$y = L$ donde $\lim_{x \to \pm\infty} f(x) = L$

### Oblicuas
Si grado(numerador) = grado(denominador) + 1:
Hacer división larga: $f(x) = mx + b + \frac{R(x)}{Q(x)}$
Asíntota: $y = mx + b$
