<!--
::METADATA::
type: cheatsheet
topic_id: ed-03-sistemas-[edo](../../glossary.md#edo)
file_id: ED-03-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->

# Resumen rápido — Sistemas de EDO

## Forma Matricial

### Sistema general
$$\mathbf{X}' = A\mathbf{X} + \mathbf{F}(t)$$

### Sistema homogéneo 2×2
$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}$$

---

## Solución por Valores Propios

### Ecuación característica
$$\det(A - \lambda I) = 0$$

Para 2×2: $\lambda^2 - \text{tr}(A)\lambda + \det(A) = 0$

donde $\text{tr}(A) = a + d$ y $\det(A) = ad - bc$

---

## Casos según Valores Propios

### Caso 1: Valores propios reales distintos $\lambda_1 \neq \lambda_2$

**Eigenvectores:** $\mathbf{v}_1, \mathbf{v}_2$

**[Solución general](../../glossary.md#solución-general):**
$$\mathbf{X}(t) = C_1 e^{\lambda_1 t}\mathbf{v}_1 + C_2 e^{\lambda_2 t}\mathbf{v}_2$$

---

### Caso 2: Valores propios complejos $\lambda = \alpha \pm \beta i$

**Eigenvector complejo:** $\mathbf{v} = \mathbf{a} + i\mathbf{b}$

**Solución real:**
$$\mathbf{X}(t) = C_1 e^{\alpha t}(\mathbf{a}\cos\beta t - \mathbf{b}\sin\beta t) + C_2 e^{\alpha t}(\mathbf{a}\sin\beta t + \mathbf{b}\cos\beta t)$$

---

### Caso 3: Valor propio repetido $\lambda$ (multiplicidad 2)

**Si hay 2 eigenvectores independientes:**
$$\mathbf{X}(t) = C_1 e^{\lambda t}\mathbf{v}_1 + C_2 e^{\lambda t}\mathbf{v}_2$$

**Si hay 1 eigenvector (deficiente):**
- Eigenvector: $\mathbf{v}$
- [Vector](../../glossary.md#vector) generalizado: $(A - \lambda I)\mathbf{w} = \mathbf{v}$

$$\mathbf{X}(t) = C_1 e^{\lambda t}\mathbf{v} + C_2 e^{\lambda t}(t\mathbf{v} + \mathbf{w})$$

---

## Matriz Fundamental

$$\Phi(t) = \begin{pmatrix} \mathbf{X}_1(t) & \mathbf{X}_2(t) \end{pmatrix}$$

**Solución general:** $\mathbf{X}(t) = \Phi(t)\mathbf{C}$

**Con condición inicial:** $\mathbf{X}(t) = \Phi(t)\Phi^{-1}(t_0)\mathbf{X}_0$

---

## Matriz Exponencial

$$e^{At} = I + At + \frac{(At)^2}{2!} + \frac{(At)^3}{3!} + \cdots$$

**Solución con condición inicial:**
$$\mathbf{X}(t) = e^{At}\mathbf{X}_0$$

### Cálculo de $e^{At}$ para 2×2

| Caso | Fórmula |
|------|---------|
| $\lambda_1 \neq \lambda_2$ | $e^{At} = \frac{e^{\lambda_1 t}(A - \lambda_2 I) - e^{\lambda_2 t}(A - \lambda_1 I)}{\lambda_1 - \lambda_2}$ |
| $\lambda$ repetido | $e^{At} = e^{\lambda t}[I + t(A - \lambda I)]$ |

---

## Sistema No Homogéneo

$$\mathbf{X}' = A\mathbf{X} + \mathbf{F}(t)$$

### Variación de parámetros
$$\mathbf{X}_p(t) = \Phi(t)\int \Phi^{-1}(t)\mathbf{F}(t)\,dt$$

### Solución general
$$\mathbf{X}(t) = \Phi(t)\mathbf{C} + \mathbf{X}_p(t)$$

---

## Retratos de Fase (2D)

Sea $\tau = \text{tr}(A)$, $\Delta = \det(A)$

| Condición | Tipo de equilibrio |
|-----------|-------------------|
| $\Delta < 0$ | Punto silla |
| $\Delta > 0$, $\tau^2 - 4\Delta > 0$, $\tau < 0$ | Nodo estable |
| $\Delta > 0$, $\tau^2 - 4\Delta > 0$, $\tau > 0$ | Nodo inestable |
| $\Delta > 0$, $\tau^2 - 4\Delta < 0$, $\tau < 0$ | Espiral estable |
| $\Delta > 0$, $\tau^2 - 4\Delta < 0$, $\tau > 0$ | Espiral inestable |
| $\Delta > 0$, $\tau = 0$ | Centro |
| $\Delta = 0$ | Caso degenerado |

---

## Estabilidad

| Criterio | Estabilidad |
|----------|-------------|
| Todos $\text{Re}(\lambda_i) < 0$ | Asintóticamente estable |
| Algún $\text{Re}(\lambda_i) > 0$ | Inestable |
| $\text{Re}(\lambda_i) \leq 0$ (alguno = 0) | Marginalmente estable o inestable |

---

<!--
IA: Hoja de referencia rápida para Sistemas de EDO.
Para desarrollo completo: theory/ED-03-Teoria-Sistemas-EDO.md
file_id: ED-03-Resumen-Formulas
-->
