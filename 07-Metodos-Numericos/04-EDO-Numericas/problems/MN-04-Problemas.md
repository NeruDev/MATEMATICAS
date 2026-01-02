<!--
::METADATA::
type: problem_set
topic_id: mn-04-[edo](../../../glossary.md#edo)-numericas
file_id: MN-04-Problemas
status: stable
audience: student
total_problems: 30
difficulty_distribution: {basic: 10, intermediate: 12, advanced: 8}
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Problemas: Solución Numérica de EDO

---

## Sección 1: Método de Euler

### [Prob-01] Aproximación de Euler con Comparación Exacta ⭐
Usa el [método de Euler](../../../glossary.md#metodo-de-euler) con $h = 0.1$ para aproximar $y(0.5)$ si:
$$y' = 2xy, \quad y(0) = 1$$
Compara con la solución exacta $y = e^{x^2}$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-01)

---

### [Prob-02] Euler con Cálculo de Errores por Paso ⭐
Resuelve $y' = y - x$, $y(0) = 2$ en $[0, 1]$ con $h = 0.2$ usando Euler. Calcula errores en cada paso.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-02)

---

### [Prob-03] Comparación de Tamaños de Paso y Estabilidad ⭐⭐
Para $y' = -2y$, $y(0) = 1$:
a) Aplica Euler con $h = 0.5$ y $h = 0.25$
b) ¿Qué método es más preciso?
c) Verifica la condición de estabilidad

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-03)

---

### [Prob-04] Modelo de Tanque con Salmuera ⭐⭐
Un tanque con 100 L de salmuera con 5 kg de sal tiene entrada de agua pura a 3 L/min y salida a 3 L/min. Si $y(t)$ es la cantidad de sal en el tiempo $t$:
$$y' = -0.03y, \quad y(0) = 5$$
Usa Euler ($h = 5$ min) para encontrar $y(30)$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-04)

---

### [Prob-05] Euler Implícito y Análisis de Estabilidad ⭐⭐⭐
Implementa el [método de Euler](../../../glossary.md#metodo-de-euler) implícito para $y' = -10y$, $y(0) = 1$ con $h = 0.3$. ¿Por qué es estable cuando Euler explícito no lo es?

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-05)

---

## Sección 2: Método de Heun

### [Prob-06] Método de Heun con Comparación a Euler ⭐
Aplica el [método de Heun](../../../glossary.md#metodo-de-heun) con $h = 0.2$ para resolver:
$$y' = x^2 + y, \quad y(0) = 1$$
Calcula $y(0.4)$ y compara con Euler.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-06)

---

### [Prob-07] Heun en Intervalo Extendido ⭐
Resuelve $y' = xy$, $y(1) = 1$ en $[1, 2]$ usando Heun con $h = 0.25$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-07)

---

### [Prob-08] Proyectil Vertical con Resistencia ⭐⭐
Un proyectil vertical satisface $v' = -g - kv^2/m$ con $g = 9.8$, $k = 0.01$, $m = 1$ kg y $v(0) = 50$ m/s. Usa Heun ($h = 0.5$) para encontrar $v(2)$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-08)

---

### [Prob-09] Comparación de Errores Euler vs Heun ⭐⭐
Compara los errores de Euler y Heun para:
$$y' = \cos(x) - y, \quad y(0) = 0$$
con $h = 0.1$ en $[0, 1]$. ¿Cuál es la razón de errores?

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-09)

---

## Sección 3: Runge-Kutta

### [Prob-10] RK4 con Solución Exacta Conocida ⭐⭐
Usa RK4 con $h = 0.2$ para resolver:
$$y' = y - x^2 + 1, \quad y(0) = 0.5$$
Compara $y(1)$ con la solución exacta $y = x^2 + 2x + 1 - 0.5e^x$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-10)

---

### [Prob-11] RK4 con Término Exponencial ⭐
Resuelve con RK4 ($h = 0.1$):
$$y' = 3y + e^{2x}, \quad y(0) = 1$$

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-11)

---

### [Prob-12] Comparación RK2 vs RK4 ⭐⭐
Aplica RK2 (punto medio) y RK4 a $y' = \sin(y)$, $y(0) = 1$ con $h = 0.2$. Calcula $y(1)$ con ambos métodos.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-12)

