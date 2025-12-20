<!--
content_type: methods
format: step_by_step
---
-->

# Métodos para Sistemas de Ecuaciones Lineales

---

## Método 1: Eliminación Gaussiana

**Pasos:**
1. Escribir la matriz aumentada $(A|b)$.
2. Hacer ceros debajo de la diagonal (forma REF).
3. Resolver por sustitución hacia atrás.

**Ejemplo:** $\begin{cases} x + 2y + z = 9 \\ 2x - y + 3z = 8 \\ 3x + y - z = 3 \end{cases}$

$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 9 \\ 2 & -1 & 3 & 8 \\ 3 & 1 & -1 & 3 \end{array}\right)$$

$R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - 3R_1$:
$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 9 \\ 0 & -5 & 1 & -10 \\ 0 & -5 & -4 & -24 \end{array}\right)$$

$R_3 \leftarrow R_3 - R_2$:
$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 9 \\ 0 & -5 & 1 & -10 \\ 0 & 0 & -5 & -14 \end{array}\right)$$

Sustitución: $z = 14/5$, $y = 2 - z/5 = 2 - 14/25 = 36/25$...

---

## Método 2: Gauss-Jordan (RREF)

**Pasos:**
1. Aplicar eliminación gaussiana.
2. Hacer pivotes = 1.
3. Hacer ceros arriba de cada pivote.
4. Leer solución directamente.

**Ejemplo:** Continuando el anterior hasta RREF:
$$\left(\begin{array}{ccc|c} 1 & 0 & 0 & x_1 \\ 0 & 1 & 0 & x_2 \\ 0 & 0 & 1 & x_3 \end{array}\right)$$

---

## Método 3: Determinar Tipo de Sistema

**Pasos:**
1. Reducir a REF.
2. Calcular $r_A = \text{rango}(A)$ y $r_{A|b} = \text{rango}(A|b)$.
3. Comparar con $n$ (número de variables).

**Casos:**
- $r_A < r_{A|b}$: Sin solución (fila tipo $[0 \, 0 \, \cdots \, 0 \, | \, c]$ con $c \neq 0$)
- $r_A = r_{A|b} = n$: Solución única
- $r_A = r_{A|b} < n$: Infinitas soluciones

---

## Método 4: Sistemas con Infinitas Soluciones

**Pasos:**
1. Reducir a RREF.
2. Identificar variables básicas (con pivote) y libres (sin pivote).
3. Expresar variables básicas en términos de las libres.
4. Escribir solución paramétrica.

**Ejemplo:**
$$\left(\begin{array}{ccc|c} 1 & 0 & 2 & 3 \\ 0 & 1 & -1 & 2 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

$x_3 = t$ (libre)
$x_1 = 3 - 2t$
$x_2 = 2 + t$

$$\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \\ 0 \end{pmatrix} + t\begin{pmatrix} -2 \\ 1 \\ 1 \end{pmatrix}$$

---

## Método 5: Sistemas Homogéneos

**Para $Ax = 0$:**
1. Reducir $A$ a RREF.
2. Si $\text{rango}(A) = n$: solo solución trivial $x = 0$.
3. Si $\text{rango}(A) < n$: expresar en forma paramétrica.

**Ejemplo:**
$$A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \end{pmatrix} \rightarrow \begin{pmatrix} 1 & 2 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$

$x_2 = s$, $x_3 = t$ (libres)
$x_1 = -2s - t$

$$x = s\begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix} + t\begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}$$

---

## Método 6: Usar Matriz Inversa

**Para sistemas $n \times n$ con $\det(A) \neq 0$:**

$$Ax = b \Rightarrow x = A^{-1}b$$

**Útil cuando:** Se resuelven múltiples sistemas con la misma $A$ pero diferentes $b$.

---

## Método 7: Regla de Cramer

**Para sistemas $n \times n$ con $\det(A) \neq 0$:**

$$x_i = \frac{\det(A_i)}{\det(A)}$$

donde $A_i$ tiene la columna $i$ reemplazada por $b$.

---

## Método 8: Verificación

**Siempre verificar** sustituyendo la solución en el sistema original:

Para $x = (x_1, x_2, x_3)$, calcular $Ax$ y comparar con $b$.
