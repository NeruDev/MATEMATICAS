# Teoría — Curvas paramétricas y polares

---

## 2.1 Ecuaciones paramétricas de curvas planas

### Concepto fundamental
Una **curva paramétrica** en el plano se define mediante dos funciones:
$$x = x(t), \quad y = y(t), \quad t \in [a, b]$$

El parámetro $t$ (frecuentemente el tiempo) "recorre" la curva generando puntos $(x(t), y(t))$.

### Ventajas de la forma paramétrica
- Permite describir curvas que no son funciones (como circunferencias completas).
- Natural para describir movimiento: $t$ representa el tiempo.
- Facilita el cálculo de velocidad y aceleración.

### Curvas paramétricas clásicas

| Curva | Ecuaciones paramétricas | Dominio típico |
|-------|------------------------|----------------|
| Circunferencia | $x = r\cos t$, $y = r\sin t$ | $[0, 2\pi]$ |
| Elipse | $x = a\cos t$, $y = b\sin t$ | $[0, 2\pi]$ |
| Cicloide | $x = r(t - \sin t)$, $y = r(1 - \cos t)$ | $[0, 2\pi]$ |
| Curva de Lissajous | $x = A\sin(at + \delta)$, $y = B\sin(bt)$ | $[0, 2\pi]$ |
| Astroide | $x = a\cos^3 t$, $y = a\sin^3 t$ | $[0, 2\pi]$ |

### Orientación
La **orientación** de la curva es la dirección en que se recorre al aumentar $t$. Esto es importante para integrales de línea.

### Eliminación del parámetro
A veces podemos eliminar $t$ para obtener una ecuación cartesiana:
- Ejemplo: $x = \cos t$, $y = \sin t$ → $x^2 + y^2 = 1$

---

## 2.2 Derivada de una curva en forma paramétrica

### Derivada primera (pendiente)
Si $x = x(t)$ y $y = y(t)$ son diferenciables y $\frac{dx}{dt} \neq 0$:
$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{y'(t)}{x'(t)}$$

**Interpretación**: Es la pendiente de la recta tangente a la curva en el punto correspondiente a $t$.

### Derivada segunda (concavidad)
$$\frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{dy}{dx}\right) = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{dx/dt}$$

