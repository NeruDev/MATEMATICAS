# Problemas — Funciones de varias variables

---

## Nivel Básico

### Dominio y curvas de nivel
1) Encuentra el dominio de $f(x, y) = \sqrt{9 - x^2 - y^2}$.

2) Determina el dominio de $f(x, y) = \ln(x - y) + \frac{1}{xy}$.

3) Dibuja las curvas de nivel $k = 0, 1, 4, 9$ de $f(x, y) = x^2 + y^2$.

4) Describe las curvas de nivel de $f(x, y) = x - 2y$.

### Derivadas parciales
5) Calcula $f_x$ y $f_y$ para $f(x, y) = x^2 y + 3y^2$.

6) Si $f(x, y) = e^{x+2y}$, encuentra $f_x$, $f_y$ y $f_{xy}$.

7) Para $f(x, y) = \sin(xy)$, calcula todas las derivadas parciales de primer orden.

8) Evalúa $f_x(1, 2)$ y $f_y(1, 2)$ si $f(x, y) = x^3 y^2 - 4xy + 5$.

---

## Nivel Intermedio

### Límites
9) Demuestra que $\lim_{(x,y) \to (0,0)} \frac{xy}{x^2 + y^2}$ no existe.

10) Calcula $\lim_{(x,y) \to (0,0)} \frac{x^2 y}{x^4 + y^2}$ si existe.

11) Determina si existe $\lim_{(x,y) \to (0,0)} \frac{\sin(x^2 + y^2)}{x^2 + y^2}$.

12) Evalúa $\lim_{(x,y) \to (1,2)} \frac{x^2 - y + 2}{x + y - 3}$.

### Diferencial y aproximación
13) Para $f(x, y) = \ln(x^2 + y^2)$ en $(1, 1)$, aproxima $f(1.05, 0.95)$ usando el diferencial.

14) Usa el diferencial para aproximar $\sqrt{(2.01)^2 + (1.98)^2}$.

15) Si $V = \pi r^2 h$, estima el error en $V$ cuando $r = 2 \pm 0.1$ y $h = 5 \pm 0.2$.

### Regla de la cadena
16) Si $z = x^2 y$ con $x = \sin t$, $y = e^t$, encuentra $\frac{dz}{dt}$.

17) Para $w = xy + yz + xz$ con $x = t$, $y = t^2$, $z = t^3$, calcula $\frac{dw}{dt}$.

18) Si $z = e^{xy}$ con $x = s + t$, $y = s - t$, encuentra $\frac{\partial z}{\partial s}$ y $\frac{\partial z}{\partial t}$.

---

## Nivel Avanzado

### Gradiente y derivada direccional
19) Para $f(x, y) = e^{xy}$, calcula $\nabla f(0, 1)$ y $D_{\mathbf{u}}f$ en $(0, 1)$ hacia $\mathbf{u} = \langle 3, 4 \rangle$.

20) Encuentra la dirección de máximo crecimiento de $f(x, y) = x^2 - xy + y^2$ en $(1, 1)$.

21) Calcula la derivada direccional de $f(x, y, z) = xyz$ en $(1, 2, 3)$ en dirección a $(2, 4, 5)$.

22) Si $f(x, y) = x^2 + y^2$, ¿en qué dirección desde $(3, 4)$ la derivada direccional es cero?

### Extremos y optimización
23) Encuentra y clasifica los puntos críticos de $f(x, y) = x^3 + y^3 - 3xy$.

24) Halla los extremos locales de $f(x, y) = x^4 + y^4 - 4xy + 1$.

25) Encuentra los puntos críticos de $f(x, y) = x^2 + xy + y^2 - 6x - 3y$.

26) Clasifica el punto crítico de $f(x, y) = x^2 y^2$ en el origen.

### Extremos en regiones cerradas
27) Encuentra el máximo y mínimo absoluto de $f(x, y) = x^2 + y^2 - 2x$ en el disco $x^2 + y^2 \leq 4$.

28) Halla los extremos de $f(x, y) = xy$ en el triángulo con vértices $(0, 0)$, $(2, 0)$, $(0, 3)$.

29) Encuentra el máximo de $f(x, y) = x + 2y$ sujeto a $x^2 + y^2 = 5$.

### Derivación implícita
30) Si $x^2 + y^2 + z^2 = 1$, calcula $\frac{\partial z}{\partial x}$ y $\frac{\partial z}{\partial y}$.

31) Para $xe^y + ye^z + ze^x = 0$, encuentra $\frac{\partial z}{\partial x}$ en $(0, 0, 0)$.

---

## Problemas de Aplicación

32) **Temperatura**: La temperatura en un punto $(x, y)$ de una placa es $T(x, y) = 100 - x^2 - 2y^2$. Encuentra la dirección en la que la temperatura disminuye más rápidamente desde $(1, 1)$.

33) **Economía**: El costo de producir $x$ unidades del producto A y $y$ unidades del producto B es $C(x, y) = 2x^2 + xy + y^2 - 10x - 8y + 50$. Encuentra la producción que minimiza el costo.

34) **Física**: El potencial eléctrico en $(x, y)$ es $V(x, y) = \frac{k}{\sqrt{x^2 + y^2}}$. Encuentra el campo eléctrico $\mathbf{E} = -\nabla V$.

35) **Geometría**: Encuentra la distancia mínima del origen al plano $2x + 3y + z = 14$ usando el método de puntos críticos.

36) **Optimización de caja**: Una caja rectangular sin tapa tiene volumen $32$ m³. Encuentra las dimensiones que minimizan el área de material usado.
