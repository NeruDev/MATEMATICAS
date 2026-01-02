<!--
::METADATA::
type: solution
topic_id: fun-02-aritmetica
file_id: FUN-02-Prob-50-Solucion
status: stable
audience: student
problem_ref: "[Prob-50]"
methods: ["[sustitución](../../../../glossary.md#sustitución)", "ecuación cuadrática", "análisis algebraico"]
-->

# Solución [Prob-50]: Ecuación suma de recíprocos

> **Problema:** Si $\frac{a}{b} + \frac{b}{a} = \frac{25}{12}$, y $a, b > 0$, encuentra $\frac{a}{b}$.

---

## Método 1: Sustitución

### Paso 1: Introducir una variable auxiliar

Sea $x = \frac{a}{b}$, donde $x > 0$ (ya que $a, b > 0$).

Entonces $\frac{b}{a} = \frac{1}{x}$.

### Paso 2: Reescribir la ecuación

La ecuación original se convierte en:

$$x + \frac{1}{x} = \frac{25}{12}$$

### Paso 3: Eliminar el denominador

Multiplicamos ambos lados por $x$:

$$x \cdot x + x \cdot \frac{1}{x} = \frac{25}{12} \cdot x$$

$$x^2 + 1 = \frac{25x}{12}$$

### Paso 4: Formar ecuación cuadrática

Multiplicamos por 12 para eliminar fracciones:

$$12x^2 + 12 = 25x$$

Reordenamos:

$$12x^2 - 25x + 12 = 0$$

### Paso 5: Resolver la ecuación cuadrática

Usamos la fórmula cuadrática con $a = 12$, $b = -25$, $c = 12$:

$$x = \frac{-(-25) \pm \sqrt{(-25)^2 - 4(12)(12)}}{2(12)}$$

$$x = \frac{25 \pm \sqrt{625 - 576}}{24}$$

$$x = \frac{25 \pm \sqrt{49}}{24}$$

$$x = \frac{25 \pm 7}{24}$$

### Paso 6: Obtener las dos soluciones

**Solución 1:**
$$x_1 = \frac{25 + 7}{24} = \frac{32}{24} = \frac{4}{3}$$

**Solución 2:**
$$x_2 = \frac{25 - 7}{24} = \frac{18}{24} = \frac{3}{4}$$

### Verificación

**Para $x = \frac{4}{3}$:**
$$\frac{4}{3} + \frac{3}{4} = \frac{16}{12} + \frac{9}{12} = \frac{25}{12} \quad \checkmark$$

**Para $x = \frac{3}{4}$:**
$$\frac{3}{4} + \frac{4}{3} = \frac{9}{12} + \frac{16}{12} = \frac{25}{12} \quad \checkmark$$

---

## Método 2: Factorización Directa

### Paso 1: Plantear la ecuación cuadrática

De la ecuación $x + \frac{1}{x} = \frac{25}{12}$, obtenemos:

$$12x^2 - 25x + 12 = 0$$

### Paso 2: Factorizar el trinomio

Buscamos dos números que:
- Multipliquen a $12 \times 12 = 144$
- Sumen a $-25$

Los números son $-16$ y $-9$ (porque $(-16)(-9) = 144$ y $-16 + (-9) = -25$).

### Paso 3: Reescribir el término medio

$$12x^2 - 16x - 9x + 12 = 0$$

### Paso 4: Factorizar por agrupación

$$4x(3x - 4) - 3(3x - 4) = 0$$

$$(4x - 3)(3x - 4) = 0$$

### Paso 5: Resolver cada factor

**Factor 1:** $4x - 3 = 0$
$$x = \frac{3}{4}$$

**Factor 2:** $3x - 4 = 0$
$$x = \frac{4}{3}$$

---

## Método 3: Análisis Algebraico

### Paso 1: Simplificar el lado izquierdo

$$\frac{a}{b} + \frac{b}{a} = \frac{a^2 + b^2}{ab}$$

### Paso 2: Igualar

$$\frac{a^2 + b^2}{ab} = \frac{25}{12}$$

### Paso 3: Establecer proporción

Esto sugiere que podemos buscar valores donde:
- $a^2 + b^2 = 25k$ para algún $k$
- $ab = 12k$

### Paso 4: Probar valores simples

**Intento con $a = 4, b = 3$:**
- $a^2 + b^2 = 16 + 9 = 25$ ✓
- $ab = 12$ ✓

$$\frac{a^2 + b^2}{ab} = \frac{25}{12} \quad \checkmark$$

Entonces $\frac{a}{b} = \frac{4}{3}$

**Intento con $a = 3, b = 4$:**
- $a^2 + b^2 = 9 + 16 = 25$ ✓
- $ab = 12$ ✓

Entonces $\frac{a}{b} = \frac{3}{4}$

---

## Observación Importante

Notemos que las dos soluciones son **recíprocas** entre sí:

$$\frac{4}{3} \times \frac{3}{4} = 1$$

Esto tiene sentido porque si $x = \frac{a}{b}$ es solución de $x + \frac{1}{x} = k$, entonces $\frac{1}{x} = \frac{b}{a}$ también es solución (la ecuación es simétrica en $x$ y $\frac{1}{x}$).

---

## Interpretación Geométrica

Si pensamos en $a$ y $b$ como lados de un rectángulo:
- Con $(a, b) = (4, 3)$: rectángulo 4×3
- Con $(a, b) = (3, 4)$: rectángulo 3×4 (el mismo rotado)

Ambos rectángulos tienen:
- Suma de cuadrados de lados: $a^2 + b^2 = 25$
- Área: $ab = 12$

---

## Respuesta Final

$$\boxed{\frac{a}{b} = \frac{4}{3} \quad \text{o} \quad \frac{a}{b} = \frac{3}{4}}$$

Ambas soluciones son válidas. Si se pide la solución mayor que 1, es $\frac{4}{3}$.
Si se pide la solución [menor](../../../../glossary.md#menor) que 1, es $\frac{3}{4}$.

---

> 📚 Volver a: [FUN-02-Problemas](../../problems/FUN-02-Problemas.md)
