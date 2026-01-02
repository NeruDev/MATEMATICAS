<!--
::METADATA::
type: problem_set
topic_id: cd-01-limites
file_id: CD-01-Problemas
status: stable
audience: student
problem_count: 57
difficulty_distribution: {basico: 18, intermedio: 24, avanzado: 12, experto: 3}
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Problemas de Límites

> **Instrucciones:** Evalúa cada [límite](../../..](../../../glossary.md)#limite). Indica si no existe y por qué. Las soluciones se encuentran en `solutions/prob-XX/`.

---

## 1.1 Concepto de Límite

### [Prob-01] Límite de función definida por partes ⭐
Usa la gráfica de $f(x)$ para estimar:
Si $f(x) = \begin{cases} x+1 & x < 2 \\ 5 & x = 2 \\ 4-x & x > 2 \end{cases}$, evalúa $\lim_{x \to 2} f(x)$.

> 📁 Solución: `solutions/prob-01/`

### [Prob-02] Límite por sustitución directa ⭐
Evalúa $\lim_{x \to 3} (2x + 5)$ usando la definición intuitiva.

> 📁 Solución: `solutions/prob-02/`

### [Prob-03] Demostración épsilon-delta ⭐⭐
Usando la definición épsilon-delta, demuestra que $\lim_{x \to 4} (3x - 7) = 5$.

> 📁 Solución: `solutions/prob-03/`

### [Prob-04] Demostración formal con función cuadrática ⭐⭐⭐
Demuestra que $\lim_{x \to 2} x^2 = 4$ usando la definición formal.

> 📁 Solución: `solutions/prob-04/`

---

## 1.2 Límites Laterales

### [Prob-05] Límites laterales con valor absoluto ⭐
Evalúa los [límites](../../..](../../../glossary.md)#limites) laterales: $\lim_{x \to 0^+} \frac{\lvert x \rvert}{x}$ y $\lim_{x \to 0^-} \frac{\lvert x \rvert}{x}$

> 📁 Solución: `solutions/prob-05/`

### [Prob-06] Límites laterales en función por partes ⭐
Para $g(x) = \begin{cases} x^2 & x \leq 1 \\ 2x-1 & x > 1 \end{cases}$, evalúa $\lim_{x \to 1^-} g(x)$ y $\lim_{x \to 1^+} g(x)$.

> 📁 Solución: `solutions/prob-06/`

### [Prob-07] Existencia de límite bilateral ⭐⭐
¿Existe $\lim_{x \to 3} f(x)$ si $f(x) = \begin{cases} x+2 & x < 3 \\ 8-x & x \geq 3 \end{cases}$?

> 📁 Solución: `solutions/prob-07/`

### [Prob-08] Límites laterales con valor absoluto en denominador ⭐⭐
Evalúa $\lim_{x \to 2} \frac{x^2 - 4}{\lvert x - 2 \rvert}$

> 📁 Solución: `solutions/prob-08/`

