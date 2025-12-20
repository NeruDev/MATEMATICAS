<!--
content_type: problems
topic: Transformaciones Lineales
difficulty: graduated
---
-->

# Problemas: Transformaciones Lineales

---

## 5.1 Definición y Verificación

### Problema 1
Determinar si las siguientes funciones son transformaciones lineales:
a) $T: \mathbb{R}^2 \to \mathbb{R}^2$, $T(x, y) = (2x + y, x - 3y)$
b) $T: \mathbb{R}^2 \to \mathbb{R}^2$, $T(x, y) = (x^2, y)$
c) $T: \mathbb{R}^2 \to \mathbb{R}$, $T(x, y) = xy$
d) $T: \mathbb{R}^2 \to \mathbb{R}^2$, $T(x, y) = (x + 1, y)$

### Problema 2
Sea $T: P_2 \to P_1$ definida por $T(p(x)) = p'(x)$ (derivada). Verificar que $T$ es lineal.

### Problema 3
Sea $T: M_{2 \times 2} \to \mathbb{R}$ definida por $T(A) = \text{tr}(A)$ (traza). ¿Es $T$ lineal?

### Problema 4
Sea $T: C[0,1] \to \mathbb{R}$ definida por $T(f) = f(0) + f(1)$. ¿Es $T$ lineal?

### Problema 5
Sea $T: \mathbb{R}^3 \to \mathbb{R}^3$ definida por $T(x, y, z) = (|x|, y, z)$. ¿Es $T$ lineal?

---

## 5.2 Núcleo e Imagen

### Problema 6
Para $T: \mathbb{R}^3 \to \mathbb{R}^2$, $T(x, y, z) = (x - y, y - z)$:
a) Encontrar $\ker(T)$ y su base
b) Encontrar $\text{Im}(T)$ y su base
c) Verificar el teorema del rango-nulidad

### Problema 7
Para $T: \mathbb{R}^2 \to \mathbb{R}^3$, $T(x, y) = (x + y, x - y, 2x)$:
a) Hallar $\ker(T)$
b) Hallar $\text{Im}(T)$
c) ¿Es $T$ inyectiva? ¿Sobreyectiva?

### Problema 8
Sea $T: P_3 \to P_2$ definida por $T(p(x)) = p'(x)$. Encontrar:
a) $\ker(T)$
b) $\text{Im}(T)$
c) Verificar rango-nulidad

### Problema 9
Para la matriz $A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 3 \end{pmatrix}$, hallar base de:
a) $\text{Nul}(A)$
b) $\text{Col}(A)$

### Problema 10
Sea $T: \mathbb{R}^4 \to \mathbb{R}^3$ con matriz $[T] = \begin{pmatrix} 1 & 0 & 2 & 1 \\ 0 & 1 & 1 & 0 \\ 1 & 1 & 3 & 1 \end{pmatrix}$. 
Determinar $\dim(\ker(T))$ y $\dim(\text{Im}(T))$.

---

## 5.3 Matriz de la Transformación

### Problema 11
Encontrar la matriz (bases estándar) de:
a) $T(x, y) = (3x - y, 2x + 4y)$
b) $T(x, y, z) = (x + y, y + z)$
c) $T(x, y) = (x, x + y, y)$

### Problema 12
Sea $T: \mathbb{R}^2 \to \mathbb{R}^2$ la reflexión respecto al eje $y$. Encontrar $[T]$.

### Problema 13
Sea $T: \mathbb{R}^2 \to \mathbb{R}^2$ la rotación de $45°$ en sentido antihorario. Encontrar $[T]$.

### Problema 14
Sea $T: \mathbb{R}^2 \to \mathbb{R}^2$ la proyección sobre la recta $y = x$. Encontrar $[T]$.

### Problema 15
Sea $T: P_2 \to P_2$ definida por $T(p(x)) = p(x + 1)$. Encontrar $[T]$ respecto a la base $\{1, x, x^2\}$.

### Problema 16
Sea $T: \mathbb{R}^2 \to \mathbb{R}^2$, $T(x, y) = (x + y, x - y)$.
Encontrar $[T]_{\mathcal{B}}$ donde $\mathcal{B} = \{(1, 1), (1, -1)\}$.

---

## 5.4 Composición e Inversa

### Problema 17
Sean $T(x, y) = (x + y, 2y)$ y $S(x, y) = (x - y, x)$.
a) Calcular $[S \circ T]$
b) Calcular $[T \circ S]$
c) ¿Son iguales?

### Problema 18
Sea $T: \mathbb{R}^2 \to \mathbb{R}^2$ con $[T] = \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix}$.
a) ¿Es $T$ invertible?
b) Si sí, encontrar $[T^{-1}]$
c) Verificar que $[T][T^{-1}] = I$

### Problema 19
Sea $R_\theta$ la rotación de ángulo $\theta$.
a) Demostrar que $R_\alpha \circ R_\beta = R_{\alpha + \beta}$
b) Encontrar $R_\theta^{-1}$

### Problema 20
Sean $T: \mathbb{R}^3 \to \mathbb{R}^2$ y $S: \mathbb{R}^2 \to \mathbb{R}^3$ lineales. ¿Puede $S \circ T$ ser la identidad de $\mathbb{R}^3$? Justificar.

---

## 5.5 Cambio de Base y Matrices Similares

### Problema 21
Sea $[T]_{\mathcal{E}} = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$ (base estándar).
Encontrar $[T]_{\mathcal{B}}$ donde $\mathcal{B} = \{(1, 1), (1, 0)\}$.

### Problema 22
Demostrar que las matrices $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ y $B = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ NO son similares.

### Problema 23
Determinar si $A = \begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix}$ y $B = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$ son similares.

### Problema 24
Sea $[T]_{\mathcal{E}} = \begin{pmatrix} 5 & -3 \\ 6 & -4 \end{pmatrix}$.
Encontrar una base $\mathcal{B}$ tal que $[T]_{\mathcal{B}}$ sea diagonal.

---

## Problemas de Aplicación

### Problema 25
En gráficos por computadora, una imagen se transforma mediante:
a) Escalar por factor 2 en $x$ y 3 en $y$
b) Rotar $30°$
c) Reflejar respecto al eje $x$

Encontrar la matriz de transformación compuesta.

### Problema 26
Un sistema de coordenadas de un robot usa la base $\mathcal{B} = \{(1, 1), (-1, 1)\}$.
Si la posición en coordenadas del robot es $[p]_{\mathcal{B}} = (3, 2)^T$, ¿cuál es la posición en coordenadas estándar?

### Problema 27
La población de dos ciudades $A$ y $B$ evoluciona según:
- Cada año, 10% de $A$ migra a $B$
- Cada año, 5% de $B$ migra a $A$

Modelar como transformación lineal y encontrar su matriz.

### Problema 28
Un filtro de imagen aplica a cada píxel $(r, g, b)$ la transformación:
$$T(r, g, b) = (0.3r + 0.6g + 0.1b, 0.3r + 0.6g + 0.1b, 0.3r + 0.6g + 0.1b)$$
a) Verificar que es lineal
b) ¿Qué hace este filtro? (escala de grises)
c) Encontrar $\ker(T)$
