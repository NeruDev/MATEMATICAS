<!--
::METADATA::
type: index
topic_id: ci-04-aplicaciones-integral
file_id: CI-04-Aplicaciones-Integral-Intro
status: stable
audience: student
requires: [ci-03-integral-definida, ci-02-tecnicas-integracion]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

---

# Aplicaciones de la Integral

## Propósito del tema

Aplicar la [integral definida](../../glossary.md#integral-definida) para resolver problemas geométricos y físicos: cálculo de áreas, volúmenes, longitud de arco, área de superficie y trabajo.

## Mapa de recursos

```
CI-04-Aplicaciones-Integral-Intro.md    ← Estás aquí
CI-04-Resumen-Formulas.md               ← Fórmulas clave para repaso
theory/
  └── CI-04-Teoria-Aplicaciones.md      ← Desarrollo completo
methods/
  └── [métodos paso a paso]
problems/
  └── [enunciados de práctica]
solutions/
  └── [soluciones detalladas]
```

## Ruta de aprendizaje

1. **Área entre curvas**: región entre dos funciones
2. **Volúmenes por discos**: sólidos de revolución alrededor de un eje
3. **Volúmenes por arandelas**: sólidos con hueco central
4. **Volúmenes por capas cilíndricas**: método alternativo
5. **Longitud de arco**: longitud de curvas planas
6. **Área de superficie de revolución**: superficies generadas por rotación
7. **Trabajo**: trabajo realizado por fuerzas variables

## Conexiones

- **Prerrequisitos**: [Integral definida](../../glossary.md#integral-definida), [Técnicas de integración](../../glossary.md#tecnicas-de-integracion), Geometría analítica
- **Usos posteriores**: Cálculo vectorial, Física, Ingeniería

## Vista previa de conceptos clave

| Aplicación | Fórmula [base](../../glossary.md#base) |
|------------|--------------|
| Área entre curvas | $A = \int_a^b [f(x) - g(x)]\,dx$ |
| Volumen (discos) | $V = \pi\int_a^b [R(x)]^2\,dx$ |
| Volumen (capas) | $V = 2\pi\int_a^b x \cdot f(x)\,dx$ |
| Longitud de arco | $L = \int_a^b \sqrt{1 + [f'(x)]^2}\,dx$ |
| Trabajo | $W = \int_a^b F(x)\,dx$ |

## Idea fundamental

La integral definida representa **acumulación**:
- Área = acumulación de "rebanadas" infinitesimales de altura
- Volumen = acumulación de "discos" o "capas" infinitesimales
- Longitud = acumulación de segmentos infinitesimales
- Trabajo = acumulación de trabajo infinitesimal

---

<!--
IA: Punto de entrada para aplicaciones de la integral.
Enfatizar la interpretación geométrica de cada fórmula.
file_id: CI-04-Aplicaciones-Integral-Intro
-->
