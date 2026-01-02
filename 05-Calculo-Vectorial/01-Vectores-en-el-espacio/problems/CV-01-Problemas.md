<!--
::METADATA::
type: problem-set
topic_id: cv-01-vectores-espacio
file_id: CV-01-Problemas
status: stable
audience: student
total_problems: 50
difficulty_distribution:
  basic: 20
  intermediate: 20
  advanced: 10
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Problemas — Vectores en el Espacio

> **Instrucciones:** Resuelve cada problema mostrando el procedimiento completo.
>
> **Respuestas:** Consulta [solutions/CV-01-Respuestas.md](../solutions/CV-01-Respuestas.md)

---

## 1.1 Operaciones Básicas con Vectores

**[Prob-01]** Dados $\mathbf{u} = \langle 3, -2, 5 \rangle$ y $\mathbf{v} = \langle -1, 4, 2 \rangle$, calcula:
a) $\mathbf{u} + \mathbf{v}$
b) $\mathbf{u} - \mathbf{v}$
c) $2\mathbf{u} - 3\mathbf{v}$

**[Prob-02]** Calcula la magnitud de $\mathbf{v} = \langle 2, -3, 6 \rangle$.

**[Prob-03]** Encuentra el [vector](../../../glossary.md#vector) unitario en la dirección de $\mathbf{w} = \langle 4, -4, 2 \rangle$.

**[Prob-04]** Si $\mathbf{a} = \langle 1, 2, -1 \rangle$ y $\mathbf{b} = \langle 3, -1, 2 \rangle$, encuentra un [vector](../../../glossary.md#vector) de magnitud 5 en la dirección de $\mathbf{a} + \mathbf{b}$.

**[Prob-05]** Encuentra los valores de $c$ tales que $\lVert \langle c, 2, 1 \rangle \rVert = 3$.

**[Prob-06]** Dados los puntos $A(1, 2, 3)$ y $B(4, -1, 5)$:
a) Encuentra el vector $\overrightarrow{AB}$
b) Calcula la distancia entre $A$ y $B$

**[Prob-07]** Encuentra el punto medio del segmento que une $P(2, -3, 5)$ y $Q(6, 1, -1)$.

**[Prob-08]** Un vector tiene punto inicial $(-2, 3, 1)$ y punto final $(4, -1, 6)$. Escríbelo en forma estándar.

---

## 1.2 Producto Escalar (Punto)

**[Prob-09]** Calcula $\mathbf{u} \cdot \mathbf{v}$ donde $\mathbf{u} = \langle 2, -1, 3 \rangle$ y $\mathbf{v} = \langle 4, 5, -2 \rangle$.

**[Prob-10]** Encuentra el ángulo entre $\mathbf{a} = \langle 1, 2, 2 \rangle$ y $\mathbf{b} = \langle 2, -1, 2 \rangle$.

**[Prob-11]** Determina si $\mathbf{u} = \langle 3, -6, 2 \rangle$ y $\mathbf{v} = \langle 2, 1, 0 \rangle$ son ortogonales.

**[Prob-12]** Encuentra el valor de $k$ para que $\langle 2, k, -3 \rangle$ y $\langle 1, 2, 4 \rangle$ sean perpendiculares.

**[Prob-13]** Calcula la componente escalar de $\mathbf{u} = \langle 6, 3, 2 \rangle$ sobre $\mathbf{v} = \langle 2, -2, 1 \rangle$.

**[Prob-14]** Encuentra la proyección vectorial de $\mathbf{u} = \langle 3, 4, 0 \rangle$ sobre $\mathbf{v} = \langle 1, 1, 1 \rangle$.

**[Prob-15]** Si $\lVert\mathbf{u}\rVert = 5$, $\lVert\mathbf{v}\rVert = 3$ y el ángulo entre ellos es $60°$, calcula $\mathbf{u} \cdot \mathbf{v}$.

**[Prob-16]** Descompón $\mathbf{F} = \langle 5, 8, -1 \rangle$ en componentes paralela y perpendicular a $\mathbf{d} = \langle 1, 2, 2 \rangle$.\n\n📂 **Solución desarrollada:** [Ver paso a paso](../solutions/prob-16/solucion-metodo.md)

