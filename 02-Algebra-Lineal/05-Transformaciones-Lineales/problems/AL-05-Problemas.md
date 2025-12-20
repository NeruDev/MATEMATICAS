---
content_type: problem_set
topic_id: al-05-transformaciones-lineales
file_id: AL-05-Problemas
title: Problemas de Transformaciones Lineales
description: Conjunto de problemas sobre transformaciones lineales, núcleo, imagen, matrices asociadas, composición e inversa, y cambio de base
author: Repositorio Matemáticas
date_created: 2025-12-20
date_modified: 2025-12-20
version: 1.0
status: migrated
difficulty_distribution:
  basic: 10
  intermediate: 12
  advanced: 6
total_problems: 28
---

# Problemas: Transformaciones Lineales

---

## 5.1 Definición y Verificación

### [Prob-01] Verificación de linealidad en funciones $\mathbb{R}^2 \to \mathbb{R}^2$ ⭐

Determinar si las siguientes funciones son transformaciones lineales:

a) $T: \mathbb{R}^2 \to \mathbb{R}^2$, $T(x, y) = (2x + y, x - 3y)$

b) $T: \mathbb{R}^2 \to \mathbb{R}^2$, $T(x, y) = (x^2, y)$

c) $T: \mathbb{R}^2 \to \mathbb{R}$, $T(x, y) = xy$

d) $T: \mathbb{R}^2 \to \mathbb{R}^2$, $T(x, y) = (x + 1, y)$

> **Solución:** Ver [solutions/prob-01/](../solutions/prob-01/)

---

### [Prob-02] Operador derivada en espacio de polinomios ⭐

Sea $T: P_2 \to P_1$ definida por $T(p(x)) = p'(x)$ (derivada). Verificar que $T$ es lineal.

> **Solución:** Ver [solutions/prob-02/](../solutions/prob-02/)

---

### [Prob-03] Linealidad de la función traza ⭐

Sea $T: M_{2 \times 2} \to \mathbb{R}$ definida por $T(A) = \text{tr}(A)$ (traza). ¿Es $T$ lineal?

> **Solución:** Ver [solutions/prob-03/](../solutions/prob-03/)

---

### [Prob-04] Funcional lineal en espacio de funciones continuas ⭐⭐

Sea $T: C[0,1] \to \mathbb{R}$ definida por $T(f) = f(0) + f(1)$. ¿Es $T$ lineal?

> **Solución:** Ver [solutions/prob-04/](../solutions/prob-04/)

---

### [Prob-05] Valor absoluto y no linealidad ⭐

Sea $T: \mathbb{R}^3 \to \mathbb{R}^3$ definida por $T(x, y, z) = (|x|, y, z)$. ¿Es $T$ lineal?

> **Solución:** Ver [solutions/prob-05/](../solutions/prob-05/)

---

## 5.2 Núcleo e Imagen

### [Prob-06] Núcleo e imagen de $T: \mathbb{R}^3 \to \mathbb{R}^2$ ⭐⭐

Para $T: \mathbb{R}^3 \to \mathbb{R}^2$, $T(x, y, z) = (x - y, y - z)$:

a) Encontrar $\ker(T)$ y su base

b) Encontrar $\text{Im}(T)$ y su base

c) Verificar el teorema del rango-nulidad

> **Solución:** Ver [solutions/prob-06/](../solutions/prob-06/)

---

### [Prob-07] Inyectividad y sobreyectividad de $T: \mathbb{R}^2 \to \mathbb{R}^3$ ⭐⭐

Para $T: \mathbb{R}^2 \to \mathbb{R}^3$, $T(x, y) = (x + y, x - y, 2x)$:

a) Hallar $\ker(T)$

b) Hallar $\text{Im}(T)$

c) ¿Es $T$ inyectiva? ¿Sobreyectiva?

> **Solución:** Ver [solutions/prob-07/](../solutions/prob-07/)

---

### [Prob-08] Derivada en polinomios: núcleo e imagen ⭐⭐

Sea $T: P_3 \to P_2$ definida por $T(p(x)) = p'(x)$. Encontrar:

