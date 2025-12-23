<!--
::METADATA::
type: solution
topic_id: fun-02-aritmetica
file_id: prob-08-solucion
problem_ref: Prob-08
status: stable
audience: student
-->

# Solución: Decimal periódico a fracción

## Problema
Expresa $3.\overline{14}$ como fracción irreducible.

---

## Método: Multiplicación por potencia de 10

### Paso 1: Definir la variable
Sea $x = 3.\overline{14} = 3.141414...$

### Paso 2: Identificar el período
El período es **14** (dos dígitos), por lo tanto multiplicamos por $10^2 = 100$.

### Paso 3: Multiplicar por la potencia de 10
$$100x = 314.141414...$$

### Paso 4: Plantear la resta
Restamos la ecuación original de la multiplicada:
$$\begin{aligned}
100x &= 314.141414... \\
-\quad x &= 3.141414... \\
\hline
99x &= 311
\end{aligned}$$

### Paso 5: Despejar x
$$x = \frac{311}{99}$$

### Paso 6: Verificar si es irreducible
Factorizamos ambos números:
- $311$ es primo (no es divisible por 2, 3, 5, 7, 11, 13, 17 y $19^2 > 311$)
- $99 = 9 \times 11 = 3^2 \times 11$

Como $\text{MCD}(311, 99) = 1$, la fracción ya es irreducible.

---

## Respuesta Final
$$3.\overline{14} = \boxed{\frac{311}{99}}$$

---

## Verificación
Dividimos $311 \div 99$:
- $311 = 99 \times 3 + 14$
- Continuamos: $140 \div 99 = 1$ resto $41$
- $410 \div 99 = 4$ resto $14$
- El patrón se repite ✓

Por lo tanto: $\frac{311}{99} = 3.141414... = 3.\overline{14}$ ✓
