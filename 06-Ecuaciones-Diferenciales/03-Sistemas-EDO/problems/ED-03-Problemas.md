---
content_type: problem_set
topic_id: ed-03-sistemas-edo
file_id: ED-03-Problemas
---

# Problemas: Sistemas de EDO

---

## 3.1 Forma Matricial

### [Prob-01] Conversión a Forma Matricial ⭐

Escribir en forma matricial $\mathbf{X}' = A\mathbf{X}$:

a) $\begin{cases} x' = 3x - 2y \\ y' = x + y \end{cases}$

b) $\begin{cases} x' = x + 2y - z \\ y' = 3x - y + 2z \\ z' = -x + y + z \end{cases}$

> 📂 **Solución:** [solutions/prob-01/](../solutions/prob-01/)

---

### [Prob-02] Reducción a Sistema de Primer Orden ⭐

Convertir a sistema de primer orden:

a) $y'' + 4y' + 3y = 0$

b) $y''' - 2y'' + y' = 0$

c) $y'' + \omega^2 y = 0$ (oscilador armónico)

> 📂 **Solución:** [solutions/prob-02/](../solutions/prob-02/)

---

## 3.2 Eigenvalores Reales Distintos

### [Prob-03] Sistemas con Eigenvalores Reales Distintos ⭐⭐

Resolver los sistemas:

a) $\mathbf{X}' = \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix}\mathbf{X}$

b) $\mathbf{X}' = \begin{pmatrix} 3 & -1 \\ 4 & -2 \end{pmatrix}\mathbf{X}$

c) $\mathbf{X}' = \begin{pmatrix} 5 & 3 \\ -6 & -4 \end{pmatrix}\mathbf{X}$

> 📂 **Solución:** [solutions/prob-03/](../solutions/prob-03/)

---

### [Prob-04] Sistemas 2×2 Eigenvalores Reales ⭐⭐

Resolver los sistemas:

a) $\mathbf{X}' = \begin{pmatrix} 1 & 1 \\ 4 & 1 \end{pmatrix}\mathbf{X}$

b) $\mathbf{X}' = \begin{pmatrix} -2 & 1 \\ 1 & -2 \end{pmatrix}\mathbf{X}$

> 📂 **Solución:** [solutions/prob-04/](../solutions/prob-04/)

---

### [Prob-05] PVI con Eigenvalores Reales Distintos ⭐⭐

Resolver el PVI:

$\mathbf{X}' = \begin{pmatrix} 2 & -1 \\ 3 & -2 \end{pmatrix}\mathbf{X}$, $\mathbf{X}(0) = \begin{pmatrix} 1 \\ 4 \end{pmatrix}$

> 📂 **Solución:** [solutions/prob-05/](../solutions/prob-05/)

---

## 3.3 Eigenvalores Complejos

### [Prob-06] Sistemas con Eigenvalores Complejos ⭐⭐

Resolver los sistemas:

a) $\mathbf{X}' = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\mathbf{X}$

b) $\mathbf{X}' = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}\mathbf{X}$

c) $\mathbf{X}' = \begin{pmatrix} -1 & 2 \\ -1 & -1 \end{pmatrix}\mathbf{X}$

> 📂 **Solución:** [solutions/prob-06/](../solutions/prob-06/)

---

### [Prob-07] Sistemas con Eigenvalores Complejos Adicionales ⭐⭐

Resolver:

a) $\mathbf{X}' = \begin{pmatrix} 2 & -5 \\ 1 & -2 \end{pmatrix}\mathbf{X}$

b) $\mathbf{X}' = \begin{pmatrix} 4 & -2 \\ 5 & 2 \end{pmatrix}\mathbf{X}$

> 📂 **Solución:** [solutions/prob-07/](../solutions/prob-07/)

---

### [Prob-08] PVI con Eigenvalores Complejos ⭐⭐

Resolver el PVI:

$\mathbf{X}' = \begin{pmatrix} 1 & -2 \\ 1 & 3 \end{pmatrix}\mathbf{X}$, $\mathbf{X}(0) = \begin{pmatrix} 2 \\ 0 \end{pmatrix}$

> 📂 **Solución:** [solutions/prob-08/](../solutions/prob-08/)

---

## 3.4 Eigenvalores Repetidos

### [Prob-09] Sistemas con Eigenvalores Repetidos ⭐⭐

Resolver los sistemas:

a) $\mathbf{X}' = \begin{pmatrix} 3 & -1 \\ 1 & 1 \end{pmatrix}\mathbf{X}$

b) $\mathbf{X}' = \begin{pmatrix} 1 & 1 \\ -1 & 3 \end{pmatrix}\mathbf{X}$

c) $\mathbf{X}' = \begin{pmatrix} -1 & 1 \\ -1 & -3 \end{pmatrix}\mathbf{X}$

> 📂 **Solución:** [solutions/prob-09/](../solutions/prob-09/)

---

### [Prob-10] Sistemas Defectivos ⭐⭐

Resolver:

a) $\mathbf{X}' = \begin{pmatrix} 5 & -4 \\ 1 & 1 \end{pmatrix}\mathbf{X}$

b) $\mathbf{X}' = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}\mathbf{X}$

> 📂 **Solución:** [solutions/prob-10/](../solutions/prob-10/)

---

### [Prob-11] PVI con Eigenvalores Repetidos ⭐⭐

Resolver el PVI:

$\mathbf{X}' = \begin{pmatrix} 3 & 1 \\ -1 & 1 \end{pmatrix}\mathbf{X}$, $\mathbf{X}(0) = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$

> 📂 **Solución:** [solutions/prob-11/](../solutions/prob-11/)

---

## 3.5 Retratos de Fase

### [Prob-12] Clasificación de Puntos de Equilibrio ⭐⭐

Clasificar el punto de equilibrio (nodo, silla, espiral, centro):

a) $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$

b) $A = \begin{pmatrix} -1 & 2 \\ -1 & -1 \end{pmatrix}$

c) $A = \begin{pmatrix} 0 & 1 \\ -4 & 0 \end{pmatrix}$

d) $A = \begin{pmatrix} -3 & 1 \\ -2 & -1 \end{pmatrix}$

> 📂 **Solución:** [solutions/prob-12/](../solutions/prob-12/)

---

### [Prob-13] Análisis de Estabilidad ⭐⭐

Para cada sistema, determinar si el origen es estable, asintóticamente estable o inestable:

a) $\mathbf{X}' = \begin{pmatrix} -2 & 1 \\ 0 & -3 \end{pmatrix}\mathbf{X}$

b) $\mathbf{X}' = \begin{pmatrix} 1 & -5 \\ 1 & -1 \end{pmatrix}\mathbf{X}$

c) $\mathbf{X}' = \begin{pmatrix} 0 & -2 \\ 2 & 0 \end{pmatrix}\mathbf{X}$

> 📂 **Solución:** [solutions/prob-13/](../solutions/prob-13/)

---

### [Prob-14] Esbozo de Retrato de Fase ⭐⭐

Esbozar el retrato de fase para:

a) $\begin{cases} x' = x \\ y' = -2y \end{cases}$

b) $\begin{cases} x' = -x - y \\ y' = x - y \end{cases}$

> 📂 **Solución:** [solutions/prob-14/](../solutions/prob-14/)

---

## 3.6 Matriz Exponencial

### [Prob-15] Cálculo de Matriz Exponencial por Diagonalización ⭐⭐⭐

Calcular $e^{At}$ por diagonalización:

a) $A = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$

b) $A = \begin{pmatrix} 0 & 1 \\ -2 & 3 \end{pmatrix}$

c) $A = \begin{pmatrix} 1 & 1 \\ 4 & 1 \end{pmatrix}$

> 📂 **Solución:** [solutions/prob-15/](../solutions/prob-15/)

---

### [Prob-16] PVI usando Matriz Exponencial ⭐⭐⭐

Usar $e^{At}$ para resolver el PVI:

$\mathbf{X}' = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}\mathbf{X}$, $\mathbf{X}(0) = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$

> 📂 **Solución:** [solutions/prob-16/](../solutions/prob-16/)

---

### [Prob-17] Matriz Exponencial y Rotación ⭐⭐⭐

Calcular $e^{At}$ para:

$A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$

y verificar que coincide con la matriz de rotación.

> 📂 **Solución:** [solutions/prob-17/](../solutions/prob-17/)

---

## 3.7 Sistemas 3×3

### [Prob-18] Sistema Diagonal 3×3 ⭐

Resolver:

$\mathbf{X}' = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}\mathbf{X}$

> 📂 **Solución:** [solutions/prob-18/](../solutions/prob-18/)

---

### [Prob-19] Sistema 3×3 General ⭐⭐⭐

Resolver:

$\mathbf{X}' = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -6 & 11 & -6 \end{pmatrix}\mathbf{X}$

> 📂 **Solución:** [solutions/prob-19/](../solutions/prob-19/)

---

## 3.8 Aplicaciones

### [Prob-20] Tanques Interconectados ⭐⭐⭐

Dos tanques de 100 L cada uno están conectados. El tanque 1 recibe agua pura a 3 L/min. La mezcla fluye del tanque 1 al 2 a 4 L/min, del tanque 2 al 1 a 1 L/min, y sale del tanque 2 a 3 L/min. Sea $x_1(t)$ y $x_2(t)$ las cantidades de sal.

a) Escribir el sistema de EDO

b) Si inicialmente hay 10 kg de sal en cada tanque, encontrar $x_1(t)$ y $x_2(t)$

> 📂 **Solución:** [solutions/prob-20/](../solutions/prob-20/)

---

### [Prob-21] Osciladores Acoplados ⭐⭐⭐

Dos masas iguales $m$ están conectadas por resortes de constante $k$. Las ecuaciones son:
$$m\ddot{x}_1 = -2kx_1 + kx_2$$
$$m\ddot{x}_2 = kx_1 - 2kx_2$$

a) Escribir como sistema de primer orden

b) Encontrar las frecuencias naturales (modos normales)

> 📂 **Solución:** [solutions/prob-21/](../solutions/prob-21/)

---

### [Prob-22] Competencia de Especies ⭐⭐⭐

Dos especies compiten según:
$$\begin{cases} x' = x(2 - x - y) \\ y' = y(3 - 2x - y) \end{cases}$$

Linearizar cerca del punto de equilibrio $(1, 1)$ y clasificarlo.

> 📂 **Solución:** [solutions/prob-22/](../solutions/prob-22/)

---

### [Prob-23] Circuito Eléctrico con Dos Mallas ⭐⭐⭐

Un circuito tiene dos mallas con:
$$L_1\frac{di_1}{dt} + R(i_1 - i_2) = E$$
$$L_2\frac{di_2}{dt} + R(i_2 - i_1) = 0$$

Con $L_1 = L_2 = 1$ H, $R = 1$ Ω, $E = 0$:

a) Escribir en forma matricial

b) Resolver con $i_1(0) = 1$ A, $i_2(0) = 0$

> 📂 **Solución:** [solutions/prob-23/](../solutions/prob-23/)
