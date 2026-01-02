<!--
::METADATA::
type: problem-set
topic_id: cv-03-funciones-vectoriales
file_id: CV-03-Problemas
status: stable
audience: student
total_problems: 50
difficulty_distribution:
  basic: 18
  intermediate: 22
  advanced: 10
-->

# Problemas — Funciones Vectoriales

> **Instrucciones:** Resuelve cada problema mostrando el procedimiento completo.
>
> **Respuestas:** Consulta [`solutions/CV-03-Respuestas.md`](../solutions/CV-03-Respuestas.md)

---

## 3.1 Dominio, Límites y Continuidad

**[Prob-01]** Encuentra el [dominio](../../../glossary.md#dominio) de $\mathbf{r}(t) = \langle \sqrt{t-1}, \ln(4-t), e^t \rangle$.

**[Prob-02]** Encuentra el dominio de $\mathbf{r}(t) = \langle \frac{1}{t}, \arcsin t, \sqrt{9-t^2} \rangle$.

**[Prob-03]** Calcula $\displaystyle\lim_{t \to 0} \left\langle \frac{\sin t}{t}, \frac{e^t - 1}{t}, \cos t \right\rangle$.

**[Prob-04]** Evalúa $\displaystyle\lim_{t \to 1} \left\langle \frac{t^2 - 1}{t - 1}, t^3, \ln t \right\rangle$.

**[Prob-05]** Determina si $\mathbf{r}(t) = \langle t^2, \sqrt{t}, \frac{1}{t} \rangle$ es continua en $t = 1$.

---

## 3.2 Derivadas de Funciones Vectoriales

**[Prob-06]** Encuentra $\mathbf{r}'(t)$ si $\mathbf{r}(t) = \langle t^3, e^{2t}, \sin 3t \rangle$.

**[Prob-07]** Calcula $\mathbf{r}'(t)$ para $\mathbf{r}(t) = \langle t\cos t, t\sin t, t^2 \rangle$.

**[Prob-08]** Si $\mathbf{r}(t) = \langle \ln t, \frac{1}{t}, \arctan t \rangle$, encuentra $\mathbf{r}'(1)$.

**[Prob-09]** Para $\mathbf{r}(t) = \langle e^t, e^{-t}, te^t \rangle$:
a) Encuentra $\mathbf{r}'(t)$
b) Encuentra $\mathbf{r}''(t)$

**[Prob-10]** Si $\mathbf{u}(t) = \langle t, t^2, t^3 \rangle$ y $\mathbf{v}(t) = \langle 1, 2t, 3t^2 \rangle$, calcula $\frac{d}{dt}[\mathbf{u}(t) \cdot \mathbf{v}(t)]$.

**[Prob-11]** Con los vectores del problema anterior, calcula $\frac{d}{dt}[\mathbf{u}(t) \times \mathbf{v}(t)]$.

**[Prob-12]** Si $f(t) = e^t$ y $\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle$, encuentra $\frac{d}{dt}[f(t)\mathbf{r}(t)]$.

---

## 3.3 Integrales de Funciones Vectoriales

**[Prob-13]** Calcula $\int \langle 3t^2, 2t, 1 \rangle\, dt$.

**[Prob-14]** Evalúa $\int_0^1 \langle e^t, t, t^2 \rangle\, dt$.

**[Prob-15]** Calcula $\int_0^{\pi/2} \langle \sin t, \cos t, 1 \rangle\, dt$.

**[Prob-16]** Si $\mathbf{r}'(t) = \langle 2t, 3t^2, e^t \rangle$ y $\mathbf{r}(0) = \langle 1, 0, 1 \rangle$, encuentra $\mathbf{r}(t)$.

**[Prob-17]** Si $\mathbf{r}''(t) = \langle 6, 0, 12t \rangle$, $\mathbf{r}'(0) = \langle 1, 1, 0 \rangle$ y $\mathbf{r}(0) = \langle 0, 0, 0 \rangle$, encuentra $\mathbf{r}(t)$.

