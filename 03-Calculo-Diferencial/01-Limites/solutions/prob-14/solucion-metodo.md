<!--
::METADATA::
type: solution
topic_id: cd-01-limites
file_id: prob-14-solucion-metodo
problem_ref: [Prob-14]
method: factorizacion
status: stable
audience: student
-->

# Solución: Factorización de diferencia de cuadrados

**Método aplicado:** Factorización

**Paso 1: Intentar sustitución directa**
$$\lim_{x \to 5} \frac{x^2 - 25}{x - 5} = \frac{5^2 - 25}{5 - 5} = \frac{0}{0}$$
Forma indeterminada, continuar con factorización.

**Paso 2: Factorizar numerador**
- Numerador: $x^2 - 25 = (x-5)(x+5)$ (diferencia de cuadrados)
- Denominador: $x - 5$ (ya factorizado)

**Paso 3: Cancelar factores comunes**
$$\frac{x^2 - 25}{x - 5} = \frac{(x-5)(x+5)}{x-5} = x + 5 \quad (x \neq 5)$$

**Paso 4: Evaluar el límite simplificado**
$$\lim_{x \to 5} (x + 5) = 5 + 5 = 10$$

**Respuesta:**

$$\lim_{x \to 5} \frac{x^2 - 25}{x - 5} = 10$$
