<!--
::METADATA::
type: method
status: active
-->

# Métodos: EDO de Primer Orden

> **Referencia rápida:** Esta guía presenta 10 métodos sistemáticos para resolver [ecuaciones diferenciales](../../../glossary.md#ecuaciones-diferenciales) ordinarias de primer [orden](../../../glossary.md#orden).

---

## Índice de Métodos

| # | Método | Forma de Ecuación | Complejidad |
|---|--------|-------------------|-------------|
| 1 | [Variables Separables](#método-1-resolver-ecuación-separable) | $\frac{dy}{dx} = g(x)h(y)$ | ⭐ |
| 2 | [Ecuación Lineal](#método-2-resolver-ecuación-lineal) | $y' + P(x)y = Q(x)$ | ⭐⭐ |
| 3 | [Ecuación Exacta](#método-3-resolver-ecuación-exacta) | $M\,dx + N\,dy = 0$, $M_y = N_x$ | ⭐⭐ |
| 4 | [Factor Integrante](#método-4-factor-integrante-para-no-exactas) | $M\,dx + N\,dy = 0$ | ⭐⭐⭐ |
| 5 | [Bernoulli](#método-5-resolver-ecuación-de-bernoulli) | $y' + P(x)y = Q(x)y^n$ | ⭐⭐⭐ |
| 6 | [Homogénea](#método-6-resolver-ecuación-homogénea) | $y' = F(y/x)$ | ⭐⭐ |
| 7 | [Reducción a Separable](#método-7-[sustitución](../../../glossary.md#sustitucion)-especial) | $y' = f(ax + by + c)$ | ⭐⭐ |
| 8 | [Ricatti](#método-8-ecuación-de-ricatti) | $y' = P(x) + Q(x)y + R(x)y^2$ | ⭐⭐⭐⭐ |
| 9 | [Identificación de Tipo](#método-9-identificar-tipo-de-ecuación) | General | ⭐ |
| 10 | [Resolver PVI](#método-10-resolver-problema-de-valor-inicial) | Con condición inicial | ⭐ |

---

## Método 1: Resolver Ecuación Separable

### Cuándo Usar

- La ecuación se puede escribir como $\frac{dy}{dx} = g(x) \cdot h(y)$
- Las variables pueden separarse completamente

### Fórmula

$$\frac{dy}{dx} = g(x)h(y) \implies \int \frac{dy}{h(y)} = \int g(x)\,dx + C$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Separar** | Llevar todos los términos con $y$ a un lado y con $x$ al otro |
| 2 | **Verificar** | Confirmar que $h(y) \neq 0$ en el dominio |
| 3 | **Integrar** | Integrar ambos lados independientemente |
| 4 | **Despejar** | Obtener $y$ explícitamente si es posible |
| 5 | **Añadir constante** | Incluir una única constante de integración $C$ |

### Ejemplo Detallado

**Problema:** Resolver $\frac{dy}{dx} = \frac{x^2}{1 + y^2}$, $y(0) = 1$

---

**Paso 1: Separar variables**

$$\frac{dy}{dx} = \frac{x^2}{1 + y^2}$$

$$(1 + y^2)\,dy = x^2\,dx$$

---

**Paso 2: Integrar ambos lados**

$$\int (1 + y^2)\,dy = \int x^2\,dx$$

$$y + \frac{y^3}{3} = \frac{x^3}{3} + C$$

---

**Paso 3: Aplicar condición inicial** $y(0) = 1$

$$1 + \frac{1^3}{3} = \frac{0^3}{3} + C$$

$$1 + \frac{1}{3} = C \implies C = \frac{4}{3}$$

---

**Paso 4: Escribir [solución particular](../../../glossary.md#solucion-particular)**

$$y + \frac{y^3}{3} = \frac{x^3}{3} + \frac{4}{3}$$

Multiplicando por 3:

$$\boxed{3y + y^3 = x^3 + 4}$$

---

**Verificación:** En $x = 0$: $3(1) + 1 = 0 + 4 \implies 4 = 4$ ✓

---

## Método 2: Resolver Ecuación Lineal

### Cuándo Usar

- Forma estándar: $\frac{dy}{dx} + P(x)y = Q(x)$
- $y$ aparece solo en primera potencia

### Fórmula

**[Factor integrante](../../../glossary.md#factor-integrante):** $\mu(x) = e^{\int P(x)\,dx}$

**Solución:**
$$y = \frac{1}{\mu(x)}\left[\int \mu(x) Q(x)\,dx + C\right]$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Forma estándar** | Escribir como $y' + P(x)y = Q(x)$ |
| 2 | **Identificar** | Determinar $P(x)$ y $Q(x)$ |
| 3 | **Factor integrante** | Calcular $\mu = e^{\int P\,dx}$ |
| 4 | **Multiplicar** | Multiplicar toda la ecuación por $\mu$ |
| 5 | **Reconocer derivada** | El lado izquierdo es $\frac{d}{dx}(\mu y)$ |
| 6 | **Integrar** | $\mu y = \int \mu Q\,dx + C$ |
| 7 | **Despejar** | $y = \frac{1}{\mu}\left[\int \mu Q\,dx + C\right]$ |

### Ejemplo Detallado

**Problema:** Resolver $xy' - 2y = x^4$

---

**Paso 1: Forma estándar** (dividir por $x$)

$$y' - \frac{2}{x}y = x^3$$

---

**Paso 2: Identificar**

$$P(x) = -\frac{2}{x}, \quad Q(x) = x^3$$

---

**Paso 3: [Factor integrante](../../../glossary.md#factor-integrante)**

$$\mu = e^{\int -\frac{2}{x}dx} = e^{-2\ln|x|} = e^{\ln|x|^{-2}} = x^{-2} = \frac{1}{x^2}$$

---

**Paso 4: Multiplicar por** $\mu = \frac{1}{x^2}$

$$\frac{1}{x^2}y' - \frac{2}{x^3}y = x$$

---

**Paso 5: Reconocer [derivada](../../../glossary.md#derivada)**

$$\frac{d}{dx}\left(\frac{y}{x^2}\right) = x$$

---

**Paso 6: Integrar**

$$\frac{y}{x^2} = \int x\,dx = \frac{x^2}{2} + C$$

---

**Paso 7: Despejar $y$**

$$y = x^2\left(\frac{x^2}{2} + C\right)$$

$$\boxed{y = \frac{x^4}{2} + Cx^2}$$

---

**Verificación:** $y' = 2x^3 + 2Cx$

$xy' - 2y = x(2x^3 + 2Cx) - 2\left(\frac{x^4}{2} + Cx^2\right) = 2x^4 + 2Cx^2 - x^4 - 2Cx^2 = x^4$ ✓

---

## Método 3: Resolver Ecuación Exacta

### Cuándo Usar

- Forma: $M(x,y)\,dx + N(x,y)\,dy = 0$
- Condición de exactitud: $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$

### Fórmula

Si es exacta, existe $F(x,y)$ [tal que](../../../glossary.md#tal-que):
$$\frac{\partial F}{\partial x} = M, \quad \frac{\partial F}{\partial y} = N$$

**Solución:** $F(x,y) = C$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Identificar** | Determinar $M(x,y)$ y $N(x,y)$ |
| 2 | **Verificar exactitud** | Comprobar $M_y = N_x$ |
| 3 | **Integrar $M$** | $F = \int M\,dx + g(y)$ |
| 4 | **Derivar** | $\frac{\partial F}{\partial y} = \frac{\partial}{\partial y}\int M\,dx + g'(y)$ |
| 5 | **Igualar a $N$** | Despejar $g'(y)$ |
| 6 | **Integrar $g'(y)$** | Obtener $g(y)$ |
| 7 | **Escribir solución** | $F(x,y) = C$ |

### Ejemplo Detallado

**Problema:** Resolver $(3x^2 + y\cos x)\,dx + (\sin x - 4y^3)\,dy = 0$

---

**Paso 1: Identificar**

$$M = 3x^2 + y\cos x, \quad N = \sin x - 4y^3$$

---

**Paso 2: Verificar exactitud**

$$M_y = \frac{\partial}{\partial y}(3x^2 + y\cos x) = \cos x$$

$$N_x = \frac{\partial}{\partial x}(\sin x - 4y^3) = \cos x$$

$M_y = N_x$ ✓ **Es exacta**

---

**Paso 3: Integrar $M$ respecto a $x$**

$$F = \int (3x^2 + y\cos x)\,dx = x^3 + y\sin x + g(y)$$

---

**Paso 4: Derivar $F$ respecto a $y$**

$$\frac{\partial F}{\partial y} = \sin x + g'(y)$$

---

**Paso 5: Igualar a $N$**

$$\sin x + g'(y) = \sin x - 4y^3$$

$$g'(y) = -4y^3$$

---

**Paso 6: Integrar para obtener $g(y)$**

$$g(y) = \int -4y^3\,dy = -y^4$$

---

**Paso 7: Escribir solución**

$$F(x,y) = x^3 + y\sin x - y^4 = C$$

$$\boxed{x^3 + y\sin x - y^4 = C}$$

---

## Método 4: Factor Integrante para No Exactas

### Cuándo Usar

- La ecuación $M\,dx + N\,dy = 0$ NO es exacta ($M_y \neq N_x$)
- Se puede encontrar $\mu(x)$ o $\mu(y)$ para hacerla exacta

### Fórmulas para Factor Integrante

**Caso 1:** Si $\frac{M_y - N_x}{N}$ depende solo de $x$:
$$\mu(x) = e^{\int \frac{M_y - N_x}{N}dx}$$

**Caso 2:** Si $\frac{N_x - M_y}{M}$ depende solo de $y$:
$$\mu(y) = e^{\int \frac{N_x - M_y}{M}dy}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Calcular** | $M_y$, $N_x$, y $M_y - N_x$ |
| 2 | **Intentar** $\mu(x)$ | Ver si $\frac{M_y - N_x}{N}$ solo depende de $x$ |
| 3 | **Si no, intentar** $\mu(y)$ | Ver si $\frac{N_x - M_y}{M}$ solo depende de $y$ |
| 4 | **Calcular** $\mu$ | Integrar la expresión encontrada |
| 5 | **Multiplicar** | Nueva ecuación: $\mu M\,dx + \mu N\,dy = 0$ |
| 6 | **Resolver** | Aplicar método de ecuación exacta |

### Ejemplo Detallado

**Problema:** Resolver $(xy + 1)\,dx + x(x + 4y - 2)\,dy = 0$

---

**Paso 1: Calcular [derivadas](../../../glossary.md#derivadas) parciales**

$$M = xy + 1, \quad N = x^2 + 4xy - 2x$$

$$M_y = x, \quad N_x = 2x + 4y - 2$$

$$M_y - N_x = x - (2x + 4y - 2) = -x - 4y + 2$$

No es exacta.

---

**Paso 2: Intentar** $\mu(x)$

$$\frac{M_y - N_x}{N} = \frac{-x - 4y + 2}{x^2 + 4xy - 2x} = \frac{-x - 4y + 2}{x(x + 4y - 2)}$$

Factorizando: $\frac{-(x + 4y - 2)}{x(x + 4y - 2)} = -\frac{1}{x}$

¡Solo depende de $x$! ✓

---

**Paso 3: Calcular factor integrante**

$$\mu(x) = e^{\int -\frac{1}{x}dx} = e^{-\ln|x|} = \frac{1}{x}$$

---

**Paso 4: Multiplicar ecuación por** $\mu = \frac{1}{x}$

$$\frac{xy + 1}{x}\,dx + \frac{x^2 + 4xy - 2x}{x}\,dy = 0$$

$$\left(y + \frac{1}{x}\right)dx + (x + 4y - 2)\,dy = 0$$

---

**Paso 5: Verificar que ahora es exacta**

$$M^* = y + \frac{1}{x}, \quad N^* = x + 4y - 2$$

$$M^*_y = 1, \quad N^*_x = 1$$ ✓

---

**Paso 6: Resolver como exacta**

$$F = \int \left(y + \frac{1}{x}\right)dx = xy + \ln|x| + g(y)$$

$$\frac{\partial F}{\partial y} = x + g'(y) = x + 4y - 2$$

$$g'(y) = 4y - 2 \implies g(y) = 2y^2 - 2y$$

$$\boxed{xy + \ln|x| + 2y^2 - 2y = C}$$

---

## Método 5: Resolver Ecuación de Bernoulli

### Cuándo Usar

- Forma: $\frac{dy}{dx} + P(x)y = Q(x)y^n$ donde $n \neq 0, 1$
- Se transforma en lineal mediante [sustitución](../../../glossary.md#sustitucion)

### Fórmula

**Sustitución:** $v = y^{1-n}$

**Ecuación transformada:** $\frac{dv}{dx} + (1-n)P(x)v = (1-n)Q(x)$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Identificar** | Determinar $n$, $P(x)$, $Q(x)$ |
| 2 | **Dividir** | Por $y^n$: $y^{-n}y' + Py^{1-n} = Q$ |
| 3 | **Sustituir** | $v = y^{1-n}$, $v' = (1-n)y^{-n}y'$ |
| 4 | **Transformar** | $\frac{v'}{1-n} + Pv = Q$ |
| 5 | **Resolver lineal** | Ecuación en $v$ |
| 6 | **Regresar** | $y = v^{\frac{1}{1-n}}$ |

### Ejemplo Detallado

**Problema:** Resolver $y' - \frac{y}{x} = -\frac{y^3}{x^2}$

---

**Paso 1: Identificar**

Forma: $y' + \left(-\frac{1}{x}\right)y = \left(-\frac{1}{x^2}\right)y^3$

$$n = 3, \quad P(x) = -\frac{1}{x}, \quad Q(x) = -\frac{1}{x^2}$$

---

**Paso 2: Dividir por $y^3$**

$$y^{-3}y' - \frac{y^{-2}}{x} = -\frac{1}{x^2}$$

---

**Paso 3: Sustituir** $v = y^{1-3} = y^{-2}$

$$\frac{dv}{dx} = -2y^{-3}\frac{dy}{dx} \implies y^{-3}y' = -\frac{1}{2}\frac{dv}{dx}$$

---

**Paso 4: Transformar a ecuación lineal**

$$-\frac{1}{2}\frac{dv}{dx} - \frac{v}{x} = -\frac{1}{x^2}$$

Multiplicar por $-2$:

$$\frac{dv}{dx} + \frac{2v}{x} = \frac{2}{x^2}$$

---

**Paso 5: Resolver ecuación lineal**

Factor integrante: $\mu = e^{\int \frac{2}{x}dx} = e^{2\ln|x|} = x^2$

$$x^2\frac{dv}{dx} + 2xv = 2$$

$$\frac{d}{dx}(x^2 v) = 2$$

$$x^2 v = 2x + C$$

$$v = \frac{2}{x} + \frac{C}{x^2}$$

---

**Paso 6: Regresar a $y$**

$$y^{-2} = \frac{2}{x} + \frac{C}{x^2} = \frac{2x + C}{x^2}$$

$$y^2 = \frac{x^2}{2x + C}$$

$$\boxed{y = \pm\sqrt{\frac{x^2}{2x + C}} = \pm\frac{x}{\sqrt{2x + C}}}$$

---

## Método 6: Resolver Ecuación Homogénea

### Cuándo Usar

- La [función](../../../glossary.md#funcion) $f(x,y)$ cumple $f(tx, ty) = f(x,y)$ (grado 0)
- Equivalente: $\frac{dy}{dx} = F\left(\frac{y}{x}\right)$

### Fórmula

**Sustitución:** $y = vx$ donde $v = \frac{y}{x}$

**[Derivada](../../../glossary.md#derivada):** $\frac{dy}{dx} = v + x\frac{dv}{dx}$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Verificar** | Comprobar que $f(tx,ty) = f(x,y)$ |
| 2 | **Reescribir** | Expresar como $\frac{dy}{dx} = F\left(\frac{y}{x}\right)$ |
| 3 | **Sustituir** | $y = vx$, $y' = v + xv'$ |
| 4 | **Simplificar** | $v + xv' = F(v)$ |
| 5 | **Separar** | $\frac{dv}{F(v) - v} = \frac{dx}{x}$ |
| 6 | **Integrar** | Ambos lados |
| 7 | **Regresar** | Sustituir $v = \frac{y}{x}$ |

### Ejemplo Detallado

**Problema:** Resolver $(x^2 + y^2)\,dx - 2xy\,dy = 0$

---

**Paso 1: Reescribir como** $y' = f(x,y)$

$$\frac{dy}{dx} = \frac{x^2 + y^2}{2xy}$$

---

**Paso 2: Verificar homogeneidad**

$$f(tx, ty) = \frac{t^2x^2 + t^2y^2}{2(tx)(ty)} = \frac{t^2(x^2 + y^2)}{2t^2xy} = \frac{x^2 + y^2}{2xy} = f(x,y)$$ ✓

---

**Paso 3: Reescribir en términos de** $v = \frac{y}{x}$

$$\frac{dy}{dx} = \frac{x^2 + y^2}{2xy} = \frac{1 + (y/x)^2}{2(y/x)} = \frac{1 + v^2}{2v}$$

---

**Paso 4: Sustituir** $y = vx$

$$v + x\frac{dv}{dx} = \frac{1 + v^2}{2v}$$

$$x\frac{dv}{dx} = \frac{1 + v^2}{2v} - v = \frac{1 + v^2 - 2v^2}{2v} = \frac{1 - v^2}{2v}$$

---

**Paso 5: Separar variables**

$$\frac{2v\,dv}{1 - v^2} = \frac{dx}{x}$$

---

**Paso 6: Integrar**

$$-\int \frac{-2v\,dv}{1 - v^2} = \int \frac{dx}{x}$$

$$-\ln|1 - v^2| = \ln|x| + C_1$$

$$\ln|1 - v^2| = -\ln|x| - C_1 = \ln\left|\frac{1}{x}\right| + C_2$$

$$1 - v^2 = \frac{C}{x}$$

---

**Paso 7: Regresar a** $y$

$$1 - \frac{y^2}{x^2} = \frac{C}{x}$$

$$x^2 - y^2 = Cx$$

$$\boxed{x^2 - y^2 = Cx}$$

---

## Método 7: Sustitución Especial

### Cuándo Usar

- Forma: $\frac{dy}{dx} = f(ax + by + c)$
- Sustitución convierte en separable

### Fórmula

**Sustitución:** $u = ax + by + c$

**Derivada:** $\frac{du}{dx} = a + b\frac{dy}{dx}$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Identificar** | $a$, $b$, $c$ en $ax + by + c$ |
| 2 | **Sustituir** | $u = ax + by + c$ |
| 3 | **Derivar** | $u' = a + by'$ |
| 4 | **Despejar** $y'$ | $y' = \frac{u' - a}{b}$ |
| 5 | **Reemplazar** | $\frac{u' - a}{b} = f(u)$ |
| 6 | **Separar y resolver** | Ecuación en $u$ |
| 7 | **Regresar** | $u = ax + by + c$ |

### Ejemplo Detallado

**Problema:** Resolver $y' = (x + y + 1)^2$

---

**Paso 1: Identificar**

$$a = 1, \quad b = 1, \quad c = 1$$

---

**Paso 2: Sustituir** $u = x + y + 1$

---

**Paso 3: Derivar**

$$\frac{du}{dx} = 1 + \frac{dy}{dx}$$

$$\frac{dy}{dx} = \frac{du}{dx} - 1$$

---

**Paso 4: Reemplazar en la ecuación**

$$\frac{du}{dx} - 1 = u^2$$

$$\frac{du}{dx} = u^2 + 1$$

---

**Paso 5: Separar variables**

$$\frac{du}{u^2 + 1} = dx$$

---

**Paso 6: Integrar**

$$\arctan(u) = x + C$$

$$u = \tan(x + C)$$

---

**Paso 7: Regresar a** $y$

$$x + y + 1 = \tan(x + C)$$

$$\boxed{y = \tan(x + C) - x - 1}$$

---

**Verificación:**

$y' = \sec^2(x + C) - 1 = \tan^2(x + C) = (x + y + 1)^2$ ✓

---

## Método 8: Ecuación de Ricatti

### Cuándo Usar

- Forma: $\frac{dy}{dx} = P(x) + Q(x)y + R(x)y^2$
- Se conoce una [solución particular](../../../glossary.md#solucion-particular) $y_1(x)$

### Fórmula

**Sustitución:** $y = y_1 + \frac{1}{v}$

**Ecuación transformada:** $\frac{dv}{dx} + [Q(x) + 2R(x)y_1]v = -R(x)$ (lineal en $v$)

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Identificar** | $P$, $Q$, $R$ y solución particular $y_1$ |
| 2 | **Verificar** | Comprobar que $y_1$ satisface la ecuación |
| 3 | **Sustituir** | $y = y_1 + \frac{1}{v}$ |
| 4 | **Derivar** | $y' = y_1' - \frac{v'}{v^2}$ |
| 5 | **Reemplazar** | Sustituir en la ecuación original |
| 6 | **Simplificar** | Obtener ecuación lineal en $v$ |
| 7 | **Resolver** | Aplicar método de ecuación lineal |
| 8 | **Regresar** | $y = y_1 + \frac{1}{v}$ |

### Ejemplo Detallado

**Problema:** Resolver $y' = 1 + x^2 - 2xy + y^2$, sabiendo que $y_1 = x$ es solución

---

**Paso 1: Identificar**

$$P(x) = 1 + x^2, \quad Q(x) = -2x, \quad R(x) = 1$$

---

**Paso 2: Verificar que** $y_1 = x$ **es solución**

$y_1' = 1$

$1 + x^2 - 2x(x) + x^2 = 1 + x^2 - 2x^2 + x^2 = 1$ ✓

---

**Paso 3: Sustituir** $y = x + \frac{1}{v}$

$$y' = 1 - \frac{v'}{v^2}$$

---

**Paso 4: Reemplazar en la ecuación**

$$1 - \frac{v'}{v^2} = 1 + x^2 - 2x\left(x + \frac{1}{v}\right) + \left(x + \frac{1}{v}\right)^2$$

$$1 - \frac{v'}{v^2} = 1 + x^2 - 2x^2 - \frac{2x}{v} + x^2 + \frac{2x}{v} + \frac{1}{v^2}$$

$$1 - \frac{v'}{v^2} = 1 + \frac{1}{v^2}$$

---

**Paso 5: Simplificar**

$$-\frac{v'}{v^2} = \frac{1}{v^2}$$

$$v' = -1$$

---

**Paso 6: Integrar**

$$v = -x + C$$

---

**Paso 7: Escribir solución**

$$y = x + \frac{1}{-x + C} = x - \frac{1}{x - C}$$

$$\boxed{y = x - \frac{1}{x - C} = \frac{x^2 - Cx - 1}{x - C}}$$

---

## Método 9: Identificar Tipo de Ecuación

### Diagrama de Decisión

```
┌─────────────────────────────────────────────────────────────┐
│                    ¿Qué forma tiene?                        │
└─────────────────────────────────────────────────────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ y' = g(x)·h(y)  │  │ y' + P(x)y = Q  │  │ M dx + N dy = 0 │
│   SEPARABLE     │  │    LINEAL       │  │                 │
└─────────────────┘  └─────────────────┘  └────────┬────────┘
                                                   │
                              ┌─────────────────────┴─────────┐
                              ▼                               ▼
                     ┌─────────────┐               ┌─────────────────┐
                     │ ¿M_y = N_x? │               │ ¿M_y ≠ N_x?     │
                     │   EXACTA    │               │ FACTOR INTEG.   │
                     └─────────────┘               └─────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                   Casos especiales                          │
└─────────────────────────────────────────────────────────────┘
                              │
    ┌─────────────┬───────────┴───────────┬─────────────┐
    ▼             ▼                       ▼             ▼
┌─────────┐ ┌───────────┐         ┌───────────┐ ┌───────────┐
│y'+Py=Qy^n│ │y'=F(y/x) │         │y'=f(ax+by)│ │y'=P+Qy+Ry²│
│BERNOULLI │ │HOMOGÉNEA │         │SUSTITUCIÓN│ │  RICATTI  │
└─────────┘ └───────────┘         └───────────┘ └───────────┘
```

### Tabla Resumen

| Tipo | Identificación | Método |
|------|----------------|--------|
| Separable | $y' = g(x)h(y)$ | Separar e integrar |
| Lineal | $y' + P(x)y = Q(x)$ | Factor integrante $e^{\int P\,dx}$ |
| Exacta | $M_y = N_x$ | Buscar $F$ [tal que](../../../glossary.md#tal-que) $F_x = M$, $F_y = N$ |
| No exacta | $M_y \neq N_x$ | Buscar factor integrante $\mu(x)$ o $\mu(y)$ |
| Bernoulli | $y' + Py = Qy^n$ | Sustitución $v = y^{1-n}$ |
| Homogénea | $f(tx,ty) = f(x,y)$ | Sustitución $y = vx$ |
| Sustitución | $y' = f(ax+by+c)$ | Sustitución $u = ax + by + c$ |
| Ricatti | $y' = P + Qy + Ry^2$ | Conocer $y_1$, usar $y = y_1 + 1/v$ |

---

## Método 10: Resolver Problema de Valor Inicial

### Cuándo Usar

- Se tiene [EDO](../../../glossary.md#edo) junto con condición inicial $y(x_0) = y_0$
- Se busca solución particular única

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Identificar tipo** | Clasificar la EDO |
| 2 | **Resolver** | Obtener solución general con $C$ |
| 3 | **Aplicar CI** | Sustituir $(x_0, y_0)$ |
| 4 | **Despejar** $C$ | Encontrar valor de la constante |
| 5 | **Escribir** | Solución particular |
| 6 | **Verificar** | Comprobar en ecuación y CI |

### Ejemplo Detallado

**Problema:** Resolver $y' + 2xy = 2xe^{-x^2}$, $y(0) = 3$

---

**Paso 1: Identificar tipo**

Ecuación lineal: $P(x) = 2x$, $Q(x) = 2xe^{-x^2}$

---

**Paso 2: Resolver ecuación lineal**

Factor integrante:
$$\mu = e^{\int 2x\,dx} = e^{x^2}$$

Multiplicar:
$$e^{x^2}y' + 2xe^{x^2}y = 2x$$

$$\frac{d}{dx}(e^{x^2}y) = 2x$$

Integrar:
$$e^{x^2}y = x^2 + C$$

$$y = (x^2 + C)e^{-x^2}$$

---

**Paso 3: Aplicar condición inicial** $y(0) = 3$

$$3 = (0 + C)e^0 = C$$

$$C = 3$$

---

**Paso 4: Escribir solución particular**

$$\boxed{y = (x^2 + 3)e^{-x^2}}$$

---

**Paso 5: Verificación**

$y' = 2xe^{-x^2} + (x^2 + 3)(-2x)e^{-x^2} = 2xe^{-x^2} - 2x(x^2 + 3)e^{-x^2}$

$y' = e^{-x^2}[2x - 2x^3 - 6x] = e^{-x^2}[-2x^3 - 4x]$

$y' + 2xy = e^{-x^2}[-2x^3 - 4x] + 2x(x^2 + 3)e^{-x^2}$
$= e^{-x^2}[-2x^3 - 4x + 2x^3 + 6x] = 2xe^{-x^2}$ ✓

$y(0) = (0 + 3)e^0 = 3$ ✓

---

## Tabla Resumen de Fórmulas

| Tipo | Forma | Solución/Técnica |
|------|-------|------------------|
| **Separable** | $y' = g(x)h(y)$ | $\int \frac{dy}{h(y)} = \int g(x)\,dx + C$ |
| **Lineal** | $y' + Py = Q$ | $y = \frac{1}{\mu}\left[\int \mu Q\,dx + C\right]$, $\mu = e^{\int P\,dx}$ |
| **Exacta** | $M\,dx + N\,dy = 0$ | Encontrar $F$ con $F_x = M$, $F_y = N$; sol: $F = C$ |
| **Bernoulli** | $y' + Py = Qy^n$ | Sustituir $v = y^{1-n}$ → lineal |
| **Homogénea** | $y' = F(y/x)$ | Sustituir $y = vx$ → separable |
| **Ricatti** | $y' = P + Qy + Ry^2$ | Con $y_1$ conocida: $y = y_1 + 1/v$ → lineal |

---

## Errores Comunes a Evitar

| Error | Consecuencia | Prevención |
|-------|--------------|------------|
| Olvidar constante $C$ | Solución incompleta | Siempre añadir $+C$ al integrar |
| No verificar $h(y) \neq 0$ | Pérdida de soluciones singulares | Analizar casos donde $h(y) = 0$ |
| Error en forma estándar | Factor integrante incorrecto | Dividir toda la ecuación correctamente |
| Confundir $M_y$ con $N_x$ | Clasificación errónea | $M$ va con $dx$, $N$ va con $dy$ |
| Olvidar verificar exactitud | Aplicar método incorrecto | Siempre calcular $M_y - N_x$ |
| Error en sustitución Bernoulli | Ecuación mal transformada | $v = y^{1-n}$, no $y^{n-1}$ |

---

## Problemas de Práctica Sugeridos

1. **Separable:** $y' = \frac{y(1-y)}{x}$
2. **Lineal:** $y' + \frac{y}{x} = \sin x$
3. **Exacta:** $(2x + 3y)\,dx + (3x + 4y)\,dy = 0$
4. **Factor integrante:** $y\,dx + (2x - ye^y)\,dy = 0$
5. **Bernoulli:** $y' + y = y^2 e^x$
6. **Homogénea:** $(x^2 + xy)\,dx - x^2\,dy = 0$
7. **Ricatti:** $y' = y^2 - xy + 1$, $y_1 = x$

---

*Documento actualizado con formato expandido para estudio detallado.*
