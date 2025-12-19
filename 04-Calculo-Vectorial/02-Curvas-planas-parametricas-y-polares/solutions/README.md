# Soluciones — Curvas paramétricas y polares

<!--
IA: Cada solución incluye contexto del método usado y verificación.
-->

---

## Nivel básico

### Problema 1
**Contexto**: La pendiente en curvas paramétricas se obtiene como cociente de derivadas respecto al parámetro.

**Desarrollo**:
- $\frac{dx}{dt} = 6t$, $\frac{dy}{dt} = 6t^2$
- $\frac{dy}{dx} = \frac{6t^2}{6t} = t$
- En $t = 1$: $\frac{dy}{dx} = 1$

**Respuesta**: Pendiente $= 1$

---

### Problema 2
**Contexto**: (a) Eliminamos el parámetro usando identidades; (b) usamos la fórmula de pendiente paramétrica.

**Desarrollo**:
- a) $x = 2\cos t$, $y = 2\sin t$ → $x^2 + y^2 = 4$ (círculo de radio 2)
- b) $\frac{dx}{dt} = -2\sin t$, $\frac{dy}{dt} = 2\cos t$
  - $\frac{dy}{dx} = \frac{2\cos t}{-2\sin t} = -\cot t$
  - En $t = \pi/4$: $\frac{dy}{dx} = -\cot(\pi/4) = -1$

**Respuestas**: a) $x^2 + y^2 = 4$; b) Pendiente $= -1$

---

### Problema 3
**Contexto**: Tangente horizontal cuando $\frac{dy}{dt} = 0$ y $\frac{dx}{dt} \neq 0$.

**Desarrollo**:
- $\frac{dx}{dt} = 1 \neq 0$ (siempre)
- $\frac{dy}{dt} = 2t = 0$ → $t = 0$
- Punto: $(0+1, 0-1) = (1, -1)$

**Respuesta**: Tangente horizontal en $(1, -1)$

---

### Problema 4
**Contexto**: La longitud de arco de una recta paramétrica debe coincidir con la distancia entre puntos.

**Desarrollo**:
- $x'(t) = 3$, $y'(t) = -4$
- $L = \int_0^1 \sqrt{9 + 16} \, dt = \int_0^1 5 \, dt = 5$

**Verificación**: Puntos $(2, 1)$ y $(5, -3)$; distancia $= \sqrt{9 + 16} = 5$ ✓

**Respuesta**: $L = 5$

---

### Problema 5
**Contexto**: Tangente vertical cuando $\frac{dx}{dt} = 0$ y $\frac{dy}{dt} \neq 0$.

**Desarrollo**:
- $\frac{dx}{dt} = 3t^2 - 3 = 3(t^2 - 1) = 0$ → $t = \pm 1$
- $\frac{dy}{dt} = 2t$; en $t = 1$: $\frac{dy}{dt} = 2 \neq 0$; en $t = -1$: $\frac{dy}{dt} = -2 \neq 0$
- Puntos: $t=1$: $(-2, 1)$; $t=-1$: $(2, 1)$

**Respuesta**: Tangentes verticales en $(-2, 1)$ y $(2, 1)$

---

## Nivel intermedio

### Problema 6
**Contexto**: La cicloide es la curva trazada por un punto en una rueda que rueda.

**Desarrollo**:
- a) $\frac{dx}{dt} = 1 - \cos t$, $\frac{dy}{dt} = \sin t$
  - $\frac{dy}{dx} = \frac{\sin t}{1 - \cos t}$
- b) En $t = \pi/2$: $\frac{dy}{dx} = \frac{1}{1-0} = 1$
- c) Tangente horizontal: $\sin t = 0$ → $t = 0, \pi, 2\pi, ...$
  - Pero en $t = 0, 2\pi$: $\frac{dx}{dt} = 0$ también (punto singular)
  - En $t = \pi$: $\frac{dx}{dt} = 2 \neq 0$ → tangente horizontal en $(\pi, 2)$

**Respuestas**: a) $\frac{\sin t}{1-\cos t}$; b) Pendiente $= 1$; c) En $t = \pi$, punto $(\pi, 2)$

---

### Problema 9
**Contexto**: Longitud de arco = integral de la rapidez.

**Desarrollo**:
- $x' = -\sin t$, $y' = \cos t$
- $\sqrt{(x')^2 + (y')^2} = \sqrt{\sin^2 t + \cos^2 t} = 1$
- $L = \int_0^\pi 1 \, dt = \pi$

**Respuesta**: $L = \pi$ (medio perímetro de círculo unitario)

---

### Problema 10
**Contexto**: Longitud de arco con integrando no simplificable; puede requerir sustitución.

**Desarrollo**:
- $x' = 2t$, $y' = 3t^2$
- $L = \int_0^1 \sqrt{4t^2 + 9t^4} \, dt = \int_0^1 t\sqrt{4 + 9t^2} \, dt$
- Sustitución: $u = 4 + 9t^2$, $du = 18t \, dt$
- $L = \frac{1}{18}\int_4^{13} \sqrt{u} \, du = \frac{1}{18} \cdot \frac{2}{3}u^{3/2}\Big|_4^{13} = \frac{1}{27}(13^{3/2} - 8)$

**Respuesta**: $L = \frac{13\sqrt{13} - 8}{27} \approx 1.44$

---

### Problema 12
**Contexto**: Área bajo curva paramétrica = $\int y(t) \cdot x'(t) \, dt$.

**Desarrollo**:
- $y(t) = 2t$, $x'(t) = 2t$
- $A = \int_0^2 (2t)(2t) \, dt = 4\int_0^2 t^2 \, dt = 4 \cdot \frac{8}{3} = \frac{32}{3}$

