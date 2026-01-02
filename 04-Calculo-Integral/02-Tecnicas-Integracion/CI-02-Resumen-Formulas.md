<!--
::METADATA::
type: cheatsheet
topic_id: ci-02-tecnicas-integracion
file_id: CI-02-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

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

| Expresión | [Sustitución](../../glossary.md#sustitucion) | Identidad usada |
|-----------|-------------|-----------------|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ | $1 - \sin^2\theta = \cos^2\theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$ | $1 + \tan^2\theta = \sec^2\theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$ | $\sec^2\theta - 1 = \tan^2\theta$ |

## 5. Fracciones parciales

Para $\int \dfrac{P(x)}{Q(x)}\,dx$ donde $\deg(P) < \deg(Q)$:

| Factor en $Q(x)$ | Descomposición |
|------------------|----------------|
| $(ax+b)$ | $\dfrac{A}{ax+b}$ |
| $(ax+b)^n$ | $\dfrac{A_1}{ax+b} + \dfrac{A_2}{(ax+b)^2} + \cdots + \dfrac{A_n}{(ax+b)^n}$ |
| $(ax^2+bx+c)$ irreducible | $\dfrac{Ax+B}{ax^2+bx+c}$ |
| $(ax^2+bx+c)^n$ irreducible | $\dfrac{A_1x+B_1}{ax^2+bx+c} + \cdots + \dfrac{A_nx+B_n}{(ax^2+bx+c)^n}$ |

### Integrales resultantes comunes

$$\int \frac{1}{x-a}\,dx = \ln|x-a| + C$$

$$\int \frac{1}{x^2+a^2}\,dx = \frac{1}{a}\arctan\frac{x}{a} + C$$

$$\int \frac{x}{x^2+a^2}\,dx = \frac{1}{2}\ln(x^2+a^2) + C$$

## 6. Completar el cuadrado

Para $ax^2 + bx + c$:

$$ax^2 + bx + c = a\left(x + \frac{b}{2a}\right)^2 + c - \frac{b^2}{4a}$$

## Guía de selección de técnica

```
¿Es integral directa? → Usar tabla básica
       ↓ No
¿Hay composición evidente? → Sustitución
       ↓ No
¿Es producto de funciones diferentes? → Por partes
       ↓ No
¿Tiene √(a²±x²) o √(x²-a²)? → Sust. trigonométrica
       ↓ No
¿Es fracción racional? → Fracciones parciales
       ↓ No
¿Tiene productos trig? → Identidades trigonométricas
```

---

<!--
IA: Hoja de referencia rápida para [técnicas de integración](../../glossary.md#tecnicas-de-integracion).
Para desarrollo completo: theory/CI-02-Teoria-Tecnicas.md
file_id: CI-02-Resumen-Formulas
-->
