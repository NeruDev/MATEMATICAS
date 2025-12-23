<!--
::METADATA::
type: solution
topic_id: cd-01-limites
file_id: prob-30-solucion
problem_ref: Prob-30
status: stable
audience: student
-->

# Solución: Límite trigonométrico de tercer orden

## Problema
Evalúa $\displaystyle\lim_{x \to 0} \frac{x - \sin x}{x^3}$

---

## Análisis inicial
Sustitución directa: $\frac{0 - 0}{0} = \frac{0}{0}$ → Forma indeterminada

---

## Método 1: Regla de L'Hôpital (tres veces)

### Aplicación 1
$$\lim_{x \to 0} \frac{x - \sin x}{x^3} = \lim_{x \to 0} \frac{1 - \cos x}{3x^2}$$

Aún forma $\frac{0}{0}$.

### Aplicación 2
$$= \lim_{x \to 0} \frac{\sin x}{6x}$$

Aún forma $\frac{0}{0}$.

### Aplicación 3
$$= \lim_{x \to 0} \frac{\cos x}{6} = \frac{1}{6}$$

---

## Método 2: Serie de Taylor

### Paso 1: Escribir la serie de Taylor de sin x
$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots = x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots$$

### Paso 2: Calcular x - sin x
$$x - \sin x = x - \left(x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots\right)$$
$$= \frac{x^3}{6} - \frac{x^5}{120} + \cdots$$

### Paso 3: Dividir entre x³
$$\frac{x - \sin x}{x^3} = \frac{\frac{x^3}{6} - \frac{x^5}{120} + \cdots}{x^3}$$
$$= \frac{1}{6} - \frac{x^2}{120} + \cdots$$

### Paso 4: Tomar el límite
$$\lim_{x \to 0} \left(\frac{1}{6} - \frac{x^2}{120} + \cdots\right) = \frac{1}{6}$$

---

## Respuesta Final
$$\boxed{\lim_{x \to 0} \frac{x - \sin x}{x^3} = \frac{1}{6}}$$

---

## Verificación numérica

| $x$ (rad) | $\frac{x - \sin x}{x^3}$ |
|:---------:|:------------------------:|
| 0.1 | 0.16658... |
| 0.01 | 0.16666... |
| 0.001 | 0.16666... |

El valor se aproxima a $\frac{1}{6} \approx 0.16667$. ✓

---

## Límites relacionados importantes

| Límite | Valor |
|:-------|:-----:|
| $\lim_{x \to 0} \frac{\sin x}{x}$ | 1 |
| $\lim_{x \to 0} \frac{1 - \cos x}{x^2}$ | $\frac{1}{2}$ |
| $\lim_{x \to 0} \frac{x - \sin x}{x^3}$ | $\frac{1}{6}$ |
| $\lim_{x \to 0} \frac{\tan x - x}{x^3}$ | $\frac{1}{3}$ |
