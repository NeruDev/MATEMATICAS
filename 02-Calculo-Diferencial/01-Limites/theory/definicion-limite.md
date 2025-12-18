<!--
HUMANO:
Aquí va teoría pura: definiciones, intuición, teoremas.
No se resuelven problemas aquí.

IA:
Este archivo define CONCEPTOS.
No generes procedimientos ni ejercicios aquí.
-->

---
content_type: theory
expected_output:
  default: markdown
audience: self-study
---

# Definición de Límite

## Definición formal

<!--
Matemática precisa. LaTeX permitido.
-->

### Definición intuitiva

El **límite** de $f(x)$ cuando $x$ tiende a $a$ es $L$ si los valores de $f(x)$ se aproximan arbitrariamente a $L$ cuando $x$ se aproxima a $a$ (sin ser igual a $a$).

$$\lim_{x \to a} f(x) = L$$

### Definición formal (épsilon-delta)

$$\lim_{x \to a} f(x) = L$$

Si y solo si: para todo $\varepsilon > 0$, existe un $\delta > 0$ tal que:

$$0 < |x - a| < \delta \Rightarrow |f(x) - L| < \varepsilon$$

### Límites laterales

**Límite por la derecha:**
$$\lim_{x \to a^+} f(x) = L$$
($x$ se aproxima a $a$ desde valores mayores que $a$)

**Límite por la izquierda:**
$$\lim_{x \to a^-} f(x) = L$$
($x$ se aproxima a $a$ desde valores menores que $a$)

**Teorema:** $\lim_{x \to a} f(x) = L$ existe si y solo si ambos límites laterales existen e son iguales.

## Intuición

<!--
Explicación conceptual, no operativa.
-->

Piensa en el límite como una pregunta sobre el **destino**, no sobre la **llegada**:

> "¿Hacia dónde va $f(x)$ cuando $x$ se acerca a $a$?"

No importa si $f(a)$ existe o cuál es su valor. El límite estudia el comportamiento **alrededor** del punto, no **en** el punto.

**Analogía:** Es como preguntar "¿hacia dónde va este camino?" mientras te acercas a un punto. Puedes ver la dirección aunque no puedas llegar exactamente al punto.

## Qué NO es

<!--
Errores comunes y confusiones típicas.
-->

**NO es:**
- El valor de la función en el punto: $\lim_{x \to a} f(x) \neq f(a)$ (en general)
- Una sustitución directa siempre válida
- Un valor que $x$ "alcanza"

**Errores comunes:**

1. **Confundir límite con valor de función:**
   - $f(2)$ puede no existir, pero $\lim_{x \to 2} f(x)$ puede existir

2. **Ignorar formas indeterminadas:**
   - $\frac{0}{0}$ no significa que el límite sea 0 o indefinido

3. **Asumir que límites laterales diferentes implican que el límite no existe:**
   - Correcto, pero debemos verificar ambos lados

## Representaciones

<!--
Algebraica, geométrica, gráfica, física si aplica.
-->

### Representación algebraica
$$\lim_{x \to 2} \frac{x^2 - 4}{x - 2} = \lim_{x \to 2} \frac{(x-2)(x+2)}{x-2} = \lim_{x \to 2} (x+2) = 4$$

### Representación gráfica
En la gráfica, el límite es el valor de $y$ al que se aproxima la curva cuando $x$ se acerca al punto de interés, siguiendo la curva desde ambos lados.

### Representación numérica (tabla)
| $x$ | $f(x)$ |
|-----|--------|
| 1.9 | 3.9 |
| 1.99 | 3.99 |
| 1.999 | 3.999 |
| 2.001 | 4.001 |
| 2.01 | 4.01 |
| 2.1 | 4.1 |

La tabla sugiere que $\lim_{x \to 2} f(x) = 4$.

---

<!--
IA: Este archivo es solo teoría. Para procedimientos, consulta methods/.
-->
