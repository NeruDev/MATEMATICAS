<!--
content_type: methods
topic: Raíces de Ecuaciones
---
-->

# Métodos: Raíces de Ecuaciones

---

## Método 1: Bisección

### Algoritmo Paso a Paso

**Entrada:** $f$, $a$, $b$, tolerancia $\varepsilon$, máximo iteraciones $N$

**Paso 1:** Verificar $f(a) \cdot f(b) < 0$

**Paso 2:** Para $i = 1, 2, ..., N$:
1. $c = \frac{a + b}{2}$
2. Si $|b - a| < 2\varepsilon$ → **return** $c$
3. Si $f(a) \cdot f(c) < 0$ → $b = c$
4. Si no → $a = c$

**Paso 3:** Si no converge → **error**

### Pseudocódigo

```python
def biseccion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos")
    
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(b - a) < 2 * tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    raise RuntimeError("No convergió")
```

### Ejemplo Completo

**Encontrar la raíz de $f(x) = x^3 - x - 2$ en $[1, 2]$**

| $n$ | $a$ | $b$ | $c$ | $f(c)$ | Nuevo intervalo |
|-----|-----|-----|-----|--------|-----------------|
| 1 | 1.0 | 2.0 | 1.5 | -0.125 | $[1.5, 2.0]$ |
| 2 | 1.5 | 2.0 | 1.75 | 1.609 | $[1.5, 1.75]$ |
| 3 | 1.5 | 1.75 | 1.625 | 0.666 | $[1.5, 1.625]$ |
| 4 | 1.5 | 1.625 | 1.5625 | 0.252 | $[1.5, 1.5625]$ |
| 5 | 1.5 | 1.5625 | 1.5313 | 0.059 | $[1.5, 1.5313]$ |

**Raíz aproximada:** $x^* \approx 1.5214$

---

## Método 2: Newton-Raphson

### Algoritmo Paso a Paso

**Entrada:** $f$, $f'$, $x_0$, tolerancia $\varepsilon$, máximo iteraciones $N$

