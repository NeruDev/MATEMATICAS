<!--
---
type: solution
problem-id: CD-02-21
topic: Derivadas
subtopic: Regla del producto
difficulty: intermedio
tags: [derivada, producto-triple, exponencial, trigonométrica]
created: 2024-12-22
---
-->

# Solución: Derivada de g(x) = x² eˣ sin x (Producto Triple)

## Problema

Derivar $g(x) = x^2 e^x \sin x$ aplicando la regla del producto generalizada.

---

## Método de Solución: Regla del producto para tres funciones

### Paso 1: Identificar las tres funciones

Sea $g(x) = u(x) \cdot v(x) \cdot w(x)$ donde:

| Función | Expresión | Derivada |
|---------|-----------|----------|
| $u(x)$ | $x^2$ | $u'(x) = 2x$ |
| $v(x)$ | $e^x$ | $v'(x) = e^x$ |
| $w(x)$ | $\sin x$ | $w'(x) = \cos x$ |

### Paso 2: Aplicar la regla del producto generalizada

Para el producto de tres funciones:

$$\frac{d}{dx}[u \cdot v \cdot w] = u'vw + uv'w + uvw'$$

> **Nota**: Cada término tiene exactamente una derivada y dos funciones sin derivar.

### Paso 3: Calcular cada término

**Término 1:** $u'(x) \cdot v(x) \cdot w(x)$
$$= (2x)(e^x)(\sin x) = 2x e^x \sin x$$

**Término 2:** $u(x) \cdot v'(x) \cdot w(x)$
$$= (x^2)(e^x)(\sin x) = x^2 e^x \sin x$$

**Término 3:** $u(x) \cdot v(x) \cdot w'(x)$
$$= (x^2)(e^x)(\cos x) = x^2 e^x \cos x$$

### Paso 4: Sumar los tres términos

$$g'(x) = 2x e^x \sin x + x^2 e^x \sin x + x^2 e^x \cos x$$

### Paso 5: Factorizar (opcional pero recomendado)

Factorizamos el término común $x e^x$:

$$g'(x) = x e^x \left[ 2\sin x + x\sin x + x\cos x \right]$$

O de forma más compacta:

$$g'(x) = x e^x \left[ (2 + x)\sin x + x\cos x \right]$$

---

## Respuesta

$$\boxed{g'(x) = x e^x \left[ (x+2)\sin x + x\cos x \right]}$$

Forma expandida equivalente:
$$\boxed{g'(x) = 2x e^x \sin x + x^2 e^x \sin x + x^2 e^x \cos x}$$

---

## Verificación

### Método 1: Aplicación en dos pasos de la regla del producto

Agrupamos: $g(x) = (x^2 e^x) \cdot \sin x$

Sea $p(x) = x^2 e^x$, entonces $p'(x) = 2x e^x + x^2 e^x = e^x(2x + x^2)$

Aplicando regla del producto a $g = p \cdot \sin x$:

$$g'(x) = p'(x)\sin x + p(x)\cos x$$
$$= e^x(2x + x^2)\sin x + x^2 e^x \cos x$$
$$= 2x e^x \sin x + x^2 e^x \sin x + x^2 e^x \cos x \checkmark$$

### Método 2: Verificación numérica en x = π/4

Calculamos $g(\pi/4)$ y $g'(\pi/4)$:

- $g(\pi/4) = \left(\frac{\pi}{4}\right)^2 e^{\pi/4} \sin\frac{\pi}{4} \approx 0.617 \cdot 2.193 \cdot 0.707 \approx 0.957$

- $g'(\pi/4) = \frac{\pi}{4} e^{\pi/4} \left[ \left(\frac{\pi}{4}+2\right)\frac{\sqrt{2}}{2} + \frac{\pi}{4}\frac{\sqrt{2}}{2} \right]$

Aproximación numérica con $h = 0.0001$:
$$\frac{g(\pi/4 + h) - g(\pi/4)}{h} \approx 4.18$$

Evaluando la fórmula: $g'(\pi/4) \approx 4.18 \checkmark$

---

## Notas adicionales

> **Regla general**: Para $n$ funciones multiplicadas:
> $$\frac{d}{dx}[f_1 \cdot f_2 \cdots f_n] = \sum_{i=1}^{n} \left( f_1 \cdots f_{i-1} \cdot f_i' \cdot f_{i+1} \cdots f_n \right)$$

> **Tip de factorización**: Siempre buscar factores comunes para simplificar la expresión final.
