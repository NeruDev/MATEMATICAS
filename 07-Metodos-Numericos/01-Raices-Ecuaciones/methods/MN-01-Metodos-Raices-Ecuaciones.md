<!--
::METADATA::
type: method
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Métodos: Raíces de Ecuaciones

> **Referencia rápida:** Esta guía presenta 10 [métodos numéricos](../../../glossary.md#metodos-numericos) para encontrar [raíces de ecuaciones](../../../glossary.md#raices-de-ecuaciones) $f(x) = 0$ con algoritmos detallados y análisis de [convergencia](../../../glossary.md#convergencia).

---

## Índice de Métodos

| # | Método | [Convergencia](#método-1-bisección) | Lineal | ⭐ |
| 2 | [Falsa Posición](#método-3-newton-raphson) | Cuadrática | ⭐⭐ |
| 4 | [Secante](#método-5-punto-fijo) | Lineal | ⭐⭐ |
| 6 | [Newton Modificado](#método-7-müller) | Superlineal (1.84) | ⭐⭐⭐ |
| 8 | [Steffensen](#método-9-brent) | Superlineal | ⭐⭐⭐⭐ |
| 10 | [Newton Multivariable](#método-10-newton-para-sistemas) | Cuadrática | ⭐⭐⭐⭐ |

---

## Conceptos Fundamentales

### Tipos de Convergencia

| Tipo | Definición | Ejemplo |
|------|------------|---------|
| **Lineal** | $\vert e_{n+1}\vert \approx c\vert e_n\vert$ con $0 < c < 1$ | Bisección |
| **Cuadrática** | $\vert e_{n+1}\vert \approx c\vert e_n\vert^2$ | Newton-Raphson |
| **Orden $p$** | $\vert e_{n+1}\vert \approx c\vert e_n\vert^p$ | Secante ($p \approx 1.618$) |

### Criterios de Parada

1. **Tolerancia absoluta:** $|x_{n+1} - x_n| < \varepsilon$
2. **Tolerancia relativa:** $\frac{|x_{n+1} - x_n|}{|x_{n+1}|} < \varepsilon$
3. **Residuo:** $|f(x_n)| < \varepsilon$
4. **Máximo iteraciones:** $n > N_{\max}$

---

## Método 1: Bisección

### Cuándo Usar

- Se conoce un intervalo $[a,b]$ con cambio de signo
- Se necesita **garantía de convergencia**
- Robustez más importante que velocidad

### Fórmula

$$c = \frac{a + b}{2}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Verificar** | $f(a) \cdot f(b) < 0$ |
| 2 | **Calcular** | $c = \frac{a+b}{2}$ |
| 3 | **Evaluar** | $f(c)$ |
| 4 | **Actualizar** | Si $f(a)f(c) < 0$: $b = c$; sino: $a = c$ |
| 5 | **Verificar** | Si $\vert b-a\vert < 2\varepsilon$: terminar |
| 6 | **Repetir** | Desde paso 2 |

### Pseudocódigo

```python
def biseccion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos")
    
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(b - a) < 2 * tol:
            return c, i
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return c, max_iter
```

### Ejemplo Detallado

**Problema:** Encontrar la raíz de $f(x) = x^3 - x - 2$ en $[1, 2]$ con $\varepsilon = 0.01$

---

**Verificación inicial:**
$f(1) = 1 - 1 - 2 = -2 < 0$
$f(2) = 8 - 2 - 2 = 4 > 0$
$f(1) \cdot f(2) < 0$ ✓

---

**Iteraciones:**

| $n$ | $a$ | $b$ | $c = \frac{a+b}{2}$ | $f(c)$ | Acción |
|:---:|:---:|:---:|:-------------------:|:------:|--------|
| 1 | 1.000 | 2.000 | 1.500 | -0.125 | $a = 1.5$ |
| 2 | 1.500 | 2.000 | 1.750 | +1.609 | $b = 1.75$ |
| 3 | 1.500 | 1.750 | 1.625 | +0.666 | $b = 1.625$ |
| 4 | 1.500 | 1.625 | 1.5625 | +0.252 | $b = 1.5625$ |
| 5 | 1.500 | 1.5625 | 1.5313 | +0.059 | $b = 1.5313$ |
| 6 | 1.500 | 1.5313 | 1.5156 | -0.034 | $a = 1.5156$ |
| 7 | 1.5156 | 1.5313 | 1.5234 | +0.012 | $b = 1.5234$ |

$|b - a| = 0.0078 < 2(0.01) = 0.02$ → Terminar

$$\boxed{x^* \approx 1.5195}$$

---

**Número de iteraciones necesarias:**

$$n \geq \frac{\ln(b-a) - \ln(2\varepsilon)}{\ln 2}$$

Para $[1,2]$ y $\varepsilon = 10^{-6}$: $n \geq \frac{\ln 1 - \ln(2 \times 10^{-6})}{\ln 2} \approx 19$ iteraciones

---

## Método 2: Falsa Posición (Regula Falsi)

### Cuándo Usar

- Similar a bisección pero potencialmente más rápido
- Intervalo con cambio de signo conocido
- [Función](../../../glossary.md#funcion) relativamente lineal

### Fórmula

$$c = b - f(b)\frac{b - a}{f(b) - f(a)} = \frac{af(b) - bf(a)}{f(b) - f(a)}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Verificar** | $f(a) \cdot f(b) < 0$ |
| 2 | **Calcular** | $c = \frac{af(b) - bf(a)}{f(b) - f(a)}$ |
| 3 | **Evaluar** | $f(c)$ |
| 4 | **Actualizar** | Si $f(a)f(c) < 0$: $b = c$; sino: $a = c$ |
| 5 | **Verificar** | Si $\vert f(c)\vert < \varepsilon$: terminar |
| 6 | **Repetir** | Desde paso 2 |

### Pseudocódigo

```python
def falsa_posicion(f, a, b, tol=1e-6, max_iter=100):
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos")
    
    for i in range(max_iter):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        
        if abs(fc) < tol:
            return c, i
        
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    
    return c, max_iter
```

### Ejemplo Detallado

**Problema:** Encontrar la raíz de $f(x) = x^3 - x - 2$ en $[1, 2]$

---

**Iteraciones:**

| $n$ | $a$ | $b$ | $c$ | $f(c)$ |
|:---:|:---:|:---:|:---:|:------:|
| 1 | 1.000 | 2.000 | 1.333 | -0.963 |
| 2 | 1.333 | 2.000 | 1.470 | -0.294 |
| 3 | 1.470 | 2.000 | 1.506 | -0.073 |
| 4 | 1.506 | 2.000 | 1.515 | -0.017 |
| 5 | 1.515 | 2.000 | 1.517 | -0.004 |

$$\boxed{x^* \approx 1.5214}$$

---

**Problema:** El extremo $b = 2$ nunca se mueve (convergencia lenta). Solución: **Illinois Algorithm** modifica $f(a)$ o $f(b)$ si un extremo permanece fijo.

---

## Método 3: Newton-Raphson

### Cuándo Usar

- Se tiene $f'(x)$ disponible
- Se necesita convergencia rápida
- Buen punto inicial disponible

### Fórmula

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

### Interpretación Geométrica

La recta [tangente](../../../glossary.md#tangente) a $f$ en $x_n$ corta al eje $x$ en $x_{n+1}$.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Elegir** | Punto inicial $x_0$ |
| 2 | **Evaluar** | $f(x_n)$ y $f'(x_n)$ |
| 3 | **Verificar** | Si $\vert f'(x_n)\vert \approx 0$: problema |
| 4 | **Calcular** | $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$ |
| 5 | **Verificar** | Si $\vert x_{n+1} - x_n\vert < \varepsilon$: terminar |
| 6 | **Repetir** | Desde paso 2 |

### Pseudocódigo

```python
def newton_raphson(f, df, x0, tol=1e-10, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        if abs(dfx) < 1e-14:
            raise ValueError("Derivada muy pequeña")
        
        x_new = x - fx / dfx
        
        if abs(x_new - x) < tol:
            return x_new, i + 1
        
        x = x_new
    
    return x, max_iter
```

### Ejemplo Detallado

**Problema:** Calcular $\sqrt{2}$ resolviendo $f(x) = x^2 - 2 = 0$

---

$f(x) = x^2 - 2$, $f'(x) = 2x$

Fórmula: $x_{n+1} = x_n - \frac{x_n^2 - 2}{2x_n} = \frac{x_n^2 + 2}{2x_n} = \frac{x_n + 2/x_n}{2}$

---

**Iteraciones con** $x_0 = 1$:

| $n$ | $x_n$ | $f(x_n)$ | $f'(x_n)$ | $x_{n+1}$ | Error |
|:---:|:-----:|:--------:|:---------:|:---------:|:-----:|
| 0 | 1.000000 | -1.000 | 2.000 | 1.500000 | 0.500 |
| 1 | 1.500000 | 0.250 | 3.000 | 1.416667 | 0.083 |
| 2 | 1.416667 | 0.00694 | 2.833 | 1.414216 | 0.00245 |
| 3 | 1.414216 | 0.00001 | 2.828 | 1.414214 | 0.000002 |

$$\boxed{\sqrt{2} \approx 1.41421356}$$

---

**Convergencia cuadrática:** El error en cada paso es aproximadamente el cuadrado del error anterior.

$e_1 \approx 0.086$, $e_2 \approx 0.0025 \approx (0.086)^2 \times 0.35$

---

### Análisis de Convergencia

$$e_{n+1} \approx \frac{f''(x^*)}{2f'(x^*)} e_n^2$$

**Convergencia garantizada si:**
- $x_0$ suficientemente cerca de $x^*$
- $f'(x^*) \neq 0$
- $f''$ continua cerca de $x^*$

---

## Método 4: Secante

### Cuándo Usar

- No se tiene $f'(x)$ disponible
- Se desea convergencia más rápida que bisección
- Se tienen dos puntos iniciales

### Fórmula

$$x_{n+1} = x_n - f(x_n)\frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}$$

### Interpretación

Aproxima $f'(x_n)$ con la diferencia finita $\frac{f(x_n) - f(x_{n-1})}{x_n - x_{n-1}}$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Elegir** | Dos puntos $x_0$, $x_1$ |
| 2 | **Evaluar** | $f(x_n)$ y $f(x_{n-1})$ |
| 3 | **Calcular** | $x_{n+1} = x_n - f(x_n)\frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}$ |
| 4 | **Verificar** | Si $\vert x_{n+1} - x_n\vert < \varepsilon$: terminar |
| 5 | **Actualizar** | $x_{n-1} = x_n$, $x_n = x_{n+1}$ |
| 6 | **Repetir** | Desde paso 2 |

### Pseudocódigo

```python
def secante(f, x0, x1, tol=1e-10, max_iter=100):
    f0, f1 = f(x0), f(x1)
    
    for i in range(max_iter):
        if abs(f1 - f0) < 1e-14:
            raise ValueError("División por cero")
        
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        
        if abs(x2 - x1) < tol:
            return x2, i + 1
        
        x0, f0 = x1, f1
        x1, f1 = x2, f(x2)
    
    return x1, max_iter
```

### Ejemplo Detallado

**Problema:** Resolver $f(x) = x^3 - x - 2 = 0$ con $x_0 = 1$, $x_1 = 2$

---

| $n$ | $x_{n-1}$ | $x_n$ | $f(x_{n-1})$ | $f(x_n)$ | $x_{n+1}$ |
|:---:|:---------:|:-----:|:------------:|:--------:|:---------:|
| 2 | 1.000 | 2.000 | -2.000 | 4.000 | 1.333 |
| 3 | 2.000 | 1.333 | 4.000 | -0.963 | 1.511 |
| 4 | 1.333 | 1.511 | -0.963 | -0.057 | 1.520 |
| 5 | 1.511 | 1.520 | -0.057 | -0.008 | 1.521 |
| 6 | 1.520 | 1.521 | -0.008 | 0.0003 | 1.5214 |

$$\boxed{x^* \approx 1.52138}$$

---

**[Orden de convergencia](../../../glossary.md#orden-de-convergencia):** $p = \frac{1 + \sqrt{5}}{2} \approx 1.618$ (número áureo)

---

## Método 5: Punto Fijo

### Cuándo Usar

- La ecuación se puede escribir como $x = g(x)$
- Para entender convergencia de otros métodos
- Como técnica general de iteración

### Fórmula

$$x_{n+1} = g(x_n)$$

### Condición de Convergencia

Si $|g'(x)| < 1$ en un entorno de la raíz $x^*$, entonces el método converge para puntos iniciales suficientemente cercanos.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Reformular** | $f(x) = 0$ como $x = g(x)$ |
| 2 | **Verificar** | $\vert g'(x^*)\vert < 1$ (si es posible) |
| 3 | **Elegir** | Punto inicial $x_0$ |
| 4 | **Calcular** | $x_{n+1} = g(x_n)$ |
| 5 | **Verificar** | Si $\vert x_{n+1} - x_n\vert < \varepsilon$: terminar |
| 6 | **Repetir** | Desde paso 4 |

### Pseudocódigo

```python
def punto_fijo(g, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        
        if abs(x_new - x) < tol:
            return x_new, i + 1
        
        x = x_new
    
    return x, max_iter
```

### Ejemplo Detallado

**Problema:** Resolver $e^{-x} - x = 0$

---

**Reformulación:** $x = e^{-x} = g(x)$

**Verificar convergencia:**
$g'(x) = -e^{-x}$
$|g'(0.5)| = e^{-0.5} \approx 0.607 < 1$ ✓

---

**Iteraciones con** $x_0 = 0.5$:

| $n$ | $x_n$ | $g(x_n) = e^{-x_n}$ | $\vert x_{n+1} - x_n\vert$ |
|:---:|:-----:|:-------------------:|:--------------------------:|
| 0 | 0.5000 | 0.6065 | 0.1065 |
| 1 | 0.6065 | 0.5452 | 0.0613 |
| 2 | 0.5452 | 0.5797 | 0.0345 |
| 3 | 0.5797 | 0.5601 | 0.0196 |
| 4 | 0.5601 | 0.5711 | 0.0111 |
| 5 | 0.5711 | 0.5649 | 0.0062 |
| ... | ... | ... | ... |
| 20 | 0.5671 | 0.5671 | < 0.0001 |

$$\boxed{x^* \approx 0.56714}$$

---

### Diferentes Reformulaciones

Para $x^3 - x - 2 = 0$:

1. $x = x^3 - 2$ → $g'(x) = 3x^2$ → diverge cerca de $x = 1.5$
2. $x = (x + 2)^{1/3}$ → $g'(x) = \frac{1}{3}(x+2)^{-2/3}$ → converge
3. $x = \frac{2}{x^2 - 1}$ → puede converger o diverger

---

## Método 6: Newton Modificado (Raíces Múltiples)

### Cuándo Usar

- Raíz de multiplicidad $m > 1$
- Newton estándar converge lentamente

### Fórmula (Conociendo Multiplicidad)

$$x_{n+1} = x_n - m\frac{f(x_n)}{f'(x_n)}$$

### Fórmula (Sin Conocer Multiplicidad)

Usar $u(x) = \frac{f(x)}{f'(x)}$ que tiene raíces simples:

$$x_{n+1} = x_n - \frac{u(x_n)}{u'(x_n)} = x_n - \frac{f(x_n)f'(x_n)}{[f'(x_n)]^2 - f(x_n)f''(x_n)}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Detectar** | Si Newton converge lentamente, sospechar raíz múltiple |
| 2 | **Estimar** $m$ | $m \approx \frac{f(x_n)}{f(x_n) - f(x_{n+1})}$ en Newton estándar |
| 3 | **Aplicar** | Newton modificado con $m$ o usar $u(x)$ |
| 4 | **Verificar** | Convergencia cuadrática restaurada |

### Ejemplo Detallado

**Problema:** Encontrar la raíz de $f(x) = (x-1)^3 = x^3 - 3x^2 + 3x - 1$

---

**Newton estándar** (convergencia lineal):

$f'(x) = 3(x-1)^2$

| $n$ | $x_n$ | Error |
|:---:|:-----:|:-----:|
| 0 | 2.000 | 1.000 |
| 1 | 1.667 | 0.667 |
| 2 | 1.444 | 0.444 |
| 3 | 1.296 | 0.296 |

Convergencia lenta → raíz múltiple

---

**Newton modificado con** $m = 3$:

$$x_{n+1} = x_n - 3\frac{f(x_n)}{f'(x_n)}$$

| $n$ | $x_n$ | Error |
|:---:|:-----:|:-----:|
| 0 | 2.000 | 1.000 |
| 1 | 1.000 | 0.000 |

$$\boxed{x^* = 1 \text{ (convergencia en 1 iteración)}}$$

---

## Método 7: Müller

### Cuándo Usar

- Puede encontrar raíces complejas
- No requiere [derivada](../../../glossary.md#derivada)
- Usa [interpolación](../../../glossary.md#interpolacion) parabólica

### Fórmula

Dados tres puntos $x_0, x_1, x_2$, ajustar parábola y encontrar raíz:

$$x_3 = x_2 - \frac{2c}{b \pm \sqrt{b^2 - 4ac}}$$

donde $a, b, c$ son coeficientes de la parábola $p(x) = a(x-x_2)^2 + b(x-x_2) + c$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Elegir** | Tres puntos $x_0, x_1, x_2$ |
| 2 | **Calcular** | $f_0, f_1, f_2$ |
| 3 | **Calcular** | $h_0 = x_1 - x_0$, $h_1 = x_2 - x_1$ |
| 4 | **Calcular** | Diferencias divididas |
| 5 | **Formar** | Coeficientes $a, b, c$ |
| 6 | **Resolver** | Para $x_3$ |
| 7 | **Actualizar** | $(x_0, x_1, x_2) \leftarrow (x_1, x_2, x_3)$ |

### Pseudocódigo

```python
def muller(f, x0, x1, x2, tol=1e-10, max_iter=100):
    for i in range(max_iter):
        f0, f1, f2 = f(x0), f(x1), f(x2)
        
        h1 = x1 - x0
        h2 = x2 - x1
        delta1 = (f1 - f0) / h1
        delta2 = (f2 - f1) / h2
        
        a = (delta2 - delta1) / (h2 + h1)
        b = a * h2 + delta2
        c = f2
        
        discriminante = cmath.sqrt(b**2 - 4*a*c)
        
        if abs(b + discriminante) > abs(b - discriminante):
            denom = b + discriminante
        else:
            denom = b - discriminante
        
        dx = -2 * c / denom
        x3 = x2 + dx
        
        if abs(dx) < tol:
            return x3, i + 1
        
        x0, x1, x2 = x1, x2, x3
    
    return x2, max_iter
```

### Ejemplo

**Problema:** Encontrar raíces de $f(x) = x^3 - 1$ (incluye complejas)

Con puntos iniciales reales, Müller puede encontrar raíces complejas:

$$x = 1, \quad x = -\frac{1}{2} + \frac{\sqrt{3}}{2}i, \quad x = -\frac{1}{2} - \frac{\sqrt{3}}{2}i$$

---

## Método 8: Steffensen

### Cuándo Usar

- Para acelerar punto fijo a convergencia cuadrática
- Sin calcular [derivada](../../../glossary.md#derivada)

### Fórmula (Aceleración de Aitken)

$$x_{n+1} = x_n - \frac{(x_n^{(1)} - x_n)^2}{x_n^{(2)} - 2x_n^{(1)} + x_n}$$

donde $x_n^{(1)} = g(x_n)$ y $x_n^{(2)} = g(x_n^{(1)})$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Calcular** | $x^{(1)} = g(x_n)$ |
| 2 | **Calcular** | $x^{(2)} = g(x^{(1)})$ |
| 3 | **Aplicar Aitken** | $x_{n+1} = x_n - \frac{(x^{(1)} - x_n)^2}{x^{(2)} - 2x^{(1)} + x_n}$ |
| 4 | **Verificar** | Convergencia |

### Pseudocódigo

```python
def steffensen(g, x0, tol=1e-10, max_iter=100):
    x = x0
    for i in range(max_iter):
        x1 = g(x)
        x2 = g(x1)
        
        denom = x2 - 2*x1 + x
        if abs(denom) < 1e-14:
            return x1, i + 1
        
        x_new = x - (x1 - x)**2 / denom
        
        if abs(x_new - x) < tol:
            return x_new, i + 1
        
        x = x_new
    
    return x, max_iter
```

### Ejemplo Detallado

**Problema:** Resolver $e^{-x} = x$ con $g(x) = e^{-x}$

---

**Punto fijo estándar:** ~20 iteraciones
**Steffensen:** ~5 iteraciones

| $n$ | $x_n$ | $x^{(1)}$ | $x^{(2)}$ | $x_{n+1}$ |
|:---:|:-----:|:---------:|:---------:|:---------:|
| 0 | 0.500 | 0.6065 | 0.5452 | 0.5663 |
| 1 | 0.5663 | 0.5676 | 0.5669 | 0.5671 |
| 2 | 0.5671 | 0.5671 | 0.5671 | 0.5671 |

$$\boxed{x^* \approx 0.56714}$$

---

## Método 9: Brent

### Cuándo Usar

- Método robusto de propósito general
- Combina bisección, secante y cuadrática inversa
- Implementación estándar en bibliotecas

### Idea Principal

1. Mantener intervalo que encierra la raíz (como bisección)
2. Usar [interpolación](../../../glossary.md#interpolacion) cuando es seguro y efectivo
3. Revertir a bisección si el progreso es insuficiente

### Características

| Propiedad | Valor |
|-----------|-------|
| Garantía de convergencia | ✓ |
| [Orden](../../../glossary.md#orden) de convergencia | Variable |
| Robustez | Muy alta |
| Eficiencia | Alta |

---

## Método 10: Newton para Sistemas No Lineales

### Cuándo Usar
- Resolver $\mathbf{F}(\mathbf{x}) = \mathbf{0}$
- Sistema de ecuaciones no lineales

### Fórmula
$$\mathbf{x}_{n+1} = \mathbf{x}_n - \mathbf{J}^{-1}(\mathbf{x}_n)\mathbf{F}(\mathbf{x}_n)$$

donde $\mathbf{J}$ es la [matriz](../../../glossary.md#matriz) jacobiana:

$$J_{ij} = \frac{\partial F_i}{\partial x_j}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Evaluar** | $\mathbf{F}(\mathbf{x}_n)$ |
| 2 | **Calcular** | Jacobiano $\mathbf{J}(\mathbf{x}_n)$ |
| 3 | **Resolver** | $\mathbf{J}\Delta\mathbf{x} = -\mathbf{F}$ |
| 4 | **Actualizar** | $\mathbf{x}_{n+1} = \mathbf{x}_n + \Delta\mathbf{x}$ |
| 5 | **Verificar** | $\|\Delta\mathbf{x}\| < \varepsilon$ |

### Ejemplo Detallado

**Problema:** Resolver el sistema
$$\begin{cases} x^2 + y^2 = 4 \\ xy = 1 \end{cases}$$

---

$F_1(x,y) = x^2 + y^2 - 4$
$F_2(x,y) = xy - 1$

**Jacobiano:**
$$\mathbf{J} = \begin{pmatrix} 2x & 2y \\ y & x \end{pmatrix}$$

---

**Iteración con** $\mathbf{x}_0 = (1.5, 1.5)$:

$\mathbf{F}(\mathbf{x}_0) = (0.5, 1.25)$

$\mathbf{J}(\mathbf{x}_0) = \begin{pmatrix} 3 & 3 \\ 1.5 & 1.5 \end{pmatrix}$

Resolver: $\begin{pmatrix} 3 & 3 \\ 1.5 & 1.5 \end{pmatrix}\begin{pmatrix} \Delta x \\ \Delta y \end{pmatrix} = \begin{pmatrix} -0.5 \\ -1.25 \end{pmatrix}$

La [matriz](../../../glossary.md#matriz) es singular en este punto, necesitamos mejor punto inicial.

---

**Con** $\mathbf{x}_0 = (1.8, 0.6)$:

Después de 4-5 iteraciones:

$$\boxed{(x^*, y^*) \approx (1.9319, 0.5176)}$$

---

## Diagrama de Decisión

```
┌─────────────────────────────────────────────┐
│       ENCONTRAR RAÍZ DE f(x) = 0            │
└─────────────────────────────────────────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │ ¿Conoces [a,b] con    │
        │ f(a)·f(b) < 0?        │
        └───────────────────────┘
                    │
          SÍ────────┴────────NO
          │                   │
          ▼                   ▼
    ┌───────────┐      ┌───────────┐
    │¿Necesitas │      │¿Tienes    │
    │garantía?  │      │f'(x)?     │
    └───────────┘      └───────────┘
          │                   │
     SÍ───┴───NO        SÍ───┴───NO
     │        │         │        │
     ▼        ▼         ▼        ▼
  Bisección  Brent   Newton   Secante
             Falsa            Punto
             Posición         Fijo
```

---

## Tabla de Comparación

| Método | Convergencia | Evaluaciones/iter | Robusto | Derivada |
|--------|:------------:|:-----------------:|:-------:|:--------:|
| Bisección | Lineal | 1 | ✓✓✓ | No |
| Falsa Posición | Superlineal | 1 | ✓✓ | No |
| Newton | Cuadrática | 2 | ✓ | Sí |
| Secante | 1.618 | 1 | ✓ | No |
| Punto Fijo | Lineal | 1 | ✓ | No |
| Steffensen | Cuadrática | 2 | ✓ | No |
| Müller | 1.84 | 1 | ✓ | No |
| Brent | Superlineal | 1-2 | ✓✓✓ | No |

---

## Errores Comunes a Evitar

| Error | Consecuencia | Prevención |
|-------|--------------|------------|
| División por cero en Newton | Falla del método | Verificar $f'(x_n) \neq 0$ |
| Mal punto inicial | No convergencia | Graficar primero |
| Intervalo sin cambio de signo | Bisección falla | Verificar $f(a)f(b) < 0$ |
| $\vert g'\vert \geq 1$ en punto fijo | [Divergencia](../../../glossary.md#maquina) |

---

## Problemas de Práctica Sugeridos

1. **Bisección:** $\cos x - x = 0$ en $[0, 1]$

2. **Newton:** $x^3 - 2x - 5 = 0$ con $x_0 = 2$

3. **Secante:** $e^x + x = 0$ con $x_0 = 0$, $x_1 = -1$

4. **Punto fijo:** Diferentes reformulaciones de $x^3 = 2x + 5$

5. **Sistema:** $x^2 - y = 0$, $x + y^2 = 2$

6. **Raíz múltiple:** $(x - 2)^2(x + 1) = 0$

---

*Documento actualizado con formato expandido para estudio detallado.*
