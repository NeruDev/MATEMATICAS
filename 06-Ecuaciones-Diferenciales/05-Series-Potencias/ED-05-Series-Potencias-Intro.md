<!--
::METADATA::
type: index
topic_id: ed-05-series-potencias
file_id: ED-05-Series-Potencias-Intro
status: stable
audience: student
requires: [ed-02-[edo](../../glossary.md#edo)-segundo-[orden](../../glossary.md#orden), cd-series-taylor]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

---

# Solución de EDO mediante Series de Potencias

## Propósito del tema

Resolver [ecuaciones diferenciales](../../glossary.md#ecuaciones-diferenciales) mediante series de potencias cuando los métodos algebraicos no son aplicables, incluyendo ecuaciones especiales de la física matemática.

## Mapa de recursos

```
ED-05-Series-Potencias-Intro.md         ← Estás aquí
ED-05-Resumen-Formulas.md               ← Fórmulas clave para repaso
theory/
  └── ED-05-Teoria-Series-EDO.md        ← Desarrollo completo
methods/
  └── [métodos paso a paso]
problems/
  └── [enunciados de práctica]
solutions/
  └── [soluciones detalladas]
```

## Ruta de aprendizaje

1. **Repaso de series**: [convergencia](../../glossary.md#convergencia), radio de convergencia
2. **Puntos ordinarios**: método de series en $x_0$
3. **Puntos singulares**: clasificación (regular vs irregular)
4. **Método de Frobenius**: ecuación indicial, soluciones
5. **Ecuaciones especiales**: Bessel, Legendre, Hermite

## Conexiones

- **Prerequisitos**: [EDO](../../glossary.md#edo) de segundo [orden](../../glossary.md#orden), Series de Taylor
- **Usos posteriores**: Física matemática, Funciones especiales, [EDP](../../glossary.md#edp)

## Vista previa de conceptos clave

### Clasificación de puntos

Para $P(x)y'' + Q(x)y' + R(x)y = 0$:

| Tipo de punto | Condición |
|---------------|-----------|
| Ordinario | $\frac{Q}{P}$ y $\frac{R}{P}$ analíticas en $x_0$ |
| Singular regular | $(x-x_0)\frac{Q}{P}$ y $(x-x_0)^2\frac{R}{P}$ analíticas |
| Singular irregular | No cumple ninguna de las anteriores |

### Ecuaciones especiales

| Ecuación | Forma | Soluciones |
|----------|-------|------------|
| Bessel | $x^2y'' + xy' + (x^2-\nu^2)y = 0$ | $J_\nu(x), Y_\nu(x)$ |
| Legendre | $(1-x^2)y'' - 2xy' + n(n+1)y = 0$ | $P_n(x), Q_n(x)$ |
| Hermite | $y'' - 2xy' + 2ny = 0$ | $H_n(x)$ |

---

<!--
IA: Punto de entrada para Series de Potencias en EDO.
Para fórmulas rápidas: ED-05-Resumen-Formulas.md
file_id: ED-05-Series-Potencias-Intro
-->
