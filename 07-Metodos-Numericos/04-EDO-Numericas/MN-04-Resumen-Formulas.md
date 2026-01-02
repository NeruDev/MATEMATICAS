<!--
---
title: Resumen de Fórmulas - [EDO Numéricas](../../glossary.md#edo-numericas)
type: cheatsheet
topic: [edo](../../glossary.md#edo)-numericas
tags: [métodos-numéricos, [EDO](../../glossary.md#edo), fórmulas, cheatsheet]
created: 2025-12-20
updated: 2025-12-20
---
-->

# Resumen de Fórmulas: EDO Numéricas

## Problema de Valor Inicial

$$\frac{dy}{dx} = f(x, y), \quad y(x_0) = y_0$$

Objetivo: Encontrar $y_1, y_2, \ldots, y_n$ en $x_1, x_2, \ldots, x_n$

---

## 1. Método de Euler (Euler Explícito)

### Fórmula Principal
$$y_{n+1} = y_n + h \cdot f(x_n, y_n)$$

donde $h = x_{n+1} - x_n$ es el tamaño de paso.

### Error Local de Truncamiento
$$\tau = \frac{h^2}{2}y''(\xi) = O(h^2)$$

### Error Global
$$E = O(h)$$

**[Orden](../../glossary.md#orden) del método:** 1

---

## 2. Método de Euler Mejorado (Heun)

### Fórmula Principal
$$\begin{aligned}
k_1 &= f(x_n, y_n) \\
k_2 &= f(x_n + h, y_n + h \cdot k_1) \\
y_{n+1} &= y_n + \frac{h}{2}(k_1 + k_2)
\end{aligned}$$

### Forma Predictor-Corrector
$$\begin{aligned}
\tilde{y}_{n+1} &= y_n + h \cdot f(x_n, y_n) \quad \text{(predictor)}\\
y_{n+1} &= y_n + \frac{h}{2}\left[f(x_n, y_n) + f(x_{n+1}, \tilde{y}_{n+1})\right] \quad \text{(corrector)}
\end{aligned}$$

**[Orden](../../glossary.md#orden) del método:** 2

---

## 3. Método del Punto Medio (RK2)

### Fórmula Principal
$$\begin{aligned}
k_1 &= f(x_n, y_n) \\
k_2 &= f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right) \\
y_{n+1} &= y_n + h \cdot k_2
\end{aligned}$$

**Orden del método:** 2

---

## 4. Runge-Kutta de Cuarto Orden (RK4)

### Fórmula Principal (El método clásico)
$$\begin{aligned}
k_1 &= f(x_n, y_n) \\
k_2 &= f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right) \\
k_3 &= f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_2\right) \\
k_4 &= f(x_n + h, y_n + h \cdot k_3) \\
y_{n+1} &= y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)
\end{aligned}$$

### Error Local de Truncamiento
$$\tau = O(h^5)$$

### Error Global
$$E = O(h^4)$$

**Orden del método:** 4

---

## 5. Sistemas de EDO

### Sistema de Primer Orden
$$\begin{aligned}
\frac{dy_1}{dx} &= f_1(x, y_1, y_2, \ldots, y_m) \\
\frac{dy_2}{dx} &= f_2(x, y_1, y_2, \ldots, y_m) \\
&\vdots \\
\frac{dy_m}{dx} &= f_m(x, y_1, y_2, \ldots, y_m)
\end{aligned}$$

### Euler para Sistemas
$$\mathbf{y}_{n+1} = \mathbf{y}_n + h \cdot \mathbf{f}(x_n, \mathbf{y}_n)$$

### RK4 para Sistemas
$$\begin{aligned}
\mathbf{k}_1 &= \mathbf{f}(x_n, \mathbf{y}_n) \\
\mathbf{k}_2 &= \mathbf{f}\left(x_n + \frac{h}{2}, \mathbf{y}_n + \frac{h}{2}\mathbf{k}_1\right) \\
\mathbf{k}_3 &= \mathbf{f}\left(x_n + \frac{h}{2}, \mathbf{y}_n + \frac{h}{2}\mathbf{k}_2\right) \\
\mathbf{k}_4 &= \mathbf{f}(x_n + h, \mathbf{y}_n + h \cdot \mathbf{k}_3) \\
\mathbf{y}_{n+1} &= \mathbf{y}_n + \frac{h}{6}(\mathbf{k}_1 + 2\mathbf{k}_2 + 2\mathbf{k}_3 + \mathbf{k}_4)
\end{aligned}$$

---

## 6. EDO de Orden Superior

### Conversión a Sistema de Primer Orden

Para $y'' = f(x, y, y')$:

Sea $y_1 = y$ y $y_2 = y'$:
$$\begin{aligned}
y_1' &= y_2 \\
y_2' &= f(x, y_1, y_2)
\end{aligned}$$

### Ejemplo: $y'' + 2y' + y = 0$

$$\begin{aligned}
y_1' &= y_2 \\
y_2' &= -2y_2 - y_1
\end{aligned}$$

---

## 7. Métodos de Adams (Paso Múltiple)

### Adams-Bashforth de 2 pasos (explícito)
$$y_{n+1} = y_n + \frac{h}{2}(3f_n - f_{n-1})$$

### Adams-Bashforth de 4 pasos
$$y_{n+1} = y_n + \frac{h}{24}(55f_n - 59f_{n-1} + 37f_{n-2} - 9f_{n-3})$$

### Adams-Moulton de 2 pasos (implícito)
$$y_{n+1} = y_n + \frac{h}{12}(5f_{n+1} + 8f_n - f_{n-1})$$

---

## 8. Estabilidad

### Ecuación de Prueba
$$y' = \lambda y, \quad \lambda < 0$$

### Región de Estabilidad (Euler)
$$|1 + h\lambda| < 1$$

Estable si $h < \frac{2}{|\lambda|}$.

### Euler Implícito (A-estable)
$$y_{n+1} = y_n + h \cdot f(x_{n+1}, y_{n+1})$$

Para $y' = \lambda y$:
$$y_{n+1} = \frac{y_n}{1 - h\lambda}$$

---

## Tabla Comparativa

| Método | Orden | Evaluaciones de $f$ | Estabilidad |
|--------|-------|---------------------|-------------|
| Euler | 1 | 1 | Condicional |
| Heun (RK2) | 2 | 2 | Condicional |
| Punto Medio | 2 | 2 | Condicional |
| RK4 | 4 | 4 | Condicional |
| Euler Implícito | 1 | 1 (implícito) | A-estable |

---

## Estimación del Error y Control de Paso

### Método de Paso Doble
1. Calcular $y_{n+1}$ con paso $h$
2. Calcular $\hat{y}_{n+1}$ con dos pasos de $h/2$
3. Estimar error: $E \approx \frac{|\hat{y}_{n+1} - y_{n+1}|}{2^p - 1}$

### Ajuste del Tamaño de Paso
$$h_{nuevo} = h \cdot \left(\frac{\varepsilon_{tol}}{E}\right)^{1/(p+1)}$$

donde $p$ es el orden del método y $\varepsilon_{tol}$ es la tolerancia.

---

## Fórmulas de Memoria Rápida

| Método | Recuerda |
|--------|----------|
| Euler | $y_{n+1} = y_n + h \cdot f$ |
| RK4 | $k_1, k_2, k_3, k_4$ con pesos $1:2:2:1$ |
| Error Euler | $O(h)$ global |
| Error RK4 | $O(h^4)$ global |
