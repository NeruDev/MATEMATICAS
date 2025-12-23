---
type: solution
problem_id: FUN-05-PROB-67
title: "Ecuación trigonométrica cuadrática"
topic: trigonometria
subtopic: ecuaciones-trigonometricas
difficulty: intermedio
tags: [ecuaciones, identidad-pitagorica, ecuacion-cuadratica, soluciones-multiples]
created: 2025-12-22
---

# Resolver: 2sin²θ + 3cosθ = 3 en [0, 2π)

## 📋 Enunciado del Problema

**Encuentra todas las soluciones de la ecuación en el intervalo $[0, 2\pi)$:**

$$2\sin^2\theta + 3\cos\theta = 3$$

---

## 🎯 Estrategia de Solución

1. Usar la identidad pitagórica $\sin^2\theta = 1 - \cos^2\theta$ para expresar todo en términos de coseno
2. Resolver la ecuación cuadrática resultante en $\cos\theta$
3. Encontrar todos los ángulos $\theta$ en el intervalo dado

### Identidades Clave

| Identidad | Fórmula |
|-----------|---------|
| Identidad pitagórica | $\sin^2\theta + \cos^2\theta = 1$ |
| Despeje | $\sin^2\theta = 1 - \cos^2\theta$ |

---

## 📝 Desarrollo Paso a Paso

### Paso 1: Sustituir usando la identidad pitagórica

Reemplazamos $\sin^2\theta$ por $1 - \cos^2\theta$:

$$2(1 - \cos^2\theta) + 3\cos\theta = 3$$

### Paso 2: Expandir el paréntesis

$$2 - 2\cos^2\theta + 3\cos\theta = 3$$

### Paso 3: Reorganizar en forma estándar

Pasamos todos los términos al lado izquierdo:

$$-2\cos^2\theta + 3\cos\theta + 2 - 3 = 0$$

$$-2\cos^2\theta + 3\cos\theta - 1 = 0$$

Multiplicamos por $-1$ para tener el coeficiente líder positivo:

$$2\cos^2\theta - 3\cos\theta + 1 = 0$$

### Paso 4: Sustitución para ecuación cuadrática

Sea $u = \cos\theta$, entonces:

$$2u^2 - 3u + 1 = 0$$

### Paso 5: Resolver la ecuación cuadrática

**Método: Factorización**

Buscamos dos números que multiplicados den $2 \times 1 = 2$ y sumados den $-3$.

Estos números son $-2$ y $-1$.

Reescribimos el término medio:
$$2u^2 - 2u - u + 1 = 0$$

Factorizamos por agrupación:
$$2u(u - 1) - 1(u - 1) = 0$$

$$(2u - 1)(u - 1) = 0$$

### Paso 6: Encontrar los valores de u

**Caso 1:** $2u - 1 = 0$
$$u = \frac{1}{2}$$

**Caso 2:** $u - 1 = 0$
$$u = 1$$

### Paso 7: Regresar a la variable original

Ahora tenemos:
- $\cos\theta = \dfrac{1}{2}$
- $\cos\theta = 1$

### Paso 8: Encontrar todos los ángulos en [0, 2π)

**Para $\cos\theta = \dfrac{1}{2}$:**

El coseno es positivo en el primer y cuarto cuadrante.

El ángulo de referencia es $\theta_{ref} = \dfrac{\pi}{3}$ (ya que $\cos\dfrac{\pi}{3} = \dfrac{1}{2}$)

- **Primer cuadrante:** $\theta_1 = \dfrac{\pi}{3}$
- **Cuarto cuadrante:** $\theta_2 = 2\pi - \dfrac{\pi}{3} = \dfrac{5\pi}{3}$

**Para $\cos\theta = 1$:**

$$\theta_3 = 0$$

(El único ángulo en $[0, 2\pi)$ donde $\cos\theta = 1$)

---

## ✅ Resultado Final

Las soluciones de la ecuación $2\sin^2\theta + 3\cos\theta = 3$ en $[0, 2\pi)$ son:

$$\boxed{\theta = 0, \quad \theta = \frac{\pi}{3}, \quad \theta = \frac{5\pi}{3}}$$

O equivalentemente en grados: $\theta = 0°, 60°, 300°$

---

## 🔍 Verificación de Soluciones

### Verificación de θ = 0

$$2\sin^2(0) + 3\cos(0) = 2(0)^2 + 3(1) = 0 + 3 = 3 \quad ✓$$

### Verificación de θ = π/3

$$2\sin^2\left(\frac{\pi}{3}\right) + 3\cos\left(\frac{\pi}{3}\right)$$

$$= 2\left(\frac{\sqrt{3}}{2}\right)^2 + 3\left(\frac{1}{2}\right)$$

$$= 2 \cdot \frac{3}{4} + \frac{3}{2}$$

$$= \frac{3}{2} + \frac{3}{2} = 3 \quad ✓$$

### Verificación de θ = 5π/3

$$2\sin^2\left(\frac{5\pi}{3}\right) + 3\cos\left(\frac{5\pi}{3}\right)$$

$$= 2\left(-\frac{\sqrt{3}}{2}\right)^2 + 3\left(\frac{1}{2}\right)$$

$$= 2 \cdot \frac{3}{4} + \frac{3}{2}$$

$$= \frac{3}{2} + \frac{3}{2} = 3 \quad ✓$$

---

## 📊 Representación Gráfica

```
Círculo Unitario - Ubicación de Soluciones

              π/2
               |
               |
      π/3  ●   |
           \   |
            \  |
             \ |
    π --------●-------- 0 (θ = 0)
             /|
            / |
           /  |
     5π/3 ●   |
               |
              3π/2
```

---

## 📚 Notas del Método

> **Consejo:** Cuando una ecuación trigonométrica contiene tanto $\sin\theta$ como $\cos\theta$, es útil usar identidades pitagóricas para expresarla en términos de una sola función trigonométrica.

### Resumen del Proceso

| Paso | Operación |
|------|-----------|
| 1 | Sustituir $\sin^2\theta = 1 - \cos^2\theta$ |
| 2 | Obtener ecuación cuadrática en $\cos\theta$ |
| 3 | Resolver usando factorización o fórmula general |
| 4 | Verificar que $\|\cos\theta\| \leq 1$ |
| 5 | Encontrar ángulos en el intervalo dado |
| 6 | Verificar cada solución |

### Solución General (fuera del intervalo restringido)

$$\theta = 2n\pi, \quad n \in \mathbb{Z}$$
$$\theta = \frac{\pi}{3} + 2n\pi, \quad n \in \mathbb{Z}$$
$$\theta = \frac{5\pi}{3} + 2n\pi, \quad n \in \mathbb{Z}$$
