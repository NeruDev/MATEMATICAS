<!--
::METADATA::
type: index
topic_id: ci-01-integral-indefinida
file_id: CI-01-Integral-Indefinida-Intro
status: stable
audience: student
requires: [03-calculo-diferencial]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

---

# Integral Indefinida

## Propósito del tema

Comprender el concepto de [antiderivada](../..](../../glossary.md)#antiderivada) y dominar las fórmulas básicas de integración como proceso inverso de la derivación.

## Mapa de recursos

```
[CI-01-Integral-Indefinida-Intro.md](CI-01-Integral-Indefinida-Intro.md)      ← Estás aquí
[CI-01-Resumen-Formulas.md](CI-01-Resumen-Formulas.md)               ← Fórmulas clave para repaso
theory/
  └── [CI-01-Teoria-Integral-Indefinida.md](CI-01-Teoria-Integral-Indefinida.md)  ← Desarrollo completo
methods/
  └── [métodos paso a paso]
problems/
  └── [enunciados de práctica]
solutions/
  └── [soluciones detalladas]
```

## Ruta de aprendizaje

1. **Concepto de [antiderivada](../..](../../glossary.md)#antiderivada)**: Si $F'(x) = f(x)$, entonces $F(x)$ es antiderivada de $f(x)$
2. **Notación y [constante de integración](../..](../../glossary.md)#constante-de-integracion)**: $\int f(x)\,dx = F(x) + C$
3. **Integrales de funciones algebraicas**: potencias, polinomios
4. **Integrales de funciones exponenciales**: $e^x$, $a^x$
5. **Integrales de funciones logarítmicas**: $\ln|x|$
6. **Integrales de funciones trigonométricas**: [seno](../..](../../glossary.md)#seno), [coseno](../..](../../glossary.md)#coseno), [tangente](../..](../../glossary.md)#tangente), etc.
7. **Integrales que producen funciones inversas**: $\arcsin$, $\arctan$, $\text{arcsec}$
8. **Propiedades de la [integral indefinida](../..](../../glossary.md)#integral-indefinida)**: [linealidad](../..](../../glossary.md)#linealidad)

## Conexiones

- **Prerrequisitos**: [Cálculo Diferencial](../..](../../glossary.md)#calculo-diferencial) ([derivadas](../..](../../glossary.md)#derivadas))
- **Usos posteriores**: [Técnicas de integración](../..](../../glossary.md)#tecnicas-de-integracion), [Integral definida](../..](../../glossary.md)#integral-definida), [Ecuaciones diferenciales](../..](../../glossary.md)#ecuaciones-diferenciales)

## Vista previa de conceptos clave

| Concepto | Descripción |
|----------|-------------|
| Antiderivada | [Función](../../glossary.md#funcion) cuya [derivada](../../glossary.md#derivada) es la función dada |
| Constante $C$ | Representa familia de funciones primitivas |
| Verificación | Derivar resultado debe dar [función](../../glossary.md#funcion) original |
| [Linealidad](../../glossary.md#linealidad) | $\int[af(x)+bg(x)]dx = a\int f(x)dx + b\int g(x)dx$ |

## Idea fundamental

$$\int f(x)\,dx = F(x) + C \iff F'(x) = f(x)$$

La integración "deshace" la derivación. Por cada regla de derivación existe una regla de integración correspondiente.

---

<!--
IA: Punto de entrada para [integral indefinida](../..](../../glossary.md)#integral-indefinida).
Verificar que el estudiante domina [derivadas](../..](../../glossary.md)#derivadas) antes de continuar.
file_id: CI-01-Integral-Indefinida-Intro
-->
