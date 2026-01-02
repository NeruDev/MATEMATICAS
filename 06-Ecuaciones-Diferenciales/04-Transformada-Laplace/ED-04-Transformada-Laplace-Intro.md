<!--
::METADATA::
type: index
topic_id: ed-04-transformada-laplace
file_id: ED-04-Transformada-Laplace-Intro
status: stable
audience: student
requires: [ed-02-[edo](../../glossary.md#orden), ci-integrales-impropias]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Transformada de Laplace

## Propósito del tema

Dominar la [transformada de Laplace](../../glossary.md#ecuaciones-diferenciales) con condiciones iniciales, especialmente útil para funciones discontinuas y sistemas de control.

## Mapa de recursos

```
[ED-04-Transformada-Laplace-Intro.md](ED-04-Resumen-Formulas.md)               ← Fórmulas clave para repaso
theory/
  └── [ED-04-Teoria-Laplace.md](theory/ED-04-Teoria-Transformada-Laplace.md)           ← Desarrollo completo
methods/
  └── [métodos paso a paso]
problems/
  └── [enunciados de práctica]
solutions/
  └── [soluciones detalladas]
```

## Ruta de aprendizaje

1. **Definición**: $\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st}f(t)\,dt$
2. **Transformadas básicas**: tabla de funciones elementales
3. **Propiedades**: [linealidad](../../glossary.md#derivadas), integrales
4. **Transformada inversa**: [fracciones parciales](../../glossary.md#edo) de segundo [orden](../../glossary.md#integrales-impropias)
- **Usos posteriores**: Control automático, Señales y sistemas, Ingeniería

## Vista previa de conceptos clave

### Transformadas fundamentales

| $f(t)$ | $\mathcal{L}\{f(t)\} = F(s)$ |
|--------|------------------------------|
| $1$ | $\frac{1}{s}$ |
| $t^n$ | $\frac{n!}{s^{n+1}}$ |
| $e^{at}$ | $\frac{1}{s-a}$ |
| $\sin(bt)$ | $\frac{b}{s^2+b^2}$ |
| $\cos(bt)$ | $\frac{s}{s^2+b^2}$ |

### Propiedades clave

| Propiedad | Fórmula |
|-----------|---------|
| [Derivada](../../glossary.md#transformada-de-laplace).
Para fórmulas rápidas: [ED-04-Resumen-Formulas.md](ED-04-Resumen-Formulas.md)
file_id: ED-04-Transformada-Laplace-Intro
-->
