<!--
::METADATA::
type: cheatsheet
topic_id: fun-03-algebra
file_id: FUN-03-Resumen-Formulas
status: stable
audience: student
requires: [fun-03-algebra-intro]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

---

# Álgebra — Resumen de Fórmulas

## Productos Notables

| Nombre | Fórmula |
|--------|---------|
| Binomio al cuadrado (+) | $(a + b)^2 = a^2 + 2ab + b^2$ |
| Binomio al cuadrado (−) | $(a - b)^2 = a^2 - 2ab + b^2$ |
| Diferencia de cuadrados | $(a + b)(a - b) = a^2 - b^2$ |
| Binomio al cubo (+) | $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$ |
| Binomio al cubo (−) | $(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$ |
| Suma de cubos | $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$ |
| Diferencia de cubos | $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$ |

---

## Factorización

| Tipo | Patrón | Ejemplo |
|------|--------|---------|
| Factor común | $ax + ay = a(x + y)$ | $6x^2 - 9x = 3x(2x - 3)$ |
| Agrupación | $xy + xz + wy + wz = x(y+z) + w(y+z)$ | $(y+z)(x+w)$ |
| TCP (+) | $a^2 + 2ab + b^2 = (a + b)^2$ | $x^2 + 6x + 9 = (x+3)^2$ |
| TCP (−) | $a^2 - 2ab + b^2 = (a - b)^2$ | $x^2 - 6x + 9 = (x-3)^2$ |
| Diferencia de cuadrados | $a^2 - b^2 = (a+b)(a-b)$ | $4x^2 - 25 = (2x+5)(2x-5)$ |
| Trinomio $x^2 + bx + c$ | Buscar $m + n = b$, $mn = c$ | $x^2 + 5x + 6 = (x+2)(x+3)$ |
| Trinomio $ax^2 + bx + c$ | Método AC | $6x^2 + 7x - 3 = (2x+3)(3x-1)$ |

---

## Ecuaciones Cuadráticas

### Forma general
$$ax^2 + bx + c = 0, \quad a \neq 0$$

### Fórmula general (cuadrática)
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

### Discriminante
$$\Delta = b^2 - 4ac$$

| Discriminante | Naturaleza de las raíces |
|---------------|--------------------------|
| $\Delta > 0$ | Dos raíces reales distintas |
| $\Delta = 0$ | Una raíz real doble |
| $\Delta < 0$ | Dos raíces complejas conjugadas |

### Relaciones de Vieta
$$r_1 + r_2 = -\frac{b}{a} \qquad r_1 \cdot r_2 = \frac{c}{a}$$

---

## Sistemas de Ecuaciones 2×2

### Regla de Cramer
Para $\begin{cases} a_1x + b_1y = c_1 \\ a_2x + b_2y = c_2 \end{cases}$

$$\Delta = a_1b_2 - a_2b_1$$

$$x = \frac{c_1b_2 - c_2b_1}{\Delta} \qquad y = \frac{a_1c_2 - a_2c_1}{\Delta}$$

---

## Desigualdades

| Forma | Equivalencia |
|-------|--------------|
| $\lvert x \rvert < a$ | $-a < x < a$ |
| $\lvert x \rvert > a$ | $x < -a$ o $x > a$ |
| $\lvert x - c \rvert < a$ | $c - a < x < c + a$ |

---

## Exponentes y Radicales

| Ley | Fórmula |
|-----|---------|
| Exponente cero | $a^0 = 1$ |
| Exponente negativo | $a^{-n} = \frac{1}{a^n}$ |
| Exponente fraccionario | $a^{m/n} = \sqrt[n]{a^m}$ |
| Producto | $a^m \cdot a^n = a^{m+n}$ |
| Cociente | $\frac{a^m}{a^n} = a^{m-n}$ |
| Potencia de potencia | $(a^m)^n = a^{mn}$ |