a) $\ker(T)$

b) $\text{Im}(T)$

c) Verificar rango-nulidad

> **Solución:** Ver [solutions/prob-08/](../solutions/prob-08/)

---

### [Prob-09] Espacios nulo y columna de una matriz ⭐⭐

Para la matriz $A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 3 \end{pmatrix}$, hallar base de:

a) $\text{Nul}(A)$

b) $\text{Col}(A)$

> **Solución:** Ver [solutions/prob-09/](../solutions/prob-09/)

---

### [Prob-10] Dimensiones mediante teorema rango-nulidad ⭐⭐

Sea $T: \mathbb{R}^4 \to \mathbb{R}^3$ con matriz $[T] = \begin{pmatrix} 1 & 0 & 2 & 1 \\ 0 & 1 & 1 & 0 \\ 1 & 1 & 3 & 1 \end{pmatrix}$.

Determinar $\dim(\ker(T))$ y $\dim(\text{Im}(T))$.

> **Solución:** Ver [solutions/prob-10/](../solutions/prob-10/)

---

## 5.3 Matriz de la Transformación

### [Prob-11] Matrices asociadas en bases estándar ⭐

Encontrar la matriz (bases estándar) de:

a) $T(x, y) = (3x - y, 2x + 4y)$

b) $T(x, y, z) = (x + y, y + z)$

c) $T(x, y) = (x, x + y, y)$

> **Solución:** Ver [solutions/prob-11/](../solutions/prob-11/)

---

### [Prob-12] Matriz de reflexión respecto al eje $y$ ⭐

Sea $T: \mathbb{R}^2 \to \mathbb{R}^2$ la reflexión respecto al eje $y$. Encontrar $[T]$.

> **Solución:** Ver [solutions/prob-12/](../solutions/prob-12/)

---

### [Prob-13] Matriz de rotación de 45° ⭐⭐

Sea $T: \mathbb{R}^2 \to \mathbb{R}^2$ la rotación de $45°$ en sentido antihorario. Encontrar $[T]$.

> **Solución:** Ver [solutions/prob-13/](../solutions/prob-13/)

---

### [Prob-14] Matriz de proyección ortogonal ⭐⭐

Sea $T: \mathbb{R}^2 \to \mathbb{R}^2$ la proyección sobre la recta $y = x$. Encontrar $[T]$.

> **Solución:** Ver [solutions/prob-14/](../solutions/prob-14/)

---

### [Prob-15] Operador de traslación en polinomios ⭐⭐⭐

Sea $T: P_2 \to P_2$ definida por $T(p(x)) = p(x + 1)$. Encontrar $[T]$ respecto a la base $\{1, x, x^2\}$.

> **Solución:** Ver [solutions/prob-15/](../solutions/prob-15/)

---

### [Prob-16] Matriz de transformación en base no estándar ⭐⭐

Sea $T: \mathbb{R}^2 \to \mathbb{R}^2$, $T(x, y) = (x + y, x - y)$.

Encontrar $[T]_{\mathcal{B}}$ donde $\mathcal{B} = \{(1, 1), (1, -1)\}$.

> **Solución:** Ver [solutions/prob-16/](../solutions/prob-16/)

---

## 5.4 Composición e Inversa

### [Prob-17] Composición de transformaciones: no conmutatividad ⭐⭐

Sean $T(x, y) = (x + y, 2y)$ y $S(x, y) = (x - y, x)$.

a) Calcular $[S \circ T]$

b) Calcular $[T \circ S]$

c) ¿Son iguales?

> **Solución:** Ver [solutions/prob-17/](../solutions/prob-17/)

---

### [Prob-18] Inversa de transformación lineal ⭐⭐

Sea $T: \mathbb{R}^2 \to \mathbb{R}^2$ con $[T] = \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix}$.

a) ¿Es $T$ invertible?

b) Si sí, encontrar $[T^{-1}]$

c) Verificar que $[T][T^{-1}] = I$

> **Solución:** Ver [solutions/prob-18/](../solutions/prob-18/)

