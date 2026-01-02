<!--
---
title: "Solución - [Integración por Partes](../../../..](../../../../glossary.md)#integracion-por-partes) Cíclicas (Exponencial-[Coseno](../../../..](../../../../glossary.md)#coseno))"
type: solution
topic: tecnicas-integracion
problem_id: CI-02-020
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

# Solución: $\int e^x \cos x \, dx$

## Problema

Calcular la [integral indefinida](../../../..](../../../../glossary.md)#integral-indefinida):
$$\int e^x \cos x \, dx$$

---

## Método de Solución: Partes Cíclicas

### Concepto Clave

Al integrar productos de exponenciales con funciones trigonométricas, la integral original **reaparece** después de aplicar partes dos veces. Esto permite formar una **ecuación algebraica** para resolver.

### Notación

Denotemos:
$$I = \int e^x \cos x \, dx$$

---

### Primera aplicación de partes

**Elección:**
| | |
|---|---|
| $u = \cos x$ | $dv = e^x \, dx$ |
| $du = -\sin x \, dx$ | $v = e^x$ |

**Aplicación de la fórmula** $\int u \, dv = uv - \int v \, du$:

$$I = e^x \cos x - \int e^x (-\sin x) \, dx$$

$$I = e^x \cos x + \int e^x \sin x \, dx$$

---

### Segunda aplicación de partes

Ahora calculamos $\int e^x \sin x \, dx$:

**Elección:**
| | |
|---|---|
| $u = \sin x$ | $dv = e^x \, dx$ |
| $du = \cos x \, dx$ | $v = e^x$ |

**Aplicación:**
$$\int e^x \sin x \, dx = e^x \sin x - \int e^x \cos x \, dx$$

$$= e^x \sin x - I$$

---

### Paso 3: Sustituir y formar la ecuación

Reemplazamos en la expresión de $I$:
$$I = e^x \cos x + [e^x \sin x - I]$$

$$I = e^x \cos x + e^x \sin x - I$$

### Paso 4: Resolver para $I$

Sumamos $I$ a ambos lados:
$$I + I = e^x \cos x + e^x \sin x$$

$$2I = e^x(\cos x + \sin x)$$

$$I = \frac{e^x(\cos x + \sin x)}{2}$$

### Paso 5: Agregar la constante

$$I = \frac{e^x(\sin x + \cos x)}{2} + C$$

---

## Respuesta Final

$$\boxed{\int e^x \cos x \, dx = \frac{e^x(\sin x + \cos x)}{2} + C}$$

**Forma alternativa:**
$$\boxed{\int e^x \cos x \, dx = \frac{e^x \sin x + e^x \cos x}{2} + C}$$

---

## Verificación por Derivación

Derivamos $f(x) = \frac{e^x(\sin x + \cos x)}{2}$:

$$\frac{d}{dx}\left[\frac{e^x(\sin x + \cos x)}{2}\right] = \frac{1}{2} \cdot \frac{d}{dx}[e^x(\sin x + \cos x)]$$

Aplicamos la regla del producto con $g(x) = e^x$ y $h(x) = \sin x + \cos x$:

- $g'(x) = e^x$
- $h'(x) = \cos x - \sin x$

$$\frac{d}{dx}[e^x(\sin x + \cos x)] = e^x(\sin x + \cos x) + e^x(\cos x - \sin x)$$

$$= e^x[(\sin x + \cos x) + (\cos x - \sin x)]$$

$$= e^x[\sin x + \cos x + \cos x - \sin x]$$

$$= e^x[2\cos x]$$

$$= 2e^x \cos x$$

Por lo tanto:
$$\frac{d}{dx}\left[\frac{e^x(\sin x + \cos x)}{2}\right] = \frac{1}{2} \cdot 2e^x \cos x = e^x \cos x \quad \checkmark$$

**La solución es correcta.**

---

## Método Alternativo: Elección inversa de $u$ y $dv$

También podemos elegir $u = e^x$ y $dv = \cos x \, dx$:

### Primera aplicación:
| | |
|---|---|
| $u = e^x$ | $dv = \cos x \, dx$ |
| $du = e^x \, dx$ | $v = \sin x$ |

$$I = e^x \sin x - \int e^x \sin x \, dx$$

### Segunda aplicación:
| | |
|---|---|
| $u = e^x$ | $dv = \sin x \, dx$ |
| $du = e^x \, dx$ | $v = -\cos x$ |

$$\int e^x \sin x \, dx = -e^x \cos x - \int (-\cos x) e^x \, dx = -e^x \cos x + I$$

### Sustitución:
$$I = e^x \sin x - [-e^x \cos x + I]$$
$$I = e^x \sin x + e^x \cos x - I$$
$$2I = e^x(\sin x + \cos x)$$
$$I = \frac{e^x(\sin x + \cos x)}{2} + C \quad \checkmark$$

---

## Fórmula General

Para $\int e^{ax} \cos(bx) \, dx$:

$$\boxed{\int e^{ax} \cos(bx) \, dx = \frac{e^{ax}(a\cos bx + b\sin bx)}{a^2 + b^2} + C}$$

**Verificación con $a = 1$, $b = 1$:**
$$\int e^x \cos x \, dx = \frac{e^x(1 \cdot \cos x + 1 \cdot \sin x)}{1^2 + 1^2} = \frac{e^x(\cos x + \sin x)}{2} \quad \checkmark$$

---

## Notas Adicionales

> **Patrón Cíclico:** Las integrales $\int e^{ax}\cos(bx)\,dx$ e $\int e^{ax}\sin(bx)\,dx$ están interconectadas. Integrar una conduce a la otra.

> **Error Común:** Olvidar que la integral reaparece con signo negativo y sumar en lugar de formar la ecuación.

> **Consistencia:** Es crucial usar la misma elección de $u$ y $dv$ en ambas aplicaciones de partes (o $u = \text{trig}$, $dv = e^x dx$ ambas veces, o viceversa).

> **Relación con números complejos:** Usando la fórmula de Euler $e^{ix} = \cos x + i\sin x$:
> $$\int e^x \cos x \, dx = \text{Re}\left(\int e^{(1+i)x} dx\right) = \text{Re}\left(\frac{e^{(1+i)x}}{1+i}\right)$$
