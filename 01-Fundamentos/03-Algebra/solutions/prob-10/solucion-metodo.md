<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: FUN-03-Prob-10-Solucion
status: stable
audience: student
problem_ref: "[Prob-10]"
methods: ["binomio-de-newton", "coeficientes-binomiales"]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../glossary.md)

---

# Solución [Prob-10]: Coeficiente en expansión del binomio

> **Problema:** ¿Cuál es el coeficiente del término de grado 3 en $(x + 2)^4$?

## Método 1: Binomio de Newton

### Paso 1: Recordar la fórmula del Binomio de Newton

La expansión de $(a + b)^n$ está dada por:

$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$$

donde $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ es el coeficiente binomial.

### Paso 2: Identificar los elementos

En nuestro caso:
- $a = x$
- $b = 2$
- $n = 4$

El término general es:

$$T_{k+1} = \binom{4}{k} x^{4-k} \cdot 2^k$$

### Paso 3: Encontrar el término de grado 3

Para que el término tenga grado 3 en $x$, necesitamos:

$$4 - k = 3$$

$$k = 1$$

### Paso 4: Calcular el término correspondiente

Sustituyendo $k = 1$:

$$T_2 = \binom{4}{1} x^{4-1} \cdot 2^1$$

$$T_2 = \binom{4}{1} x^3 \cdot 2$$

### Paso 5: Calcular el coeficiente binomial

$$\binom{4}{1} = \frac{4!}{1!(4-1)!} = \frac{4!}{1! \cdot 3!}$$

$$\binom{4}{1} = \frac{4 \cdot 3!}{1 \cdot 3!} = \frac{4}{1} = 4$$

### Paso 6: Calcular el coeficiente total

$$T_2 = 4 \cdot x^3 \cdot 2 = 8x^3$$

El coeficiente del término de grado 3 es:

$$4 \cdot 2 = 8$$

---

## Método 2: Expansión directa

### Paso 1: Expandir $(x + 2)^4$ como $((x + 2)^2)^2$

Primero calculamos $(x + 2)^2$:

$$(x + 2)^2 = x^2 + 2 \cdot x \cdot 2 + 2^2$$

$$(x + 2)^2 = x^2 + 4x + 4$$

### Paso 2: Elevar al cuadrado

$$(x + 2)^4 = (x^2 + 4x + 4)^2$$

### Paso 3: Expandir el cuadrado del trinomio

$$(x^2 + 4x + 4)^2 = (x^2)^2 + (4x)^2 + (4)^2 + 2(x^2)(4x) + 2(x^2)(4) + 2(4x)(4)$$

Calculando término por término:

- $(x^2)^2 = x^4$
- $(4x)^2 = 16x^2$
- $(4)^2 = 16$
- $2(x^2)(4x) = 8x^3$
- $2(x^2)(4) = 8x^2$
- $2(4x)(4) = 32x$

### Paso 4: Combinar términos

$$(x + 2)^4 = x^4 + 8x^3 + 16x^2 + 8x^2 + 32x + 16$$

$$(x + 2)^4 = x^4 + 8x^3 + 24x^2 + 32x + 16$$

### Paso 5: Identificar el coeficiente de $x^3$

De la expansión completa, el término de grado 3 es $8x^3$.

El coeficiente es **8**.

---

## Verificación con Triángulo de Pascal

La fila 4 del triángulo de Pascal es: $1, 4, 6, 4, 1$

Los términos de $(x + 2)^4$ son:

| $k$ | Coef. Binomial | $x^{4-k}$ | $2^k$ | Término completo |
|-----|----------------|-----------|-------|------------------|
| 0 | 1 | $x^4$ | 1 | $1 \cdot x^4 \cdot 1 = x^4$ |
| 1 | 4 | $x^3$ | 2 | $4 \cdot x^3 \cdot 2 = 8x^3$ |
| 2 | 6 | $x^2$ | 4 | $6 \cdot x^2 \cdot 4 = 24x^2$ |
| 3 | 4 | $x^1$ | 8 | $4 \cdot x \cdot 8 = 32x$ |
| 4 | 1 | $x^0$ | 16 | $1 \cdot 1 \cdot 16 = 16$ |

✓ Confirma que el coeficiente de $x^3$ es **8**.

---

## Respuesta Final

**El coeficiente del término de grado 3 en $(x + 2)^4$ es $\boxed{8}$**

> 📚 Volver a: [FUN-03-Problemas](../../problems/FUN-03-Problemas.md)
