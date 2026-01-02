<!--
::METADATA::
type: solution
topic_id: cd-01-limites
file_id: prob-21-solucion
problem_ref: Prob-21
status: stable
audience: student
-->

# Solución: Racionalización doble

## Problema
Evalúa $\displaystyle\lim_{x \to 0} \frac{\sqrt{1+x} - \sqrt{1-x}}{x}$

---

## Análisis inicial
[Sustitución](../../../../glossary.md#sustitucion) directa: $\frac{\sqrt{1} - \sqrt{1}}{0} = \frac{0}{0}$ → [Forma indeterminada](../../../../glossary.md#forma-indeterminada)

---

## Método: Racionalización por conjugado

### Paso 1: Multiplicar por el conjugado
El conjugado de $\sqrt{1+x} - \sqrt{1-x}$ es $\sqrt{1+x} + \sqrt{1-x}$.

$$\lim_{x \to 0} \frac{\sqrt{1+x} - \sqrt{1-x}}{x} \cdot \frac{\sqrt{1+x} + \sqrt{1-x}}{\sqrt{1+x} + \sqrt{1-x}}$$

### Paso 2: Aplicar diferencia de cuadrados en el numerador
$$\frac{(\sqrt{1+x})^2 - (\sqrt{1-x})^2}{x(\sqrt{1+x} + \sqrt{1-x})}$$

$$= \frac{(1+x) - (1-x)}{x(\sqrt{1+x} + \sqrt{1-x})}$$

### Paso 3: Simplificar el numerador
$$= \frac{1 + x - 1 + x}{x(\sqrt{1+x} + \sqrt{1-x})}$$

$$= \frac{2x}{x(\sqrt{1+x} + \sqrt{1-x})}$$

### Paso 4: Cancelar x (válido pues x ≠ 0 en el límite)
$$= \frac{2}{\sqrt{1+x} + \sqrt{1-x}}$$

### Paso 5: Evaluar el límite
$$\lim_{x \to 0} \frac{2}{\sqrt{1+x} + \sqrt{1-x}} = \frac{2}{\sqrt{1+0} + \sqrt{1-0}} = \frac{2}{1 + 1} = \frac{2}{2} = 1$$

---

## Respuesta Final
$$\boxed{\lim_{x \to 0} \frac{\sqrt{1+x} - \sqrt{1-x}}{x} = 1}$$

---

## Verificación numérica

| $x$ | $\frac{\sqrt{1+x} - \sqrt{1-x}}{x}$ |
|:---:|:-----------------------------------:|
| 0.1 | 0.99750... |
| 0.01 | 0.99997... |
| 0.001 | 0.99999... |
| -0.1 | 1.00251... |
| -0.01 | 1.00002... |

Los valores se aproximan a 1 desde ambos lados. ✓

---

## Interpretación geométrica
Este [límite](../../../../glossary.md#limite) representa la [derivada](../../../../glossary.md#derivada) de $f(x) = \sqrt{1+x} - \sqrt{1-x}$ evaluada en $x = 0$:

$$f'(0) = \lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{\sqrt{1+x} - \sqrt{1-x}}{x} = 1$$

Verificación: $f'(x) = \frac{1}{2\sqrt{1+x}} + \frac{1}{2\sqrt{1-x}}$, entonces $f'(0) = \frac{1}{2} + \frac{1}{2} = 1$ ✓
