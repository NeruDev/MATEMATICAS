<!--
::METADATA::
type: index
topic_id: ed-01-edo-primer-orden
file_id: ED-01-EDO-Primer-Orden-Intro
status: stable
audience: student
requires: [ci-integral-indefinida, ci-tecnicas-integracion]
-->

# EDO de Primer Orden

## Propósito del tema

Dominar los métodos de resolución de ecuaciones diferenciales ordinarias de primer orden, fundamentales para modelar fenómenos de crecimiento, decaimiento y sistemas dinámicos.

## Mapa de recursos

```
ED-01-EDO-Primer-Orden-Intro.md         ← Estás aquí
ED-01-Resumen-Formulas.md               ← Fórmulas clave para repaso
theory/
  └── ED-01-Teoria-EDO-Primer-Orden.md  ← Desarrollo completo
methods/
  └── [métodos paso a paso]
problems/
  └── [enunciados de práctica]
solutions/
  └── [soluciones detalladas]
```

## Ruta de aprendizaje

1. **Conceptos fundamentales**: orden, grado, solución general y particular
2. **Ecuaciones separables**: $\frac{dy}{dx} = f(x)g(y)$
3. **Ecuaciones lineales**: $\frac{dy}{dx} + P(x)y = Q(x)$
4. **Ecuaciones exactas**: $M(x,y)dx + N(x,y)dy = 0$
5. **Ecuación de Bernoulli**: $\frac{dy}{dx} + P(x)y = Q(x)y^n$
6. **Ecuaciones homogéneas**: sustitución $y = vx$

## Conexiones

- **Prerequisitos**: Cálculo Integral (integración, técnicas)
- **Usos posteriores**: EDO de orden superior, Sistemas de EDO, Modelado

## Vista previa de conceptos clave

| Tipo de EDO | Forma | Método |
|-------------|-------|--------|
| Separable | $\frac{dy}{dx} = f(x)g(y)$ | Separar e integrar |
| Lineal | $y' + P(x)y = Q(x)$ | Factor integrante $\mu = e^{\int P\,dx}$ |
| Exacta | $M\,dx + N\,dy = 0$, $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$ | Hallar $F(x,y) = C$ |
| Bernoulli | $y' + P(x)y = Q(x)y^n$ | Sustitución $v = y^{1-n}$ |
| Homogénea | $\frac{dy}{dx} = f\left(\frac{y}{x}\right)$ | Sustitución $y = vx$ |

---

<!--
IA: Punto de entrada para EDO de Primer Orden.
Para fórmulas rápidas: ED-01-Resumen-Formulas.md
file_id: ED-01-EDO-Primer-Orden-Intro
-->
