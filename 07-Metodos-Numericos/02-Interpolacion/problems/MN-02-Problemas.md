<!--
---
content_type: problem_set
topic_id: mn-02-interpolacion
file_id: MN-02-Problemas
title: "Problemas: [Interpolación](../../../glossary.md#interpolacion)"
---
-->

# Problemas: Interpolación

---

## Sección 1: Interpolación de Lagrange

### [Prob-01] Polinomio de Lagrange básico ⭐
> **Solución:** [solutions/prob-01/](../solutions/prob-01/)

Usar la fórmula de Lagrange para encontrar el [polinomio](../../../glossary.md#polinomio) que interpola los puntos $(0, 1)$, $(1, 0)$, $(2, 1)$.

---

### [Prob-02] Polinomio de Lagrange y evaluación ⭐⭐
> **Solución:** [solutions/prob-02/](../solutions/prob-02/)

Dados los puntos $(-1, 4)$, $(0, 1)$, $(1, 0)$, $(2, 1)$:
a) Encontrar el [polinomio de Lagrange](../../../glossary.md#polinomio-de-lagrange)
b) Evaluar $P(0.5)$

---

### [Prob-03] Interpolación de función logarítmica ⭐⭐
> **Solución:** [solutions/prob-03/](../solutions/prob-03/)

Construir el [polinomio](../../../glossary.md#polinomio) de [interpolación](../../../glossary.md#interpolacion) de grado 2 para $f(x) = \ln(x)$ usando $x = 1, 2, 4$ y estimar $\ln(3)$.

---

### [Prob-04] Propiedad de suma de polinomios base ⭐⭐⭐
> **Solución:** [solutions/prob-04/](../solutions/prob-04/)

Demostrar que $\sum_{i=0}^{n} L_i(x) = 1$ para cualquier $x$.

---

## Sección 2: Diferencias Divididas

### [Prob-05] Tabla de diferencias divididas ⭐⭐
> **Solución:** [solutions/prob-05/](../solutions/prob-05/)

Construir la tabla de [diferencias divididas](../../../glossary.md#diferencias-divididas) para los puntos $(0, -1)$, $(1, 1)$, $(3, 7)$, $(4, 13)$ y escribir el polinomio de Newton.

---

### [Prob-06] Diferencias divididas de función cúbica ⭐⭐
> **Solución:** [solutions/prob-06/](../solutions/prob-06/)

Para $f(x) = x^3$, calcular:
a) $f[0, 1]$
b) $f[0, 1, 2]$
c) $f[0, 1, 2, 3]$

---

### [Prob-07] Simetría de diferencias divididas ⭐⭐⭐
> **Solución:** [solutions/prob-07/](../solutions/prob-07/)

