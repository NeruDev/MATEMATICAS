<!--
::METADATA::
type: index
topic_id: ed-04-transformada-laplace
file_id: ED-04-Transformada-Laplace-Intro
status: stable
audience: student
requires: [ed-02-[edo](../../glossary.md#edo)-segundo-[orden](../../glossary.md#orden), ci-integrales-impropias]
-->

# Transformada de Laplace

## Propósito del tema

Dominar la [transformada de Laplace](../../glossary.md#transformada-de-laplace) como herramienta algebraica para resolver [ecuaciones diferenciales](../../glossary.md#ecuaciones-diferenciales) con condiciones iniciales, especialmente útil para funciones discontinuas y sistemas de control.

## Mapa de recursos

```
ED-04-Transformada-Laplace-Intro.md     ← Estás aquí
ED-04-Resumen-Formulas.md               ← Fórmulas clave para repaso
theory/
  └── ED-04-Teoria-Laplace.md           ← Desarrollo completo
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
3. **Propiedades**: [linealidad](../../glossary.md#linealidad), traslación, [derivadas](../../glossary.md#derivadas), integrales
4. **Transformada inversa**: [fracciones parciales](../../glossary.md#fracciones-parciales)
5. **Resolución de PVI**: método algebraico
6. **Funciones especiales**: escalón unitario, delta de Dirac

## Conexiones

- **Prerequisitos**: [EDO](../../glossary.md#edo) de segundo [orden](../../glossary.md#orden), [Integrales impropias](../../glossary.md#integrales-impropias)
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
| [Derivada](../../glossary.md#derivada) | $\mathcal{L}\{f'(t)\} = sF(s) - f(0)$ |
| Traslación en $s$ | $\mathcal{L}\{e^{at}f(t)\} = F(s-a)$ |
| Traslación en $t$ | $\mathcal{L}\{u(t-a)f(t-a)\} = e^{-as}F(s)$ |

---

<!--
IA: Punto de entrada para [Transformada de Laplace](../../glossary.md#transformada-de-laplace).
Para fórmulas rápidas: ED-04-Resumen-Formulas.md
file_id: ED-04-Transformada-Laplace-Intro
-->
