# Métodos — Curvas paramétricas y polares

<!--
IA: Cada método incluye contexto, pasos detallados y ejemplo práctico.
-->

---

## Método 1: Calcular la pendiente de una curva paramétrica

### ¿Cuándo usarlo?
Cuando tienes una curva en forma paramétrica y necesitas la pendiente de la tangente en un punto específico.

### Pasos detallados
1. **Deriva** $x(t)$ para obtener $x'(t) = \frac{dx}{dt}$.
2. **Deriva** $y(t)$ para obtener $y'(t) = \frac{dy}{dt}$.
3. **Calcula la pendiente**: $\frac{dy}{dx} = \frac{y'(t)}{x'(t)}$.
4. **Evalúa** en el valor de $t$ dado.

### Ejemplo práctico
**Problema**: Para $x = 3t^2$, $y = 2t^3$, encuentra la pendiente en $t = 1$.

**Solución**:
1. $x'(t) = 6t$
2. $y'(t) = 6t^2$
3. $\frac{dy}{dx} = \frac{6t^2}{6t} = t$
4. En $t = 1$: $\frac{dy}{dx} = 1$

**Verificación**: La pendiente es 1, lo que significa una inclinación de 45° en ese punto.

---

## Método 2: Encontrar la ecuación de la recta tangente

### ¿Cuándo usarlo?
Para escribir la ecuación completa de la tangente a una curva paramétrica.

### Pasos detallados
1. **Calcula** $(x_0, y_0) = (x(t_0), y(t_0))$.
2. **Calcula** la pendiente $m = \frac{dy}{dx}\big|_{t_0}$ (usa Método 1).
3. **Escribe** la ecuación punto-pendiente: $y - y_0 = m(x - x_0)$.

### Ejemplo práctico
**Problema**: Encuentra la tangente a $x = t^2$, $y = t^3$ en $t = 2$.

**Solución**:
1. Punto: $(x_0, y_0) = (4, 8)$
2. $x' = 2t$, $y' = 3t^2$; $\frac{dy}{dx} = \frac{3t^2}{2t} = \frac{3t}{2}$. En $t=2$: $m = 3$.
3. Tangente: $y - 8 = 3(x - 4)$ → $y = 3x - 4$

**Verificación**: En $t = 2$, el punto $(4, 8)$ satisface $y = 3(4) - 4 = 8$ ✓

---

## Método 3: Calcular la longitud de arco (forma paramétrica)

### ¿Cuándo usarlo?
Para medir la longitud de una curva entre dos valores del parámetro.

### Pasos detallados
1. **Calcula** las derivadas $x'(t)$ y $y'(t)$.
2. **Forma** el integrando: $\sqrt{[x'(t)]^2 + [y'(t)]^2}$.
3. **Simplifica** si es posible (busca cuadrados perfectos).
4. **Integra** en el intervalo $[a, b]$.

### Ejemplo práctico
**Problema**: Longitud del semicírculo $x = \cos t$, $y = \sin t$, $t \in [0, \pi]$.

**Solución**:
1. $x' = -\sin t$, $y' = \cos t$
2. Integrando: $\sqrt{\sin^2 t + \cos^2 t} = \sqrt{1} = 1$
3. $L = \int_0^\pi 1 \, dt = \pi$

**Verificación**: Medio perímetro de circunferencia de radio 1 es $\pi$ ✓

---

## Método 4: Calcular el área bajo una curva paramétrica

### ¿Cuándo usarlo?
Para encontrar el área entre una curva paramétrica y el eje $x$.

### Pasos detallados
1. **Verifica** que la curva no se cruza en el intervalo.
2. **Identifica** la fórmula: $A = \int_a^b y(t) \cdot x'(t) \, dt$.
3. **Sustituye** las expresiones de $y(t)$ y $x'(t)$.
4. **Integra** y aplica valor absoluto si es necesario.

### Ejemplo práctico
**Problema**: Área bajo $x = t^2$, $y = 2t$, $t \in [0, 2]$.

**Solución**:
1. La curva es una parábola de $x = 0$ a $x = 4$.
2. $x'(t) = 2t$
3. $A = \int_0^2 (2t)(2t) \, dt = 4\int_0^2 t^2 \, dt$
4. $A = 4 \cdot \frac{t^3}{3}\Big|_0^2 = 4 \cdot \frac{8}{3} = \frac{32}{3}$

**Verificación**: En cartesianas, $y = 2\sqrt{x}$, área $= \int_0^4 2\sqrt{x} \, dx = \frac{4x^{3/2}}{3}\Big|_0^4 = \frac{32}{3}$ ✓

---

## Método 5: Graficar curvas polares

### ¿Cuándo usarlo?
Para visualizar curvas dadas en coordenadas polares.

### Pasos detallados
1. **Identifica simetrías**: prueba $f(-\theta)$, $f(\pi - \theta)$, $f(\theta + \pi)$.
2. **Encuentra ceros**: valores de $\theta$ donde $r = 0$.
3. **Calcula valores máximos/mínimos** de $r$.
4. **Construye tabla** de valores para $\theta$ representativos.
5. **Dibuja** marcando $(r, \theta)$ y conectando suavemente.

### Ejemplo práctico
**Problema**: Grafica $r = 2\cos\theta$.

