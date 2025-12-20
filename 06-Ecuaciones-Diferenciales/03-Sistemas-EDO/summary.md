# Resumen: Sistemas de EDO

## Forma General
$$\mathbf{X}' = A\mathbf{X} + \mathbf{F}(t)$$

donde $\mathbf{X} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}$, $A$ es matriz $n \times n$

## Sistema Homogéneo 2×2
$$\begin{cases} x' = ax + by \\ y' = cx + dy \end{cases} \Rightarrow \mathbf{X}' = \begin{pmatrix} a & b \\ c & d \end{pmatrix}\mathbf{X}$$

## Método de Valores Propios

| Tipo de $\lambda$ | Solución General |
|-------------------|------------------|
| $\lambda_1 \neq \lambda_2$ reales | $\mathbf{X} = C_1 e^{\lambda_1 t}\mathbf{v}_1 + C_2 e^{\lambda_2 t}\mathbf{v}_2$ |
| $\lambda = \alpha \pm \beta i$ | $\mathbf{X} = e^{\alpha t}(C_1\mathbf{u}\cos\beta t + C_2\mathbf{u}\sin\beta t + ...)$ |
| $\lambda$ repetido | $\mathbf{X} = C_1 e^{\lambda t}\mathbf{v} + C_2 e^{\lambda t}(t\mathbf{v} + \mathbf{w})$ |

donde $\mathbf{v}$ = eigenvector, $\mathbf{w}$ = vector generalizado

## Retratos de Fase (2D)

| $\lambda_1, \lambda_2$ | Tipo | Estabilidad |
|------------------------|------|-------------|
| $\lambda_1 < \lambda_2 < 0$ | Nodo estable | Asintóticamente estable |
| $0 < \lambda_1 < \lambda_2$ | Nodo inestable | Inestable |
| $\lambda_1 < 0 < \lambda_2$ | Punto silla | Inestable |
| $\alpha \pm \beta i$, $\alpha < 0$ | Espiral estable | Asintóticamente estable |
| $\alpha \pm \beta i$, $\alpha > 0$ | Espiral inestable | Inestable |
| $\pm \beta i$ | Centro | Estable (no asintótico) |

## Matriz Exponencial
$$\mathbf{X}(t) = e^{At}\mathbf{X}_0$$

Para $A$ diagonalizable: $e^{At} = PDP^{-1}$ donde $D = \text{diag}(e^{\lambda_1 t}, e^{\lambda_2 t}, ...)$
