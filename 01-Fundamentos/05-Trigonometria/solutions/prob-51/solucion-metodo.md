<!--
::METADATA::
type: solution
topic_id: fun-05-trigonometria
file_id: prob-51-solucion
problem_ref: Prob-51
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Seno de 75° por fórmula de suma

## Problema
Calcula el valor exacto de $\sin 75°$ usando la fórmula de suma.

---

## Método: Fórmula de suma de ángulos

### Paso 1: Expresar 75° como suma de ángulos notables
$$75° = 45° + 30°$$

### Paso 2: Aplicar la fórmula de seno de suma
$$\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$$

Con $\alpha = 45°$ y $\beta = 30°$:
$$\sin 75° = \sin 45°\cos 30° + \cos 45°\sin 30°$$

### Paso 3: Sustituir valores conocidos

| Ángulo | sin | cos |
|:------:|:---:|:---:|
| 30° | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ |
| 45° | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ |

$$\sin 75° = \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \cdot \frac{1}{2}$$

### Paso 4: Realizar los productos
$$= \frac{\sqrt{2} \cdot \sqrt{3}}{4} + \frac{\sqrt{2}}{4}$$

$$= \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4}$$

### Paso 5: Sumar las fracciones
$$= \frac{\sqrt{6} + \sqrt{2}}{4}$$

---

## Método alternativo: 75° = 120° - 45°

### Aplicando fórmula de resta
$$\sin 75° = \sin(120° - 45°) = \sin 120°\cos 45° - \cos 120°\sin 45°$$

$$= \frac{\sqrt{3}}{2} \cdot \frac{\sqrt{2}}{2} - \left(-\frac{1}{2}\right) \cdot \frac{\sqrt{2}}{2}$$

$$= \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4} = \frac{\sqrt{6} + \sqrt{2}}{4}$$ ✓

---

## Respuesta Final
$$\boxed{\sin 75° = \frac{\sqrt{6} + \sqrt{2}}{4}}$$

---

## Verificación numérica
**Valor exacto:**
$$\frac{\sqrt{6} + \sqrt{2}}{4} = \frac{2.449 + 1.414}{4} = \frac{3.863}{4} \approx 0.9659$$

**Calculadora:**
$$\sin 75° \approx 0.9659 \checkmark$$

---

## Formas equivalentes
$$\sin 75° = \frac{\sqrt{6} + \sqrt{2}}{4} = \frac{\sqrt{2}(\sqrt{3} + 1)}{4} = \cos 15°$$

---

## Nota
Esta identidad también muestra que:
$$\sin 75° = \cos(90° - 75°) = \cos 15°$$

Por lo tanto: $\cos 15° = \frac{\sqrt{6} + \sqrt{2}}{4}$
