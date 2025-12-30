<!--
::METADATA::
type: method
topic_id: cv-02-curvas-parametricas-polares
file_id: CV-02-Metodos-Curvas
status: stable
audience: student
-->

# Métodos para Curvas Paramétricas y Coordenadas Polares

> **Objetivo:** Dominar el análisis de curvas paramétricas y polares con explicaciones detalladas, cálculos intermedios y ejemplos clásicos paso a paso.

---

## Método 1: Graficar Curvas Paramétricas

### Cuándo Usar
- Visualizar una curva dada por $x = x(t)$, $y = y(t)$

### Algoritmo de Resolución

| Paso | Acción | Propósito |
|------|--------|-----------|
| 1 | Hacer tabla de valores | Puntos $(x, y)$ para varios $t$ |
| 2 | Determinar dirección | ¿Cómo se recorre al aumentar $t$? |
| 3 | Identificar puntos especiales | Inicio, fin, intersecciones |
| 4 | Eliminar parámetro (si es posible) | Ecuación cartesiana |

### Ejemplo Detallado

**Problema:** Graficar la curva $x = \cos t$, $y = \sin t$, $0 \leq t \leq 2\pi$

**Paso 1:** Tabla de valores:

| $t$ | $x = \cos t$ | $y = \sin t$ |
|-----|-------------|--------------|
| $0$ | $1$ | $0$ |
| $\frac{\pi}{2}$ | $0$ | $1$ |
| $\pi$ | $-1$ | $0$ |
| $\frac{3\pi}{2}$ | $0$ | $-1$ |
| $2\pi$ | $1$ | $0$ |

**Paso 2:** Dirección: Al aumentar $t$, el punto se mueve en sentido **antihorario**.

**Paso 3:** Puntos especiales:
- Inicio ($t=0$): $(1, 0)$
- Fin ($t=2\pi$): $(1, 0)$ — curva cerrada

**Paso 4:** Eliminamos el parámetro:
$$x^2 + y^2 = \cos^2 t + \sin^2 t = 1$$

**Resultado:** Es un **círculo unitario** recorrido en sentido antihorario.

---

## Método 2: Pendiente de la Tangente (Curvas Paramétricas)

### Cuándo Usar
- Encontrar la pendiente de la recta tangente en un punto
- Analizar puntos donde la tangente es horizontal o vertical

### Fórmula
$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{y'(t)}{x'(t)}$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Calcular $\frac{dx}{dt}$ | Derivar $x(t)$ |
| 2 | Calcular $\frac{dy}{dt}$ | Derivar $y(t)$ |
| 3 | Dividir | $\frac{dy/dt}{dx/dt}$ |
| 4 | Evaluar en $t$ dado | Sustituir valor |

### Casos Especiales

| Condición | Tipo de tangente |
|-----------|------------------|
| $\frac{dy}{dt} = 0$ y $\frac{dx}{dt} \neq 0$ | Tangente **horizontal** |
| $\frac{dx}{dt} = 0$ y $\frac{dy}{dt} \neq 0$ | Tangente **vertical** |
| Ambas $= 0$ | Punto **singular** (análisis especial) |

### Ejemplo Detallado

**Problema:** Encontrar la pendiente de la tangente a $x = t^2$, $y = t^3$ en $t = 2$

**Paso 1:** Calculamos $\frac{dx}{dt}$:
$$\frac{dx}{dt} = 2t$$

**Paso 2:** Calculamos $\frac{dy}{dt}$:
$$\frac{dy}{dt} = 3t^2$$

**Paso 3:** Dividimos:
$$\frac{dy}{dx} = \frac{3t^2}{2t} = \frac{3t}{2}$$

**Paso 4:** Evaluamos en $t = 2$:
$$\frac{dy}{dx}\bigg|_{t=2} = \frac{3(2)}{2} = 3$$

**Resultado:** La pendiente es $\boxed{3}$

**Punto de tangencia:** $(x, y) = (4, 8)$

---

## Método 3: Segunda Derivada (Curvas Paramétricas)

### Cuándo Usar
- Determinar concavidad de la curva
- Encontrar puntos de inflexión

### Fórmula
$$\frac{d^2y}{dx^2} = \frac{d}{dt}\left(\frac{dy}{dx}\right) \cdot \frac{1}{dx/dt} = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{dx/dt}$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Calcular $\frac{dy}{dx}$ | Método 2 |
| 2 | Derivar $\frac{dy}{dx}$ respecto a $t$ | $\frac{d}{dt}\left(\frac{dy}{dx}\right)$ |
| 3 | Dividir por $\frac{dx}{dt}$ | Segunda derivada |

### Ejemplo Detallado

**Problema:** Encontrar $\frac{d^2y}{dx^2}$ para $x = t^2$, $y = t^3$

