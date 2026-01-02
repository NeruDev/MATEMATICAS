<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: FUN-03-Prob-67-Solucion
status: stable
audience: student
problem_ref: "[Prob-67]"
methods: ["formula-cuadratica", "numeros-complejos", "discriminante"]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución [Prob-67]: Raíces complejas de una ecuación cuadrática

> **Problema:** Resuelve: $x^2 + 4x + 5 = 0$

## Conceptos previos

Cuando una ecuación cuadrática $ax^2 + bx + c = 0$ tiene **discriminante negativo** ($b^2 - 4ac < 0$), no tiene soluciones reales, pero sí tiene dos soluciones complejas conjugadas.

Recordemos que $i = \sqrt{-1}$ es la **unidad imaginaria**, y $i^2 = -1$.

---

## Método 1: Fórmula cuadrática

### Paso 1: Identificar los coeficientes

Para $x^2 + 4x + 5 = 0$:

- $a = 1$
- $b = 4$
- $c = 5$

### Paso 2: Calcular el discriminante

$$\Delta = b^2 - 4ac$$

$$\Delta = (4)^2 - 4(1)(5)$$

$$\Delta = 16 - 20$$

$$\Delta = -4$$

Como $\Delta < 0$, **no hay soluciones reales**.

### Paso 3: Aplicar la fórmula cuadrática

$$x = \frac{-b \pm \sqrt{\Delta}}{2a}$$

$$x = \frac{-4 \pm \sqrt{-4}}{2(1)}$$

### Paso 4: Simplificar $\sqrt{-4}$

$$\sqrt{-4} = \sqrt{4 \cdot (-1)} = \sqrt{4} \cdot \sqrt{-1} = 2i$$

### Paso 5: Obtener las soluciones

$$x = \frac{-4 \pm 2i}{2}$$

Separamos en sus dos soluciones:

$$x_1 = \frac{-4 + 2i}{2} = \frac{-4}{2} + \frac{2i}{2} = -2 + i$$

$$x_2 = \frac{-4 - 2i}{2} = \frac{-4}{2} - \frac{2i}{2} = -2 - i$$

---

## Método 2: Completar el cuadrado

### Paso 1: Aislar los términos con $x$

$$x^2 + 4x + 5 = 0$$

$$x^2 + 4x = -5$$

### Paso 2: Completar el cuadrado

Para completar el cuadrado, añadimos $\left(\frac{b}{2}\right)^2 = \left(\frac{4}{2}\right)^2 = 4$ a ambos lados:

$$x^2 + 4x + 4 = -5 + 4$$

$$(x + 2)^2 = -1$$

### Paso 3: Aplicar la raíz cuadrada

$$x + 2 = \pm\sqrt{-1}$$

$$x + 2 = \pm i$$

### Paso 4: Despejar $x$

$$x = -2 \pm i$$

Por lo tanto:
- $x_1 = -2 + i$
- $x_2 = -2 - i$

---

## Análisis de las soluciones

### Propiedades de las raíces complejas conjugadas

Las soluciones $x_1 = -2 + i$ y $x_2 = -2 - i$ son **complejos conjugados**:

$$\overline{x_1} = x_2$$

Esto siempre ocurre cuando los coeficientes de la ecuación son reales y el discriminante es negativo.

### Forma general de un número complejo

Un número complejo tiene la forma $z = a + bi$ donde:
- $a$ es la **parte real**: $\text{Re}(z) = a$
- $b$ es la **parte imaginaria**: $\text{Im}(z) = b$

Para nuestras soluciones:

| Raíz | Parte Real | Parte Imaginaria |
|------|------------|------------------|
| $x_1 = -2 + i$ | $-2$ | $1$ |
| $x_2 = -2 - i$ | $-2$ | $-1$ |

---

## Verificación algebraica

### Verificación de $x_1 = -2 + i$

Sustituimos en $x^2 + 4x + 5$:

