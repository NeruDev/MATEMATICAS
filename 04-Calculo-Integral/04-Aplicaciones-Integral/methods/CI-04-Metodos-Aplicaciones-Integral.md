<!--
HUMANO:
Métodos para aplicaciones de la integral.

IA:
Procedimientos paso a paso para cada tipo de aplicación con ejemplos detallados.

---
content_type: methods
format: step_by_step
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Métodos para Aplicaciones de la Integral

> **Objetivo:** Dominar las aplicaciones geométricas y físicas de la integral con explicaciones detalladas, cálculos intermedios y ejemplos clásicos paso a paso.

---

## Método 1: Área entre Curvas (Integración Vertical)

### Cuándo Usar
- Región delimitada entre dos curvas $y = f(x)$ e $y = g(x)$
- Cuando es más fácil expresar las funciones en términos de $x$

### Fórmula Fundamental
$$A = \int_a^b [f_{\text{arriba}}(x) - f_{\text{abajo}}(x)]\,dx$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Graficar las curvas | Visualizar la región |
| 2 | Encontrar intersecciones | Resolver $f(x) = g(x)$ |
| 3 | Determinar cuál está arriba | En el intervalo de interés |
| 4 | Integrar la diferencia | Arriba menos abajo |

### Ejemplo Detallado

**Problema:** Calcular el área entre $y = x^2$ y $y = x$.

**Paso 1:** Graficamos mentalmente:
- $y = x^2$ es una parábola que abre hacia arriba
- $y = x$ es una línea recta con pendiente 1

**Paso 2:** Encontramos los puntos de intersección:
$$x^2 = x$$
$$x^2 - x = 0$$
$$x(x - 1) = 0$$
$$x = 0 \quad \text{o} \quad x = 1$$

**Paso 3:** Determinamos cuál curva está arriba en $(0, 1)$:

Evaluamos en $x = 0.5$:
- $y = x$: $y = 0.5$
- $y = x^2$: $y = 0.25$

Como $0.5 > 0.25$, la recta $y = x$ está **arriba** de $y = x^2$ en este intervalo.

**Paso 4:** Planteamos la integral:
$$A = \int_0^1 (x - x^2)\,dx$$

**Paso 5:** Evaluamos:
$$A = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1$$

$$= \left(\frac{1}{2} - \frac{1}{3}\right) - (0 - 0)$$

$$= \frac{3}{6} - \frac{2}{6} = \frac{1}{6}$$

**Resultado:** El área es $\boxed{\frac{1}{6}}$ unidades cuadradas.

---

## Método 2: Área entre Curvas (Integración Horizontal)

### Cuándo Usar
- Región delimitada entre curvas expresadas como $x = f(y)$
- Cuando integrar respecto a $y$ simplifica el problema

