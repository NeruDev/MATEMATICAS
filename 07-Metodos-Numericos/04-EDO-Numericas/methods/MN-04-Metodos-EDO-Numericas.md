<!--
::METADATA::
type: method
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Métodos: Solución Numérica de EDO

> **Referencia rápida:** Esta guía presenta 12 [métodos numéricos](../../../glossary.md#metodos-numericos) para resolver [ecuaciones diferenciales](../../../glossary.md#ecuaciones-diferenciales) ordinarias con algoritmos detallados, análisis de error y ejemplos completos.

---

## Índice de Métodos

| # | Método | [Orden](../../../glossary.md#orden) de Error | Complejidad |
|---|--------|----------------|-------------|
| 1 | [Euler Explícito](#método-1-euler-explícito) | $O(h)$ | ⭐ |
| 2 | [Heun (Euler Mejorado)](#método-2-heun-euler-mejorado) | $O(h^2)$ | ⭐ |
| 3 | [Punto Medio](#método-3-punto-medio) | $O(h^2)$ | ⭐ |
| 4 | [Runge-Kutta 2 (RK2)](#método-4-runge-kutta-2-rk2) | $O(h^2)$ | ⭐⭐ |
| 5 | [Runge-Kutta 4 (RK4)](#método-5-runge-kutta-4-rk4) | $O(h^4)$ | ⭐⭐ |
| 6 | [Runge-Kutta-Fehlberg (RKF45)](#método-6-runge-kutta-fehlberg-rkf45) | Adaptativo | ⭐⭐⭐ |
| 7 | [Adams-Bashforth](#método-7-adams-bashforth) | $O(h^k)$ | ⭐⭐⭐ |
| 8 | [Adams-Moulton](#método-8-adams-moulton) | $O(h^{k+1})$ | ⭐⭐⭐ |
| 9 | [Predictor-Corrector](#método-9-predictor-corrector) | $O(h^4)$-$O(h^5)$ | ⭐⭐⭐ |
| 10 | [Euler Implícito](#método-10-euler-implícito) | $O(h)$ | ⭐⭐ |
| 11 | [Trapecio (Crank-Nicolson)](#método-11-trapecio-crank-nicolson) | $O(h^2)$ | ⭐⭐⭐ |
| 12 | [Sistemas de EDO](#método-12-sistemas-de-[edo](../../../glossary.md#edo)-con-rk4) | Variable | ⭐⭐⭐ |

---

## Conceptos Fundamentales

### Problema de Valor Inicial (PVI)

$$\frac{dy}{dx} = f(x, y), \quad y(x_0) = y_0$$

**Objetivo:** Encontrar $y(x)$ numéricamente en puntos discretos.

### Discretización

- Paso: $h = x_{n+1} - x_n$
- Nodos: $x_n = x_0 + nh$
- Aproximaciones: $y_n \approx y(x_n)$

### Tipos de Error

| Error | Definición |
|-------|------------|
| **Local** | Error en un paso (suponiendo $y_n$ exacto) |
| **Global** | Error acumulado $\vert y_n - y(x_n)\vert$ |
| **De truncamiento** | Por truncar serie de Taylor |
| **De redondeo** | Por aritmética de punto flotante |

### Estabilidad

Un método es **estable** si los errores no crecen sin [límite](../../../glossary.md#limite).

**Región de estabilidad:** Valores de $h\lambda$ donde el método es estable para $y' = \lambda y$.

---

## Método 1: Euler Explícito

### Cuándo Usar

- Introducción a [métodos numéricos](../../../glossary.md#metodos-numericos)
- Problemas donde la velocidad prima sobre precisión
- [Base](../../../glossary.md#base) para métodos más avanzados

### Fórmula

$$y_{n+1} = y_n + h \cdot f(x_n, y_n)$$

### Error

- **Local:** $O(h^2)$
- **Global:** $O(h)$

### Derivación

Serie de Taylor:
$$y(x_{n+1}) = y(x_n) + hy'(x_n) + \frac{h^2}{2}y''(\xi)$$

Truncando: $y_{n+1} \approx y_n + hf(x_n, y_n)$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Inicializar** | $x_0$, $y_0$, $h$, $x_f$ |
| 2 | **Mientras** $x < x_f$ | |
| 3 | → **Calcular** | $y_{n+1} = y_n + h \cdot f(x_n, y_n)$ |
| 4 | → **Actualizar** | $x_{n+1} = x_n + h$ |
| 5 | → **Guardar** | $(x_{n+1}, y_{n+1})$ |

### Pseudocódigo

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

### Ejemplo Detallado

**Problema:** Resolver $y' = x + y$, $y(0) = 1$ en $[0, 0.4]$ con $h = 0.1$

---

**Iteraciones:**

| $n$ | $x_n$ | $y_n$ | $f(x_n, y_n) = x_n + y_n$ | $y_{n+1} = y_n + 0.1 \cdot f_n$ |
|:---:|:-----:|:-----:|:-------------------------:|:-------------------------------:|
| 0 | 0.0 | 1.0000 | 1.0000 | 1.1000 |
| 1 | 0.1 | 1.1000 | 1.2000 | 1.2200 |
| 2 | 0.2 | 1.2200 | 1.4200 | 1.3620 |
| 3 | 0.3 | 1.3620 | 1.6620 | 1.5282 |
| 4 | 0.4 | 1.5282 | — | — |

---

**Verificación con solución exacta:**

La solución exacta de $y' = x + y$, $y(0) = 1$ es:

$$y(x) = 2e^x - x - 1$$

$y(0.4) = 2e^{0.4} - 0.4 - 1 = 2(1.4918) - 1.4 = 1.5836$

**Error en $x = 0.4$:** $|1.5282 - 1.5836| = 0.0554$

$$\boxed{y(0.4) \approx 1.5282}$$

---

## Método 2: Heun (Euler Mejorado)

### Cuándo Usar

- Mayor precisión que Euler con poco costo extra
- Primer método predictor-corrector
- Funciones con pendiente variable

### Fórmulas

**Predictor:**
$$\tilde{y}_{n+1} = y_n + h \cdot f(x_n, y_n)$$

**Corrector:**
$$y_{n+1} = y_n + \frac{h}{2}\left[f(x_n, y_n) + f(x_{n+1}, \tilde{y}_{n+1})\right]$$

### Error

- **Local:** $O(h^3)$
- **Global:** $O(h^2)$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Calcular** $k_1$ | $k_1 = f(x_n, y_n)$ |
| 2 | **Predicción** | $\tilde{y} = y_n + h \cdot k_1$ |
| 3 | **Calcular** $k_2$ | $k_2 = f(x_n + h, \tilde{y})$ |
| 4 | **Corrección** | $y_{n+1} = y_n + \frac{h}{2}(k_1 + k_2)$ |

### Pseudocódigo

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

### Ejemplo Detallado

**Problema:** Resolver $y' = x + y$, $y(0) = 1$ con $h = 0.1$

---

**Paso 0 → 1 (de $x = 0$ a $x = 0.1$):**

$k_1 = f(0, 1) = 0 + 1 = 1$

$\tilde{y}_1 = 1 + 0.1(1) = 1.1$

$k_2 = f(0.1, 1.1) = 0.1 + 1.1 = 1.2$

$y_1 = 1 + \frac{0.1}{2}(1 + 1.2) = 1 + 0.05(2.2) = 1.11$

---

**Paso 1 → 2 (de $x = 0.1$ a $x = 0.2$):**

$k_1 = f(0.1, 1.11) = 0.1 + 1.11 = 1.21$

$\tilde{y}_2 = 1.11 + 0.1(1.21) = 1.231$

$k_2 = f(0.2, 1.231) = 0.2 + 1.231 = 1.431$

$y_2 = 1.11 + \frac{0.1}{2}(1.21 + 1.431) = 1.11 + 0.1321 = 1.2421$

---

**Resumen:**

| $n$ | $x_n$ | $y_n$ (Heun) | $y$ exacta | Error |
|:---:|:-----:|:------------:|:----------:|:-----:|
| 0 | 0.0 | 1.0000 | 1.0000 | 0 |
| 1 | 0.1 | 1.1100 | 1.1103 | 0.0003 |
| 2 | 0.2 | 1.2421 | 1.2428 | 0.0007 |
| 3 | 0.3 | 1.3985 | 1.3997 | 0.0012 |
| 4 | 0.4 | 1.5818 | 1.5836 | 0.0018 |

$$\boxed{y(0.4) \approx 1.5818}$$

---

## Método 3: Punto Medio

### Cuándo Usar

- Alternativa a Heun
- Precisión de segundo [orden](../../../glossary.md#orden)
- [Base](../../../glossary.md#base) para entender RK2

### Fórmula

$$k_1 = f(x_n, y_n)$$
$$k_2 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right)$$
$$y_{n+1} = y_n + h \cdot k_2$$

### Interpretación Geométrica

1. Evalúa la pendiente en $(x_n, y_n)$
2. Avanza medio paso con esa pendiente
3. Evalúa nueva pendiente en el punto medio
4. Usa la pendiente del punto medio para el paso completo

### Pseudocódigo

```python
def punto_medio(f, x0, y0, xf, h):
    x, y = x0, y0
    resultados = [(x, y)]
    
    while x < xf:
        k1 = f(x, y)
        k2 = f(x + h/2, y + h/2 * k1)
        y = y + h * k2
        x = x + h
        resultados.append((x, y))
    
    return resultados
```

---

## Método 4: Runge-Kutta 2 (RK2)

### Cuándo Usar

- Compromiso velocidad-precisión
- Entender la estructura de métodos RK
- Problemas donde $O(h^2)$ es [suficiente](../../../glossary.md#suficiente)

### Familia RK2

Forma general:
$$y_{n+1} = y_n + h[(1-\alpha)k_1 + \alpha k_2]$$
$$k_1 = f(x_n, y_n)$$
$$k_2 = f\left(x_n + \frac{h}{2\alpha}, y_n + \frac{h}{2\alpha}k_1\right)$$

| $\alpha$ | Método |
|:--------:|--------|
| 1/2 | Punto Medio |
| 1 | Heun |
| 2/3 | Ralston |

### Fórmula Ralston (óptimo)

$$k_1 = f(x_n, y_n)$$
$$k_2 = f\left(x_n + \frac{3h}{4}, y_n + \frac{3h}{4}k_1\right)$$
$$y_{n+1} = y_n + \frac{h}{3}(k_1 + 2k_2)$$

---

## Método 5: Runge-Kutta 4 (RK4)

### Cuándo Usar

- **Método estándar** para la mayoría de problemas
- Excelente equilibrio precisión/costo
- Funciones suaves sin comportamiento rígido

### Fórmulas

$$k_1 = f(x_n, y_n)$$
$$k_2 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right)$$
$$k_3 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_2\right)$$
$$k_4 = f(x_n + h, y_n + hk_3)$$
$$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

### Error

- **Local:** $O(h^5)$
- **Global:** $O(h^4)$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Calcular** $k_1$ | $k_1 = f(x_n, y_n)$ |
| 2 | **Calcular** $k_2$ | $k_2 = f(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_1)$ |
| 3 | **Calcular** $k_3$ | $k_3 = f(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_2)$ |
| 4 | **Calcular** $k_4$ | $k_4 = f(x_n + h, y_n + hk_3)$ |
| 5 | **Actualizar** | $y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$ |

### Pseudocódigo

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

### Ejemplo Detallado

**Problema:** Resolver $y' = x + y$, $y(0) = 1$ con $h = 0.2$

---

**Paso 0 → 1 (de $x = 0$ a $x = 0.2$):**

$k_1 = f(0, 1) = 0 + 1 = 1$

$k_2 = f(0 + 0.1, 1 + 0.1 \times 1) = f(0.1, 1.1) = 0.1 + 1.1 = 1.2$

$k_3 = f(0 + 0.1, 1 + 0.1 \times 1.2) = f(0.1, 1.12) = 0.1 + 1.12 = 1.22$

$k_4 = f(0 + 0.2, 1 + 0.2 \times 1.22) = f(0.2, 1.244) = 0.2 + 1.244 = 1.444$

---

$y_1 = 1 + \frac{0.2}{6}(1 + 2(1.2) + 2(1.22) + 1.444)$

$= 1 + \frac{0.2}{6}(1 + 2.4 + 2.44 + 1.444)$

$= 1 + \frac{0.2}{6}(7.284)$

$= 1 + 0.2428 = 1.2428$

---

**Comparación:**

| $x$ | RK4 | Exacta | Error |
|:---:|:---:|:------:|:-----:|
| 0.2 | 1.2428 | 1.2428 | $< 10^{-5}$ |
| 0.4 | 1.5836 | 1.5836 | $< 10^{-5}$ |

$$\boxed{y(0.2) \approx 1.2428 \text{ (4 cifras exactas)}}$$

---

## Método 6: Runge-Kutta-Fehlberg (RKF45)

### Cuándo Usar

- Control automático del paso $h$
- Precisión variable según la región
- Evita pasos innecesariamente pequeños

### Idea

Usar dos métodos RK (orden 4 y 5) simultáneamente para estimar el error.

### Fórmulas

Calcular $k_1, \ldots, k_6$ con coeficientes específicos.

**Método orden 4:**
$$y_{n+1}^{(4)} = y_n + \sum_{i=1}^{6} a_i k_i$$

**Método orden 5:**
$$y_{n+1}^{(5)} = y_n + \sum_{i=1}^{6} b_i k_i$$

**Estimación del error:**
$$\varepsilon \approx |y_{n+1}^{(5)} - y_{n+1}^{(4)}|$$

### Control del Paso

Si $\varepsilon > \text{tol}$: rechazar, reducir $h$

Si $\varepsilon < \text{tol}$: aceptar, posiblemente aumentar $h$

**Factor de ajuste:**
$$h_{nuevo} = 0.84 \cdot h \left(\frac{\text{tol}}{\varepsilon}\right)^{1/4}$$

### Pseudocódigo

```python
def rkf45(f, x0, y0, xf, tol=1e-6, h_init=0.1):
    x, y = x0, y0
    h = h_init
    resultados = [(x, y)]
    
    while x < xf:
        # Calcular k1 a k6 con coeficientes de Fehlberg
        k1 = f(x, y)
        k2 = f(x + h/4, y + h*k1/4)
        k3 = f(x + 3*h/8, y + 3*h*k1/32 + 9*h*k2/32)
        k4 = f(x + 12*h/13, y + 1932*h*k1/2197 - 7200*h*k2/2197 + 7296*h*k3/2197)
        k5 = f(x + h, y + 439*h*k1/216 - 8*h*k2 + 3680*h*k3/513 - 845*h*k4/4104)
        k6 = f(x + h/2, y - 8*h*k1/27 + 2*h*k2 - 3544*h*k3/2565 + 1859*h*k4/4104 - 11*h*k5/40)
        
        # Soluciones de orden 4 y 5
        y4 = y + h*(25*k1/216 + 1408*k3/2565 + 2197*k4/4104 - k5/5)
        y5 = y + h*(16*k1/135 + 6656*k3/12825 + 28561*k4/56430 - 9*k5/50 + 2*k6/55)
        
        # Error estimado
        error = abs(y5 - y4)
        
        if error <= tol:
            x = x + h
            y = y5
            resultados.append((x, y))
        
        # Ajustar paso
        if error > 0:
            h = 0.84 * h * (tol / error)**0.25
        h = min(h, xf - x)
    
    return resultados
```

---

## Método 7: Adams-Bashforth

### Cuándo Usar

- Muchos pasos de integración
- Información de pasos previos disponible
- Eficiencia (una evaluación de $f$ por paso)

### Idea

Método multipaso **explícito**: usa valores previos $f_n, f_{n-1}, \ldots$

### Fórmulas

**2 pasos (AB2):**
$$y_{n+1} = y_n + \frac{h}{2}(3f_n - f_{n-1})$$

**3 pasos (AB3):**
$$y_{n+1} = y_n + \frac{h}{12}(23f_n - 16f_{n-1} + 5f_{n-2})$$

**4 pasos (AB4):**
$$y_{n+1} = y_n + \frac{h}{24}(55f_n - 59f_{n-1} + 37f_{n-2} - 9f_{n-3})$$

### Arranque

Requiere valores iniciales (típicamente de RK4).

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Arrancar** | Usar RK4 para $y_1, y_2, y_3$ |
| 2 | **Guardar** | $f_0, f_1, f_2, f_3$ |
| 3 | **Para** $n \geq 3$ | |
| 4 | → **Calcular** | $y_{n+1}$ con fórmula AB4 |
| 5 | → **Actualizar** | $f_{n+1} = f(x_{n+1}, y_{n+1})$ |

### Pseudocódigo

```python
def adams_bashforth_4(f, x0, y0, xf, h):
    # Arranque con RK4
    resultados = rk4(f, x0, y0, x0 + 3*h, h)
    
    x_vals = [r[0] for r in resultados]
    y_vals = [r[1] for r in resultados]
    f_vals = [f(x, y) for x, y in resultados]
    
    x = x_vals[-1]
    
    while x < xf - 1e-10:
        y_new = y_vals[-1] + h/24 * (
            55*f_vals[-1] - 59*f_vals[-2] + 37*f_vals[-3] - 9*f_vals[-4]
        )
        x = x + h
        
        y_vals.append(y_new)
        x_vals.append(x)
        f_vals.append(f(x, y_new))
        resultados.append((x, y_new))
    
    return resultados
```

### Ejemplo

**Problema:** $y' = x + y$, $y(0) = 1$, $h = 0.1$

**Arranque (RK4):**
- $y_0 = 1$, $f_0 = 1$
- $y_1 = 1.1103$, $f_1 = 1.2103$
- $y_2 = 1.2428$, $f_2 = 1.4428$
- $y_3 = 1.3997$, $f_3 = 1.6997$

**Paso AB4 ($n = 3 \to 4$):**

$$y_4 = 1.3997 + \frac{0.1}{24}[55(1.6997) - 59(1.4428) + 37(1.2103) - 9(1)]$$

$$= 1.3997 + \frac{0.1}{24}[93.48 - 85.13 + 44.78 - 9]$$

$$= 1.3997 + \frac{0.1}{24}(44.13) = 1.3997 + 0.1839 = 1.5836$$

---

## Método 8: Adams-Moulton

### Cuándo Usar

- Mayor precisión que Adams-Bashforth del mismo orden
- Como corrector en métodos predictor-corrector
- [EDO](../../../glossary.md#edo) menos rígidas

### Idea

Método multipaso **implícito**: incluye $f_{n+1}$ (desconocido).

### Fórmulas

**2 pasos (AM2 = Trapecio):**
$$y_{n+1} = y_n + \frac{h}{2}(f_{n+1} + f_n)$$

**3 pasos (AM3):**
$$y_{n+1} = y_n + \frac{h}{12}(5f_{n+1} + 8f_n - f_{n-1})$$

**4 pasos (AM4):**
$$y_{n+1} = y_n + \frac{h}{24}(9f_{n+1} + 19f_n - 5f_{n-1} + f_{n-2})$$

### Resolución del Sistema Implícito

Para AM2 con $f = f(x, y)$:

$$y_{n+1} = y_n + \frac{h}{2}[f(x_{n+1}, y_{n+1}) + f_n]$$

Requiere iteración (punto fijo o Newton) o usar predictor.

---

## Método 9: Predictor-Corrector

### Cuándo Usar

- Combina ventajas de Adams-Bashforth y Adams-Moulton
- Mejor estabilidad que AB puro
- Estimación de error local

### Fórmulas (PECE)

**P**redictor (AB4):
$$\tilde{y}_{n+1} = y_n + \frac{h}{24}(55f_n - 59f_{n-1} + 37f_{n-2} - 9f_{n-3})$$

**E**valuar:
$$\tilde{f}_{n+1} = f(x_{n+1}, \tilde{y}_{n+1})$$

**C**orrector (AM3):
$$y_{n+1} = y_n + \frac{h}{24}(9\tilde{f}_{n+1} + 19f_n - 5f_{n-1} + f_{n-2})$$

**E**valuar:
$$f_{n+1} = f(x_{n+1}, y_{n+1})$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Arranque** | RK4 para $y_0, y_1, y_2, y_3$ |
| 2 | **Predictor** | AB4: $\tilde{y}_{n+1}$ |
| 3 | **Evaluar** | $\tilde{f}_{n+1} = f(x_{n+1}, \tilde{y}_{n+1})$ |
| 4 | **Corrector** | AM3: $y_{n+1}$ |
| 5 | **Evaluar** | $f_{n+1} = f(x_{n+1}, y_{n+1})$ |
| 6 | **Repetir** | Pasos 2-5 |

### Pseudocódigo

```python
def predictor_corrector(f, x0, y0, xf, h):
    # Arranque RK4
    resultados = rk4(f, x0, y0, x0 + 3*h, h)
    
    x_vals = [r[0] for r in resultados]
    y_vals = [r[1] for r in resultados]
    f_vals = [f(x, y) for x, y in resultados]
    
    x = x_vals[-1]
    
    while x < xf - 1e-10:
        # Predictor AB4
        y_pred = y_vals[-1] + h/24 * (
            55*f_vals[-1] - 59*f_vals[-2] + 37*f_vals[-3] - 9*f_vals[-4]
        )
        f_pred = f(x + h, y_pred)
        
        # Corrector AM3
        y_new = y_vals[-1] + h/24 * (
            9*f_pred + 19*f_vals[-1] - 5*f_vals[-2] + f_vals[-3]
        )
        
        x = x + h
        y_vals.append(y_new)
        x_vals.append(x)
        f_vals.append(f(x, y_new))
        resultados.append((x, y_new))
    
    return resultados
```

---

## Método 10: Euler Implícito

### Cuándo Usar

- **EDO rígidas** (stiff)
- Estabilidad más importante que precisión
- Problemas con constantes de tiempo muy diferentes

### Fórmula

$$y_{n+1} = y_n + h \cdot f(x_{n+1}, y_{n+1})$$

### Resolución

Para $y' = \lambda y$ (lineal):
$$y_{n+1} = y_n + h\lambda y_{n+1}$$
$$y_{n+1}(1 - h\lambda) = y_n$$
$$y_{n+1} = \frac{y_n}{1 - h\lambda}$$

Para $f$ no lineal: iteración de punto fijo o Newton.

### Estabilidad

**A-estable:** estable para todo $h\lambda$ con $\text{Re}(\lambda) < 0$.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Predictor** | $y^{(0)} = y_n + hf(x_n, y_n)$ |
| 2 | **Iterar** | $y^{(k+1)} = y_n + hf(x_{n+1}, y^{(k)})$ |
| 3 | **Convergencia** | Hasta $\vert y^{(k+1)} - y^{(k)}\vert < \varepsilon$ |
| 4 | **Aceptar** | $y_{n+1} = y^{(k+1)}$ |

### Pseudocódigo

```python
def euler_implicito(f, x0, y0, xf, h, tol=1e-8, max_iter=100):
    x, y = x0, y0
    resultados = [(x, y)]
    
    while x < xf:
        x_new = x + h
        
        # Punto fijo
        y_iter = y + h * f(x, y)  # Euler explícito como semilla
        
        for _ in range(max_iter):
            y_new = y + h * f(x_new, y_iter)
            if abs(y_new - y_iter) < tol:
                break
            y_iter = y_new
        
        y = y_new
        x = x_new
        resultados.append((x, y))
    
    return resultados
```

---

## Método 11: Trapecio (Crank-Nicolson)

### Cuándo Usar

- EDO rígidas con precisión $O(h^2)$
- A-estable
- Ecuaciones en [derivadas](../../../glossary.md#derivadas) parciales parabólicas

### Fórmula

$$y_{n+1} = y_n + \frac{h}{2}\left[f(x_n, y_n) + f(x_{n+1}, y_{n+1})\right]$$

### Propiedades

- Orden 2
- A-estable
- Promedio de Euler explícito e implícito

### Pseudocódigo

```python
def trapecio_implicito(f, x0, y0, xf, h, tol=1e-8):
    x, y = x0, y0
    resultados = [(x, y)]
    
    while x < xf:
        x_new = x + h
        f_n = f(x, y)
        
        # Iteración de punto fijo
        y_iter = y + h * f_n
        for _ in range(100):
            f_new = f(x_new, y_iter)
            y_new = y + h/2 * (f_n + f_new)
            if abs(y_new - y_iter) < tol:
                break
            y_iter = y_new
        
        y = y_new
        x = x_new
        resultados.append((x, y))
    
    return resultados
```

---

## Método 12: Sistemas de EDO con RK4

### Cuándo Usar

- EDO de orden superior (convertir a sistema)
- Sistemas acoplados
- Problemas físicos (mecánica, circuitos)

### Conversión de EDO de Orden $n$

Para $y^{(n)} = g(x, y, y', \ldots, y^{(n-1)})$:

Definir: $z_1 = y$, $z_2 = y'$, ..., $z_n = y^{(n-1)}$

Sistema:
$$z_1' = z_2$$
$$z_2' = z_3$$
$$\vdots$$
$$z_n' = g(x, z_1, z_2, \ldots, z_n)$$

### Fórmulas RK4 Vectorial

$$\mathbf{k}_1 = \mathbf{f}(x_n, \mathbf{y}_n)$$
$$\mathbf{k}_2 = \mathbf{f}\left(x_n + \frac{h}{2}, \mathbf{y}_n + \frac{h}{2}\mathbf{k}_1\right)$$
$$\mathbf{k}_3 = \mathbf{f}\left(x_n + \frac{h}{2}, \mathbf{y}_n + \frac{h}{2}\mathbf{k}_2\right)$$
$$\mathbf{k}_4 = \mathbf{f}(x_n + h, \mathbf{y}_n + h\mathbf{k}_3)$$
$$\mathbf{y}_{n+1} = \mathbf{y}_n + \frac{h}{6}(\mathbf{k}_1 + 2\mathbf{k}_2 + 2\mathbf{k}_3 + \mathbf{k}_4)$$

### Pseudocódigo

```python
import numpy as np

def rk4_sistema(f, x0, y0_vec, xf, h):
    """
    f: función que retorna array de derivadas
    y0_vec: condiciones iniciales [y1(0), y2(0), ...]
    """
    x = x0
    y = np.array(y0_vec, dtype=float)
    resultados = [(x, y.copy())]
    
    while x < xf:
        k1 = np.array(f(x, y))
        k2 = np.array(f(x + h/2, y + h/2 * k1))
        k3 = np.array(f(x + h/2, y + h/2 * k2))
        k4 = np.array(f(x + h, y + h * k3))
        
        y = y + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        x = x + h
        resultados.append((x, y.copy()))
    
    return resultados
```

### Ejemplo Detallado

**Problema:** Resolver $y'' + 4y = 0$, $y(0) = 1$, $y'(0) = 0$

---

**Paso 1: Convertir a sistema**

$z_1 = y$, $z_2 = y'$

$$z_1' = z_2$$
$$z_2' = -4z_1$$

**Condiciones:** $z_1(0) = 1$, $z_2(0) = 0$

---

**Paso 2: Definir [función](../../../glossary.md#funcion)**

```python
def f(x, z):
    return [z[1], -4*z[0]]
```

---

**Paso 3: Aplicar RK4 con $h = 0.1$**

| $x$ | $z_1 = y$ | $z_2 = y'$ | $y$ exacta = $\cos(2x)$ |
|:---:|:---------:|:----------:|:-----------------------:|
| 0.0 | 1.0000 | 0.0000 | 1.0000 |
| 0.1 | 0.9801 | -0.3987 | 0.9801 |
| 0.2 | 0.9211 | -0.7833 | 0.9211 |
| 0.3 | 0.8253 | -1.1375 | 0.8253 |
| 0.4 | 0.6967 | -1.4482 | 0.6967 |
| 0.5 | 0.5403 | -1.6865 | 0.5403 |

---

**Solución exacta:** $y = \cos(2x)$

$$\boxed{\text{RK4 para sistemas produce resultados exactos a 4 decimales}}$$

---

## Diagrama de Decisión

```
┌─────────────────────────────────────────────────────┐
│          SOLUCIÓN NUMÉRICA DE EDO                   │
└─────────────────────────────────────────────────────┘
                      │
                      ▼
            ┌──────────────────┐
            │ ¿Tipo de EDO?    │
            └──────────────────┘
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
   Simple         Sistema         Rígida
   $y'=f$         $\mathbf{y}'$   (stiff)
      │               │               │
      ▼               ▼               ▼
  ¿Precisión?    RK4 vectorial    Métodos
      │                            implícitos
 ┌────┴────┐                          │
Baja    Alta                    ┌─────┴─────┐
 │        │                  Euler      Trapecio
 ▼        ▼                implícito   (C-N)
Euler    RK4
Heun     RKF45
         AB/AM
```

---

## Tabla Comparativa de Métodos

| Método | Eval. $f$/paso | Orden | Memoria | Estabilidad |
|--------|:--------------:|:-----:|:-------:|:-----------:|
| Euler explícito | 1 | 1 | Mínima | Condicional |
| Heun | 2 | 2 | Mínima | Condicional |
| RK4 | 4 | 4 | Mínima | Condicional |
| RKF45 | 6 | 4-5 | Mínima | Adaptativo |
| AB4 | 1* | 4 | 4 valores | Condicional |
| AM4 | 1* | 5 | 4 valores | Mejor |
| Predictor-Corrector | 2* | 4-5 | 4 valores | Buena |
| Euler implícito | Iterativo | 1 | Mínima | A-estable |
| Trapecio | Iterativo | 2 | Mínima | A-estable |

*Usa valores previos almacenados.

---

## Errores Comunes a Evitar

| Error | Consecuencia | Prevención |
|-------|--------------|------------|
| Paso $h$ muy grande | Inestabilidad | Verificar estabilidad |
| Paso $h$ muy pequeño | Error de redondeo | Usar adaptativo |
| Ignorar rigidez | Falla o lentitud | Detectar y usar implícitos |
| Arranque inadecuado | Error en multipaso | Usar RK4 para arranque |
| No verificar solución | Resultados incorrectos | Comparar con caso conocido |

---

## Análisis de Estabilidad

### Ecuación de Prueba

$$y' = \lambda y, \quad \lambda \in \mathbb{C}$$

### Regiones de Estabilidad

| Método | Región ($z = h\lambda$) |
|--------|------------------------|
| Euler explícito | $\vert 1 + z\vert < 1$ |
| Euler implícito | $\vert 1 - z\vert^{-1} < 1$ (todo $\text{Re}(z) < 0$) |
| RK4 | $\vert 1 + z + z^2/2 + z^3/6 + z^4/24\vert < 1$ |
| Trapecio | Todo $\text{Re}(z) < 0$ |

### EDO Rígida (Stiff)

Sistema es rígido si:
$$\frac{\max|\lambda_i|}{\min|\lambda_i|} \gg 1$$

**Solución:** Métodos implícitos (A-estables).

---

## Problemas de Práctica Sugeridos

1. **Euler:** $y' = -2y + x$, $y(0) = 1$, $h = 0.1$

2. **RK4:** $y' = y\cos(x)$, $y(0) = 1$, hasta $x = 2$

3. **Sistema:** $y'' + y' + y = 0$, $y(0) = 1$, $y'(0) = 0$

4. **Rígida:** $y' = -1000y + 1$, $y(0) = 0$ (comparar explícito vs implícito)

5. **Predictor-Corrector:** $y' = x^2 + y^2$, $y(0) = 0$, $h = 0.1$

6. **Adaptativo:** $y' = \sin(10x)$, $y(0) = 0$, tolerancia $10^{-6}$

---

*Documento actualizado con formato expandido para estudio detallado.*