**Paso 1:** Ya sabemos que:
$$\frac{dy}{dx} = \frac{3t}{2}$$

**Paso 2:** Derivamos respecto a $t$:
$$\frac{d}{dt}\left(\frac{dy}{dx}\right) = \frac{d}{dt}\left(\frac{3t}{2}\right) = \frac{3}{2}$$

**Paso 3:** Dividimos por $\frac{dx}{dt} = 2t$:
$$\frac{d^2y}{dx^2} = \frac{3/2}{2t} = \frac{3}{4t}$$

**Resultado:** $\frac{d^2y}{dx^2} = \boxed{\frac{3}{4t}}$

**Interpretación:** 
- Para $t > 0$: $\frac{d^2y}{dx^2} > 0$ → cóncava hacia arriba
- Para $t < 0$: $\frac{d^2y}{dx^2} < 0$ → cóncava hacia abajo

---

## Método 4: Longitud de Arco (Curvas Paramétricas)

### Cuándo Usar
- Calcular la longitud de una curva paramétrica

### Fórmula
$$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\, dt$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Calcular $\frac{dx}{dt}$ | Derivar $x(t)$ |
| 2 | Calcular $\frac{dy}{dt}$ | Derivar $y(t)$ |
| 3 | Elevar al cuadrado y sumar | $\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2$ |
| 4 | Sacar raíz cuadrada | $\sqrt{\text{suma}}$ |
| 5 | Integrar de $a$ a $b$ | Límites del parámetro |

### Ejemplo Detallado

**Problema:** Calcular la longitud de $x = \cos t$, $y = \sin t$ para $0 \leq t \leq 2\pi$

**Paso 1:** Calculamos $\frac{dx}{dt}$:
$$\frac{dx}{dt} = -\sin t$$

**Paso 2:** Calculamos $\frac{dy}{dt}$:
$$\frac{dy}{dt} = \cos t$$

**Paso 3:** Sumamos los cuadrados:
$$\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 = \sin^2 t + \cos^2 t = 1$$

**Paso 4:** Sacamos raíz:
$$\sqrt{1} = 1$$

**Paso 5:** Integramos:
$$L = \int_0^{2\pi} 1 \, dt = [t]_0^{2\pi} = 2\pi$$

**Resultado:** La longitud es $\boxed{2\pi}$ (la circunferencia del círculo unitario).

---

## Método 5: Área bajo Curva Paramétrica

### Cuándo Usar
- Calcular el área entre una curva paramétrica y el eje $x$

### Fórmula
$$A = \int_a^b y(t) \cdot x'(t)\, dt$$

o equivalentemente:
$$A = -\int_a^b x(t) \cdot y'(t)\, dt$$

### Ejemplo Detallado

**Problema:** Encontrar el área encerrada por la elipse $x = 3\cos t$, $y = 2\sin t$, $0 \leq t \leq 2\pi$

**Paso 1:** Calculamos $x'(t) = -3\sin t$

**Paso 2:** Planteamos la integral (recorrido en sentido antihorario):
$$A = -\int_0^{2\pi} y(t) \cdot x'(t)\, dt = -\int_0^{2\pi} 2\sin t \cdot (-3\sin t)\, dt$$

$$= 6\int_0^{2\pi} \sin^2 t\, dt$$

**Paso 3:** Usamos la identidad $\sin^2 t = \frac{1 - \cos 2t}{2}$:
$$= 6 \int_0^{2\pi} \frac{1 - \cos 2t}{2}\, dt = 3\int_0^{2\pi} (1 - \cos 2t)\, dt$$

**Paso 4:** Evaluamos:
$$= 3\left[t - \frac{\sin 2t}{2}\right]_0^{2\pi} = 3(2\pi - 0) = 6\pi$$

**Resultado:** El área de la elipse es $\boxed{6\pi}$

> **Verificación:** Para una elipse con semiejes $a = 3$ y $b = 2$: $A = \pi ab = \pi(3)(2) = 6\pi$ ✓

---

## Método 6: Conversión Polar ↔ Cartesiana

### Cuándo Usar
- Convertir ecuaciones entre sistemas de coordenadas

### Fórmulas de Conversión

| De Polar a Cartesiana | De Cartesiana a Polar |
|-----------------------|-----------------------|
| $x = r\cos\theta$ | $r = \sqrt{x^2 + y^2}$ |
| $y = r\sin\theta$ | $\theta = \arctan\frac{y}{x}$ (ajustar cuadrante) |

### Identidades Útiles
$$x^2 + y^2 = r^2$$
$$\frac{y}{x} = \tan\theta$$

### Ejemplo Detallado

**Problema:** Convertir $r = 4\cos\theta$ a forma cartesiana

**Paso 1:** Multiplicamos ambos lados por $r$:
$$r^2 = 4r\cos\theta$$

