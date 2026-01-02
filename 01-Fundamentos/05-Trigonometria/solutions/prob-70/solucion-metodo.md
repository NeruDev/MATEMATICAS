<!--
---
type: solution
problem_id: FUN-05-PROB-70
title: "Ecuación lineal en [seno](../../../../glossary.md#seno) y [coseno](../../../../glossary.md#coseno)"
topic: trigonometria
subtopic: ecuaciones-trigonometricas
difficulty: intermedio
tags: [ecuaciones, identidad-auxiliar, soluciones-extranas, metodos-multiples]
created: 2025-12-22
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../glossary.md)

---

# Resolver: sinθ + cosθ = 1

## 📋 Enunciado del Problema

**Encuentra todas las soluciones de la ecuación:**

$$\sin\theta + \cos\theta = 1$$

---

## 🎯 Estrategia de Solución

Presentamos dos [métodos de solución](../../../../glossary.md#metodos-de-solucion):
- **Método 1:** Elevar al cuadrado ambos lados
- **Método 2:** Usar la identidad auxiliar $R\sin(\theta + \phi)$

⚠️ **Importante:** El Método 1 puede introducir soluciones extrañas que deben verificarse.

---

# 📝 Método 1: Elevar al Cuadrado

### Paso 1: Elevar ambos lados al cuadrado

$$(\sin\theta + \cos\theta)^2 = 1^2$$

### Paso 2: Expandir el binomio

$$\sin^2\theta + 2\sin\theta\cos\theta + \cos^2\theta = 1$$

### Paso 3: Aplicar identidad pitagórica

Como $\sin^2\theta + \cos^2\theta = 1$:

$$1 + 2\sin\theta\cos\theta = 1$$

### Paso 4: Simplificar

$$2\sin\theta\cos\theta = 0$$

### Paso 5: Usar identidad del ángulo doble

Recordando que $\sin(2\theta) = 2\sin\theta\cos\theta$:

$$\sin(2\theta) = 0$$

### Paso 6: Resolver para 2θ

$$2\theta = n\pi, \quad n \in \mathbb{Z}$$

$$\theta = \frac{n\pi}{2}, \quad n \in \mathbb{Z}$$

### Paso 7: Listar las soluciones candidatas

Para $n = 0, 1, 2, 3$ en $[0, 2\pi)$:

| n | θ | Valor |
|---|---|-------|
| 0 | 0 | $0$ |
| 1 | $\frac{\pi}{2}$ | $\frac{\pi}{2}$ |
| 2 | $\pi$ | $\pi$ |
| 3 | $\frac{3\pi}{2}$ | $\frac{3\pi}{2}$ |

### Paso 8: Verificar soluciones (eliminar extrañas)

**θ = 0:**
$$\sin(0) + \cos(0) = 0 + 1 = 1 \quad ✓$$

**θ = π/2:**
$$\sin\left(\frac{\pi}{2}\right) + \cos\left(\frac{\pi}{2}\right) = 1 + 0 = 1 \quad ✓$$

**θ = π:**
$$\sin(\pi) + \cos(\pi) = 0 + (-1) = -1 \neq 1 \quad ✗ \text{ (Solución extraña)}$$

**θ = 3π/2:**
$$\sin\left(\frac{3\pi}{2}\right) + \cos\left(\frac{3\pi}{2}\right) = -1 + 0 = -1 \neq 1 \quad ✗ \text{ (Solución extraña)}$$

> ⚠️ **Las soluciones $\theta = \pi$ y $\theta = \frac{3\pi}{2}$ son extrañas**, introducidas al elevar al cuadrado. Corresponden a $\sin\theta + \cos\theta = -1$.

---

# 📝 Método 2: Identidad Auxiliar R·sin(θ + φ)

### Paso 1: Forma general de la identidad auxiliar

Para una expresión de la forma $a\sin\theta + b\cos\theta$, podemos escribirla como:

$$a\sin\theta + b\cos\theta = R\sin(\theta + \phi)$$

donde:
- $R = \sqrt{a^2 + b^2}$
- $\tan\phi = \dfrac{b}{a}$

### Paso 2: Identificar coeficientes

En nuestra ecuación $\sin\theta + \cos\theta = 1$:
- $a = 1$ (coeficiente de $\sin\theta$)
- $b = 1$ (coeficiente de $\cos\theta$)

### Paso 3: Calcular R

$$R = \sqrt{1^2 + 1^2} = \sqrt{2}$$

### Paso 4: Calcular φ

$$\tan\phi = \frac{b}{a} = \frac{1}{1} = 1$$

$$\phi = \frac{\pi}{4}$$

### Paso 5: Reescribir la ecuación

$$\sin\theta + \cos\theta = \sqrt{2}\sin\left(\theta + \frac{\pi}{4}\right)$$

La ecuación original se convierte en:

$$\sqrt{2}\sin\left(\theta + \frac{\pi}{4}\right) = 1$$

### Paso 6: Despejar el seno

$$\sin\left(\theta + \frac{\pi}{4}\right) = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}$$

