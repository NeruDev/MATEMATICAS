<!--
---
type: solution
problem_id: FUN-05-PROB-57
title: "Demostración de la identidad del [coseno](../../../../glossary.md#coseno) del ángulo triple"
topic: trigonometria
subtopic: identidades-trigonometricas
difficulty: intermedio
tags: [identidades, angulo-triple, demostracion, coseno]
created: 2025-12-22
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Demostración: cos(3θ) = 4cos³θ - 3cosθ

## 📋 Enunciado del Problema

**Demuestra la siguiente [identidad trigonométrica](../../../../glossary.md#identidad-trigonometrica):**

$$\cos(3\theta) = 4\cos^3\theta - 3\cos\theta$$

---

## 🎯 Estrategia de Solución

Utilizaremos las **identidades de suma de ángulos** y la **identidad del ángulo doble** para expandir $\cos(3\theta)$ expresándolo como $\cos(2\theta + \theta)$.

### Identidades Clave a Utilizar

| Identidad | Fórmula |
|-----------|---------|
| [Coseno](../../../../glossary.md#coseno) de suma | $\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$ |
| Coseno del ángulo doble | $\cos(2\theta) = 2\cos^2\theta - 1$ |
| [Seno](../../../../glossary.md#seno) del ángulo doble | $\sin(2\theta) = 2\sin\theta\cos\theta$ |
| Identidad pitagórica | $\sin^2\theta + \cos^2\theta = 1$ |

---

## 📝 Desarrollo Paso a Paso

### Paso 1: Expresar 3θ como suma de ángulos

Escribimos el ángulo triple como la suma de un ángulo doble más el ángulo simple:

$$\cos(3\theta) = \cos(2\theta + \theta)$$

### Paso 2: Aplicar la identidad del coseno de la suma

Usando $\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$ con $\alpha = 2\theta$ y $\beta = \theta$:

$$\cos(3\theta) = \cos(2\theta)\cos(\theta) - \sin(2\theta)\sin(\theta)$$

### Paso 3: Sustituir las identidades del ángulo doble

Reemplazamos $\cos(2\theta) = 2\cos^2\theta - 1$ y $\sin(2\theta) = 2\sin\theta\cos\theta$:

$$\cos(3\theta) = (2\cos^2\theta - 1)\cos\theta - (2\sin\theta\cos\theta)\sin\theta$$

### Paso 4: Expandir los productos

Distribuimos los términos:

$$\cos(3\theta) = 2\cos^3\theta - \cos\theta - 2\sin^2\theta\cos\theta$$

### Paso 5: Factorizar el coseno

Factorizamos $\cos\theta$ en los dos últimos términos:

$$\cos(3\theta) = 2\cos^3\theta - \cos\theta(1 + 2\sin^2\theta)$$

### Paso 6: Aplicar la identidad pitagórica

De $\sin^2\theta + \cos^2\theta = 1$, despejamos $\sin^2\theta = 1 - \cos^2\theta$:

$$\cos(3\theta) = 2\cos^3\theta - \cos\theta(1 + 2(1 - \cos^2\theta))$$

### Paso 7: Simplificar dentro del paréntesis

Expandimos y simplificamos:

$$\cos(3\theta) = 2\cos^3\theta - \cos\theta(1 + 2 - 2\cos^2\theta)$$

$$\cos(3\theta) = 2\cos^3\theta - \cos\theta(3 - 2\cos^2\theta)$$

### Paso 8: Distribuir el coseno

$$\cos(3\theta) = 2\cos^3\theta - 3\cos\theta + 2\cos^3\theta$$

### Paso 9: Combinar términos semejantes

$$\cos(3\theta) = 2\cos^3\theta + 2\cos^3\theta - 3\cos\theta$$

$$\cos(3\theta) = 4\cos^3\theta - 3\cos\theta$$

---

## ✅ Resultado Final

$$\boxed{\cos(3\theta) = 4\cos^3\theta - 3\cos\theta \quad \text{Q.E.D.}}$$

---

## 🔍 Verificación con Valores Específicos

### Verificación 1: θ = 0°

**Lado izquierdo:**
$$\cos(3 \cdot 0°) = \cos(0°) = 1$$

**Lado derecho:**
$$4\cos^3(0°) - 3\cos(0°) = 4(1)^3 - 3(1) = 4 - 3 = 1$$

✓ Ambos lados son iguales.

### Verificación 2: θ = 60°

**Lado izquierdo:**
$$\cos(3 \cdot 60°) = \cos(180°) = -1$$

**Lado derecho:**
$$4\cos^3(60°) - 3\cos(60°) = 4\left(\frac{1}{2}\right)^3 - 3\left(\frac{1}{2}\right)$$
$$= 4 \cdot \frac{1}{8} - \frac{3}{2} = \frac{1}{2} - \frac{3}{2} = -1$$

✓ Ambos lados son iguales.

### Verificación 3: θ = 30°

**Lado izquierdo:**
$$\cos(3 \cdot 30°) = \cos(90°) = 0$$

**Lado derecho:**
$$4\cos^3(30°) - 3\cos(30°) = 4\left(\frac{\sqrt{3}}{2}\right)^3 - 3\left(\frac{\sqrt{3}}{2}\right)$$
$$= 4 \cdot \frac{3\sqrt{3}}{8} - \frac{3\sqrt{3}}{2} = \frac{3\sqrt{3}}{2} - \frac{3\sqrt{3}}{2} = 0$$

✓ Ambos lados son iguales.

---

## 📚 Notas Adicionales

> **Observación:** Esta identidad es fundamental para:
> - Resolver ecuaciones trigonométricas de tercer grado
> - La fórmula de De Moivre
> - Cálculo de valores exactos de funciones trigonométricas
> - El problema clásico de la trisección del ángulo

### Identidades Relacionadas

- **[Seno](../../../../glossary.md#seno) del ángulo triple:** $\sin(3\theta) = 3\sin\theta - 4\sin^3\theta$
- **[Tangente](../../../../glossary.md#tangente) del ángulo triple:** $\tan(3\theta) = \dfrac{3\tan\theta - \tan^3\theta}{1 - 3\tan^2\theta}$