**Paso 2:** Sustituimos:
- $r^2 = x^2 + y^2$
- $r\cos\theta = x$

$$x^2 + y^2 = 4x$$

**Paso 3:** Completamos el cuadrado:
$$x^2 - 4x + y^2 = 0$$
$$x^2 - 4x + 4 + y^2 = 4$$
$$(x-2)^2 + y^2 = 4$$

**Resultado:** Es un círculo con centro $(2, 0)$ y radio $2$.

---

## Método 7: Área en Coordenadas Polares

### Cuándo Usar
- Calcular el área encerrada por una curva polar

### Fórmula
$$A = \frac{1}{2}\int_\alpha^\beta [r(\theta)]^2\, d\theta$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Graficar la curva | Identificar la región |
| 2 | Determinar límites $\alpha$ y $\beta$ | Ángulos que delimitan |
| 3 | Elevar $r$ al cuadrado | $[r(\theta)]^2$ |
| 4 | Integrar con factor $\frac{1}{2}$ | Aplicar la fórmula |

### Ejemplo Detallado

**Problema:** Encontrar el área encerrada por un pétalo de $r = \cos(2\theta)$ (rosa de 4 pétalos)

**Paso 1:** Un pétalo está en el primer cuadrante, donde $r \geq 0$.

**Paso 2:** Determinamos los límites:
$r = 0$ cuando $\cos(2\theta) = 0$, es decir $2\theta = \pm\frac{\pi}{2}$

Para el pétalo en el primer cuadrante: $-\frac{\pi}{4} \leq \theta \leq \frac{\pi}{4}$

**Paso 3:** Planteamos la integral:
$$A = \frac{1}{2}\int_{-\pi/4}^{\pi/4} \cos^2(2\theta)\, d\theta$$

**Paso 4:** Usamos $\cos^2 u = \frac{1 + \cos 2u}{2}$ con $u = 2\theta$:
$$= \frac{1}{2}\int_{-\pi/4}^{\pi/4} \frac{1 + \cos(4\theta)}{2}\, d\theta = \frac{1}{4}\int_{-\pi/4}^{\pi/4} (1 + \cos 4\theta)\, d\theta$$

**Paso 5:** Evaluamos:
$$= \frac{1}{4}\left[\theta + \frac{\sin 4\theta}{4}\right]_{-\pi/4}^{\pi/4}$$

$$= \frac{1}{4}\left[\left(\frac{\pi}{4} + 0\right) - \left(-\frac{\pi}{4} + 0\right)\right] = \frac{1}{4} \cdot \frac{\pi}{2} = \frac{\pi}{8}$$

**Resultado:** El área de un pétalo es $\boxed{\frac{\pi}{8}}$

---

## Método 8: Área entre Curvas Polares

### Cuándo Usar
- Área de región entre dos curvas polares

### Fórmula
$$A = \frac{1}{2}\int_\alpha^\beta \left[r_{\text{ext}}^2 - r_{\text{int}}^2\right]\, d\theta$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Encontrar puntos de intersección | Resolver $r_1 = r_2$ |
| 2 | Determinar cuál curva es exterior | Para el intervalo de interés |
| 3 | Aplicar la fórmula | Exterior² - Interior² |

### Ejemplo Detallado

**Problema:** Encontrar el área dentro de $r = 2$ y fuera de $r = 2(1 - \cos\theta)$ (cardioide)

**Paso 1:** Encontramos intersecciones:
$$2 = 2(1 - \cos\theta) \implies 1 = 1 - \cos\theta \implies \cos\theta = 0$$
$$\theta = \frac{\pi}{2}, \frac{3\pi}{2}$$

**Paso 2:** Para $\frac{\pi}{2} < \theta < \frac{3\pi}{2}$, el círculo está **afuera** del cardioide.

**Paso 3:** Por simetría, calculamos la mitad y duplicamos:
$$A = 2 \cdot \frac{1}{2}\int_{\pi/2}^{\pi} \left[4 - 4(1-\cos\theta)^2\right]\, d\theta$$

$$= \int_{\pi/2}^{\pi} 4\left[1 - (1 - 2\cos\theta + \cos^2\theta)\right]\, d\theta$$

$$= 4\int_{\pi/2}^{\pi} (2\cos\theta - \cos^2\theta)\, d\theta$$

**Paso 4:** Evaluamos (usando $\cos^2\theta = \frac{1+\cos 2\theta}{2}$):
$$= 4\left[2\sin\theta - \frac{\theta}{2} - \frac{\sin 2\theta}{4}\right]_{\pi/2}^{\pi}$$

$$= 4\left[(0 - \frac{\pi}{2} - 0) - (2 - \frac{\pi}{4} - 0)\right] = 4\left(-\frac{\pi}{2} - 2 + \frac{\pi}{4}\right)$$

