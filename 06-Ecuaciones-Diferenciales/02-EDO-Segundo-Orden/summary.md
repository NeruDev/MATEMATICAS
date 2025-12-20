# Resumen: EDO de Segundo Orden

## Forma General
$$ay'' + by' + cy = f(x)$$

## Ecuación Homogénea ($f(x) = 0$)

### Ecuación Característica
$$ar^2 + br + c = 0$$

### Tipos de Raíces

| Discriminante | Raíces | Solución General |
|---------------|--------|------------------|
| $b^2 - 4ac > 0$ | $r_1 \neq r_2$ reales | $y_h = C_1 e^{r_1 x} + C_2 e^{r_2 x}$ |
| $b^2 - 4ac = 0$ | $r_1 = r_2 = r$ | $y_h = (C_1 + C_2 x)e^{rx}$ |
| $b^2 - 4ac < 0$ | $r = \alpha \pm \beta i$ | $y_h = e^{\alpha x}(C_1 \cos\beta x + C_2 \sin\beta x)$ |

## Ecuación No Homogénea
$$y = y_h + y_p$$

### Coeficientes Indeterminados

| $f(x)$ | Forma de $y_p$ |
|--------|---------------|
| $e^{ax}$ | $Ae^{ax}$ |
| $\cos(bx)$ o $\sin(bx)$ | $A\cos(bx) + B\sin(bx)$ |
| $x^n$ | $A_n x^n + A_{n-1}x^{n-1} + \cdots + A_0$ |
| $e^{ax}\cos(bx)$ | $e^{ax}(A\cos bx + B\sin bx)$ |

**Regla de Modificación:** Si $y_p$ duplica a $y_h$, multiplicar por $x$ (o $x^2$).

### Variación de Parámetros
$$y_p = u_1 y_1 + u_2 y_2$$

$$u_1' = -\frac{y_2 f(x)}{W}, \quad u_2' = \frac{y_1 f(x)}{W}$$

Wronskiano: $W = y_1 y_2' - y_2 y_1'$

## Ecuación de Cauchy-Euler
$$ax^2y'' + bxy' + cy = 0$$

Sustitución: $y = x^m$ → Ecuación auxiliar: $am(m-1) + bm + c = 0$

## Aplicaciones Físicas

### Oscilador Armónico
$$m\ddot{x} + c\dot{x} + kx = F(t)$$

- Sin amortiguamiento: $\omega_0 = \sqrt{k/m}$
- Subamortiguado: $c^2 < 4mk$
- Críticamente amortiguado: $c^2 = 4mk$
- Sobreamortiguado: $c^2 > 4mk$

### Circuito RLC
$$L\frac{d^2q}{dt^2} + R\frac{dq}{dt} + \frac{q}{C} = E(t)$$
