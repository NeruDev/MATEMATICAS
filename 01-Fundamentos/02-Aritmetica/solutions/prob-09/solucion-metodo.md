<!--
::METADATA::
type: solution
topic_id: fun-02-aritmetica
file_id: FUN-02-Prob-09-Solucion
status: stable
audience: student
problem_ref: "[Prob-09]"
methods: ["demostración directa", "definición de racionales"]
-->

# Solución [Prob-09]: Demostración suma de racionales es racional

> **Problema:** Demuestra que la suma de dos números racionales es racional.

---

## Método 1: Demostración Directa

### Paso 1: Definición de números racionales

Por definición, un número es **racional** si puede expresarse como el cociente de dos enteros, donde el denominador es distinto de cero.

Sean $r_1$ y $r_2$ dos números racionales. Entonces existen enteros $a, b, c, d$ con $b \neq 0$ y $d \neq 0$ tales que:

$$r_1 = \frac{a}{b} \quad \text{y} \quad r_2 = \frac{c}{d}$$

### Paso 2: Calcular la suma

Sumamos los dos racionales:

$$r_1 + r_2 = \frac{a}{b} + \frac{c}{d}$$

### Paso 3: Encontrar denominador común

Para sumar fracciones, usamos el denominador común $bd$:

$$r_1 + r_2 = \frac{a}{b} + \frac{c}{d} = \frac{a \cdot d}{b \cdot d} + \frac{c \cdot b}{d \cdot b}$$

### Paso 4: Realizar la suma

$$r_1 + r_2 = \frac{ad + cb}{bd}$$

### Paso 5: Verificar que el resultado es racional

Debemos demostrar que $\frac{ad + cb}{bd}$ es un número racional:

1. **Numerador:** $ad + cb$
   - Como $a, d \in \mathbb{Z}$, entonces $ad \in \mathbb{Z}$ (producto de enteros es entero)
   - Como $c, b \in \mathbb{Z}$, entonces $cb \in \mathbb{Z}$ (producto de enteros es entero)
   - Como $ad, cb \in \mathbb{Z}$, entonces $ad + cb \in \mathbb{Z}$ (suma de enteros es entero)

2. **Denominador:** $bd$
   - Como $b, d \in \mathbb{Z}$, entonces $bd \in \mathbb{Z}$ (producto de enteros es entero)
   - Como $b \neq 0$ y $d \neq 0$, entonces $bd \neq 0$

### Paso 6: Conclusión

Por lo tanto:
- El numerador $ad + cb$ es un número entero
- El denominador $bd$ es un número entero distinto de cero

Esto significa que $r_1 + r_2 = \frac{ad + cb}{bd}$ cumple la definición de número racional.

$$\boxed{r_1 + r_2 \in \mathbb{Q}}$$

### Verificación

**Ejemplo numérico:** Tomemos $r_1 = \frac{2}{3}$ y $r_2 = \frac{5}{7}$

$$r_1 + r_2 = \frac{2}{3} + \frac{5}{7} = \frac{2 \cdot 7 + 5 \cdot 3}{3 \cdot 7} = \frac{14 + 15}{21} = \frac{29}{21}$$

- $29 \in \mathbb{Z}$ ✓
- $21 \in \mathbb{Z}$ y $21 \neq 0$ ✓
- Por lo tanto, $\frac{29}{21} \in \mathbb{Q}$ ✓

---

## Método 2: Usando propiedades de clausura

### Paso 1: Propiedades de los enteros

Los números enteros $\mathbb{Z}$ son **cerrados** bajo:
- **Suma:** Si $m, n \in \mathbb{Z}$, entonces $m + n \in \mathbb{Z}$
- **Multiplicación:** Si $m, n \in \mathbb{Z}$, entonces $m \cdot n \in \mathbb{Z}$

### Paso 2: Aplicar la definición

Sean $\frac{a}{b}, \frac{c}{d} \in \mathbb{Q}$ donde $a, b, c, d \in \mathbb{Z}$ con $b, d \neq 0$.

### Paso 3: La suma

$$\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$$

### Paso 4: Aplicar clausura

Por la propiedad de clausura de $\mathbb{Z}$:
- $ad \in \mathbb{Z}$ (clausura bajo multiplicación)
- $bc \in \mathbb{Z}$ (clausura bajo multiplicación)
- $ad + bc \in \mathbb{Z}$ (clausura bajo suma)
- $bd \in \mathbb{Z}$ (clausura bajo multiplicación)

### Paso 5: Verificar denominador no nulo

Como $\mathbb{Z}$ es un dominio de integridad (no tiene divisores de cero):
$$b \neq 0 \text{ y } d \neq 0 \implies bd \neq 0$$

### Paso 6: Conclusión

$\frac{ad + bc}{bd}$ tiene numerador entero y denominador entero no nulo, por lo tanto es racional.

$$\therefore \mathbb{Q} \text{ es cerrado bajo la suma} \quad \blacksquare$$

---

## Respuesta Final

**La suma de dos números racionales siempre es racional.**

Formalmente: Si $r_1, r_2 \in \mathbb{Q}$, entonces $r_1 + r_2 \in \mathbb{Q}$.

Esto demuestra que el conjunto de los números racionales $\mathbb{Q}$ es **cerrado** bajo la operación de suma.

---

> 📚 Volver a: [FUN-02-Problemas](../../problems/FUN-02-Problemas.md)
