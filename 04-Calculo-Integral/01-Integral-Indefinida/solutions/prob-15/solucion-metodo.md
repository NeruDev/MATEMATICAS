<!--
---
title: "Solución - Integral de Cociente de Polinomios"
type: solution
topic: integral-indefinida
problem_id: CI-01-015
techniques:
  - division-polinomios
  - factorizacion
  - diferencia-cuadrados
difficulty: intermedio
tags:
  - fracciones-algebraicas
  - division-sintetica
  - arctangente
created: 2025-12-22
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../glossary.md)

---

# Solución: $\int\frac{x^4 - 1}{x^2 + 1} \, dx$

## Problema

Calcular la [integral indefinida](../../../../glossary.md#integral-indefinida):
$$\int\frac{x^4 - 1}{x^2 + 1} \, dx$$

---

## Método de Solución: División y Factorización

### Paso 1: Analizar el numerador

Observamos que $x^4 - 1$ es una diferencia de cuadrados:
$$x^4 - 1 = (x^2)^2 - 1^2 = (x^2 + 1)(x^2 - 1)$$

### Paso 2: Simplificar la fracción

Sustituimos la [factorización](../../../../glossary.md#factorizacion):
$$\frac{x^4 - 1}{x^2 + 1} = \frac{(x^2 + 1)(x^2 - 1)}{x^2 + 1}$$

Cancelamos el factor común $(x^2 + 1)$:
$$\frac{(x^2 + 1)(x^2 - 1)}{x^2 + 1} = x^2 - 1$$

### Paso 3: Integrar el resultado simplificado

La integral se reduce a:
$$\int\frac{x^4 - 1}{x^2 + 1} \, dx = \int(x^2 - 1) \, dx$$

Integrando término a término:
$$\int(x^2 - 1) \, dx = \int x^2 \, dx - \int 1 \, dx$$

Aplicando la regla de potencias:
$$= \frac{x^3}{3} - x + C$$

---

## Método Alternativo: División de Polinomios

Si no reconocemos la [factorización](../../../../glossary.md#factorizacion), podemos realizar la división directamente.

### División larga de $x^4 - 1$ entre $x^2 + 1$:

```
         x² - 1
       ─────────────
x²+1 │ x⁴ + 0x³ + 0x² + 0x - 1
       x⁴ + 0x³ + x²
       ─────────────────
              - x² + 0x - 1
              - x² + 0x - 1
              ─────────────
                      0
```

**Resultado de la división:**
$$\frac{x^4 - 1}{x^2 + 1} = x^2 - 1 + \frac{0}{x^2 + 1} = x^2 - 1$$

La división es exacta (residuo = 0), confirmando el resultado del Paso 2.

### Integración:
$$\int(x^2 - 1) \, dx = \frac{x^3}{3} - x + C$$

---

## Respuesta Final

$$\boxed{\int\frac{x^4 - 1}{x^2 + 1} \, dx = \frac{x^3}{3} - x + C}$$

---

## Verificación por Derivación

Derivamos el resultado:
$$\frac{d}{dx}\left(\frac{x^3}{3} - x + C\right)$$

Derivando término a término:
- $\frac{d}{dx}\left(\frac{x^3}{3}\right) = x^2$
- $\frac{d}{dx}(-x) = -1$
- $\frac{d}{dx}(C) = 0$

Resultado:
$$x^2 - 1$$

Verificamos que $\frac{x^4 - 1}{x^2 + 1} = x^2 - 1$:
$$x^4 - 1 = (x^2 - 1)(x^2 + 1) \quad \checkmark$$

**La solución es correcta.**

---

## Notas Adicionales

> **Estrategia General:** Cuando el grado del numerador es mayor o igual al del denominador, siempre realizar la división primero.

> **Factorizaciones Útiles:**
> - $a^2 - b^2 = (a+b)(a-b)$ (diferencia de cuadrados)
> - $a^4 - b^4 = (a^2+b^2)(a^2-b^2) = (a^2+b^2)(a+b)(a-b)$

> **Caso Especial:** Si la división no fuera exacta y quedara un residuo de la forma $\frac{k}{x^2+1}$, la integral de ese término sería $k\arctan(x)$.