**Calculamos $x^2$:**

$$(-2 + i)^2 = (-2)^2 + 2(-2)(i) + (i)^2$$

$$= 4 - 4i + i^2$$

$$= 4 - 4i + (-1)$$

$$= 3 - 4i$$

**Calculamos $4x$:**

$$4(-2 + i) = -8 + 4i$$

**Sumamos todo:**

$$x^2 + 4x + 5 = (3 - 4i) + (-8 + 4i) + 5$$

$$= 3 - 4i - 8 + 4i + 5$$

$$= (3 - 8 + 5) + (-4i + 4i)$$

$$= 0 + 0i = 0 \quad \checkmark$$

### Verificación de $x_2 = -2 - i$

Por simetría (conjugados), si $x_1$ es solución, $x_2 = \overline{x_1}$ también lo es cuando los coeficientes son reales.

---

## Relación con las fórmulas de Vieta

Para $x^2 + 4x + 5 = 0$:

**Suma de las raíces:**

$$x_1 + x_2 = (-2 + i) + (-2 - i) = -4$$

Según Vieta: $x_1 + x_2 = -\frac{b}{a} = -\frac{4}{1} = -4$ ✓

**Producto de las raíces:**

$$x_1 \cdot x_2 = (-2 + i)(-2 - i)$$

Usando $(a + b)(a - b) = a^2 - b^2$:

$$= (-2)^2 - (i)^2 = 4 - (-1) = 4 + 1 = 5$$

Según Vieta: $x_1 \cdot x_2 = \frac{c}{a} = \frac{5}{1} = 5$ ✓

---

## Representación en el plano complejo

Los números complejos se representan en el **plano de Argand**:

```
        Im (eje imaginario)
          │
        1 ┼─────────────● x₁ = -2 + i
          │             │
          │             │
    ──────┼─────────────┼──────▶ Re (eje real)
         -2             │
          │             │
       -1 ┼─────────────● x₂ = -2 - i
          │
```

Las raíces conjugadas son simétricas respecto al eje real.

---

## Forma polar (opcional)

Cada raíz puede expresarse en forma polar $z = r(\cos\theta + i\sin\theta)$:

**Para $x_1 = -2 + i$:**

- Módulo: $r = |x_1| = \sqrt{(-2)^2 + 1^2} = \sqrt{4 + 1} = \sqrt{5}$
- Argumento: $\theta = \arctan\left(\frac{1}{-2}\right) + \pi = \pi - \arctan\left(\frac{1}{2}\right)$

(El $+\pi$ es porque el punto está en el segundo cuadrante)

---

## Diagrama resumen

```
              x² + 4x + 5 = 0
                    │
        Identificar: a=1, b=4, c=5
                    │
        Calcular Δ = b² - 4ac = -4
                    │
                Δ < 0
                    │
        ┌───────────┴───────────┐
        │                       │
   No hay raíces          Hay raíces
      reales               complejas
                                │
                    x = (-4 ± √(-4))/2
                                │
                    x = (-4 ± 2i)/2
                                │
                    x = -2 ± i
```

---

## Errores comunes a evitar

⚠️ **Error 1:** Escribir que "no tiene solución" cuando el discriminante es negativo.

Corrección: No tiene soluciones **reales**, pero sí tiene soluciones **complejas**.

⚠️ **Error 2:** Olvidar que $\sqrt{-4} = 2i$ (no $-2i$).

⚠️ **Error 3:** Confundir $i^2 = -1$ con $i^2 = 1$.

---

## Respuesta Final

$$\boxed{x = -2 + i \quad \text{y} \quad x = -2 - i}$$

O de forma compacta: $x = -2 \pm i$

**Conjunto solución en $\mathbb{C}$:** $\{-2 + i, -2 - i\}$

> 📚 Volver a: [FUN-03-Problemas](../../problems/FUN-03-Problemas.md)
