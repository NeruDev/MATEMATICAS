<!--
::METADATA::
type: solution
topic_id: cd-01-limites
file_id: prob-34-solucion-metodo
problem_ref: [Prob-34]
method: division-por-termino-dominante
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Cociente de polinomios al infinito

**Método aplicado:** División por término de mayor grado

**Paso 1: Identificar el término dominante**
El término de mayor grado tanto en el numerador como en el denominador es $x^1$.

**Paso 2: Dividir todo entre $x$**
$$\lim_{x \to \infty} \frac{3x + 2}{x - 1} = \lim_{x \to \infty} \frac{\frac{3x}{x} + \frac{2}{x}}{\frac{x}{x} - \frac{1}{x}}$$

**Paso 3: Simplificar**
$$= \lim_{x \to \infty} \frac{3 + \frac{2}{x}}{1 - \frac{1}{x}}$$

**Paso 4: Evaluar el [límite](../../../..](../../../../glossary.md)#limite)**
Cuando $x \to \infty$: $\frac{2}{x} \to 0$ y $\frac{1}{x} \to 0$

$$= \frac{3 + 0}{1 - 0} = \frac{3}{1} = 3$$

**Respuesta:**

$$\lim_{x \to \infty} \frac{3x + 2}{x - 1} = 3$$

**Nota:** Cuando los grados son iguales, el [límite](../../../..](../../../../glossary.md)#limite) es el cociente de los coeficientes principales.
