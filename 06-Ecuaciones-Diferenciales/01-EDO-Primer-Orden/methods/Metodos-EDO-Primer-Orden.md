<!--
content_type: methods
topic: EDO de Primer Orden
---
-->

# Métodos: EDO de Primer Orden

---

## Método 1: Resolver Ecuación Separable

**Objetivo:** Resolver $\frac{dy}{dx} = g(x)h(y)$

### Pasos

1. Separar variables: $\frac{dy}{h(y)} = g(x)dx$
2. Integrar ambos lados
3. Despejar $y$ si es posible
4. Aplicar condición inicial si hay PVI

### Ejemplo

$\frac{dy}{dx} = \frac{x}{y}$, $y(0) = 2$

**Paso 1:** $y\,dy = x\,dx$

**Paso 2:** $\frac{y^2}{2} = \frac{x^2}{2} + C$

**Paso 3:** $y^2 = x^2 + C_1$

**Paso 4:** $4 = 0 + C_1 \Rightarrow C_1 = 4$

**Solución:** $y = \sqrt{x^2 + 4}$ (tomamos raíz positiva por $y(0) = 2 > 0$)

---

## Método 2: Resolver Ecuación Lineal

**Objetivo:** Resolver $\frac{dy}{dx} + P(x)y = Q(x)$

### Pasos

1. Identificar $P(x)$ y $Q(x)$
2. Calcular factor integrante: $\mu = e^{\int P\,dx}$
3. Multiplicar toda la ecuación por $\mu$
4. Reconocer que el lado izquierdo es $\frac{d}{dx}(\mu y)$
5. Integrar: $\mu y = \int \mu Q\,dx + C$
6. Despejar $y$

### Ejemplo

$\frac{dy}{dx} - 3y = e^{2x}$

**Paso 1:** $P(x) = -3$, $Q(x) = e^{2x}$

**Paso 2:** $\mu = e^{\int -3dx} = e^{-3x}$

**Paso 3:** $e^{-3x}\frac{dy}{dx} - 3e^{-3x}y = e^{-x}$

**Paso 4:** $\frac{d}{dx}(e^{-3x}y) = e^{-x}$

**Paso 5:** $e^{-3x}y = -e^{-x} + C$

**Paso 6:** $y = -e^{2x} + Ce^{3x}$

---

## Método 3: Resolver Ecuación Exacta

**Objetivo:** Resolver $M(x,y)dx + N(x,y)dy = 0$

### Pasos

1. Verificar exactitud: $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$
2. Integrar $M$ respecto a $x$: $F = \int M\,dx + g(y)$
3. Derivar $F$ respecto a $y$: $\frac{\partial F}{\partial y} = ... + g'(y)$
4. Igualar a $N$ y despejar $g'(y)$
5. Integrar $g'(y)$ para obtener $g(y)$
6. Escribir solución: $F(x,y) = C$

### Ejemplo

$(2xy + 1)dx + (x^2 + 2y)dy = 0$

**Paso 1:** $M_y = 2x$, $N_x = 2x$ ✓

**Paso 2:** $F = \int (2xy + 1)dx = x^2y + x + g(y)$

**Paso 3:** $\frac{\partial F}{\partial y} = x^2 + g'(y)$

**Paso 4:** $x^2 + g'(y) = x^2 + 2y \Rightarrow g'(y) = 2y$

**Paso 5:** $g(y) = y^2$

**Paso 6:** $x^2y + x + y^2 = C$

---

## Método 4: Factor Integrante para No Exactas

**Objetivo:** Encontrar $\mu$ para hacer exacta $Mdx + Ndy = 0$

### Pasos

1. Calcular $M_y - N_x$
2. Intentar $\frac{M_y - N_x}{N}$. Si solo depende de $x$: $\mu(x) = e^{\int \frac{M_y - N_x}{N}dx}$
3. Si no, intentar $\frac{N_x - M_y}{M}$. Si solo depende de $y$: $\mu(y) = e^{\int \frac{N_x - M_y}{M}dy}$
4. Multiplicar ecuación por $\mu$ y resolver como exacta

### Ejemplo

$(y + 1)dx - xdy = 0$

$M = y + 1$, $N = -x$

$M_y = 1$, $N_x = -1$, $M_y - N_x = 2$

$\frac{M_y - N_x}{N} = \frac{2}{-x} = -\frac{2}{x}$ (depende solo de $x$) ✓

$\mu = e^{\int -\frac{2}{x}dx} = e^{-2\ln|x|} = x^{-2}$

Nueva ecuación: $\frac{y+1}{x^2}dx - \frac{1}{x}dy = 0$