---

### [Prob-19] Propiedades de rotaciones ⭐⭐⭐

Sea $R_\theta$ la rotación de ángulo $\theta$.

a) Demostrar que $R_\alpha \circ R_\beta = R_{\alpha + \beta}$

b) Encontrar $R_\theta^{-1}$

> **Solución:** Ver [solutions/prob-19/](../solutions/prob-19/)

---

### [Prob-20] Imposibilidad de inversa por dimensiones ⭐⭐⭐

Sean $T: \mathbb{R}^3 \to \mathbb{R}^2$ y $S: \mathbb{R}^2 \to \mathbb{R}^3$ lineales. ¿Puede $S \circ T$ ser la identidad de $\mathbb{R}^3$? Justificar.

> **Solución:** Ver [solutions/prob-20/](../solutions/prob-20/)

---

## 5.5 Cambio de Base y Matrices Similares

### [Prob-21] Cambio de base para matriz de transformación ⭐⭐

Sea $[T]_{\mathcal{E}} = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$ (base estándar).

Encontrar $[T]_{\mathcal{B}}$ donde $\mathcal{B} = \{(1, 1), (1, 0)\}$.

> **Solución:** Ver [solutions/prob-21/](../solutions/prob-21/)

---

### [Prob-22] Matrices no similares: invariantes ⭐⭐⭐

Demostrar que las matrices $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ y $B = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ NO son similares.

> **Solución:** Ver [solutions/prob-22/](../solutions/prob-22/)

---

### [Prob-23] Determinación de similitud mediante valores propios ⭐⭐⭐

Determinar si $A = \begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix}$ y $B = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$ son similares.

> **Solución:** Ver [solutions/prob-23/](../solutions/prob-23/)

---

### [Prob-24] Diagonalización mediante cambio de base ⭐⭐⭐

Sea $[T]_{\mathcal{E}} = \begin{pmatrix} 5 & -3 \\ 6 & -4 \end{pmatrix}$.

Encontrar una base $\mathcal{B}$ tal que $[T]_{\mathcal{B}}$ sea diagonal.

> **Solución:** Ver [solutions/prob-24/](../solutions/prob-24/)

---

## 5.6 Problemas de Aplicación

### [Prob-25] Transformaciones geométricas en gráficos por computadora ⭐⭐

En gráficos por computadora, una imagen se transforma mediante:

a) Escalar por factor 2 en $x$ y 3 en $y$

b) Rotar $30°$

c) Reflejar respecto al eje $x$

Encontrar la matriz de transformación compuesta.

> **Solución:** Ver [solutions/prob-25/](../solutions/prob-25/)

---

### [Prob-26] Conversión de coordenadas en robótica ⭐⭐

Un sistema de coordenadas de un robot usa la base $\mathcal{B} = \{(1, 1), (-1, 1)\}$.

Si la posición en coordenadas del robot es $[p]_{\mathcal{B}} = (3, 2)^T$, ¿cuál es la posición en coordenadas estándar?

> **Solución:** Ver [solutions/prob-26/](../solutions/prob-26/)

---

### [Prob-27] Modelo de migración poblacional ⭐⭐

La población de dos ciudades $A$ y $B$ evoluciona según:
- Cada año, 10% de $A$ migra a $B$
- Cada año, 5% de $B$ migra a $A$

Modelar como transformación lineal y encontrar su matriz.

> **Solución:** Ver [solutions/prob-27/](../solutions/prob-27/)

---

### [Prob-28] Transformación de color: filtro escala de grises ⭐⭐

Un filtro de imagen aplica a cada píxel $(r, g, b)$ la transformación:

$$T(r, g, b) = (0.3r + 0.6g + 0.1b, 0.3r + 0.6g + 0.1b, 0.3r + 0.6g + 0.1b)$$

a) Verificar que es lineal

b) ¿Qué hace este filtro? (escala de grises)

c) Encontrar $\ker(T)$

> **Solución:** Ver [solutions/prob-28/](../solutions/prob-28/)