Expandiendo:
$$\frac{d^2y}{dx^2} = \frac{x'(t)y''(t) - y'(t)x''(t)}{[x'(t)]^3}$$

### Vector velocidad y aceleración
- **Posición**: $\mathbf{r}(t) = \langle x(t), y(t) \rangle$
- **Velocidad**: $\mathbf{v}(t) = \mathbf{r}'(t) = \langle x'(t), y'(t) \rangle$
- **Rapidez**: $|\mathbf{v}(t)| = \sqrt{[x'(t)]^2 + [y'(t)]^2}$
- **Aceleración**: $\mathbf{a}(t) = \mathbf{v}'(t) = \langle x''(t), y''(t) \rangle$

---

## 2.3 Tangentes a una curva

### Recta tangente
En el punto $(x_0, y_0) = (x(t_0), y(t_0))$, la ecuación de la tangente es:
$$y - y_0 = \frac{dy}{dx}\bigg|_{t_0} (x - x_0)$$

### Recta normal
Perpendicular a la tangente en el mismo punto:
$$y - y_0 = -\frac{1}{dy/dx}\bigg|_{t_0} (x - x_0)$$

(si $dy/dx \neq 0$)

### Casos especiales
- **Tangente horizontal**: cuando $\frac{dy}{dt} = 0$ y $\frac{dx}{dt} \neq 0$.
- **Tangente vertical**: cuando $\frac{dx}{dt} = 0$ y $\frac{dy}{dt} \neq 0$.
- **Punto singular**: cuando $\frac{dx}{dt} = \frac{dy}{dt} = 0$ (requiere análisis más detallado).

---

## 2.4 Área y longitud de arco

### Longitud de arco (forma paramétrica)
$$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt = \int_a^b |\mathbf{v}(t)| \, dt$$

**Interpretación**: Integramos la rapidez para obtener la distancia recorrida.

### Función longitud de arco
$$s(t) = \int_{t_0}^t \sqrt{[x'(u)]^2 + [y'(u)]^2} \, du$$

$s(t)$ mide la longitud desde $t_0$ hasta $t$.

### Área bajo una curva paramétrica
Si la curva no se cruza a sí misma y $x(t)$ es creciente en $[a, b]$:
$$A = \int_a^b y(t) \cdot x'(t) \, dt$$

**Nota**: El signo depende de la orientación. Si $x$ decrece, usar valor absoluto o cambiar límites.

### Área encerrada por una curva cerrada (fórmula de Green)
$$A = \frac{1}{2} \left| \int_a^b \left( x \frac{dy}{dt} - y \frac{dx}{dt} \right) dt \right|$$

---

## 2.5 Curvas planas en coordenadas polares

### Sistema de coordenadas polares
Un punto se describe por $(r, \theta)$:
- $r$: distancia al origen (polo)
- $\theta$: ángulo desde el eje polar (eje $x$ positivo)

### Conversión entre sistemas
| Polar → Cartesiano | Cartesiano → Polar |
|-------------------|-------------------|
| $x = r\cos\theta$ | $r = \sqrt{x^2 + y^2}$ |
| $y = r\sin\theta$ | $\theta = \arctan(y/x)$ (ajustar cuadrante) |

### Curvas polares
Una curva polar se define como $r = f(\theta)$.

### Curvas polares clásicas

| Curva | Ecuación | Característica |
|-------|----------|----------------|
| Circunferencia | $r = a$ | Radio constante |
| Recta por origen | $\theta = c$ | Ángulo constante |
| Cardioide | $r = a(1 + \cos\theta)$ | Forma de corazón |
| Limaçon | $r = a + b\cos\theta$ | Varía según $a/b$ |
| Rosa de $n$ pétalos | $r = a\cos(n\theta)$ | $n$ o $2n$ pétalos |
| Espiral de Arquímedes | $r = a\theta$ | Crece linealmente |
| Lemniscata | $r^2 = a^2\cos(2\theta)$ | Forma de $\infty$ |

### Simetrías en polares
- **Eje polar** (eje $x$): Si $f(-\theta) = f(\theta)$.
- **Eje $\theta = \pi/2$** (eje $y$): Si $f(\pi - \theta) = f(\theta)$.
- **Origen**: Si $f(\theta + \pi) = f(\theta)$ o $f(-\theta) = -f(\theta)$.

---

## 2.6 Cálculo en coordenadas polares

### Pendiente de la tangente en polares
Convertimos a paramétricas con $\theta$ como parámetro:
$$x = r(\theta)\cos\theta, \quad y = r(\theta)\sin\theta$$

$$\frac{dy}{dx} = \frac{dy/d\theta}{dx/d\theta} = \frac{r'\sin\theta + r\cos\theta}{r'\cos\theta - r\sin\theta}$$

### Área en coordenadas polares
El área encerrada por $r = f(\theta)$ desde $\theta = \alpha$ hasta $\theta = \beta$:
$$A = \frac{1}{2} \int_\alpha^\beta [r(\theta)]^2 \, d\theta$$

**Derivación**: El área de un sector circular es $\frac{1}{2}r^2 \Delta\theta$; integramos estos sectores infinitesimales.

### Área entre dos curvas polares
Si $r_1(\theta) \leq r_2(\theta)$ en $[\alpha, \beta]$:
$$A = \frac{1}{2} \int_\alpha^\beta \left( [r_2(\theta)]^2 - [r_1(\theta)]^2 \right) d\theta$$

### Longitud de arco en polares
$$L = \int_\alpha^\beta \sqrt{[r(\theta)]^2 + [r'(\theta)]^2} \, d\theta$$

**Derivación**: Sustituir $x = r\cos\theta$, $y = r\sin\theta$ en la fórmula paramétrica y simplificar.

---

<!--
IA: Esta teoría cubre los 6 subtemas del temario.
Al explicar, usa ejemplos visuales (cardioide, rosa) para anclar conceptos.
-->