Verificar: ahora es exacta y resolver.

---

## Método 5: Resolver Ecuación de Bernoulli

**Objetivo:** Resolver $\frac{dy}{dx} + P(x)y = Q(x)y^n$

### Pasos

1. Identificar $n$, $P(x)$, $Q(x)$
2. Dividir por $y^n$: $y^{-n}\frac{dy}{dx} + P(x)y^{1-n} = Q(x)$
3. Sustituir $v = y^{1-n}$, entonces $\frac{dv}{dx} = (1-n)y^{-n}\frac{dy}{dx}$
4. Reescribir: $\frac{1}{1-n}\frac{dv}{dx} + P(x)v = Q(x)$
5. Resolver ecuación lineal en $v$
6. Volver a $y$: $y = v^{\frac{1}{1-n}}$

### Ejemplo

$\frac{dy}{dx} + \frac{y}{x} = xy^2$

**Paso 1:** $n = 2$, $P = \frac{1}{x}$, $Q = x$

**Paso 2:** $y^{-2}\frac{dy}{dx} + \frac{1}{x}y^{-1} = x$

**Paso 3:** $v = y^{-1}$, $\frac{dv}{dx} = -y^{-2}\frac{dy}{dx}$

**Paso 4:** $-\frac{dv}{dx} + \frac{v}{x} = x \Rightarrow \frac{dv}{dx} - \frac{v}{x} = -x$

**Paso 5:** $\mu = e^{-\ln x} = \frac{1}{x}$

$\frac{v}{x} = -\int 1\,dx + C = -x + C$

$v = -x^2 + Cx$

**Paso 6:** $y = \frac{1}{v} = \frac{1}{Cx - x^2}$

---

## Método 6: Resolver Ecuación Homogénea

**Objetivo:** Resolver $\frac{dy}{dx} = F\left(\frac{y}{x}\right)$

### Pasos

1. Verificar que es homogénea (reescribir como función de $\frac{y}{x}$)
2. Sustituir $y = vx$ donde $v = \frac{y}{x}$
3. Calcular $\frac{dy}{dx} = v + x\frac{dv}{dx}$
4. Sustituir en la ecuación
5. Separar variables en $v$ y $x$
6. Integrar
7. Volver a $y = vx$

### Ejemplo

$\frac{dy}{dx} = \frac{y^2 + xy}{x^2}$

**Paso 1:** $\frac{dy}{dx} = \left(\frac{y}{x}\right)^2 + \frac{y}{x} = v^2 + v$

**Paso 2-3:** $y = vx$, $\frac{dy}{dx} = v + x\frac{dv}{dx}$

**Paso 4:** $v + x\frac{dv}{dx} = v^2 + v$

**Paso 5:** $x\frac{dv}{dx} = v^2$, $\frac{dv}{v^2} = \frac{dx}{x}$

**Paso 6:** $-\frac{1}{v} = \ln|x| + C$

**Paso 7:** $-\frac{x}{y} = \ln|x| + C$, entonces $y = \frac{-x}{\ln|x| + C}$

---

## Método 7: Identificar Tipo de Ecuación

**Objetivo:** Determinar qué método usar.

### Diagrama de Decisión

```
¿La ecuación tiene forma dy/dx = f(x,y)?
│
├─ ¿f(x,y) = g(x)·h(y)? ──────► SEPARABLE
│
├─ ¿Forma dy/dx + P(x)y = Q(x)? ──────► LINEAL
│
├─ ¿Forma dy/dx + P(x)y = Q(x)y^n? ──────► BERNOULLI
│
├─ ¿f(tx,ty) = f(x,y)? ──────► HOMOGÉNEA
│
└─ ¿Forma M dx + N dy = 0?
    │
    ├─ ¿M_y = N_x? ──────► EXACTA
    │
    └─ ¿Existe μ(x) o μ(y)? ──────► FACTOR INTEGRANTE
```

---

## Método 8: Resolver PVI

**Objetivo:** Resolver $\frac{dy}{dx} = f(x,y)$, $y(x_0) = y_0$

### Pasos

1. Resolver la EDO obteniendo solución general con constante $C$
2. Sustituir la condición inicial: $y(x_0) = y_0$
3. Despejar $C$
4. Escribir la solución particular

### Ejemplo

$\frac{dy}{dx} = 2xy$, $y(0) = 3$

**Paso 1:** Separable: $\frac{dy}{y} = 2x\,dx$

$\ln|y| = x^2 + C_1$

$y = Ce^{x^2}$

**Paso 2:** $y(0) = Ce^0 = C = 3$

**Paso 3:** $C = 3$

**Paso 4:** $y = 3e^{x^2}$
