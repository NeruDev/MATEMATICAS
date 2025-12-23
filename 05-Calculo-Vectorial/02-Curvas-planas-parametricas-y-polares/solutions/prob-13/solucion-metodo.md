<!--
::METADATA::
type: solution
topic_id: cv-02-curvas-parametricas-polares
file_id: prob-13-solucion
problem_ref: Prob-13
status: stable
audience: student
-->

# Solución: Longitud de Arco de la Cicloide

## Problema

Calcular la longitud de la cicloide definida por:
$$x = t - \sin t, \quad y = 1 - \cos t$$
para $t \in [0, 2\pi]$.

---

## Conceptos clave

**Fórmula de longitud de arco para curvas paramétricas:**
$$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt$$

**Identidades trigonométricas útiles:**
$$1 - \cos t = 2\sin^2\left(\frac{t}{2}\right)$$
$$\sin t = 2\sin\left(\frac{t}{2}\right)\cos\left(\frac{t}{2}\right)$$

---

## Solución

### Paso 1: Calcular las derivadas

**Derivada de $x$:**
$$\frac{dx}{dt} = \frac{d}{dt}(t - \sin t) = 1 - \cos t$$

**Derivada de $y$:**
$$\frac{dy}{dt} = \frac{d}{dt}(1 - \cos t) = \sin t$$

### Paso 2: Calcular la suma de cuadrados

$$\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 = (1 - \cos t)^2 + \sin^2 t$$

Expandimos $(1 - \cos t)^2$:
$$= 1 - 2\cos t + \cos^2 t + \sin^2 t$$

Usando la identidad $\sin^2 t + \cos^2 t = 1$:
$$= 1 - 2\cos t + 1$$
$$= 2 - 2\cos t$$
$$= 2(1 - \cos t)$$

### Paso 3: Aplicar la identidad del ángulo mitad

Usando $1 - \cos t = 2\sin^2\left(\frac{t}{2}\right)$:

$$2(1 - \cos t) = 2 \cdot 2\sin^2\left(\frac{t}{2}\right) = 4\sin^2\left(\frac{t}{2}\right)$$

### Paso 4: Calcular la raíz cuadrada

$$\sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} = \sqrt{4\sin^2\left(\frac{t}{2}\right)}$$

$$= 2\left|\sin\left(\frac{t}{2}\right)\right|$$

Para $t \in [0, 2\pi]$, tenemos $\frac{t}{2} \in [0, \pi]$, donde $\sin\left(\frac{t}{2}\right) \geq 0$.

Por lo tanto:
$$= 2\sin\left(\frac{t}{2}\right)$$

### Paso 5: Plantear la integral de longitud

$$L = \int_0^{2\pi} 2\sin\left(\frac{t}{2}\right) \, dt$$

### Paso 6: Resolver la integral

Usamos la sustitución $u = \frac{t}{2}$, entonces $du = \frac{1}{2}dt$, es decir, $dt = 2\,du$.

Cambio de límites:
- Cuando $t = 0$: $u = 0$
- Cuando $t = 2\pi$: $u = \pi$

$$L = \int_0^{\pi} 2\sin(u) \cdot 2\,du = 4\int_0^{\pi} \sin(u) \, du$$

### Paso 7: Evaluar la integral

$$L = 4[-\cos(u)]_0^{\pi}$$

$$= 4[-\cos(\pi) - (-\cos(0))]$$

$$= 4[-(-1) + 1]$$

$$= 4[1 + 1]$$

$$= 4 \cdot 2 = 8$$

---

## Respuesta Final

$$\boxed{L = 8}$$

La longitud de un arco completo de la cicloide es exactamente **8 unidades**.

---

## Verificación y Notas

### Verificación dimensional

La cicloide tiene radio $r = 1$ (coeficiente implícito en las ecuaciones). Para una cicloide de radio $r$, la longitud de un arco es $8r$. 

Con $r = 1$: $L = 8(1) = 8$ ✓

### Interpretación geométrica

La cicloide es la curva trazada por un punto en el borde de un círculo de radio 1 que rueda sobre una línea recta. Un arco completo corresponde a una revolución completa del círculo.

- **Distancia horizontal recorrida:** $2\pi r = 2\pi$ (circunferencia del círculo)
- **Longitud del arco:** $8r = 8$ (siempre mayor que la distancia horizontal)

### Propiedad notable

La longitud de la cicloide ($8r$) es exactamente **4 veces el diámetro** del círculo generador:
$$L = 8r = 4(2r) = 4 \cdot \text{diámetro}$$

Esta es una de las propiedades clásicas de la cicloide, descubierta por Christopher Wren en 1658.

### Gráfica de la velocidad de arco

La función $\sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} = 2\sin\left(\frac{t}{2}\right)$:
- Es **cero** cuando $t = 0$ y $t = 2\pi$ (puntos cúspides)
- Alcanza su **máximo** de 2 cuando $t = \pi$ (punto más alto de la cicloide)
