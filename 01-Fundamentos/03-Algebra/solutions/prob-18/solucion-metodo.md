<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: FUN-03-Prob-18-Solucion
status: stable
audience: student
problem_ref: "[Prob-18]"
methods: ["division-sintetica", "factorizacion-por-raices", "teorema-del-factor"]
-->

# Solución [Prob-18]: Factorización con raíces (división sintética)

> **Problema:** Si $P(x) = x^3 - 6x^2 + 11x - 6$ y $P(1) = 0$, factoriza $P(x)$ completamente.

## Método 1: División Sintética

### Paso 1: Verificar que $x = 1$ es raíz

Calculamos $P(1)$:

$$P(1) = (1)^3 - 6(1)^2 + 11(1) - 6$$

$$P(1) = 1 - 6 + 11 - 6$$

$$P(1) = 0 \quad \checkmark$$

Como $P(1) = 0$, por el **Teorema del Factor**, $(x - 1)$ es factor de $P(x)$.

### Paso 2: Aplicar división sintética con $x = 1$

Coeficientes de $P(x)$: $1, -6, 11, -6$

```
    1  │  1    -6    11    -6
       │       1    -5     6
       ├─────────────────────
          1    -5     6     0
```

**Proceso detallado:**
1. Bajar el 1: $\downarrow 1$
2. $1 \times 1 = 1$, luego $-6 + 1 = -5$
3. $1 \times (-5) = -5$, luego $11 + (-5) = 6$
4. $1 \times 6 = 6$, luego $-6 + 6 = 0$ ✓ (residuo cero)

### Paso 3: Escribir el cociente

El cociente es: $x^2 - 5x + 6$

Por lo tanto:

$$P(x) = (x - 1)(x^2 - 5x + 6)$$

### Paso 4: Factorizar el trinomio cuadrático

Necesitamos factorizar $x^2 - 5x + 6$.

Buscamos dos números que:
- **Sumen** $-5$
- **Multipliquen** $6$

Los números son: $-2$ y $-3$

$$(-2) + (-3) = -5 \quad \checkmark$$
$$(-2) \times (-3) = 6 \quad \checkmark$$

Por lo tanto:

$$x^2 - 5x + 6 = (x - 2)(x - 3)$$

### Paso 5: Factorización completa

$$P(x) = (x - 1)(x - 2)(x - 3)$$

---

## Método 2: División Sintética Consecutiva

### Paso 1: Primera división con $x = 1$

Como ya verificamos, $(x - 1)$ es factor:

$$P(x) = (x - 1)(x^2 - 5x + 6)$$

### Paso 2: Buscar raíces del cociente

Para $Q(x) = x^2 - 5x + 6$, probamos valores enteros divisores de 6: $\pm 1, \pm 2, \pm 3, \pm 6$

Probamos $x = 2$:

$$Q(2) = (2)^2 - 5(2) + 6 = 4 - 10 + 6 = 0 \quad \checkmark$$

### Paso 3: Segunda división sintética con $x = 2$

Coeficientes de $Q(x)$: $1, -5, 6$

```
    2  │  1    -5     6
       │       2    -6
       ├──────────────
          1    -3     0
```

**Proceso:**
1. Bajar el 1
2. $2 \times 1 = 2$, luego $-5 + 2 = -3$
3. $2 \times (-3) = -6$, luego $6 + (-6) = 0$ ✓

El cociente es: $x - 3$

### Paso 4: Factorización completa

$$Q(x) = (x - 2)(x - 3)$$

$$P(x) = (x - 1)(x - 2)(x - 3)$$

---

## Método 3: Fórmula cuadrática para el cociente

### Paso 1: Después de la primera división

$$P(x) = (x - 1)(x^2 - 5x + 6)$$

### Paso 2: Aplicar fórmula cuadrática a $x^2 - 5x + 6$

Identificamos: $a = 1$, $b = -5$, $c = 6$

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

$$x = \frac{-(-5) \pm \sqrt{(-5)^2 - 4(1)(6)}}{2(1)}$$

$$x = \frac{5 \pm \sqrt{25 - 24}}{2}$$

$$x = \frac{5 \pm \sqrt{1}}{2}$$

$$x = \frac{5 \pm 1}{2}$$

Las raíces son:

$$x_1 = \frac{5 + 1}{2} = \frac{6}{2} = 3$$

$$x_2 = \frac{5 - 1}{2} = \frac{4}{2} = 2$$

### Paso 3: Factorización completa

$$x^2 - 5x + 6 = (x - 2)(x - 3)$$

$$P(x) = (x - 1)(x - 2)(x - 3)$$

---

## Verificación

Expandimos $(x - 1)(x - 2)(x - 3)$:

**Primero:** $(x - 1)(x - 2)$

$$= x^2 - 2x - x + 2$$

$$= x^2 - 3x + 2$$

**Luego:** $(x^2 - 3x + 2)(x - 3)$

$$= x^3 - 3x^2 - 3x^2 + 9x + 2x - 6$$

$$= x^3 - 6x^2 + 11x - 6$$

$$= P(x) \quad \checkmark$$

**Verificación de raíces:**
- $P(1) = 1 - 6 + 11 - 6 = 0$ ✓
- $P(2) = 8 - 24 + 22 - 6 = 0$ ✓
- $P(3) = 27 - 54 + 33 - 6 = 0$ ✓

---

## Respuesta Final

**$P(x) = x^3 - 6x^2 + 11x - 6 = \boxed{(x - 1)(x - 2)(x - 3)}$**

> 📚 Volver a: [FUN-03-Problemas](../../problems/FUN-03-Problemas.md)
