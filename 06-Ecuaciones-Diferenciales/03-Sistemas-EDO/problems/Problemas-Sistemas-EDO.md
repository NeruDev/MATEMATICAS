<!--
content_type: problems
topic: Sistemas de EDO
---
-->

# Problemas: Sistemas de EDO

---

## 3.1 Forma Matricial

**Problema 1.** Escribir en forma matricial $\mathbf{X}' = A\mathbf{X}$:

a) $\begin{cases} x' = 3x - 2y \\ y' = x + y \end{cases}$

b) $\begin{cases} x' = x + 2y - z \\ y' = 3x - y + 2z \\ z' = -x + y + z \end{cases}$

**Problema 2.** Convertir a sistema de primer orden:

a) $y'' + 4y' + 3y = 0$

b) $y''' - 2y'' + y' = 0$

c) $y'' + \omega^2 y = 0$ (oscilador armónico)

---

## 3.2 Eigenvalores Reales Distintos

**Problema 3.** Resolver los sistemas:

a) $\mathbf{X}' = \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix}\mathbf{X}$

b) $\mathbf{X}' = \begin{pmatrix} 3 & -1 \\ 4 & -2 \end{pmatrix}\mathbf{X}$

c) $\mathbf{X}' = \begin{pmatrix} 5 & 3 \\ -6 & -4 \end{pmatrix}\mathbf{X}$

**Problema 4.** Resolver los sistemas:

a) $\mathbf{X}' = \begin{pmatrix} 1 & 1 \\ 4 & 1 \end{pmatrix}\mathbf{X}$

b) $\mathbf{X}' = \begin{pmatrix} -2 & 1 \\ 1 & -2 \end{pmatrix}\mathbf{X}$

**Problema 5.** Resolver el PVI:

$\mathbf{X}' = \begin{pmatrix} 2 & -1 \\ 3 & -2 \end{pmatrix}\mathbf{X}$, $\mathbf{X}(0) = \begin{pmatrix} 1 \\ 4 \end{pmatrix}$

---

## 3.3 Eigenvalores Complejos

**Problema 6.** Resolver los sistemas:

a) $\mathbf{X}' = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\mathbf{X}$

b) $\mathbf{X}' = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}\mathbf{X}$

c) $\mathbf{X}' = \begin{pmatrix} -1 & 2 \\ -1 & -1 \end{pmatrix}\mathbf{X}$

**Problema 7.** Resolver:

a) $\mathbf{X}' = \begin{pmatrix} 2 & -5 \\ 1 & -2 \end{pmatrix}\mathbf{X}$

b) $\mathbf{X}' = \begin{pmatrix} 4 & -2 \\ 5 & 2 \end{pmatrix}\mathbf{X}$

**Problema 8.** Resolver el PVI:

$\mathbf{X}' = \begin{pmatrix} 1 & -2 \\ 1 & 3 \end{pmatrix}\mathbf{X}$, $\mathbf{X}(0) = \begin{pmatrix} 2 \\ 0 \end{pmatrix}$

---

## 3.4 Eigenvalores Repetidos

**Problema 9.** Resolver los sistemas:

a) $\mathbf{X}' = \begin{pmatrix} 3 & -1 \\ 1 & 1 \end{pmatrix}\mathbf{X}$

b) $\mathbf{X}' = \begin{pmatrix} 1 & 1 \\ -1 & 3 \end{pmatrix}\mathbf{X}$

c) $\mathbf{X}' = \begin{pmatrix} -1 & 1 \\ -1 & -3 \end{pmatrix}\mathbf{X}$

**Problema 10.** Resolver:

a) $\mathbf{X}' = \begin{pmatrix} 5 & -4 \\ 1 & 1 \end{pmatrix}\mathbf{X}$

b) $\mathbf{X}' = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}\mathbf{X}$

**Problema 11.** Resolver el PVI:

$\mathbf{X}' = \begin{pmatrix} 3 & 1 \\ -1 & 1 \end{pmatrix}\mathbf{X}$, $\mathbf{X}(0) = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$

---

## 3.5 Retratos de Fase

**Problema 12.** Clasificar el punto de equilibrio (nodo, silla, espiral, centro):

a) $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$

b) $A = \begin{pmatrix} -1 & 2 \\ -1 & -1 \end{pmatrix}$

c) $A = \begin{pmatrix} 0 & 1 \\ -4 & 0 \end{pmatrix}$

d) $A = \begin{pmatrix} -3 & 1 \\ -2 & -1 \end{pmatrix}$

**Problema 13.** Para cada sistema, determinar si el origen es estable, asintóticamente estable o inestable:

a) $\mathbf{X}' = \begin{pmatrix} -2 & 1 \\ 0 & -3 \end{pmatrix}\mathbf{X}$

b) $\mathbf{X}' = \begin{pmatrix} 1 & -5 \\ 1 & -1 \end{pmatrix}\mathbf{X}$

c) $\mathbf{X}' = \begin{pmatrix} 0 & -2 \\ 2 & 0 \end{pmatrix}\mathbf{X}$

**Problema 14.** Esbozar el retrato de fase para:

a) $\begin{cases} x' = x \\ y' = -2y \end{cases}$

b) $\begin{cases} x' = -x - y \\ y' = x - y \end{cases}$

---

## 3.6 Matriz Exponencial

**Problema 15.** Calcular $e^{At}$ por diagonalización:

a) $A = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$

b) $A = \begin{pmatrix} 0 & 1 \\ -2 & 3 \end{pmatrix}$

c) $A = \begin{pmatrix} 1 & 1 \\ 4 & 1 \end{pmatrix}$

**Problema 16.** Usar $e^{At}$ para resolver el PVI:

$\mathbf{X}' = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}\mathbf{X}$, $\mathbf{X}(0) = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$

**Problema 17.** Calcular $e^{At}$ para:

$A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$

y verificar que coincide con la matriz de rotación.

---

## 3.7 Sistemas 3×3

**Problema 18.** Resolver:

$\mathbf{X}' = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}\mathbf{X}$

**Problema 19.** Resolver:

$\mathbf{X}' = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -6 & 11 & -6 \end{pmatrix}\mathbf{X}$

---

## 3.8 Aplicaciones

**Problema 20.** (Tanques interconectados) Dos tanques de 100 L cada uno están conectados. El tanque 1 recibe agua pura a 3 L/min. La mezcla fluye del tanque 1 al 2 a 4 L/min, del tanque 2 al 1 a 1 L/min, y sale del tanque 2 a 3 L/min. Sea $x_1(t)$ y $x_2(t)$ las cantidades de sal.

a) Escribir el sistema de EDO

b) Si inicialmente hay 10 kg de sal en cada tanque, encontrar $x_1(t)$ y $x_2(t)$

**Problema 21.** (Osciladores acoplados) Dos masas iguales $m$ están conectadas por resortes de constante $k$. Las ecuaciones son:
$$m\ddot{x}_1 = -2kx_1 + kx_2$$
$$m\ddot{x}_2 = kx_1 - 2kx_2$$

a) Escribir como sistema de primer orden

b) Encontrar las frecuencias naturales (modos normales)

**Problema 22.** (Competencia de especies) Dos especies compiten según:
$$\begin{cases} x' = x(2 - x - y) \\ y' = y(3 - 2x - y) \end{cases}$$

Linearizar cerca del punto de equilibrio $(1, 1)$ y clasificarlo.

**Problema 23.** (Circuito eléctrico) Un circuito tiene dos mallas con:
$$L_1\frac{di_1}{dt} + R(i_1 - i_2) = E$$
$$L_2\frac{di_2}{dt} + R(i_2 - i_1) = 0$$

Con $L_1 = L_2 = 1$ H, $R = 1$ Ω, $E = 0$:

a) Escribir en forma matricial

b) Resolver con $i_1(0) = 1$ A, $i_2(0) = 0$