**Paso 1:** Para $i = 1, 2, ..., N$:
1. $x_{i} = x_{i-1} - \frac{f(x_{i-1})}{f'(x_{i-1})}$
2. Si $|x_i - x_{i-1}| < \varepsilon$ → **return** $x_i$

**Paso 2:** Si no converge → **error**

### Pseudocódigo

```python
def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-12:
            raise ValueError("Derivada muy pequeña")
        
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    
    raise RuntimeError("No convergió")
```

### Ejemplo Completo

**Encontrar $\sqrt{2}$ resolviendo $f(x) = x^2 - 2 = 0$**

$f(x) = x^2 - 2$, $f'(x) = 2x$, $x_0 = 1$

| $n$ | $x_n$ | $f(x_n)$ | $f'(x_n)$ | $x_{n+1}$ | Error |
|-----|-------|----------|-----------|-----------|-------|
| 0 | 1.0 | -1.0 | 2.0 | 1.5 | 0.5 |
| 1 | 1.5 | 0.25 | 3.0 | 1.4167 | 0.0833 |
| 2 | 1.4167 | 0.0069 | 2.8333 | 1.4142 | 0.0025 |
| 3 | 1.4142 | 0.00006 | 2.8284 | 1.41421356 | 0.00002 |

**Convergencia cuadrática:** El número de dígitos correctos se duplica en cada iteración.

---

## Método 3: Secante

### Algoritmo Paso a Paso

**Entrada:** $f$, $x_0$, $x_1$, tolerancia $\varepsilon$, máximo iteraciones $N$

**Paso 1:** Para $i = 2, 3, ..., N$:
1. $x_i = x_{i-1} - f(x_{i-1})\frac{x_{i-1} - x_{i-2}}{f(x_{i-1}) - f(x_{i-2})}$
2. Si $|x_i - x_{i-1}| < \varepsilon$ → **return** $x_i$

### Pseudocódigo

```python
def secante(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        fx0, fx1 = f(x0), f(x1)
        if abs(fx1 - fx0) < 1e-12:
            raise ValueError("División por cero")
        
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    
    raise RuntimeError("No convergió")
```

### Ejemplo Completo

**Resolver $f(x) = x^3 - x - 2 = 0$ con $x_0 = 1$, $x_1 = 2$**

| $n$ | $x_{n-1}$ | $x_n$ | $f(x_n)$ | $x_{n+1}$ |
|-----|-----------|-------|----------|-----------|
| 2 | 1.0 | 2.0 | 4.0 | 1.4 |
| 3 | 2.0 | 1.4 | -0.656 | 1.5610 |
| 4 | 1.4 | 1.5610 | 0.2424 | 1.5179 |
| 5 | 1.5610 | 1.5179 | -0.0196 | 1.5213 |

---

## Método 4: Punto Fijo

### Algoritmo Paso a Paso

**Entrada:** $g$, $x_0$, tolerancia $\varepsilon$, máximo iteraciones $N$

**Paso 1:** Para $i = 1, 2, ..., N$:
1. $x_i = g(x_{i-1})$
2. Si $|x_i - x_{i-1}| < \varepsilon$ → **return** $x_i$

### Cómo Construir $g(x)$

Para $f(x) = 0$, posibles reformulaciones:
1. $x = x - f(x)$ (no siempre converge)
2. $x = x - cf(x)$ donde $c$ se elige para convergencia
3. Despejar $x$ de alguna manera

**Criterio:** $|g'(x^*)| < 1$ garantiza convergencia local

### Ejemplo Completo

**Resolver $e^{-x} - x = 0$**

Reformulación: $x = e^{-x}$, es decir, $g(x) = e^{-x}$

Verificar: $g'(x) = -e^{-x}$, $|g'(0.5)| \approx 0.6 < 1$ ✓

| $n$ | $x_n$ | $g(x_n) = e^{-x_n}$ | Error |
|-----|-------|---------------------|-------|
| 0 | 0.5 | 0.6065 | - |
| 1 | 0.6065 | 0.5452 | 0.0613 |
| 2 | 0.5452 | 0.5797 | 0.0345 |
| 3 | 0.5797 | 0.5601 | 0.0196 |
| ... | ... | ... | ... |
| 15 | 0.5671 | 0.5671 | < 0.0001 |

**Raíz:** $x^* \approx 0.5671$

---

## Método 5: Falsa Posición (Regula Falsi)

### Algoritmo Paso a Paso

**Entrada:** $f$, $a$, $b$, tolerancia $\varepsilon$, máximo iteraciones $N$

**Paso 1:** Verificar $f(a) \cdot f(b) < 0$

**Paso 2:** Para $i = 1, 2, ..., N$:
1. $c = b - f(b)\frac{b - a}{f(b) - f(a)}$
2. Si $|f(c)| < \varepsilon$ → **return** $c$
3. Si $f(a) \cdot f(c) < 0$ → $b = c$
4. Si no → $a = c$

### Comparación con Bisección

**Bisección:** Siempre divide por 2
**Falsa posición:** Usa interpolación lineal

Generalmente más rápido, pero puede quedar "atascado" si un extremo no se mueve.

---

## Método 6: Newton Modificado (Raíces Múltiples)

### Fórmula

Para raíz de multiplicidad $m$:
$$x_{n+1} = x_n - m\frac{f(x_n)}{f'(x_n)}$$

O usar la función $u(x) = \frac{f(x)}{f'(x)}$ que tiene raíces simples:
$$x_{n+1} = x_n - \frac{u(x_n)}{u'(x_n)} = x_n - \frac{f(x_n)f'(x_n)}{[f'(x_n)]^2 - f(x_n)f''(x_n)}$$

---

## Diagrama de Decisión

```
ENCONTRAR RAÍZ DE f(x) = 0
          │
          ▼
   ¿Puedes encontrar
   [a,b] con f(a)·f(b) < 0?
          │
    SÍ────┴────NO
    │          │
    ▼          ▼
¿Necesitas    ¿Tienes f'(x)?
garantía?          │
    │        SÍ───┴───NO
 SÍ─┴─NO     │         │
 │     │     ▼         ▼
 ▼     ▼  Newton    Secante
Bisec. Falsa      (2 puntos
       Posición    iniciales)
```

---

## Tabla de Referencia Rápida

| Método | Fórmula | Convergencia | Req. |
|--------|---------|--------------|------|
| Bisección | $c = \frac{a+b}{2}$ | Lineal | [a,b], signo |
| Falsa Pos. | $c = b - f(b)\frac{b-a}{f(b)-f(a)}$ | Lineal | [a,b], signo |
| Newton | $x = x - \frac{f}{f'}$ | Cuadrática | $f'$, $x_0$ |
| Secante | $x = x_1 - f_1\frac{x_1-x_0}{f_1-f_0}$ | 1.618 | $x_0$, $x_1$ |
| Punto fijo | $x = g(x)$ | Lineal | $|g'|<1$ |
