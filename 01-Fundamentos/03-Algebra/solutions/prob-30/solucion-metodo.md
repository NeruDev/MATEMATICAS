<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: FUN-03-Prob-30-Solucion
status: stable
audience: student
problem_ref: "[Prob-30]"
methods: ["binomio-de-newton", "triangulo-de-pascal", "coeficientes-binomiales"]
-->

# Solución [Prob-30]: Binomio de Newton - expansión completa

> **Problema:** Expande $(x + 1)^5$ usando el binomio de Newton.

## Método 1: Fórmula del Binomio de Newton

### Paso 1: Recordar la fórmula general

$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$$

### Paso 2: Identificar los elementos

En nuestro caso:
- $a = x$
- $b = 1$
- $n = 5$

### Paso 3: Escribir la expansión término por término

$$(x + 1)^5 = \sum_{k=0}^{5} \binom{5}{k} x^{5-k} \cdot 1^k$$

Como $1^k = 1$ para todo $k$:

$$(x + 1)^5 = \sum_{k=0}^{5} \binom{5}{k} x^{5-k}$$

### Paso 4: Calcular cada coeficiente binomial

**Para $k = 0$:**
$$\binom{5}{0} = \frac{5!}{0! \cdot 5!} = \frac{5!}{1 \cdot 5!} = 1$$

**Para $k = 1$:**
$$\binom{5}{1} = \frac{5!}{1! \cdot 4!} = \frac{5 \cdot 4!}{1 \cdot 4!} = 5$$

**Para $k = 2$:**
$$\binom{5}{2} = \frac{5!}{2! \cdot 3!} = \frac{5 \cdot 4 \cdot 3!}{2 \cdot 1 \cdot 3!} = \frac{20}{2} = 10$$

**Para $k = 3$:**
$$\binom{5}{3} = \frac{5!}{3! \cdot 2!} = \frac{5 \cdot 4 \cdot 3!}{3! \cdot 2} = \frac{20}{2} = 10$$

**Para $k = 4$:**
$$\binom{5}{4} = \frac{5!}{4! \cdot 1!} = \frac{5 \cdot 4!}{4! \cdot 1} = 5$$

**Para $k = 5$:**
$$\binom{5}{5} = \frac{5!}{5! \cdot 0!} = \frac{5!}{5! \cdot 1} = 1$$

### Paso 5: Construir cada término

| $k$ | $\binom{5}{k}$ | $x^{5-k}$ | Término |
|-----|----------------|-----------|---------|
| 0 | 1 | $x^5$ | $1 \cdot x^5 = x^5$ |
| 1 | 5 | $x^4$ | $5 \cdot x^4 = 5x^4$ |
| 2 | 10 | $x^3$ | $10 \cdot x^3 = 10x^3$ |
| 3 | 10 | $x^2$ | $10 \cdot x^2 = 10x^2$ |
| 4 | 5 | $x^1$ | $5 \cdot x = 5x$ |
| 5 | 1 | $x^0$ | $1 \cdot 1 = 1$ |

### Paso 6: Escribir la expansión completa

$$(x + 1)^5 = x^5 + 5x^4 + 10x^3 + 10x^2 + 5x + 1$$

---

## Método 2: Triángulo de Pascal

### Paso 1: Construir el triángulo hasta la fila 5

```
Fila 0:           1
Fila 1:          1   1
Fila 2:         1   2   1
Fila 3:        1   3   3   1
Fila 4:       1   4   6   4   1
Fila 5:      1   5  10  10   5   1
```

Cada número es la suma de los dos números directamente arriba de él.

### Paso 2: Usar los coeficientes de la fila 5

La fila 5 es: $1, 5, 10, 10, 5, 1$

### Paso 3: Formar los términos

$$(x + 1)^5 = 1 \cdot x^5 + 5 \cdot x^4 + 10 \cdot x^3 + 10 \cdot x^2 + 5 \cdot x + 1$$

$$(x + 1)^5 = x^5 + 5x^4 + 10x^3 + 10x^2 + 5x + 1$$

---

## Método 3: Expansión iterativa

### Paso 1: Calcular $(x + 1)^2$

$$(x + 1)^2 = x^2 + 2x + 1$$

### Paso 2: Calcular $(x + 1)^3 = (x + 1)^2 \cdot (x + 1)$

$$(x^2 + 2x + 1)(x + 1)$$

Multiplicando término por término:

$$= x^2 \cdot x + x^2 \cdot 1 + 2x \cdot x + 2x \cdot 1 + 1 \cdot x + 1 \cdot 1$$

$$= x^3 + x^2 + 2x^2 + 2x + x + 1$$

$$= x^3 + 3x^2 + 3x + 1$$

### Paso 3: Calcular $(x + 1)^4 = (x + 1)^3 \cdot (x + 1)$

$$(x^3 + 3x^2 + 3x + 1)(x + 1)$$

$$= x^3 \cdot x + x^3 \cdot 1 + 3x^2 \cdot x + 3x^2 \cdot 1 + 3x \cdot x + 3x \cdot 1 + 1 \cdot x + 1 \cdot 1$$

$$= x^4 + x^3 + 3x^3 + 3x^2 + 3x^2 + 3x + x + 1$$

$$= x^4 + 4x^3 + 6x^2 + 4x + 1$$

### Paso 4: Calcular $(x + 1)^5 = (x + 1)^4 \cdot (x + 1)$

$$(x^4 + 4x^3 + 6x^2 + 4x + 1)(x + 1)$$

$$= x^4 \cdot x + x^4 \cdot 1 + 4x^3 \cdot x + 4x^3 \cdot 1 + 6x^2 \cdot x + 6x^2 \cdot 1 + 4x \cdot x + 4x \cdot 1 + 1 \cdot x + 1 \cdot 1$$

$$= x^5 + x^4 + 4x^4 + 4x^3 + 6x^3 + 6x^2 + 4x^2 + 4x + x + 1$$

Agrupando términos semejantes:

$$= x^5 + (1 + 4)x^4 + (4 + 6)x^3 + (6 + 4)x^2 + (4 + 1)x + 1$$

$$= x^5 + 5x^4 + 10x^3 + 10x^2 + 5x + 1$$

---

## Verificación numérica

Evaluamos en $x = 2$:

**Lado izquierdo:**
$$(2 + 1)^5 = 3^5 = 243$$

**Lado derecho:**
$$2^5 + 5(2^4) + 10(2^3) + 10(2^2) + 5(2) + 1$$

$$= 32 + 5(16) + 10(8) + 10(4) + 10 + 1$$

$$= 32 + 80 + 80 + 40 + 10 + 1$$

$$= 243 \quad \checkmark$$

---

## Propiedades observadas

1. **Simetría:** Los coeficientes son simétricos: $1, 5, 10, 10, 5, 1$

2. **Suma de coeficientes:** $1 + 5 + 10 + 10 + 5 + 1 = 32 = 2^5$
   (Esto se verifica evaluando en $x = 1$: $(1+1)^5 = 2^5 = 32$)

3. **Alternancia de signos:** Si evaluamos en $x = -1$: $(−1+1)^5 = 0$
   (La suma alternada de coeficientes es 0)

---

## Respuesta Final

**$(x + 1)^5 = \boxed{x^5 + 5x^4 + 10x^3 + 10x^2 + 5x + 1}$**

> 📚 Volver a: [FUN-03-Problemas](../../problems/FUN-03-Problemas.md)
