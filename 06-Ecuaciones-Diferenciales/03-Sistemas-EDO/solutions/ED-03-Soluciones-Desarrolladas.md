<!--
::METADATA::
type: solution
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Soluciones: Sistemas de EDO

---

## Problema 1a
**Sistema:** $\begin{cases} x' = 3x - 2y \\ y' = x + y \end{cases}$

**Solución:**
$$\mathbf{X}' = \begin{pmatrix} 3 & -2 \\ 1 & 1 \end{pmatrix}\mathbf{X}$$

---

## Problema 2a
**[EDO](../../..](../../../glossary.md)#edo):** $y'' + 4y' + 3y = 0$

**Solución:**
Sea $x_1 = y$, $x_2 = y'$

$x_1' = x_2$

$x_2' = y'' = -4y' - 3y = -3x_1 - 4x_2$

$$\mathbf{X}' = \begin{pmatrix} 0 & 1 \\ -3 & -4 \end{pmatrix}\mathbf{X}$$

---

## Problema 3a
**Sistema:** $\mathbf{X}' = \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix}\mathbf{X}$

**Solución:**
$\det(A - \lambda I) = (1-\lambda)(2-\lambda) - 6 = \lambda^2 - 3\lambda - 4 = 0$

$(\lambda - 4)(\lambda + 1) = 0 \Rightarrow \lambda_1 = 4, \lambda_2 = -1$

Para $\lambda_1 = 4$: $\begin{pmatrix} -3 & 2 \\ 3 & -2 \end{pmatrix}\mathbf{v} = 0 \Rightarrow \mathbf{v}_1 = \begin{pmatrix} 2 \\ 3 \end{pmatrix}$

Para $\lambda_2 = -1$: $\begin{pmatrix} 2 & 2 \\ 3 & 3 \end{pmatrix}\mathbf{v} = 0 \Rightarrow \mathbf{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$

$$\mathbf{X} = C_1 e^{4t}\begin{pmatrix} 2 \\ 3 \end{pmatrix} + C_2 e^{-t}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$$

---

## Problema 5
**PVI:** $\mathbf{X}' = \begin{pmatrix} 2 & -1 \\ 3 & -2 \end{pmatrix}\mathbf{X}$, $\mathbf{X}(0) = \begin{pmatrix} 1 \\ 4 \end{pmatrix}$

**Solución:**
$\det(A - \lambda I) = (2-\lambda)(-2-\lambda) + 3 = \lambda^2 - 1 = 0$

$\lambda_1 = 1$, $\lambda_2 = -1$

$\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, $\mathbf{v}_2 = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$

$\mathbf{X}(0)$: $C_1\begin{pmatrix} 1 \\ 1 \end{pmatrix} + C_2\begin{pmatrix} 1 \\ 3 \end{pmatrix} = \begin{pmatrix} 1 \\ 4 \end{pmatrix}$

$C_1 + C_2 = 1$, $C_1 + 3C_2 = 4$

$2C_2 = 3 \Rightarrow C_2 = \frac{3}{2}$, $C_1 = -\frac{1}{2}$

$$\mathbf{X} = -\frac{1}{2}e^{t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + \frac{3}{2}e^{-t}\begin{pmatrix} 1 \\ 3 \end{pmatrix}$$

---

## Problema 6a
**Sistema:** $\mathbf{X}' = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\mathbf{X}$

**Solución:**
$\lambda^2 + 1 = 0 \Rightarrow \lambda = \pm i$

Para $\lambda = i$: $\begin{pmatrix} -i & 1 \\ -1 & -i \end{pmatrix}\mathbf{v} = 0$

$\mathbf{v} = \begin{pmatrix} 1 \\ i \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} + i\begin{pmatrix} 0 \\ 1 \end{pmatrix}$

$\alpha = 0$, $\beta = 1$, $\mathbf{a} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $\mathbf{b} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$

$$\mathbf{X} = C_1\begin{pmatrix} \cos t \\ -\sin t \end{pmatrix} + C_2\begin{pmatrix} \sin t \\ \cos t \end{pmatrix}$$

---

## Problema 9a
**Sistema:** $\mathbf{X}' = \begin{pmatrix} 3 & -1 \\ 1 & 1 \end{pmatrix}\mathbf{X}$

**Solución:**
$\det(A - \lambda I) = (3-\lambda)(1-\lambda) + 1 = \lambda^2 - 4\lambda + 4 = 0$

$(\lambda - 2)^2 = 0 \Rightarrow \lambda = 2$ (doble)

Eigenvector: $\begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix}\mathbf{v} = 0 \Rightarrow \mathbf{v} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$

