<!--
::METADATA::
type: index
topic_id: ci-01-integral-indefinida
file_id: CI-01-Integral-Indefinida-Intro
status: stable
audience: student
requires: [03-calculo-diferencial]
-->

# Integral Indefinida

## Propósito del tema

Comprender el concepto de antiderivada y dominar las fórmulas básicas de integración como proceso inverso de la derivación.

## Mapa de recursos

```
CI-01-Integral-Indefinida-Intro.md      ← Estás aquí
CI-01-Resumen-Formulas.md               ← Fórmulas clave para repaso
theory/
  └── CI-01-Teoria-Integral-Indefinida.md  ← Desarrollo completo
methods/
  └── [métodos paso a paso]
problems/
  └── [enunciados de práctica]
solutions/
  └── [soluciones detalladas]
```

## Ruta de aprendizaje

1. **Concepto de antiderivada**: Si $F'(x) = f(x)$, entonces $F(x)$ es antiderivada de $f(x)$
2. **Notación y constante de integración**: $\int f(x)\,dx = F(x) + C$
3. **Integrales de funciones algebraicas**: potencias, polinomios
4. **Integrales de funciones exponenciales**: $e^x$, $a^x$
5. **Integrales de funciones logarítmicas**: $\ln|x|$
6. **Integrales de funciones trigonométricas**: seno, coseno, tangente, etc.
7. **Integrales que producen funciones inversas**: $\arcsin$, $\arctan$, $\text{arcsec}$
8. **Propiedades de la integral indefinida**: linealidad

## Conexiones

- **Prerrequisitos**: Cálculo Diferencial (derivadas)
- **Usos posteriores**: Técnicas de integración, Integral definida, Ecuaciones diferenciales

## Vista previa de conceptos clave

| Concepto | Descripción |
|----------|-------------|
| Antiderivada | Función cuya derivada es la función dada |
| Constante $C$ | Representa familia de funciones primitivas |
| Verificación | Derivar resultado debe dar función original |
| Linealidad | $\int[af(x)+bg(x)]dx = a\int f(x)dx + b\int g(x)dx$ |

## Idea fundamental

$$\int f(x)\,dx = F(x) + C \iff F'(x) = f(x)$$

La integración "deshace" la derivación. Por cada regla de derivación existe una regla de integración correspondiente.

---

<!--
IA: Punto de entrada para integral indefinida.
Verificar que el estudiante domina derivadas antes de continuar.
file_id: CI-01-Integral-Indefinida-Intro
-->
