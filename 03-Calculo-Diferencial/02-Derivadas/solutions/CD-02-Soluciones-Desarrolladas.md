<!--
HUMANO:
Soluciones de [derivadas](../../../glossary.md#derivadas) con contexto y desarrollo.

IA:
Cada solución incluye: contexto → desarrollo → verificación.

---
content_type: solutions
expected_output:
  default: markdown
audience: self-study
---
-->

# Soluciones de Derivadas

> **Formato:** Contexto teórico → Desarrollo paso a paso → Verificación

---

## 2.1 Definición de Derivada

### Solución 2.1.2
**Contexto:** Usar $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$

**Desarrollo:**
$$f'(x) = \lim_{h \to 0} \frac{[(x+h)^2 + (x+h)] - [x^2 + x]}{h}$$
$$= \lim_{h \to 0} \frac{x^2 + 2xh + h^2 + x + h - x^2 - x}{h}$$
$$= \lim_{h \to 0} \frac{2xh + h^2 + h}{h} = \lim_{h \to 0} (2x + h + 1) = 2x + 1$$

---

## 2.3 Reglas de Diferenciación

### Solución 2.3.3
**Contexto:** Regla del cociente: $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$

**Desarrollo:**
$$h'(x) = \frac{(2x)(x^2-1) - (x^2+1)(2x)}{(x^2-1)^2}$$
$$= \frac{2x^3 - 2x - 2x^3 - 2x}{(x^2-1)^2} = \frac{-4x}{(x^2-1)^2}$$

---

## 2.4 Regla de la Cadena

### Solución 2.4.4
**Contexto:** $f(x) = (x^2+1)^{1/2}$, aplicar cadena.

**Desarrollo:**
$$f'(x) = \frac{1}{2}(x^2+1)^{-1/2} \cdot 2x = \frac{x}{\sqrt{x^2+1}}$$

### Solución 2.4.10
**Contexto:** Esta es la [derivada](../../../glossary.md#derivada) de $\ln(\sec x + \tan x)$.

**Desarrollo:**
$$f'(x) = \frac{1}{\sec x + \tan x} \cdot (\sec x \tan x + \sec^2 x)$$
$$= \frac{\sec x(\tan x + \sec x)}{\sec x + \tan x} = \sec x$$

**Verificación:** Esta es la [antiderivada](../../../glossary.md#antiderivada) clásica de $\sec x$.

---

## 2.5 Derivación Implícita

### Solución 2.5.3
**Contexto:** Derivar término por término, aplicando la regla del producto en $xy$.

**Desarrollo:**
$$\frac{d}{dx}[x^2 + xy + y^2] = \frac{d}{dx}[7]$$
$$2x + \left(y + x\frac{dy}{dx}\right) + 2y\frac{dy}{dx} = 0$$
$$2x + y + \frac{dy}{dx}(x + 2y) = 0$$
$$\frac{dy}{dx} = -\frac{2x + y}{x + 2y}$$

### Solución 2.5.6
**Contexto:** Esta es la folieta de Descartes.

**Desarrollo:**
$$3x^2 + 3y^2\frac{dy}{dx} = 6y + 6x\frac{dy}{dx}$$
$$3y^2\frac{dy}{dx} - 6x\frac{dy}{dx} = 6y - 3x^2$$
$$\frac{dy}{dx}(3y^2 - 6x) = 6y - 3x^2$$
$$\frac{dy}{dx} = \frac{6y - 3x^2}{3y^2 - 6x}$$

En $(3, 3)$:
$$\frac{dy}{dx} = \frac{6(3) - 3(9)}{3(9) - 6(3)} = \frac{18 - 27}{27 - 18} = \frac{-9}{9} = -1$$

---

## 2.6 Derivadas de Orden Superior

### Solución 2.6.5
**Contexto:** Buscar patrón en [derivadas](../../../glossary.md#derivadas) sucesivas.

**Desarrollo:**
$f(x) = e^{ax}$
$f'(x) = ae^{ax}$
$f''(x) = a^2 e^{ax}$
$f'''(x) = a^3 e^{ax}$

**Fórmula general:** $f^{(n)}(x) = a^n e^{ax}$

### Solución 2.6.6
**Contexto:** Derivar implícitamente dos veces.

**Desarrollo:**
Primera [derivada](../../../glossary.md#derivada): $2x + 2y\frac{dy}{dx} = 0$ → $\frac{dy}{dx} = -\frac{x}{y}$

Segunda derivada:
$$\frac{d^2y}{dx^2} = -\frac{y - x\frac{dy}{dx}}{y^2} = -\frac{y - x(-\frac{x}{y})}{y^2} = -\frac{y + \frac{x^2}{y}}{y^2}$$
$$= -\frac{y^2 + x^2}{y^3} = -\frac{1}{y^3}$$ (usando $x^2 + y^2 = 1$)

---

## 2.8 Derivación Logarítmica

### Solución 2.8.1
**Contexto:** Para $y = x^x$, tomar logaritmo.

**Desarrollo:**
$\ln y = x \ln x$

Derivando:
$$\frac{1}{y}\frac{dy}{dx} = \ln x + x \cdot \frac{1}{x} = \ln x + 1$$
$$\frac{dy}{dx} = y(\ln x + 1) = x^x(\ln x + 1)$$

---

## Problemas de Síntesis

### Solución 2.S.1
**Contexto:** [Tangente](../../../glossary.md#tangente) horizontal significa $f'(x) = 0$.

**Desarrollo:**
$f'(x) = 3x^2 - 3 = 0$
$3(x^2 - 1) = 0$
$x = \pm 1$

**Puntos:** $(1, -2)$ y $(-1, 2)$

### Solución 2.S.4
**Contexto:** La suma $\arcsin x + \arccos x$ es constante.

**Desarrollo:**
$$\frac{d}{dx}[\arcsin x] = \frac{1}{\sqrt{1-x^2}}$$
$$\frac{d}{dx}[\arccos x] = -\frac{1}{\sqrt{1-x^2}}$$
$$\frac{d}{dx}[\arcsin x + \arccos x] = \frac{1}{\sqrt{1-x^2}} - \frac{1}{\sqrt{1-x^2}} = 0$$

**Interpretación:** $\arcsin x + \arccos x = \frac{\pi}{2}$ para todo $x \in [-1, 1]$.

Geométricamente: si $\theta = \arcsin x$, entonces $\arccos x = \frac{\pi}{2} - \theta$ (ángulos complementarios).
