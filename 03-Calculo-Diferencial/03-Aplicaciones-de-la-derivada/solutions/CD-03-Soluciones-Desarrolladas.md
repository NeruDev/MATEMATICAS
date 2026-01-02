<!--
HUMANO:
Soluciones de aplicaciones de la [derivada](../../../glossary.md#derivada).

IA:
Cada solución incluye: contexto → desarrollo → verificación.

---
content_type: solutions
expected_output:
  default: markdown
audience: self-study
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Soluciones de Aplicaciones de la Derivada

---

## 3.1 Recta Tangente

### Solución 3.1.1
**Contexto:** [Tangente](../../../glossary.md#tangente): $y - f(a) = f'(a)(x - a)$

**Desarrollo:**
$f(x) = x^3 - 2x$, $f(1) = 1 - 2 = -1$
$f'(x) = 3x^2 - 2$, $f'(1) = 3 - 2 = 1$

[Tangente](../../../glossary.md#tangente): $y - (-1) = 1(x - 1)$ → $y = x - 2$

---

## 3.2 Razones Relacionadas

### Solución 3.2.2
**Contexto:** Relación pitagórica entre posición de [base](../../../glossary.md#base), altura y longitud.

**Desarrollo:**
$x^2 + y^2 = 25$ (escalera de 5 m)

Derivando: $2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0$

Cuando $x = 3$: $y = \sqrt{25 - 9} = 4$

$2(3)(0.5) + 2(4)\frac{dy}{dt} = 0$

$\frac{dy}{dt} = -\frac{3}{8}$ m/s

**Respuesta:** La parte superior desciende a $\frac{3}{8}$ m/s.

---

## 3.3 Valores Extremos

### Solución 3.3.1
**Contexto:** Método del intervalo cerrado.

**Desarrollo:**
$f(x) = x^2 - 4x + 3$, $f'(x) = 2x - 4 = 0$ → $x = 2$

Evaluando:
- $f(0) = 3$
- $f(2) = 4 - 8 + 3 = -1$
- $f(4) = 16 - 16 + 3 = 3$

**Respuesta:** Máximo absoluto: $3$ en $x = 0$ y $x = 4$. Mínimo absoluto: $-1$ en $x = 2$.

---

## 3.6 Optimización

### Solución 3.6.1
**Contexto:** Un lado junto al río no necesita cerca.

**Desarrollo:**
Sea $x$ = lado paralelo al río, $y$ = lados perpendiculares.
Restricción: $x + 2y = 100$ → $x = 100 - 2y$
Área: $A = xy = (100 - 2y)y = 100y - 2y^2$

$A' = 100 - 4y = 0$ → $y = 25$
$x = 100 - 50 = 50$

$A'' = -4 < 0$ → máximo

**Respuesta:** $50 \times 25$ m, área máxima = $1250$ m²

### Solución 3.6.3
**Contexto:** Caja de lámina 12×12 cm cortando cuadrados de lado $x$.

**Desarrollo:**
[Base](../../../glossary.md#base): $(12 - 2x) \times (12 - 2x)$, Altura: $x$
Volumen: $V = x(12-2x)^2 = x(144 - 48x + 4x^2) = 4x^3 - 48x^2 + 144x$

$V' = 12x^2 - 96x + 144 = 12(x^2 - 8x + 12) = 12(x-2)(x-6) = 0$

$x = 2$ o $x = 6$ (no válido, sería toda la lámina)

$V''(2) = 24(2) - 96 = -48 < 0$ → máximo

**Respuesta:** Cortar cuadrados de $2$ cm. Volumen máximo: $V(2) = 128$ cm³

### Solución 3.6.6
**Contexto:** Cilindro con $V = \pi r^2 h = 1000$ cm³.

**Desarrollo:**
De la restricción: $h = \frac{1000}{\pi r^2}$

Área: $A = 2\pi r^2 + 2\pi rh = 2\pi r^2 + 2\pi r \cdot \frac{1000}{\pi r^2} = 2\pi r^2 + \frac{2000}{r}$

$A' = 4\pi r - \frac{2000}{r^2} = 0$

$r^3 = \frac{500}{\pi}$ → $r = \sqrt[3]{\frac{500}{\pi}} \approx 5.42$ cm

$h = \frac{1000}{\pi r^2} = 2r \approx 10.84$ cm

**Respuesta:** Radio ≈ 5.42 cm, altura ≈ 10.84 cm (altura = diámetro)

---

## 3.7 Aproximaciones

### Solución 3.7.1
**Contexto:** $f(x) = \sqrt{x}$, aproximar cerca de $a = 9$.

**Desarrollo:**
$f(9) = 3$, $f'(x) = \frac{1}{2\sqrt{x}}$, $f'(9) = \frac{1}{6}$

$\sqrt{9.1} \approx 3 + \frac{1}{6}(0.1) = 3 + 0.01\overline{6} \approx 3.0167$

**Verificación:** Valor real ≈ 3.0166...

---

## 3.9 Newton-Raphson

### Solución 3.9.1
**Contexto:** $f(x) = x^2 - 5$, $f'(x) = 2x$

**Desarrollo:**
$x_{n+1} = x_n - \frac{x_n^2 - 5}{2x_n}$

$x_0 = 2$
$x_1 = 2 - \frac{-1}{4} = 2.25$
$x_2 = 2.25 - \frac{0.0625}{4.5} = 2.2361...$

**Respuesta:** $\sqrt{5} \approx 2.236$

---

## Problemas de Síntesis

### Solución 3.S.4
**Contexto:** Usar análisis de [función](../../../glossary.md#funcion) $g(x) = e^x - 1 - x$.

**Desarrollo:**
$g(x) = e^x - 1 - x$
$g'(x) = e^x - 1$
$g'(x) = 0$ cuando $x = 0$

$g''(x) = e^x > 0$ siempre (cóncava arriba)

$g(0) = 1 - 1 - 0 = 0$ → mínimo global

Como $g(x) \geq g(0) = 0$ para todo $x$:
$$e^x - 1 - x \geq 0$$
$$e^x \geq 1 + x$$ ∎
