<!--
::METADATA::
type: solution
topic_id: al-01-matrices
file_id: prob-10-solucion-metodo
problem_ref: [Prob-10]
method: multiplicacion-fila-columna
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: No conmutatividad del producto

**Método aplicado:** Multiplicación fila por columna

**Paso 1: Calcular BA**
$$BA = \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$$

**Paso 2: Elementos de BA**
- $(BA)_{11} = 2(1) + 0(3) = 2$
- $(BA)_{12} = 2(2) + 0(4) = 4$
- $(BA)_{21} = 1(1) + 3(3) = 10$
- $(BA)_{22} = 1(2) + 3(4) = 14$

**Paso 3: Comparar con AB**
$$BA = \begin{pmatrix} 2 & 4 \\ 10 & 14 \end{pmatrix} \quad \text{vs} \quad AB = \begin{pmatrix} 4 & 6 \\ 10 & 12 \end{pmatrix}$$

**Respuesta:**

$$BA = \begin{pmatrix} 2 & 4 \\ 10 & 14 \end{pmatrix}$$

**Conclusión:** $AB \neq BA$. La multiplicación de matrices **no es conmutativa**.
