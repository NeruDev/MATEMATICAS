<!--
content_type: problems
format: unlabeled_list
---
-->

# Problemas de Sistemas de Ecuaciones Lineales

---

## 3.1-3.2 Forma Matricial y Eliminación

### Nivel Básico ★

1. Escribir en forma matricial $Ax = b$:
$$\begin{cases} 2x + 3y = 7 \\ x - y = 1 \end{cases}$$

2. Resolver por eliminación gaussiana:
$$\begin{cases} x + y = 5 \\ 2x - y = 4 \end{cases}$$

3. Resolver:
$$\begin{cases} x + 2y + z = 6 \\ 2x + y - z = 1 \\ x - y + 2z = 5 \end{cases}$$

### Nivel Intermedio ★★

4. Resolver:
$$\begin{cases} 2x + y - z = 3 \\ x - y + 2z = 0 \\ 3x + 2y + z = 5 \end{cases}$$

5. Resolver y verificar:
$$\begin{cases} x + y + z + w = 10 \\ 2x - y + z = 5 \\ x + 2y - z + w = 4 \\ 3x + y + 2z - w = 9 \end{cases}$$

---

## 3.3 Forma Escalonada

### Nivel Básico ★

6. Llevar a REF:
$$\begin{pmatrix} 1 & 2 & 3 \\ 2 & 5 & 3 \\ 1 & 0 & 8 \end{pmatrix}$$

7. Llevar a RREF:
$$\begin{pmatrix} 1 & 2 & 1 \\ 3 & 8 & 1 \\ 2 & 4 & 3 \end{pmatrix}$$

### Nivel Intermedio ★★

8. ¿Cuál de las siguientes está en REF? ¿En RREF?
   - $\begin{pmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$
   - $\begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & 3 \\ 0 & 0 & 0 \end{pmatrix}$

---

## 3.4 Clasificación de Soluciones

### Nivel Básico ★

9. Clasificar (sin resolver):
$$\begin{cases} x + y = 2 \\ 2x + 2y = 4 \end{cases}$$

10. Clasificar:
$$\begin{cases} x + y = 2 \\ x + y = 3 \end{cases}$$

### Nivel Intermedio ★★

11. ¿Para qué valor de $k$ el sistema tiene infinitas soluciones?
$$\begin{cases} x + ky = 1 \\ 2x + 2y = 2 \end{cases}$$

12. ¿Para qué valor de $k$ el sistema no tiene solución?
$$\begin{cases} x + y + z = 1 \\ x + 2y + 3z = 2 \\ 2x + 3y + kz = 3 \end{cases}$$

13. Clasificar según el valor de $a$:
$$\begin{cases} x + y + z = 1 \\ x + 2y + az = 2 \\ x + 4y + a^2z = 4 \end{cases}$$

---

## 3.5 Rango

### Nivel Básico ★

14. Hallar el rango de $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 1 & 1 \end{pmatrix}$.

15. Hallar el rango de $A = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & 3 \\ 2 & 1 & 7 \end{pmatrix}$.

### Nivel Intermedio ★★

16. ¿Para qué valores de $k$ el rango es menor que 3?
$$A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & k & 2 \\ 1 & 1 & 1 \end{pmatrix}$$

---

## 3.6 Sistemas Homogéneos

### Nivel Básico ★

17. Resolver $Ax = 0$ donde $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$.

18. Resolver:
$$\begin{cases} x + 2y + 3z = 0 \\ 2x + 4y + 6z = 0 \end{cases}$$

### Nivel Intermedio ★★

19. Hallar una base para el espacio nulo de $A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 3 \end{pmatrix}$.

20. ¿Para qué valores de $k$ el sistema homogéneo tiene solución no trivial?
$$\begin{cases} x + y + kz = 0 \\ x + ky + z = 0 \\ kx + y + z = 0 \end{cases}$$

---

## Problemas de Aplicación

### Nivel Avanzado ★★★

21. Un triángulo tiene vértices que satisfacen el sistema. Hallar los vértices:
$$\begin{cases} x + y = 5 \\ x - y = 1 \end{cases}$$

22. Encontrar $a$, $b$, $c$ tal que la parábola $y = ax^2 + bx + c$ pase por $(1, 2)$, $(2, 3)$ y $(3, 6)$.

23. Hallar el polinomio de grado 2 que interpola los puntos $(-1, 4)$, $(0, 1)$, $(2, 7)$.
