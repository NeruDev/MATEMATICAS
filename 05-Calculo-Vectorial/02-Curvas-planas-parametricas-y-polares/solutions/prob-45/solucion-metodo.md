<!--
::METADATA::
type: solution
topic_id: cv-02-curvas-parametricas-polares
file_id: prob-45-solucion
problem_ref: Prob-45
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../glossary.md)

---

# Solución: Longitud de Arco de la Cardioide

## Problema

Calcular la longitud de la cardioide:
$$r = 1 + \cos\theta$$

---

## Conceptos clave

**Fórmula de longitud de arco en coordenadas polares:**
$$L = \int_{\alpha}^{\beta} \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2} \, d\theta$$

**Identidades trigonométricas útiles:**
$$1 + \cos\theta = 2\cos^2\left(\frac{\theta}{2}\right)$$
$$\sin^2\theta + \cos^2\theta = 1$$
$$\sin\theta = 2\sin\left(\frac{\theta}{2}\right)\cos\left(\frac{\theta}{2}\right)$$

---

## Solución

### Paso 1: Calcular la derivada $\frac{dr}{d\theta}$

$$r = 1 + \cos\theta$$

$$\frac{dr}{d\theta} = -\sin\theta$$

### Paso 2: Calcular $r^2 + \left(\frac{dr}{d\theta}\right)^2$

$$r^2 = (1 + \cos\theta)^2 = 1 + 2\cos\theta + \cos^2\theta$$

$$\left(\frac{dr}{d\theta}\right)^2 = (-\sin\theta)^2 = \sin^2\theta$$

Sumando:
$$r^2 + \left(\frac{dr}{d\theta}\right)^2 = 1 + 2\cos\theta + \cos^2\theta + \sin^2\theta$$

Usando $\sin^2\theta + \cos^2\theta = 1$:
$$= 1 + 2\cos\theta + 1 = 2 + 2\cos\theta = 2(1 + \cos\theta)$$

### Paso 3: Aplicar la identidad del ángulo mitad

Usando $1 + \cos\theta = 2\cos^2\left(\frac{\theta}{2}\right)$:

$$2(1 + \cos\theta) = 2 \cdot 2\cos^2\left(\frac{\theta}{2}\right) = 4\cos^2\left(\frac{\theta}{2}\right)$$

### Paso 4: Calcular la raíz cuadrada

$$\sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2} = \sqrt{4\cos^2\left(\frac{\theta}{2}\right)} = 2\left|\cos\left(\frac{\theta}{2}\right)\right|$$

### Paso 5: Analizar el valor absoluto

Para $\theta \in [0, 2\pi]$:
- $\frac{\theta}{2} \in [0, \pi]$
- En $[0, \frac{\pi}{2}]$: $\cos\left(\frac{\theta}{2}\right) \geq 0$
- En $[\frac{\pi}{2}, \pi]$: $\cos\left(\frac{\theta}{2}\right) \leq 0$

Esto corresponde a:
- $\theta \in [0, \pi]$: $\cos\left(\frac{\theta}{2}\right) \geq 0$
- $\theta \in [\pi, 2\pi]$: $\cos\left(\frac{\theta}{2}\right) \leq 0$

### Paso 6: Usar simetría para simplificar

Por la simetría de la cardioide respecto al eje polar, calculamos la longitud de $\theta \in [0, \pi]$ y duplicamos:

$$L = 2\int_0^{\pi} 2\cos\left(\frac{\theta}{2}\right) \, d\theta = 4\int_0^{\pi} \cos\left(\frac{\theta}{2}\right) \, d\theta$$

### Paso 7: Resolver la integral

Usamos la [sustitución](../../../../glossary.md#sustitucion) $u = \frac{\theta}{2}$, entonces $du = \frac{1}{2}d\theta$, es decir, $d\theta = 2\,du$.

Cambio de [límites](../../../../glossary.md#limites):
- Cuando $\theta = 0$: $u = 0$
- Cuando $\theta = \pi$: $u = \frac{\pi}{2}$

$$L = 4\int_0^{\pi/2} \cos(u) \cdot 2\,du = 8\int_0^{\pi/2} \cos(u) \, du$$

### Paso 8: Evaluar la integral

$$L = 8[\sin(u)]_0^{\pi/2}$$

$$= 8\left[\sin\left(\frac{\pi}{2}\right) - \sin(0)\right]$$

$$= 8[1 - 0]$$

$$= 8$$

---

## Respuesta Final

$$\boxed{L = 8}$$

La longitud total de la cardioide $r = 1 + \cos\theta$ es exactamente **8 unidades**.

---

## Verificación

### Método alternativo: Integral directa con valor absoluto

$$L = \int_0^{2\pi} 2\left|\cos\left(\frac{\theta}{2}\right)\right| \, d\theta$$

Dividiendo en dos intervalos:

$$L = \int_0^{\pi} 2\cos\left(\frac{\theta}{2}\right) \, d\theta + \int_{\pi}^{2\pi} 2\left(-\cos\left(\frac{\theta}{2}\right)\right) \, d\theta$$

$$= 2\left[2\sin\left(\frac{\theta}{2}\right)\right]_0^{\pi} - 2\left[2\sin\left(\frac{\theta}{2}\right)\right]_{\pi}^{2\pi}$$

$$= 4\left[\sin\left(\frac{\pi}{2}\right) - \sin(0)\right] - 4\left[\sin(\pi) - \sin\left(\frac{\pi}{2}\right)\right]$$

$$= 4[1 - 0] - 4[0 - 1]$$

$$= 4 + 4 = 8 \checkmark$$

### Fórmula general para cardioides

Para la cardioide general $r = a(1 + \cos\theta)$, la longitud es:
$$L = 8a$$

En nuestro caso, $a = 1$, confirmando $L = 8$.

### Comparación con otras curvas

| Curva | Ecuación | Longitud |
|-------|----------|----------|
| Cardioide | $r = a(1 + \cos\theta)$ | $8a$ |
| Círculo | $r = a$ | $2\pi a$ |
| Cicloide (un arco) | $x = a(t - \sin t)$, $y = a(1 - \cos t)$ | $8a$ |

**Notable:** La cardioide y la cicloide (con el mismo parámetro $a$) tienen exactamente la misma longitud.

### Interpretación geométrica

La cardioide es la **epicicloide** generada cuando un círculo de radio $a$ rueda alrededor del exterior de otro círculo de radio $a$. El punto trazador está en la circunferencia del círculo móvil.

La propiedad de que su longitud sea $8a$ (exactamente 4 veces el diámetro del círculo generador) es análoga a la propiedad de la cicloide, lo cual tiene sentido ya que ambas son curvas cicloidales.
