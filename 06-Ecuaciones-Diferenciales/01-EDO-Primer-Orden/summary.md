# Resumen: EDO de Primer Orden

## Forma General

$$\frac{dy}{dx} = f(x, y) \quad \text{o} \quad M(x,y)dx + N(x,y)dy = 0$$

## Clasificación y Métodos

| Tipo | Forma | Método |
|------|-------|--------|
| **Separable** | $\frac{dy}{dx} = g(x)h(y)$ | $\int \frac{dy}{h(y)} = \int g(x)dx$ |
| **Lineal** | $\frac{dy}{dx} + P(x)y = Q(x)$ | Factor integrante $\mu = e^{\int P dx}$ |
| **Exacta** | $M dx + N dy = 0$ con $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$ | Encontrar $F(x,y) = C$ |
| **Bernoulli** | $\frac{dy}{dx} + P(x)y = Q(x)y^n$ | Sustituir $v = y^{1-n}$ |
| **Homogénea** | $\frac{dy}{dx} = F\left(\frac{y}{x}\right)$ | Sustituir $y = vx$ |

## Ecuación Lineal de Primer Orden

$$\frac{dy}{dx} + P(x)y = Q(x)$$

**Factor integrante:** $\mu(x) = e^{\int P(x)dx}$

**Solución general:**
$$y = \frac{1}{\mu(x)}\left[\int \mu(x)Q(x)dx + C\right]$$

## Ecuación Exacta

$M(x,y)dx + N(x,y)dy = 0$ es exacta si:
$$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$$

**Solución:** $F(x,y) = C$ donde:
$$\frac{\partial F}{\partial x} = M, \quad \frac{\partial F}{\partial y} = N$$

## Factor Integrante para Exactas

Si no es exacta, buscar $\mu$:

- Si $\frac{M_y - N_x}{N}$ depende solo de $x$: $\mu = e^{\int \frac{M_y - N_x}{N}dx}$
- Si $\frac{N_x - M_y}{M}$ depende solo de $y$: $\mu = e^{\int \frac{N_x - M_y}{M}dy}$

## Teorema de Existencia y Unicidad

Si $f(x,y)$ y $\frac{\partial f}{\partial y}$ son continuas en una región que contiene $(x_0, y_0)$, entonces el PVI:
$$\frac{dy}{dx} = f(x,y), \quad y(x_0) = y_0$$
tiene solución única en algún intervalo que contiene a $x_0$.
