<!--
---
title: "Solución - [Integración por Partes](../../../..](../../../../glossary.md)#integracion-por-partes) Cíclicas (Exponencial-[Seno](../../../..](../../../../glossary.md)#seno))"
type: solution
topic: tecnicas-integracion
problem_id: CI-02-021
techniques:
  - integracion-por-partes
  - partes-ciclicas
  - ecuacion-integral
difficulty: avanzado
tags:
  - exponenciales
  - trigonometricas
  - sistema-ecuaciones
created: 2025-12-22
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: $\int e^x \sin x \, dx$

## Problema

Calcular la [integral indefinida](../../../..](../../../../glossary.md)#integral-indefinida):
$$\int e^x \sin x \, dx$$

---

## Método de Solución: Partes Cíclicas

### Concepto Clave

Al igual que con $\int e^x \cos x \, dx$, esta integral exhibe un **comportamiento cíclico**: después de dos aplicaciones de partes, la integral original reaparece, permitiendo resolver algebraicamente.

### Notación

Denotemos:
$$J = \int e^x \sin x \, dx$$

---

### Primera aplicación de partes

**Elección:**
| | |
|---|---|
| $u = \sin x$ | $dv = e^x \, dx$ |
| $du = \cos x \, dx$ | $v = e^x$ |

**Aplicación de la fórmula** $\int u \, dv = uv - \int v \, du$:

$$J = e^x \sin x - \int e^x \cos x \, dx$$

---

### Segunda aplicación de partes

Calculamos $\int e^x \cos x \, dx$:

**Elección (manteniendo consistencia):**
| | |
|---|---|
| $u = \cos x$ | $dv = e^x \, dx$ |
| $du = -\sin x \, dx$ | $v = e^x$ |

**Aplicación:**
$$\int e^x \cos x \, dx = e^x \cos x - \int e^x (-\sin x) \, dx$$

$$= e^x \cos x + \int e^x \sin x \, dx$$

$$= e^x \cos x + J$$

---

### Paso 3: Sustituir y formar la ecuación

Reemplazamos en la expresión de $J$:
$$J = e^x \sin x - [e^x \cos x + J]$$

$$J = e^x \sin x - e^x \cos x - J$$

### Paso 4: Resolver para $J$

Sumamos $J$ a ambos lados:
$$J + J = e^x \sin x - e^x \cos x$$

$$2J = e^x(\sin x - \cos x)$$

$$J = \frac{e^x(\sin x - \cos x)}{2}$$

### Paso 5: Agregar la constante

$$J = \frac{e^x(\sin x - \cos x)}{2} + C$$

---

## Respuesta Final

$$\boxed{\int e^x \sin x \, dx = \frac{e^x(\sin x - \cos x)}{2} + C}$$

**Forma alternativa:**
$$\boxed{\int e^x \sin x \, dx = \frac{e^x \sin x - e^x \cos x}{2} + C}$$

---

## Verificación por Derivación

Derivamos $f(x) = \frac{e^x(\sin x - \cos x)}{2}$:

$$\frac{d}{dx}\left[\frac{e^x(\sin x - \cos x)}{2}\right] = \frac{1}{2} \cdot \frac{d}{dx}[e^x(\sin x - \cos x)]$$

Aplicamos la regla del producto con $g(x) = e^x$ y $h(x) = \sin x - \cos x$:

- $g'(x) = e^x$
- $h'(x) = \cos x - (-\sin x) = \cos x + \sin x$

$$\frac{d}{dx}[e^x(\sin x - \cos x)] = e^x(\sin x - \cos x) + e^x(\cos x + \sin x)$$

$$= e^x[(\sin x - \cos x) + (\cos x + \sin x)]$$

$$= e^x[\sin x - \cos x + \cos x + \sin x]$$

$$= e^x[2\sin x]$$

$$= 2e^x \sin x$$

Por lo tanto:
$$\frac{d}{dx}\left[\frac{e^x(\sin x - \cos x)}{2}\right] = \frac{1}{2} \cdot 2e^x \sin x = e^x \sin x \quad \checkmark$$

