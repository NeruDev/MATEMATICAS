<!--
::METADATA::
type: solution
topic_id: al-01-matrices
file_id: prob-28-solucion-metodo
problem_ref: [Prob-28]
method: gauss-jordan
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Inversa por Gauss-Jordan 3×3

**Método aplicado:** Eliminación de Gauss-Jordan

**Paso 1: Formar la matriz aumentada [A|I]**
$$\left(\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 0 & 0 & 1 \end{array}\right)$$

**Paso 2: $R_3 \leftarrow R_3 - R_1$**
$$\left(\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 1 & -1 & -1 & 0 & 1 \end{array}\right)$$

**Paso 3: $R_3 \leftarrow R_3 - R_2$**
$$\left(\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & -2 & -1 & -1 & 1 \end{array}\right)$$

**Paso 4: $R_3 \leftarrow -\frac{1}{2}R_3$**
$$\left(\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & 1/2 & 1/2 & -1/2 \end{array}\right)$$

**Paso 5: $R_1 \leftarrow R_1 - R_3$, $R_2 \leftarrow R_2 - R_3$**
$$\left(\begin{array}{ccc|ccc} 1 & 0 & 0 & 1/2 & -1/2 & 1/2 \\ 0 & 1 & 0 & -1/2 & 1/2 & 1/2 \\ 0 & 0 & 1 & 1/2 & 1/2 & -1/2 \end{array}\right)$$

**Respuesta:**

$$A^{-1} = \frac{1}{2}\begin{pmatrix} 1 & -1 & 1 \\ -1 & 1 & 1 \\ 1 & 1 & -1 \end{pmatrix}$$