---

## 3.4 Vectores Tangente y Recta Tangente

**[Prob-18]** Encuentra el [vector](../../../glossary.md#vector) [tangente](../../../glossary.md#tangente) unitario $\mathbf{T}(t)$ para $\mathbf{r}(t) = \langle t, t^2, t^3 \rangle$ en $t = 1$.

**[Prob-19]** Para la hélice $\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle$:
a) Encuentra $\mathbf{T}(t)$
b) Evalúa $\mathbf{T}(\pi/4)$

**[Prob-20]** Encuentra la ecuación de la recta tangente a $\mathbf{r}(t) = \langle e^t, e^{-t}, e^{2t} \rangle$ en $t = 0$.

**[Prob-21]** Halla la recta tangente a la curva $\mathbf{r}(t) = \langle t^2 + 1, 2t - 1, t^3 \rangle$ en el punto $(2, 1, 1)$.

---

## 3.5 Longitud de Arco y Parametrización

**[Prob-22]** Calcula la longitud de la curva $\mathbf{r}(t) = \langle 2t, t^2, \frac{2}{3}t^3 \rangle$ desde $t = 0$ hasta $t = 1$.

**[Prob-23]** Encuentra la longitud de $\mathbf{r}(t) = \langle 3\cos t, 3\sin t, 4t \rangle$ desde $t = 0$ hasta $t = 2\pi$.

**[Prob-24]** Calcula la longitud de la hélice $\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle$ para $t \in [0, 2\pi]$.

**[Prob-25]** Encuentra la [función](../../../glossary.md#función) longitud de arco $s(t)$ desde $t = 0$ para $\mathbf{r}(t) = \langle t^2, \frac{2\sqrt{2}}{3}t^{3/2}, \frac{t^2}{2} \rangle$.

**[Prob-26]** Reparametriza la curva $\mathbf{r}(t) = \langle 3t, 4t, 0 \rangle$ usando la longitud de arco.

---

## 3.6 Curvatura

**[Prob-27]** Calcula la curvatura de $\mathbf{r}(t) = \langle t, t^2, 0 \rangle$ en $t = 0$.

**[Prob-28]** Encuentra la curvatura de la hélice $\mathbf{r}(t) = \langle 2\cos t, 2\sin t, t \rangle$.

**[Prob-29]** Calcula la curvatura de $y = x^2$ en el punto $(0, 0)$ usando la fórmula para curvas planas.

**[Prob-30]** Encuentra la curvatura de $y = \sin x$ en $x = 0$ y en $x = \frac{\pi}{2}$.

**[Prob-31]** Calcula la curvatura de $\mathbf{r}(t) = \langle e^t\cos t, e^t\sin t, e^t \rangle$ en $t = 0$.

**[Prob-32]** Encuentra el radio de curvatura de $y = e^x$ en $x = 0$.

---

## 3.7 Marco TNB y Torsión

**[Prob-33]** Para $\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle$, encuentra $\mathbf{T}$, $\mathbf{N}$ y $\mathbf{B}$.

**[Prob-34]** Calcula el vector normal principal $\mathbf{N}(t)$ para $\mathbf{r}(t) = \langle t, t^2, 0 \rangle$ en $t = 1$.

**[Prob-35]** Encuentra la torsión de la hélice $\mathbf{r}(t) = \langle 3\cos t, 3\sin t, 4t \rangle$.

**[Prob-36]** Demuestra que la torsión de una curva plana es cero para $\mathbf{r}(t) = \langle t, t^2, 0 \rangle$.

---

## 3.8 Movimiento: Velocidad y Aceleración

**[Prob-37]** Una partícula se mueve según $\mathbf{r}(t) = \langle t^2, 2t, t^3 \rangle$. Encuentra:
a) Velocidad $\mathbf{v}(t)$
b) Aceleración $\mathbf{a}(t)$
c) Rapidez en $t = 1$

