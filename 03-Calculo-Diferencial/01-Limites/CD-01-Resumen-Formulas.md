<!--
::METADATA::
type: cheatsheet
topic_id: cd-01-limites
file_id: CD-01-Resumen-Formulas
status: stable
audience: student
-->

# Resumen de Fórmulas: Límites

## Definición Formal (Épsilon-Delta)

$$\lim_{x \to a} f(x) = L \iff \forall \varepsilon > 0, \exists \delta > 0 : 0 < |x - a| < \delta \Rightarrow |f(x) - L| < \varepsilon$$

## Propiedades de los Límites

Sean $\lim_{x \to a} f(x) = L$ y $\lim_{x \to a} g(x) = M$, entonces:

| Propiedad | Fórmula |
|-----------|---------|
| Suma | $\lim_{x \to a} [f(x) + g(x)] = L + M$ |
| Diferencia | $\lim_{x \to a} [f(x) - g(x)] = L - M$ |
| Producto | $\lim_{x \to a} [f(x) \cdot g(x)] = L \cdot M$ |
| Cociente | $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{L}{M}, \quad M \neq 0$ |
| Potencia | $\lim_{x \to a} [f(x)]^n = L^n$ |
| Constante | $\lim_{x \to a} c = c$ |
| Múltiplo | $\lim_{x \to a} c \cdot f(x) = c \cdot L$ |

## Límites Notables

### Límites Trigonométricos

$$\lim_{x \to 0} \frac{\sin x}{x} = 1$$

$$\lim_{x \to 0} \frac{1 - \cos x}{x} = 0$$

$$\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$$

$$\lim_{x \to 0} \frac{\tan x}{x} = 1$$

### Límites Exponenciales y Logarítmicos

$$\lim_{x \to 0} \frac{e^x - 1}{x} = 1$$

$$\lim_{x \to 0} \frac{\ln(1 + x)}{x} = 1$$

$$\lim_{x \to 0} \frac{a^x - 1}{x} = \ln a$$

$$\lim_{x \to 0} (1 + x)^{1/x} = e$$

$$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e$$

$$\lim_{x \to 0} \frac{(1+x)^n - 1}{x} = n$$

## Límites al Infinito

### Funciones Racionales

Si $P(x) = a_n x^n + \ldots$ y $Q(x) = b_m x^m + \ldots$:

$$\lim_{x \to \infty} \frac{P(x)}{Q(x)} = \begin{cases} 0 & \text{si } n < m \\ \frac{a_n}{b_m} & \text{si } n = m \\ \pm\infty & \text{si } n > m \end{cases}$$

### Límites Exponenciales

$$\lim_{x \to \infty} e^x = \infty, \quad \lim_{x \to -\infty} e^x = 0$$

$$\lim_{x \to \infty} e^{-x} = 0, \quad \lim_{x \to -\infty} e^{-x} = \infty$$

## Regla de L'Hôpital

Si $\lim_{x \to a} f(x) = \lim_{x \to a} g(x) = 0$ o $\pm\infty$, entonces:

$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

siempre que el límite del lado derecho exista.

## Teorema del Sándwich (Squeeze)

Si $g(x) \leq f(x) \leq h(x)$ cerca de $a$ y:

$$\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L$$

entonces:

$$\lim_{x \to a} f(x) = L$$

## Continuidad

Una función $f$ es **continua** en $x = a$ si:

1. $f(a)$ está definida
2. $\lim_{x \to a} f(x)$ existe
3. $\lim_{x \to a} f(x) = f(a)$

---

> **Tip**: Siempre intenta sustitución directa primero. Si obtienes una forma indeterminada, aplica técnicas algebraicas o L'Hôpital.
