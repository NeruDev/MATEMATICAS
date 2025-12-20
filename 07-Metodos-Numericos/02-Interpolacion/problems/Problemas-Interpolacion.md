<!--
content_type: problems
topic: Interpolación
---
-->

# Problemas: Interpolación

---

## Sección 1: Interpolación de Lagrange

**Problema 1.** Usar la fórmula de Lagrange para encontrar el polinomio que interpola los puntos $(0, 1)$, $(1, 0)$, $(2, 1)$.

**Problema 2.** Dados los puntos $(-1, 4)$, $(0, 1)$, $(1, 0)$, $(2, 1)$:
a) Encontrar el polinomio de Lagrange
b) Evaluar $P(0.5)$

**Problema 3.** Construir el polinomio de interpolación de grado 2 para $f(x) = \ln(x)$ usando $x = 1, 2, 4$ y estimar $\ln(3)$.

**Problema 4.** Demostrar que $\sum_{i=0}^{n} L_i(x) = 1$ para cualquier $x$.

---

## Sección 2: Diferencias Divididas

**Problema 5.** Construir la tabla de diferencias divididas para los puntos $(0, -1)$, $(1, 1)$, $(3, 7)$, $(4, 13)$ y escribir el polinomio de Newton.

**Problema 6.** Para $f(x) = x^3$, calcular:
a) $f[0, 1]$
b) $f[0, 1, 2]$
c) $f[0, 1, 2, 3]$

**Problema 7.** Demostrar que $f[x_0, x_1, ..., x_n]$ es simétrica (invariante ante permutaciones).

**Problema 8.** Si $f(x) = a_0 + a_1x + ... + a_nx^n$, demostrar que $f[x_0, ..., x_n] = a_n$.

---

## Sección 3: Datos Equiespaciados

**Problema 9.** Construir la tabla de diferencias finitas para:

| $x$ | 0 | 1 | 2 | 3 | 4 |
|-----|---|---|---|---|---|
| $y$ | 1 | 1 | 2 | 6 | 24 |

y escribir el polinomio de Newton progresivo.

**Problema 10.** Usar Newton regresivo para interpolar hacia atrás con los datos:

| $x$ | 1.0 | 1.1 | 1.2 | 1.3 |
|-----|-----|-----|-----|-----|
| $y$ | 0.841 | 0.891 | 0.932 | 0.964 |

Estimar $y(1.25)$.

**Problema 11.** La siguiente tabla da $f(x) = \sin(x)$:

| $x$ | 0.0 | 0.2 | 0.4 | 0.6 |
|-----|-----|-----|-----|-----|
| $f(x)$ | 0.0 | 0.1987 | 0.3894 | 0.5646 |

Usar Newton progresivo para estimar $\sin(0.15)$.

---

## Sección 4: Error de Interpolación

**Problema 12.** Acotar el error de interpolación lineal ($n=1$) de $f(x) = e^x$ en $[0, 1]$ con puntos $x_0 = 0$, $x_1 = 1$.

**Problema 13.** Para $f(x) = \sin(x)$ interpolada en $0, \pi/4, \pi/2$:
a) Escribir el polinomio interpolante
b) Acotar el error en $[0, \pi/2]$

**Problema 14.** Explicar el fenómeno de Runge para $f(x) = \frac{1}{1+25x^2}$ en $[-1, 1]$. ¿Por qué empeora al aumentar $n$?

**Problema 15.** Calcular los nodos de Chebyshev para $n = 3$ en $[-1, 1]$ y compararlos con nodos equiespaciados.

---

## Sección 5: Splines Cúbicos

**Problema 16.** Encontrar el spline cúbico natural para los puntos $(0, 0)$, $(1, 1)$, $(2, 0)$.

**Problema 17.** Para los datos $(0, 1)$, $(1, 2)$, $(2, 3)$, $(3, 0)$:
a) Construir el spline cúbico natural
b) Evaluar $S(1.5)$

**Problema 18.** Comparar la interpolación polinómica de grado 4 vs spline cúbico para:

| $x$ | 0 | 1 | 2 | 3 | 4 |
|-----|---|---|---|---|---|
| $y$ | 0 | 1 | 4 | 1 | 0 |

**Problema 19.** ¿Por qué los splines cúbicos evitan el fenómeno de Runge?

---

## Sección 6: Interpolación de Hermite

**Problema 20.** Encontrar el polinomio de Hermite que interpola:
- $f(0) = 1$, $f'(0) = 2$
- $f(1) = 2$, $f'(1) = 0$

**Problema 21.** Construir la interpolación de Hermite para $f(x) = e^x$ en $x = 0, 1$ usando valores y derivadas exactas.

---

## Sección 7: Problemas Aplicados

**Problema 22.** (Tabla de densidades) La densidad del agua a diferentes temperaturas es:

| T (°C) | 0 | 20 | 40 | 60 | 80 | 100 |
|--------|---|----|----|----|----|-----|
| ρ (g/cm³) | 0.9999 | 0.9982 | 0.9922 | 0.9832 | 0.9718 | 0.9584 |

Estimar la densidad a 50°C usando:
a) Interpolación de Lagrange (grado 2, puntos cercanos)
b) Spline cúbico

**Problema 23.** (Trayectoria de proyectil) Las posiciones medidas de un proyectil son:

| $t$ (s) | 0 | 1 | 2 | 3 |
|---------|---|---|---|---|
| $x$ (m) | 0 | 8 | 14 | 18 |

a) Interpolar con un polinomio de grado 3
b) Estimar la posición en $t = 1.5$ s
c) Estimar la velocidad en $t = 1.5$ s (derivar el polinomio)

**Problema 24.** (Diseño de carreteras) Una curva de carretera debe pasar por los puntos $(0, 0)$, $(100, 10)$, $(200, 0)$ con pendiente 0 en los extremos. Usar spline cúbico sujeto.

---

## Sección 8: Problemas de Implementación

**Problema 25.** Implementar en Python/MATLAB:
a) Función para calcular diferencias divididas
b) Función para evaluar el polinomio de Newton

**Problema 26.** Crear un programa que:
a) Tome $n$ puntos como entrada
b) Construya el spline cúbico natural
c) Grafique el spline junto con los puntos originales

**Problema 27.** Comparar numéricamente Lagrange vs Newton para $n = 10, 20, 50$ puntos aleatorios. ¿Hay diferencia en precisión o tiempo?

---

## Sección 9: Problemas Teóricos

**Problema 28.** Demostrar que el polinomio de Lagrange y el de Newton son idénticos.

**Problema 29.** Demostrar la fórmula del error:
$$f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x - x_i)$$

**Problema 30.** Demostrar que un spline cúbico natural minimiza $\int_a^b [S''(x)]^2 dx$ entre todas las funciones interpolantes con segunda derivada continua.
