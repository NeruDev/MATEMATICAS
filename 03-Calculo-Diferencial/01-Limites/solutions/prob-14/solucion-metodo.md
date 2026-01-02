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


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Factorización de diferencia de cuadrados

**Método aplicado:** [Factorización](../../../../glossary.md#factorizacion)

**Paso 1: Intentar [sustitución](../../../../glossary.md#sustitucion) directa**
$$\lim_{x \to 5} \frac{x^2 - 25}{x - 5} = \frac{5^2 - 25}{5 - 5} = \frac{0}{0}$$
[Forma indeterminada](../../../../glossary.md#forma-indeterminada), continuar con [factorización](../../../../glossary.md#factorizacion).

**Paso 2: [Factorizar](../../../../glossary.md#factorizar) numerador**
- Numerador: $x^2 - 25 = (x-5)(x+5)$ (diferencia de cuadrados)
- Denominador: $x - 5$ (ya factorizado)

**Paso 3: Cancelar factores comunes**
$$\frac{x^2 - 25}{x - 5} = \frac{(x-5)(x+5)}{x-5} = x + 5 \quad (x \neq 5)$$

**Paso 4: Evaluar el [límite](../../../../glossary.md#limite) simplificado**
$$\lim_{x \to 5} (x + 5) = 5 + 5 = 10$$

**Respuesta:**

$$\lim_{x \to 5} \frac{x^2 - 25}{x - 5} = 10$$
