<!--
::METADATA::
type: solution
topic_id: fun-04-geometria
file_id: FUN-04-Prob-77-Solucion
status: stable
audience: student
problem_ref: "[Prob-77]"
methods: ["relaciones-metricas", "media-geometrica", "triangulo-rectangulo", "teorema-altura"]
-->

# Solución [Prob-77]: Relaciones métricas en el triángulo rectángulo

> **Problema:** En el triángulo rectángulo ABC (recto en C), la altura CH a la hipotenusa divide a esta en AH = 4 cm y HB = 9 cm. Calcula CH, AC y BC.

## Diagrama del problema

```
                    C
                   /|\
                  / | \
                 /  |  \
                /   |h  \
               /    |    \
              /     |     \
             /      |      \
            /       |       \
           A ———————H——————— B
              m=4      n=9

    Ángulo recto en C
    CH = h (altura a la hipotenusa)
    AH = m = 4 cm (proyección de AC)
    HB = n = 9 cm (proyección de BC)
```

---

## Datos del problema

- $\angle ACB = 90°$ (ángulo recto en $C$)
- $AH = m = 4$ cm (proyección del cateto $AC$ sobre la hipotenusa)
- $HB = n = 9$ cm (proyección del cateto $BC$ sobre la hipotenusa)
- $AB = c = m + n = 4 + 9 = 13$ cm (hipotenusa)

**Incógnitas:**
- $CH = h$ (altura)
- $AC = b$ (cateto)
- $BC = a$ (cateto)

---

## Relaciones métricas fundamentales

