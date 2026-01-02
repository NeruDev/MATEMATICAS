<!--
::METADATA::
type: method
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Métodos de Aplicaciones de la Derivada

> Guía completa de aplicaciones prácticas de la [derivada](../../..](../../../glossary.md)#derivada) con algoritmos detallados, tablas de procedimientos y ejemplos paso a paso.

---

## Método 1: Recta Tangente y Recta Normal

**Cuándo Usar:** Para encontrar la ecuación de la recta [tangente](../../..](../../../glossary.md)#tangente) o normal a una curva en un punto dado.

### Fórmulas

| Tipo | Ecuación |
|------|----------|
| Recta [Tangente](../../../glossary.md#tangente) | $y - y_0 = f'(x_0)(x - x_0)$ |
| Recta Normal | $y - y_0 = -\frac{1}{f'(x_0)}(x - x_0)$ |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Calcular $y_0$ | $y_0 = f(x_0)$ |
| 2 | Calcular la [derivada](../../../glossary.md#derivada) | $f'(x)$ |
| 3 | Evaluar la pendiente | $m = f'(x_0)$ |
| 4 | Escribir la ecuación | Usar punto-pendiente |

### Ejemplo Detallado

**Problema:** Encontrar la recta tangente a $f(x) = x^3 - 2x + 1$ en $x = 2$

---

**Paso 1: Calcular el punto de tangencia**

$$y_0 = f(2) = (2)^3 - 2(2) + 1 = 8 - 4 + 1 = 5$$

Punto: $(2, 5)$

---

**Paso 2: Calcular la derivada**

$$f'(x) = 3x^2 - 2$$

---

**Paso 3: Evaluar la pendiente en $x = 2$**

$$m = f'(2) = 3(2)^2 - 2 = 12 - 2 = 10$$

---

**Paso 4: Ecuación de la recta tangente**

$$y - 5 = 10(x - 2)$$
$$y = 10x - 20 + 5$$
$$y = 10x - 15$$

$$\boxed{y = 10x - 15}$$

---

**Recta Normal (perpendicular):**

$$m_{normal} = -\frac{1}{10}$$
$$y - 5 = -\frac{1}{10}(x - 2)$$

$$\boxed{y = -\frac{1}{10}x + \frac{26}{5}}$$

---

## Método 2: Razones de Cambio Relacionadas

**Cuándo Usar:** Cuando dos o más cantidades cambian con el tiempo y están relacionadas por una ecuación.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar variables | Las cantidades que cambian |
| 2 | Escribir la ecuación | Que relaciona las variables |
| 3 | Derivar implícitamente | Respecto al tiempo $t$ |
| 4 | Sustituir valores conocidos | Incluyendo las razones de cambio |
| 5 | Despejar la incógnita | La razón buscada |

### Ejemplo Detallado

**Problema:** Una escalera de 10 m de largo está apoyada contra una pared. El pie de la escalera se desliza alejándose de la pared a razón de 2 m/s. ¿Qué tan rápido desciende el extremo superior cuando el pie está a 6 m de la pared?

---

**Paso 1: Definir variables**

- $x$ = distancia del pie a la pared
- $y$ = altura del extremo superior
- $\frac{dx}{dt} = 2$ m/s (dado)
- Buscar: $\frac{dy}{dt}$ cuando $x = 6$

---

**Paso 2: Escribir la ecuación (Pitágoras)**

$$x^2 + y^2 = 10^2 = 100$$

---

**Paso 3: Derivar respecto a $t$**

$$2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0$$

---

**Paso 4: Encontrar $y$ cuando $x = 6$**

$$36 + y^2 = 100 \Rightarrow y^2 = 64 \Rightarrow y = 8$$

---

**Paso 5: Sustituir y despejar**

$$2(6)(2) + 2(8)\frac{dy}{dt} = 0$$
$$24 + 16\frac{dy}{dt} = 0$$
$$\frac{dy}{dt} = -\frac{24}{16} = -\frac{3}{2}$$

$$\boxed{\frac{dy}{dt} = -1.5 \text{ m/s}}$$

El signo negativo indica que la altura está disminuyendo.

---

## Método 3: Valores Extremos Absolutos en Intervalo Cerrado

**Cuándo Usar:** Para encontrar los valores máximo y mínimo absolutos de $f(x)$ en $[a, b]$.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Calcular $f'(x)$ | La derivada |
| 2 | Encontrar puntos críticos | Resolver $f'(x) = 0$ y donde $f'$ no existe |
| 3 | Evaluar $f$ en críticos | Solo los que están en $[a, b]$ |
| 4 | Evaluar en extremos | $f(a)$ y $f(b)$ |
| 5 | Comparar valores | El mayor es máximo, el [menor](../../../glossary.md#menor) es mínimo |

### Ejemplo Detallado

**Problema:** Encontrar los extremos absolutos de $f(x) = x^3 - 3x^2 + 1$ en $[-1, 4]$

---

**Paso 1: Calcular la derivada**

$$f'(x) = 3x^2 - 6x = 3x(x - 2)$$

---

**Paso 2: Encontrar puntos críticos**

$$3x(x - 2) = 0$$
$$x = 0 \quad \text{o} \quad x = 2$$

Ambos están en $[-1, 4]$ ✓

---

**Paso 3: Evaluar en puntos críticos**

$$f(0) = 0 - 0 + 1 = 1$$
$$f(2) = 8 - 12 + 1 = -3$$

---

**Paso 4: Evaluar en extremos del intervalo**

$$f(-1) = -1 - 3 + 1 = -3$$
$$f(4) = 64 - 48 + 1 = 17$$

---

**Paso 5: Comparar**

| Punto | Valor de $f$ |
|-------|-------------|
| $x = -1$ | $-3$ |
| $x = 0$ | $1$ |
| $x = 2$ | $-3$ |
| $x = 4$ | $17$ |

$$\boxed{\text{Máximo absoluto: } 17 \text{ en } x = 4}$$
$$\boxed{\text{Mínimo absoluto: } -3 \text{ en } x = -1 \text{ y } x = 2}$$

---

## Método 4: Criterio de la Primera Derivada

**Cuándo Usar:** Para determinar si un [punto crítico](../../..](../../../glossary.md)#punto-critico) es máximo local, mínimo local, o ninguno.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Encontrar puntos críticos | Resolver $f'(x) = 0$ |
| 2 | Crear intervalos | Divididos por los puntos críticos |
| 3 | Evaluar signo de $f'$ | En cada intervalo |
| 4 | Determinar tipo | Según cambio de signo |

### Criterio de Clasificación

| Cambio de signo de $f'$ | Conclusión |
|------------------------|------------|
| $+ \to -$ | Máximo local |
| $- \to +$ | Mínimo local |
| $+ \to +$ o $- \to -$ | [Punto de inflexión](../../../glossary.md#punto-de-inflexion) (no extremo) |

### Ejemplo Detallado

**Problema:** Clasificar los puntos críticos de $f(x) = x^4 - 4x^3$

---

**Paso 1: Encontrar puntos críticos**

$$f'(x) = 4x^3 - 12x^2 = 4x^2(x - 3)$$
$$4x^2(x - 3) = 0 \Rightarrow x = 0, \quad x = 3$$

---

**Paso 2: Crear tabla de signos**

| Intervalo | $4x^2$ | $(x-3)$ | $f'(x)$ | Comportamiento |
|-----------|--------|---------|---------|----------------|
| $(-\infty, 0)$ | $+$ | $-$ | $-$ | Decreciente |
| $(0, 3)$ | $+$ | $-$ | $-$ | Decreciente |
| $(3, \infty)$ | $+$ | $+$ | $+$ | Creciente |

---

**Paso 3: Clasificar**

- En $x = 0$: No hay cambio de signo ($- \to -$)
  - **No es extremo** ([punto de inflexión](../../..](../../../glossary.md)#punto-de-inflexion) horizontal)
  
- En $x = 3$: Cambio $- \to +$
  - **Mínimo local** en $x = 3$

$$\boxed{x = 0: \text{ Punto de inflexión horizontal}}$$
$$\boxed{x = 3: \text{ Mínimo local}, \, f(3) = 81 - 108 = -27}$$

---

## Método 5: Criterio de la Segunda Derivada

**Cuándo Usar:** Alternativa más rápida para clasificar puntos críticos (cuando $f''$ es fácil de calcular).

### Criterio

| Condición | Conclusión |
|-----------|------------|
| $f'(c) = 0$ y $f''(c) > 0$ | Mínimo local en $c$ |
| $f'(c) = 0$ y $f''(c) < 0$ | Máximo local en $c$ |
| $f'(c) = 0$ y $f''(c) = 0$ | Prueba inconclusa (usar 1ª derivada) |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Calcular $f'(x)$ y $f''(x)$ | Las dos [derivadas](../../../glossary.md#derivadas) |
| 2 | Encontrar puntos críticos | Resolver $f'(x) = 0$ |
| 3 | Evaluar $f''$ en cada crítico | Determinar signo |
| 4 | Clasificar | Según el criterio |

### Ejemplo Detallado

**Problema:** Clasificar los puntos críticos de $f(x) = x^3 - 6x^2 + 9x + 2$

---

**Paso 1: Calcular [derivadas](../../..](../../../glossary.md)#derivadas)**

$$f'(x) = 3x^2 - 12x + 9 = 3(x^2 - 4x + 3) = 3(x-1)(x-3)$$
$$f''(x) = 6x - 12$$

---

**Paso 2: Puntos críticos**

$$f'(x) = 0 \Rightarrow x = 1, \quad x = 3$$

---

**Paso 3: Evaluar segunda derivada**

$$f''(1) = 6(1) - 12 = -6 < 0 \Rightarrow \text{Máximo local}$$
$$f''(3) = 6(3) - 12 = 6 > 0 \Rightarrow \text{Mínimo local}$$

---

**Paso 4: Calcular valores**

$$f(1) = 1 - 6 + 9 + 2 = 6$$
$$f(3) = 27 - 54 + 27 + 2 = 2$$

$$\boxed{\text{Máximo local: } (1, 6)}$$
$$\boxed{\text{Mínimo local: } (3, 2)}$$

---

## Método 6: Problemas de Optimización

**Cuándo Usar:** Para encontrar el valor máximo o mínimo de una cantidad sujeta a restricciones.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar objetivo | ¿Qué maximizar/minimizar? |
| 2 | Definir variables | Asignar símbolos |
| 3 | Escribir [función](../../../glossary.md#funcion) objetivo | En términos de las variables |
| 4 | Escribir restricciones | Ecuaciones que limitan las variables |
| 5 | Reducir a una variable | Usar restricciones para eliminar |
| 6 | Derivar y resolver | $f'(x) = 0$ |
| 7 | Verificar máximo/mínimo | Criterio de 2ª derivada o contexto |

### Ejemplo Detallado

**Problema:** Un granjero quiere cercar un área rectangular con 400 m de cerca, usando un río como uno de los lados. ¿Qué dimensiones maximizan el área?

---

**Paso 1-2: Definir variables**

- $x$ = lado perpendicular al río (dos lados)
- $y$ = lado paralelo al río (un lado)

---

**Paso 3: [Función](../../..](../../../glossary.md)#funcion) objetivo (área)**

$$A = xy$$

---

**Paso 4: Restricción (perímetro)**

$$2x + y = 400$$

---

**Paso 5: Reducir a una variable**

De la restricción: $y = 400 - 2x$

Sustituyendo:
$$A(x) = x(400 - 2x) = 400x - 2x^2$$

---

**Paso 6: Derivar y resolver**

$$A'(x) = 400 - 4x = 0$$
$$x = 100$$

---

**Paso 7: Verificar máximo**

$$A''(x) = -4 < 0 \Rightarrow \text{Máximo}$$

---

**Calcular dimensiones:**

$$y = 400 - 2(100) = 200$$

$$\boxed{x = 100 \text{ m}, \quad y = 200 \text{ m}}$$
$$\boxed{A_{max} = 100 \times 200 = 20,000 \text{ m}^2}$$

---

### Ejemplo de Optimización con Costo

**Problema:** Diseñar una caja abierta de volumen 4000 cm³ con [base](../../..](../../../glossary.md)#base) cuadrada que use la mínima cantidad de material.

---

**Variables:** [Base](../../..](../../../glossary.md)#base) $x \times x$, altura $h$

**Objetivo:** Minimizar superficie $S = x^2 + 4xh$

**Restricción:** Volumen $V = x^2h = 4000$

---

**Reducir a una variable:**

$$h = \frac{4000}{x^2}$$

$$S(x) = x^2 + 4x \cdot \frac{4000}{x^2} = x^2 + \frac{16000}{x}$$

---

**Derivar:**

$$S'(x) = 2x - \frac{16000}{x^2} = 0$$
$$2x^3 = 16000$$
$$x^3 = 8000 \Rightarrow x = 20$$

---

**Verificar:**

$$S''(x) = 2 + \frac{32000}{x^3}$$
$$S''(20) = 2 + \frac{32000}{8000} = 2 + 4 = 6 > 0 \Rightarrow \text{Mínimo}$$

---

**Dimensiones:**

$$h = \frac{4000}{400} = 10 \text{ cm}$$

$$\boxed{\text{Base: } 20 \times 20 \text{ cm}, \quad \text{Altura: } 10 \text{ cm}}$$

---

## Método 7: Aproximación Lineal (Linealización)

**Cuándo Usar:** Para aproximar valores de funciones cerca de un punto conocido.

### Fórmula

$$L(x) = f(a) + f'(a)(x - a)$$

### Aproximación

$$f(x) \approx f(a) + f'(a)(x - a) \quad \text{para } x \text{ cerca de } a$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Elegir punto base | $a$ donde $f(a)$ es fácil de calcular |
| 2 | Calcular $f(a)$ y $f'(a)$ | Los valores en el punto base |
| 3 | Escribir linealización | $L(x) = f(a) + f'(a)(x-a)$ |
| 4 | Evaluar | $L(x)$ en el punto deseado |

### Ejemplo Detallado

**Problema:** Aproximar $\sqrt{4.1}$ usando linealización.

---

**Paso 1: Elegir punto base**

$f(x) = \sqrt{x}$, elegimos $a = 4$ (cuadrado perfecto cercano)

---

**Paso 2: Calcular valores**

$$f(4) = \sqrt{4} = 2$$
$$f'(x) = \frac{1}{2\sqrt{x}}$$
$$f'(4) = \frac{1}{2\sqrt{4}} = \frac{1}{4}$$

---

**Paso 3: Linealización**

$$L(x) = 2 + \frac{1}{4}(x - 4)$$

---

**Paso 4: Evaluar en $x = 4.1$**

$$L(4.1) = 2 + \frac{1}{4}(4.1 - 4) = 2 + \frac{1}{4}(0.1) = 2 + 0.025 = 2.025$$

$$\boxed{\sqrt{4.1} \approx 2.025}$$

**Valor exacto:** $\sqrt{4.1} = 2.0248...$

**Error:** $|2.025 - 2.0248| \approx 0.0002$ (excelente aproximación)

---

## Método 8: Diferenciales

**Cuándo Usar:** Para estimar el cambio en $y$ dado un pequeño cambio en $x$.

### Fórmulas

$$dy = f'(x) \, dx$$
$$\Delta y \approx dy \quad \text{cuando } \Delta x \text{ es pequeño}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Calcular $f'(x)$ | La derivada |
| 2 | Identificar $dx$ | El cambio en $x$ |
| 3 | Calcular $dy$ | $dy = f'(x) \cdot dx$ |

### Ejemplo Detallado

**Problema:** El radio de una esfera se mide como 10 cm con error posible de 0.05 cm. Estimar el error máximo en el volumen calculado.

---

**Paso 1: Función volumen**

$$V = \frac{4}{3}\pi r^3$$
$$\frac{dV}{dr} = 4\pi r^2$$

---

**Paso 2: Identificar valores**

$$r = 10 \text{ cm}, \quad dr = 0.05 \text{ cm}$$

---

**Paso 3: Calcular diferencial**

$$dV = 4\pi r^2 \, dr = 4\pi(10)^2(0.05)$$
$$= 4\pi(100)(0.05) = 20\pi \approx 62.83 \text{ cm}^3$$

$$\boxed{\text{Error máximo en volumen} \approx 62.83 \text{ cm}^3}$$

---

**Error relativo:**

$$\frac{dV}{V} = \frac{4\pi r^2 \, dr}{\frac{4}{3}\pi r^3} = \frac{3 \, dr}{r} = \frac{3(0.05)}{10} = 0.015 = 1.5\%$$

$$\boxed{\text{Error relativo} \approx 1.5\%}$$

---

## Método 9: Análisis Completo de Gráfica

**Cuándo Usar:** Para bosquejar la gráfica de una función analizando sus características.

### Algoritmo de Resolución

| Paso | Analizar | Método |
|------|----------|--------|
| 1 | [Dominio](../../../glossary.md#dominio) | Restricciones en $x$ |
| 2 | Interceptos | $y$-intercept: $f(0)$; $x$-intercepts: $f(x)=0$ |
| 3 | Simetría | Par si $f(-x)=f(x)$; impar si $f(-x)=-f(x)$ |
| 4 | Asíntotas | Verticales, horizontales, oblicuas |
| 5 | Intervalos de crecimiento | Signo de $f'(x)$ |
| 6 | Extremos locales | $f'(x) = 0$ y clasificar |
| 7 | [Concavidad](../../../glossary.md#concavidad) | Signo de $f''(x)$ |
| 8 | Puntos de inflexión | Donde $f''(x)$ cambia de signo |

### Ejemplo Detallado

**Problema:** Analizar $f(x) = \frac{x^2}{x^2 - 1}$

---

**1. [Dominio](../../..](../../../glossary.md)#dominio):**
$$x^2 - 1 \neq 0 \Rightarrow x \neq \pm 1$$
$$D = (-\infty, -1) \cup (-1, 1) \cup (1, \infty)$$

---

**2. Interceptos:**
- $y$-intercept: $f(0) = 0$ → $(0, 0)$
- $x$-intercept: $x^2 = 0 \Rightarrow x = 0$ → $(0, 0)$

---

**3. Simetría:**
$$f(-x) = \frac{(-x)^2}{(-x)^2 - 1} = \frac{x^2}{x^2 - 1} = f(x)$$
**Función par** (simétrica respecto al eje $y$)

---

**4. Asíntotas:**
- Verticales: $x = 1$ y $x = -1$
- Horizontal: $\lim_{x \to \pm\infty} \frac{x^2}{x^2-1} = 1$ → $y = 1$

---

**5-6. Derivada y extremos:**
$$f'(x) = \frac{2x(x^2-1) - x^2(2x)}{(x^2-1)^2} = \frac{-2x}{(x^2-1)^2}$$

$f'(x) = 0 \Rightarrow x = 0$

| Intervalo | Signo $f'$ | Comportamiento |
|-----------|------------|----------------|
| $(-\infty, -1)$ | $+$ | Creciente |
| $(-1, 0)$ | $+$ | Creciente |
| $(0, 1)$ | $-$ | Decreciente |
| $(1, \infty)$ | $-$ | Decreciente |

**Máximo local en $x = 0$:** $f(0) = 0$

---

**7-8. Segunda derivada y [concavidad](../../..](../../../glossary.md)#concavidad):**
$$f''(x) = \frac{2(3x^2 + 1)}{(x^2-1)^3}$$

| Intervalo | Signo $f''$ | Concavidad |
|-----------|-------------|------------|
| $(-\infty, -1)$ | $-$ | Cóncava abajo |
| $(-1, 1)$ | $+$ | Cóncava arriba |
| $(1, \infty)$ | $-$ | Cóncava abajo |

No hay puntos de inflexión (discontinuidades en $x = \pm 1$).

$$\boxed{\text{Ver gráfica con AV: } x = \pm 1, \text{ AH: } y = 1, \text{ Máx: } (0,0)}$$

---

## Método 10: Método de Newton-Raphson

**Cuándo Usar:** Para encontrar [raíces de ecuaciones](../../..](../../../glossary.md)#raices-de-ecuaciones) (soluciones de $f(x) = 0$) numéricamente.

### Fórmula Iterativa

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Elegir $x_0$ | Estimación inicial cercana a la raíz |
| 2 | Calcular $f(x_n)$ y $f'(x_n)$ | En el punto actual |
| 3 | Aplicar fórmula | Obtener $x_{n+1}$ |
| 4 | Verificar [convergencia](../../../glossary.md#convergencia) | Si $\vert x_{n+1} - x_n\vert < \epsilon$ |
| 5 | Repetir | Hasta [convergencia](../../../glossary.md#convergencia) |

### Ejemplo Detallado

**Problema:** Encontrar $\sqrt{2}$ usando Newton-Raphson (resolver $x^2 - 2 = 0$)

---

**Configuración:**

$$f(x) = x^2 - 2, \quad f'(x) = 2x$$

$$x_{n+1} = x_n - \frac{x_n^2 - 2}{2x_n}$$

---

**Iteraciones con $x_0 = 1$:**

**Iteración 1:**
$$x_1 = 1 - \frac{1 - 2}{2(1)} = 1 - \frac{-1}{2} = 1.5$$

**Iteración 2:**
$$x_2 = 1.5 - \frac{(1.5)^2 - 2}{2(1.5)} = 1.5 - \frac{0.25}{3} = 1.4167$$

**Iteración 3:**
$$x_3 = 1.4167 - \frac{(1.4167)^2 - 2}{2(1.4167)} = 1.4142$$

**Iteración 4:**
$$x_4 = 1.41421356...$$

$$\boxed{\sqrt{2} \approx 1.41421356}$$

---

## Método 11: Análisis de Concavidad y Puntos de Inflexión

**Cuándo Usar:** Para determinar dónde la gráfica es cóncava hacia arriba o abajo, y encontrar puntos de inflexión.

### Criterios

| Condición | Significado |
|-----------|-------------|
| $f''(x) > 0$ | Cóncava hacia arriba (∪) |
| $f''(x) < 0$ | Cóncava hacia abajo (∩) |
| $f''(c) = 0$ y cambia signo | Punto de inflexión en $x = c$ |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Calcular $f''(x)$ | Segunda derivada |
| 2 | Resolver $f''(x) = 0$ | Candidatos a inflexión |
| 3 | Crear tabla de signos | De $f''$ en cada intervalo |
| 4 | Identificar cambios | Donde $f''$ cambia de signo |

### Ejemplo Detallado

**Problema:** Encontrar puntos de inflexión de $f(x) = x^4 - 6x^2 + 8x + 2$

---

**Paso 1: Calcular derivadas**

$$f'(x) = 4x^3 - 12x + 8$$
$$f''(x) = 12x^2 - 12 = 12(x^2 - 1) = 12(x-1)(x+1)$$

---

**Paso 2: Resolver $f''(x) = 0$**

$$12(x-1)(x+1) = 0 \Rightarrow x = -1, \quad x = 1$$

---

**Paso 3: Tabla de signos**

| Intervalo | $(x-1)$ | $(x+1)$ | $f''(x)$ | Concavidad |
|-----------|---------|---------|----------|------------|
| $(-\infty, -1)$ | $-$ | $-$ | $+$ | Arriba ∪ |
| $(-1, 1)$ | $-$ | $+$ | $-$ | Abajo ∩ |
| $(1, \infty)$ | $+$ | $+$ | $+$ | Arriba ∪ |

---

**Paso 4: Puntos de inflexión**

Hay cambio de signo en $x = -1$ y $x = 1$.

$$f(-1) = 1 - 6 - 8 + 2 = -11$$
$$f(1) = 1 - 6 + 8 + 2 = 5$$

$$\boxed{\text{Puntos de inflexión: } (-1, -11) \text{ y } (1, 5)}$$

---

## Resumen: Tabla de Aplicaciones

| Aplicación | Herramienta | Resultado |
|------------|-------------|-----------|
| Recta tangente | $f'(x_0)$ | Pendiente de tangente |
| Extremos | $f'(x) = 0$ | Máximos/mínimos |
| Concavidad | Signo de $f''$ | ∪ o ∩ |
| Inflexión | $f'' = 0$ + cambio signo | Punto de inflexión |
| Optimización | $f'(x) = 0$ + restricciones | Valor óptimo |
| Aproximación | $L(x) = f(a) + f'(a)(x-a)$ | Valor aproximado |
| Razones relacionadas | $\frac{d}{dt}[\text{ecuación}]$ | Razón de cambio |

---

## Errores Comunes

| Error | Corrección |
|-------|------------|
| No verificar dominio en optimización | Las respuestas deben estar en el dominio físico |
| Olvidar extremos del intervalo | Siempre evaluar en $a$ y $b$ para extremos absolutos |
| Confundir extremo local con absoluto | Local = vecindad; Absoluto = todo el dominio |
| No verificar si $f''(c) = 0$ es inflexión | Debe haber cambio de signo en $f''$ |
| Ignorar el signo en razones relacionadas | El signo indica dirección del cambio |
| Olvidar unidades en problemas aplicados | Siempre incluir unidades en la respuesta |
| No elegir buen punto base en linealización | Elegir $a$ donde $f(a)$ sea fácil de calcular |
