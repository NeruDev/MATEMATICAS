<!--
::METADATA::
type: index
topic_id: ci-05-integrales-impropias
file_id: CI-05-Integrales-Impropias-Intro
status: stable
audience: student
requires: [ci-03-integral-definida, ci-02-tecnicas-integracion]
-->

# Integrales Impropias

## Propósito del tema

Extender el concepto de integral definida a casos con límites infinitos o integrandos con discontinuidades, y determinar convergencia o divergencia.

## Mapa de recursos

```
CI-05-Integrales-Impropias-Intro.md     ← Estás aquí
CI-05-Resumen-Formulas.md               ← Fórmulas clave para repaso
theory/
  └── CI-05-Teoria-Impropias.md         ← Desarrollo completo
methods/
  └── [métodos paso a paso]
problems/
  └── [enunciados de práctica]
solutions/
  └── [soluciones detalladas]
```

## Ruta de aprendizaje

1. **Tipo I - Límites infinitos**: $\int_a^\infty f(x)\,dx$, $\int_{-\infty}^b f(x)\,dx$
2. **Tipo II - Discontinuidades**: integrando discontinuo en el intervalo
3. **Convergencia y divergencia**: cuándo existe el límite
4. **Criterio de comparación directa**: comparar con integrales conocidas
5. **Criterio de comparación por límite**: para funciones que se comportan similarmente
6. **Integrales p**: $\int_1^\infty \frac{1}{x^p}\,dx$ convergente si $p > 1$

## Conexiones

- **Prerrequisitos**: Integral definida, Límites, Técnicas de integración
- **Usos posteriores**: Series, Transformada de Laplace, Probabilidad

## Vista previa de conceptos clave

| Concepto | Descripción |
|----------|-------------|
| Tipo I | Límites de integración infinitos |
| Tipo II | Integrando con discontinuidad |
| Convergente | El límite existe y es finito |
| Divergente | El límite no existe o es infinito |
| Integral p | Referencia fundamental para comparación |

## Idea fundamental

Una integral impropia se evalúa como **límite**:

$$\int_a^\infty f(x)\,dx = \lim_{t\to\infty} \int_a^t f(x)\,dx$$

Si el límite existe y es finito → **converge**  
Si el límite no existe o es infinito → **diverge**

---

<!--
IA: Punto de entrada para integrales impropias.
Enfatizar la diferencia entre convergencia y divergencia.
file_id: CI-05-Integrales-Impropias-Intro
-->
