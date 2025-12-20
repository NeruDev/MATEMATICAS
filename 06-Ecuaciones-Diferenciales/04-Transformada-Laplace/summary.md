# Resumen: Transformada de Laplace

## Definición
$$\mathcal{L}\{f(t)\} = F(s) = \int_0^{\infty} e^{-st}f(t)\,dt$$

## Tabla de Transformadas

| $f(t)$ | $F(s) = \mathcal{L}\{f\}$ |
|--------|---------------------------|
| $1$ | $\frac{1}{s}$ |
| $t^n$ | $\frac{n!}{s^{n+1}}$ |
| $e^{at}$ | $\frac{1}{s-a}$ |
| $\sin(bt)$ | $\frac{b}{s^2+b^2}$ |
| $\cos(bt)$ | $\frac{s}{s^2+b^2}$ |
| $e^{at}\sin(bt)$ | $\frac{b}{(s-a)^2+b^2}$ |
| $e^{at}\cos(bt)$ | $\frac{s-a}{(s-a)^2+b^2}$ |
| $t^n e^{at}$ | $\frac{n!}{(s-a)^{n+1}}$ |
| $u(t-a)$ | $\frac{e^{-as}}{s}$ |
| $\delta(t-a)$ | $e^{-as}$ |

## Propiedades Principales

| Propiedad | Fórmula |
|-----------|--------|
| Linealidad | $\mathcal{L}\{af + bg\} = aF + bG$ |
| Derivada | $\mathcal{L}\{f'\} = sF(s) - f(0)$ |
| Segunda derivada | $\mathcal{L}\{f''\} = s^2F(s) - sf(0) - f'(0)$ |
| Traslación en $s$ | $\mathcal{L}\{e^{at}f\} = F(s-a)$ |
| Traslación en $t$ | $\mathcal{L}\{u(t-a)f(t-a)\} = e^{-as}F(s)$ |
| Convolución | $\mathcal{L}\{f*g\} = F(s)G(s)$ |

## Método para PVI

1. Aplicar $\mathcal{L}$ a la EDO
2. Usar propiedades de derivadas (incluir condiciones iniciales)
3. Despejar $Y(s)$
4. Aplicar $\mathcal{L}^{-1}$ para obtener $y(t)$