**Respuesta**: $A = \frac{32}{3}$

---

### Problema 13
**Contexto**: Área de elipse usando Green o la fórmula paramétrica para curvas cerradas.

**Desarrollo**:
$$A = \frac{1}{2}\left|\int_0^{2\pi} \left(x\frac{dy}{dt} - y\frac{dx}{dt}\right) dt\right|$$
- $x = 3\cos t$, $y = 2\sin t$, $\frac{dx}{dt} = -3\sin t$, $\frac{dy}{dt} = 2\cos t$
- $x\frac{dy}{dt} - y\frac{dx}{dt} = 6\cos^2 t + 6\sin^2 t = 6$
- $A = \frac{1}{2}\int_0^{2\pi} 6 \, dt = 6\pi$

**Respuesta**: $A = 6\pi$ (coincide con $\pi ab = \pi(3)(2)$)

---

## Polares

### Problema 14
**Contexto**: $r = 2\cos\theta$ es un círculo; el área en polares usa $\frac{1}{2}\int r^2 d\theta$.

**Desarrollo**:
- a) Es un círculo de radio 1 centrado en $(1, 0)$.
- b) $A = \frac{1}{2}\int_0^{\pi/2} 4\cos^2\theta \, d\theta = 2\int_0^{\pi/2} \frac{1+\cos 2\theta}{2} \, d\theta = \frac{\pi}{2}$

**Respuestas**: a) Círculo; b) $A = \frac{\pi}{2}$

---

### Problema 17
**Contexto**: Área de cardioide completa, integrando de $0$ a $2\pi$.

**Desarrollo**:
$$A = \frac{1}{2}\int_0^{2\pi} (1 + \cos\theta)^2 \, d\theta = \frac{1}{2}\int_0^{2\pi} (1 + 2\cos\theta + \cos^2\theta) \, d\theta$$
- $\int_0^{2\pi} 1 \, d\theta = 2\pi$
- $\int_0^{2\pi} 2\cos\theta \, d\theta = 0$
- $\int_0^{2\pi} \cos^2\theta \, d\theta = \pi$
- $A = \frac{1}{2}(2\pi + 0 + \pi) = \frac{3\pi}{2}$

**Respuesta**: $A = \frac{3\pi}{2}$

---

### Problema 18
**Contexto**: La rosa $r = 2\cos(2\theta)$ tiene 4 pétalos; un pétalo corresponde a un intervalo donde $r \geq 0$.

**Desarrollo**:
- Un pétalo está en $\theta \in [-\pi/4, \pi/4]$ donde $\cos(2\theta) \geq 0$.
$$A = \frac{1}{2}\int_{-\pi/4}^{\pi/4} 4\cos^2(2\theta) \, d\theta = 2\int_{-\pi/4}^{\pi/4} \frac{1 + \cos 4\theta}{2} \, d\theta$$
$$= \int_{-\pi/4}^{\pi/4} (1 + \cos 4\theta) \, d\theta = \left[\theta + \frac{\sin 4\theta}{4}\right]_{-\pi/4}^{\pi/4} = \frac{\pi}{2}$$

**Respuesta**: Área de un pétalo $= \frac{\pi}{2}$

---

### Problema 20
**Contexto**: Longitud de arco en polares requiere $\sqrt{r^2 + (r')^2}$.

**Desarrollo**:
- $r = 1 + \cos\theta$, $r' = -\sin\theta$
- $r^2 + (r')^2 = (1 + \cos\theta)^2 + \sin^2\theta = 2 + 2\cos\theta = 4\cos^2(\theta/2)$
- $L = \int_0^\pi 2|\cos(\theta/2)| \, d\theta = 2\int_0^\pi \cos(\theta/2) \, d\theta = 4\sin(\theta/2)\Big|_0^\pi = 4$

**Respuesta**: $L = 4$

---

### Problema 22 (Avanzado)
**Contexto**: Área entre curvas polares = diferencia de áreas individuales donde se cumple $r_1 > r_2$.

**Desarrollo**:
- Primero encontrar intersecciones: $3\cos\theta = 1 + \cos\theta$ → $\cos\theta = 1/2$ → $\theta = \pm\pi/3$
- En $[-\pi/3, \pi/3]$, $3\cos\theta > 1 + \cos\theta$
$$A = \frac{1}{2}\int_{-\pi/3}^{\pi/3} \left[(3\cos\theta)^2 - (1+\cos\theta)^2\right] d\theta$$
$$= \frac{1}{2}\int_{-\pi/3}^{\pi/3} (9\cos^2\theta - 1 - 2\cos\theta - \cos^2\theta) \, d\theta$$
$$= \frac{1}{2}\int_{-\pi/3}^{\pi/3} (8\cos^2\theta - 1 - 2\cos\theta) \, d\theta$$

Evaluando: $A = \pi$

**Respuesta**: $A = \pi$

---

### Problema 25 (Aplicación física)
**Contexto**: La rapidez es la magnitud del vector velocidad.

**Desarrollo**:
- $\mathbf{v}(t) = \langle -2\sin t, 3\cos t \rangle$
- En $t = \pi/4$: $\mathbf{v} = \langle -\sqrt{2}, \frac{3\sqrt{2}}{2} \rangle$
- Rapidez: $|\mathbf{v}| = \sqrt{2 + \frac{9}{2}} = \sqrt{\frac{13}{2}} = \frac{\sqrt{26}}{2}$

**Respuesta**: Rapidez $= \frac{\sqrt{26}}{2} \approx 2.55$ unidades/tiempo

---

<!--
IA: Al presentar soluciones, incluye siempre:
1. Contexto/método aplicado
2. Pasos claros
3. Respuesta final destacada
-->
