<!--
::METADATA::
type: theory
status: active
-->

# Teoría de Sistemas de Ecuaciones Lineales

---

## 3.1 Forma Matricial

### Sistema de Ecuaciones Lineales

Un sistema de $m$ ecuaciones con $n$ incógnitas:
$$\begin{cases} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\ \vdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m \end{cases}$$

### Notación Matricial

$$Ax = b$$

donde:
- $A$ = [matriz](../../../glossary.md#matriz) de coeficientes $(m \times n)$
- $x$ = [vector](../../../glossary.md#vector) de incógnitas $(n \times 1)$
- $b$ = vector de términos independientes $(m \times 1)$

### Matriz Aumentada

$$(A | b) = \left(\begin{array}{cccc|c} a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\ a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} & b_m \end{array}\right)$$

---

## 3.2 Eliminación Gaussiana

### Operaciones Elementales de Fila

1. **Intercambio:** $R_i \leftrightarrow R_j$
2. **Escalamiento:** $R_i \leftarrow kR_i$ con $k \neq 0$
3. **Reemplazo:** $R_i \leftarrow R_i + kR_j$

Estas operaciones no cambian el conjunto solución.

### Algoritmo de Eliminación

1. Comenzar con la matriz aumentada $(A | b)$.
2. Usar operaciones elementales para crear ceros debajo de la diagonal.
3. Obtener forma escalonada.
4. Resolver por [sustitución](../../../glossary.md#sustitución) hacia atrás.

---

## 3.3 Forma Escalonada

### Forma Escalonada por Filas (REF)

Una matriz está en REF si:
1. Todas las filas de ceros están al final.
2. El primer elemento no nulo de cada fila (pivote) está a la derecha del pivote de la fila superior.
3. Todos los elementos debajo de un pivote son cero.

**Ejemplo:**
$$\begin{pmatrix} 2 & 1 & 3 & 4 \\ 0 & 3 & 1 & 2 \\ 0 & 0 & 0 & 5 \end{pmatrix}$$

### Forma Escalonada Reducida (RREF)

Además de REF:
4. Cada pivote es 1.
5. Cada pivote es el único elemento no nulo en su columna.

**Ejemplo:**
$$\begin{pmatrix} 1 & 0 & 2 & 0 \\ 0 & 1 & -1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

---

## 3.4 Clasificación de Soluciones

### Teorema de Rouché-Frobenius

Sea $Ax = b$ un sistema con matriz de coeficientes $A$ y matriz aumentada $(A|b)$:

| $\text{rango}(A)$ vs $\text{rango}(A|b)$ | Tipo de Sistema |
|------------------------------------------|-----------------|
| $\text{rango}(A) < \text{rango}(A|b)$ | **Incompatible** (sin solución) |
| $\text{rango}(A) = \text{rango}(A|b) = n$ | **Compatible determinado** (solución única) |
| $\text{rango}(A) = \text{rango}(A|b) < n$ | **Compatible indeterminado** (infinitas soluciones) |

### Variables Libres y Básicas

- **Variables básicas:** corresponden a columnas con pivote
- **Variables libres:** corresponden a columnas sin pivote

Número de variables libres = $n - \text{rango}(A)$

---

## 3.5 Rango de una Matriz

### Definición

El **rango** de una matriz $A$ es:
- El número de pivotes en su forma escalonada
- El número de filas no nulas en REF
- La [dimensión](../../../glossary.md#dimensión) del espacio fila (o columna)

### Propiedades

1. $\text{rango}(A) \leq \min(m, n)$
2. $\text{rango}(A) = \text{rango}(A^T)$
3. $\text{rango}(AB) \leq \min(\text{rango}(A), \text{rango}(B))$

### Cálculo

Reducir a REF y contar pivotes.

---

## 3.6 Sistemas Homogéneos

### Definición

Un sistema es **homogéneo** si $b = 0$:
$$Ax = 0$$

### Propiedades

1. **Siempre tiene solución:** $x = 0$ (solución [trivial](../../../glossary.md#trivial))
2. **Solución no trivial existe** $\Leftrightarrow \text{rango}(A) < n$
3. Si $m < n$ (más incógnitas que ecuaciones), siempre hay solución no trivial

### Espacio Nulo

El conjunto de todas las soluciones de $Ax = 0$ forma un [subespacio](../../../glossary.md#subespacio) vectorial llamado **espacio nulo** o **kernel** de $A$:
$$\text{Nul}(A) = \{x : Ax = 0\}$$

**Dimensión:** $\dim(\text{Nul}(A)) = n - \text{rango}(A)$

### Solución General

Si $Ax = b$ tiene [solución particular](../../../glossary.md#solución-particular) $x_p$ y $Ax = 0$ tiene [solución general](../../../glossary.md#solución-general) $x_h$:
$$x = x_p + x_h$$
