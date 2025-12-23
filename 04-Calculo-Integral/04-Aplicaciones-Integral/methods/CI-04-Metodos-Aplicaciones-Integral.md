<!--
HUMANO:
Métodos para aplicaciones de la integral.

IA:
Procedimientos paso a paso para cada tipo de aplicación.

---
content_type: methods
format: step_by_step
---
-->

# Métodos para Aplicaciones de la Integral

---

## Método 1: Área entre Curvas (Integración Vertical)

**Pasos:**
1. Dibujar las curvas e identificar la región.
2. Encontrar puntos de intersección resolviendo $f(x) = g(x)$.
3. Determinar cuál curva está arriba en el intervalo.
4. Integrar: $A = \int_a^b [f_{\text{arriba}} - f_{\text{abajo}}]\,dx$

**Ejemplo:** Área entre $y = x^2$ y $y = x$.

1. Intersecciones: $x^2 = x \Rightarrow x = 0, 1$
2. En $(0,1)$: $x > x^2$
3. $A = \int_0^1 (x - x^2)\,dx = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = \frac{1}{6}$

---

## Método 2: Área entre Curvas (Integración Horizontal)

**Pasos:**
1. Expresar las curvas como $x = f(y)$.
2. Encontrar intersecciones en términos de $y$.
3. Determinar cuál está a la derecha.
4. Integrar: $A = \int_c^d [f_{\text{derecha}} - f_{\text{izquierda}}]\,dy$

**Ejemplo:** Área entre $x = y^2$ y $x = y + 2$.

1. Intersecciones: $y^2 = y + 2 \Rightarrow y = -1, 2$
2. $x = y + 2$ está a la derecha.
3. $A = \int_{-1}^{2} [(y+2) - y^2]\,dy = \frac{9}{2}$

---

## Método 3: Volumen por Discos

**Pasos:**
1. Identificar el eje de rotación.
2. Determinar el radio $r(x)$ o $r(y)$.
3. Establecer límites de integración.
4. Aplicar $V = \pi\int [r]^2\,dx$ (o $dy$).

**Ejemplo:** Rotar $y = \sqrt{x}$, $0 \leq x \leq 4$, alrededor del eje $x$.

$$V = \pi\int_0^4 (\sqrt{x})^2\,dx = \pi\int_0^4 x\,dx = \pi\left[\frac{x^2}{2}\right]_0^4 = 8\pi$$

---

## Método 4: Volumen por Arandelas

**Pasos:**
1. Identificar radio exterior $R$ y radio interior $r$.
2. Los radios se miden desde el eje de rotación.
3. Aplicar $V = \pi\int (R^2 - r^2)\,dx$.

**Ejemplo:** Región entre $y = x^2$ y $y = x$ rotada alrededor del eje $x$.

$$V = \pi\int_0^1 [x^2 - (x^2)^2]\,dx = \pi\int_0^1 (x^2 - x^4)\,dx = \frac{2\pi}{15}$$

---

## Método 5: Volumen por Capas Cilíndricas

**Pasos:**
1. Identificar el eje de rotación.
2. Radio del tubo = distancia de $x$ (o $y$) al eje.
3. Altura del tubo = valor de la función.
4. Aplicar $V = 2\pi\int (\text{radio})(\text{altura})\,dx$.

**Ejemplo:** Rotar $y = x^2$, $0 \leq x \leq 2$, alrededor del eje $y$.

$$V = 2\pi\int_0^2 x \cdot x^2\,dx = 2\pi\int_0^2 x^3\,dx = 2\pi\left[\frac{x^4}{4}\right]_0^2 = 8\pi$$

---

## Método 6: Longitud de Arco

**Pasos:**
1. Calcular $\frac{dy}{dx}$.
2. Formar $\sqrt{1 + (dy/dx)^2}$.
3. Integrar en el intervalo dado.

**Ejemplo:** Longitud de $y = x^{3/2}$ de $x = 0$ a $x = 4$.

1. $\frac{dy}{dx} = \frac{3}{2}x^{1/2}$
2. $1 + \left(\frac{dy}{dx}\right)^2 = 1 + \frac{9}{4}x$
3. $L = \int_0^4 \sqrt{1 + \frac{9x}{4}}\,dx$

Con $u = 1 + \frac{9x}{4}$:
$$L = \frac{4}{9} \cdot \frac{2}{3}\left[u^{3/2}\right]_1^{10} = \frac{8}{27}(10^{3/2} - 1)$$

---

## Método 7: Área de Superficie (Rotación alrededor de eje $x$)

**Pasos:**
1. Calcular $f'(x)$ y $\sqrt{1 + [f'(x)]^2}$.
2. Aplicar $S = 2\pi\int f(x)\sqrt{1 + [f'(x)]^2}\,dx$.

**Ejemplo:** Superficie al rotar $y = x^2$, $0 \leq x \leq 1$, alrededor del eje $x$.

1. $f'(x) = 2x$, $\sqrt{1 + 4x^2}$
2. $S = 2\pi\int_0^1 x^2\sqrt{1 + 4x^2}\,dx$ (requiere sustitución trigonométrica)

---

## Método 8: Trabajo con Resortes

**Pasos:**
1. Determinar la constante $k$ del resorte.
2. Establecer posiciones inicial $x_1$ y final $x_2$.
3. Calcular $W = \int_{x_1}^{x_2} kx\,dx$.

**Ejemplo:** Estirar un resorte con $k = 50$ N/m de 0.1 m a 0.3 m.

$$W = \int_{0.1}^{0.3} 50x\,dx = 50\left[\frac{x^2}{2}\right]_{0.1}^{0.3} = 25(0.09 - 0.01) = 2 \text{ J}$$

---

## Método 9: Trabajo de Bombeo

**Pasos:**
1. Establecer un sistema de coordenadas (usualmente $y$ hacia arriba).
2. Determinar $A(y)$ (área de sección transversal del tanque).
3. Determinar $d(y)$ (distancia que se eleva el elemento).
4. Integrar $W = \int \rho g A(y) d(y)\,dy$.

**Ejemplo:** Bombear agua de un tanque cilíndrico (radio 2 m, altura 5 m) hasta el borde.

- $A(y) = \pi(2)^2 = 4\pi$
- $d(y) = 5 - y$
- $\rho g = 9800$ N/m³

$$W = 9800 \cdot 4\pi \int_0^5 (5-y)\,dy = 39200\pi\left[5y - \frac{y^2}{2}\right]_0^5 = 490000\pi \text{ J}$$

---

## Método 10: Valor Promedio

**Pasos:**
1. Identificar el intervalo $[a,b]$.
2. Calcular $\int_a^b f(x)\,dx$.
3. Dividir por $(b-a)$.

**Ejemplo:** Valor promedio de $f(x) = x^2$ en $[0, 3]$.

$$f_{\text{prom}} = \frac{1}{3-0}\int_0^3 x^2\,dx = \frac{1}{3}\left[\frac{x^3}{3}\right]_0^3 = \frac{1}{3} \cdot 9 = 3$$
