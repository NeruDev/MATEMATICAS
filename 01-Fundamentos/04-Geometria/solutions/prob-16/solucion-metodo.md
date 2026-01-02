<!--
::METADATA::
type: solution
topic_id: fun-04-geometria
file_id: FUN-04-Prob-16-Solucion
status: stable
audience: student
problem_ref: "[Prob-16]"
methods: ["demostracion-geometrica", "paralelas-transversal", "angulos-alternos"]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución [Prob-16]: Suma de ángulos interiores de un triángulo

> **Problema:** Demuestra que la suma de los ángulos interiores de un triángulo es 180° usando el teorema de las paralelas cortadas por una transversal.

## Diagrama conceptual

```
                    D ←————————— A ——————————→ E
                                /\
                               /  \
                              /    \
                             /      \
                            /   α    \
                           /          \
                          /            \
                         /              \
                        /                \
                       /                  \
                      / β                γ \
                     B ———————————————————— C
```

**Elementos del diagrama:**
- $\triangle ABC$ es el triángulo con ángulos interiores $\alpha$, $\beta$, $\gamma$
- $\overleftrightarrow{DE}$ es una recta paralela a $\overline{BC}$ que pasa por el vértice $A$
- $\alpha = \angle BAC$ (ángulo en el vértice $A$)
- $\beta = \angle ABC$ (ángulo en el vértice $B$)
- $\gamma = \angle BCA$ (ángulo en el vértice $C$)

---

## Hipótesis y Tesis

### Hipótesis
- $\triangle ABC$ es un triángulo cualquiera
- $\alpha$, $\beta$, $\gamma$ son sus ángulos interiores

### Tesis
$$\alpha + \beta + \gamma = 180°$$

---

## Demostración paso a paso

### Paso 1: Construcción auxiliar

Por el vértice $A$, trazamos la recta $\overleftrightarrow{DE}$ paralela al lado $\overline{BC}$.

$$\overleftrightarrow{DE} \parallel \overline{BC}$$

> **Justificación:** Por el postulado de las paralelas (Euclides), por un punto exterior a una recta pasa una única recta paralela a ella.

### Paso 2: Identificar las transversales

Los lados $\overline{AB}$ y $\overline{AC}$ del triángulo actúan como **transversales** que cortan a las rectas paralelas $\overleftrightarrow{DE}$ y $\overline{BC}$.

**Transversal 1:** $\overleftrightarrow{AB}$ corta a:
- $\overleftrightarrow{DE}$ en el punto $A$
- $\overline{BC}$ en el punto $B$

**Transversal 2:** $\overleftrightarrow{AC}$ corta a:
- $\overleftrightarrow{DE}$ en el punto $A$
- $\overline{BC}$ en el punto $C$

### Paso 3: Aplicar el teorema de ángulos alternos internos (Primera transversal)

Para la transversal $\overleftrightarrow{AB}$ que corta a las paralelas $\overleftrightarrow{DE}$ y $\overline{BC}$:

$$\angle DAB = \angle ABC = \beta$$

> **Justificación:** Si dos rectas paralelas son cortadas por una transversal, los ángulos alternos internos son congruentes.

Los ángulos $\angle DAB$ y $\angle ABC$ son alternos internos porque:
- Están en lados opuestos de la transversal $\overleftrightarrow{AB}$
- Están entre las paralelas $\overleftrightarrow{DE}$ y $\overline{BC}$

### Paso 4: Aplicar el teorema de ángulos alternos internos (Segunda transversal)

Para la transversal $\overleftrightarrow{AC}$ que corta a las paralelas $\overleftrightarrow{DE}$ y $\overline{BC}$:

$$\angle EAC = \angle BCA = \gamma$$

> **Justificación:** Nuevamente, por el teorema de ángulos alternos internos.

### Paso 5: Analizar los ángulos sobre la recta $\overleftrightarrow{DE}$

Los tres ángulos $\angle DAB$, $\angle BAC$ y $\angle EAC$ son **ángulos adyacentes** que juntos forman un **ángulo llano** sobre la recta $\overleftrightarrow{DE}$.

$$\angle DAB + \angle BAC + \angle EAC = 180°$$

> **Justificación:** Los ángulos sobre una recta (ángulo llano) suman 180°.

### Paso 6: Sustitución y conclusión

Sustituimos las igualdades obtenidas en los pasos 3 y 4:

$$\angle DAB = \beta, \quad \angle BAC = \alpha, \quad \angle EAC = \gamma$$

Por lo tanto:

$$\beta + \alpha + \gamma = 180°$$

Reordenando:

$$\boxed{\alpha + \beta + \gamma = 180°}$$

---

## Resumen de la demostración

| Paso | Afirmación | Justificación |
|:----:|:-----------|:--------------|
| 1 | Trazar $\overleftrightarrow{DE} \parallel \overline{BC}$ por $A$ | Postulado de las paralelas |
| 2 | $\overleftrightarrow{AB}$ y $\overleftrightarrow{AC}$ son transversales | Definición de transversal |
| 3 | $\angle DAB = \beta$ | Ángulos alternos internos |
| 4 | $\angle EAC = \gamma$ | Ángulos alternos internos |
| 5 | $\angle DAB + \angle BAC + \angle EAC = 180°$ | Ángulo llano |
| 6 | $\alpha + \beta + \gamma = 180°$ | [Sustitución](../../../../glossary.md#sustitucion) |

---

## Verificación: Casos particulares

### Triángulo equilátero

Si $\alpha = \beta = \gamma$, entonces:

$$3\alpha = 180° \implies \alpha = 60°$$

Cada ángulo mide $60°$, lo cual coincide con la definición de triángulo equilátero. ✓

### Triángulo rectángulo

Si $\gamma = 90°$, entonces:

$$\alpha + \beta = 180° - 90° = 90°$$

Los ángulos agudos de un triángulo rectángulo son complementarios. ✓

### Triángulo isósceles con $\alpha = 100°$

$$\beta + \gamma = 180° - 100° = 80°$$

Si $\beta = \gamma$ (isósceles), entonces $\beta = \gamma = 40°$. ✓

---

## Observaciones importantes

1. **Validez universal:** Esta demostración aplica a **cualquier triángulo** (equilátero, isósceles, escaleno, acutángulo, rectángulo u obtusángulo).

2. **Dependencia del quinto postulado:** La demostración utiliza el postulado de las paralelas de Euclides. En geometrías no euclidianas, la suma puede ser diferente de 180°.

3. **Corolario:** Un triángulo no puede tener más de un ángulo recto ni más de un ángulo obtuso.

---

## Respuesta Final

$$\boxed{\text{La suma de los ángulos interiores de un triángulo es } 180°}$$

La demostración se basa en trazar una paralela a un lado por el vértice opuesto y aplicar el teorema de ángulos alternos internos formados por las paralelas cortadas por transversales.
