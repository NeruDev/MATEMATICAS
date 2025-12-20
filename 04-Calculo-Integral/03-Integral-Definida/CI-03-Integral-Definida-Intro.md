<!--
::METADATA::
type: index
topic_id: ci-03-integral-definida
file_id: CI-03-Integral-Definida-Intro
status: stable
audience: student
requires: [ci-01-integral-indefinida, ci-02-tecnicas-integracion]
-->

# Integral Definida

## Propósito del tema

Comprender la integral definida como límite de sumas de Riemann y aplicar el Teorema Fundamental del Cálculo para evaluar integrales.

## Mapa de recursos

```
CI-03-Integral-Definida-Intro.md        ← Estás aquí
CI-03-Resumen-Formulas.md               ← Fórmulas clave para repaso
theory/
  └── CI-03-Teoria-Integral-Definida.md ← Desarrollo completo
methods/
  └── [métodos paso a paso]
problems/
  └── [enunciados de práctica]
solutions/
  └── [soluciones detalladas]
```

## Ruta de aprendizaje

1. **Sumas de Riemann**: aproximación del área bajo la curva
2. **Definición de integral definida**: límite de sumas de Riemann
3. **Propiedades de la integral definida**: linealidad, aditividad, comparación
4. **Teorema Fundamental del Cálculo (Parte 1)**: derivada de la función integral
5. **Teorema Fundamental del Cálculo (Parte 2)**: evaluación de integrales
6. **Sustitución en integrales definidas**: cambio de límites
7. **Funciones pares e impares**: simplificación de cálculos

## Conexiones

- **Prerrequisitos**: Integral indefinida, Técnicas de integración, Límites
- **Usos posteriores**: Aplicaciones de la integral, Integrales impropias, Cálculo vectorial

## Vista previa de conceptos clave

| Concepto | Descripción |
|----------|-------------|
| Suma de Riemann | $\sum_{i=1}^{n} f(x_i^*) \Delta x$ |
| Integral definida | $\int_a^b f(x)\,dx = \lim_{n\to\infty} \sum_{i=1}^{n} f(x_i^*) \Delta x$ |
| TFC Parte 1 | $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$ |
| TFC Parte 2 | $\int_a^b f(x)\,dx = F(b) - F(a)$ |

## Idea fundamental

La integral definida conecta dos conceptos aparentemente distintos:
- **Geométrico**: Área bajo la curva
- **Analítico**: Antiderivada evaluada en los límites

$$\int_a^b f(x)\,dx = F(b) - F(a) = \left[F(x)\right]_a^b$$

---

<!--
IA: Punto de entrada para integral definida.
El TFC es el resultado central de este tema.
file_id: CI-03-Integral-Definida-Intro
-->
