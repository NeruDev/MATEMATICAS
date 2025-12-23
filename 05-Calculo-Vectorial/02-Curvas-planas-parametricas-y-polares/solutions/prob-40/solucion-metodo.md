<!--
::METADATA::
type: solution
topic_id: cv-02-curvas-parametricas-polares
file_id: prob-40-solucion
problem_ref: Prob-40
status: stable
audience: student
-->

# Solución: Área Encerrada por la Cardioide

## Problema

Calcular el área encerrada por la cardioide:
$$r = 1 + \cos\theta$$

---

## Conceptos clave

**Fórmula de área en coordenadas polares:**
$$A = \frac{1}{2}\int_{\alpha}^{\beta} r^2 \, d\theta$$

**Identidades trigonométricas útiles:**
$$\cos^2\theta = \frac{1 + \cos(2\theta)}{2}$$
$$\cos(2\theta) = 2\cos^2\theta - 1$$

---

## Solución

### Paso 1: Determinar los límites de integración

La cardioide $r = 1 + \cos\theta$ es una curva cerrada que se traza completamente cuando $\theta$ varía de $0$ a $2\pi$.

- Cuando $\theta = 0$: $r = 1 + 1 = 2$ (punto más alejado del origen)
- Cuando $\theta = \pi$: $r = 1 + (-1) = 0$ (cúspide en el origen)
- Cuando $\theta = 2\pi$: $r = 1 + 1 = 2$ (regresa al punto inicial)

Por lo tanto, $\theta \in [0, 2\pi]$.

### Paso 2: Plantear la integral de área

$$A = \frac{1}{2}\int_0^{2\pi} (1 + \cos\theta)^2 \, d\theta$$

### Paso 3: Expandir el binomio $(1 + \cos\theta)^2$

$$(1 + \cos\theta)^2 = 1 + 2\cos\theta + \cos^2\theta$$

### Paso 4: Aplicar la identidad del ángulo doble para $\cos^2\theta$

$$\cos^2\theta = \frac{1 + \cos(2\theta)}{2}$$

Sustituyendo:
$$1 + 2\cos\theta + \cos^2\theta = 1 + 2\cos\theta + \frac{1 + \cos(2\theta)}{2}$$

$$= 1 + 2\cos\theta + \frac{1}{2} + \frac{\cos(2\theta)}{2}$$

$$= \frac{3}{2} + 2\cos\theta + \frac{\cos(2\theta)}{2}$$

### Paso 5: Escribir la integral expandida

$$A = \frac{1}{2}\int_0^{2\pi} \left(\frac{3}{2} + 2\cos\theta + \frac{\cos(2\theta)}{2}\right) d\theta$$

### Paso 6: Separar en tres integrales

$$A = \frac{1}{2}\left[\int_0^{2\pi} \frac{3}{2} \, d\theta + \int_0^{2\pi} 2\cos\theta \, d\theta + \int_0^{2\pi} \frac{\cos(2\theta)}{2} \, d\theta\right]$$

### Paso 7: Evaluar cada integral

**Integral 1:** Constante
$$\int_0^{2\pi} \frac{3}{2} \, d\theta = \frac{3}{2}[\theta]_0^{2\pi} = \frac{3}{2}(2\pi - 0) = 3\pi$$

**Integral 2:** Coseno sobre período completo
$$\int_0^{2\pi} 2\cos\theta \, d\theta = 2[\sin\theta]_0^{2\pi} = 2(\sin 2\pi - \sin 0) = 2(0 - 0) = 0$$

**Integral 3:** Coseno de ángulo doble sobre período completo
$$\int_0^{2\pi} \frac{\cos(2\theta)}{2} \, d\theta = \frac{1}{2} \cdot \frac{1}{2}[\sin(2\theta)]_0^{2\pi}$$

$$= \frac{1}{4}[\sin(4\pi) - \sin(0)] = \frac{1}{4}(0 - 0) = 0$$

### Paso 8: Sumar los resultados

$$A = \frac{1}{2}[3\pi + 0 + 0] = \frac{1}{2} \cdot 3\pi = \frac{3\pi}{2}$$

---

## Respuesta Final

$$\boxed{A = \frac{3\pi}{2}}$$

El área encerrada por la cardioide $r = 1 + \cos\theta$ es $\frac{3\pi}{2}$ unidades cuadradas.

---

## Verificación y Notas

### Verificación por simetría

La cardioide es simétrica respecto al eje polar (eje $x$). Podemos calcular el área de la mitad superior y duplicar:

$$A = 2 \cdot \frac{1}{2}\int_0^{\pi} (1 + \cos\theta)^2 \, d\theta = \int_0^{\pi} (1 + \cos\theta)^2 \, d\theta$$

$$= \int_0^{\pi} \left(\frac{3}{2} + 2\cos\theta + \frac{\cos(2\theta)}{2}\right) d\theta$$

$$= \left[\frac{3\theta}{2} + 2\sin\theta + \frac{\sin(2\theta)}{4}\right]_0^{\pi}$$

$$= \left(\frac{3\pi}{2} + 2\sin\pi + \frac{\sin(2\pi)}{4}\right) - \left(0 + 0 + 0\right)$$

$$= \frac{3\pi}{2} + 0 + 0 = \frac{3\pi}{2} \checkmark$$

### Comparación con el círculo

Para un círculo de radio $a$: $A_{círculo} = \pi a^2$

La cardioide $r = 1 + \cos\theta$ tiene:
- Radio máximo: $r_{max} = 2$ (cuando $\theta = 0$)
- Si comparamos con un círculo de radio 2: $A_{círculo} = 4\pi$
- El área de la cardioide es $\frac{3\pi}{2} = \frac{3}{8} \cdot 4\pi$

La cardioide ocupa **3/8** del área de su círculo circunscrito.

### Fórmula general para cardioides

Para la cardioide general $r = a(1 + \cos\theta)$, el área es:
$$A = \frac{3\pi a^2}{2}$$

En nuestro caso, $a = 1$, confirmando $A = \frac{3\pi}{2}$.

### Interpretación geométrica

La cardioide ("forma de corazón" en griego) es el lugar geométrico de un punto en la circunferencia de un círculo de radio $a$ que rueda alrededor de otro círculo fijo del mismo radio.
