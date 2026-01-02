<!--
::METADATA::
type: solution
topic_id: cd-01-limites
file_id: prob-05-solucion-metodo
problem_ref: [Prob-05]
method: analisis-por-casos
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Límites laterales con valor absoluto

**Método aplicado:** Análisis por casos

**Paso 1: Recordar la definición de valor absoluto**
$$|x| = \begin{cases} x & \text{si } x \geq 0 \\ -x & \text{si } x < 0 \end{cases}$$

**Paso 2: [Límite](../../../..](../../../../glossary.md)#limite) por la derecha ($x \to 0^+$)**
Cuando $x > 0$: $|x| = x$

$$\lim_{x \to 0^+} \frac{|x|}{x} = \lim_{x \to 0^+} \frac{x}{x} = \lim_{x \to 0^+} 1 = 1$$

**Paso 3: [Límite](../../../..](../../../../glossary.md)#limite) por la izquierda ($x \to 0^-$)**
Cuando $x < 0$: $|x| = -x$

$$\lim_{x \to 0^-} \frac{|x|}{x} = \lim_{x \to 0^-} \frac{-x}{x} = \lim_{x \to 0^-} (-1) = -1$$

**Respuesta:**
$$\lim_{x \to 0^+} \frac{|x|}{x} = 1, \quad \lim_{x \to 0^-} \frac{|x|}{x} = -1$$

**Conclusión:** Como los límites laterales son distintos, $\lim_{x \to 0} \frac{|x|}{x}$ **no existe**.
