<!--
::METADATA::
type: solution
topic_id: al-01-matrices
file_id: prob-32-solucion-metodo
problem_ref: [Prob-32]
method: formula-inversa-2x2
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../glossary.md)

---

# Solución: Inversa paramétrica

**Método aplicado:** Fórmula de inversa 2×2

**Paso 1: Calcular el [determinante](../../../../glossary.md#determinante)**
$$\det = 1(1) - a(0) = 1 \neq 0$$

La [matriz](../../../../glossary.md#matriz) es invertible para cualquier valor de $a$.

**Paso 2: Aplicar la fórmula**
Para $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, $A^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$

$$\begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix}^{-1} = \frac{1}{1}\begin{pmatrix} 1 & -a \\ 0 & 1 \end{pmatrix}$$

**Verificación:**
$$\begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & -a \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1+0 & -a+a \\ 0+0 & 0+1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$ ✓

**Respuesta:**

$$\begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix}^{-1} = \begin{pmatrix} 1 & -a \\ 0 & 1 \end{pmatrix}$$
