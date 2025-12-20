<!--
content_type: problems
topic: EDO Numéricas
difficulty_range: básico a avanzado
total_problems: 30
---
-->

# Problemas: Solución Numérica de EDO

---

## Sección 1: Método de Euler

### Problema 1.1
Usa el método de Euler con $h = 0.1$ para aproximar $y(0.5)$ si:
$$y' = 2xy, \quad y(0) = 1$$
Compara con la solución exacta $y = e^{x^2}$.

### Problema 1.2
Resuelve $y' = y - x$, $y(0) = 2$ en $[0, 1]$ con $h = 0.2$ usando Euler. Calcula errores en cada paso.

### Problema 1.3
Para $y' = -2y$, $y(0) = 1$:
a) Aplica Euler con $h = 0.5$ y $h = 0.25$
b) ¿Qué método es más preciso?
c) Verifica la condición de estabilidad

### Problema 1.4
Un tanque con 100 L de salmuera con 5 kg de sal tiene entrada de agua pura a 3 L/min y salida a 3 L/min. Si $y(t)$ es la cantidad de sal en el tiempo $t$:
$$y' = -0.03y, \quad y(0) = 5$$
Usa Euler ($h = 5$ min) para encontrar $y(30)$.

### Problema 1.5
Implementa el método de Euler implícito para $y' = -10y$, $y(0) = 1$ con $h = 0.3$. ¿Por qué es estable cuando Euler explícito no lo es?

---

## Sección 2: Método de Heun

### Problema 2.1
Aplica el método de Heun con $h = 0.2$ para resolver:
$$y' = x^2 + y, \quad y(0) = 1$$
Calcula $y(0.4)$ y compara con Euler.

### Problema 2.2
Resuelve $y' = xy$, $y(1) = 1$ en $[1, 2]$ usando Heun con $h = 0.25$.

### Problema 2.3
Un proyectil vertical satisface $v' = -g - kv^2/m$ con $g = 9.8$, $k = 0.01$, $m = 1$ kg y $v(0) = 50$ m/s. Usa Heun ($h = 0.5$) para encontrar $v(2)$.

### Problema 2.4
Compara los errores de Euler y Heun para:
$$y' = \cos(x) - y, \quad y(0) = 0$$
con $h = 0.1$ en $[0, 1]$. ¿Cuál es la razón de errores?

---

## Sección 3: Runge-Kutta

### Problema 3.1
Usa RK4 con $h = 0.2$ para resolver:
$$y' = y - x^2 + 1, \quad y(0) = 0.5$$
Compara $y(1)$ con la solución exacta $y = x^2 + 2x + 1 - 0.5e^x$.

### Problema 3.2
Resuelve con RK4 ($h = 0.1$):
$$y' = 3y + e^{2x}, \quad y(0) = 1$$

### Problema 3.3
Aplica RK2 (punto medio) y RK4 a $y' = \sin(y)$, $y(0) = 1$ con $h = 0.2$. Calcula $y(1)$ con ambos métodos.

### Problema 3.4
Un circuito RL tiene $L\frac{di}{dt} + Ri = V$ con $L = 2$ H, $R = 4$ Ω, $V = 12$ V e $i(0) = 0$. Usa RK4 ($h = 0.1$) para encontrar $i(1)$.

### Problema 3.5
Demuestra que RK4 integra exactamente el polinomio $y' = 1 + 2x + 3x^2 + 4x^3$ con $y(0) = 0$ usando cualquier tamaño de paso $h$.

---

## Sección 4: Métodos Multipaso

### Problema 4.1
Dados los valores iniciales (de RK4) para $y' = y - x$, $y(0) = 2$:
- $y_0 = 2$, $y_1 = 2.0103$, $y_2 = 2.0428$, $y_3 = 2.0997$

Usa Adams-Bashforth de 4 pasos con $h = 0.1$ para calcular $y_4$ y $y_5$.

### Problema 4.2
Aplica el método predictor-corrector (AB4-AM3) al problema:
$$y' = x + y, \quad y(0) = 1$$
con $h = 0.1$. Calcula $y(0.5)$.

### Problema 4.3
Compara la eficiencia de RK4 vs Adams-Bashforth 4 para resolver:
$$y' = -y, \quad y(0) = 1$$
en $[0, 10]$ con $h = 0.1$. ¿Cuántas evaluaciones de $f$ requiere cada método?

---

## Sección 5: Sistemas de EDO

