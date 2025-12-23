---
type: solution
problem-id: CD-02-37
topic: Derivadas
subtopic: Derivación implícita
difficulty: avanzado
tags: [derivada, implícita, folio-descartes, curvas-algebraicas, pendiente]
created: 2024-12-22
---

# Solución: Pendiente del Folio de Descartes en (3,3)

## Problema

Para la curva $x^3 + y^3 = 6xy$ (Folio de Descartes), encontrar la pendiente de la recta tangente en el punto $(3, 3)$.

---

## Método de Solución: Derivación implícita

### Paso 1: Verificar que el punto pertenece a la curva

Sustituimos $(3, 3)$ en la ecuación:
$$3^3 + 3^3 = 6(3)(3)$$
$$27 + 27 = 54$$
$$54 = 54 \checkmark$$

El punto $(3, 3)$ sí pertenece a la curva.

### Paso 2: Derivar implícitamente ambos lados respecto a x

Partimos de:
$$x^3 + y^3 = 6xy$$

**Derivada del lado izquierdo:**
$$\frac{d}{dx}[x^3 + y^3] = \frac{d}{dx}[x^3] + \frac{d}{dx}[y^3]$$

- $\dfrac{d}{dx}[x^3] = 3x^2$
- $\dfrac{d}{dx}[y^3] = 3y^2 \cdot \dfrac{dy}{dx}$ (regla de la cadena)

$$= 3x^2 + 3y^2 \frac{dy}{dx}$$

**Derivada del lado derecho (regla del producto):**
$$\frac{d}{dx}[6xy] = 6\frac{d}{dx}[xy] = 6\left[ x\frac{dy}{dx} + y \cdot 1 \right] = 6x\frac{dy}{dx} + 6y$$

### Paso 3: Igualar las derivadas

$$3x^2 + 3y^2 \frac{dy}{dx} = 6x\frac{dy}{dx} + 6y$$

### Paso 4: Despejar dy/dx

Agrupamos los términos con $\dfrac{dy}{dx}$ en un lado:

$$3y^2 \frac{dy}{dx} - 6x\frac{dy}{dx} = 6y - 3x^2$$

Factorizamos $\dfrac{dy}{dx}$:

$$\frac{dy}{dx}(3y^2 - 6x) = 6y - 3x^2$$

Despejamos:

$$\frac{dy}{dx} = \frac{6y - 3x^2}{3y^2 - 6x}$$

### Paso 5: Simplificar la expresión

Factorizamos 3 en numerador y denominador:

$$\frac{dy}{dx} = \frac{3(2y - x^2)}{3(y^2 - 2x)} = \frac{2y - x^2}{y^2 - 2x}$$

### Paso 6: Evaluar en el punto (3, 3)

$$\left.\frac{dy}{dx}\right|_{(3,3)} = \frac{2(3) - (3)^2}{(3)^2 - 2(3)}$$

$$= \frac{6 - 9}{9 - 6} = \frac{-3}{3} = -1$$

---

## Respuesta

$$\boxed{m = \frac{dy}{dx}\bigg|_{(3,3)} = -1}$$

---

## Verificación

### Método 1: Verificación por simetría

El Folio de Descartes $x^3 + y^3 = 6xy$ es simétrico respecto a la recta $y = x$.

El punto $(3, 3)$ está **sobre** la línea de simetría $y = x$.

Por simetría, la tangente en un punto sobre $y = x$ debe ser perpendicular a esta línea, lo que significa que tiene pendiente $m = -1$. ✓

### Método 2: Verificación paramétrica

El Folio de Descartes se puede parametrizar como:
$$x = \frac{6t}{1+t^3}, \quad y = \frac{6t^2}{1+t^3}$$

Para el punto $(3, 3)$: $t = 1$ (verificable: $x = y = \frac{6}{2} = 3$)

Calculando $\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}$:

$$\frac{dx}{dt} = \frac{6(1+t^3) - 6t(3t^2)}{(1+t^3)^2} = \frac{6 - 12t^3}{(1+t^3)^2}$$

$$\frac{dy}{dt} = \frac{12t(1+t^3) - 6t^2(3t^2)}{(1+t^3)^2} = \frac{12t - 6t^4}{(1+t^3)^2}$$

En $t = 1$:
$$\frac{dx}{dt}\bigg|_{t=1} = \frac{6 - 12}{4} = \frac{-6}{4} = -\frac{3}{2}$$

$$\frac{dy}{dt}\bigg|_{t=1} = \frac{12 - 6}{4} = \frac{6}{4} = \frac{3}{2}$$

$$\frac{dy}{dx} = \frac{3/2}{-3/2} = -1 \checkmark$$

---

## Información adicional sobre el Folio de Descartes

### Gráfica de la curva

```
        y
        ↑
        │    ╱
        │   ╱
        │  ●(3,3)
        │ ╱╲
        │╱  ╲
   ─────●────→ x
       ╱│    asíntota: x + y + 2 = 0
      ╱ │
```

### Características del Folio:
- **Asíntota**: $x + y + 2 = 0$
- **Punto doble**: origen $(0, 0)$
- **Simetría**: respecto a la recta $y = x$
- **Lazo**: en el primer cuadrante

---

## Ecuación de la recta tangente

Con $m = -1$ y punto $(3, 3)$:

$$y - 3 = -1(x - 3)$$
$$y = -x + 6$$

O en forma general:
$$\boxed{x + y = 6}$$
