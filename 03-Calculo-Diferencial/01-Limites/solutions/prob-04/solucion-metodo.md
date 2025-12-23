<!--
::METADATA::
type: solution
topic_id: cd-01-limites
file_id: prob-04-solucion
problem_ref: Prob-04
status: stable
audience: student
-->

# Solución: Demostración épsilon-delta para x²

## Problema
Demuestra que $\displaystyle\lim_{x \to 2} x^2 = 4$ usando la definición formal.

---

## Definición formal de límite
$$\lim_{x \to a} f(x) = L \iff \forall \varepsilon > 0, \exists \delta > 0 : 0 < |x - a| < \delta \Rightarrow |f(x) - L| < \varepsilon$$

---

## Demostración

### Paso 1: Identificar los elementos
- $f(x) = x^2$
- $a = 2$
- $L = 4$

Debemos demostrar: $\forall \varepsilon > 0, \exists \delta > 0 : 0 < |x - 2| < \delta \Rightarrow |x^2 - 4| < \varepsilon$

### Paso 2: Trabajar con |f(x) - L|
$$|x^2 - 4| = |x - 2||x + 2|$$

Factorizamos usando diferencia de cuadrados.

### Paso 3: Acotar |x + 2|
Para encontrar $\delta$, primero acotamos $|x + 2|$.

Supongamos inicialmente que $\delta \leq 1$. Entonces:
$$|x - 2| < 1 \Rightarrow -1 < x - 2 < 1 \Rightarrow 1 < x < 3$$

Por lo tanto:
$$3 < x + 2 < 5 \Rightarrow |x + 2| < 5$$

### Paso 4: Establecer la desigualdad
Con $|x + 2| < 5$ y $|x - 2| < \delta$:
$$|x^2 - 4| = |x - 2||x + 2| < 5|x - 2| < 5\delta$$

### Paso 5: Encontrar δ
Queremos $|x^2 - 4| < \varepsilon$.

Si $5\delta < \varepsilon$, entonces $\delta < \frac{\varepsilon}{5}$.

Pero también necesitamos $\delta \leq 1$ para que la acotación de $|x + 2|$ sea válida.

**Elección de δ:**
$$\delta = \min\left\{1, \frac{\varepsilon}{5}\right\}$$

### Paso 6: Verificación formal
Dado $\varepsilon > 0$, elegimos $\delta = \min\left\{1, \frac{\varepsilon}{5}\right\}$.

Si $0 < |x - 2| < \delta$, entonces:

1. Como $\delta \leq 1$: $|x - 2| < 1 \Rightarrow |x + 2| < 5$

2. Como $\delta \leq \frac{\varepsilon}{5}$:
$$|x^2 - 4| = |x - 2||x + 2| < \delta \cdot 5 \leq \frac{\varepsilon}{5} \cdot 5 = \varepsilon$$

---

## Conclusión
$$\boxed{\lim_{x \to 2} x^2 = 4 \quad \blacksquare}$$

Con $\delta = \min\left\{1, \frac{\varepsilon}{5}\right\}$

---

## Ejemplo numérico
Si $\varepsilon = 0.01$:
$$\delta = \min\left\{1, \frac{0.01}{5}\right\} = \min\{1, 0.002\} = 0.002$$

Verificación: Si $|x - 2| < 0.002$, entonces $1.998 < x < 2.002$

$$|x^2 - 4| < |2.002^2 - 4| = |4.008004 - 4| = 0.008004 < 0.01 = \varepsilon \checkmark$$
