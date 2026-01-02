<!--
::METADATA::
type: solution
topic_id: al-01-matrices
file_id: prob-13-solucion-metodo
problem_ref: [Prob-13]
method: potencias-de-matrices
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../glossary.md)

---

# Solución: Potencias de matrices

**Método aplicado:** Multiplicación sucesiva

**Paso 1: Calcular A²**
$$A^2 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$$

- $(A^2)_{11} = 1(1) + 2(0) = 1$
- $(A^2)_{12} = 1(2) + 2(1) = 4$
- $(A^2)_{21} = 0(1) + 1(0) = 0$
- $(A^2)_{22} = 0(2) + 1(1) = 1$

$$A^2 = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$$

**Paso 2: Calcular A³**
$$A^3 = A^2 \cdot A = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$$

$$A^3 = \begin{pmatrix} 1 & 6 \\ 0 & 1 \end{pmatrix}$$

**Respuesta:**

$$A^2 = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}, \quad A^3 = \begin{pmatrix} 1 & 6 \\ 0 & 1 \end{pmatrix}$$

**Patrón observado:** $A^n = \begin{pmatrix} 1 & 2n \\ 0 & 1 \end{pmatrix}$
