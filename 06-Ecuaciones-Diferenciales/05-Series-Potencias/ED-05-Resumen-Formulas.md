<!--
::METADATA::
type: cheatsheet
topic_id: ed-05-series-potencias
file_id: ED-05-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Resumen rápido — Series de Potencias en EDO

## Serie de Potencias

$$y = \sum_{n=0}^{\infty} a_n (x - x_0)^n$$

**Radio de convergencia:** $R = \frac{1}{\limsup_{n\to\infty} |a_n|^{1/n}}$ o por cociente.

---

## Clasificación de Puntos Singulares

Para $y'' + P(x)y' + Q(x)y = 0$:

| Tipo | Condición en $x_0$ |
|------|-------------------|
| Ordinario | $P(x)$ y $Q(x)$ analíticas |
| Singular regular | $(x-x_0)P(x)$ y $(x-x_0)^2Q(x)$ analíticas |
| Singular irregular | No cumple lo anterior |

---

## Solución en Punto Ordinario

1. Proponer $y = \sum_{n=0}^{\infty} a_n x^n$
2. Calcular $y' = \sum_{n=1}^{\infty} n a_n x^{n-1}$
3. Calcular $y'' = \sum_{n=2}^{\infty} n(n-1) a_n x^{n-2}$
4. Sustituir en la [EDO](../../glossary.md#menor) potencia da:

$$r(r-1) + p_0 r + q_0 = 0$$

donde $p_0 = \lim_{x\to 0} xP(x)$ y $q_0 = \lim_{x\to 0} x^2Q(x)$

---

## Casos según Raíces de Ecuación Indicial

Sean $r_1 \geq r_2$ las raíces.

### Caso 1: $r_1 - r_2 \notin \mathbb{Z}$

Dos soluciones independientes de Frobenius:
$$y_1 = x^{r_1}\sum a_n x^n, \quad y_2 = x^{r_2}\sum b_n x^n$$

### Caso 2: $r_1 = r_2 = r$

$$y_1 = x^r \sum a_n x^n$$
$$y_2 = y_1 \ln x + x^r \sum b_n x^n$$

### Caso 3: $r_1 - r_2 = N$ (entero positivo)

$$y_1 = x^{r_1}\sum a_n x^n$$
$$y_2 = Cy_1 \ln x + x^{r_2}\sum b_n x^n$$

donde $C$ puede ser $0$.

---

## Ecuación de Bessel

$$x^2 y'' + xy' + (x^2 - \nu^2)y = 0$$

### Soluciones

| [Orden](../../glossary.md#edo).
Para desarrollo completo: [theory/ED-05-Teoria-Series-Potencias.md](theory/ED-05-Teoria-Series-Potencias.md)
file_id: ED-05-Resumen-Formulas
-->
