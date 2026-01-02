<!--
HUMANO:
Métodos para [integrales impropias](../../../glossary.md#integrales-impropias).

IA:
Procedimientos para evaluar y determinar [convergencia](../../../glossary.md#convergencia) con explicaciones detalladas.

---
content_type: methods
format: step_by_step
---
-->

# Métodos para Integrales Impropias

> **Objetivo:** Dominar la evaluación y análisis de convergencia de integrales impropias con explicaciones detalladas, cálculos intermedios y ejemplos clásicos paso a paso.

---

## Método 1: Evaluación Directa (Tipo I - Límite Infinito)

### Cuándo Usar
Integrales de la forma $\int_a^{\infty} f(x)\,dx$ o $\int_{-\infty}^{b} f(x)\,dx$ que se pueden evaluar explícitamente.

### Definición
$$\int_a^{\infty} f(x)\,dx = \lim_{t \to \infty} \int_a^t f(x)\,dx$$

### Algoritmo de Resolución

| Paso | Acción | Verificación |
|------|--------|--------------|
| 1 | Reemplazar $\infty$ por $t$ | Convertir en [integral definida](../../../glossary.md#integral-definida) |
| 2 | Calcular la integral en términos de $t$ | Aplicar técnicas usuales |
| 3 | Tomar el [límite](../../../glossary.md#límite) cuando $t \to \infty$ | Evaluar convergencia |
| 4 | Si el límite existe y es finito | La integral **converge** |
| 5 | Si el límite es $\pm\infty$ o no existe | La integral **diverge** |

### Ejemplo Detallado

**Problema:** Evaluar $\int_1^{\infty} e^{-x}\,dx$

**Paso 1:** Reemplazamos el límite infinito por $t$:
$$\int_1^{\infty} e^{-x}\,dx = \lim_{t \to \infty} \int_1^t e^{-x}\,dx$$

**Paso 2:** Calculamos la integral definida:
$$\int_1^t e^{-x}\,dx = \left[-e^{-x}\right]_1^t = -e^{-t} - (-e^{-1}) = -e^{-t} + e^{-1}$$

**Paso 3:** Tomamos el límite:
$$\lim_{t \to \infty} (-e^{-t} + e^{-1})$$

Sabemos que $e^{-t} \to 0$ cuando $t \to \infty$.

$$= 0 + e^{-1} = \frac{1}{e}$$

**Conclusión:** La integral **converge** y su valor es $\boxed{\frac{1}{e}}$.

---

## Método 2: Evaluación Directa (Tipo II - Discontinuidad)

### Cuándo Usar
Integrales donde el integrando tiene una discontinuidad ([asíntota](../../../glossary.md#asíntota) vertical) en uno de los [límites](../../../glossary.md#límites) o dentro del intervalo.

### Definición
Si $f$ tiene discontinuidad en $x = a$:
$$\int_a^b f(x)\,dx = \lim_{t \to a^+} \int_t^b f(x)\,dx$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar el punto de discontinuidad | Donde $f(x) \to \pm\infty$ |
| 2 | Reemplazar el punto problemático por $t$ | Con límite apropiado |
| 3 | Evaluar la integral definida | En términos de $t$ |
| 4 | Tomar el límite | $t \to$ punto de discontinuidad |

### Ejemplo Detallado

**Problema:** Evaluar $\int_0^4 \frac{1}{\sqrt{x}}\,dx$

**Paso 1:** Identificamos la discontinuidad:
$$f(x) = \frac{1}{\sqrt{x}} \to \infty \text{ cuando } x \to 0^+$$

**Paso 2:** Reemplazamos el límite problemático por $t$:
$$\int_0^4 \frac{1}{\sqrt{x}}\,dx = \lim_{t \to 0^+} \int_t^4 x^{-1/2}\,dx$$

**Paso 3:** Calculamos la integral:
$$\int_t^4 x^{-1/2}\,dx = \left[\frac{x^{1/2}}{1/2}\right]_t^4 = \left[2\sqrt{x}\right]_t^4 = 2\sqrt{4} - 2\sqrt{t} = 4 - 2\sqrt{t}$$

**Paso 4:** Tomamos el límite:
$$\lim_{t \to 0^+} (4 - 2\sqrt{t}) = 4 - 0 = 4$$

**Conclusión:** La integral **converge** y su valor es $\boxed{4}$.

---

## Método 3: Test de la Integral p (Límite Infinito)

### Cuándo Usar
Para determinar rápidamente si $\int_1^{\infty} \frac{1}{x^p}\,dx$ converge o diverge.

### Regla Fundamental

$$\int_1^{\infty} \frac{1}{x^p}\,dx \begin{cases} \text{Converge a } \frac{1}{p-1} & \text{si } p > 1 \\ \text{Diverge} & \text{si } p \leq 1 \end{cases}$$

### ¿Por qué funciona?

**Caso $p > 1$:**
$$\int_1^{\infty} x^{-p}\,dx = \lim_{t\to\infty}\left[\frac{x^{-p+1}}{-p+1}\right]_1^t = \lim_{t\to\infty}\frac{1}{1-p}\left(\frac{1}{t^{p-1}} - 1\right) = \frac{1}{p-1}$$

**Caso $p < 1$:**
El término $t^{1-p} \to \infty$ cuando $t \to \infty$.

**Caso $p = 1$:**
$$\int_1^{\infty} \frac{1}{x}\,dx = \lim_{t\to\infty}[\ln x]_1^t = \infty$$

### Ejemplo Detallado

**Problema:** Determinar si $\int_1^{\infty} \frac{1}{x^{3/2}}\,dx$ converge.

**Paso 1:** Identificamos $p = \frac{3}{2} = 1.5$

**Paso 2:** Como $p = 1.5 > 1$, la integral **converge**.

**Paso 3:** Calculamos el valor:
$$\int_1^{\infty} \frac{1}{x^{3/2}}\,dx = \frac{1}{p-1} = \frac{1}{3/2 - 1} = \frac{1}{1/2} = 2$$

**Resultado:** La integral converge y su valor es $\boxed{2}$.

---

## Método 4: Test de la Integral p (Discontinuidad en 0)

### Cuándo Usar
Para determinar si $\int_0^{1} \frac{1}{x^p}\,dx$ converge o diverge.

### Regla Fundamental

$$\int_0^{1} \frac{1}{x^p}\,dx \begin{cases} \text{Converge a } \frac{1}{1-p} & \text{si } p < 1 \\ \text{Diverge} & \text{si } p \geq 1 \end{cases}$$

> **¡Atención!** La condición es **opuesta** al caso del infinito.

### Ejemplo Detallado

**Problema:** Determinar si $\int_0^1 \frac{1}{x^{2/3}}\,dx$ converge.

**Paso 1:** Identificamos $p = \frac{2}{3}$

**Paso 2:** Como $p = \frac{2}{3} < 1$, la integral **converge**.

**Paso 3:** Calculamos el valor:
$$\int_0^1 \frac{1}{x^{2/3}}\,dx = \frac{1}{1-p} = \frac{1}{1 - 2/3} = \frac{1}{1/3} = 3$$

**Resultado:** La integral converge y su valor es $\boxed{3}$.

---

## Método 5: Comparación Directa

### Cuándo Usar
Cuando no se puede calcular la integral explícitamente pero se puede comparar con otra conocida.

### Teoremas de Comparación

**Para convergencia:** Si $0 \leq f(x) \leq g(x)$ y $\int g(x)\,dx$ converge, entonces $\int f(x)\,dx$ converge.

**Para [divergencia](../../../glossary.md#divergencia):** Si $f(x) \geq g(x) \geq 0$ y $\int g(x)\,dx$ diverge, entonces $\int f(x)\,dx$ diverge.

### Algoritmo de Resolución

| Paso | Acción | Propósito |
|------|--------|-----------|
| 1 | Identificar el comportamiento dominante | Para $x$ grande o cerca de discontinuidad |
| 2 | Encontrar [función](../../../glossary.md#función) de comparación $g(x)$ | Más simple, convergencia conocida |
| 3 | Verificar la desigualdad | $f \leq g$ o $f \geq g$ |
| 4 | Aplicar el teorema apropiado | Concluir convergencia/divergencia |

### Ejemplo Detallado

**Problema:** Determinar si $\int_1^{\infty} \frac{1}{x^2 + 1}\,dx$ converge.

**Paso 1:** Para $x \geq 1$, comparamos:
$$x^2 + 1 > x^2$$

**Paso 2:** Por lo tanto:
$$\frac{1}{x^2 + 1} < \frac{1}{x^2}$$

**Paso 3:** Sabemos que $\int_1^{\infty} \frac{1}{x^2}\,dx$ converge (test p con $p = 2 > 1$).

**Paso 4:** Por el teorema de comparación:
$$0 < \frac{1}{x^2+1} < \frac{1}{x^2}$$

Como la función mayor converge, la integral $\int_1^{\infty} \frac{1}{x^2 + 1}\,dx$ **converge**.

---

## Método 6: Comparación por Límite

### Cuándo Usar
Cuando la comparación directa es difícil de establecer.

### Teorema
Si $f(x) > 0$, $g(x) > 0$, y
$$L = \lim_{x \to \infty} \frac{f(x)}{g(x)}$$

- Si $0 < L < \infty$: ambas integrales tienen el **mismo comportamiento**.
- Si $L = 0$ y $\int g$ converge: $\int f$ converge.
- Si $L = \infty$ y $\int g$ diverge: $\int f$ diverge.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar término dominante de $f(x)$ | Para $x \to \infty$ |
| 2 | Elegir $g(x)$ con ese comportamiento | Función simple |
| 3 | Calcular $L = \lim \frac{f}{g}$ | Regla de L'Hôpital si es [necesario](../../../glossary.md#necesario) |
| 4 | Determinar convergencia de $\int g$ | Test p u otro método |
| 5 | Concluir sobre $\int f$ | Mismo comportamiento |

### Ejemplo Detallado

**Problema:** Determinar si $\int_1^{\infty} \frac{x^2 + 3}{x^4 - x + 2}\,dx$ converge.

**Paso 1:** Identificamos el comportamiento dominante:
- Numerador: $x^2 + 3 \approx x^2$ para $x$ grande
- Denominador: $x^4 - x + 2 \approx x^4$ para $x$ grande

**Paso 2:** Elegimos $g(x) = \frac{x^2}{x^4} = \frac{1}{x^2}$

**Paso 3:** Calculamos el límite:
$$L = \lim_{x \to \infty} \frac{(x^2+3)/(x^4-x+2)}{1/x^2}$$

$$= \lim_{x \to \infty} \frac{(x^2+3) \cdot x^2}{x^4 - x + 2}$$

$$= \lim_{x \to \infty} \frac{x^4 + 3x^2}{x^4 - x + 2}$$

Dividimos todo por $x^4$:
$$= \lim_{x \to \infty} \frac{1 + 3/x^2}{1 - 1/x^3 + 2/x^4} = \frac{1 + 0}{1 - 0 + 0} = 1$$

**Paso 4:** Como $L = 1$ (finito y positivo) y $\int_1^{\infty} \frac{1}{x^2}\,dx$ converge (test p, $p = 2 > 1$), entonces la integral original **converge**.

---

## Método 7: División en Subintervalos

### Cuándo Usar
- Discontinuidad en el **interior** del intervalo
- **Ambos** límites son infinitos

### Principio
La integral total converge si y solo si **todas** las partes convergen.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar puntos problemáticos | Discontinuidades o infinitos |
| 2 | Dividir en el punto problemático | Usar cualquier punto finito para $\pm\infty$ |
| 3 | Evaluar cada parte por separado | Como integrales impropias |
| 4 | Verificar que **todas** convergen | Si una diverge, todo diverge |
| 5 | Sumar si ambas convergen | Resultado final |

### Ejemplo Detallado

**Problema:** Evaluar $\int_{-\infty}^{\infty} \frac{1}{1+x^2}\,dx$

**Paso 1:** Ambos límites son infinitos. Dividimos en $x = 0$.

**Paso 2:** 
$$\int_{-\infty}^{\infty} \frac{1}{1+x^2}\,dx = \int_{-\infty}^{0} \frac{1}{1+x^2}\,dx + \int_0^{\infty} \frac{1}{1+x^2}\,dx$$

**Paso 3:** Evaluamos la primera parte:
$$\int_{-\infty}^{0} \frac{1}{1+x^2}\,dx = \lim_{t \to -\infty} \left[\arctan x\right]_t^0$$
$$= \arctan(0) - \lim_{t \to -\infty} \arctan(t) = 0 - \left(-\frac{\pi}{2}\right) = \frac{\pi}{2}$$

**Paso 4:** Evaluamos la segunda parte:
$$\int_0^{\infty} \frac{1}{1+x^2}\,dx = \lim_{s \to \infty} \left[\arctan x\right]_0^s$$
$$= \lim_{s \to \infty} \arctan(s) - \arctan(0) = \frac{\pi}{2} - 0 = \frac{\pi}{2}$$

**Paso 5:** Sumamos:
$$\int_{-\infty}^{\infty} \frac{1}{1+x^2}\,dx = \frac{\pi}{2} + \frac{\pi}{2} = \pi$$

**Resultado:** La integral converge y su valor es $\boxed{\pi}$.

---

## Método 8: Sustitución en Impropias

### Cuándo Usar
Para simplificar la integral antes de evaluar, especialmente con sustituciones trigonométricas.

### Punto Clave
Al hacer [sustitución](../../../glossary.md#sustitución), los límites de integración **también cambian**. Un límite infinito puede convertirse en un valor finito.

### Algoritmo de Resolución

| Paso | Acción | Cuidado |
|------|--------|---------|
| 1 | Aplicar sustitución usual | $u = g(x)$, $du = g'(x)dx$ |
| 2 | Cambiar límites de integración | Evaluar $g(a)$ y $g(b)$ |
| 3 | Si $x \to \infty$, determinar $u \to ?$ | Puede ser finito |
| 4 | Evaluar la nueva integral | Puede ser propia o impropia |

### Ejemplo Detallado

**Problema:** Evaluar $\int_1^{\infty} \frac{1}{x\sqrt{x^2-1}}\,dx$

**Paso 1:** Hacemos la [sustitución trigonométrica](../../../glossary.md#sustitución-trigonométrica) $x = \sec\theta$:
- $dx = \sec\theta\tan\theta\,d\theta$
- $\sqrt{x^2-1} = \sqrt{\sec^2\theta - 1} = \tan\theta$

**Paso 2:** Cambiamos los límites:
- Cuando $x = 1$: $\sec\theta = 1 \Rightarrow \theta = 0$
- Cuando $x \to \infty$: $\sec\theta \to \infty \Rightarrow \theta \to \frac{\pi}{2}$

**Paso 3:** Sustituimos:
$$\int_1^{\infty} \frac{1}{x\sqrt{x^2-1}}\,dx = \int_0^{\pi/2} \frac{\sec\theta\tan\theta}{\sec\theta \cdot \tan\theta}\,d\theta$$

$$= \int_0^{\pi/2} 1\,d\theta = \left[\theta\right]_0^{\pi/2} = \frac{\pi}{2}$$

**Resultado:** La integral converge y su valor es $\boxed{\frac{\pi}{2}}$.

---

## Método 9: Identificar Formas Conocidas

### Cuándo Usar
Para reconocer integrales clásicas cuyo valor es conocido.

### Tabla de Integrales Impropias Famosas

| Integral | Valor | Condición |
|----------|-------|-----------|
| $\int_0^{\infty} e^{-ax}\,dx$ | $\frac{1}{a}$ | $a > 0$ |
| $\int_0^{\infty} x^{n}e^{-x}\,dx$ | $n!$ | $n \in \mathbb{N}$ (función Gamma) |
| $\int_{-\infty}^{\infty} e^{-x^2}\,dx$ | $\sqrt{\pi}$ | Integral gaussiana |
| $\int_0^{\infty} \frac{\sin x}{x}\,dx$ | $\frac{\pi}{2}$ | Integral de Dirichlet |
| $\int_0^{\infty} e^{-x^2}\,dx$ | $\frac{\sqrt{\pi}}{2}$ | Mitad de gaussiana |

### Ejemplo Detallado

**Problema:** Evaluar $\int_0^{\infty} x^3 e^{-x}\,dx$

**Paso 1:** Reconocemos la forma $\int_0^{\infty} x^n e^{-x}\,dx = n!$

**Paso 2:** Con $n = 3$:
$$\int_0^{\infty} x^3 e^{-x}\,dx = 3! = 6$$

**Verificación por partes (opcional):**
Usando [integración por partes](../../../glossary.md#integración-por-partes) repetida o la fórmula de reducción, se confirma que el resultado es $6$.

**Resultado:** $\boxed{6}$

---

## Método 10: Análisis de Comportamiento Asintótico

### Cuándo Usar
Para determinar convergencia sin calcular la integral, analizando el comportamiento del integrando.

### Principios Guía

**Para $x \to \infty$:**
- Si $f(x) \sim \frac{c}{x^p}$ con $p > 1$: converge
- Si $f(x) \sim \frac{c}{x^p}$ con $p \leq 1$: diverge

**Para $x \to 0^+$ (discontinuidad):**
- Si $f(x) \sim \frac{c}{x^p}$ con $p < 1$: converge
- Si $f(x) \sim \frac{c}{x^p}$ con $p \geq 1$: diverge

### Ejemplo Detallado

**Problema:** Determinar si $\int_2^{\infty} \frac{\ln x}{x^2}\,dx$ converge.

**Paso 1:** Analizamos el comportamiento para $x$ grande:
- $\ln x$ crece más lento que cualquier potencia positiva de $x$
- Específicamente: $\ln x < x^{1/2}$ para $x$ suficientemente grande

**Paso 2:** Establecemos la comparación:
$$\frac{\ln x}{x^2} < \frac{x^{1/2}}{x^2} = \frac{1}{x^{3/2}}$$

**Paso 3:** Verificamos convergencia de la cota:
$$\int_2^{\infty} \frac{1}{x^{3/2}}\,dx$$

Con $p = \frac{3}{2} > 1$, esta integral converge (test p).

**Paso 4:** Por comparación directa:
Como $0 < \frac{\ln x}{x^2} < \frac{1}{x^{3/2}}$ y la integral mayor converge, la integral original **converge**.

**Resultado:** La integral $\int_2^{\infty} \frac{\ln x}{x^2}\,dx$ **converge**.