[Vector](../../..](../../../glossary.md)#vector) generalizado: $\begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix}\mathbf{w} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$

$w_1 - w_2 = 1 \Rightarrow \mathbf{w} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$

$$\mathbf{X} = C_1 e^{2t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + C_2 e^{2t}\left[t\begin{pmatrix} 1 \\ 1 \end{pmatrix} + \begin{pmatrix} 1 \\ 0 \end{pmatrix}\right]$$

---

## Problema 12a
**[Matriz](../../..](../../../glossary.md)#matriz):** $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$

**Solución:**
$\tau = 5$, $\Delta = 4 - 6 = -2$

$\Delta < 0$ → **Punto silla** (inestable)

---

## Problema 12c
**[Matriz](../../..](../../../glossary.md)#matriz):** $A = \begin{pmatrix} 0 & 1 \\ -4 & 0 \end{pmatrix}$

**Solución:**
$\tau = 0$, $\Delta = 4 > 0$

$\tau = 0$ y $\Delta > 0$ → **Centro** (estable, no asintóticamente)

---

## Problema 15b
**Matriz:** $A = \begin{pmatrix} 0 & 1 \\ -2 & 3 \end{pmatrix}$

**Solución:**
$\lambda^2 - 3\lambda + 2 = 0 \Rightarrow \lambda_1 = 1, \lambda_2 = 2$

$\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, $\mathbf{v}_2 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$

$P = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$, $P^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$

$$e^{At} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} e^t & 0 \\ 0 & e^{2t} \end{pmatrix}\begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$$

$$e^{At} = \begin{pmatrix} 2e^t - e^{2t} & -e^t + e^{2t} \\ 2e^t - 2e^{2t} & -e^t + 2e^{2t} \end{pmatrix}$$

---

## Problema 17
**Matriz:** $A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$

**Solución:**
$\lambda = \pm i$

Para $\lambda = i$: $\mathbf{v} = \begin{pmatrix} 1 \\ i \end{pmatrix}$

Usando la forma de solución compleja:

$$e^{At} = \begin{pmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{pmatrix}$$

Esta es la **matriz de rotación** por ángulo $t$ (en sentido antihorario).

---

## Problema 20
**Tanques interconectados**

a) $\frac{dx_1}{dt} = -\frac{4}{100}x_1 + \frac{1}{100}x_2 = -0.04x_1 + 0.01x_2$

$\frac{dx_2}{dt} = \frac{4}{100}x_1 - \frac{4}{100}x_2 = 0.04x_1 - 0.04x_2$

$$\mathbf{X}' = \begin{pmatrix} -0.04 & 0.01 \\ 0.04 & -0.04 \end{pmatrix}\mathbf{X}$$

b) Eigenvalores: $\lambda^2 + 0.08\lambda + 0.0012 = 0$

$\lambda_1 = -0.02$, $\lambda_2 = -0.06$

Eigenvectores: $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$, $\mathbf{v}_2 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}$

Con $\mathbf{X}(0) = \begin{pmatrix} 10 \\ 10 \end{pmatrix}$:

$C_1 = 7.5$, $C_2 = 2.5$

$$x_1(t) = 7.5e^{-0.02t} + 2.5e^{-0.06t}$$
$$x_2(t) = 15e^{-0.02t} - 5e^{-0.06t}$$

---

## Problema 23
**Circuito eléctrico**

a) $\mathbf{I}' = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}\mathbf{I}$

b) $\lambda^2 + 2\lambda = 0 \Rightarrow \lambda_1 = 0, \lambda_2 = -2$

$\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, $\mathbf{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$

Con $\mathbf{I}(0) = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$:

$C_1 + C_2 = 1$, $C_1 - C_2 = 0$

$C_1 = C_2 = \frac{1}{2}$

$$i_1(t) = \frac{1}{2} + \frac{1}{2}e^{-2t}$$
$$i_2(t) = \frac{1}{2} - \frac{1}{2}e^{-2t}$$

Cuando $t \to \infty$: $i_1 = i_2 = 0.5$ A (corrientes iguales)
