<!--
content_type: methods
topic: EDO Numéricas
---
-->

# Métodos: Solución Numérica de EDO

---

## Método 1: Euler Explícito

### Fórmula

$$y_{n+1} = y_n + h \cdot f(x_n, y_n)$$

### Algoritmo

```python
def euler(f, x0, y0, xf, h):
    x, y = x0, y0
    resultados = [(x, y)]
    while x < xf:
        y = y + h * f(x, y)
        x = x + h
        resultados.append((x, y))
    return resultados
```

### Ejemplo Completo

**Resolver $y' = x + y$, $y(0) = 1$ en $[0, 0.4]$ con $h = 0.1$**

| $n$ | $x_n$ | $y_n$ | $f(x_n, y_n) = x_n + y_n$ | $y_{n+1} = y_n + 0.1 \cdot f_n$ |
|-----|-------|-------|---------------------------|--------------------------------|
| 0 | 0 | 1 | 1 | 1.1 |
| 1 | 0.1 | 1.1 | 1.2 | 1.22 |
| 2 | 0.2 | 1.22 | 1.42 | 1.362 |
| 3 | 0.3 | 1.362 | 1.662 | 1.5282 |
| 4 | 0.4 | 1.5282 | — | — |

**Solución exacta:** $y = 2e^x - x - 1$

$y(0.4) = 2e^{0.4} - 0.4 - 1 = 1.5836$

**Error:** $|1.5282 - 1.5836| = 0.0554$

---

## Método 2: Heun (Euler Mejorado)

### Fórmulas

$$\tilde{y}_{n+1} = y_n + h \cdot f(x_n, y_n) \quad \text{(predictor)}$$
$$y_{n+1} = y_n + \frac{h}{2}[f(x_n, y_n) + f(x_{n+1}, \tilde{y}_{n+1})] \quad \text{(corrector)}$$

### Algoritmo

```python
def heun(f, x0, y0, xf, h):
    x, y = x0, y0
    resultados = [(x, y)]
    while x < xf:
        k1 = f(x, y)
        y_pred = y + h * k1
        k2 = f(x + h, y_pred)
        y = y + h/2 * (k1 + k2)
        x = x + h
        resultados.append((x, y))
    return resultados
```

### Ejemplo Completo

**Resolver $y' = x + y$, $y(0) = 1$ con $h = 0.1$**

**Paso 0 → 1:**
- $k_1 = f(0, 1) = 1$
- $\tilde{y}_1 = 1 + 0.1(1) = 1.1$
- $k_2 = f(0.1, 1.1) = 1.2$
- $y_1 = 1 + 0.05(1 + 1.2) = 1.11$

**Paso 1 → 2:**
- $k_1 = f(0.1, 1.11) = 1.21$
- $\tilde{y}_2 = 1.11 + 0.1(1.21) = 1.231$
- $k_2 = f(0.2, 1.231) = 1.431$
- $y_2 = 1.11 + 0.05(1.21 + 1.431) = 1.2421$

| $n$ | $x_n$ | $y_n$ (Heun) | $y$ exacta | Error |
|-----|-------|--------------|------------|-------|
| 0 | 0 | 1 | 1 | 0 |
| 1 | 0.1 | 1.11 | 1.1103 | 0.0003 |
| 2 | 0.2 | 1.2421 | 1.2428 | 0.0007 |
| 3 | 0.3 | 1.3985 | 1.3997 | 0.0012 |
| 4 | 0.4 | 1.5818 | 1.5836 | 0.0018 |

---

## Método 3: Runge-Kutta 4 (RK4)

### Fórmulas

$$k_1 = f(x_n, y_n)$$
$$k_2 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right)$$
$$k_3 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_2\right)$$
$$k_4 = f(x_n + h, y_n + hk_3)$$
$$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

### Algoritmo

```python
def rk4(f, x0, y0, xf, h):
    x, y = x0, y0
    resultados = [(x, y)]
    while x < xf:
        k1 = f(x, y)
        k2 = f(x + h/2, y + h/2 * k1)
        k3 = f(x + h/2, y + h/2 * k2)
        k4 = f(x + h, y + h * k3)
        y = y + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        x = x + h
        resultados.append((x, y))
    return resultados
```

### Ejemplo Completo

**Resolver $y' = x + y$, $y(0) = 1$ con $h = 0.2$**

**Paso 0 → 1 ($x: 0 \to 0.2$):**

$k_1 = f(0, 1) = 0 + 1 = 1$

$k_2 = f(0.1, 1 + 0.1 \times 1) = f(0.1, 1.1) = 1.2$

$k_3 = f(0.1, 1 + 0.1 \times 1.2) = f(0.1, 1.12) = 1.22$

$k_4 = f(0.2, 1 + 0.2 \times 1.22) = f(0.2, 1.244) = 1.444$

$y_1 = 1 + \frac{0.2}{6}(1 + 2(1.2) + 2(1.22) + 1.444)$
$= 1 + \frac{0.2}{6}(7.284) = 1.2428$

**Comparación $y(0.2)$:**
- RK4: 1.2428
- Exacta: 1.2428
- Error: < 0.00005

---

## Método 4: Adams-Bashforth 4 Pasos

### Fórmula