---

## 1.3 Producto Vectorial (Cruz)

**[Prob-17]** Calcula $\mathbf{u} \times \mathbf{v}$ donde $\mathbf{u} = \langle 2, 1, -1 \rangle$ y $\mathbf{v} = \langle 1, 3, 2 \rangle$.

**[Prob-18]** Verifica que $\mathbf{u} \times \mathbf{v}$ es ortogonal tanto a $\mathbf{u}$ como a $\mathbf{v}$ del problema anterior.

**[Prob-19]** Encuentra un vector perpendicular al plano que contiene los puntos $A(1, 0, 0)$, $B(0, 2, 0)$ y $C(0, 0, 3)$.

**[Prob-20]** Calcula el área del paralelogramo determinado por $\mathbf{u} = \langle 3, 2, 1 \rangle$ y $\mathbf{v} = \langle 1, -1, 2 \rangle$.

**[Prob-21]** Encuentra el área del triángulo con vértices $P(1, 1, 1)$, $Q(2, 3, 1)$ y $R(4, 1, 2)$.

**[Prob-22]** Si $\mathbf{a} \times \mathbf{b} = \langle 2, -3, 1 \rangle$, encuentra $\mathbf{b} \times \mathbf{a}$.

**[Prob-23]** Demuestra que $\lVert\mathbf{u} \times \mathbf{v}\rVert = \lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert\sin\theta$ para $\mathbf{u} = \langle 1, 0, 0 \rangle$ y $\mathbf{v} = \langle 1, 1, 0 \rangle$.

**[Prob-24]** Simplifica $(\mathbf{u} + \mathbf{v}) \times (\mathbf{u} - \mathbf{v})$.

---

## 1.4 Triple Producto Escalar

**[Prob-25]** Calcula $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})$ donde:
$\mathbf{u} = \langle 1, 2, 3 \rangle$, $\mathbf{v} = \langle 2, -1, 1 \rangle$, $\mathbf{w} = \langle 3, 1, -2 \rangle$\n\n📂 **Solución desarrollada:** [Ver paso a paso](../solutions/prob-25/solucion-metodo.md)

**[Prob-26]** Encuentra el volumen del paralelepípedo determinado por:
$\mathbf{a} = \langle 1, 0, 2 \rangle$, $\mathbf{b} = \langle 0, 3, 1 \rangle$, $\mathbf{c} = \langle 2, 1, 0 \rangle$

**[Prob-27]** Determina si los vectores $\mathbf{u} = \langle 1, 2, -1 \rangle$, $\mathbf{v} = \langle 2, 1, 1 \rangle$ y $\mathbf{w} = \langle 1, -1, 2 \rangle$ son coplanares.

**[Prob-28]** Encuentra el volumen del tetraedro con vértices $A(0, 0, 0)$, $B(1, 0, 0)$, $C(0, 2, 0)$ y $D(0, 0, 3)$.

---

## 1.5 Ecuaciones de Rectas

**[Prob-29]** Escribe las ecuaciones paramétricas y simétricas de la recta que pasa por $P(2, -1, 3)$ con vector director $\mathbf{v} = \langle 1, 4, -2 \rangle$.

**[Prob-30]** Encuentra las ecuaciones de la recta que pasa por los puntos $A(1, 2, -1)$ y $B(3, -1, 4)$.

**[Prob-31]** Determina si las rectas son paralelas, coincidentes o se cruzan:
$$L_1: \frac{x-1}{2} = \frac{y+2}{3} = \frac{z}{1}$$
$$L_2: \frac{x-3}{4} = \frac{y-1}{6} = \frac{z-2}{2}$$

**[Prob-32]** Encuentra el punto de intersección de las rectas:
$$L_1: x = 1 + t,\ y = 2 - t,\ z = 3 + 2t$$
$$L_2: x = 2 + s,\ y = -1 + 3s,\ z = 1 - s$$

**[Prob-33]** Calcula la distancia del punto $P(1, 1, 1)$ a la recta que pasa por $A(2, 0, -1)$ con dirección $\mathbf{v} = \langle 1, 2, 2 \rangle$.

