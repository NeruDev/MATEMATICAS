<!--
HUMANO:
Solución usando ÚNICAMENTE el método asignado.
Concisa, sin explicaciones largas.

IA:
Respeta estrictamente el método indicado.
No introduzcas métodos alternativos aquí.

---
content_type: solution
solution_type: method
expected_output:
  default: markdown
---
-->

# Solución por método

<!--
Pasos claros y directos
-->

**Método aplicado:** factorizacion

**Paso 1: Intentar sustitución directa**
$$\lim_{x \to 3} \frac{x^2 - 9}{x - 3} = \frac{3^2 - 9}{3 - 3} = \frac{0}{0}$$
Forma indeterminada, continuar con factorización.

**Paso 2: Factorizar numerador y denominador**
- Numerador: $x^2 - 9 = (x-3)(x+3)$ (diferencia de cuadrados)
- Denominador: $x - 3$ (ya factorizado)

**Paso 3: Cancelar factores comunes**
$$\frac{x^2 - 9}{x - 3} = \frac{(x-3)(x+3)}{x-3} = x + 3 \quad (x \neq 3)$$

**Paso 4: Evaluar el límite simplificado**
$$\lim_{x \to 3} (x + 3) = 3 + 3 = 6$$

**Respuesta:**

$$\lim_{x \to 3} \frac{x^2 - 9}{x - 3} = 6$$

---

<!--
IA: Esta solución sigue estrictamente el método "factorizacion".
-->
