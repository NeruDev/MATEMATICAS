<!--
::METADATA::
type: method
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Métodos para Calcular Derivadas

> Guía completa de reglas de derivación con algoritmos detallados, tablas de fórmulas y ejemplos paso a paso.

---

## Método 1: Derivación Directa (Regla de la Potencia)

**Cuándo Usar:** Funciones polinómicas, potencias de $x$, y combinaciones lineales.

### Fórmulas Fundamentales

| [Función](../../../glossary.md#derivada) |
|---------|----------|
| $c$ (constante) | $0$ |
| $x^n$ | $nx^{n-1}$ |
| $cf(x)$ | $cf'(x)$ |
| $f(x) \pm g(x)$ | $f'(x) \pm g'(x)$ |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar términos | Separar sumas y diferencias |
| 2 | Aplicar regla de potencia | $\frac{d}{dx}[x^n] = nx^{n-1}$ |
| 3 | Sacar constantes | $\frac{d}{dx}[cf(x)] = c\frac{d}{dx}[f(x)]$ |
| 4 | Simplificar | Reducir exponentes y coeficientes |

### Ejemplo Detallado

**Problema:** Derivar $f(x) = 3x^5 - 2x^3 + 7x - 4$

---

**Paso 1: Derivar término por término**

$$f'(x) = \frac{d}{dx}[3x^5] - \frac{d}{dx}[2x^3] + \frac{d}{dx}[7x] - \frac{d}{dx}[4]$$

---

**Paso 2: Aplicar la regla de la potencia**

$$= 3 \cdot 5x^{5-1} - 2 \cdot 3x^{3-1} + 7 \cdot 1x^{1-1} - 0$$

---

**Paso 3: Simplificar**

$$= 15x^4 - 6x^2 + 7$$

$$\boxed{f'(x) = 15x^4 - 6x^2 + 7}$$

---

### Ejemplo con Exponentes Fraccionarios y Negativos

**Problema:** Derivar $g(x) = \sqrt{x} + \frac{1}{x^2} - \frac{3}{\sqrt[3]{x}}$

---

**Paso 1: Reescribir con exponentes**

$$g(x) = x^{1/2} + x^{-2} - 3x^{-1/3}$$

---

**Paso 2: Derivar**

$$g'(x) = \frac{1}{2}x^{-1/2} + (-2)x^{-3} - 3 \cdot \left(-\frac{1}{3}\right)x^{-4/3}$$

---

**Paso 3: Simplificar**

$$= \frac{1}{2}x^{-1/2} - 2x^{-3} + x^{-4/3}$$

$$= \frac{1}{2\sqrt{x}} - \frac{2}{x^3} + \frac{1}{\sqrt[3]{x^4}}$$

$$\boxed{g'(x) = \frac{1}{2\sqrt{x}} - \frac{2}{x^3} + \frac{1}{\sqrt[3]{x^4}}}$$

---

## Método 2: Regla del Producto

**Cuándo Usar:** Derivar el producto de dos funciones: $h(x) = f(x) \cdot g(x)$

### Fórmula

$$\frac{d}{dx}[f(x) \cdot g(x)] = f'(x) \cdot g(x) + f(x) \cdot g'(x)$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar $f$ y $g$ | Las dos funciones multiplicadas |
| 2 | Calcular [derivadas](../../../glossary.md#factorizar) si es posible |

### Ejemplo Detallado

**Problema:** Derivar $h(x) = (x^2 + 3x)(2x^3 - x)$

---

**Paso 1: Identificar funciones**

$$f(x) = x^2 + 3x, \quad g(x) = 2x^3 - x$$

---

**Paso 2: Calcular [derivadas](../../../glossary.md#derivadas)**

$$f'(x) = 2x + 3$$
$$g'(x) = 6x^2 - 1$$

---

**Paso 3: Aplicar regla del producto**

$$h'(x) = f'(x) \cdot g(x) + f(x) \cdot g'(x)$$
$$= (2x + 3)(2x^3 - x) + (x^2 + 3x)(6x^2 - 1)$$

---

**Paso 4: Expandir y simplificar**

Primer término:
$$= 4x^4 - 2x^2 + 6x^3 - 3x$$

Segundo término:
$$= 6x^4 - x^2 + 18x^3 - 3x$$

Suma:
$$= 4x^4 + 6x^4 + 6x^3 + 18x^3 - 2x^2 - x^2 - 3x - 3x$$
$$= 10x^4 + 24x^3 - 3x^2 - 6x$$

$$\boxed{h'(x) = 10x^4 + 24x^3 - 3x^2 - 6x}$$

---

## Método 3: Regla del Cociente

**Cuándo Usar:** Derivar el cociente de dos funciones: $h(x) = \frac{f(x)}{g(x)}$

### Fórmula

$$\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{[g(x)]^2}$$

### Nemotecnia

> "Lo de abajo por la [derivada](../../../glossary.md#derivada) de lo de arriba, menos lo de arriba por la derivada de lo de abajo, todo sobre lo de abajo al cuadrado"

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar $f$ y $g$ | Numerador y denominador |
| 2 | Calcular derivadas | $f'(x)$ y $g'(x)$ |
| 3 | Aplicar fórmula | $\frac{f'g - fg'}{g^2}$ |
| 4 | Simplificar | [Factorizar](../../../glossary.md#factorizar) numerador si es posible |

### Ejemplo Detallado

**Problema:** Derivar $h(x) = \frac{x^2 - 1}{x^2 + 1}$

---

**Paso 1: Identificar funciones**

$$f(x) = x^2 - 1, \quad g(x) = x^2 + 1$$

---

**Paso 2: Calcular derivadas**

$$f'(x) = 2x, \quad g'(x) = 2x$$

---

**Paso 3: Aplicar regla del cociente**

$$h'(x) = \frac{(2x)(x^2 + 1) - (x^2 - 1)(2x)}{(x^2 + 1)^2}$$

---

**Paso 4: Simplificar numerador**

$$= \frac{2x^3 + 2x - 2x^3 + 2x}{(x^2 + 1)^2}$$
$$= \frac{4x}{(x^2 + 1)^2}$$

$$\boxed{h'(x) = \frac{4x}{(x^2 + 1)^2}}$$

---

## Método 4: Regla de la Cadena

**Cuándo Usar:** Funciones compuestas: $h(x) = f(g(x))$

### Fórmula

$$\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$$

### Notación alternativa (Leibniz)

Si $y = f(u)$ y $u = g(x)$:
$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar [función](../../..](../../../glossary.md#regla-de-la-cadena)**

$$h'(x) = f'(g(x)) \cdot g'(x)$$
$$= 5(3x^2 + 2x - 1)^4 \cdot (6x + 2)$$

---

**Paso 4: Simplificar (factorizar si es útil)**

$$= 5(6x + 2)(3x^2 + 2x - 1)^4$$
$$= 10(3x + 1)(3x^2 + 2x - 1)^4$$

$$\boxed{h'(x) = 10(3x + 1)(3x^2 + 2x - 1)^4}$$

---

### Ejemplo con Función Trigonométrica

**Problema:** Derivar $f(x) = \sin(x^3 + 2x)$

---

**Paso 1: Identificar**

Externa: $\sin(u)$, Interna: $u = x^3 + 2x$

---

**Paso 2: Derivadas**

$$\frac{d}{du}[\sin u] = \cos u$$
$$\frac{d}{dx}[x^3 + 2x] = 3x^2 + 2$$

---

**Paso 3: Aplicar cadena**

$$f'(x) = \cos(x^3 + 2x) \cdot (3x^2 + 2)$$

$$\boxed{f'(x) = (3x^2 + 2)\cos(x^3 + 2x)}$$

---

## Método 5: Derivación Implícita

**Cuándo Usar:** Cuando $y$ está definida implícitamente por una ecuación $F(x, y) = 0$.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Derivar ambos lados | Respecto a $x$ |
| 2 | Usar regla de cadena | Para términos con $y$: $\frac{d}{dx}[y^n] = ny^{n-1}\frac{dy}{dx}$ |
| 3 | Agrupar términos | Con $\frac{dy}{dx}$ a un lado |
| 4 | Despejar $\frac{dy}{dx}$ | Factorizar y dividir |

### Ejemplo Detallado

**Problema:** Encontrar $\frac{dy}{dx}$ si $x^2 + y^2 = 25$

---

**Paso 1: Derivar ambos lados respecto a $x$**

$$\frac{d}{dx}[x^2] + \frac{d}{dx}[y^2] = \frac{d}{dx}[25]$$

---

**Paso 2: Aplicar reglas (cadena para $y^2$)**

$$2x + 2y\frac{dy}{dx} = 0$$

---

**Paso 3: Despejar $\frac{dy}{dx}$**

$$2y\frac{dy}{dx} = -2x$$
$$\frac{dy}{dx} = \frac{-2x}{2y} = -\frac{x}{y}$$

$$\boxed{\frac{dy}{dx} = -\frac{x}{y}}$$

---

### Ejemplo Más Complejo

**Problema:** Encontrar $\frac{dy}{dx}$ si $x^3 + y^3 = 6xy$

---

**Paso 1: Derivar ambos lados**

$$\frac{d}{dx}[x^3] + \frac{d}{dx}[y^3] = \frac{d}{dx}[6xy]$$

---

**Paso 2: Aplicar reglas**

- $\frac{d}{dx}[x^3] = 3x^2$
- $\frac{d}{dx}[y^3] = 3y^2\frac{dy}{dx}$ (cadena)
- $\frac{d}{dx}[6xy] = 6y + 6x\frac{dy}{dx}$ (producto)

$$3x^2 + 3y^2\frac{dy}{dx} = 6y + 6x\frac{dy}{dx}$$

---

**Paso 3: Agrupar términos con $\frac{dy}{dx}$**

$$3y^2\frac{dy}{dx} - 6x\frac{dy}{dx} = 6y - 3x^2$$

---

**Paso 4: Factorizar y despejar**

$$\frac{dy}{dx}(3y^2 - 6x) = 6y - 3x^2$$
$$\frac{dy}{dx} = \frac{6y - 3x^2}{3y^2 - 6x} = \frac{3(2y - x^2)}{3(y^2 - 2x)} = \frac{2y - x^2}{y^2 - 2x}$$

$$\boxed{\frac{dy}{dx} = \frac{2y - x^2}{y^2 - 2x}}$$

---

## Método 6: Derivación Logarítmica

**Cuándo Usar:** Productos/cocientes complicados, funciones de la forma $f(x)^{g(x)}$, o para simplificar derivadas.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Tomar logaritmo natural | $\ln y = \ln f(x)$ |
| 2 | Simplificar con propiedades | $\ln(ab) = \ln a + \ln b$, $\ln\frac{a}{b} = \ln a - \ln b$, $\ln a^n = n\ln a$ |
| 3 | Derivar implícitamente | $\frac{1}{y}\frac{dy}{dx} = \frac{d}{dx}[\ln f(x)]$ |
| 4 | Despejar y sustituir | $\frac{dy}{dx} = y \cdot (\text{derivada del lado derecho})$ |

### Ejemplo Detallado

**Problema:** Derivar $y = x^x$ (para $x > 0$)

---

**Paso 1: Tomar logaritmo natural**

$$\ln y = \ln(x^x) = x \ln x$$

---

**Paso 2: Derivar implícitamente**

$$\frac{1}{y}\frac{dy}{dx} = \frac{d}{dx}[x \ln x]$$

---

**Paso 3: Derivar el lado derecho (producto)**

$$\frac{d}{dx}[x \ln x] = 1 \cdot \ln x + x \cdot \frac{1}{x} = \ln x + 1$$

---

**Paso 4: Despejar $\frac{dy}{dx}$**

$$\frac{dy}{dx} = y(\ln x + 1) = x^x(\ln x + 1)$$

$$\boxed{\frac{dy}{dx} = x^x(\ln x + 1)}$$

---

### Ejemplo con Producto Complejo

**Problema:** Derivar $y = \frac{x^2 \sqrt{x+1}}{(2x-3)^4}$

---

**Paso 1: Tomar logaritmo y simplificar**

$$\ln y = \ln x^2 + \ln\sqrt{x+1} - \ln(2x-3)^4$$
$$= 2\ln x + \frac{1}{2}\ln(x+1) - 4\ln(2x-3)$$

---

**Paso 2: Derivar**

$$\frac{1}{y}\frac{dy}{dx} = \frac{2}{x} + \frac{1}{2(x+1)} - \frac{4 \cdot 2}{2x-3}$$
$$= \frac{2}{x} + \frac{1}{2(x+1)} - \frac{8}{2x-3}$$

---

**Paso 3: Despejar**

$$\frac{dy}{dx} = \frac{x^2\sqrt{x+1}}{(2x-3)^4}\left(\frac{2}{x} + \frac{1}{2(x+1)} - \frac{8}{2x-3}\right)$$

$$\boxed{\frac{dy}{dx} = \frac{x^2\sqrt{x+1}}{(2x-3)^4}\left(\frac{2}{x} + \frac{1}{2(x+1)} - \frac{8}{2x-3}\right)}$$

---

## Método 7: Derivadas de Funciones Trigonométricas

**Cuándo Usar:** Funciones que involucran [seno](../../../glossary.md#seno), [coseno](../../../glossary.md#coseno), [tangente](../../../glossary.md#tangente), etc.

### Tabla de Derivadas Trigonométricas

| Función | Derivada |
|---------|----------|
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |
| $\cot x$ | $-\csc^2 x$ |
| $\sec x$ | $\sec x \tan x$ |
| $\csc x$ | $-\csc x \cot x$ |

### Ejemplo Detallado

**Problema:** Derivar $f(x) = \sec^3(2x)$

---

**Paso 1: Identificar estructura (cadena doble)**

$$f(x) = [\sec(2x)]^3$$

Externa 1: $u^3$, Media: $\sec(v)$, Interna: $v = 2x$

---

**Paso 2: Aplicar cadena (de afuera hacia adentro)**

$$f'(x) = 3[\sec(2x)]^2 \cdot \frac{d}{dx}[\sec(2x)]$$

---

**Paso 3: Derivar $\sec(2x)$ (otra cadena)**

$$\frac{d}{dx}[\sec(2x)] = \sec(2x)\tan(2x) \cdot 2$$

---

**Paso 4: Combinar**

$$f'(x) = 3\sec^2(2x) \cdot 2\sec(2x)\tan(2x)$$
$$= 6\sec^3(2x)\tan(2x)$$

$$\boxed{f'(x) = 6\sec^3(2x)\tan(2x)}$$

---

## Método 8: Derivadas de Funciones Trigonométricas Inversas

**Cuándo Usar:** Funciones arcoseno, arcocoseno, arcotangente, etc.

### Tabla de Derivadas

| Función | Derivada | [Dominio](../../../glossary.md#dominio) de validez |
|---------|----------|-------------------|
| $\arcsin x$ | $\frac{1}{\sqrt{1-x^2}}$ | $-1 < x < 1$ |
| $\arccos x$ | $-\frac{1}{\sqrt{1-x^2}}$ | $-1 < x < 1$ |
| $\arctan x$ | $\frac{1}{1+x^2}$ | $\mathbb{R}$ |
| $\text{arccot } x$ | $-\frac{1}{1+x^2}$ | $\mathbb{R}$ |
| $\text{arcsec } x$ | $\frac{1}{\vert x\vert\sqrt{x^2-1}}$ | $\vert x\vert > 1$ |
| $\text{arccsc } x$ | $-\frac{1}{\vert x\vert\sqrt{x^2-1}}$ | $\vert x\vert > 1$ |

### Ejemplo Detallado

**Problema:** Derivar $f(x) = \arctan(3x^2)$

---

**Paso 1: Identificar (cadena)**

Externa: $\arctan(u)$, Interna: $u = 3x^2$

---

**Paso 2: Derivada de arcotangente**

$$\frac{d}{du}[\arctan u] = \frac{1}{1 + u^2}$$

---

**Paso 3: Derivada de la interna**

$$\frac{d}{dx}[3x^2] = 6x$$

---

**Paso 4: Aplicar cadena**

$$f'(x) = \frac{1}{1 + (3x^2)^2} \cdot 6x = \frac{6x}{1 + 9x^4}$$

$$\boxed{f'(x) = \frac{6x}{1 + 9x^4}}$$

---

## Método 9: Derivadas de Funciones Exponenciales y Logarítmicas

**Cuándo Usar:** Funciones con $e^x$, $a^x$, $\ln x$, $\log_a x$.

### Tabla de Derivadas

| Función | Derivada |
|---------|----------|
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ | $\frac{1}{x}$ |
| $\log_a x$ | $\frac{1}{x \ln a}$ |
| $e^{g(x)}$ | $e^{g(x)} \cdot g'(x)$ |
| $\ln(g(x))$ | $\frac{g'(x)}{g(x)}$ |

### Ejemplo Detallado

**Problema:** Derivar $f(x) = e^{x^2 - 3x}$

---

**Paso 1: Identificar (cadena)**

Externa: $e^u$, Interna: $u = x^2 - 3x$

---

**Paso 2: Derivadas**

$$\frac{d}{du}[e^u] = e^u$$
$$\frac{d}{dx}[x^2 - 3x] = 2x - 3$$

---

**Paso 3: Aplicar cadena**

$$f'(x) = e^{x^2 - 3x} \cdot (2x - 3)$$

$$\boxed{f'(x) = (2x - 3)e^{x^2 - 3x}}$$

---

### Ejemplo con Logaritmo

**Problema:** Derivar $g(x) = \ln(\sin x)$

---

**Paso 1: Aplicar fórmula $\frac{d}{dx}[\ln u] = \frac{u'}{u}$**

$$g'(x) = \frac{\cos x}{\sin x} = \cot x$$

$$\boxed{g'(x) = \cot x}$$

---

## Método 10: Derivadas de Funciones Hiperbólicas

**Cuándo Usar:** Funciones sinh, cosh, tanh y sus inversas.

### Tabla de Derivadas Hiperbólicas

| Función | Derivada |
|---------|----------|
| $\sinh x$ | $\cosh x$ |
| $\cosh x$ | $\sinh x$ |
| $\tanh x$ | $\text{sech}^2 x$ |
| $\text{coth } x$ | $-\text{csch}^2 x$ |
| $\text{sech } x$ | $-\text{sech } x \tanh x$ |
| $\text{csch } x$ | $-\text{csch } x \coth x$ |

### Derivadas Hiperbólicas Inversas

| Función | Derivada |
|---------|----------|
| $\sinh^{-1} x$ | $\frac{1}{\sqrt{x^2+1}}$ |
| $\cosh^{-1} x$ | $\frac{1}{\sqrt{x^2-1}}$ |
| $\tanh^{-1} x$ | $\frac{1}{1-x^2}$ |

### Ejemplo Detallado

**Problema:** Derivar $f(x) = \tanh(x^3)$

---

**Paso 1: Aplicar cadena**

$$f'(x) = \text{sech}^2(x^3) \cdot 3x^2$$

$$\boxed{f'(x) = 3x^2 \text{sech}^2(x^3)}$$

---

## Método 11: Derivadas de Orden Superior

**Cuándo Usar:** Encontrar $f''(x)$, $f'''(x)$, etc. para análisis de [concavidad](../../../glossary.md#concavidad), aceleración, etc.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Calcular $f'(x)$ | Primera derivada |
| 2 | Derivar $f'(x)$ | Obtener $f''(x)$ |
| 3 | Repetir | Tantas veces como se necesite |

### Notaciones

| Notación Leibniz | Notación Prima | Nombre |
|------------------|----------------|--------|
| $\frac{dy}{dx}$ | $y'$ | Primera derivada |
| $\frac{d^2y}{dx^2}$ | $y''$ | Segunda derivada |
| $\frac{d^3y}{dx^3}$ | $y'''$ | Tercera derivada |
| $\frac{d^ny}{dx^n}$ | $y^{(n)}$ | n-ésima derivada |

### Ejemplo Detallado

**Problema:** Encontrar $f''(x)$ si $f(x) = x^4 - 3x^3 + 2x$

---

**Paso 1: Primera derivada**

$$f'(x) = 4x^3 - 9x^2 + 2$$

---

**Paso 2: Segunda derivada**

$$f''(x) = 12x^2 - 18x$$

$$\boxed{f''(x) = 12x^2 - 18x = 6x(2x - 3)}$$

---

### Ejemplo con Funciones Trigonométricas

**Problema:** Encontrar las primeras 4 derivadas de $f(x) = \sin x$

---

| [Orden](../../../glossary.md#orden) | Derivada |
|-------|----------|
| $f(x)$ | $\sin x$ |
| $f'(x)$ | $\cos x$ |
| $f''(x)$ | $-\sin x$ |
| $f'''(x)$ | $-\cos x$ |
| $f^{(4)}(x)$ | $\sin x$ |

**Patrón cíclico con período 4:**

$$\boxed{f^{(n)}(x) = \sin\left(x + \frac{n\pi}{2}\right)}$$

---

## Método 12: Derivadas Paramétricas

**Cuándo Usar:** Curvas definidas por $x = x(t)$, $y = y(t)$.

### Fórmula

$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{y'(t)}{x'(t)}$$

### Segunda Derivada Paramétrica

$$\frac{d^2y}{dx^2} = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{\frac{dx}{dt}}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Derivar $x$ e $y$ | Respecto a $t$ |
| 2 | Formar cociente | $\frac{dy/dt}{dx/dt}$ |
| 3 | Simplificar | Si es posible |

### Ejemplo Detallado

**Problema:** Encontrar $\frac{dy}{dx}$ si $x = t^2 - 1$, $y = t^3 + t$

---

**Paso 1: Derivar respecto a $t$**

$$\frac{dx}{dt} = 2t$$
$$\frac{dy}{dt} = 3t^2 + 1$$

---

**Paso 2: Formar cociente**

$$\frac{dy}{dx} = \frac{3t^2 + 1}{2t}$$

$$\boxed{\frac{dy}{dx} = \frac{3t^2 + 1}{2t}}$$

---

### Ejemplo: Segunda Derivada

**Continuación:** Encontrar $\frac{d^2y}{dx^2}$

---

**Paso 1: Derivar $\frac{dy}{dx}$ respecto a $t$**

$$\frac{d}{dt}\left[\frac{3t^2 + 1}{2t}\right] = \frac{6t \cdot 2t - (3t^2 + 1) \cdot 2}{4t^2}$$
$$= \frac{12t^2 - 6t^2 - 2}{4t^2} = \frac{6t^2 - 2}{4t^2} = \frac{3t^2 - 1}{2t^2}$$

---

**Paso 2: Dividir por $\frac{dx}{dt}$**

$$\frac{d^2y}{dx^2} = \frac{(3t^2 - 1)/(2t^2)}{2t} = \frac{3t^2 - 1}{4t^3}$$

$$\boxed{\frac{d^2y}{dx^2} = \frac{3t^2 - 1}{4t^3}}$$

---

## Resumen: Tabla de Derivadas Fundamentales

### Funciones Algebraicas

| Función | Derivada |
|---------|----------|
| $c$ | $0$ |
| $x^n$ | $nx^{n-1}$ |
| $\sqrt{x}$ | $\frac{1}{2\sqrt{x}}$ |
| $\frac{1}{x}$ | $-\frac{1}{x^2}$ |

### Funciones Trigonométricas

| Función | Derivada |
|---------|----------|
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |
| $\sec x$ | $\sec x \tan x$ |

### Funciones Exponenciales y Logarítmicas

| Función | Derivada |
|---------|----------|
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ | $\frac{1}{x}$ |
| $\log_a x$ | $\frac{1}{x\ln a}$ |

---

## Errores Comunes

| Error | Corrección |
|-------|------------|
| $\frac{d}{dx}[x^n] = x^{n-1}$ | Falta el coeficiente: $nx^{n-1}$ |
| $\frac{d}{dx}[\sin x] = \sin x$ | Es $\cos x$, no $\sin x$ |
| Olvidar la cadena | Siempre multiplicar por derivada interna |
| $\frac{d}{dx}[fg] = f'g'$ | Es $f'g + fg'$ (regla del producto) |
| $\frac{d}{dx}\left[\frac{f}{g}\right] = \frac{f'}{g'}$ | Es $\frac{f'g - fg'}{g^2}$ |
| $\frac{d}{dx}[e^{f(x)}] = e^{f(x)}$ | Falta: $e^{f(x)} \cdot f'(x)$ |
| $\frac{d}{dx}[\ln f(x)] = \frac{1}{f(x)}$ | Falta: $\frac{f'(x)}{f(x)}$ |
| $\frac{d}{dx}[(f \circ g)(x)] = f'(g(x))$ | Falta multiplicar por $g'(x)$ |
