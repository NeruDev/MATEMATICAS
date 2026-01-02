<!--
::METADATA::
type: index
topic_id: ed-02-[edo](../../glossary.md#edo)-segundo-[orden](../../glossary.md#orden)
file_id: ED-02-[EDO](../../glossary.md#edo)-Segundo-[Orden](../../glossary.md#orden)-Intro
status: stable
audience: student
requires: [ed-01-edo-primer-orden, al-valores-vectores-propios]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

---

# EDO de Segundo Orden

## Propósito del tema

Resolver [ecuaciones diferenciales](../../glossary.md#ecuaciones-diferenciales) de segundo orden con coeficientes constantes y variables, esenciales para modelar oscilaciones, vibraciones y circuitos eléctricos.

## Mapa de recursos

```
ED-02-EDO-Segundo-Orden-Intro.md        ← Estás aquí
ED-02-Resumen-Formulas.md               ← Fórmulas clave para repaso
theory/
  └── ED-02-Teoria-EDO-Segundo-Orden.md ← Desarrollo completo
methods/
  └── [métodos paso a paso]
problems/
  └── [enunciados de práctica]
solutions/
  └── [soluciones detalladas]
```

## Ruta de aprendizaje

1. **Ecuaciones homogéneas**: $ay'' + by' + cy = 0$
2. **Ecuación característica**: raíces reales, repetidas, complejas
3. **Ecuaciones no homogéneas**: $ay'' + by' + cy = g(x)$
4. **Coeficientes indeterminados**: polinomios, exponenciales, trigonométricas
5. **Variación de parámetros**: método general
6. **Ecuación de Cauchy-Euler**: $ax^2y'' + bxy' + cy = 0$

## Conexiones

- **Prerequisitos**: EDO de primer orden, [Álgebra lineal](../../glossary.md#algebra-lineal) (valores propios)
- **Usos posteriores**: Sistemas de EDO, [Transformada de Laplace](../../glossary.md#transformada-de-laplace), Vibraciones

## Vista previa de conceptos clave

| Tipo de raíces | Ecuación característica | Solución homogénea |
|----------------|-------------------------|---------------------|
| Reales distintas $r_1 \neq r_2$ | $ar^2 + br + c = 0$ | $y_h = C_1 e^{r_1 x} + C_2 e^{r_2 x}$ |
| Reales repetidas $r_1 = r_2 = r$ | discriminante = 0 | $y_h = (C_1 + C_2 x)e^{rx}$ |
| Complejas $\alpha \pm \beta i$ | discriminante < 0 | $y_h = e^{\alpha x}(C_1 \cos\beta x + C_2 \sin\beta x)$ |

### Métodos para solución particular

| Método | Cuándo usar |
|--------|-------------|
| Coeficientes indeterminados | $g(x)$ es [polinomio](../../glossary.md#polinomio), exponencial o trigonométrica |
| Variación de parámetros | Cualquier $g(x)$ continua |

---

<!--
IA: Punto de entrada para EDO de Segundo Orden.
Para fórmulas rápidas: ED-02-Resumen-Formulas.md
file_id: ED-02-EDO-Segundo-Orden-Intro
-->
