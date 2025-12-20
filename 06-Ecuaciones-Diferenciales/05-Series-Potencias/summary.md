# Resumen: Series de Potencias para EDO

## Forma de Solución
$$y = \sum_{n=0}^{\infty} c_n (x-x_0)^n$$

## Clasificación de Puntos

Para $P(x)y'' + Q(x)y' + R(x)y = 0$:

| Tipo | Condición | Método |
|------|-----------|--------|
| Ordinario | $P(x_0) \neq 0$ | Series de potencias |
| Singular regular | $\lim_{x\to x_0}(x-x_0)\frac{Q}{P}$ y $\lim_{x\to x_0}(x-x_0)^2\frac{R}{P}$ finitos | Frobenius |
| Singular irregular | Límites no finitos | Métodos avanzados |

## Método de Frobenius

Solución: $y = \sum_{n=0}^{\infty} c_n x^{n+r}$

**Ecuación indicial:** $r(r-1) + p_0 r + q_0 = 0$

donde $p_0 = \lim_{x\to 0} xP(x)/Q(x)$ y $q_0 = \lim_{x\to 0} x^2 R(x)/Q(x)$

### Casos según raíces $r_1, r_2$ ($r_1 \geq r_2$)

| Caso | Condición | Soluciones |
|------|-----------|------------|
| 1 | $r_1 - r_2 \notin \mathbb{Z}$ | Dos series de Frobenius |
| 2 | $r_1 = r_2$ | $y_1$ serie, $y_2 = y_1 \ln x + \sum c_n x^{n+r}$ |
| 3 | $r_1 - r_2 \in \mathbb{Z}^+$ | $y_1$ serie, $y_2$ puede tener $\ln x$ |

## Ecuaciones Especiales

**Bessel:** $x^2y'' + xy' + (x^2 - \nu^2)y = 0$

Soluciones: $J_\nu(x)$, $Y_\nu(x)$

**Legendre:** $(1-x^2)y'' - 2xy' + n(n+1)y = 0$

Soluciones: $P_n(x)$ (polinomios de Legendre)