**[Prob-38]** Para el movimiento $\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle$:
a) Calcula $\mathbf{v}(t)$ y $\mathbf{a}(t)$
b) Encuentra las componentes tangencial y normal de la aceleración

**[Prob-39]** Una partícula tiene $\mathbf{a}(t) = \langle 0, 0, -10 \rangle$, $\mathbf{v}(0) = \langle 20, 30, 40 \rangle$ y $\mathbf{r}(0) = \langle 0, 0, 0 \rangle$. Encuentra $\mathbf{r}(t)$.

**[Prob-40]** Encuentra las componentes $a_T$ y $a_N$ para $\mathbf{r}(t) = \langle t, t^2, t^3 \rangle$ en $t = 1$.

**[Prob-41]** Un proyectil se lanza con velocidad inicial $\mathbf{v}_0 = \langle 50, 50\sqrt{3} \rangle$ m/s. Con $g = 10$ m/s²:
a) Encuentra la ecuación de posición
b) ¿Cuál es la altura máxima?
c) ¿Cuál es el alcance horizontal?

---

## 3.9 Planos Normal y Osculador

**[Prob-42]** Encuentra la ecuación del plano normal a $\mathbf{r}(t) = \langle t, t^2, t^3 \rangle$ en $t = 1$.

**[Prob-43]** Halla la ecuación del plano osculador a la hélice $\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle$ en $t = 0$.

**[Prob-44]** Encuentra el centro del círculo osculador a $y = x^2$ en el origen.

---

## 3.10 Problemas de Síntesis

**[Prob-45]** La posición de un electrón en un campo magnético es $\mathbf{r}(t) = \langle R\cos(\omega t), R\sin(\omega t), v_0 t \rangle$ donde $R = 0.1$ m, $\omega = 10^6$ rad/s y $v_0 = 10^5$ m/s.
a) Calcula la rapidez
b) Encuentra la curvatura
c) Determina $a_T$ y $a_N$

**[Prob-46]** Una abeja vuela siguiendo $\mathbf{r}(t) = \langle t\cos t, t\sin t, t \rangle$ para $t \geq 0$.
a) Describe la trayectoria
b) Calcula la velocidad en $t = \pi$
c) Encuentra la longitud recorrida desde $t = 0$ hasta $t = 2\pi$

**[Prob-47]** Demuestra que para cualquier curva $\mathbf{r}(t)$, si $\lVert\mathbf{r}(t)\rVert$ es constante, entonces $\mathbf{r}(t) \perp \mathbf{r}'(t)$.

**[Prob-48]** Para la curva $\mathbf{r}(t) = \langle t - \sin t, 1 - \cos t, 4\sin(t/2) \rangle$:
a) Encuentra los puntos donde $\mathbf{r}'(t) = \mathbf{0}$
b) Calcula la curvatura donde esté definida

**[Prob-49]** Una partícula viaja sobre una esfera de radio 5 con posición $\mathbf{r}(t) = \langle 5\sin t\cos(2t), 5\sin t\sin(2t), 5\cos t \rangle$.
a) Verifica que la partícula permanece en la esfera
b) Encuentra la rapidez
c) Calcula la aceleración en $t = 0$

**[Prob-50]** Demuestra las fórmulas de Frenet-Serret:
a) $\frac{d\mathbf{T}}{ds} = \kappa\mathbf{N}$
b) $\frac{d\mathbf{N}}{ds} = -\kappa\mathbf{T} + \tau\mathbf{B}$
c) $\frac{d\mathbf{B}}{ds} = -\tau\mathbf{N}$

Para la hélice $\mathbf{r}(t) = \langle a\cos t, a\sin t, bt \rangle$.

---

> 📚 **Respuestas:** [`solutions/CV-03-Respuestas.md`](../solutions/CV-03-Respuestas.md)
> 📖 **Teoría:** [`theory/`](../theory/)
> 📋 **Fórmulas:** [`CV-03-Resumen-Formulas.md`](../CV-03-Resumen-Formulas.md)
