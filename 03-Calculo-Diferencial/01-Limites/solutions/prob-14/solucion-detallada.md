<!--
::METADATA::
type: solution
topic_id: cd-01-limites
file_id: prob-14-solucion-detallada
problem_ref: [Prob-14]
method: factorizacion
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución detallada: Factorización de diferencia de cuadrados

## Método principal

### Análisis del problema

Evaluamos:
$$\lim_{x \to 5} \frac{x^2 - 25}{x - 5}$$

### Desarrollo paso a paso

**Paso 1: Verificar si hay [forma indeterminada](../../../..](../../../../glossary.md)#forma-indeterminada)**

Intentamos [sustitución](../../../..](../../../../glossary.md)#sustitucion) directa:
$$f(5) = \frac{5^2 - 25}{5 - 5} = \frac{25 - 25}{0} = \frac{0}{0}$$

Obtenemos la [forma indeterminada](../../../..](../../../../glossary.md)#forma-indeterminada) $\frac{0}{0}$, lo que nos indica que:
- El [límite](../../../..](../../../../glossary.md)#limite) **podría** existir (no está determinado aún)
- Necesitamos técnicas algebraicas para resolverlo
- Hay un factor común que se anula en ambos

**Paso 2: [Factorización](../../../..](../../../../glossary.md)#factorizacion) del numerador**

El numerador $x^2 - 25$ es una diferencia de cuadrados:
$$x^2 - 25 = x^2 - 5^2 = (x - 5)(x + 5)$$

**Paso 3: Simplificación**

Sustituimos y simplificamos:
$$\frac{x^2 - 25}{x - 5} = \frac{(x-5)(x+5)}{x-5}$$

Como estamos evaluando el [límite](../../../..](../../../../glossary.md)#limite) cuando $x \to 5$ (no en $x = 5$), tenemos $x \neq 5$, lo que nos permite cancelar:
$$= x + 5 \quad \text{para } x \neq 5$$

**Paso 4: Evaluación del límite**

Ahora la expresión simplificada es continua en $x = 5$:
$$\lim_{x \to 5} (x + 5) = 5 + 5 = 10$$

### Verificación numérica

| $x$ | $\frac{x^2-25}{x-5}$ |
|-----|----------------------|
| 4.9 | 9.9 |
| 4.99 | 9.99 |
| 4.999 | 9.999 |
| 5.001 | 10.001 |
| 5.01 | 10.01 |
| 5.1 | 10.1 |

Los valores se aproximan a 10 desde ambos lados. ✓

## Métodos alternativos

### Método gráfico

La [función](../../../..](../../../../glossary.md)#funcion) $f(x) = \frac{x^2-25}{x-5}$ tiene:
- Un "hueco" en $x = 5$ ([discontinuidad removible](../../../..](../../../../glossary.md)#discontinuidad-removible))
- La gráfica es la recta $y = x + 5$ con un hueco en $(5, 10)$

### Comparación de métodos

| Método | Resultado | Precisión |
|--------|-----------|-----------|
| [Factorización](../../../../glossary.md#factorizacion) | 10 | Exacto |
| Numérico | ≈ 10 | Aproximado |
| Gráfico | 10 | Visual |

La factorización proporciona el resultado exacto y justificado algebraicamente.
