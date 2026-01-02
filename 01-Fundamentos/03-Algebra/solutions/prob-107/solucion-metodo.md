<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: FUN-03-Prob-107-Solucion
status: stable
audience: student
problem_ref: "[Prob-107]"
methods: ["ecuacion-cuadratica", "formula-general", "factorizacion", "analisis-fisico"]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución [Prob-107]: Movimiento de proyectil (ecuación cuadrática)

> **Problema:** La altura de un proyectil está dada por $h(t) = -5t^2 + 30t + 10$. ¿Cuándo alcanza 55 metros?

## Contexto físico

La ecuación $h(t) = -5t^2 + 30t + 10$ describe el movimiento vertical de un proyectil bajo la acción de la gravedad, donde:

- $h(t)$: altura en metros
- $t$: tiempo en segundos
- $-5$: relacionado con $-\frac{g}{2}$ donde $g \approx 10$ m/s² (gravedad)
- $30$: velocidad inicial vertical (m/s)
- $10$: altura inicial (m)

---

## Método 1: Fórmula general (cuadrática)

### Paso 1: Plantear la ecuación

Buscamos el tiempo $t$ cuando $h(t) = 55$:

$$-5t^2 + 30t + 10 = 55$$

### Paso 2: Reordenar en forma estándar $at^2 + bt + c = 0$

$$-5t^2 + 30t + 10 - 55 = 0$$

$$-5t^2 + 30t - 45 = 0$$

### Paso 3: Simplificar dividiendo por $-5$

$$t^2 - 6t + 9 = 0$$

### Paso 4: Identificar coeficientes

$$a = 1, \quad b = -6, \quad c = 9$$

### Paso 5: Calcular el discriminante

$$\Delta = b^2 - 4ac = (-6)^2 - 4(1)(9)$$

$$\Delta = 36 - 36 = 0$$

### Paso 6: Aplicar la fórmula general

$$t = \frac{-b \pm \sqrt{\Delta}}{2a} = \frac{-(-6) \pm \sqrt{0}}{2(1)}$$

$$t = \frac{6 \pm 0}{2} = \frac{6}{2} = 3$$

### Paso 7: Conclusión

$$\boxed{t = 3 \text{ segundos}}$$

---

## Método 2: Factorización (trinomio cuadrado perfecto)

### Paso 1: Partimos de la ecuación simplificada

$$t^2 - 6t + 9 = 0$$

### Paso 2: Reconocer el trinomio cuadrado perfecto

Observamos que:
- $t^2 = (t)^2$
- $9 = (3)^2$
- $-6t = -2(t)(3)$

Por lo tanto:
$$t^2 - 6t + 9 = (t - 3)^2$$

### Paso 3: Resolver

$$(t - 3)^2 = 0$$

$$t - 3 = 0$$

$$t = 3$$

---

## Método 3: Completar el cuadrado

### Paso 1: Partimos de la ecuación simplificada

$$t^2 - 6t + 9 = 0$$

### Paso 2: Agrupar términos con $t$

$$t^2 - 6t = -9$$

### Paso 3: Completar el cuadrado

Para completar el cuadrado, sumamos $\left(\frac{-6}{2}\right)^2 = 9$ a ambos lados:

$$t^2 - 6t + 9 = -9 + 9$$

$$(t - 3)^2 = 0$$

### Paso 4: Resolver

$$t - 3 = 0 \quad \Rightarrow \quad t = 3$$

---

## Interpretación física

### ¿Por qué hay una sola solución?

El discriminante $\Delta = 0$ indica que la parábola $h(t) = -5t^2 + 30t + 10$ es **[tangente](../../../../glossary.md#tangente)** a la recta horizontal $h = 55$.

Esto significa que:
- El proyectil alcanza exactamente 55 metros **una sola vez**
- Esa altura coincide con la **altura máxima** del proyectil

### Verificación: altura máxima

El vértice de $h(t) = -5t^2 + 30t + 10$ ocurre en:

$$t_{\text{vértice}} = -\frac{b}{2a} = -\frac{30}{2(-5)} = \frac{30}{10} = 3$$

La altura máxima es:

$$h(3) = -5(3)^2 + 30(3) + 10$$

$$= -5(9) + 90 + 10$$

$$= -45 + 90 + 10$$

$$= 55 \text{ metros}$$

**¡Confirmado!** La altura de 55 metros es exactamente la altura máxima.

---

## Análisis gráfico

### Gráfica de $h(t) = -5t^2 + 30t + 10$

```
  h (metros)
     │
  55 │─ ─ ─ ─ ─ ─ ●─ ─ ─ ─ ─  altura máxima
     │          * * 
  50 │         *   *
     │        *     *
  40 │       *       *
     │      *         *
  30 │     *           *
     │    *             *
  20 │   *               *
     │  *                 *
  10 │ ●                   *
     │*                     *
   0 └────────────────────────► t (s)
       0   1   2   3   4   5   6
                   ↑
               t = 3 s
```

### Puntos clave de la trayectoria

| Tiempo (s) | Altura (m) | Descripción |
|------------|------------|-------------|
| $t = 0$ | $10$ | Altura inicial |
| $t = 1$ | $35$ | Subiendo |
| $t = 2$ | $50$ | Subiendo |
| $t = 3$ | $55$ | **Altura máxima** ✓ |
| $t = 4$ | $50$ | Bajando |
| $t = 5$ | $35$ | Bajando |
| $t = 6$ | $10$ | Vuelve a altura inicial |

---

## Verificación completa

### Verificación directa

$$h(3) = -5(3)^2 + 30(3) + 10$$

$$= -5 \cdot 9 + 90 + 10$$

$$= -45 + 90 + 10$$

$$= 55 \quad \checkmark$$

### Verificación de la ecuación

$$-5(3)^2 + 30(3) + 10 = 55$$

$$-45 + 90 + 10 = 55$$

$$55 = 55 \quad \checkmark$$

---

## Caso hipotético: ¿Cuándo alcanza 40 metros?

Si el problema pidiera $h(t) = 40$:

$$-5t^2 + 30t + 10 = 40$$

$$-5t^2 + 30t - 30 = 0$$

$$t^2 - 6t + 6 = 0$$

$$\Delta = 36 - 24 = 12 > 0$$

$$t = \frac{6 \pm \sqrt{12}}{2} = \frac{6 \pm 2\sqrt{3}}{2} = 3 \pm \sqrt{3}$$

**Dos soluciones:**
- $t_1 = 3 - \sqrt{3} \approx 1.27$ s (subiendo)
- $t_2 = 3 + \sqrt{3} \approx 4.73$ s (bajando)

Esto es consistente: alturas menores que la máxima se alcanzan dos veces.

---

## Resumen

| Aspecto | Valor |
|---------|-------|
| Ecuación a resolver | $-5t^2 + 30t + 10 = 55$ |
| Forma simplificada | $t^2 - 6t + 9 = 0$ |
| Discriminante | $\Delta = 0$ |
| Tipo de solución | Única (raíz doble) |
| **Solución** | $\boxed{t = 3 \text{ segundos}}$ |
| Interpretación | Altura máxima del proyectil |

---

## Datos adicionales del problema

- **Altura inicial:** $h(0) = 10$ m
- **Velocidad inicial:** $v_0 = 30$ m/s
- **Altura máxima:** $55$ m (en $t = 3$ s)
- **Tiempo de vuelo total** (regresa a $h = 0$): $t \approx 6.32$ s
