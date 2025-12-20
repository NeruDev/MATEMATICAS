<!--
::METADATA::
type: cheatsheet
topic_id: cv-01-vectores-espacio
file_id: CV-01-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->

# Resumen rápido — Vectores en el espacio

## Operaciones básicas

| Operación | Fórmula |
|-----------|---------|
| **Magnitud** | $\lVert\mathbf{v}\rVert = \sqrt{v_x^2+v_y^2+v_z^2}$ |
| **Vector unitario** | $\hat{\mathbf{v}} = \frac{\mathbf{v}}{\lVert\mathbf{v}\rVert}$ |
| **Suma** | $\mathbf{u}+\mathbf{v} = \langle u_x+v_x, u_y+v_y, u_z+v_z \rangle$ |

## Productos

| Producto | Fórmula | Resultado |
|----------|---------|-----------|
| **Escalar** | $\mathbf{u}\cdot\mathbf{v}=u_xv_x+u_yv_y+u_zv_z$ | Escalar |
| **Escalar (geom.)** | $\mathbf{u}\cdot\mathbf{v}=\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert\cos\theta$ | Ángulo |
| **Vectorial** | $\mathbf{u}\times\mathbf{v}$ (determinante) | Vector ⊥ |
| **Triple escalar** | $\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w})$ | Volumen |

## Proyecciones

- **Componente escalar:** $\text{comp}_{\mathbf{v}}\mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{v} \rVert}$
- **Proyección vectorial:** $\text{proy}_{\mathbf{v}}\mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{v} \rVert^2}\mathbf{v}$

## Rectas en $\mathbb{R}^3$

| Forma | Ecuación |
|-------|----------|
| Vectorial | $\mathbf{r}(t)=\mathbf{r}_0+t\mathbf{v}$ |
| Paramétrica | $x=x_0+at,\; y=y_0+bt,\; z=z_0+ct$ |
| Simétrica | $\frac{x-x_0}{a}=\frac{y-y_0}{b}=\frac{z-z_0}{c}$ |

## Planos

| Concepto | Fórmula |
|----------|---------|
| **Forma normal** | $\mathbf{n}\cdot(\mathbf{r}-\mathbf{r}_0)=0$ |
| **Forma general** | $ax+by+cz=d$ donde $\mathbf{n}=(a,b,c)$ |
| **Distancia punto-plano** | $D = \frac{\lvert ax_1+by_1+cz_1-d\rvert}{\sqrt{a^2+b^2+c^2}}$ |

## Ángulos

- **Entre vectores:** $\cos\theta = \frac{\mathbf{u}\cdot\mathbf{v}}{\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert}$
- **Entre planos:** $\cos\theta = \frac{|\mathbf{n}_1\cdot\mathbf{n}_2|}{\lVert\mathbf{n}_1\rVert\lVert\mathbf{n}_2\rVert}$
- **Recta-plano:** $\sin\alpha = \frac{|\mathbf{v}\cdot\mathbf{n}|}{\lVert\mathbf{v}\rVert\lVert\mathbf{n}\rVert}$

## Criterios rápidos

| Condición | Significado |
|-----------|-------------|
| $\mathbf{u}\cdot\mathbf{v}=0$ | Vectores ortogonales |
| $\mathbf{u}\times\mathbf{v}=\mathbf{0}$ | Vectores paralelos |
| $\lVert\mathbf{u}\times\mathbf{v}\rVert$ | Área del paralelogramo |
| $|\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w})|$ | Volumen del paralelepípedo |

---

<!--
IA: Usa este resumen para respuestas breves.
Para desarrollo completo, consulta theory/CV-01-Teoria-Vectores.md
file_id: CV-01-Resumen-Formulas
-->
