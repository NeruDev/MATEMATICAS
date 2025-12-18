<!--
HUMANO:
Solución detallada.
Puede incluir el mismo método con todos los pasos
y/o métodos alternativos comparados.

IA:
Aquí SÍ puedes explicar, justificar y comparar.
-->

---
content_type: solution
solution_type: detailed
expected_output:
  default: markdown
---

# Solución detallada

## Método principal

<!--
Explicación paso a paso
-->

### Análisis del problema

Evaluamos:
$$\lim_{x \to 3} \frac{x^2 - 9}{x - 3}$$

### Desarrollo paso a paso

**Paso 1: Verificar si hay forma indeterminada**

Intentamos sustitución directa:
$$f(3) = \frac{3^2 - 9}{3 - 3} = \frac{9 - 9}{0} = \frac{0}{0}$$

Obtenemos la forma indeterminada $\frac{0}{0}$, lo que nos indica que:
- El límite **podría** existir (no está determinado aún)
- Necesitamos técnicas algebraicas para resolverlo
- Hay un factor común que se anula en ambos

**Paso 2: Factorización del numerador**

El numerador $x^2 - 9$ es una diferencia de cuadrados:
$$x^2 - 9 = x^2 - 3^2 = (x - 3)(x + 3)$$

**Paso 3: Simplificación**

Sustituimos y simplificamos:
$$\frac{x^2 - 9}{x - 3} = \frac{(x-3)(x+3)}{x-3}$$

Como estamos evaluando el límite cuando $x \to 3$ (no en $x = 3$), tenemos $x \neq 3$, lo que nos permite cancelar:
$$= x + 3 \quad \text{para } x \neq 3$$

**Paso 4: Evaluación del límite**

Ahora la expresión simplificada es continua en $x = 3$:
$$\lim_{x \to 3} (x + 3) = 3 + 3 = 6$$

### Verificación numérica

| $x$ | $\frac{x^2-9}{x-3}$ |
|-----|---------------------|
| 2.9 | 5.9 |
| 2.99 | 5.99 |
| 2.999 | 5.999 |
| 3.001 | 6.001 |
| 3.01 | 6.01 |
| 3.1 | 6.1 |

Los valores se aproximan a 6 desde ambos lados. ✓

## Métodos alternativos (si existen)

<!--
Comparación conceptual
-->

### Método gráfico

La función $f(x) = \frac{x^2-9}{x-3}$ tiene:
- Un "hueco" en $x = 3$ (punto de discontinuidad removible)
- La gráfica es la recta $y = x + 3$ con un hueco en $(3, 6)$

Observando la gráfica, vemos que la función se aproxima a $y = 6$ cuando $x \to 3$.

### Comparación de métodos

| Método | Resultado | Precisión |
|--------|-----------|-----------|
| Factorización | 6 | Exacto |
| Numérico | ≈ 6 | Aproximado |
| Gráfico | 6 | Visual |

La factorización proporciona el resultado exacto y justificado algebraicamente.

---

<!--
IA: Para soluciones rápidas, consulta method-solution.md en esta carpeta.
-->
