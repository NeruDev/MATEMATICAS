<!--
::METADATA::
type: solution
topic_id: cd-01-limites
file_id: prob-18-solucion-metodo
problem_ref: [Prob-18]
method: racionalizacion
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../glossary.md)

---

# Solución: Racionalización de numerador

**Método aplicado:** Racionalización

**Paso 1: Verificar [forma indeterminada](../../../../glossary.md#forma-indeterminada)**
$$\lim_{x \to 4} \frac{\sqrt{x} - 2}{x - 4} = \frac{\sqrt{4} - 2}{4 - 4} = \frac{0}{0}$$

**Paso 2: Multiplicar por el conjugado**
$$\frac{\sqrt{x} - 2}{x - 4} \cdot \frac{\sqrt{x} + 2}{\sqrt{x} + 2} = \frac{(\sqrt{x})^2 - 2^2}{(x - 4)(\sqrt{x} + 2)}$$

**Paso 3: Simplificar**
$$= \frac{x - 4}{(x - 4)(\sqrt{x} + 2)} = \frac{1}{\sqrt{x} + 2} \quad (x \neq 4)$$

**Paso 4: Evaluar el [límite](../../../../glossary.md#limite)**
$$\lim_{x \to 4} \frac{1}{\sqrt{x} + 2} = \frac{1}{\sqrt{4} + 2} = \frac{1}{2 + 2} = \frac{1}{4}$$

**Respuesta:**

$$\lim_{x \to 4} \frac{\sqrt{x} - 2}{x - 4} = \frac{1}{4}$$