$$y_{n+1} = y_n + \frac{h}{24}(55f_n - 59f_{n-1} + 37f_{n-2} - 9f_{n-3})$$

### Algoritmo con Arranque RK4

```python
def adams_bashforth_4(f, x0, y0, xf, h):
    # Arranque con RK4
    resultados = rk4(f, x0, y0, x0 + 3*h, h)
    x_vals = [r[0] for r in resultados]
    y_vals = [r[1] for r in resultados]
    f_vals = [f(x, y) for x, y in resultados]
    
    x = x_vals[-1]
    while x < xf:
        y_new = y_vals[-1] + h/24 * (55*f_vals[-1] - 59*f_vals[-2] 
                                     + 37*f_vals[-3] - 9*f_vals[-4])
        x = x + h
        y_vals.append(y_new)
        x_vals.append(x)
        f_vals.append(f(x, y_new))
        resultados.append((x, y_new))
    
    return resultados
```

### Ejemplo

**Resolver $y' = x + y$, $y(0) = 1$ hasta $x = 0.6$ con $h = 0.1$**

**Arranque (RK4):** $y_0 = 1$, $y_1 = 1.1103$, $y_2 = 1.2428$, $y_3 = 1.3997$

$f_0 = 1$, $f_1 = 1.2103$, $f_2 = 1.4428$, $f_3 = 1.6997$

**Paso 4 (Adams-Bashforth):**
$$y_4 = 1.3997 + \frac{0.1}{24}[55(1.6997) - 59(1.4428) + 37(1.2103) - 9(1)]$$
$$= 1.3997 + \frac{0.1}{24}[93.48 - 85.13 + 44.78 - 9]$$
$$= 1.3997 + \frac{0.1}{24}(44.13) = 1.5836$$

---

## Método 5: Sistemas de EDO

### Fórmulas (Euler para Sistema)

Para $\mathbf{y}' = \mathbf{f}(x, \mathbf{y})$:
$$\mathbf{y}_{n+1} = \mathbf{y}_n + h \cdot \mathbf{f}(x_n, \mathbf{y}_n)$$

### Algoritmo

```python
import numpy as np

def euler_sistema(f, x0, y0_vec, xf, h):
    x = x0
    y = np.array(y0_vec)
    resultados = [(x, y.copy())]
    while x < xf:
        y = y + h * np.array(f(x, y))
        x = x + h
        resultados.append((x, y.copy()))
    return resultados
```

### Ejemplo: EDO de Segundo Orden

**Resolver $y'' + 4y = 0$, $y(0) = 1$, $y'(0) = 0$**

**Conversión a sistema:**
$$z_1 = y, \quad z_2 = y'$$
$$z_1' = z_2$$
$$z_2' = -4z_1$$

**Condiciones:** $z_1(0) = 1$, $z_2(0) = 0$

**Con RK4 y $h = 0.1$:**

| $x$ | $z_1 = y$ | $z_2 = y'$ | $y$ exacta = $\cos(2x)$ |
|-----|-----------|------------|-------------------------|
| 0 | 1 | 0 | 1 |
| 0.1 | 0.9801 | -0.3987 | 0.9801 |
| 0.2 | 0.9211 | -0.7833 | 0.9211 |
| 0.3 | 0.8253 | -1.1375 | 0.8253 |

---

## Método 6: Predictor-Corrector

### Fórmulas

**Predictor (Adams-Bashforth 4):**
$$\tilde{y}_{n+1} = y_n + \frac{h}{24}(55f_n - 59f_{n-1} + 37f_{n-2} - 9f_{n-3})$$

**Corrector (Adams-Moulton 3):**
$$y_{n+1} = y_n + \frac{h}{24}(9\tilde{f}_{n+1} + 19f_n - 5f_{n-1} + f_{n-2})$$

donde $\tilde{f}_{n+1} = f(x_{n+1}, \tilde{y}_{n+1})$

### Algoritmo

```python
def predictor_corrector(f, x0, y0, xf, h):
    # Arranque RK4
    resultados = rk4(f, x0, y0, x0 + 3*h, h)
    # ... (similar a Adams-Bashforth con paso de corrección adicional)
```

---

## Tabla Comparativa de Métodos

| Método | Código | Evaluaciones $f$/paso | Orden | Uso recomendado |
|--------|--------|----------------------|-------|-----------------|
| Euler | Simple | 1 | 1 | Visualización, enseñanza |
| Heun | Simple | 2 | 2 | Precisión moderada |
| RK4 | Moderado | 4 | 4 | **Estándar general** |
| AB4 | Moderado | 1* | 4 | Muchos pasos, eficiencia |
| PC | Mayor | 2* | 4-5 | Alta precisión |

*Usa valores previos ya calculados.

---

## Diagrama de Decisión

```
¿Qué tipo de problema?
│
├── SIMPLE/ENSEÑANZA → Euler
│
├── PROBLEMA GENERAL
│   │
│   └── ¿Cuántos pasos?
│       │
│       ├── POCOS → RK4
│       │
│       └── MUCHOS → Adams-Bashforth/Moulton
│
├── EDO RÍGIDA → Métodos implícitos
│
└── PRECISIÓN VARIABLE → RK adaptativo (RKF45)
```