**[Prob-34]** Encuentra las ecuaciones de la recta que pasa por $(1, 2, 3)$ y es paralela a la recta de intersección de los planos $x + y + z = 6$ y $2x - y + z = 3$.

---

## 1.6 Ecuaciones de Planos

**[Prob-35]** Encuentra la ecuación del plano que pasa por $P(2, 1, -1)$ con vector normal $\mathbf{n} = \langle 3, -2, 5 \rangle$.

**[Prob-36]** Escribe la ecuación del plano que contiene los puntos $A(1, 0, 0)$, $B(0, 2, 0)$ y $C(0, 0, 3)$.

**[Prob-37]** Encuentra la ecuación del plano que contiene la recta $\frac{x-1}{2} = \frac{y}{3} = \frac{z+1}{1}$ y el punto $P(0, 1, 2)$.

**[Prob-38]** Determina si los planos son paralelos, perpendiculares o ninguno:
a) $2x - y + 3z = 4$ y $4x - 2y + 6z = 1$
b) $x + y - z = 1$ y $2x - 3y + z = 2$

**[Prob-39]** Encuentra el ángulo entre los planos $x + 2y - z = 5$ y $2x - y + 2z = 3$.

**[Prob-40]** Calcula la distancia del punto $P(3, 1, -2)$ al plano $2x - 2y + z = 6$.

**[Prob-41]** Encuentra la ecuación del plano que pasa por $(1, 2, 3)$ y es paralelo al plano $3x - y + 2z = 7$.

**[Prob-42]** Halla la ecuación del plano que pasa por $(2, 0, 1)$ y es perpendicular a la recta $x = 1 + 2t$, $y = -t$, $z = 3 + t$.

---

## 1.7 Problemas de Síntesis

**[Prob-43]** Encuentra la distancia entre las rectas paralelas:
$$L_1: \frac{x}{1} = \frac{y-1}{2} = \frac{z}{1}$$
$$L_2: \frac{x-2}{1} = \frac{y}{2} = \frac{z-1}{1}$$

**[Prob-44]** Calcula la distancia entre las rectas que se cruzan:
$$L_1: x = 1 + t,\ y = 2t,\ z = -1 + t$$
$$L_2: x = 2 + s,\ y = 1 + s,\ z = s$$\n\n📂 **Solución desarrollada:** [Ver paso a paso](../solutions/prob-44/solucion-metodo.md)

**[Prob-45]** Encuentra la ecuación del plano que contiene la recta $\frac{x-1}{2} = \frac{y+1}{1} = \frac{z}{3}$ y es perpendicular al plano $x - y + z = 5$.

**[Prob-46]** Encuentra la recta de intersección de los planos $x + y - z = 2$ y $2x - y + z = 1$.

**[Prob-47]** Un avión viaja en la dirección del vector $\mathbf{v} = \langle 200, 300, 50 \rangle$ km/h. El viento sopla con velocidad $\mathbf{w} = \langle -30, 20, 0 \rangle$ km/h. Encuentra la velocidad resultante y su magnitud.

**[Prob-48]** Una fuerza $\mathbf{F} = \langle 20, 15, -10 \rangle$ N actúa sobre una partícula que se desplaza de $A(1, 0, 2)$ a $B(4, 3, 5)$ (en metros). Calcula el trabajo realizado.

**[Prob-49]** Encuentra el torque $\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$ cuando la fuerza $\mathbf{F} = \langle 3, -2, 5 \rangle$ N actúa en el punto $P(2, 1, -1)$ m respecto al origen.

**[Prob-50]** Demuestra que los puntos $A(1, 2, 3)$, $B(4, 6, 9)$, $C(0, 0, 1)$ y $D(3, 4, 7)$ son coplanares y encuentra la ecuación del plano que los contiene.

---

> 📚 **Respuestas:** [solutions/CV-01-Respuestas.md](../theory/)
> 📋 **Fórmulas:** [CV-01-Resumen-Formulas.md](../CV-01-Resumen-Formulas.md)
