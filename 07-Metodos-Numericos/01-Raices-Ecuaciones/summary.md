<!--
content_type: summary
topic: Raíces de Ecuaciones
---
-->

# Resumen: Raíces de Ecuaciones

## Problema Fundamental

Encontrar $x^*$ tal que $f(x^*) = 0$ cuando no existe solución analítica.

## Clasificación de Métodos

| Tipo | Métodos | Ventaja | Desventaja |
|------|---------|---------|------------|
| **Cerrados** | Bisección, Falsa posición | Siempre convergen | Lentos |
| **Abiertos** | Newton-Raphson, Secante, Punto fijo | Rápidos | Pueden divergir |

## Tabla Comparativa

| Método | Convergencia | Requisitos | Orden |
|--------|--------------|------------|-------|
| Bisección | Lineal | $f$ continua, cambio de signo | 1 |
| Falsa posición | Lineal | $f$ continua, cambio de signo | 1 |
| Newton-Raphson | Cuadrática | $f'(x)$ conocida | 2 |
| Secante | Superlineal | Dos puntos iniciales | ≈1.618 |
| Punto fijo | Lineal | $|g'(x)| < 1$ | 1 |

## Fórmulas Clave

### Bisección
$$x_{n+1} = \frac{a_n + b_n}{2}$$

### Newton-Raphson
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

### Secante
$$x_{n+1} = x_n - f(x_n)\frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}$$

### Punto Fijo
$$x_{n+1} = g(x_n)$$

## Criterios de Convergencia

1. **Error absoluto:** $|x_{n+1} - x_n| < \varepsilon$
2. **Error relativo:** $\left|\frac{x_{n+1} - x_n}{x_{n+1}}\right| < \varepsilon$
3. **Valor de función:** $|f(x_n)| < \delta$

## Orden de Convergencia

$$\lim_{n \to \infty} \frac{|e_{n+1}|}{|e_n|^p} = C$$

- $p = 1$: Convergencia lineal
- $p = 2$: Convergencia cuadrática
- $p \approx 1.618$: Convergencia superlineal (secante)

## Diagrama de Selección

```
¿Tienes f'(x)?
├── SÍ → ¿f' es fácil de calcular?
│        ├── SÍ → Newton-Raphson
│        └── NO → Secante
│
└── NO → ¿Puedes encontrar [a,b] con cambio de signo?
         ├── SÍ → Bisección (seguro) o Falsa posición (más rápido)
         └── NO → Punto fijo (si existe g apropiada)
```