**Solución**:
1. Simetría: $\cos(-\theta) = \cos\theta$ → simétrica respecto al eje polar.
2. $r = 0$ cuando $\theta = \pi/2$.
3. $r_{max} = 2$ en $\theta = 0$.
4. Tabla:

| $\theta$ | $0$ | $\pi/4$ | $\pi/2$ | $3\pi/4$ | $\pi$ |
|----------|-----|---------|---------|----------|-------|
| $r$      | 2   | $\sqrt{2}$ | 0 | $-\sqrt{2}$ | $-2$ |

5. La curva es un **círculo** de radio 1 centrado en $(1, 0)$.

---

## Método 6: Calcular área en coordenadas polares

### ¿Cuándo usarlo?
Para encontrar el área encerrada por una curva polar o entre dos curvas polares.

### Pasos detallados
1. **Determina el intervalo** $[\alpha, \beta]$ que recorre la región exactamente una vez.
2. **Aplica** la fórmula: $A = \frac{1}{2}\int_\alpha^\beta [r(\theta)]^2 \, d\theta$.
3. **Simplifica** usando identidades si hay funciones trigonométricas.
4. **Evalúa** la integral.

### Ejemplo práctico
**Problema**: Área dentro del círculo $r = 2\cos\theta$ en el primer cuadrante.

**Solución**:
1. En el primer cuadrante: $\theta \in [0, \pi/2]$.
2. $A = \frac{1}{2}\int_0^{\pi/2} (2\cos\theta)^2 \, d\theta = 2\int_0^{\pi/2} \cos^2\theta \, d\theta$
3. Usa $\cos^2\theta = \frac{1 + \cos(2\theta)}{2}$:
   $$A = 2 \cdot \frac{1}{2}\int_0^{\pi/2} (1 + \cos 2\theta) \, d\theta = \left[\theta + \frac{\sin 2\theta}{2}\right]_0^{\pi/2}$$
4. $A = \frac{\pi}{2} + 0 - 0 = \frac{\pi}{2}$

**Verificación**: El círculo completo tiene radio 1, área $\pi$. El primer cuadrante es la mitad: $\frac{\pi}{2}$ ✓

---

## Método 7: Calcular longitud de arco en polares

### ¿Cuándo usarlo?
Para medir la longitud de una curva dada en forma polar.

### Pasos detallados
1. **Calcula** $r'(\theta) = \frac{dr}{d\theta}$.
2. **Forma** el integrando: $\sqrt{r^2 + (r')^2}$.
3. **Simplifica** algebraicamente si es posible.
4. **Integra** en el intervalo $[\alpha, \beta]$.

### Ejemplo práctico
**Problema**: Longitud de la cardioide $r = 1 + \cos\theta$ para $\theta \in [0, \pi]$.

**Solución**:
1. $r' = -\sin\theta$
2. Integrando:
   $$\sqrt{(1+\cos\theta)^2 + \sin^2\theta} = \sqrt{1 + 2\cos\theta + \cos^2\theta + \sin^2\theta}$$
   $$= \sqrt{2 + 2\cos\theta} = \sqrt{2(1 + \cos\theta)}$$
3. Usa la identidad $1 + \cos\theta = 2\cos^2(\theta/2)$:
   $$= \sqrt{4\cos^2(\theta/2)} = 2|\cos(\theta/2)|$$
   En $[0, \pi]$, $\cos(\theta/2) \geq 0$, así que $= 2\cos(\theta/2)$.
4. $L = \int_0^\pi 2\cos(\theta/2) \, d\theta = 4\sin(\theta/2)\Big|_0^\pi = 4(1 - 0) = 4$

**Verificación**: La cardioide completa tiene longitud 8; la mitad es 4 ✓

---

## Método 8: Pendiente de tangente en polares

### ¿Cuándo usarlo?
Para encontrar la pendiente de la recta tangente a una curva polar.

### Pasos detallados
1. **Convierte** a paramétricas: $x = r\cos\theta$, $y = r\sin\theta$.
2. **Deriva** usando regla del producto:
   - $\frac{dx}{d\theta} = r'\cos\theta - r\sin\theta$
   - $\frac{dy}{d\theta} = r'\sin\theta + r\cos\theta$
3. **Calcula** $\frac{dy}{dx} = \frac{dy/d\theta}{dx/d\theta}$.
4. **Evalúa** en el $\theta$ dado.

### Ejemplo práctico
**Problema**: Pendiente de la tangente a $r = 1 + \sin\theta$ en $\theta = \pi/2$.

**Solución**:
1. $r = 1 + \sin\theta$, $r' = \cos\theta$
2. En $\theta = \pi/2$: $r = 2$, $r' = 0$
3. Derivadas:
   - $\frac{dx}{d\theta} = 0 \cdot 0 - 2 \cdot 1 = -2$
   - $\frac{dy}{d\theta} = 0 \cdot 1 + 2 \cdot 0 = 0$
4. $\frac{dy}{dx} = \frac{0}{-2} = 0$

**Resultado**: Tangente horizontal en $\theta = \pi/2$.

---

<!--
IA: Usa estos métodos como plantilla para resolver problemas de curvas.
Siempre verifica el resultado con un método alternativo cuando sea posible.
-->