En un triángulo rectángulo, cuando se [traza](../../../../glossary.md#traza) la altura al lado de la hipotenusa, se cumplen las siguientes relaciones:

### Teorema de la altura (Media geométrica)

$$h^2 = m \cdot n$$

> La altura es la **media geométrica** de las proyecciones de los catetos sobre la hipotenusa.

### Teorema del cateto (Relación de Euclides)

$$b^2 = m \cdot c$$
$$a^2 = n \cdot c$$

> Cada cateto es la **media geométrica** entre su proyección y la hipotenusa completa.

---

## Resolución paso a paso

### Paso 1: Calcular la altura CH

Aplicamos el teorema de la altura:

$$h^2 = m \cdot n$$

$$h^2 = 4 \times 9 = 36$$

$$h = \sqrt{36} = 6 \text{ cm}$$

$$\boxed{CH = 6 \text{ cm}}$$

### Paso 2: Calcular el cateto AC

Aplicamos el teorema del cateto para $AC$:

$$b^2 = m \cdot c$$

donde:
- $m = 4$ (proyección de $AC$)
- $c = 13$ (hipotenusa)

$$b^2 = 4 \times 13 = 52$$

$$b = \sqrt{52} = \sqrt{4 \times 13} = 2\sqrt{13} \text{ cm}$$

$$\boxed{AC = 2\sqrt{13} \text{ cm} \approx 7.21 \text{ cm}}$$

### Paso 3: Calcular el cateto BC

Aplicamos el teorema del cateto para $BC$:

$$a^2 = n \cdot c$$

donde:
- $n = 9$ (proyección de $BC$)
- $c = 13$ (hipotenusa)

$$a^2 = 9 \times 13 = 117$$

$$a = \sqrt{117} = \sqrt{9 \times 13} = 3\sqrt{13} \text{ cm}$$

$$\boxed{BC = 3\sqrt{13} \text{ cm} \approx 10.82 \text{ cm}}$$

---

## Resumen de resultados

| Elemento | Valor exacto | Valor aproximado |
|:---------|:-------------|:-----------------|
| $CH$ (altura) | $6$ cm | $6$ cm |
| $AC$ (cateto) | $2\sqrt{13}$ cm | $7.21$ cm |
| $BC$ (cateto) | $3\sqrt{13}$ cm | $10.82$ cm |
| $AB$ (hipotenusa) | $13$ cm | $13$ cm |

---

## Verificación

### Verificación 1: Teorema de Pitágoras

$$AC^2 + BC^2 = AB^2$$

$$(2\sqrt{13})^2 + (3\sqrt{13})^2 = 13^2$$

$$4 \times 13 + 9 \times 13 = 169$$

$$52 + 117 = 169$$

$$169 = 169 \quad \checkmark$$

### Verificación 2: Área del triángulo (dos métodos)

**Método 1:** Usando los catetos como [base](../../../../glossary.md#base) y altura

$$A = \frac{1}{2} \times AC \times BC = \frac{1}{2} \times 2\sqrt{13} \times 3\sqrt{13}$$

$$A = \frac{1}{2} \times 6 \times 13 = 39 \text{ cm}^2$$

**Método 2:** Usando la hipotenusa y la altura $h$

$$A = \frac{1}{2} \times AB \times h = \frac{1}{2} \times 13 \times 6 = 39 \text{ cm}^2$$

$$39 = 39 \quad \checkmark$$

### Verificación 3: Triángulos semejantes

Los triángulos $\triangle ACH$, $\triangle CBH$ y $\triangle ABC$ son semejantes.

**Para $\triangle ACH \sim \triangle ABC$:**

$$\frac{AC}{AB} = \frac{AH}{AC}$$

$$\frac{2\sqrt{13}}{13} = \frac{4}{2\sqrt{13}}$$

$$\frac{2\sqrt{13}}{13} = \frac{2}{\sqrt{13}} = \frac{2\sqrt{13}}{13} \quad \checkmark$$

**Para $\triangle CBH \sim \triangle ABC$:**

$$\frac{BC}{AB} = \frac{BH}{BC}$$

$$\frac{3\sqrt{13}}{13} = \frac{9}{3\sqrt{13}}$$

$$\frac{3\sqrt{13}}{13} = \frac{3}{\sqrt{13}} = \frac{3\sqrt{13}}{13} \quad \checkmark$$

---

## Justificación de las relaciones métricas

### ¿Por qué $h^2 = m \cdot n$?

Los triángulos $\triangle ACH$ y $\triangle CHB$ son semejantes (criterio AA).

$$\triangle ACH \sim \triangle CHB$$

Por semejanza:

$$\frac{CH}{HB} = \frac{AH}{CH}$$

$$\frac{h}{n} = \frac{m}{h}$$

$$h^2 = m \cdot n$$

### ¿Por qué $b^2 = m \cdot c$?

Los triángulos $\triangle ACH$ y $\triangle ABC$ son semejantes.

$$\triangle ACH \sim \triangle ABC$$

Por semejanza:

$$\frac{AC}{AB} = \frac{AH}{AC}$$

$$\frac{b}{c} = \frac{m}{b}$$

$$b^2 = m \cdot c$$

---

## Respuesta Final

$$\boxed{CH = 6 \text{ cm}, \quad AC = 2\sqrt{13} \text{ cm}, \quad BC = 3\sqrt{13} \text{ cm}}$$

---

## Observaciones adicionales

### Razón entre los catetos

$$\frac{BC}{AC} = \frac{3\sqrt{13}}{2\sqrt{13}} = \frac{3}{2}$$

Esta razón es igual a la razón de las proyecciones:

$$\sqrt{\frac{n}{m}} = \sqrt{\frac{9}{4}} = \frac{3}{2} \quad \checkmark$$

### Relación con la media geométrica

- $h = 6$ es la media geométrica de $4$ y $9$: $\sqrt{4 \times 9} = 6$
- $AC = 2\sqrt{13}$ es la media geométrica de $4$ y $13$: $\sqrt{4 \times 13} = 2\sqrt{13}$
- $BC = 3\sqrt{13}$ es la media geométrica de $9$ y $13$: $\sqrt{9 \times 13} = 3\sqrt{13}$

### Tabla resumen de relaciones métricas

| Relación | Fórmula | Aplicación en este problema |
|:---------|:--------|:---------------------------|
| Teorema de la altura | $h^2 = m \cdot n$ | $h^2 = 4 \times 9 = 36$ |
| Teorema del cateto (AC) | $b^2 = m \cdot c$ | $b^2 = 4 \times 13 = 52$ |
| Teorema del cateto (BC) | $a^2 = n \cdot c$ | $a^2 = 9 \times 13 = 117$ |
| Pitágoras | $a^2 + b^2 = c^2$ | $52 + 117 = 169$ ✓ |
