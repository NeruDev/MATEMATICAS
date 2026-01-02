<!--
::METADATA::
type: cheat-sheet
topic_id: al-03-sistemas-lineales
file_id: AL-03-Resumen-Formulas
status: stable
audience: student
-->

> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Resumen de Fórmulas: Sistemas de Ecuaciones Lineales

## Representación matricial

Sistema de $m$ ecuaciones con $n$ incógnitas:
$$Ax = b$$

donde:
- $A$: [matriz](../../glossary.md#vector) de incógnitas ($n \times 1$)
- $b$: [vector](../../glossary.md#vector) de términos independientes ($m \times 1$)

**Matriz aumentada**: $[A | b]$

## Operaciones elementales de fila

| Operación | Notación | Efecto |
|-----------|----------|--------|
| Intercambiar filas | $F_i \leftrightarrow F_j$ | Cambia [orden](../../glossary.md#combinacion-lineal) |

## Formas escalonadas

### Forma escalonada por filas (REF)
1. Filas de ceros al final
2. Pivote de cada fila a la derecha del anterior
3. Ceros debajo de cada pivote

### Forma escalonada reducida (RREF)
1. Todo lo de REF
2. Pivotes iguales a 1
3. Ceros arriba y abajo de cada pivote

## Algoritmo de Gauss-Jordan

1. Formar [matriz](../../glossary.md#matriz) aumentada $[A|b]$
2. Reducir a RREF usando operaciones elementales
3. Leer solución del sistema reducido

## Clasificación de soluciones

| Caso | Condición | Resultado |
|------|-----------|-----------|
| **Compatible determinado** | $\text{rang}(A) = \text{rang}([A|b]) = n$ | Solución única |
| **Compatible indeterminado** | $\text{rang}(A) = \text{rang}([A|b]) < n$ | Infinitas soluciones |
| **Incompatible** | $\text{rang}(A) < \text{rang}([A|b])$ | Sin solución |

## Rango de una matriz

$$\text{rang}(A) = \text{número de pivotes en la forma escalonada}$$

### Teorema de Rouché-Frobenius
El sistema $Ax = b$ es compatible si y solo si:
$$\text{rang}(A) = \text{rang}([A|b])$$

## Sistemas homogéneos

$$Ax = 0$$

### Propiedades
- Siempre tiene solución [trivial](../../glossary.md#solucion-particular) de $Ax = b$
- $x_h$: [solución general](../../glossary.md#regla-de-cramer)**:
$$x_i = \frac{\det(A_i)}{\det(A)}$$

## Variables pivote y libres

En la RREF:
- **Variables pivote**: corresponden a columnas con pivotes
- **Variables libres**: corresponden a columnas sin pivotes

**Solución paramétrica**: expresar variables pivote en términos de variables libres.

## Verificación

Para verificar solución $x^*$:
$$Ax^* = b \quad \checkmark$$
