<!--
::METADATA::
type: cheatsheet
topic_id: cv-05-integracion-multiple
file_id: CV-05-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->

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

| [Orden](../../glossary.md#orden) | Integral |
|-------|----------|
| $dz\,dy\,dx$ | $\int_a^b \int_{g_1(x)}^{g_2(x)} \int_{u_1(x,y)}^{u_2(x,y)} f\, dz\, dy\, dx$ |

## Coordenadas cilíndricas

| Conversión | Jacobiano |
|------------|-----------|
| $x = r\cos\theta$ | |
| $y = r\sin\theta$ | $dV = r\, dr\, d\theta\, dz$ |
| $z = z$ | |

$$\iiint_E f\, dV = \int \int \int f(r\cos\theta, r\sin\theta, z)\, r\, dr\, d\theta\, dz$$

## Coordenadas esféricas

| Conversión | Relaciones |
|------------|------------|
| $x = \rho\sin\phi\cos\theta$ | $\rho = \sqrt{x^2+y^2+z^2}$ |
| $y = \rho\sin\phi\sin\theta$ | $\phi$: ángulo desde eje $z$ positivo |
| $z = \rho\cos\phi$ | $\theta$: ángulo en plano $xy$ |

$$dV = \rho^2 \sin\phi\, d\rho\, d\phi\, d\theta$$

## Cambio de variables general

Para $x = x(u,v)$, $y = y(u,v)$:

$$\iint_R f(x,y)\, dx\, dy = \iint_S f(x(u,v), y(u,v)) \left| \frac{\partial(x,y)}{\partial(u,v)} \right| du\, dv$$

### Jacobiano

$$\frac{\partial(x,y)}{\partial(u,v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix}$$

## Aplicaciones

| Cantidad | Fórmula |
|----------|---------|
| **Área** | $A = \iint_R dA$ |
| **Volumen** | $V = \iint_R f(x,y)\, dA$ o $V = \iiint_E dV$ |
| **Masa** | $m = \iint_R \rho(x,y)\, dA$ o $\iiint_E \rho\, dV$ |

## Centro de masa

| Coordenada | Fórmula (2D) |
|------------|--------------|
| $\bar{x}$ | $\frac{1}{m} \iint_R x\rho(x,y)\, dA$ |
| $\bar{y}$ | $\frac{1}{m} \iint_R y\rho(x,y)\, dA$ |

## Momentos de inercia

| Eje | Fórmula |
|-----|---------|
| $I_x$ | $\iint_R y^2 \rho(x,y)\, dA$ |
| $I_y$ | $\iint_R x^2 \rho(x,y)\, dA$ |
| $I_0$ | $\iint_R (x^2 + y^2) \rho(x,y)\, dA$ |

## Valor promedio

$$f_{\text{prom}} = \frac{1}{\text{Área}(R)} \iint_R f(x,y)\, dA$$

## Jacobianos comunes

| Sistema | Jacobiano |
|---------|-----------|
| Polar | $r$ |
| Cilíndrico | $r$ |
| Esférico | $\rho^2 \sin\phi$ |

---

<!--
IA: Usa este resumen para respuestas breves.
Para desarrollo completo, consulta theory/CV-05-Teoria-Integracion.md
file_id: CV-05-Resumen-Formulas
-->
