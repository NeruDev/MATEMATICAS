<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: FUN-03-Prob-78-Solucion
status: stable
audience: student
problem_ref: "[Prob-78]"
methods: ["eliminacion-gaussiana", "sustitucion-hacia-atras", "sistemas-3x3"]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución [Prob-78]: Sistema de ecuaciones 3×3

> **Problema:** Resuelve el sistema 3×3:
> $$\begin{cases} x + y + z = 6 \\ 2x - y + z = 3 \\ x + 2y - z = 3 \end{cases}$$

## Método 1: Eliminación Gaussiana

### Paso 1: Escribir el sistema

Numeramos las ecuaciones para referencia:

- $(E_1): \quad x + y + z = 6$
- $(E_2): \quad 2x - y + z = 3$
- $(E_3): \quad x + 2y - z = 3$

### Paso 2: Eliminar $x$ de las ecuaciones (2) y (3)

**Eliminar $x$ de $E_2$:**

Calculamos $E_2 - 2E_1$:

$$\begin{aligned}
(2x - y + z) - 2(x + y + z) &= 3 - 2(6) \\
2x - y + z - 2x - 2y - 2z &= 3 - 12 \\
-3y - z &= -9
\end{aligned}$$

Nueva ecuación $(E_2')$: $-3y - z = -9$

Simplificando (dividiendo entre $-1$): $3y + z = 9$

**Eliminar $x$ de $E_3$:**

Calculamos $E_3 - E_1$:

$$\begin{aligned}
(x + 2y - z) - (x + y + z) &= 3 - 6 \\
x + 2y - z - x - y - z &= -3 \\
y - 2z &= -3
\end{aligned}$$

Nueva ecuación $(E_3')$: $y - 2z = -3$

### Paso 3: Sistema reducido en $y$ y $z$

Ahora tenemos:
- $(E_2'): \quad 3y + z = 9$
- $(E_3'): \quad y - 2z = -3$

### Paso 4: Eliminar $y$ del sistema reducido

Calculamos $E_2' - 3E_3'$:

$$\begin{aligned}
(3y + z) - 3(y - 2z) &= 9 - 3(-3) \\
3y + z - 3y + 6z &= 9 + 9 \\
7z &= 18
\end{aligned}$$

Por lo tanto:

$$z = \frac{18}{7}$$

### Paso 5: Sustitución hacia atrás para encontrar $y$

Sustituimos $z = \frac{18}{7}$ en $(E_3')$:

$$y - 2\left(\frac{18}{7}\right) = -3$$

$$y - \frac{36}{7} = -3$$

$$y = -3 + \frac{36}{7}$$

$$y = \frac{-21 + 36}{7} = \frac{15}{7}$$

### Paso 6: Sustitución hacia atrás para encontrar $x$

Sustituimos $y = \frac{15}{7}$ y $z = \frac{18}{7}$ en $(E_1)$:

$$x + \frac{15}{7} + \frac{18}{7} = 6$$

$$x + \frac{33}{7} = 6$$

$$x = 6 - \frac{33}{7}$$

$$x = \frac{42 - 33}{7} = \frac{9}{7}$$

---

## Método 2: Eliminación por suma/resta directa

### Paso 1: Sumar ecuaciones estratégicamente

**Sumamos todas las ecuaciones:**

$$(E_1) + (E_2) + (E_3):$$

$$(x + y + z) + (2x - y + z) + (x + 2y - z) = 6 + 3 + 3$$

$$4x + 2y + z = 12 \quad \text{...(A)}$$

**Sumamos $E_1$ y $E_3$:**

$$(x + y + z) + (x + 2y - z) = 6 + 3$$

$$2x + 3y = 9 \quad \text{...(B)}$$

**Sumamos $E_1$ y $E_2$:**

$$(x + y + z) + (2x - y + z) = 6 + 3$$

$$3x + 2z = 9 \quad \text{...(C)}$$

### Paso 2: Continuar la eliminación

De (B): $2x + 3y = 9$, despejamos $x$:

$$x = \frac{9 - 3y}{2}$$

De (C): $3x + 2z = 9$

Sustituimos $x$:

$$3 \cdot \frac{9 - 3y}{2} + 2z = 9$$

$$\frac{27 - 9y}{2} + 2z = 9$$

$$27 - 9y + 4z = 18$$

$$-9y + 4z = -9$$

$$9y - 4z = 9 \quad \text{...(D)}$$

### Paso 3: Usar $(E_3')$ con (D)

De $(E_3')$: $y - 2z = -3$, tenemos $y = 2z - 3$

Sustituimos en (D):

$$9(2z - 3) - 4z = 9$$

$$18z - 27 - 4z = 9$$

$$14z = 36$$

$$z = \frac{36}{14} = \frac{18}{7}$$

Y continuamos como antes para obtener $y$ y $x$.

---

## Método 3: Regla de Cramer

### Paso 1: Escribir la matriz de coeficientes

$$A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & -1 & 1 \\ 1 & 2 & -1 \end{pmatrix}$$

### Paso 2: Calcular el determinante principal $|A|$

Expandiendo por la primera fila:

$$|A| = 1 \cdot \begin{vmatrix} -1 & 1 \\ 2 & -1 \end{vmatrix} - 1 \cdot \begin{vmatrix} 2 & 1 \\ 1 & -1 \end{vmatrix} + 1 \cdot \begin{vmatrix} 2 & -1 \\ 1 & 2 \end{vmatrix}$$

Calculamos cada [determinante](../../../../glossary.md#determinante) 2×2:

$$\begin{vmatrix} -1 & 1 \\ 2 & -1 \end{vmatrix} = (-1)(-1) - (1)(2) = 1 - 2 = -1$$

$$\begin{vmatrix} 2 & 1 \\ 1 & -1 \end{vmatrix} = (2)(-1) - (1)(1) = -2 - 1 = -3$$

$$\begin{vmatrix} 2 & -1 \\ 1 & 2 \end{vmatrix} = (2)(2) - (-1)(1) = 4 + 1 = 5$$

Por lo tanto:

$$|A| = 1(-1) - 1(-3) + 1(5) = -1 + 3 + 5 = 7$$

### Paso 3: Calcular $|A_x|$ (reemplazando columna $x$ por términos independientes)

$$A_x = \begin{pmatrix} 6 & 1 & 1 \\ 3 & -1 & 1 \\ 3 & 2 & -1 \end{pmatrix}$$

$$|A_x| = 6 \cdot \begin{vmatrix} -1 & 1 \\ 2 & -1 \end{vmatrix} - 1 \cdot \begin{vmatrix} 3 & 1 \\ 3 & -1 \end{vmatrix} + 1 \cdot \begin{vmatrix} 3 & -1 \\ 3 & 2 \end{vmatrix}$$

$$= 6(-1) - 1((-3) - 3) + 1(6 + 3)$$

$$= -6 - 1(-6) + 1(9)$$

$$= -6 + 6 + 9 = 9$$

### Paso 4: Calcular $|A_y|$

$$A_y = \begin{pmatrix} 1 & 6 & 1 \\ 2 & 3 & 1 \\ 1 & 3 & -1 \end{pmatrix}$$

$$|A_y| = 1 \cdot \begin{vmatrix} 3 & 1 \\ 3 & -1 \end{vmatrix} - 6 \cdot \begin{vmatrix} 2 & 1 \\ 1 & -1 \end{vmatrix} + 1 \cdot \begin{vmatrix} 2 & 3 \\ 1 & 3 \end{vmatrix}$$

$$= 1(-3 - 3) - 6(-2 - 1) + 1(6 - 3)$$

$$= 1(-6) - 6(-3) + 1(3)$$

$$= -6 + 18 + 3 = 15$$

### Paso 5: Calcular $|A_z|$

$$A_z = \begin{pmatrix} 1 & 1 & 6 \\ 2 & -1 & 3 \\ 1 & 2 & 3 \end{pmatrix}$$

$$|A_z| = 1 \cdot \begin{vmatrix} -1 & 3 \\ 2 & 3 \end{vmatrix} - 1 \cdot \begin{vmatrix} 2 & 3 \\ 1 & 3 \end{vmatrix} + 6 \cdot \begin{vmatrix} 2 & -1 \\ 1 & 2 \end{vmatrix}$$

$$= 1(-3 - 6) - 1(6 - 3) + 6(4 + 1)$$

$$= 1(-9) - 1(3) + 6(5)$$

$$= -9 - 3 + 30 = 18$$

### Paso 6: Aplicar la regla de Cramer

$$x = \frac{|A_x|}{|A|} = \frac{9}{7}$$

$$y = \frac{|A_y|}{|A|} = \frac{15}{7}$$

$$z = \frac{|A_z|}{|A|} = \frac{18}{7}$$

---

## Verificación

Sustituimos $x = \frac{9}{7}$, $y = \frac{15}{7}$, $z = \frac{18}{7}$ en cada ecuación:

**Ecuación 1:** $x + y + z = 6$

$$\frac{9}{7} + \frac{15}{7} + \frac{18}{7} = \frac{9 + 15 + 18}{7} = \frac{42}{7} = 6 \quad \checkmark$$

**Ecuación 2:** $2x - y + z = 3$

$$2\left(\frac{9}{7}\right) - \frac{15}{7} + \frac{18}{7} = \frac{18 - 15 + 18}{7} = \frac{21}{7} = 3 \quad \checkmark$$

**Ecuación 3:** $x + 2y - z = 3$

$$\frac{9}{7} + 2\left(\frac{15}{7}\right) - \frac{18}{7} = \frac{9 + 30 - 18}{7} = \frac{21}{7} = 3 \quad \checkmark$$

---

## Diagrama del proceso

```
         Sistema Original
         ┌─────────────────────┐
         │ x + y + z = 6       │ (E₁)
         │ 2x - y + z = 3      │ (E₂)
         │ x + 2y - z = 3      │ (E₃)
         └─────────────────────┘
                   │
        Eliminación de x
                   │
         ┌─────────┴─────────┐
         │                   │
     E₂ - 2E₁            E₃ - E₁
         │                   │
    3y + z = 9          y - 2z = -3
         │                   │
         └─────────┬─────────┘
                   │
        Eliminación de y
                   │
              7z = 18
                   │
              z = 18/7
                   │
        Sustitución hacia atrás
                   │
         ┌─────────┴─────────┐
         │                   │
      y = 15/7           x = 9/7
```

---

## Expresión de la solución

La solución puede escribirse como:

**Forma fraccionaria:**
$$(x, y, z) = \left(\frac{9}{7}, \frac{15}{7}, \frac{18}{7}\right)$$

**Forma decimal aproximada:**
$$(x, y, z) \approx (1.286, 2.143, 2.571)$$

---

## Respuesta Final

$$\boxed{x = \frac{9}{7}, \quad y = \frac{15}{7}, \quad z = \frac{18}{7}}$$

O equivalentemente: $(x, y, z) = \left(\frac{9}{7}, \frac{15}{7}, \frac{18}{7}\right)$

> 📚 Volver a: [FUN-03-Problemas](../../problems/FUN-03-Problemas.md)
