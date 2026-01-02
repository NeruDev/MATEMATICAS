<!--
::METADATA::
type: solution
topic_id: fun-02-aritmetica
file_id: prob-52-solucion
problem_ref: Prob-52
status: stable
audience: student
-->

# Solución: Decimal mixto periódico a fracción

## Problema
Convierte $0.1\overline{6}$ a fracción.

---

## Método: Sistema de ecuaciones con potencias de 10

### Paso 1: Definir la variable
Sea $x = 0.1\overline{6} = 0.16666...$

### Paso 2: Identificar la estructura
- Hay **1** dígito antes del período (el 1)
- El período es **6** (1 dígito)

### Paso 3: Multiplicar para mover el período al inicio
Multiplicamos por $10$ (para mover el dígito no periódico):
$$10x = 1.6666... = 1.\overline{6}$$

### Paso 4: Multiplicar de nuevo para alinear el período
Multiplicamos por $100$ (para tener otra ecuación con $.\overline{6}$):
$$100x = 16.6666... = 16.\overline{6}$$

### Paso 5: Restar las ecuaciones
$$\begin{aligned}
100x &= 16.\overline{6} \\
-\quad 10x &= 1.\overline{6} \\
\hline
90x &= 15
\end{aligned}$$

### Paso 6: Despejar x
$$x = \frac{15}{90}$$

### Paso 7: Simplificar
$$\frac{15}{90} = \frac{15 \div 15}{90 \div 15} = \frac{1}{6}$$

**Detalle de simplificación:**
$$\text{[MCD](../../../../glossary.md#mcd)}(15, 90) = 15$$
- $15 = 3 \times 5$
- $90 = 2 \times 3^2 \times 5$
- $\text{[MCD](../../../../glossary.md#mcd)} = 3 \times 5 = 15$

---

## Respuesta Final
$$0.1\overline{6} = \boxed{\frac{1}{6}}$$

---

## Verificación
$$\frac{1}{6} = 1 \div 6 = 0.16666... = 0.1\overline{6} \checkmark$$

---

## Fórmula general para decimales mixtos periódicos
Para $0.a_1a_2...a_m\overline{b_1b_2...b_n}$:

$$\text{Fracción} = \frac{\text{(todo junto)} - \text{(parte no periódica)}}{\underbrace{99...9}_{n \text{ nueves}}\underbrace{00...0}_{m \text{ ceros}}}$$

En nuestro caso: $0.1\overline{6}$
- $m = 1$ (un dígito antes del período)
- $n = 1$ (un dígito en el período)

$$\frac{16 - 1}{90} = \frac{15}{90} = \frac{1}{6}$$
