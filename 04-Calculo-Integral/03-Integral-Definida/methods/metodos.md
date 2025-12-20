<!--
HUMANO:
Métodos para integral definida.

IA:
10 métodos prácticos detallados.

---
content_type: methods
format: step_by_step
---
-->

# Métodos para Integral Definida

---

## Método 1: Evaluación Directa usando TFC

**Aplicación:** Para cualquier integral donde se conoce la antiderivada.

**Pasos:**
1. Encontrar $F(x)$ tal que $F'(x) = f(x)$.
2. Calcular $F(b) - F(a)$.

**Ejemplo:**
$$\int_0^2 x^2 \, dx$$

1. $F(x) = \frac{x^3}{3}$
2. $F(2) - F(0) = \frac{8}{3} - 0 = \frac{8}{3}$

---

## Método 2: Sustitución con Cambio de Límites

**Aplicación:** Integrales que requieren sustitución $u = g(x)$.

**Pasos:**
1. Elegir $u = g(x)$.
2. Calcular $du = g'(x)dx$.
3. **Cambiar los límites:**
   - Límite inferior: $u_1 = g(a)$
   - Límite superior: $u_2 = g(b)$
4. Evaluar la nueva integral en $u$.

**Ejemplo:**
$$\int_0^1 2x(x^2+1)^3 \, dx$$

1. $u = x^2 + 1 \Rightarrow du = 2x\,dx$
2. Nuevos límites: $x = 0 \to u = 1$; $x = 1 \to u = 2$
3. $$\int_1^2 u^3 \, du = \left.\frac{u^4}{4}\right|_1^2 = \frac{16}{4} - \frac{1}{4} = \frac{15}{4}$$

---

## Método 3: Simetría para Funciones Pares

**Aplicación:** $f(-x) = f(x)$ en intervalo simétrico.

**Fórmula:**
$$\int_{-a}^{a} f(x)\,dx = 2\int_0^a f(x)\,dx$$

**Ejemplo:**
$$\int_{-1}^{1} x^4 \, dx = 2\int_0^1 x^4\,dx = 2 \cdot \frac{1}{5} = \frac{2}{5}$$

---

## Método 4: Simetría para Funciones Impares

**Aplicación:** $f(-x) = -f(x)$ en intervalo simétrico.

**Fórmula:**
$$\int_{-a}^{a} f(x)\,dx = 0$$

**Ejemplo:**
$$\int_{-2}^{2} x^3 \, dx = 0$$

---

## Método 5: Separar Parte Par e Impar

**Aplicación:** Funciones mixtas en intervalo simétrico.

**Pasos:**
1. Descomponer $f(x) = \underbrace{\frac{f(x)+f(-x)}{2}}_{\text{par}} + \underbrace{\frac{f(x)-f(-x)}{2}}_{\text{impar}}$
2. Solo la parte par contribuye.

**Ejemplo:**
$$\int_{-2}^{2} (x^3 + x^2)\,dx = \int_{-2}^2 x^3\,dx + \int_{-2}^2 x^2\,dx = 0 + 2\int_0^2 x^2\,dx = \frac{16}{3}$$

---

## Método 6: División del Intervalo

**Aplicación:** Funciones definidas por partes o con valor absoluto.

**Pasos:**
1. Identificar puntos donde cambia la definición.
2. Dividir la integral en subintervalos.
3. Sumar los resultados.

**Ejemplo:**
$$\int_0^2 |x - 1| \, dx$$

1. $|x-1|$ cambia en $x = 1$.
2. $$= \int_0^1 (1-x)\,dx + \int_1^2 (x-1)\,dx$$
3. $$= \left[x - \frac{x^2}{2}\right]_0^1 + \left[\frac{x^2}{2} - x\right]_1^2 = \frac{1}{2} + \frac{1}{2} = 1$$

---

## Método 7: Derivada de Integral con Límite Variable

**Aplicación:** Hallar $\frac{d}{dx}\int_a^{g(x)} f(t)\,dt$.

**Fórmula (Regla de Leibniz):**
$$\frac{d}{dx}\int_a^{g(x)} f(t)\,dt = f(g(x)) \cdot g'(x)$$

**Ejemplo:**
$$\frac{d}{dx}\int_0^{x^2} \cos t \, dt = \cos(x^2) \cdot 2x = 2x\cos(x^2)$$

---

## Método 8: Derivada con Ambos Límites Variables

**Aplicación:** $\frac{d}{dx}\int_{h(x)}^{g(x)} f(t)\,dt$

**Fórmula:**
$$\frac{d}{dx}\int_{h(x)}^{g(x)} f(t)\,dt = f(g(x))g'(x) - f(h(x))h'(x)$$

**Ejemplo:**
$$\frac{d}{dx}\int_x^{x^2} e^t \, dt = e^{x^2} \cdot 2x - e^x \cdot 1 = 2xe^{x^2} - e^x$$

---

## Método 9: Propiedad de Traslación

**Aplicación:** Cambio de variable lineal.

**Fórmula:**
$$\int_a^b f(x)\,dx = \int_{a-c}^{b-c} f(u+c)\,du$$

**Ejemplo:** Evaluar $\int_1^3 (x-2)^2\,dx$

Con $u = x - 2$:
$$\int_{-1}^{1} u^2\,du = 2\int_0^1 u^2\,du = \frac{2}{3}$$

---

## Método 10: Propiedad de Reflexión

**Aplicación:** Algunas integrales trigonométricas.

**Fórmula:**
$$\int_0^a f(x)\,dx = \int_0^a f(a-x)\,dx$$

**Ejemplo:** Demostrar $\int_0^{\pi/2} \sin^n x\,dx = \int_0^{\pi/2} \cos^n x\,dx$

Con $u = \frac{\pi}{2} - x$:
$$\int_0^{\pi/2} \sin^n x\,dx = \int_0^{\pi/2} \sin^n\left(\frac{\pi}{2}-u\right)\,du = \int_0^{\pi/2} \cos^n u\,du$$
