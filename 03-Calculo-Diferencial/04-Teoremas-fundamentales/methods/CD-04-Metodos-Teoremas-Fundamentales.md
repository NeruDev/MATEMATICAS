<!--
::METADATA::
type: method
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Métodos para Teoremas Fundamentales del Cálculo Diferencial

> Guía completa de teoremas fundamentales con demostraciones, algoritmos de aplicación y ejemplos detallados.

---

## Método 1: Teorema de Rolle

**Cuándo Usar:** Para demostrar la existencia de al menos un punto donde $f'(c) = 0$ en un intervalo.

### Enunciado del Teorema

Si $f$ satisface:
1. $f$ es continua en $[a, b]$
2. $f$ es derivable en $(a, b)$
3. $f(a) = f(b)$

Entonces existe al menos un $c \in (a, b)$ [tal que](../../../glossary.md#tal-que) $f'(c) = 0$.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar [continuidad](../../../glossary.md#continuidad) | $f$ continua en $[a, b]$ |
| 2 | Verificar derivabilidad | $f$ derivable en $(a, b)$ |
| 3 | Verificar $f(a) = f(b)$ | Calcular ambos valores |
| 4 | Resolver $f'(x) = 0$ | Encontrar los valores de $c$ |
| 5 | Verificar $c \in (a, b)$ | El valor debe estar en el interior |

### Ejemplo Detallado

**Problema:** Verificar el Teorema de Rolle para $f(x) = x^3 - 3x$ en $[-\sqrt{3}, \sqrt{3}]$

---

**Paso 1: Verificar [continuidad](../../../glossary.md#continuidad)**

$f(x) = x^3 - 3x$ es un [polinomio](../../../glossary.md#polinomio), continuo en todo $\mathbb{R}$ ✓

---

**Paso 2: Verificar derivabilidad**

$f'(x) = 3x^2 - 3$ existe para todo $x \in \mathbb{R}$ ✓

---

**Paso 3: Verificar $f(a) = f(b)$**

$$f(-\sqrt{3}) = (-\sqrt{3})^3 - 3(-\sqrt{3}) = -3\sqrt{3} + 3\sqrt{3} = 0$$
$$f(\sqrt{3}) = (\sqrt{3})^3 - 3(\sqrt{3}) = 3\sqrt{3} - 3\sqrt{3} = 0$$

$f(-\sqrt{3}) = f(\sqrt{3}) = 0$ ✓

---

**Paso 4: Resolver $f'(x) = 0$**

$$3x^2 - 3 = 0$$
$$x^2 = 1$$
$$x = \pm 1$$

---

**Paso 5: Verificar $c \in (-\sqrt{3}, \sqrt{3})$**

Como $\sqrt{3} \approx 1.732$, ambos valores $c_1 = -1$ y $c_2 = 1$ están en $(-\sqrt{3}, \sqrt{3})$ ✓

$$\boxed{c_1 = -1, \quad c_2 = 1}$$

---

## Método 2: Teorema del Valor Medio (TVM)

**Cuándo Usar:** Para relacionar el cambio promedio de una [función](../../../glossary.md#funcion) con su [derivada](../../../glossary.md#derivada) instantánea.

### Enunciado del Teorema

Si $f$ satisface:
1. $f$ es continua en $[a, b]$
2. $f$ es derivable en $(a, b)$

Entonces existe al menos un $c \in (a, b)$ [tal que](../../../glossary.md#tal-que):
$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

### Interpretación Geométrica

> La pendiente de la recta secante entre $(a, f(a))$ y $(b, f(b))$ es igual a la pendiente de la recta [tangente](../../../glossary.md#tangente) en algún punto $c$ intermedio.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar hipótesis | Continuidad y derivabilidad |
| 2 | Calcular $f(a)$ y $f(b)$ | Los valores en los extremos |
| 3 | Calcular pendiente secante | $m = \frac{f(b) - f(a)}{b - a}$ |
| 4 | Resolver $f'(x) = m$ | Para encontrar $c$ |
| 5 | Verificar $c \in (a, b)$ | Confirmar que está en el intervalo |

### Ejemplo Detallado

**Problema:** Encontrar el valor de $c$ garantizado por el TVM para $f(x) = x^2 + 2x - 1$ en $[0, 2]$

---

**Paso 1: Verificar hipótesis**

$f(x)$ es [polinomio](../../../glossary.md#polinomio): continua y derivable en todo $\mathbb{R}$ ✓

---

**Paso 2: Calcular valores en extremos**

$$f(0) = 0 + 0 - 1 = -1$$
$$f(2) = 4 + 4 - 1 = 7$$

---

**Paso 3: Calcular pendiente de la secante**

$$m = \frac{f(2) - f(0)}{2 - 0} = \frac{7 - (-1)}{2} = \frac{8}{2} = 4$$

---

**Paso 4: Resolver $f'(x) = 4$**

$$f'(x) = 2x + 2$$
$$2x + 2 = 4$$
$$2x = 2$$
$$x = 1$$

---

**Paso 5: Verificar**

$c = 1 \in (0, 2)$ ✓

$$\boxed{c = 1}$$

**Verificación:** $f'(1) = 2(1) + 2 = 4 = \frac{f(2) - f(0)}{2 - 0}$ ✓

---

## Método 3: Regla de L'Hôpital (Forma $\frac{0}{0}$)

**Cuándo Usar:** [Límites](../../../glossary.md#limites) de la forma $\frac{0}{0}$ que no se pueden resolver por métodos algebraicos simples.

### Enunciado

Si $\displaystyle\lim_{x \to a} f(x) = 0$ y $\displaystyle\lim_{x \to a} g(x) = 0$, y el [límite](../../../glossary.md#limite) $\displaystyle\lim_{x \to a} \frac{f'(x)}{g'(x)}$ existe, entonces:

$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar forma $\frac{0}{0}$ | Sustituir directamente |
| 2 | Derivar numerador y denominador | Por separado |
| 3 | Evaluar nuevo [límite](../../../glossary.md#necesario) | Si sigue siendo indeterminado |

### Ejemplo Detallado

**Problema:** Calcular $\displaystyle\lim_{x \to 0} \frac{e^x - 1 - x}{x^2}$

---

**Paso 1: Verificar forma**

$$\frac{e^0 - 1 - 0}{0^2} = \frac{1 - 1 - 0}{0} = \frac{0}{0}$$

---

**Paso 2: Aplicar L'Hôpital (primera vez)**

$$\lim_{x \to 0} \frac{e^x - 1 - x}{x^2} = \lim_{x \to 0} \frac{\frac{d}{dx}[e^x - 1 - x]}{\frac{d}{dx}[x^2]}$$
$$= \lim_{x \to 0} \frac{e^x - 1}{2x}$$

---

**Paso 3: Verificar nueva forma**

$$\frac{e^0 - 1}{2(0)} = \frac{0}{0}$$

Sigue siendo indeterminado.

---

**Paso 4: Aplicar L'Hôpital (segunda vez)**

$$\lim_{x \to 0} \frac{e^x - 1}{2x} = \lim_{x \to 0} \frac{e^x}{2} = \frac{e^0}{2} = \frac{1}{2}$$

$$\boxed{\lim_{x \to 0} \frac{e^x - 1 - x}{x^2} = \frac{1}{2}}$$

---

## Método 4: Regla de L'Hôpital (Forma $\frac{\infty}{\infty}$)

**Cuándo Usar:** [Límites](../../../glossary.md#limites) donde tanto numerador como denominador tienden a infinito.

### Ejemplo Detallado

**Problema:** Calcular $\displaystyle\lim_{x \to \infty} \frac{\ln x}{x}$

---

**Paso 1: Verificar forma**

$$\frac{\ln(\infty)}{\infty} = \frac{\infty}{\infty}$$

---

**Paso 2: Aplicar L'Hôpital**

$$\lim_{x \to \infty} \frac{\ln x}{x} = \lim_{x \to \infty} \frac{1/x}{1} = \lim_{x \to \infty} \frac{1}{x} = 0$$

$$\boxed{\lim_{x \to \infty} \frac{\ln x}{x} = 0}$$

---

### Ejemplo con múltiples aplicaciones

**Problema:** Calcular $\displaystyle\lim_{x \to \infty} \frac{x^3}{e^x}$

---

**Verificar:** $\frac{\infty}{\infty}$

**L'Hôpital 1:**
$$\lim_{x \to \infty} \frac{3x^2}{e^x} \quad \text{(aún } \frac{\infty}{\infty}\text{)}$$

**L'Hôpital 2:**
$$\lim_{x \to \infty} \frac{6x}{e^x} \quad \text{(aún } \frac{\infty}{\infty}\text{)}$$

**L'Hôpital 3:**
$$\lim_{x \to \infty} \frac{6}{e^x} = \frac{6}{\infty} = 0$$

$$\boxed{\lim_{x \to \infty} \frac{x^3}{e^x} = 0}$$

**Conclusión:** La exponencial crece más rápido que cualquier polinomio.

---

## Método 5: L'Hôpital para Forma $0 \cdot \infty$

**Cuándo Usar:** Productos donde un factor tiende a 0 y otro a infinito.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar forma $0 \cdot \infty$ | Verificar límites de cada factor |
| 2 | Reescribir como cociente | $f \cdot g = \frac{f}{1/g}$ o $\frac{g}{1/f}$ |
| 3 | Aplicar L'Hôpital | Al nuevo cociente |

### Ejemplo Detallado

**Problema:** Calcular $\displaystyle\lim_{x \to 0^+} x \ln x$

---

**Paso 1: Identificar forma**

$$\lim_{x \to 0^+} x = 0, \quad \lim_{x \to 0^+} \ln x = -\infty$$

Forma: $0 \cdot (-\infty)$

---

**Paso 2: Reescribir como cociente**

$$x \ln x = \frac{\ln x}{1/x} = \frac{\ln x}{x^{-1}}$$

Ahora tenemos: $\frac{-\infty}{\infty}$

---

**Paso 3: Aplicar L'Hôpital**

$$\lim_{x \to 0^+} \frac{\ln x}{x^{-1}} = \lim_{x \to 0^+} \frac{1/x}{-x^{-2}} = \lim_{x \to 0^+} \frac{1/x}{-1/x^2}$$

$$= \lim_{x \to 0^+} \frac{x^2}{-x} = \lim_{x \to 0^+} (-x) = 0$$

$$\boxed{\lim_{x \to 0^+} x \ln x = 0}$$

---

## Método 6: L'Hôpital para Forma $\infty - \infty$

**Cuándo Usar:** Diferencias de funciones donde ambas tienden a infinito.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar forma $\infty - \infty$ | Verificar límites |
| 2 | Combinar en fracción común | O racionalizar |
| 3 | Simplificar | Obtener $\frac{0}{0}$ o $\frac{\infty}{\infty}$ |
| 4 | Aplicar L'Hôpital | Si es [necesario](../../../glossary.md#necesario) |

### Ejemplo Detallado

**Problema:** Calcular $\displaystyle\lim_{x \to 0^+} \left(\frac{1}{x} - \frac{1}{\sin x}\right)$

---

**Paso 1: Verificar forma**

$$\lim_{x \to 0^+} \frac{1}{x} = +\infty, \quad \lim_{x \to 0^+} \frac{1}{\sin x} = +\infty$$

Forma: $\infty - \infty$

---

**Paso 2: Combinar en fracción común**

$$\frac{1}{x} - \frac{1}{\sin x} = \frac{\sin x - x}{x \sin x}$$

---

**Paso 3: Verificar nueva forma**

$$\frac{\sin 0 - 0}{0 \cdot \sin 0} = \frac{0}{0}$$

---

**Paso 4: Aplicar L'Hôpital**

$$\lim_{x \to 0^+} \frac{\sin x - x}{x \sin x} = \lim_{x \to 0^+} \frac{\cos x - 1}{\sin x + x \cos x}$$

Verificar: $\frac{\cos 0 - 1}{\sin 0 + 0} = \frac{0}{0}$

---

**Paso 5: L'Hôpital segunda vez**

$$= \lim_{x \to 0^+} \frac{-\sin x}{\cos x + \cos x - x\sin x} = \frac{0}{2} = 0$$

$$\boxed{\lim_{x \to 0^+} \left(\frac{1}{x} - \frac{1}{\sin x}\right) = 0}$$

---

## Método 7: L'Hôpital para Formas Exponenciales ($0^0$, $1^\infty$, $\infty^0$)

**Cuándo Usar:** Límites de la forma $[f(x)]^{g(x)}$ donde la [base](../../../glossary.md#base) y/o exponente producen indeterminación.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Sea $y = [f(x)]^{g(x)}$ | Definir la expresión |
| 2 | Tomar logaritmo | $\ln y = g(x) \ln f(x)$ |
| 3 | Calcular $\lim(\ln y)$ | Forma $0 \cdot \infty$ generalmente |
| 4 | Resultado | $\lim y = e^{\lim(\ln y)}$ |

### Ejemplo Detallado: Forma $1^\infty$

**Problema:** Calcular $\displaystyle\lim_{x \to 0^+} (1 + x)^{1/x}$

---

**Paso 1: Definir**

Sea $y = (1 + x)^{1/x}$

---

**Paso 2: Tomar logaritmo**

$$\ln y = \frac{1}{x} \ln(1 + x) = \frac{\ln(1 + x)}{x}$$

---

**Paso 3: Calcular límite (forma $\frac{0}{0}$)**

$$\lim_{x \to 0^+} \frac{\ln(1 + x)}{x} = \lim_{x \to 0^+} \frac{\frac{1}{1+x}}{1} = \frac{1}{1+0} = 1$$

---

**Paso 4: Resultado**

$$\lim_{x \to 0^+} \ln y = 1$$
$$\lim_{x \to 0^+} y = e^1 = e$$

$$\boxed{\lim_{x \to 0^+} (1 + x)^{1/x} = e}$$

---

### Ejemplo: Forma $0^0$

**Problema:** Calcular $\displaystyle\lim_{x \to 0^+} x^x$

---

**Sea $y = x^x$**

$$\ln y = x \ln x$$

---

**Calcular $\lim(x \ln x)$** (forma $0 \cdot (-\infty)$):

$$\lim_{x \to 0^+} x \ln x = \lim_{x \to 0^+} \frac{\ln x}{1/x} = \lim_{x \to 0^+} \frac{1/x}{-1/x^2} = \lim_{x \to 0^+} (-x) = 0$$

---

**Resultado:**

$$\lim_{x \to 0^+} y = e^0 = 1$$

$$\boxed{\lim_{x \to 0^+} x^x = 1}$$

---

## Método 8: Series de Taylor

**Cuándo Usar:** Para aproximar funciones mediante polinomios, calcular límites, o representar funciones como series infinitas.

### Fórmula de Taylor

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$$

$$= f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots$$

### Series de Maclaurin Importantes (Taylor en $a = 0$)

| [Función](../../../glossary.md#derivadas) | $f(a), f'(a), f''(a), \ldots$ |
| 3 | Escribir términos | $\frac{f^{(n)}(a)}{n!}(x-a)^n$ |
| 4 | Identificar patrón | Si existe |

### Ejemplo Detallado

**Problema:** Encontrar el polinomio de Taylor de grado 4 para $f(x) = e^x$ centrado en $a = 0$

---

**Paso 1: Calcular [derivadas](../../../glossary.md#derivadas) y evaluarlas en $a = 0$**

| $n$ | $f^{(n)}(x)$ | $f^{(n)}(0)$ |
|-----|-------------|-------------|
| 0 | $e^x$ | $1$ |
| 1 | $e^x$ | $1$ |
| 2 | $e^x$ | $1$ |
| 3 | $e^x$ | $1$ |
| 4 | $e^x$ | $1$ |

---

**Paso 2: Escribir el polinomio**

$$P_4(x) = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!}$$

$$= 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24}$$

$$\boxed{P_4(x) = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24}}$$

---

### Aplicación: Calcular Límite con Taylor

**Problema:** Calcular $\displaystyle\lim_{x \to 0} \frac{\sin x - x}{x^3}$

---

**Usando serie de $\sin x$:**

$$\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots$$

$$\sin x - x = -\frac{x^3}{6} + \frac{x^5}{120} - \cdots$$

$$\frac{\sin x - x}{x^3} = \frac{-\frac{x^3}{6} + \frac{x^5}{120} - \cdots}{x^3}$$

$$= -\frac{1}{6} + \frac{x^2}{120} - \cdots$$

$$\lim_{x \to 0} = -\frac{1}{6}$$

$$\boxed{\lim_{x \to 0} \frac{\sin x - x}{x^3} = -\frac{1}{6}}$$

---

## Método 9: Error en Aproximación de Taylor

**Cuándo Usar:** Para estimar la precisión de una aproximación de Taylor.

### Fórmula del Residuo (Lagrange)

$$R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$

donde $c$ está entre $a$ y $x$.

### Cota del Error

$$|R_n(x)| \leq \frac{M}{(n+1)!}|x-a|^{n+1}$$

donde $M = \max|f^{(n+1)}(t)|$ para $t$ entre $a$ y $x$.

### Ejemplo Detallado

**Problema:** Estimar el error al aproximar $e^{0.1}$ usando el polinomio de Taylor de grado 3.

---

**Polinomio:**
$$P_3(0.1) = 1 + 0.1 + \frac{(0.1)^2}{2} + \frac{(0.1)^3}{6}$$
$$= 1 + 0.1 + 0.005 + 0.000167 = 1.105167$$

---

**Error:**
$$R_3(0.1) = \frac{e^c}{4!}(0.1)^4$$

donde $0 < c < 0.1$.

Como $e^c < e^{0.1} < e^1 < 3$:

$$|R_3(0.1)| < \frac{3}{24}(0.0001) = \frac{0.0003}{24} = 0.0000125$$

$$\boxed{|Error| < 0.0000125}$$

---

## Método 10: Series de Maclaurin para Funciones Compuestas

**Cuándo Usar:** Para encontrar series de funciones como $e^{-x^2}$, $\sin(x^2)$, etc.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar serie [base](../../../glossary.md#base) | $e^u$, $\sin u$, etc. |
| 2 | Sustituir | $u$ por la expresión compuesta |
| 3 | Expandir | Los términos resultantes |

### Ejemplo Detallado

**Problema:** Encontrar los primeros 4 términos de la serie de $f(x) = e^{-x^2}$

---

**Paso 1: Serie base**

$$e^u = 1 + u + \frac{u^2}{2!} + \frac{u^3}{3!} + \cdots$$

---

**Paso 2: Sustituir $u = -x^2$**

$$e^{-x^2} = 1 + (-x^2) + \frac{(-x^2)^2}{2!} + \frac{(-x^2)^3}{3!} + \cdots$$

---

**Paso 3: Simplificar**

$$= 1 - x^2 + \frac{x^4}{2} - \frac{x^6}{6} + \cdots$$

$$\boxed{e^{-x^2} = 1 - x^2 + \frac{x^4}{2} - \frac{x^6}{6} + \cdots}$$

---

## Resumen: Cuándo Usar Cada Método

| Situación | Método Recomendado |
|-----------|-------------------|
| $f(a) = f(b)$, buscar $f'(c) = 0$ | Teorema de Rolle |
| Relacionar $\frac{f(b)-f(a)}{b-a}$ con $f'(c)$ | TVM |
| $\frac{0}{0}$ | L'Hôpital |
| $\frac{\infty}{\infty}$ | L'Hôpital |
| $0 \cdot \infty$ | Reescribir + L'Hôpital |
| $\infty - \infty$ | Combinar fracciones + L'Hôpital |
| $0^0$, $1^\infty$, $\infty^0$ | Logaritmo + L'Hôpital |
| Aproximación de funciones | Series de Taylor |
| Límites complicados | Taylor (alternativa a L'Hôpital) |

---

## Tabla de Formas Indeterminadas y Estrategias

| Forma | Estrategia |
|-------|------------|
| $\frac{0}{0}$ | L'Hôpital directo |
| $\frac{\infty}{\infty}$ | L'Hôpital directo |
| $0 \cdot \infty$ | Convertir a $\frac{0}{0}$ o $\frac{\infty}{\infty}$ |
| $\infty - \infty$ | Fracción común o racionalizar |
| $0^0$ | $y = f^g \Rightarrow \ln y = g \ln f$ |
| $1^\infty$ | $y = f^g \Rightarrow \ln y = g \ln f$ |
| $\infty^0$ | $y = f^g \Rightarrow \ln y = g \ln f$ |

---

## Errores Comunes

| Error | Corrección |
|-------|------------|
| Aplicar L'Hôpital sin verificar forma | Solo para $\frac{0}{0}$ o $\frac{\infty}{\infty}$ |
| Derivar como cociente $\frac{f'}{g'}$ | NO es $\left(\frac{f}{g}\right)'$; derivar numerador y denominador por separado |
| Olvidar verificar hipótesis de Rolle/TVM | Siempre verificar continuidad y derivabilidad |
| No verificar que $c \in (a,b)$ | El punto debe estar en el interior del intervalo |
| Aplicar L'Hôpital indefinidamente | Si no converge, usar otro método |
| Confundir Taylor con Maclaurin | Maclaurin es Taylor con $a = 0$ |
| Olvidar el residuo en aproximaciones | Siempre considerar el error |