### Fórmula
$$A = \int_c^d [f_{\text{derecha}}(y) - f_{\text{izquierda}}(y)]\,dy$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Expresar curvas como $x = f(y)$ | Despejar $x$ |
| 2 | Encontrar intersecciones en $y$ | [Límites](../../../glossary.md#limites) verticales |
| 3 | Determinar cuál está a la derecha | Mayor valor de $x$ |
| 4 | Integrar respecto a $y$ | Derecha menos izquierda |

### Ejemplo Detallado

**Problema:** Calcular el área entre $x = y^2$ y $x = y + 2$.

**Paso 1:** Las curvas ya están en la forma $x = f(y)$.

**Paso 2:** Encontramos intersecciones:
$$y^2 = y + 2$$
$$y^2 - y - 2 = 0$$
$$(y-2)(y+1) = 0$$
$$y = 2 \quad \text{o} \quad y = -1$$

**Paso 3:** Determinamos cuál está a la derecha en $(-1, 2)$:

Evaluamos en $y = 0$:
- $x = y^2$: $x = 0$
- $x = y + 2$: $x = 2$

Como $2 > 0$, la recta $x = y + 2$ está a la **derecha**.

**Paso 4:** Planteamos la integral:
$$A = \int_{-1}^{2} [(y+2) - y^2]\,dy$$

**Paso 5:** Evaluamos:
$$A = \int_{-1}^{2} (y + 2 - y^2)\,dy$$

$$= \left[\frac{y^2}{2} + 2y - \frac{y^3}{3}\right]_{-1}^{2}$$

En $y = 2$:
$$\frac{4}{2} + 4 - \frac{8}{3} = 2 + 4 - \frac{8}{3} = 6 - \frac{8}{3} = \frac{18 - 8}{3} = \frac{10}{3}$$

En $y = -1$:
$$\frac{1}{2} - 2 - \frac{-1}{3} = \frac{1}{2} - 2 + \frac{1}{3} = \frac{3 + 2 - 12}{6} = -\frac{7}{6}$$

$$A = \frac{10}{3} - \left(-\frac{7}{6}\right) = \frac{10}{3} + \frac{7}{6} = \frac{20 + 7}{6} = \frac{27}{6} = \frac{9}{2}$$

**Resultado:** El área es $\boxed{\frac{9}{2}}$ unidades cuadradas.

---

## Método 3: Volumen por Discos

### Cuándo Usar
- Sólido de revolución sin "hueco" en el centro
- El eje de rotación es un borde de la región

### Fórmula
$$V = \pi\int_a^b [r(x)]^2\,dx$$

donde $r(x)$ es el radio del disco (distancia de la curva al eje).

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar el eje de rotación | Eje $x$, eje $y$, u otro |
| 2 | Determinar el radio $r$ | Distancia al eje |
| 3 | Establecer [límites](../../../glossary.md#limites) | En la variable de integración |
| 4 | Aplicar $V = \pi\int r^2$ | No olvidar el $\pi$ |

### Ejemplo Detallado

**Problema:** Hallar el volumen al rotar $y = \sqrt{x}$, $0 \leq x \leq 4$, alrededor del eje $x$.

**Paso 1:** El eje de rotación es el eje $x$.

**Paso 2:** El radio de cada disco es la distancia vertical de la curva al eje $x$:
$$r(x) = y = \sqrt{x}$$

**Paso 3:** Los límites son $x = 0$ hasta $x = 4$.

**Paso 4:** Aplicamos la fórmula:
$$V = \pi\int_0^4 (\sqrt{x})^2\,dx = \pi\int_0^4 x\,dx$$

**Paso 5:** Evaluamos:
$$V = \pi\left[\frac{x^2}{2}\right]_0^4 = \pi\left(\frac{16}{2} - 0\right) = 8\pi$$

**Resultado:** El volumen es $\boxed{8\pi}$ unidades cúbicas.

---

## Método 4: Volumen por Arandelas (Washers)

### Cuándo Usar
- Sólido de revolución con "hueco" en el centro
- Región entre dos curvas rotada alrededor de un eje

### Fórmula
$$V = \pi\int_a^b [R(x)^2 - r(x)^2]\,dx$$

donde:
- $R$ = radio exterior (curva más alejada del eje)
- $r$ = radio interior (curva más cercana al eje)

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar radio exterior $R$ | Curva más lejos del eje |
| 2 | Identificar radio interior $r$ | Curva más cerca del eje |
| 3 | Los radios se miden desde el eje | Distancia perpendicular |
| 4 | Aplicar $V = \pi\int (R^2 - r^2)$ | Diferencia de cuadrados |

### Ejemplo Detallado

**Problema:** Encontrar el volumen cuando la región entre $y = x^2$ y $y = x$ se rota alrededor del eje $x$.

**Paso 1:** Identificamos los límites (ya calculados antes): $x = 0$ a $x = 1$.

**Paso 2:** Determinamos los radios (distancia al eje $x$):
- Radio exterior $R = x$ (la recta está más arriba)
- Radio interior $r = x^2$ (la parábola está más abajo)

**Paso 3:** Planteamos la integral:
$$V = \pi\int_0^1 [x^2 - (x^2)^2]\,dx = \pi\int_0^1 (x^2 - x^4)\,dx$$

**Paso 4:** Evaluamos:
$$V = \pi\left[\frac{x^3}{3} - \frac{x^5}{5}\right]_0^1$$

$$= \pi\left(\frac{1}{3} - \frac{1}{5}\right) = \pi\left(\frac{5 - 3}{15}\right) = \frac{2\pi}{15}$$

**Resultado:** El volumen es $\boxed{\frac{2\pi}{15}}$ unidades cúbicas.

---

## Método 5: Volumen por Capas Cilíndricas (Shells)

### Cuándo Usar
- Cuando el método de discos/arandelas es complicado
- Especialmente útil cuando se rota alrededor del eje $y$ una [función](../../../glossary.md#funcion) $y = f(x)$

### Fórmula
$$V = 2\pi\int_a^b (\text{radio}) \cdot (\text{altura})\,dx$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Radio del cilindro | Distancia horizontal al eje (generalmente $x$) |
| 2 | Altura del cilindro | Valor de la [función](../../../glossary.md#funcion) $f(x)$ |
| 3 | Espesor | $dx$ (o $dy$) |
| 4 | Aplicar $V = 2\pi\int$ (radio)(altura) | Factor $2\pi$ del perímetro |

### Ejemplo Detallado

**Problema:** Hallar el volumen al rotar $y = x^2$, $0 \leq x \leq 2$, alrededor del eje $y$.

**Paso 1:** Visualizamos una capa cilíndrica a distancia $x$ del eje $y$:
- **Radio** = $x$ (distancia al eje $y$)
- **Altura** = $x^2$ (valor de la función)
- **Espesor** = $dx$

**Paso 2:** El volumen de cada capa es aproximadamente:
$$dV = 2\pi \cdot (\text{radio}) \cdot (\text{altura}) \cdot (\text{espesor}) = 2\pi \cdot x \cdot x^2 \cdot dx$$

**Paso 3:** Integramos:
$$V = 2\pi\int_0^2 x \cdot x^2\,dx = 2\pi\int_0^2 x^3\,dx$$

**Paso 4:** Evaluamos:
$$V = 2\pi\left[\frac{x^4}{4}\right]_0^2 = 2\pi \cdot \frac{16}{4} = 2\pi \cdot 4 = 8\pi$$

**Resultado:** El volumen es $\boxed{8\pi}$ unidades cúbicas.

---

## Método 6: Longitud de Arco

### Cuándo Usar
- Calcular la longitud de una curva $y = f(x)$ de $x = a$ a $x = b$

### Fórmula
$$L = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Calcular $\frac{dy}{dx}$ | Derivar la función |
| 2 | Elevar al cuadrado | $\left(\frac{dy}{dx}\right)^2$ |
| 3 | Sumar 1 | $1 + \left(\frac{dy}{dx}\right)^2$ |
| 4 | Sacar raíz cuadrada | $\sqrt{1 + \left(\frac{dy}{dx}\right)^2}$ |
| 5 | Integrar | En el intervalo dado |

### Ejemplo Detallado

**Problema:** Calcular la longitud de $y = x^{3/2}$ de $x = 0$ a $x = 4$.

**Paso 1:** Calculamos la [derivada](../../../glossary.md#derivada):
$$\frac{dy}{dx} = \frac{3}{2}x^{1/2} = \frac{3}{2}\sqrt{x}$$

**Paso 2:** Elevamos al cuadrado:
$$\left(\frac{dy}{dx}\right)^2 = \left(\frac{3}{2}\sqrt{x}\right)^2 = \frac{9}{4}x$$

**Paso 3:** Sumamos 1:
$$1 + \frac{9}{4}x = \frac{4 + 9x}{4}$$

**Paso 4:** Planteamos la integral:
$$L = \int_0^4 \sqrt{1 + \frac{9x}{4}}\,dx = \int_0^4 \sqrt{\frac{4 + 9x}{4}}\,dx = \frac{1}{2}\int_0^4 \sqrt{4 + 9x}\,dx$$

**Paso 5:** Usamos [sustitución](../../../glossary.md#sustitucion) $u = 4 + 9x$, $du = 9dx$:

Cuando $x = 0$: $u = 4$
Cuando $x = 4$: $u = 40$

$$L = \frac{1}{2} \cdot \frac{1}{9}\int_4^{40} \sqrt{u}\,du = \frac{1}{18}\left[\frac{2u^{3/2}}{3}\right]_4^{40}$$

$$= \frac{1}{27}\left[40^{3/2} - 4^{3/2}\right] = \frac{1}{27}\left[40\sqrt{40} - 8\right]$$

$$= \frac{1}{27}\left[80\sqrt{10} - 8\right] = \frac{8(10\sqrt{10} - 1)}{27}$$

**Resultado:** La longitud es $\boxed{\frac{8(10\sqrt{10} - 1)}{27}}$ unidades.

---

## Método 7: Área de Superficie de Revolución

### Cuándo Usar
- Calcular el área de la superficie generada al rotar una curva

### Fórmula (rotación alrededor del eje $x$)
$$S = 2\pi\int_a^b f(x)\sqrt{1 + [f'(x)]^2}\,dx$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Calcular $f'(x)$ | [Derivada](../../../glossary.md#derivada) de la función |
| 2 | Formar $\sqrt{1 + [f'(x)]^2}$ | Factor de longitud de arco |
| 3 | Multiplicar por $f(x)$ | Radio de la circunferencia |
| 4 | Multiplicar por $2\pi$ | Perímetro |
| 5 | Integrar | En el intervalo dado |

### Ejemplo Detallado

**Problema:** Calcular el área de la superficie al rotar $y = \sqrt{x}$, $1 \leq x \leq 4$, alrededor del eje $x$.

**Paso 1:** Calculamos $f'(x)$:
$$f(x) = \sqrt{x} = x^{1/2}$$
$$f'(x) = \frac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}$$

**Paso 2:** Calculamos $[f'(x)]^2$:
$$[f'(x)]^2 = \frac{1}{4x}$$

**Paso 3:** Formamos $1 + [f'(x)]^2$:
$$1 + \frac{1}{4x} = \frac{4x + 1}{4x}$$

**Paso 4:** Sacamos raíz:
$$\sqrt{1 + [f'(x)]^2} = \sqrt{\frac{4x+1}{4x}} = \frac{\sqrt{4x+1}}{2\sqrt{x}}$$

**Paso 5:** Planteamos la integral:
$$S = 2\pi\int_1^4 \sqrt{x} \cdot \frac{\sqrt{4x+1}}{2\sqrt{x}}\,dx = \pi\int_1^4 \sqrt{4x+1}\,dx$$

**Paso 6:** Evaluamos con $u = 4x + 1$:
$$S = \pi \cdot \frac{1}{4} \cdot \frac{2}{3}\left[(4x+1)^{3/2}\right]_1^4 = \frac{\pi}{6}\left[17^{3/2} - 5^{3/2}\right]$$

**Resultado:** $S = \boxed{\frac{\pi}{6}(17\sqrt{17} - 5\sqrt{5})}$ unidades cuadradas.

---

## Método 8: Trabajo con Resortes (Ley de Hooke)

### Cuándo Usar
- Calcular el trabajo para estirar o comprimir un resorte
- Ley de Hooke: $F = kx$ donde $k$ es la constante del resorte

### Fórmula
$$W = \int_{x_1}^{x_2} kx\,dx = \frac{k}{2}(x_2^2 - x_1^2)$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Determinar $k$ | De datos del problema |
| 2 | Establecer $x_1$ y $x_2$ | Desplazamientos desde equilibrio |
| 3 | Calcular la integral | $W = \int kx\,dx$ |

### Ejemplo Detallado

**Problema:** Un resorte tiene constante $k = 50$ N/m. Calcular el trabajo para estirarlo de 0.1 m a 0.3 m desde su posición natural.

**Paso 1:** Tenemos $k = 50$ N/m.

**Paso 2:** Los límites son:
- $x_1 = 0.1$ m
- $x_2 = 0.3$ m

**Paso 3:** Calculamos el trabajo:
$$W = \int_{0.1}^{0.3} 50x\,dx = 50\left[\frac{x^2}{2}\right]_{0.1}^{0.3}$$

$$= 25\left[(0.3)^2 - (0.1)^2\right] = 25(0.09 - 0.01) = 25(0.08) = 2 \text{ J}$$

**Resultado:** El trabajo es $\boxed{2 \text{ Joules}}$.

---

## Método 9: Trabajo de Bombeo

### Cuándo Usar
- Calcular el trabajo para bombear líquido desde un tanque

### Fórmula General
$$W = \int \rho g \cdot A(y) \cdot d(y)\,dy$$

donde:
- $\rho g$ = peso específico del líquido (agua: 9800 N/m³)
- $A(y)$ = área de la sección transversal a altura $y$
- $d(y)$ = distancia que se eleva cada elemento

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Establecer [sistema de coordenadas](../../../glossary.md#sistema-de-coordenadas) | Generalmente $y$ hacia arriba |
| 2 | Determinar $A(y)$ | Área de sección transversal |
| 3 | Determinar $d(y)$ | Distancia al punto de descarga |
| 4 | Establecer límites | Nivel inicial y final del líquido |
| 5 | Integrar | $W = \int \rho g A(y) d(y)\,dy$ |

### Ejemplo Detallado

**Problema:** Un tanque cilíndrico tiene radio 2 m y altura 5 m, lleno de agua. Calcular el trabajo para bombear toda el agua hasta el borde superior.

**Paso 1:** Establecemos $y = 0$ en el fondo del tanque.

**Paso 2:** El área de cada sección es constante:
$$A(y) = \pi r^2 = \pi(2)^2 = 4\pi \text{ m}^2$$

**Paso 3:** La distancia que cada capa debe subir:
$$d(y) = 5 - y$$
(desde altura $y$ hasta el borde en $y = 5$)

**Paso 4:** Los límites son $y = 0$ (fondo) hasta $y = 5$ (superficie).

**Paso 5:** Calculamos:
$$W = \int_0^5 9800 \cdot 4\pi \cdot (5-y)\,dy$$

$$= 39200\pi \int_0^5 (5-y)\,dy$$

$$= 39200\pi \left[5y - \frac{y^2}{2}\right]_0^5$$

$$= 39200\pi \left(25 - \frac{25}{2}\right) = 39200\pi \cdot \frac{25}{2}$$

$$= 490000\pi \text{ J} \approx 1{,}539{,}380 \text{ J}$$

**Resultado:** El trabajo es $\boxed{490{,}000\pi \text{ J}}$.

---

## Método 10: Valor Promedio de una Función

### Cuándo Usar
- Encontrar el valor "típico" de una función en un intervalo

### Fórmula
$$f_{\text{prom}} = \frac{1}{b-a}\int_a^b f(x)\,dx$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Identificar el intervalo $[a,b]$ | Límites de integración |
| 2 | Calcular $\int_a^b f(x)\,dx$ | [Integral definida](../../..](../../../glossary.md#valor-promedio) de $f(x) = x^2$ en el intervalo $[0, 3]$.

**Paso 1:** Identificamos:
- $a = 0$
- $b = 3$
- $b - a = 3$

**Paso 2:** Calculamos la integral:
$$\int_0^3 x^2\,dx = \left[\frac{x^3}{3}\right]_0^3 = \frac{27}{3} - 0 = 9$$

**Paso 3:** Dividimos por la longitud del intervalo:
$$f_{\text{prom}} = \frac{1}{3} \cdot 9 = 3$$

**Resultado:** El [valor promedio](../../../glossary.md#valor-promedio) es $\boxed{3}$.

**Interpretación:** Aunque $f(x) = x^2$ varía de 0 a 9 en el intervalo, su valor "típico" es 3.