### Problema 5.1
Convierte a sistema de primer orden y resuelve con Euler ($h = 0.1$):
$$y'' + y = 0, \quad y(0) = 1, \; y'(0) = 0$$
Calcula $y(0.3)$ y compara con $\cos(0.3)$.

### Problema 5.2
Resuelve el sistema con RK4 ($h = 0.2$):
$$x' = x - y, \quad y' = x + y$$
$$x(0) = 1, \quad y(0) = 0$$
Calcula $(x(0.4), y(0.4))$.

### Problema 5.3
El modelo depredador-presa de Lotka-Volterra:
$$x' = 0.4x - 0.01xy$$
$$y' = -0.3y + 0.005xy$$
con $x(0) = 50$ (presas) e $y(0) = 20$ (depredadores). Usa RK4 ($h = 0.5$) para simular hasta $t = 10$.

### Problema 5.4
Un péndulo simple satisface $\theta'' + \sin\theta = 0$ con $\theta(0) = 0.5$ rad y $\theta'(0) = 0$. Resuelve con RK4 ($h = 0.1$) hasta $t = 2$.

### Problema 5.5
Resuelve la ecuación de Van der Pol:
$$y'' - \mu(1-y^2)y' + y = 0, \quad \mu = 1$$
con $y(0) = 2$, $y'(0) = 0$ usando RK4 ($h = 0.1$) hasta $t = 10$.

---

## Sección 6: Análisis de Error y Estabilidad

### Problema 6.1
Para $y' = -5y$, $y(0) = 1$:
a) Determina el tamaño de paso máximo para estabilidad con Euler
b) Verifica experimentalmente con $h = 0.3$ y $h = 0.5$

### Problema 6.2
Usa extrapolación de Richardson: si Euler con $h = 0.1$ da $y(1) = 2.5937$ y con $h = 0.05$ da $y(1) = 2.6408$, estima el valor exacto.

### Problema 6.3
Para RK4 aplicado a $y' = y$, $y(0) = 1$:
a) Calcula $y(1)$ con $h = 0.2$ y $h = 0.1$
b) Estima el error usando la fórmula $E \approx \frac{y_{h/2} - y_h}{15}$

### Problema 6.4
La ecuación $y' = -1000y + 3000 - 2000e^{-x}$ es rígida. Verifica que:
a) Euler con $h = 0.001$ diverge
b) Euler con $h = 0.0001$ converge
c) Euler implícito con $h = 0.1$ converge

---

## Sección 7: Problemas Aplicados

### Problema 7.1 (Enfriamiento de Newton)
Un objeto a 90°C se coloca en ambiente a 20°C. Si $T' = -0.1(T - 20)$, usa RK4 ($h = 1$ min) para determinar cuándo $T = 50°C$.

### Problema 7.2 (Crecimiento logístico)
Una población sigue $P' = 0.1P(1 - P/1000)$ con $P(0) = 100$. Simula con RK4 ($h = 1$) hasta $t = 50$ y encuentra cuándo $P = 500$.

### Problema 7.3 (Caída libre con resistencia)
Un paracaidista de 80 kg cae con $v' = 9.8 - 0.005v^2$, $v(0) = 0$. Usa RK4 ($h = 0.5$) para:
a) Encontrar $v(10)$
b) Estimar la velocidad terminal

### Problema 7.4 (Cinética química)
En una reacción de segundo orden: $c' = -kc^2$ con $k = 0.5$ y $c(0) = 2$ mol/L. Calcula $c(5)$ con RK4.

### Problema 7.5 (Oscilador amortiguado)
$$y'' + 0.5y' + 4y = 0, \quad y(0) = 2, \; y'(0) = 0$$
Grafica la solución en $[0, 10]$ usando RK4 ($h = 0.1$).

---

## Sección 8: Problemas de Diseño

### Problema 8.1
Implementa un algoritmo RK adaptativo que ajuste $h$ automáticamente para mantener error local menor que $10^{-6}$.

### Problema 8.2
Diseña un programa que compare automáticamente Euler, Heun y RK4, mostrando errores y número de evaluaciones.

### Problema 8.3
El método de Runge-Kutta-Fehlberg (RKF45) calcula:
$$y_{n+1}^{(4)} = y_n + \frac{h}{360}(90k_1 + 224k_3 + 64k_4 - 10k_5)$$
$$y_{n+1}^{(5)} = y_n + \frac{h}{720}(180k_1 + 448k_3 + 90k_4 + 56k_5 - 54k_6)$$
Implementa y aplica a $y' = y$, $y(0) = 1$ con tolerancia $10^{-8}$.