### [Prob-09] Función piso y límites laterales ⭐⭐⭐
Para $f(x) = \lfloor x \rfloor$ ([función](../../..](../../../glossary.md)#funcion) piso), evalúa $\lim_{x \to 3^-} f(x)$ y $\lim_{x \to 3^+} f(x)$.

> 📁 Solución: `solutions/prob-09/`

---

## 1.3 Propiedades de los Límites

### [Prob-10] Combinación lineal de límites ⭐
Si $\lim_{x \to 4} f(x) = 3$ y $\lim_{x \to 4} g(x) = -2$, calcula $\lim_{x \to 4} [5f(x) - 2g(x)]$.

> 📁 Solución: `solutions/prob-10/`

### [Prob-11] Límite de composición con raíz ⭐
Evalúa $\lim_{x \to 2} \sqrt{x^2 + 5}$

> 📁 Solución: `solutions/prob-11/`

### [Prob-12] Producto con límite cero ⭐⭐
Si $\lim_{x \to a} f(x) = 4$ y $\lim_{x \to a} g(x) = 0$, ¿qué se puede concluir sobre $\lim_{x \to a} f(x) \cdot g(x)$?

> 📁 Solución: `solutions/prob-12/`

### [Prob-13] Teorema del emparedado ⭐⭐⭐
Usa el teorema del emparedado para evaluar $\lim_{x \to 0} x^2 \cos\left(\frac{1}{x}\right)$.

> 📁 Solución: `solutions/prob-13/`

---

## 1.4 Técnicas de Evaluación

### [Prob-14] Factorización de diferencia de cuadrados ⭐
$\lim_{x \to 5} \frac{x^2 - 25}{x - 5}$

> 📁 Solución: `solutions/prob-14/`

### [Prob-15] Factorización de trinomio cuadrado ⭐
$\lim_{x \to -2} \frac{x^2 + 5x + 6}{x + 2}$

> 📁 Solución: `solutions/prob-15/`

### [Prob-16] Factorización doble ⭐
$\lim_{x \to 3} \frac{x^2 - 9}{x^2 - 5x + 6}$

> 📁 Solución: `solutions/prob-16/`

### [Prob-17] Factorización de diferencia de cubos ⭐⭐
$\lim_{x \to 1} \frac{x^3 - 1}{x - 1}$

> 📁 Solución: `solutions/prob-17/`

### [Prob-18] Racionalización de numerador ⭐⭐
$\lim_{x \to 4} \frac{\sqrt{x} - 2}{x - 4}$

> 📁 Solución: `solutions/prob-18/`

### [Prob-19] Racionalización básica ⭐⭐
$\lim_{x \to 0} \frac{\sqrt{1+x} - 1}{x}$

> 📁 Solución: `solutions/prob-19/`

### [Prob-20] Racionalización de denominador ⭐⭐
$\lim_{x \to 9} \frac{3 - \sqrt{x}}{9 - x}$

> 📁 Solución: `solutions/prob-20/`

### [Prob-21] Racionalización doble ⭐⭐⭐
$\lim_{x \to 0} \frac{\sqrt{1+x} - \sqrt{1-x}}{x}$

> 📁 Solución: `solutions/prob-21/`

### [Prob-22] Definición de derivada (cubo) ⭐⭐⭐
$\lim_{h \to 0} \frac{(2+h)^3 - 8}{h}$

> 📁 Solución: `solutions/prob-22/`

### [Prob-23] Límite con raíz cúbica ⭐⭐⭐
$\lim_{x \to 1} \frac{x^{1/3} - 1}{x - 1}$

> 📁 Solución: `solutions/prob-23/`

---

## 1.5 Límites Trigonométricos

### [Prob-24] Límite seno fundamental ⭐
$\lim_{x \to 0} \frac{\sin 5x}{x}$

> 📁 Solución: `solutions/prob-24/`

### [Prob-25] Límite seno con coeficiente ⭐
$\lim_{x \to 0} \frac{\sin x}{3x}$

> 📁 Solución: `solutions/prob-25/`

### [Prob-26] Cociente de senos ⭐⭐
$\lim_{x \to 0} \frac{\sin 3x}{\sin 5x}$

> 📁 Solución: `solutions/prob-26/`

### [Prob-27] Límite de tangente ⭐⭐
$\lim_{x \to 0} \frac{\tan x}{x}$

> 📁 Solución: `solutions/prob-27/`

### [Prob-28] Límite 1-cos x ⭐⭐
$\lim_{x \to 0} \frac{1 - \cos x}{x^2}$

> 📁 Solución: `solutions/prob-28/`

### [Prob-29] Cuadrado de seno ⭐⭐
$\lim_{x \to 0} \frac{\sin^2 x}{x^2}$

> 📁 Solución: `solutions/prob-29/`

### [Prob-30] Aproximación de tercer orden ⭐⭐⭐
$\lim_{x \to 0} \frac{x - \sin x}{x^3}$

> 📁 Solución: `solutions/prob-30/`

### [Prob-31] Tangente menos seno ⭐⭐⭐
$\lim_{x \to 0} \frac{\tan x - \sin x}{x^3}$

> 📁 Solución: `solutions/prob-31/`

### [Prob-32] Límite trigonométrico compuesto ⭐⭐⭐
$\lim_{\theta \to 0} \frac{\sin 3\theta}{\theta \cos 2\theta}$

> 📁 Solución: `solutions/prob-32/`

### [Prob-33] Límite en π/4 ⭐⭐⭐⭐
$\lim_{x \to \pi/4} \frac{\sin x - \cos x}{1 - \tan x}$

> 📁 Solución: `solutions/prob-33/`

---

## 1.6 Límites al Infinito

### [Prob-34] Cociente de polinomios grado igual ⭐
$\lim_{x \to \infty} \frac{3x + 2}{x - 1}$

> 📁 Solución: `solutions/prob-34/`

### [Prob-35] Cociente de polinomios cuadráticos ⭐
$\lim_{x \to \infty} \frac{x^2 + 1}{2x^2 - 3}$

> 📁 Solución: `solutions/prob-35/`

### [Prob-36] Grado mayor en denominador ⭐
$\lim_{x \to \infty} \frac{5x}{x^2 + 4}$

> 📁 Solución: `solutions/prob-36/`

### [Prob-37] Grado mayor en numerador ⭐⭐
$\lim_{x \to \infty} \frac{x^3 - 2x}{3x^2 + x}$

> 📁 Solución: `solutions/prob-37/`

### [Prob-38] Límite a menos infinito ⭐⭐
$\lim_{x \to -\infty} \frac{2x^2 - x}{x^2 + 1}$

> 📁 Solución: `solutions/prob-38/`

### [Prob-39] Forma infinito - infinito ⭐⭐
$\lim_{x \to \infty} \left(\sqrt{x^2 + x} - x\right)$

> 📁 Solución: `solutions/prob-39/`

### [Prob-40] Diferencia de raíces ⭐⭐⭐
$\lim_{x \to \infty} \left(\sqrt{x^2 + 2x} - \sqrt{x^2 - 2x}\right)$

> 📁 Solución: `solutions/prob-40/`

### [Prob-41] Producto con forma indeterminada ⭐⭐⭐
$\lim_{x \to \infty} x\left(\sqrt{x^2+1} - x\right)$

> 📁 Solución: `solutions/prob-41/`

### [Prob-42] Función acotada al infinito ⭐⭐⭐
$\lim_{x \to \infty} \frac{\sin x}{x}$

> 📁 Solución: `solutions/prob-42/`

### [Prob-43] Número e ⭐⭐⭐⭐
$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x$

> 📁 Solución: `solutions/prob-43/`

---

## 1.7 Límites Infinitos

### [Prob-44] Límite infinito lateral ⭐
$\lim_{x \to 3^+} \frac{1}{x-3}$

> 📁 Solución: `solutions/prob-44/`

### [Prob-45] Límite infinito con exponente par ⭐
$\lim_{x \to 2^-} \frac{1}{(x-2)^2}$

> 📁 Solución: `solutions/prob-45/`

### [Prob-46] Límite infinito bilateral ⭐⭐
$\lim_{x \to 0} \frac{1}{x^2}$

> 📁 Solución: `solutions/prob-46/`

### [Prob-47] Cociente con factor cuadrático ⭐⭐
$\lim_{x \to 1} \frac{x^2}{(x-1)^2}$

> 📁 Solución: `solutions/prob-47/`

### [Prob-48] Asíntotas verticales ⭐⭐
Encuentra las asíntotas verticales de $f(x) = \frac{x}{x^2-4}$.

> 📁 Solución: `solutions/prob-48/`

### [Prob-49] Análisis completo de asíntotas ⭐⭐⭐
Encuentra todas las asíntotas de $f(x) = \frac{x^2 - 1}{x^2 - 4}$.

> 📁 Solución: `solutions/prob-49/`

### [Prob-50] Forma 0·∞ ⭐⭐⭐
$\lim_{x \to 0^+} x \ln x$

> 📁 Solución: `solutions/prob-50/`

---

## 1.8 Continuidad

### [Prob-51] Discontinuidad evitable ⭐
¿Es $f(x) = \frac{x^2-1}{x-1}$ continua en $x = 1$? Si no, ¿qué tipo de discontinuidad tiene?

> 📁 Solución: `solutions/prob-51/`

### [Prob-52] Continuidad con parámetro ⭐
Encuentra el valor de $k$ para que $f(x) = \begin{cases} x^2 & x \leq 2 \\ kx & x > 2 \end{cases}$ sea continua.

> 📁 Solución: `solutions/prob-52/`

### [Prob-53] Puntos de discontinuidad ⭐⭐
Determina los puntos de discontinuidad de $f(x) = \frac{1}{x^2 - 5x + 6}$.

> 📁 Solución: `solutions/prob-53/`

### [Prob-54] Extensión continua con seno ⭐⭐
¿Es continua $f(x) = \begin{cases} \frac{\sin x}{x} & x \neq 0 \\ 1 & x = 0 \end{cases}$?

> 📁 Solución: `solutions/prob-54/`

### [Prob-55] Continuidad con dos parámetros ⭐⭐⭐
Encuentra $a$ y $b$ para que $f(x) = \begin{cases} ax+b & x < 1 \\ 3 & x = 1 \\ x^2 + 1 & x > 1 \end{cases}$ sea continua en todo $\mathbb{R}$.

> 📁 Solución: `solutions/prob-55/`

### [Prob-56] Clasificación de discontinuidades ⭐⭐⭐
Clasifica todas las discontinuidades de $f(x) = \frac{\lvert x-2 \rvert}{x-2}$.

> 📁 Solución: `solutions/prob-56/`

---

## 1.9 Teorema del Valor Intermedio

### [Prob-57] Existencia de raíz (TVI) ⭐⭐
Demuestra que $x^3 - x - 1 = 0$ tiene al menos una solución en $(1, 2)$.

> 📁 Solución: `solutions/prob-57/`
