<!--
::METADATA::
type: solution
topic_id: al-01-matrices
file_id: prob-23-solucion-metodo
problem_ref: [Prob-23]
method: descomposicion-simetrica
status: stable
audience: student
-->

# Solución: Descomposición simétrica-antisimétrica

**Método aplicado:** Fórmulas $S = \frac{1}{2}(A + A^T)$ y $K = \frac{1}{2}(A - A^T)$

**Paso 1: Calcular la [transpuesta](../../../../glossary.md#transpuesta)**
$$A^T = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$$

**Paso 2: Parte simétrica**
$$S = \frac{1}{2}(A + A^T) = \frac{1}{2}\begin{pmatrix} 1+1 & 2+3 \\ 3+2 & 4+4 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 2 & 5 \\ 5 & 8 \end{pmatrix}$$

$$S = \begin{pmatrix} 1 & 5/2 \\ 5/2 & 4 \end{pmatrix}$$

**Paso 3: Parte antisimétrica**
$$K = \frac{1}{2}(A - A^T) = \frac{1}{2}\begin{pmatrix} 1-1 & 2-3 \\ 3-2 & 4-4 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$

$$K = \begin{pmatrix} 0 & -1/2 \\ 1/2 & 0 \end{pmatrix}$$

**Verificación:** 
$$S + K = \begin{pmatrix} 1 & 5/2 \\ 5/2 & 4 \end{pmatrix} + \begin{pmatrix} 0 & -1/2 \\ 1/2 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = A$$ ✓

**Respuesta:**

$$A = \underbrace{\begin{pmatrix} 1 & 5/2 \\ 5/2 & 4 \end{pmatrix}}_{\text{simétrica}} + \underbrace{\begin{pmatrix} 0 & -1/2 \\ 1/2 & 0 \end{pmatrix}}_{\text{antisimétrica}}$$