Demostrar que $f[x_0, x_1, ..., x_n]$ es simétrica ([invariante](../../../glossary.md#invariante) ante permutaciones).

---

### [Prob-08] Diferencia dividida de polinomio ⭐⭐⭐
> **Solución:** [solutions/prob-08/](../solutions/prob-08/)

Si $f(x) = a_0 + a_1x + ... + a_nx^n$, demostrar que $f[x_0, ..., x_n] = a_n$.

---

## Sección 3: Datos Equiespaciados

### [Prob-09] Newton progresivo con diferencias finitas ⭐⭐
> **Solución:** [solutions/prob-09/](../solutions/prob-09/)

Construir la tabla de diferencias finitas para:

| $x$ | 0 | 1 | 2 | 3 | 4 |
|-----|---|---|---|---|---|
| $y$ | 1 | 1 | 2 | 6 | 24 |

y escribir el polinomio de Newton progresivo.

---

### [Prob-10] Newton regresivo ⭐⭐
> **Solución:** [solutions/prob-10/](../solutions/prob-10/)

Usar Newton regresivo para interpolar hacia atrás con los datos:

| $x$ | 1.0 | 1.1 | 1.2 | 1.3 |
|-----|-----|-----|-----|-----|
| $y$ | 0.841 | 0.891 | 0.932 | 0.964 |

Estimar $y(1.25)$.

---

### [Prob-11] Interpolación de función seno ⭐⭐
> **Solución:** [solutions/prob-11/](../solutions/prob-11/)

La siguiente tabla da $f(x) = \sin(x)$:

| $x$ | 0.0 | 0.2 | 0.4 | 0.6 |
|-----|-----|-----|-----|-----|
| $f(x)$ | 0.0 | 0.1987 | 0.3894 | 0.5646 |

Usar Newton progresivo para estimar $\sin(0.15)$.

---

## Sección 4: Error de Interpolación

### [Prob-12] Error de interpolación lineal ⭐⭐
> **Solución:** [solutions/prob-12/](../solutions/prob-12/)

Acotar el [error de interpolación](../../../glossary.md#error-de-interpolacion) lineal ($n=1$) de $f(x) = e^x$ en $[0, 1]$ con puntos $x_0 = 0$, $x_1 = 1$.

---

### [Prob-13] Error de interpolación del seno ⭐⭐
> **Solución:** [solutions/prob-13/](../solutions/prob-13/)

Para $f(x) = \sin(x)$ interpolada en $0, \pi/4, \pi/2$:
a) Escribir el polinomio interpolante
b) Acotar el error en $[0, \pi/2]$

---

### [Prob-14] Fenómeno de Runge ⭐⭐⭐
> **Solución:** [solutions/prob-14/](../solutions/prob-14/)

Explicar el [fenómeno de Runge](../../../glossary.md#fenomeno-de-runge) para $f(x) = \frac{1}{1+25x^2}$ en $[-1, 1]$. ¿Por qué empeora al aumentar $n$?

---

### [Prob-15] Nodos de Chebyshev ⭐⭐
> **Solución:** [solutions/prob-15/](../solutions/prob-15/)

Calcular los nodos de Chebyshev para $n = 3$ en $[-1, 1]$ y compararlos con nodos equiespaciados.

---

## Sección 5: Splines Cúbicos

### [Prob-16] Spline cúbico natural básico ⭐⭐
> **Solución:** [solutions/prob-16/](../solutions/prob-16/)

Encontrar el [spline cúbico](../../../glossary.md#spline-cubico) natural para los puntos $(0, 0)$, $(1, 1)$, $(2, 0)$.

---

### [Prob-17] Spline cúbico con 4 puntos ⭐⭐
> **Solución:** [solutions/prob-17/](../solutions/prob-17/)

Para los datos $(0, 1)$, $(1, 2)$, $(2, 3)$, $(3, 0)$:
a) Construir el [spline cúbico](../../../glossary.md#spline-cubico) natural
b) Evaluar $S(1.5)$

---

### [Prob-18] Comparación polinomio vs spline ⭐⭐
> **Solución:** [solutions/prob-18/](../solutions/prob-18/)

Comparar la interpolación polinómica de grado 4 vs spline cúbico para:

| $x$ | 0 | 1 | 2 | 3 | 4 |
|-----|---|---|---|---|---|
| $y$ | 0 | 1 | 4 | 1 | 0 |

---

### [Prob-19] Splines y fenómeno de Runge ⭐⭐⭐
> **Solución:** [solutions/prob-19/](../solutions/prob-19/)

¿Por qué los splines cúbicos evitan el [fenómeno de Runge](../../../glossary.md#fenomeno-de-runge)?

---

## Sección 6: Interpolación de Hermite

### [Prob-20] Polinomio de Hermite básico ⭐⭐
> **Solución:** [solutions/prob-20/](../solutions/prob-20/)

Encontrar el polinomio de Hermite que interpola:
- $f(0) = 1$, $f'(0) = 2$
- $f(1) = 2$, $f'(1) = 0$

---

### [Prob-21] Hermite para función exponencial ⭐⭐
> **Solución:** [solutions/prob-21/](../solutions/prob-21/)

Construir la interpolación de Hermite para $f(x) = e^x$ en $x = 0, 1$ usando valores y [derivadas](../../../glossary.md#derivadas) exactas.

---

## Sección 7: Problemas Aplicados

### [Prob-22] Tabla de densidades del agua ⭐⭐
> **Solución:** [solutions/prob-22/](../solutions/prob-22/)

La densidad del agua a diferentes temperaturas es:

| T (°C) | 0 | 20 | 40 | 60 | 80 | 100 |
|--------|---|----|----|----|----|-----|
| ρ (g/cm³) | 0.9999 | 0.9982 | 0.9922 | 0.9832 | 0.9718 | 0.9584 |

Estimar la densidad a 50°C usando:
a) Interpolación de Lagrange (grado 2, puntos cercanos)
b) Spline cúbico

---

### [Prob-23] Trayectoria de proyectil ⭐⭐
> **Solución:** [solutions/prob-23/](../solutions/prob-23/)

Las posiciones medidas de un proyectil son:

| $t$ (s) | 0 | 1 | 2 | 3 |
|---------|---|---|---|---|
| $x$ (m) | 0 | 8 | 14 | 18 |

a) Interpolar con un polinomio de grado 3
b) Estimar la posición en $t = 1.5$ s
c) Estimar la velocidad en $t = 1.5$ s (derivar el polinomio)

---

### [Prob-24] Diseño de curva de carretera ⭐⭐⭐
> **Solución:** [solutions/prob-24/](../solutions/prob-24/)

Una curva de carretera debe pasar por los puntos $(0, 0)$, $(100, 10)$, $(200, 0)$ con pendiente 0 en los extremos. Usar spline cúbico sujeto.

---

## Sección 8: Problemas de Implementación

### [Prob-25] Implementación de diferencias divididas ⭐⭐
> **Solución:** [solutions/prob-25/](../solutions/prob-25/)

Implementar en Python/MATLAB:
a) [Función](../../../glossary.md#funcion) para calcular [diferencias divididas](../../../glossary.md#diferencias-divididas)
b) [Función](../../../glossary.md#funcion) para evaluar el polinomio de Newton

---

### [Prob-26] Programa de spline cúbico ⭐⭐⭐
> **Solución:** [solutions/prob-26/](../solutions/prob-26/)

Crear un programa que:
a) Tome $n$ puntos como entrada
b) Construya el spline cúbico natural
c) Grafique el spline junto con los puntos originales

---

### [Prob-27] Comparación numérica Lagrange vs Newton ⭐⭐⭐
> **Solución:** [solutions/prob-27/](../solutions/prob-27/)

Comparar numéricamente Lagrange vs Newton para $n = 10, 20, 50$ puntos aleatorios. ¿Hay diferencia en precisión o tiempo?

---

## Sección 9: Problemas Teóricos

### [Prob-28] Equivalencia Lagrange-Newton ⭐⭐⭐
> **Solución:** [solutions/prob-28/](../solutions/prob-28/)

Demostrar que el [polinomio de Lagrange](../../../glossary.md#polinomio-de-lagrange) y el de Newton son idénticos.

---

### [Prob-29] Demostración fórmula del error ⭐⭐⭐
> **Solución:** [solutions/prob-29/](../solutions/prob-29/)

Demostrar la fórmula del error:
$$f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x - x_i)$$

---

### [Prob-30] Optimalidad del spline cúbico ⭐⭐⭐
> **Solución:** [solutions/prob-30/](../solutions/prob-30/)

Demostrar que un spline cúbico natural minimiza $\int_a^b [S''(x)]^2 dx$ entre todas las funciones interpolantes con segunda [derivada](../../../glossary.md#derivada) continua.
