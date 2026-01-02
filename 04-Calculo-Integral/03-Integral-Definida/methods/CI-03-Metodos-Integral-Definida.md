<!--
HUMANO:
Métodos para [integral definida](../../../glossary.md#integral-definida).

IA:
10 métodos prácticos detallados con explicaciones paso a paso.

---
content_type: methods
format: step_by_step
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Métodos para Integral Definida

> **Objetivo:** Dominar la evaluación de integrales definidas con explicaciones detalladas, cálculos intermedios y ejemplos clásicos paso a paso.

---

## Método 1: Evaluación Directa usando TFC

### Cuándo Usar
Para cualquier integral donde se conoce la [antiderivada](../../../glossary.md#antiderivada).

### Teorema Fundamental del Cálculo
$$\int_a^b f(x) \, dx = F(b) - F(a) = \left[F(x)\right]_a^b$$
donde $F'(x) = f(x)$

### Algoritmo de Resolución

| Paso | Acción | Verificación |
|------|--------|--------------|
| 1 | Encontrar $F(x)$ [tal que](../../../glossary.md#derivada) da $f(x)$? |
| 2 | Evaluar $F(b)$ | Sustituir [límite](../../../glossary.md#limite) inferior |
| 4 | Calcular $F(b) - F(a)$ | Restar los valores |

### Ejemplo Detallado

**Problema:** Calcular $\int_0^2 x^2 \, dx$

**Paso 1:** Encontramos la [antiderivada](../../../glossary.md#antiderivada) de $x^2$:
$$F(x) = \frac{x^3}{3}$$

**Verificación:** $F'(x) = \frac{3x^2}{3} = x^2$ ✓

**Paso 2:** Evaluamos en el límite superior $b = 2$:
$$F(2) = \frac{2^3}{3} = \frac{8}{3}$$

**Paso 3:** Evaluamos en el límite inferior $a = 0$:
$$F(0) = \frac{0^3}{3} = 0$$

**Paso 4:** Calculamos la diferencia:
$$\int_0^2 x^2 \, dx = F(2) - F(0) = \frac{8}{3} - 0 = \frac{8}{3}$$

---

## Método 2: Sustitución con Cambio de Límites

### Cuándo Usar
Integrales definidas que requieren [sustitución](../../../glossary.md#sustitucion) $u = g(x)$.

### Ventaja del Cambio de Límites
Al cambiar los [límites](../../../glossary.md#limites) de integración, no es [necesario](../../../glossary.md#necesario) regresar a la variable original.

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Elegir $u = g(x)$ | Identificar la [sustitución](../../..](../../../glossary.md#limites) de integración:
- Cuando $x = 0$: $u = 0^2 + 1 = 1$
- Cuando $x = 1$: $u = 1^2 + 1 = 2$

**Paso 4:** Reescribimos la integral:
$$\int_0^1 2x(x^2+1)^3 \, dx = \int_1^2 u^3 \, du$$

**Paso 5:** Evaluamos:
$$\int_1^2 u^3 \, du = \left[\frac{u^4}{4}\right]_1^2 = \frac{2^4}{4} - \frac{1^4}{4} = \frac{16}{4} - \frac{1}{4} = \frac{15}{4}$$

---

## Método 3: Simetría para Funciones Pares

### Cuándo Usar
- La [función](../../../glossary.md#funcion) satisface $f(-x) = f(x)$
- El intervalo de integración es simétrico: $[-a, a]$

### Fórmula de Simetría Par
$$\int_{-a}^{a} f(x)\,dx = 2\int_0^a f(x)\,dx$$

### Algoritmo de Resolución

| Paso | Acción | Verificación |
|------|--------|--------------|
| 1 | Verificar que $f(-x) = f(x)$ | [Función](../../../glossary.md#funcion) par |
| 2 | Verificar intervalo simétrico $[-a, a]$ | Centro en 0 |
| 3 | Aplicar la fórmula | Duplicar integral de $0$ a $a$ |
| 4 | Evaluar la integral simplificada | Solo lado positivo |

### Ejemplo Detallado

**Problema:** Calcular $\int_{-1}^{1} x^4 \, dx$

**Paso 1:** Verificamos paridad:
$$f(x) = x^4 \implies f(-x) = (-x)^4 = x^4 = f(x) \checkmark$$

**Paso 2:** El intervalo $[-1, 1]$ es simétrico respecto al origen ✓

**Paso 3:** Aplicamos la fórmula:
$$\int_{-1}^{1} x^4 \, dx = 2\int_0^1 x^4\,dx$$

**Paso 4:** Evaluamos:
$$= 2\left[\frac{x^5}{5}\right]_0^1 = 2\left(\frac{1}{5} - 0\right) = \frac{2}{5}$$

---

## Método 4: Simetría para Funciones Impares

### Cuándo Usar
- La función satisface $f(-x) = -f(x)$
- El intervalo de integración es simétrico: $[-a, a]$

### Fórmula de Simetría Impar
$$\int_{-a}^{a} f(x)\,dx = 0$$

### ¿Por qué funciona?
El área bajo la curva para $x < 0$ es exactamente el negativo del área para $x > 0$, por lo que se cancelan.

### Algoritmo de Resolución

| Paso | Acción | Verificación |
|------|--------|--------------|
| 1 | Verificar que $f(-x) = -f(x)$ | Función impar |
| 2 | Verificar intervalo simétrico $[-a, a]$ | Centro en 0 |
| 3 | Concluir que la integral es 0 | Sin cálculos adicionales |

### Ejemplo Detallado

**Problema:** Calcular $\int_{-2}^{2} x^3 \, dx$

**Paso 1:** Verificamos imparidad:
$$f(x) = x^3 \implies f(-x) = (-x)^3 = -x^3 = -f(x) \checkmark$$

**Paso 2:** El intervalo $[-2, 2]$ es simétrico respecto al origen ✓

**Paso 3:** Aplicamos la propiedad:
$$\int_{-2}^{2} x^3 \, dx = 0$$

**Verificación directa (opcional):**
$$\int_{-2}^{2} x^3 \, dx = \left[\frac{x^4}{4}\right]_{-2}^{2} = \frac{16}{4} - \frac{16}{4} = 0 \checkmark$$

---

## Método 5: Separar Parte Par e Impar

### Cuándo Usar
- Funciones mixtas (ni pares ni impares) en intervalo simétrico
- Útil para simplificar cálculos

### Descomposición de una Función
Cualquier función se puede escribir como:
$$f(x) = \underbrace{\frac{f(x)+f(-x)}{2}}_{\text{parte par}} + \underbrace{\frac{f(x)-f(-x)}{2}}_{\text{parte impar}}$$

### Algoritmo de Resolución

| Paso | Acción | Resultado |
|------|--------|-----------|
| 1 | Identificar términos pares e impares | Separar la suma |
| 2 | La parte impar integra a 0 | Eliminar esos términos |
| 3 | Calcular solo la parte par | $2\int_0^a$ (parte par) |

### Ejemplo Detallado

**Problema:** Calcular $\int_{-2}^{2} (x^3 + x^2)\,dx$

**Paso 1:** Identificamos cada término:
- $x^3$ es **impar** (exponente impar)
- $x^2$ es **par** (exponente par)

**Paso 2:** Separamos la integral:
$$\int_{-2}^{2} (x^3 + x^2)\,dx = \int_{-2}^{2} x^3\,dx + \int_{-2}^{2} x^2\,dx$$

**Paso 3:** Aplicamos las propiedades de simetría:
$$= 0 + 2\int_0^2 x^2\,dx$$

**Paso 4:** Evaluamos:
$$= 2\left[\frac{x^3}{3}\right]_0^2 = 2 \cdot \frac{8}{3} = \frac{16}{3}$$

---

## Método 6: División del Intervalo

### Cuándo Usar
- Funciones definidas por partes
- Funciones con valor absoluto
- Discontinuidades en el integrando

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar puntos de cambio | Donde cambia la definición |
| 2 | Dividir la integral | Una integral por cada tramo |
| 3 | Evaluar cada parte | Con la fórmula correcta |
| 4 | Sumar los resultados | Total = suma de partes |

### Ejemplo Detallado

**Problema:** Calcular $\int_0^2 |x - 1| \, dx$

**Paso 1:** Identificamos dónde cambia el valor absoluto:
$$|x-1| = 0 \text{ cuando } x = 1$$

**Paso 2:** Determinamos la expresión en cada intervalo:
- Para $0 \leq x < 1$: $x - 1 < 0$, entonces $|x-1| = -(x-1) = 1-x$
- Para $1 \leq x \leq 2$: $x - 1 \geq 0$, entonces $|x-1| = x-1$

**Paso 3:** Dividimos la integral:
$$\int_0^2 |x - 1| \, dx = \int_0^1 (1-x)\,dx + \int_1^2 (x-1)\,dx$$

**Paso 4:** Evaluamos cada parte:

Primera integral:
$$\int_0^1 (1-x)\,dx = \left[x - \frac{x^2}{2}\right]_0^1 = \left(1 - \frac{1}{2}\right) - 0 = \frac{1}{2}$$

Segunda integral:
$$\int_1^2 (x-1)\,dx = \left[\frac{x^2}{2} - x\right]_1^2 = \left(2 - 2\right) - \left(\frac{1}{2} - 1\right) = 0 + \frac{1}{2} = \frac{1}{2}$$

**Paso 5:** Sumamos:
$$\int_0^2 |x - 1| \, dx = \frac{1}{2} + \frac{1}{2} = 1$$

---

## Método 7: Derivada de Integral con Límite Variable

### Cuándo Usar
Hallar $\frac{d}{dx}\int_a^{g(x)} f(t)\,dt$ donde el límite superior depende de $x$.

### Fórmula (Regla de Leibniz - caso simple)
$$\frac{d}{dx}\int_a^{g(x)} f(t)\,dt = f(g(x)) \cdot g'(x)$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Identificar $f(t)$ y $g(x)$ | Integrando y límite superior |
| 2 | Evaluar $f(g(x))$ | Sustituir $g(x)$ en $f$ |
| 3 | Calcular $g'(x)$ | Derivar el límite |
| 4 | Multiplicar | $f(g(x)) \cdot g'(x)$ |

### Ejemplo Detallado

**Problema:** Calcular $\frac{d}{dx}\int_0^{x^2} \cos t \, dt$

**Paso 1:** Identificamos:
- $f(t) = \cos t$
- $g(x) = x^2$

**Paso 2:** Evaluamos $f(g(x))$:
$$f(g(x)) = f(x^2) = \cos(x^2)$$

**Paso 3:** Calculamos $g'(x)$:
$$g'(x) = \frac{d}{dx}(x^2) = 2x$$

**Paso 4:** Aplicamos la regla:
$$\frac{d}{dx}\int_0^{x^2} \cos t \, dt = \cos(x^2) \cdot 2x = 2x\cos(x^2)$$

---

## Método 8: Derivada con Ambos Límites Variables

### Cuándo Usar
Hallar $\frac{d}{dx}\int_{h(x)}^{g(x)} f(t)\,dt$ donde ambos límites dependen de $x$.

### Fórmula General
$$\frac{d}{dx}\int_{h(x)}^{g(x)} f(t)\,dt = f(g(x)) \cdot g'(x) - f(h(x)) \cdot h'(x)$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Identificar $f$, $g$, $h$ | Integrando y ambos límites |
| 2 | Calcular contribución superior | $f(g(x)) \cdot g'(x)$ |
| 3 | Calcular contribución inferior | $f(h(x)) \cdot h'(x)$ |
| 4 | Restar | Superior $-$ Inferior |

### Ejemplo Detallado

**Problema:** Calcular $\frac{d}{dx}\int_x^{x^2} e^t \, dt$

**Paso 1:** Identificamos:
- $f(t) = e^t$
- $g(x) = x^2$ (límite superior)
- $h(x) = x$ (límite inferior)

**Paso 2:** Contribución del límite superior:
$$f(g(x)) \cdot g'(x) = e^{x^2} \cdot 2x = 2xe^{x^2}$$

**Paso 3:** Contribución del límite inferior:
$$f(h(x)) \cdot h'(x) = e^x \cdot 1 = e^x$$

**Paso 4:** Restamos:
$$\frac{d}{dx}\int_x^{x^2} e^t \, dt = 2xe^{x^2} - e^x$$

---

## Método 9: Propiedad de Traslación

### Cuándo Usar
- Cambio de variable lineal $u = x - c$
- Simplificar el integrando mediante una traslación

### Fórmula
$$\int_a^b f(x)\,dx = \int_{a-c}^{b-c} f(u+c)\,du$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Elegir $c$ apropiado | Generalmente el centro |
| 2 | Sustituir $u = x - c$ | $du = dx$ |
| 3 | Ajustar límites | $a-c$ y $b-c$ |
| 4 | Simplificar y evaluar | Nueva integral más simple |

### Ejemplo Detallado

**Problema:** Calcular $\int_1^3 (x-2)^2\,dx$

**Paso 1:** Elegimos $c = 2$ para simplificar $(x-2)^2$.

**Paso 2:** Hacemos $u = x - 2$, entonces $du = dx$.

**Paso 3:** Cambiamos los límites:
- $x = 1 \Rightarrow u = 1 - 2 = -1$
- $x = 3 \Rightarrow u = 3 - 2 = 1$

**Paso 4:** Reescribimos:
$$\int_1^3 (x-2)^2\,dx = \int_{-1}^{1} u^2\,du$$

**Paso 5:** ¡Observamos simetría! $u^2$ es par en $[-1, 1]$:
$$= 2\int_0^1 u^2\,du = 2\left[\frac{u^3}{3}\right]_0^1 = 2 \cdot \frac{1}{3} = \frac{2}{3}$$

---

## Método 10: Propiedad de Reflexión

### Cuándo Usar
- Integrales trigonométricas especiales
- Cuando $f(x)$ y $f(a-x)$ tienen relación útil

### Fórmula
$$\int_0^a f(x)\,dx = \int_0^a f(a-x)\,dx$$

### Algoritmo de Resolución

| Paso | Acción | Propósito |
|------|--------|-----------|
| 1 | Sustituir $u = a - x$ | Reflexión del intervalo |
| 2 | Calcular $du = -dx$ | Cambio de signo |
| 3 | Ajustar límites | Se invierten y cambian signo |
| 4 | Simplificar | Relacionar con integral original |

### Ejemplo Detallado

**Problema:** Demostrar que $\int_0^{\pi/2} \sin^n x\,dx = \int_0^{\pi/2} \cos^n x\,dx$

**Paso 1:** Partimos de $\int_0^{\pi/2} \sin^n x\,dx$

**Paso 2:** Hacemos la sustitución $u = \frac{\pi}{2} - x$:
- $du = -dx$
- Cuando $x = 0$: $u = \frac{\pi}{2}$
- Cuando $x = \frac{\pi}{2}$: $u = 0$

**Paso 3:** Sustituimos:
$$\int_0^{\pi/2} \sin^n x\,dx = \int_{\pi/2}^{0} \sin^n\left(\frac{\pi}{2}-u\right) \cdot (-du)$$

**Paso 4:** Invertimos los límites (cambia el signo):
$$= \int_0^{\pi/2} \sin^n\left(\frac{\pi}{2}-u\right)\,du$$

**Paso 5:** Usamos la identidad $\sin\left(\frac{\pi}{2}-u\right) = \cos u$:
$$= \int_0^{\pi/2} \cos^n u\,du$$

**Conclusión:**
$$\int_0^{\pi/2} \sin^n x\,dx = \int_0^{\pi/2} \cos^n x\,dx \quad \blacksquare$$