**La solución es correcta.**

---

## Método Alternativo: Elección inversa de $u$ y $dv$

Eligiendo $u = e^x$ y $dv = \sin x \, dx$:

### Primera aplicación:
| | |
|---|---|
| $u = e^x$ | $dv = \sin x \, dx$ |
| $du = e^x \, dx$ | $v = -\cos x$ |

$$J = -e^x \cos x - \int (-\cos x) e^x \, dx$$
$$J = -e^x \cos x + \int e^x \cos x \, dx$$

### Segunda aplicación:
| | |
|---|---|
| $u = e^x$ | $dv = \cos x \, dx$ |
| $du = e^x \, dx$ | $v = \sin x$ |

$$\int e^x \cos x \, dx = e^x \sin x - \int e^x \sin x \, dx = e^x \sin x - J$$

### Sustitución:
$$J = -e^x \cos x + [e^x \sin x - J]$$
$$J = -e^x \cos x + e^x \sin x - J$$
$$2J = e^x(\sin x - \cos x)$$
$$J = \frac{e^x(\sin x - \cos x)}{2} + C \quad \checkmark$$

---

## Sistema de Ecuaciones: Conexión entre ambas integrales

Definamos:
- $I = \int e^x \cos x \, dx$
- $J = \int e^x \sin x \, dx$

De las aplicaciones de partes obtenemos el sistema:

$$\begin{cases}
I = e^x \cos x + J \\
J = e^x \sin x - I
\end{cases}$$

### Resolución del sistema:

**Sustituyendo la segunda ecuación en la primera:**
$$I = e^x \cos x + (e^x \sin x - I)$$
$$2I = e^x(\cos x + \sin x)$$
$$I = \frac{e^x(\cos x + \sin x)}{2}$$

**Sustituyendo en la segunda:**
$$J = e^x \sin x - \frac{e^x(\cos x + \sin x)}{2}$$
$$J = \frac{2e^x \sin x - e^x \cos x - e^x \sin x}{2}$$
$$J = \frac{e^x(\sin x - \cos x)}{2}$$

---

## Fórmula General

Para $\int e^{ax} \sin(bx) \, dx$:

$$\boxed{\int e^{ax} \sin(bx) \, dx = \frac{e^{ax}(a\sin bx - b\cos bx)}{a^2 + b^2} + C}$$

**Verificación con $a = 1$, $b = 1$:**
$$\int e^x \sin x \, dx = \frac{e^x(1 \cdot \sin x - 1 \cdot \cos x)}{1^2 + 1^2} = \frac{e^x(\sin x - \cos x)}{2} \quad \checkmark$$

---

## Comparación: Seno vs Coseno

| Integral | Resultado |
|----------|-----------|
| $\int e^x \cos x \, dx$ | $\frac{e^x(\sin x + \cos x)}{2} + C$ |
| $\int e^x \sin x \, dx$ | $\frac{e^x(\sin x - \cos x)}{2} + C$ |

**Observación:** La diferencia está solo en el signo del término $\cos x$.

---

## Notas Adicionales

> **Consistencia en las elecciones:** Es fundamental mantener el mismo tipo de elección ($u = \text{trig}$ o $u = e^x$) en ambas aplicaciones de partes para que la integral original reaparezca.

> **Signo del ciclo:** Al integrar [seno](../../../..](../../../../glossary.md)#seno), el ciclo produce un signo **negativo** frente a la integral que reaparece (a diferencia del [coseno](../../../..](../../../../glossary.md)#coseno) que produce signo positivo).

> **Truco de memoria:** 
> - [Coseno](../../../..](../../../../glossary.md)#coseno): $\frac{e^x(\sin x + \cos x)}{2}$ (ambos signos positivos)
> - Seno: $\frac{e^x(\sin x - \cos x)}{2}$ (seno positivo, coseno negativo)

> **Relación con la fórmula de Euler:**
> $$\int e^x \sin x \, dx = \text{Im}\left(\int e^{(1+i)x} dx\right) = \text{Im}\left(\frac{e^{(1+i)x}}{1+i}\right)$$
