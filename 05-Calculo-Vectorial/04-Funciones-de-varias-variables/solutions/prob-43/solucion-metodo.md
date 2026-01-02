<!--
::METADATA::
type: solution
topic_id: cv-04-puntos-criticos
file_id: prob-43-solucion
problem_ref: Prob-43
status: stable
audience: student
-->

# Solución: Clasificación de Puntos Críticos

## Problema

Encontrar y clasificar todos los puntos críticos de la [función](../../../../glossary.md#funcion):

$$f(x,y) = x^3 + y^3 - 3xy$$

---

## Conceptos clave

**Gradiente:**
$$\nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)$$

**Puntos críticos:** Soluciones de $\nabla f = \mathbf{0}$

**[Matriz](../../../../glossary.md#matriz) Hessiana:**
$$H = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{pmatrix}$$

**Discriminante:**
$$D = f_{xx} \cdot f_{yy} - (f_{xy})^2 = \det(H)$$

**Criterio de clasificación:**
- $D > 0$ y $f_{xx} > 0$: Mínimo local
- $D > 0$ y $f_{xx} < 0$: Máximo local
- $D < 0$: Punto silla
- $D = 0$: Criterio no concluyente

---

## Solución

### Paso 1: Calcular las derivadas parciales de primer orden

$$\frac{\partial f}{\partial x} = 3x^2 - 3y$$

$$\frac{\partial f}{\partial y} = 3y^2 - 3x$$

---

### Paso 2: Encontrar los puntos críticos

Igualamos el gradiente a cero:

$$\begin{cases}
3x^2 - 3y = 0 \\
3y^2 - 3x = 0
\end{cases}$$

Simplificamos dividiendo entre 3:

$$\begin{cases}
x^2 = y \quad \text{...(1)} \\
y^2 = x \quad \text{...(2)}
\end{cases}$$

Sustituimos (1) en (2):

$$(x^2)^2 = x$$

$$x^4 = x$$

$$x^4 - x = 0$$

$$x(x^3 - 1) = 0$$

**Caso A:** $x = 0$
- De (1): $y = 0^2 = 0$
- [Punto crítico](../../../../glossary.md#punto-critico): $(0, 0)$

**Caso B:** $x^3 = 1 \Rightarrow x = 1$
- De (1): $y = 1^2 = 1$
- [Punto crítico](../../../../glossary.md#punto-critico): $(1, 1)$

**Puntos críticos encontrados:** $(0, 0)$ y $(1, 1)$

---

### Paso 3: Calcular las derivadas parciales de segundo orden

$$f_{xx} = \frac{\partial^2 f}{\partial x^2} = 6x$$

$$f_{yy} = \frac{\partial^2 f}{\partial y^2} = 6y$$

$$f_{xy} = \frac{\partial^2 f}{\partial x \partial y} = -3$$

---

### Paso 4: Construir la matriz Hessiana

$$H = \begin{pmatrix} 6x & -3 \\ -3 & 6y \end{pmatrix}$$

El discriminante es:

$$D = f_{xx} \cdot f_{yy} - (f_{xy})^2 = (6x)(6y) - (-3)^2 = 36xy - 9$$

---

### Paso 5: Clasificar el punto $(0, 0)$

Evaluamos en $(0, 0)$:

$$f_{xx}(0,0) = 6(0) = 0$$

$$f_{yy}(0,0) = 6(0) = 0$$

$$D(0,0) = 36(0)(0) - 9 = -9$$

Como $D = -9 < 0$:

$$\boxed{(0, 0) \text{ es un punto silla}}$$

**[Matriz](../../../../glossary.md#matriz) Hessiana en $(0,0)$:**
$$H(0,0) = \begin{pmatrix} 0 & -3 \\ -3 & 0 \end{pmatrix}$$

---

### Paso 6: Clasificar el punto $(1, 1)$

Evaluamos en $(1, 1)$:

$$f_{xx}(1,1) = 6(1) = 6$$

$$f_{yy}(1,1) = 6(1) = 6$$

$$D(1,1) = 36(1)(1) - 9 = 36 - 9 = 27$$

Como $D = 27 > 0$ y $f_{xx} = 6 > 0$:

$$\boxed{(1, 1) \text{ es un mínimo local}}$$

**Matriz Hessiana en $(1,1)$:**
$$H(1,1) = \begin{pmatrix} 6 & -3 \\ -3 & 6 \end{pmatrix}$$

---

### Paso 7: Calcular el valor de la función en los puntos críticos

En $(0, 0)$:
$$f(0,0) = 0^3 + 0^3 - 3(0)(0) = 0$$

En $(1, 1)$:
$$f(1,1) = 1^3 + 1^3 - 3(1)(1) = 1 + 1 - 3 = -1$$

---

## Respuesta Final

$$\boxed{\begin{array}{|c|c|c|c|c|}
\hline
\textbf{Punto} & \textbf{D} & \textbf{f}_{xx} & \textbf{Clasificación} & \textbf{f(x,y)} \\
\hline
(0, 0) & -9 & 0 & \text{Punto silla} & 0 \\
\hline
(1, 1) & 27 & 6 & \text{Mínimo local} & -1 \\
\hline
\end{array}}$$

---

## Verificación

**Verificación del punto silla $(0,0)$:**
- Por $y = x$: $f(x,x) = x^3 + x^3 - 3x^2 = 2x^3 - 3x^2 = x^2(2x-3)$
  - Para $x$ pequeño positivo: $f < 0$
  - Para $x$ pequeño negativo: $f < 0$
- Por $y = 0$: $f(x,0) = x^3$
  - Para $x > 0$: $f > 0$
  - Para $x < 0$: $f < 0$

La [función](../../../../glossary.md#funcion) toma valores tanto positivos como negativos cerca del origen, confirmando el punto silla.

**Verificación del mínimo $(1,1)$:**

Los eigenvalores de $H(1,1)$ son:
$$\det\begin{pmatrix} 6-\lambda & -3 \\ -3 & 6-\lambda \end{pmatrix} = (6-\lambda)^2 - 9 = 0$$
$$\lambda = 6 \pm 3 \Rightarrow \lambda_1 = 9, \lambda_2 = 3$$

Ambos eigenvalores son positivos, confirmando que $H$ es definida positiva y $(1,1)$ es un mínimo local.
