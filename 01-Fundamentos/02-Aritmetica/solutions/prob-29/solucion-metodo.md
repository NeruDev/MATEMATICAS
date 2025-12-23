<!--
::METADATA::
type: solution
topic_id: fun-02-aritmetica
file_id: FUN-02-Prob-29-Solucion
status: stable
audience: student
problem_ref: "[Prob-29]"
methods: ["demostración por contradicción", "demostración directa"]
-->

# Solución [Prob-29]: Demostración primos impares

> **Problema:** Demuestra que si $p$ es primo y $p > 2$, entonces $p$ es impar.

---

## Método 1: Demostración por Contradicción

### Paso 1: Establecer la hipótesis

Queremos demostrar: Si $p$ es primo y $p > 2$, entonces $p$ es impar.

**Supongamos lo contrario** (para llegar a una contradicción):
- Supongamos que existe un número $p$ tal que:
  - $p$ es primo
  - $p > 2$
  - $p$ es **par**

### Paso 2: Analizar qué significa ser par

Un número par es aquel que es divisible por 2. Es decir, si $p$ es par, entonces:

$$2 \mid p$$

Lo que significa que $p = 2k$ para algún entero $k \geq 1$.

### Paso 3: Analizar los divisores de p

Como $p$ es par, sus divisores incluyen:
- $1$ (siempre divide a cualquier entero positivo)
- $2$ (porque $p$ es par)
- $p$ (todo número es divisible por sí mismo)

### Paso 4: Encontrar la contradicción

Por definición, un número primo tiene **exactamente dos divisores**: 1 y él mismo.

Si $p > 2$ y $p$ es par, entonces:
- $1$ divide a $p$
- $2$ divide a $p$
- $p$ divide a $p$

Pero como $p > 2$, tenemos que $2 \neq p$.

Por lo tanto, $p$ tendría **al menos tres divisores**: $1, 2$ y $p$.

Esto contradice que $p$ sea primo (que debe tener exactamente dos divisores).

### Paso 5: Conclusión

La suposición de que $p$ es par lleva a una contradicción.

Por lo tanto, si $p$ es primo y $p > 2$, entonces $p$ **debe ser impar**.

$$\blacksquare$$

---

## Método 2: Demostración Directa

### Paso 1: Clasificación de enteros

Todo número entero positivo es **par** o **impar**:
- Par: $n = 2k$ para algún $k \in \mathbb{Z}^+$
- Impar: $n = 2k + 1$ para algún $k \in \mathbb{Z}^+ \cup \{0\}$

### Paso 2: Analizar los números pares mayores que 2

Sea $n$ un número par mayor que 2. Entonces:

$$n = 2k \quad \text{donde } k > 1$$

### Paso 3: Divisores de un número par

Si $n = 2k$ con $k > 1$, entonces los divisores de $n$ incluyen:
- $1$
- $2$
- $k$ (si $k \neq 2$)
- $n$

Como $n > 2$, tenemos $k \geq 2$, y dado que $n = 2k$:
- Si $k = 2$: $n = 4$, divisores: $\{1, 2, 4\}$ → 3 divisores
- Si $k > 2$: $n$ tiene al menos divisores $\{1, 2, k, n\}$ → al menos 3 divisores

### Paso 4: Números pares no son primos (excepto 2)

En cualquier caso, un número par $n > 2$ tiene más de dos divisores:
- Siempre tiene $1$ y $n$ como divisores
- Siempre tiene $2$ como divisor adicional (ya que es par)

Por lo tanto, ningún número par mayor que 2 puede ser primo.

### Paso 5: Conclusión

El único número par que es primo es $2$ (cuyos únicos divisores son $1$ y $2$).

Todos los demás primos deben ser impares.

$$\therefore \text{Si } p \text{ es primo y } p > 2, \text{ entonces } p \text{ es impar.}$$

---

## Verificación

Verifiquemos con los primeros números primos mayores que 2:

| Primo $p$ | ¿Es impar? | $p = 2k+1$ |
|-----------|------------|------------|
| 3 | Sí ✓ | $3 = 2(1) + 1$ |
| 5 | Sí ✓ | $5 = 2(2) + 1$ |
| 7 | Sí ✓ | $7 = 2(3) + 1$ |
| 11 | Sí ✓ | $11 = 2(5) + 1$ |
| 13 | Sí ✓ | $13 = 2(6) + 1$ |
| 17 | Sí ✓ | $17 = 2(8) + 1$ |
| 19 | Sí ✓ | $19 = 2(9) + 1$ |
| 23 | Sí ✓ | $23 = 2(11) + 1$ |

Todos los primos mayores que 2 son impares. ✓

---

## Respuesta Final

**Si $p$ es primo y $p > 2$, entonces $p$ es impar.**

El número 2 es el único primo par. Esto se debe a que cualquier otro número par tiene a 2 como divisor, lo que impide que sea primo (tendría más de dos divisores).

---

> 📚 Volver a: [FUN-02-Problemas](../../problems/FUN-02-Problemas.md)
