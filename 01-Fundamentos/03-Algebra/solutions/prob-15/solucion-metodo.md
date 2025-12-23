<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: prob-15-solucion
problem_ref: Prob-15
status: stable
audience: student
-->

# Solución: División larga de polinomios

## Problema
Divide $(x^3 + 2x^2 - 5x + 1)$ entre $(x - 2)$ usando división larga.

---

## Método: División larga de polinomios

### Paso 1: Preparar la división
```
                    _______________
    x - 2  |  x³ + 2x² - 5x + 1
```

### Paso 2: Primera división
**¿Cuántas veces cabe $x$ en $x^3$?**
$$\frac{x^3}{x} = x^2$$

**Multiplicar:** $(x - 2) \times x^2 = x^3 - 2x^2$

**Restar:**
$$\begin{aligned}
(x^3 + 2x^2) - (x^3 - 2x^2) &= x^3 + 2x^2 - x^3 + 2x^2 \\
&= 4x^2
\end{aligned}$$

**Estado actual:**
```
                      x²
                    _______________
    x - 2  |  x³ + 2x² - 5x + 1
              x³ - 2x²
              ─────────
                   4x² - 5x
```

### Paso 3: Segunda división
**¿Cuántas veces cabe $x$ en $4x^2$?**
$$\frac{4x^2}{x} = 4x$$

**Multiplicar:** $(x - 2) \times 4x = 4x^2 - 8x$

**Restar:**
$$\begin{aligned}
(4x^2 - 5x) - (4x^2 - 8x) &= 4x^2 - 5x - 4x^2 + 8x \\
&= 3x
\end{aligned}$$

**Estado actual:**
```
                      x² + 4x
                    _______________
    x - 2  |  x³ + 2x² - 5x + 1
              x³ - 2x²
              ─────────
                   4x² - 5x
                   4x² - 8x
                   ─────────
                         3x + 1
```

### Paso 4: Tercera división
**¿Cuántas veces cabe $x$ en $3x$?**
$$\frac{3x}{x} = 3$$

**Multiplicar:** $(x - 2) \times 3 = 3x - 6$

**Restar:**
$$\begin{aligned}
(3x + 1) - (3x - 6) &= 3x + 1 - 3x + 6 \\
&= 7
\end{aligned}$$

### Paso 5: Resultado final
```
                      x² + 4x + 3
                    _______________
    x - 2  |  x³ + 2x² - 5x + 1
              x³ - 2x²
              ─────────
                   4x² - 5x
                   4x² - 8x
                   ─────────
                         3x + 1
                         3x - 6
                         ──────
                              7  ← Residuo
```

---

## Respuesta Final
$$\frac{x^3 + 2x^2 - 5x + 1}{x - 2} = \boxed{x^2 + 4x + 3 + \frac{7}{x-2}}$$

O equivalentemente:
$$x^3 + 2x^2 - 5x + 1 = (x - 2)(x^2 + 4x + 3) + 7$$

---

## Verificación
Expandimos $(x - 2)(x^2 + 4x + 3) + 7$:
$$\begin{aligned}
&= x(x^2 + 4x + 3) - 2(x^2 + 4x + 3) + 7 \\
&= x^3 + 4x^2 + 3x - 2x^2 - 8x - 6 + 7 \\
&= x^3 + (4-2)x^2 + (3-8)x + (-6+7) \\
&= x^3 + 2x^2 - 5x + 1 \checkmark
\end{aligned}$$
