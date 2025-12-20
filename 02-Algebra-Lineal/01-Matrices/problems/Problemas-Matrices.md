<!--
content_type: problems
format: unlabeled_list
---
-->

# Problemas de Matrices

---

## 1.1-1.2 Definición y Tipos

### Nivel Básico ★

1. Dada $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$, determinar: (a) dimensiones, (b) $a_{12}$, (c) $a_{23}$.

2. Identificar el tipo de cada matriz:
   - $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$
   - $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix}$
   - $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$

3. Escribir la matriz identidad $I_4$.

---

## 1.3 Operaciones Básicas

### Nivel Básico ★

4. Calcular $A + B$ donde $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ y $B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$.

5. Calcular $3A - 2B$ con las matrices del problema anterior.

6. Si $A = \begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix}$, hallar $2A$.

### Nivel Intermedio ★★

7. Resolver para $X$: $2X + A = B$ donde $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, $B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$.

8. Si $A + B = \begin{pmatrix} 5 & 3 \\ 2 & 7 \end{pmatrix}$ y $A - B = \begin{pmatrix} 1 & 1 \\ 0 & 3 \end{pmatrix}$, hallar $A$ y $B$.

---

## 1.4 Multiplicación de Matrices

### Nivel Básico ★

9. Calcular $AB$ donde $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ y $B = \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix}$.

10. Calcular $BA$ con las matrices del problema anterior. ¿Es igual a $AB$?

11. Calcular $\begin{pmatrix} 1 & 2 & 3 \end{pmatrix} \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}$.

12. Calcular $\begin{pmatrix} 1 \\ 2 \end{pmatrix} \begin{pmatrix} 3 & 4 \end{pmatrix}$.

### Nivel Intermedio ★★

13. Si $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$, calcular $A^2$ y $A^3$.

14. Verificar que $AI = IA = A$ para $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.

15. Calcular $\begin{pmatrix} 1 & 0 & 2 \\ 3 & 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \\ 4 & 0 \end{pmatrix}$.

### Nivel Avanzado ★★★

16. Si $A^2 = A$, demostrar que $(I - A)^2 = I - A$.

17. Encontrar todas las matrices $2 \times 2$ que conmutan con $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

---

## 1.5 Transpuesta

### Nivel Básico ★

18. Hallar $A^T$ para $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$.

19. Verificar que $(A^T)^T = A$ para $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix}$.

20. Determinar si cada matriz es simétrica, antisimétrica o ninguna:
   - $\begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}$
   - $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$
   - $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$

### Nivel Intermedio ★★

21. Verificar que $(AB)^T = B^T A^T$ para $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, $B = \begin{pmatrix} 0 & 1 \\ 2 & 3 \end{pmatrix}$.

22. Demostrar que $A + A^T$ es simétrica para cualquier matriz cuadrada $A$.

23. Expresar $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ como suma de matriz simétrica y antisimétrica.

---

## 1.6 Matriz Inversa

### Nivel Básico ★

24. Hallar la inversa de $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$.

25. Hallar la inversa de $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.

26. Verificar que $AA^{-1} = I$ para el resultado del problema anterior.

### Nivel Intermedio ★★

27. Determinar si existe la inversa: $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$.

28. Usar Gauss-Jordan para encontrar la inversa de $A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{pmatrix}$.

29. Si $A$ es invertible, resolver $AX = B$ donde $B = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ y $A = \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix}$.

### Nivel Avanzado ★★★

30. Demostrar que si $AB = I$, entonces $BA = I$ (para matrices cuadradas).

31. Si $A^2 = I$, demostrar que $A$ es su propia inversa.

32. Encontrar la inversa de $\begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix}$.
