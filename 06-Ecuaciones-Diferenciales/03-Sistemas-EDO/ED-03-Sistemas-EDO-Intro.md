<!--
::METADATA::
type: index
topic_id: ed-03-sistemas-[edo](../..](../../glossary.md)#edo)
file_id: ED-03-Sistemas-[EDO](../..](../../glossary.md)#edo)-Intro
status: stable
audience: student
requires: [ed-02-edo-segundo-[orden](../..](../../glossary.md)#orden), al-valores-vectores-propios]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

---

# Sistemas de Ecuaciones Diferenciales

## Propósito del tema

Resolver sistemas de [ecuaciones diferenciales](../..](../../glossary.md)#ecuaciones-diferenciales) usando métodos matriciales, esenciales para modelar sistemas interconectados y analizar estabilidad.

## Mapa de recursos

```
[ED-03-Sistemas-EDO-Intro.md](ED-03-Sistemas-EDO-Intro.md)             ← Estás aquí
[ED-03-Resumen-Formulas.md](ED-03-Resumen-Formulas.md)               ← Fórmulas clave para repaso
theory/
  └── [ED-03-Teoria-Sistemas-EDO.md](ED-03-Teoria-Sistemas-EDO.md)      ← Desarrollo completo
methods/
  └── [métodos paso a paso]
problems/
  └── [enunciados de práctica]
solutions/
  └── [soluciones detalladas]
```

## Ruta de aprendizaje

1. **Forma matricial**: conversión $\mathbf{X}' = A\mathbf{X}$
2. **Valores propios reales distintos**: solución con eigenvectores
3. **Valores propios complejos**: soluciones reales
4. **Valores propios repetidos**: vectores generalizados
5. **Sistemas no homogéneos**: variación de parámetros
6. **Retratos de fase**: clasificación de puntos críticos
7. **[Matriz](../..](../../glossary.md)#matriz) exponencial**: $e^{At}$ y solución fundamental

## Conexiones

- **Prerequisitos**: EDO de segundo [orden](../..](../../glossary.md)#orden), [Álgebra lineal](../..](../../glossary.md)#algebra-lineal) (eigenvalores)
- **Usos posteriores**: Estabilidad, Control, Modelado de sistemas

## Vista previa de conceptos clave

### Forma matricial

$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} \quad \Leftrightarrow \quad \mathbf{X}' = A\mathbf{X}$$

### Clasificación de puntos de equilibrio

| Valores propios | Tipo | Estabilidad |
|-----------------|------|-------------|
| $\lambda_1, \lambda_2 < 0$ reales | Nodo estable | Asintóticamente estable |
| $\lambda_1, \lambda_2 > 0$ reales | Nodo inestable | Inestable |
| $\lambda_1 < 0 < \lambda_2$ | Punto silla | Inestable |
| $\alpha \pm \beta i$, $\alpha < 0$ | Espiral estable | Asintóticamente estable |
| $\alpha \pm \beta i$, $\alpha > 0$ | Espiral inestable | Inestable |
| $\pm \beta i$ (puros) | Centro | Estable (no asintótico) |

---

<!--
IA: Punto de entrada para Sistemas de EDO.
Para fórmulas rápidas: [ED-03-Resumen-Formulas.md](ED-03-Resumen-Formulas.md)
file_id: ED-03-Sistemas-EDO-Intro
-->
