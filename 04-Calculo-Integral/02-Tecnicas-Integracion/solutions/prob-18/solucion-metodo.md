<!--
---
title: "Solución - [Integración por Partes](../../../../glossary.md#integracion-por-partes) Iteradas"
type: solution
topic: tecnicas-integracion
problem_id: CI-02-018
techniques:
  - integracion-por-partes
  - partes-iteradas
  - metodo-tabular
difficulty: intermedio-avanzado
tags:
  - exponenciales
  - polinomios
  - partes-repetidas
created: 2025-12-22
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../glossary.md)

---

# Solución: $\int x^2 e^x \, dx$

## Problema

Calcular la [integral indefinida](../../../../glossary.md#integral-indefinida):
$$\int x^2 e^x \, dx$$

---

## Método de Solución: Integración por Partes Iteradas

### Fórmula de Integración por Partes

$$\int u \, dv = uv - \int v \, du$$

### Estrategia

Para integrales de la forma $\int x^n e^{ax} \, dx$:
- Elegir $u = x^n$ (se simplifica al derivar)
- Elegir $dv = e^{ax} \, dx$ (fácil de integrar)

Aplicaremos partes **dos veces** para eliminar el factor polinomial.

---

### Primera aplicación de partes

**Elección:**
| | |
|---|---|
| $u = x^2$ | $dv = e^x \, dx$ |
| $du = 2x \, dx$ | $v = e^x$ |

**Aplicación:**
$$\int x^2 e^x \, dx = x^2 e^x - \int e^x \cdot 2x \, dx$$

$$= x^2 e^x - 2\int x e^x \, dx$$

---

### Segunda aplicación de partes

Ahora calculamos $\int x e^x \, dx$:

**Elección:**
| | |
|---|---|
| $u = x$ | $dv = e^x \, dx$ |
| $du = dx$ | $v = e^x$ |

**Aplicación:**
$$\int x e^x \, dx = x e^x - \int e^x \, dx$$

$$= x e^x - e^x$$

$$= e^x(x - 1)$$

---

### Paso 3: Sustituir en el resultado original

$$\int x^2 e^x \, dx = x^2 e^x - 2\int x e^x \, dx$$

$$= x^2 e^x - 2[e^x(x - 1)]$$

$$= x^2 e^x - 2xe^x + 2e^x$$

### Paso 4: Factorizar

$$= e^x(x^2 - 2x + 2) + C$$

---

## Método Tabular (LIATE)

El método tabular organiza las partes iteradas de forma sistemática.

### Construcción de la tabla

| Signo | [Derivadas](../../../../glossary.md#derivadas) de $x^2$ | Integrales de $e^x$ |
|:-----:|:------------------:|:-------------------:|
| $+$ | $x^2$ | $e^x$ |
| $-$ | $2x$ | $e^x$ |
| $+$ | $2$ | $e^x$ |
| $-$ | $0$ | $e^x$ |

### Lectura de la tabla (productos diagonales)

Multiplicamos diagonalmente con los signos alternados:
$$\int x^2 e^x \, dx = (+)(x^2)(e^x) + (-)(2x)(e^x) + (+)(2)(e^x) + C$$

$$= x^2 e^x - 2xe^x + 2e^x + C$$

$$= e^x(x^2 - 2x + 2) + C$$

---

## Respuesta Final

$$\boxed{\int x^2 e^x \, dx = e^x(x^2 - 2x + 2) + C}$$

**Forma expandida:**
$$\boxed{\int x^2 e^x \, dx = x^2 e^x - 2xe^x + 2e^x + C}$$

---

## Verificación por Derivación

Derivamos $f(x) = e^x(x^2 - 2x + 2)$ usando la regla del producto:

$$\frac{d}{dx}[e^x(x^2 - 2x + 2)]$$

Sea $g(x) = e^x$ y $h(x) = x^2 - 2x + 2$

Entonces: $g'(x) = e^x$ y $h'(x) = 2x - 2$

Por la regla del producto:
$$\frac{d}{dx}[g \cdot h] = g' \cdot h + g \cdot h'$$

$$= e^x(x^2 - 2x + 2) + e^x(2x - 2)$$

$$= e^x[(x^2 - 2x + 2) + (2x - 2)]$$

$$= e^x[x^2 - 2x + 2 + 2x - 2]$$

$$= e^x \cdot x^2$$

$$= x^2 e^x \quad \checkmark$$

**La solución es correcta.**

---

## Fórmula General

Para $\int x^n e^{ax} \, dx$, el patrón es:

$$\int x^n e^{ax} \, dx = e^{ax}\sum_{k=0}^{n} (-1)^k \frac{n!}{(n-k)!} \frac{x^{n-k}}{a^{k+1}} + C$$

### Casos particulares:

| Integral | Resultado |
|----------|-----------|
| $\int x e^x \, dx$ | $e^x(x - 1) + C$ |
| $\int x^2 e^x \, dx$ | $e^x(x^2 - 2x + 2) + C$ |
| $\int x^3 e^x \, dx$ | $e^x(x^3 - 3x^2 + 6x - 6) + C$ |

---

## Notas Adicionales

> **Regla LIATE:** Para elegir $u$ en [integración por partes](../../../../glossary.md#integracion-por-partes), priorizar:
> - **L**ogarítmicas
> - **I**nversas trigonométricas
> - **A**lgebraicas (polinomios)
> - **T**rigonométricas
> - **E**xponenciales

> **Cuántas veces aplicar partes:** Para $\int x^n e^{ax} \, dx$, se necesitan exactamente $n$ aplicaciones de partes.

> **Ventaja del método tabular:** Reduce errores de signos y organiza el cálculo sistemáticamente.
