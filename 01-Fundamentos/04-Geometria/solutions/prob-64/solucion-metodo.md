<!--
::METADATA::
type: solution
topic_id: fun-04-geometria
file_id: FUN-04-Prob-64-Solucion
status: stable
audience: student
problem_ref: "[Prob-64]"
methods: ["formula-heron", "semiperimetro", "calculo-area"]
-->

# Solución [Prob-64]: Área de un triángulo por fórmula de Herón

> **Problema:** Un triángulo tiene lados de 13 cm, 14 cm y 15 cm. Calcula su área usando la fórmula de Herón.

## Datos del problema

- Lado $a = 13$ cm
- Lado $b = 14$ cm  
- Lado $c = 15$ cm

---

## Fórmula de Herón

El área de un triángulo con lados $a$, $b$, $c$ es:

$$A = \sqrt{s(s-a)(s-b)(s-c)}$$

donde $s$ es el **semiperímetro**:

$$s = \frac{a + b + c}{2}$$

---

## Resolución paso a paso

### Paso 1: Verificar que los lados forman un triángulo válido

Para que tres segmentos formen un triángulo, deben cumplir la **desigualdad triangular**:

$$a + b > c, \quad a + c > b, \quad b + c > a$$

**Verificación:**
- $13 + 14 = 27 > 15$ ✓
- $13 + 15 = 28 > 14$ ✓
- $14 + 15 = 29 > 13$ ✓

El triángulo es válido.

### Paso 2: Calcular el perímetro

$$P = a + b + c = 13 + 14 + 15 = 42 \text{ cm}$$

### Paso 3: Calcular el semiperímetro

$$s = \frac{P}{2} = \frac{42}{2} = 21 \text{ cm}$$

### Paso 4: Calcular cada factor $(s - \text{lado})$

$$s - a = 21 - 13 = 8$$

$$s - b = 21 - 14 = 7$$

$$s - c = 21 - 15 = 6$$

### Paso 5: Calcular el producto bajo la raíz

$$s \cdot (s-a) \cdot (s-b) \cdot (s-c) = 21 \times 8 \times 7 \times 6$$

**Cálculo paso a paso:**

$$21 \times 8 = 168$$

$$168 \times 7 = 1176$$

$$1176 \times 6 = 7056$$

### Paso 6: Calcular la raíz cuadrada

$$A = \sqrt{7056}$$

Para calcular $\sqrt{7056}$, factorizamos:

$$7056 = 2^4 \times 3^2 \times 7^2 = 16 \times 9 \times 49$$

$$\sqrt{7056} = \sqrt{16} \times \sqrt{9} \times \sqrt{49} = 4 \times 3 \times 7 = 84$$

**Verificación directa:**

$$84^2 = 7056 \quad \checkmark$$

### Paso 7: Expresar el resultado

$$A = 84 \text{ cm}^2$$

---

## Respuesta Final

$$\boxed{A = 84 \text{ cm}^2}$$

---

## Verificación por método alternativo

### Método: Fórmula base × altura

Podemos verificar encontrando la altura del triángulo.

**Usando la [base](../../../../glossary.md#base) $c = 15$ cm:**

$$A = \frac{1}{2} \times \text{[base](../../../../glossary.md#base)} \times \text{altura}$$

$$84 = \frac{1}{2} \times 15 \times h$$

$$h = \frac{84 \times 2}{15} = \frac{168}{15} = 11.2 \text{ cm}$$

**Verificación con el teorema de Pitágoras:**

Si la altura cae en el punto $H$ sobre el lado $c$, divide a este en segmentos $x$ y $(15-x)$.

Para el triángulo con lado $a = 13$:
$$13^2 = h^2 + x^2$$
$$169 = 125.44 + x^2$$
$$x^2 = 43.56$$
$$x = 6.6 \text{ cm}$$

Para el triángulo con lado $b = 14$:
$$14^2 = h^2 + (15-x)^2$$
$$196 = 125.44 + (8.4)^2$$
$$196 = 125.44 + 70.56 = 196 \quad \checkmark$$

---

## Resumen del cálculo

| Paso | Operación | Resultado |
|:----:|:----------|:----------|
| 1 | Perímetro: $13 + 14 + 15$ | $42$ cm |
| 2 | Semiperímetro: $\frac{42}{2}$ | $21$ cm |
| 3 | $s - a = 21 - 13$ | $8$ |
| 4 | $s - b = 21 - 14$ | $7$ |
| 5 | $s - c = 21 - 15$ | $6$ |
| 6 | Producto: $21 \times 8 \times 7 \times 6$ | $7056$ |
| 7 | Área: $\sqrt{7056}$ | $84$ cm² |

---

## Observaciones

### ¿Por qué funciona la fórmula de Herón?

La fórmula de Herón se deriva de la fórmula $A = \frac{1}{2}bh$ combinada con el teorema de Pitágoras. Permite calcular el área conociendo solo los tres lados, sin necesidad de conocer ángulos ni alturas.

### Triángulo 13-14-15: Un caso especial

Este triángulo (13, 14, 15) es conocido porque:
- Tiene área entera ($84$ cm²)
- Su altura respecto al lado 14 también es entera ($h = 12$ cm)
- Es un "triángulo de Herón" (área y lados enteros)

**Verificación con base 14:**

$$A = \frac{1}{2} \times 14 \times h = 84$$
$$h = \frac{168}{14} = 12 \text{ cm}$$

Con el teorema de Pitágoras:
- $13^2 = 12^2 + x^2 \Rightarrow x = 5$
- $15^2 = 12^2 + (14-x)^2 = 144 + 81 = 225$ ✓

Este triángulo puede verse como dos triángulos rectángulos notables:
- Triángulo $5$-$12$-$13$ (pitagórico)
- Triángulo $9$-$12$-$15$ (múltiplo de $3$-$4$-$5$)

---

## Fórmula de Herón: Forma alternativa

También puede escribirse como:

$$A = \frac{1}{4}\sqrt{4a^2b^2 - (a^2 + b^2 - c^2)^2}$$

Esta forma evita calcular el semiperímetro pero es más compleja computacionalmente.
