<!--
content_type: summary
topic: Interpolación
---
-->

# Resumen: Interpolación

## Problema Fundamental

Dados $n+1$ puntos $(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)$, encontrar un polinomio $P(x)$ de grado $\leq n$ tal que $P(x_i) = y_i$ para todo $i$.

## Teorema de Unicidad

Existe un **único** polinomio de grado $\leq n$ que interpola $n+1$ puntos con abscisas distintas.

## Formas del Polinomio Interpolante

| Forma | Fórmula | Ventaja |
|-------|---------|--------|
| **Lagrange** | $P(x) = \sum_{i=0}^{n} y_i L_i(x)$ | Directa, conceptual |
| **Newton** | $P(x) = \sum_{i=0}^{n} f[x_0,...,x_i]\prod_{j=0}^{i-1}(x-x_j)$ | Agregar puntos fácil |

## Fórmulas de Lagrange

$$L_i(x) = \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}$$

$$P(x) = \sum_{i=0}^{n} y_i L_i(x)$$

## Diferencias Divididas

$$f[x_i] = f(x_i)$$
$$f[x_i, x_{i+1}] = \frac{f[x_{i+1}] - f[x_i]}{x_{i+1} - x_i}$$
$$f[x_i, ..., x_{i+k}] = \frac{f[x_{i+1},...,x_{i+k}] - f[x_i,...,x_{i+k-1}]}{x_{i+k} - x_i}$$

## Error de Interpolación

$$f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x - x_i)$$

**Fenómeno de Runge:** Interpolación de alto grado puede oscilar en los extremos.

## Splines Cúbicos

Polinomios de grado 3 por tramos con:
- Continuidad de $S$, $S'$, $S''$
- $S(x_i) = y_i$

**Condiciones de frontera:**
- Natural: $S''(x_0) = S''(x_n) = 0$
- Sujeto: $S'(x_0) = f'_0$, $S'(x_n) = f'_n$

## Diagrama de Selección

```
¿Cuántos puntos tienes?
├── Pocos (≤5) → Lagrange o Newton
├── Muchos → ¿Datos equiespaciados?
│            ├── SÍ → Newton progresivo/regresivo
│            └── NO → Splines cúbicos
│
└── ¿Conoces derivadas? → Hermite
```
