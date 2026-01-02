<!--
::METADATA::
type: cheatsheet
topic_id: cv-05-integracion-multiple
file_id: CV-05-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Resumen rápido — Integración múltiple

## Integrales dobles

| Tipo de región | Integral iterada |
|----------------|------------------|
| **Tipo I** (límites en $y$) | $\int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y)\, dy\, dx$ |
| **Tipo II** (límites en $x$) | $\int_c^d \int_{h_1(y)}^{h_2(y)} f(x,y)\, dx\, dy$ |

## Propiedades

- $\iint_R [f + g]\, dA = \iint_R f\, dA + \iint_R g\, dA$
- $\iint_R cf\, dA = c \iint_R f\, dA$
- Si $R = R_1 \cup R_2$ disjuntas: $\iint_R f\, dA = \iint_{R_1} f\, dA + \iint_{R_2} f\, dA$

## Coordenadas polares

| Conversión | Fórmula |
|------------|---------|
| $x = r\cos\theta$ | $y = r\sin\theta$ |
| $dA = r\, dr\, d\theta$ | Jacobiano: $r$ |

$$\iint_R f(x,y)\, dA = \int_\alpha^\beta \int_{r_1(\theta)}^{r_2(\theta)} f(r\cos\theta, r\sin\theta)\, r\, dr\, d\theta$$

## Integrales triples

| [Orden](theory/CV-05-Teoria-Integracion.md)
file_id: CV-05-Resumen-Formulas
-->
