<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: prob-50-solucion
problem_ref: Prob-50
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../glossary.md)

---

# Solución: Ecuación con fracciones algebraicas

## Problema
Resuelve: $\frac{x}{x-2} + \frac{2}{x+2} = \frac{8}{x^2-4}$

---

## Método: Multiplicar por el MCM

### Paso 1: Factorizar los denominadores
- $(x - 2)$: ya factorizado
- $(x + 2)$: ya factorizado
- $(x^2 - 4) = (x-2)(x+2)$: diferencia de cuadrados

### Paso 2: Identificar el MCM
$$\text{[MCM](../../../../glossary.md#mcm)} = (x - 2)(x + 2) = x^2 - 4$$

### Paso 3: Identificar restricciones
Para que la ecuación tenga sentido, los denominadores no pueden ser cero:
- $x - 2 \neq 0 \Rightarrow x \neq 2$
- $x + 2 \neq 0 \Rightarrow x \neq -2$

### Paso 4: Multiplicar toda la ecuación por el MCM
$$\frac{x}{x-2} \cdot (x-2)(x+2) + \frac{2}{x+2} \cdot (x-2)(x+2) = \frac{8}{(x-2)(x+2)} \cdot (x-2)(x+2)$$

### Paso 5: Simplificar cada término
**Primer término:**
$$\frac{x \cdot (x-2)(x+2)}{x-2} = x(x+2) = x^2 + 2x$$

**Segundo término:**
$$\frac{2 \cdot (x-2)(x+2)}{x+2} = 2(x-2) = 2x - 4$$

**Tercer término:**
$$\frac{8 \cdot (x-2)(x+2)}{(x-2)(x+2)} = 8$$

### Paso 6: Escribir la ecuación simplificada
$$x^2 + 2x + 2x - 4 = 8$$

### Paso 7: Simplificar
$$x^2 + 4x - 4 = 8$$
$$x^2 + 4x - 12 = 0$$

### Paso 8: Resolver la ecuación cuadrática

**Método: [Factorización](../../../../glossary.md#factorizacion)**

Buscamos dos números que:
- Multipliquen a $-12$
- Sumen $4$

Los números son: $6$ y $-2$ (porque $6 \times (-2) = -12$ y $6 + (-2) = 4$)

$$x^2 + 4x - 12 = (x + 6)(x - 2) = 0$$

**Soluciones:**
$$x + 6 = 0 \Rightarrow x = -6$$
$$x - 2 = 0 \Rightarrow x = 2$$

### Paso 9: Verificar restricciones
- $x = -6$: Válido (no está en las restricciones)
- $x = 2$: **Inválido** (hace el denominador cero)

---

## Respuesta Final
$$\boxed{x = -6}$$

---

## Verificación
Sustituyendo $x = -6$ en la ecuación original:

**Lado izquierdo:**
$$\frac{-6}{-6-2} + \frac{2}{-6+2} = \frac{-6}{-8} + \frac{2}{-4} = \frac{3}{4} - \frac{1}{2} = \frac{3}{4} - \frac{2}{4} = \frac{1}{4}$$

**Lado derecho:**
$$\frac{8}{(-6)^2-4} = \frac{8}{36-4} = \frac{8}{32} = \frac{1}{4}$$

$$\frac{1}{4} = \frac{1}{4}$$ ✓

---

## Nota sobre la solución extraña
La solución $x = 2$ es una **solución extraña**. Aparece porque al multiplicar por $(x-2)(x+2)$, introducimos artificialmente la posibilidad de que $x = 2$. Por eso es fundamental verificar las restricciones al final.
