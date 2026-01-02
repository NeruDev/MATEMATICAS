<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: FUN-03-Prob-41-Solucion
status: stable
audience: student
problem_ref: "[Prob-41]"
methods: ["diferencia-de-cuadrados", "factorizacion-cascada", "suma-de-cuadrados"]
-->

# Solución [Prob-41]: Diferencia de cuartas potencias (factorización cascada)

> **Problema:** Factoriza: $x^4 - 16$

## Método 1: Factorización en Cascada

### Paso 1: Reconocer la estructura

Observamos que $x^4 - 16$ es una **diferencia de cuadrados**:

$$x^4 - 16 = (x^2)^2 - (4)^2$$

Identificamos:
- $a = x^2$
- $b = 4$

### Paso 2: Aplicar la fórmula $a^2 - b^2 = (a+b)(a-b)$

$$x^4 - 16 = (x^2 + 4)(x^2 - 4)$$

### Paso 3: Analizar cada factor

**Factor 1: $x^2 + 4$**

Este es una **suma de cuadrados**. En los números reales, $x^2 + 4$ **no se puede [factorizar](../../../../glossary.md#factorizar)** porque:
- $x^2 \geq 0$ para todo $x \in \mathbb{R}$
- $x^2 + 4 \geq 4 > 0$ (nunca es cero)
- No tiene raíces reales

**Factor 2: $x^2 - 4$**

Este es otra **diferencia de cuadrados**:

$$x^2 - 4 = (x)^2 - (2)^2$$

### Paso 4: Factorizar $x^2 - 4$

$$x^2 - 4 = (x + 2)(x - 2)$$

### Paso 5: Escribir la factorización completa (en $\mathbb{R}$)

$$x^4 - 16 = (x^2 + 4)(x + 2)(x - 2)$$

---

## Método 2: Reconocimiento directo de potencias

### Paso 1: Escribir como diferencia de cuartas potencias

$$x^4 - 16 = x^4 - 2^4$$

### Paso 2: Usar la fórmula $a^4 - b^4$

La diferencia de cuartas potencias se factoriza como:

$$a^4 - b^4 = (a^2 + b^2)(a^2 - b^2)$$

Y luego:

$$a^4 - b^4 = (a^2 + b^2)(a + b)(a - b)$$

### Paso 3: Aplicar con $a = x$ y $b = 2$

$$x^4 - 2^4 = (x^2 + 2^2)(x + 2)(x - 2)$$

$$x^4 - 16 = (x^2 + 4)(x + 2)(x - 2)$$

---

## Método 3: Factorización completa en $\mathbb{C}$

### Paso 1: Factorización en reales

$$x^4 - 16 = (x^2 + 4)(x + 2)(x - 2)$$

### Paso 2: Factorizar $x^2 + 4$ en los complejos

En $\mathbb{C}$, podemos escribir:

$$x^2 + 4 = x^2 - (-4) = x^2 - (2i)^2$$

Aplicando diferencia de cuadrados:

$$x^2 + 4 = (x + 2i)(x - 2i)$$

### Paso 3: Factorización completa en $\mathbb{C}$

$$x^4 - 16 = (x + 2i)(x - 2i)(x + 2)(x - 2)$$

Las cuatro raíces de $x^4 - 16 = 0$ son: $x = 2, -2, 2i, -2i$

---

## Diagrama de factorización en cascada

```
                    x⁴ - 16
                       │
            ┌──────────┴──────────┐
            │                     │
       (x² + 4)              (x² - 4)
     [suma de cuadrados]   [diferencia de cuadrados]
            │                     │
    No factoriza en ℝ    ┌────────┴────────┐
            │            │                 │
            │        (x + 2)           (x - 2)
            │            │                 │
            └────────────┼─────────────────┘
                         │
               Factorización en ℝ:
           (x² + 4)(x + 2)(x - 2)
```

---

## Verificación algebraica

Expandimos $(x^2 + 4)(x + 2)(x - 2)$:

**Primero:** $(x + 2)(x - 2)$

$$= x^2 - 2x + 2x - 4$$

$$= x^2 - 4$$

**Luego:** $(x^2 + 4)(x^2 - 4)$

$$= x^2 \cdot x^2 + x^2 \cdot (-4) + 4 \cdot x^2 + 4 \cdot (-4)$$

$$= x^4 - 4x^2 + 4x^2 - 16$$

$$= x^4 - 16 \quad \checkmark$$

---

## Verificación numérica

Para $x = 3$:

**Expresión original:**
$$3^4 - 16 = 81 - 16 = 65$$

**[Factorización](../../../../glossary.md#factorización):**
$$(3^2 + 4)(3 + 2)(3 - 2) = (9 + 4)(5)(1)$$

$$= 13 \cdot 5 \cdot 1 = 65 \quad \checkmark$$

---

## Nota importante

⚠️ **Error común:** Intentar factorizar $x^2 + 4$ como $(x + 2)^2$ o $(x + 2)(x + 2)$.

Esto es **incorrecto** porque:
$$(x + 2)^2 = x^2 + 4x + 4 \neq x^2 + 4$$

La suma de cuadrados $a^2 + b^2$ **no se factoriza** en factores lineales con coeficientes reales.

---

## Respuesta Final

**En números reales:**
$$x^4 - 16 = \boxed{(x^2 + 4)(x + 2)(x - 2)}$$

**En números complejos:**
$$x^4 - 16 = (x + 2i)(x - 2i)(x + 2)(x - 2)$$

> 📚 Volver a: [FUN-03-Problemas](../../problems/FUN-03-Problemas.md)
