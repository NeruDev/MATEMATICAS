<!--
content_type: problems
format: unlabeled_list
---
-->

# Problemas de Determinantes

---

## 2.1 Determinantes $2 \times 2$ y $3 \times 3$

### Nivel Básico ★

1. $\begin{vmatrix} 2 & 3 \\ 1 & 4 \end{vmatrix}$

2. $\begin{vmatrix} 5 & -2 \\ 3 & 7 \end{vmatrix}$

3. $\begin{vmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{vmatrix}$

4. $\begin{vmatrix} 2 & 0 & 1 \\ 3 & 1 & 2 \\ 1 & 0 & 4 \end{vmatrix}$

### Nivel Intermedio ★★

5. $\begin{vmatrix} 1 & 2 & 3 \\ 0 & 1 & 2 \\ 0 & 0 & 3 \end{vmatrix}$

6. $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$ en términos de $a, b, c, d$

---

## 2.2 Propiedades

### Nivel Básico ★

7. Si $\det(A) = 3$ y $\det(B) = 2$, hallar $\det(AB)$.

8. Si $\det(A) = 4$, hallar $\det(A^{-1})$.

9. Si $\det(A) = 2$ y $A$ es $3 \times 3$, hallar $\det(3A)$.

### Nivel Intermedio ★★

10. Usando propiedades, calcular $\begin{vmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 1 & 1 \end{vmatrix}$ sin expandir.

11. Si intercambiamos dos filas de $A$ para obtener $B$, ¿cuál es la relación entre $\det(A)$ y $\det(B)$?

12. Demostrar que $\det(A^T) = \det(A)$ para $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.

---

## 2.3-2.4 Cofactores y Expansión

### Nivel Básico ★

13. Hallar todos los cofactores de $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.

14. Calcular $M_{11}$ y $C_{11}$ de $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$.

### Nivel Intermedio ★★

15. Calcular el determinante por expansión de la primera fila:
$$\begin{vmatrix} 2 & 1 & 3 \\ 0 & 4 & 1 \\ 5 & 2 & 0 \end{vmatrix}$$

16. Calcular el determinante por expansión de la columna 2:
$$\begin{vmatrix} 1 & 0 & 2 \\ 3 & 0 & 4 \\ 5 & 1 & 6 \end{vmatrix}$$

### Nivel Avanzado ★★★

17. Calcular: $\begin{vmatrix} 1 & 2 & 3 & 4 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 1 \end{vmatrix}$

---

## 2.5 Matriz Adjunta

### Nivel Básico ★

18. Hallar $\text{adj}(A)$ para $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$.

19. Usar la fórmula $A^{-1} = \frac{1}{\det(A)}\text{adj}(A)$ para encontrar la inversa de $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.

### Nivel Intermedio ★★

20. Hallar $\text{adj}(A)$ para $A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{pmatrix}$.

21. Verificar que $A \cdot \text{adj}(A) = \det(A) \cdot I$ para $A = \begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix}$.

---

## 2.6 Regla de Cramer

### Nivel Básico ★

22. Resolver por Cramer: $\begin{cases} 2x + y = 5 \\ x + 3y = 5 \end{cases}$

23. Resolver por Cramer: $\begin{cases} 3x - 2y = 7 \\ x + y = 4 \end{cases}$

### Nivel Intermedio ★★

24. Resolver por Cramer:
$$\begin{cases} x + y + z = 6 \\ x - y + z = 2 \\ 2x + y - z = 1 \end{cases}$$

25. ¿Para qué valor de $k$ el sistema NO tiene solución única por Cramer?
$$\begin{cases} kx + y = 1 \\ 2x + ky = 2 \end{cases}$$

---

## Problemas de Aplicación

### Nivel Avanzado ★★★

26. Demostrar que el área del triángulo con vértices $(x_1,y_1)$, $(x_2,y_2)$, $(x_3,y_3)$ es:
$$\text{Área} = \frac{1}{2}\left|\begin{vmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{vmatrix}\right|$$

27. Si $A$ es una matriz $n \times n$ y $\det(A) = 5$, hallar $\det(A^3)$.

28. Probar que si $A^2 = A$, entonces $\det(A) = 0$ o $\det(A) = 1$.
