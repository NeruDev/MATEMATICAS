<!--
::METADATA::
type: solution
topic_id: al-01-matrices
file_id: prob-24-solucion-metodo
problem_ref: [Prob-24]
method: formula-inversa-2x2
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Inversa por fórmula 2×2

**Método aplicado:** Fórmula $A^{-1} = \frac{1}{\det(A)}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$

**Paso 1: Calcular el [determinante](../../../..](../../../../glossary.md)#determinante)**
$$\det(A) = 2(3) - 1(5) = 6 - 5 = 1$$

Como $\det(A) \neq 0$, la [matriz](../../../..](../../../../glossary.md)#matriz) es invertible.

**Paso 2: Aplicar la fórmula**
$$A^{-1} = \frac{1}{1}\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$$

**Verificación:**
$$AA^{-1} = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} 6-5 & -2+2 \\ 15-15 & -5+6 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$ ✓

**Respuesta:**

$$A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$$
