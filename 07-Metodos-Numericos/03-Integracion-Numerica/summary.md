<!--
content_type: summary
topic: Integración Numérica
---
-->

# Resumen: Integración Numérica

## Problema Fundamental

Aproximar $I = \int_a^b f(x)\,dx$ mediante una suma ponderada:
$$I \approx \sum_{i=0}^{n} w_i f(x_i)$$

## Fórmulas de Newton-Cotes

| Método | Fórmula | Error |
|--------|---------|-------|
| **Trapecio** | $\frac{h}{2}[f_0 + f_1]$ | $O(h^3)$ |
| **Simpson 1/3** | $\frac{h}{3}[f_0 + 4f_1 + f_2]$ | $O(h^5)$ |
| **Simpson 3/8** | $\frac{3h}{8}[f_0 + 3f_1 + 3f_2 + f_3]$ | $O(h^5)$ |

## Fórmulas Compuestas

### Trapecio Compuesto ($n$ subintervalos)
$$I \approx \frac{h}{2}[f_0 + 2(f_1 + ... + f_{n-1}) + f_n]$$
**Error:** $-\frac{(b-a)h^2}{12}f''(\xi)$

### Simpson Compuesto ($n$ par)
$$I \approx \frac{h}{3}[f_0 + 4(f_1+f_3+...) + 2(f_2+f_4+...) + f_n]$$
**Error:** $-\frac{(b-a)h^4}{180}f^{(4)}(\xi)$

## Cuadratura de Gauss-Legendre

Para $\int_{-1}^{1} f(x)\,dx$:

| $n$ | Nodos $x_i$ | Pesos $w_i$ | Exacto para |
|-----|-------------|-------------|-------------|
| 1 | 0 | 2 | Grado ≤ 1 |
| 2 | $\pm\frac{1}{\sqrt{3}}$ | 1, 1 | Grado ≤ 3 |
| 3 | $0, \pm\sqrt{0.6}$ | 8/9, 5/9, 5/9 | Grado ≤ 5 |

**Cambio de variable** para $[a,b]$:
$$\int_a^b f(x)\,dx = \frac{b-a}{2}\int_{-1}^{1} f\left(\frac{b-a}{2}t + \frac{a+b}{2}\right)dt$$

## Integración de Romberg

Extrapolación de Richardson aplicada al trapecio:
$$R_{k,j} = \frac{4^j R_{k,j-1} - R_{k-1,j-1}}{4^j - 1}$$

Iniciando con $R_{k,0} = T(h_k)$ donde $h_k = \frac{b-a}{2^k}$

## Diagrama de Selección

```
¿Conoces f(x) analíticamente?
├── SÍ → ¿Puedes elegir nodos?
│          ├── SÍ → Gauss-Legendre
│          └── NO → Simpson o Romberg
│
└── NO (datos tabulados)
           → Trapecio o Simpson (según número de puntos)
```