---

### [Prob-13] Circuito RL con RK4 ⭐⭐
Un circuito RL tiene $L\frac{di}{dt} + Ri = V$ con $L = 2$ H, $R = 4$ Ω, $V = 12$ V e $i(0) = 0$. Usa RK4 ($h = 0.1$) para encontrar $i(1)$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-13)

---

### [Prob-14] Demostración de Exactitud de RK4 ⭐⭐⭐
Demuestra que RK4 integra exactamente el [polinomio](../../../glossary.md#polinomio) $y' = 1 + 2x + 3x^2 + 4x^3$ con $y(0) = 0$ usando cualquier tamaño de paso $h$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-14)

---

## Sección 4: Métodos Multipaso

### [Prob-15] Adams-Bashforth de 4 Pasos ⭐⭐
Dados los valores iniciales (de RK4) para $y' = y - x$, $y(0) = 2$:
- $y_0 = 2$, $y_1 = 2.0103$, $y_2 = 2.0428$, $y_3 = 2.0997$

Usa Adams-Bashforth de 4 pasos con $h = 0.1$ para calcular $y_4$ y $y_5$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-15)

---

### [Prob-16] Predictor-Corrector AB4-AM3 ⭐⭐⭐
Aplica el método predictor-corrector (AB4-AM3) al problema:
$$y' = x + y, \quad y(0) = 1$$
con $h = 0.1$. Calcula $y(0.5)$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-16)

---

### [Prob-17] Eficiencia RK4 vs Adams-Bashforth ⭐⭐
Compara la eficiencia de RK4 vs Adams-Bashforth 4 para resolver:
$$y' = -y, \quad y(0) = 1$$
en $[0, 10]$ con $h = 0.1$. ¿Cuántas evaluaciones de $f$ requiere cada método?

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-17)

---

## Sección 5: Sistemas de EDO

### [Prob-18] Conversión a Sistema de Primer Orden ⭐⭐
Convierte a sistema de primer [orden](../../../glossary.md#orden) y resuelve con Euler ($h = 0.1$):
$$y'' + y = 0, \quad y(0) = 1, \; y'(0) = 0$$
Calcula $y(0.3)$ y compara con $\cos(0.3)$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-18)

---

### [Prob-19] Sistema de EDO con RK4 ⭐⭐
Resuelve el sistema con RK4 ($h = 0.2$):
$$x' = x - y, \quad y' = x + y$$
$$x(0) = 1, \quad y(0) = 0$$
Calcula $(x(0.4), y(0.4))$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-19)

---

### [Prob-20] Modelo Lotka-Volterra Depredador-Presa ⭐⭐⭐
El modelo depredador-presa de Lotka-Volterra:
$$x' = 0.4x - 0.01xy$$
$$y' = -0.3y + 0.005xy$$
con $x(0) = 50$ (presas) e $y(0) = 20$ (depredadores). Usa RK4 ($h = 0.5$) para simular hasta $t = 10$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-20)

---

### [Prob-21] Péndulo Simple No Lineal ⭐⭐
Un péndulo simple satisface $\theta'' + \sin\theta = 0$ con $\theta(0) = 0.5$ rad y $\theta'(0) = 0$. Resuelve con RK4 ($h = 0.1$) hasta $t = 2$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-21)

---

### [Prob-22] Ecuación de Van der Pol ⭐⭐⭐
Resuelve la ecuación de Van der Pol:
$$y'' - \mu(1-y^2)y' + y = 0, \quad \mu = 1$$
con $y(0) = 2$, $y'(0) = 0$ usando RK4 ($h = 0.1$) hasta $t = 10$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-22)

---

## Sección 6: Análisis de Error y Estabilidad

### [Prob-23] Análisis de Estabilidad de Euler ⭐⭐
Para $y' = -5y$, $y(0) = 1$:
a) Determina el tamaño de paso máximo para estabilidad con Euler
b) Verifica experimentalmente con $h = 0.3$ y $h = 0.5$

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-23)

---

### [Prob-24] Extrapolación de Richardson ⭐⭐
Usa extrapolación de Richardson: si Euler con $h = 0.1$ da $y(1) = 2.5937$ y con $h = 0.05$ da $y(1) = 2.6408$, estima el valor exacto.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-24)

---

