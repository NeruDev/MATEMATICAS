<!--
::METADATA::
type: cheatsheet
topic_id: ci-02-tecnicas-integracion
file_id: CI-02-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Resumen rápido — Técnicas de Integración

## 1. Sustitución (Cambio de variable)

$$\int f(g(x)) \cdot g'(x)\,dx = \int f(u)\,du \quad \text{donde } u = g(x)$$

**Pasos:**
1. Identificar $u = g(x)$
2. Calcular $du = g'(x)\,dx$
3. Sustituir y resolver
4. Regresar a variable original

## 2. Integración por partes

$$\int u\,dv = uv - \int v\,du$$

**Regla LIATE** (prioridad para elegir $u$):
| Prioridad | Tipo | Ejemplo |
|-----------|------|---------|
| 1 | Logarítmicas | $\ln x$, $\log x$ |
| 2 | Inversas trig. | $\arctan x$, $\arcsin x$ |
| 3 | Algebraicas | $x^2$, $x$, $\sqrt{x}$ |
| 4 | Trigonométricas | $\sin x$, $\cos x$ |
| 5 | Exponenciales | $e^x$, $a^x$ |

**Fórmula tabular** para múltiples aplicaciones.

## 3. Integrales trigonométricas

### $\int \sin^m x \cos^n x\,dx$

| Caso | Estrategia |
|------|------------|
| $m$ impar | Guardar $\sin x$, usar $\sin^2 x = 1 - \cos^2 x$ |
| $n$ impar | Guardar $\cos x$, usar $\cos^2 x = 1 - \sin^2 x$ |
| Ambos pares | Usar: $\sin^2 x = \frac{1-\cos 2x}{2}$, $\cos^2 x = \frac{1+\cos 2x}{2}$ |

### $\int \tan^m x \sec^n x\,dx$

| Caso | Estrategia |
|------|------------|
| $n$ par | Guardar $\sec^2 x$, usar $\sec^2 x = 1 + \tan^2 x$ |
| $m$ impar | Guardar $\sec x \tan x$, usar $\tan^2 x = \sec^2 x - 1$ |

## 4. Sustitución trigonométrica

| Expresión | [Sustitución](../../glossary.md#tecnicas-de-integracion).
Para desarrollo completo: [theory/CI-02-Teoria-Tecnicas-Integracion.md](theory/CI-02-Teoria-Tecnicas-Integracion.md)
file_id: CI-02-Resumen-Formulas
-->