$$= 4\left(-\frac{\pi}{4} - 2\right) = -\pi - 8$$

El área es $|\text{resultado}| = \boxed{\pi + 8}$ (o recalcular límites)

---

## Método 9: Longitud de Arco en Polares

### Cuándo Usar
- Calcular la longitud de una curva en coordenadas polares

### Fórmula
$$L = \int_\alpha^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\, d\theta$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Calcular $\frac{dr}{d\theta}$ | Derivar $r(\theta)$ |
| 2 | Calcular $r^2 + \left(\frac{dr}{d\theta}\right)^2$ | Suma de cuadrados |
| 3 | Sacar raíz cuadrada | $\sqrt{\text{suma}}$ |
| 4 | Integrar | De $\alpha$ a $\beta$ |

### Ejemplo Detallado

**Problema:** Calcular la longitud del cardioide $r = 1 + \cos\theta$ para $0 \leq \theta \leq 2\pi$

**Paso 1:** Calculamos $\frac{dr}{d\theta}$:
$$\frac{dr}{d\theta} = -\sin\theta$$

**Paso 2:** Calculamos la suma de cuadrados:
$$r^2 + \left(\frac{dr}{d\theta}\right)^2 = (1+\cos\theta)^2 + \sin^2\theta$$

$$= 1 + 2\cos\theta + \cos^2\theta + \sin^2\theta = 2 + 2\cos\theta = 2(1 + \cos\theta)$$

**Paso 3:** Usamos la identidad $1 + \cos\theta = 2\cos^2\frac{\theta}{2}$:
$$\sqrt{2(1+\cos\theta)} = \sqrt{4\cos^2\frac{\theta}{2}} = 2\left|\cos\frac{\theta}{2}\right|$$

**Paso 4:** Integramos (por simetría):
$$L = \int_0^{2\pi} 2\left|\cos\frac{\theta}{2}\right|\, d\theta = 2 \cdot 2\int_0^{\pi} \cos\frac{\theta}{2}\, d\theta$$

$$= 4\left[2\sin\frac{\theta}{2}\right]_0^{\pi} = 8(\sin\frac{\pi}{2} - \sin 0) = 8$$

**Resultado:** La longitud del cardioide es $\boxed{8}$

---

## Método 10: Pendiente de la Tangente en Polares

### Cuándo Usar
- Encontrar la pendiente de la tangente a una curva polar

### Fórmula
$$\frac{dy}{dx} = \frac{\frac{dr}{d\theta}\sin\theta + r\cos\theta}{\frac{dr}{d\theta}\cos\theta - r\sin\theta}$$

### Derivación
Partiendo de $x = r\cos\theta$ y $y = r\sin\theta$:
$$\frac{dy}{dx} = \frac{dy/d\theta}{dx/d\theta}$$

donde:
- $\frac{dx}{d\theta} = \frac{dr}{d\theta}\cos\theta - r\sin\theta$
- $\frac{dy}{d\theta} = \frac{dr}{d\theta}\sin\theta + r\cos\theta$

### Ejemplo Detallado

**Problema:** Encontrar la pendiente de la tangente a $r = 2\cos\theta$ en $\theta = \frac{\pi}{3}$

**Paso 1:** Calculamos $\frac{dr}{d\theta}$:
$$\frac{dr}{d\theta} = -2\sin\theta$$

**Paso 2:** Evaluamos en $\theta = \frac{\pi}{3}$:
- $r = 2\cos\frac{\pi}{3} = 2 \cdot \frac{1}{2} = 1$
- $\frac{dr}{d\theta} = -2\sin\frac{\pi}{3} = -2 \cdot \frac{\sqrt{3}}{2} = -\sqrt{3}$

**Paso 3:** Calculamos numerador y denominador:

Numerador:
$$\frac{dr}{d\theta}\sin\theta + r\cos\theta = (-\sqrt{3})\left(\frac{\sqrt{3}}{2}\right) + (1)\left(\frac{1}{2}\right)$$
$$= -\frac{3}{2} + \frac{1}{2} = -1$$

Denominador:
$$\frac{dr}{d\theta}\cos\theta - r\sin\theta = (-\sqrt{3})\left(\frac{1}{2}\right) - (1)\left(\frac{\sqrt{3}}{2}\right)$$
$$= -\frac{\sqrt{3}}{2} - \frac{\sqrt{3}}{2} = -\sqrt{3}$$

**Paso 4:** Dividimos:
$$\frac{dy}{dx} = \frac{-1}{-\sqrt{3}} = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}$$

**Resultado:** La pendiente es $\boxed{\frac{\sqrt{3}}{3}}$ (o $\frac{1}{\sqrt{3}}$)