### [Prob-25] Estimación de Error en RK4 ⭐⭐
Para RK4 aplicado a $y' = y$, $y(0) = 1$:
a) Calcula $y(1)$ con $h = 0.2$ y $h = 0.1$
b) Estima el error usando la fórmula $E \approx \frac{y_{h/2} - y_h}{15}$

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-25)

---

### [Prob-26] Ecuación Rígida y Euler Implícito ⭐⭐⭐
La ecuación $y' = -1000y + 3000 - 2000e^{-x}$ es rígida. Verifica que:
a) Euler con $h = 0.001$ diverge
b) Euler con $h = 0.0001$ converge
c) Euler implícito con $h = 0.1$ converge

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-26)

---

## Sección 7: Problemas Aplicados

### [Prob-27] Enfriamiento de Newton ⭐
Un objeto a 90°C se coloca en ambiente a 20°C. Si $T' = -0.1(T - 20)$, usa RK4 ($h = 1$ min) para determinar cuándo $T = 50°C$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-27)

---

### [Prob-28] Crecimiento Logístico Poblacional ⭐
Una población sigue $P' = 0.1P(1 - P/1000)$ con $P(0) = 100$. Simula con RK4 ($h = 1$) hasta $t = 50$ y encuentra cuándo $P = 500$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-28)

---

### [Prob-29] Caída de Paracaidista ⭐⭐
Un paracaidista de 80 kg cae con $v' = 9.8 - 0.005v^2$, $v(0) = 0$. Usa RK4 ($h = 0.5$) para:
a) Encontrar $v(10)$
b) Estimar la velocidad terminal

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-29)

---

### [Prob-30] Cinética Química de Segundo Orden ⭐
En una reacción de segundo [orden](../../../glossary.md#orden): $c' = -kc^2$ con $k = 0.5$ y $c(0) = 2$ mol/L. Calcula $c(5)$ con RK4.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-30)

---

### [Prob-31] Oscilador Armónico Amortiguado ⭐⭐
$$y'' + 0.5y' + 4y = 0, \quad y(0) = 2, \; y'(0) = 0$$
Grafica la solución en $[0, 10]$ usando RK4 ($h = 0.1$).

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-31)

---

## Sección 8: Problemas de Diseño

### [Prob-32] RK Adaptativo con Control de Error ⭐⭐⭐
Implementa un algoritmo RK adaptativo que ajuste $h$ automáticamente para mantener error local [menor](../../../glossary.md#menor) que $10^{-6}$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-32)

---

### [Prob-33] Comparador Automático de Métodos ⭐⭐⭐
Diseña un programa que compare automáticamente Euler, Heun y RK4, mostrando errores y número de evaluaciones.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-33)

---

### [Prob-34] Implementación de RKF45 ⭐⭐⭐
El método de Runge-Kutta-Fehlberg (RKF45) calcula:
$$y_{n+1}^{(4)} = y_n + \frac{h}{360}(90k_1 + 224k_3 + 64k_4 - 10k_5)$$
$$y_{n+1}^{(5)} = y_n + \frac{h}{720}(180k_1 + 448k_3 + 90k_4 + 56k_5 - 54k_6)$$
Implementa y aplica a $y' = y$, $y(0) = 1$ con tolerancia $10^{-8}$.

📎 **Solución:** [Ver respuesta](../solutions/MN-04-Respuestas.md#prob-34)

---

## Resumen de Problemas

| Sección | Problemas | Dificultad |
|---------|-----------|------------|
| 1. Método de Euler | Prob-01 a Prob-05 | ⭐ a ⭐⭐⭐ |
| 2. [Método de Heun](../../../glossary.md#metodos-multipaso) | Prob-15 a Prob-17 | ⭐⭐ a ⭐⭐⭐ |
| 5. Sistemas de [EDO](../../../glossary.md#edo) | Prob-18 a Prob-22 | ⭐⭐ a ⭐⭐⭐ |
| 6. Error y Estabilidad | Prob-23 a Prob-26 | ⭐⭐ a ⭐⭐⭐ |
| 7. Problemas Aplicados | Prob-27 a Prob-31 | ⭐ a ⭐⭐ |
| 8. Problemas de Diseño | Prob-32 a Prob-34 | ⭐⭐⭐ |
