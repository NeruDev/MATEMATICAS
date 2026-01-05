<!--
::METADATA::
type: index
topic_id: ed-02-edo-segundo-orden
file_id: ED-02-EDO-Segundo-Orden-Intro
status: stable
learning_role: introduction
difficulty: 4/5
prerequisites: ["ED-01", "AL-06"]
concepts: ["edo-segundo-orden", "ecuacion-caracteristica", "coeficientes-indeterminados", "variacion-parametros"]
audience: student
last_updated: 2026-01-05
-->

> 🏠 **Navegación:** [← Volver al Índice](../00-Index.md) | [📚 Glosario](../../glossary.md) | [🗺️ Wiki](../../WIKI_INDEX.md)

---

# EDO de Segundo Orden

## Propósito del tema

Resolver ecuaciones diferenciales ordinarias de segundo orden, tanto homogéneas como no homogéneas, usando métodos algebraicos y el concepto de ecuación característica.

## Mapa de Recursos

| Recurso | Archivo | Descripción |
|---------|---------|-------------|
| 📘 Teoría | [ED-02-Teoria-EDO-Segundo-Orden.md](theory/ED-02-Teoria-EDO-Segundo-Orden.md) | Desarrollo completo |
| 🔧 Métodos | [ED-02-Metodos-EDO-Segundo-Orden.md](methods/ED-02-Metodos-EDO-Segundo-Orden.md) | Procedimientos paso a paso |
| 📝 Problemas | [ED-02-Problemas.md](problems/ED-02-Problemas.md) | Ejercicios de práctica |
| ✅ Soluciones | [ED-02-Respuestas.md](solutions/ED-02-Respuestas.md) | Respuestas y desarrollos |
| 📋 Fórmulas | [ED-02-Resumen-Formulas.md](ED-02-Resumen-Formulas.md) | Cheat sheet |

## Ruta de aprendizaje

1. **Ecuaciones homogéneas**: $ay'' + by' + cy = 0$
2. **Ecuación característica**: raíces reales, repetidas, complejas
3. **Ecuaciones no homogéneas**: $ay'' + by' + cy = g(x)$
4. **Coeficientes indeterminados**: polinomios, exponenciales, trigonométricas
5. **Variación de parámetros**: método general
6. **Ecuación de Cauchy-Euler**: $ax^2y'' + bxy' + cy = 0$

## Conexiones

- **Prerrequisitos**: [EDO de primer orden](../01-EDO-Primer-Orden/ED-01-EDO-Primer-Orden-Intro.md), [Valores propios](../../02-Algebra-Lineal/06-Valores-Vectores-Propios/AL-06-Valores-Propios-Intro.md)
- **Usos posteriores**: [Sistemas de EDO](../03-Sistemas-EDO/ED-03-Sistemas-EDO-Intro.md), [Transformada de Laplace](../04-Transformada-Laplace/ED-04-Transformada-Laplace-Intro.md), Vibraciones mecánicas

## Vista previa de conceptos clave

| Tipo de raíces | Ecuación característica | Solución homogénea |
|----------------|-------------------------|---------------------|
| Reales distintas $r_1 \neq r_2$ | $ar^2 + br + c = 0$ | $y_h = C_1 e^{r_1 x} + C_2 e^{r_2 x}$ |
| Reales repetidas $r_1 = r_2 = r$ | discriminante = 0 | $y_h = (C_1 + C_2 x)e^{rx}$ |
| Complejas $\alpha \pm \beta i$ | discriminante < 0 | $y_h = e^{\alpha x}(C_1 \cos\beta x + C_2 \sin\beta x)$ |

### Métodos para solución particular

| Método | Cuándo usar |
|--------|-------------|
| Coeficientes indeterminados | $g(x)$ es polinomio, exponencial, seno/coseno o combinación |
| Variación de parámetros | Cualquier $g(x)$ continua (método general) |

---

> **Nota**: Las EDO de segundo orden modelan vibraciones, circuitos eléctricos y muchos fenómenos físicos. Dominar la ecuación característica es clave.
