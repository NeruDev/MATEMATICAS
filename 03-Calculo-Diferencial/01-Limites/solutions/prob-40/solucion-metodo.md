<!--
::METADATA::
type: solution
topic_id: cd-01-limites
file_id: prob-40-solucion
problem_ref: Prob-40
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../glossary.md)

---

# Solución: Diferencia de raíces al infinito

## Problema
Evalúa $\displaystyle\lim_{x \to \infty} \left(\sqrt{x^2 + 2x} - \sqrt{x^2 - 2x}\right)$

---

## Análisis inicial
[Forma indeterminada](../../../../glossary.md#forma-indeterminada): $\infty - \infty$

---

## Método: Racionalización por conjugado

### Paso 1: Multiplicar por el conjugado
$$\lim_{x \to \infty} \left(\sqrt{x^2 + 2x} - \sqrt{x^2 - 2x}\right) \cdot \frac{\sqrt{x^2 + 2x} + \sqrt{x^2 - 2x}}{\sqrt{x^2 + 2x} + \sqrt{x^2 - 2x}}$$

### Paso 2: Aplicar diferencia de cuadrados
$$= \lim_{x \to \infty} \frac{(x^2 + 2x) - (x^2 - 2x)}{\sqrt{x^2 + 2x} + \sqrt{x^2 - 2x}}$$

### Paso 3: Simplificar el numerador
$$= \lim_{x \to \infty} \frac{x^2 + 2x - x^2 + 2x}{\sqrt{x^2 + 2x} + \sqrt{x^2 - 2x}}$$

$$= \lim_{x \to \infty} \frac{4x}{\sqrt{x^2 + 2x} + \sqrt{x^2 - 2x}}$$

### Paso 4: Dividir numerador y denominador entre x
Para $x > 0$: $\sqrt{x^2} = x$, entonces:
$$\sqrt{x^2 + 2x} = x\sqrt{1 + \frac{2}{x}}$$
$$\sqrt{x^2 - 2x} = x\sqrt{1 - \frac{2}{x}}$$

$$= \lim_{x \to \infty} \frac{4x}{x\sqrt{1 + \frac{2}{x}} + x\sqrt{1 - \frac{2}{x}}}$$

### Paso 5: Simplificar
$$= \lim_{x \to \infty} \frac{4x}{x\left(\sqrt{1 + \frac{2}{x}} + \sqrt{1 - \frac{2}{x}}\right)}$$

$$= \lim_{x \to \infty} \frac{4}{\sqrt{1 + \frac{2}{x}} + \sqrt{1 - \frac{2}{x}}}$$

### Paso 6: Evaluar el límite
Cuando $x \to \infty$: $\frac{2}{x} \to 0$

$$= \frac{4}{\sqrt{1 + 0} + \sqrt{1 - 0}} = \frac{4}{1 + 1} = \frac{4}{2} = 2$$

---

## Respuesta Final
$$\boxed{\lim_{x \to \infty} \left(\sqrt{x^2 + 2x} - \sqrt{x^2 - 2x}\right) = 2}$$

---

## Verificación numérica

| $x$ | $\sqrt{x^2 + 2x} - \sqrt{x^2 - 2x}$ |
|:---:|:-----------------------------------:|
| 10 | 1.9611... |
| 100 | 1.9960... |
| 1000 | 1.9996... |
| 10000 | 1.99996... |

El valor converge a 2. ✓

---

## Fórmula general
Para $\lim_{x \to \infty} \left(\sqrt{x^2 + ax} - \sqrt{x^2 + bx}\right)$:

$$= \lim_{x \to \infty} \frac{(a-b)x}{\sqrt{x^2 + ax} + \sqrt{x^2 + bx}} = \frac{a - b}{2}$$

En nuestro caso: $a = 2$, $b = -2$, resultado $= \frac{2 - (-2)}{2} = 2$ ✓