### Paso 7: Resolver para (θ + π/4)

El [seno](../../../../glossary.md#seno) vale $\frac{\sqrt{2}}{2}$ cuando el argumento es:

$$\theta + \frac{\pi}{4} = \frac{\pi}{4} + 2n\pi \quad \text{o} \quad \theta + \frac{\pi}{4} = \pi - \frac{\pi}{4} + 2n\pi$$

### Paso 8: Despejar θ

**Primera familia:**
$$\theta = \frac{\pi}{4} - \frac{\pi}{4} + 2n\pi = 2n\pi$$

**Segunda familia:**
$$\theta = \frac{3\pi}{4} - \frac{\pi}{4} + 2n\pi = \frac{\pi}{2} + 2n\pi$$

### Paso 9: Soluciones en [0, 2π)

- De $\theta = 2n\pi$: $\theta = 0$
- De $\theta = \frac{\pi}{2} + 2n\pi$: $\theta = \frac{\pi}{2}$

---

## ✅ Resultado Final

Las soluciones de $\sin\theta + \cos\theta = 1$ en $[0, 2\pi)$ son:

$$\boxed{\theta = 0 \quad \text{y} \quad \theta = \frac{\pi}{2}}$$

### Solución General

$$\boxed{\theta = 2n\pi \quad \text{o} \quad \theta = \frac{\pi}{2} + 2n\pi, \quad n \in \mathbb{Z}}$$

---

## 🔍 Verificación Final

### Para θ = 0:
$$\sin(0) + \cos(0) = 0 + 1 = 1 \quad ✓$$

### Para θ = π/2:
$$\sin\left(\frac{\pi}{2}\right) + \cos\left(\frac{\pi}{2}\right) = 1 + 0 = 1 \quad ✓$$

---

## 📊 Comparación de Métodos

| Aspecto | Método 1 (Cuadrado) | Método 2 (R·sin(θ+φ)) |
|---------|---------------------|----------------------|
| Dificultad | [Menor](../../../../glossary.md#menor) | Mayor |
| Soluciones extrañas | Sí, requiere verificar | No |
| Generalizable | Limitado | Muy general |
| Errores comunes | Olvidar verificar | Cálculo de φ |

---

## ⚠️ Análisis de Soluciones Extrañas

### ¿Por qué aparecen soluciones extrañas en el Método 1?

Al elevar al cuadrado, la ecuación $\sin\theta + \cos\theta = 1$ y $\sin\theta + \cos\theta = -1$ producen el mismo resultado:

$$(\sin\theta + \cos\theta)^2 = 1 \quad \Leftrightarrow \quad \sin\theta + \cos\theta = \pm 1$$

Las soluciones de $\sin\theta + \cos\theta = -1$ son:
- $\theta = \pi$ donde $\sin\pi + \cos\pi = 0 - 1 = -1$
- $\theta = \frac{3\pi}{2}$ donde $\sin\frac{3\pi}{2} + \cos\frac{3\pi}{2} = -1 + 0 = -1$

> **Regla:** Siempre que se eleva al cuadrado una ecuación, se debe verificar cada solución en la ecuación original.

---

## 📚 Derivación de la Identidad Auxiliar

Para demostrar que $a\sin\theta + b\cos\theta = R\sin(\theta + \phi)$:

Expandimos el lado derecho:
$$R\sin(\theta + \phi) = R[\sin\theta\cos\phi + \cos\theta\sin\phi]$$

$$= (R\cos\phi)\sin\theta + (R\sin\phi)\cos\theta$$

Comparando coeficientes:
- $a = R\cos\phi$
- $b = R\sin\phi$

Por tanto:
$$a^2 + b^2 = R^2\cos^2\phi + R^2\sin^2\phi = R^2$$

$$R = \sqrt{a^2 + b^2}$$

Y:
$$\frac{b}{a} = \frac{R\sin\phi}{R\cos\phi} = \tan\phi$$
