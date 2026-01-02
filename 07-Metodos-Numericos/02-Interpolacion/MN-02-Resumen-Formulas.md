<!--
---
title: Resumen de Fórmulas - Interpolación
type: cheatsheet
topic: interpolacion
tags: [métodos-numéricos, interpolación, fórmulas, cheatsheet]
created: 2025-12-20
updated: 2025-12-20
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Resumen de Fórmulas: Interpolación

## 1. Interpolación de Lagrange

### Fórmula Principal
$$P_n(x) = \sum_{i=0}^{n} y_i \cdot L_i(x)$$

### Polinomios Base de Lagrange
$$L_i(x) = \prod_{j=0, j \neq i}^{n} \frac{x - x_j}{x_i - x_j}$$

### Forma Expandida para 3 puntos
$$P_2(x) = y_0 \frac{(x-x_1)(x-x_2)}{(x_0-x_1)(x_0-x_2)} + y_1 \frac{(x-x_0)(x-x_2)}{(x_1-x_0)(x_1-x_2)} + y_2 \frac{(x-x_0)(x-x_1)}{(x_2-x_0)(x_2-x_1)}$$

---

## 2. Interpolación de Newton (Diferencias Divididas)

### Fórmula Principal
$$P_n(x) = f[x_0] + f[x_0,x_1](x-x_0)(x-x_1) + \cdots$$

### Diferencias Divididas

**[Orden](../../glossary.md#orden) 0:**
$$f[x_i] = f(x_i) = y_i$$

**[Orden](../../glossary.md#orden) 1:**
$$f[x_i, x_{i+1}] = \frac{f[x_{i+1}] - f[x_i]}{x_{i+1} - x_i}$$

**Orden 2:**
$$f[x_i, x_{i+1}, x_{i+2}] = \frac{f[x_{i+1}, x_{i+2}] - f[x_i, x_{i+1}]}{x_{i+2} - x_i}$$

**Orden k (general):**
$$f[x_i, \ldots, x_{i+k}] = \frac{f[x_{i+1}, \ldots, x_{i+k}] - f[x_i, \ldots, x_{i+k-1}]}{x_{i+k} - x_i}$$

---

## 3. Diferencias Finitas (Nodos Equidistantes)

### Diferencias Progresivas
$$\Delta^0 y_i = y_i$$
$$\Delta y_i = y_{i+1} - y_i$$
$$\Delta^2 y_i = \Delta y_{i+1} - \Delta y_i$$
$$\Delta^n y_i = \Delta^{n-1} y_{i+1} - \Delta^{n-1} y_i$$

### Fórmula de Newton Progresiva
$$P_n(x) = \sum_{k=0}^{n} \binom{s}{k} \Delta^k y_0$$

donde $s = \frac{x - x_0}{h}$ y $h$ es el espaciamiento.

### Diferencias Regresivas
$$\nabla y_i = y_i - y_{i-1}$$
$$\nabla^n y_i = \nabla^{n-1} y_i - \nabla^{n-1} y_{i-1}$$

---

## 4. Splines Cúbicos

### Forma General del Spline en $[x_i, x_{i+1}]$
$$S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3$$

### Condiciones de Continuidad
1. $S_i(x_i) = y_i$ (pasa por los puntos)
2. $S_i(x_{i+1}) = S_{i+1}(x_{i+1})$ ([continuidad](../../glossary.md#derivada) primera continua)
4. $S''_i(x_{i+1}) = S''_{i+1}(x_{i+1})$ ([derivada](../../glossary.md#derivadas) continuas | Sistema de ecuaciones más grande |

---

## Fórmulas Útiles

### Coeficiente Binomial Generalizado
$$\binom{s}{k} = \frac{s(s-1)(s-2)\cdots(s-k+1)}{k!}$$

### Unicidad del Polinomio
Para $n+1$ puntos con $x_i$ distintos, existe un **único** [polinomio](../../glossary.md#polinomio) de grado $\leq n$ que pasa por todos ellos.
