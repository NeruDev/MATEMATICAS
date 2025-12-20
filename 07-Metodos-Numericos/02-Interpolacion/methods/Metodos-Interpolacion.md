<!--
content_type: methods
topic: Interpolación
---
-->

# Métodos: Interpolación

---

## Método 1: Interpolación de Lagrange

### Algoritmo Paso a Paso

**Entrada:** Puntos $(x_0, y_0), ..., (x_n, y_n)$, valor $x$ a evaluar

**Paso 1:** Para cada $i = 0, ..., n$, calcular $L_i(x)$:
$$L_i(x) = \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}$$

**Paso 2:** Calcular el resultado:
$$P(x) = \sum_{i=0}^{n} y_i L_i(x)$$

### Pseudocódigo

```python
def lagrange(x_data, y_data, x):
    n = len(x_data)
    resultado = 0
    
    for i in range(n):
        Li = 1
        for j in range(n):
            if j != i:
                Li *= (x - x_data[j]) / (x_data[i] - x_data[j])
        resultado += y_data[i] * Li
    
    return resultado
```

### Ejemplo Completo

**Interpolar en $x = 1.5$ usando $(0, 1), (1, 3), (2, 2)$**

$$L_0(1.5) = \frac{(1.5-1)(1.5-2)}{(0-1)(0-2)} = \frac{0.5 \cdot (-0.5)}{2} = -0.125$$

$$L_1(1.5) = \frac{(1.5-0)(1.5-2)}{(1-0)(1-2)} = \frac{1.5 \cdot (-0.5)}{-1} = 0.75$$

$$L_2(1.5) = \frac{(1.5-0)(1.5-1)}{(2-0)(2-1)} = \frac{1.5 \cdot 0.5}{2} = 0.375$$

$$P(1.5) = 1(-0.125) + 3(0.75) + 2(0.375) = -0.125 + 2.25 + 0.75 = 2.875$$

---

## Método 2: Diferencias Divididas de Newton

### Algoritmo Paso a Paso

**Entrada:** Puntos $(x_0, y_0), ..., (x_n, y_n)$

**Paso 1:** Construir tabla de diferencias divididas:
- Primera columna: $f[x_i] = y_i$
- Siguiente columna: $f[x_i, x_{i+1}] = \frac{f[x_{i+1}] - f[x_i]}{x_{i+1} - x_i}$
- Continuar recursivamente

**Paso 2:** Leer los coeficientes de la diagonal principal.

**Paso 3:** Construir el polinomio:
$$P(x) = a_0 + a_1(x-x_0) + a_2(x-x_0)(x-x_1) + ...$$

### Pseudocódigo

```python
def diferencias_divididas(x_data, y_data):
    n = len(x_data)
    # Crear tabla
    tabla = [[0] * n for _ in range(n)]
    
    # Primera columna
    for i in range(n):
        tabla[i][0] = y_data[i]
    
    # Llenar tabla
    for j in range(1, n):
        for i in range(n - j):
            tabla[i][j] = (tabla[i+1][j-1] - tabla[i][j-1]) / (x_data[i+j] - x_data[i])
    
    # Coeficientes (primera fila)
    return [tabla[0][j] for j in range(n)]

def evaluar_newton(coefs, x_data, x):
    n = len(coefs)
    resultado = coefs[n-1]
    for i in range(n-2, -1, -1):
        resultado = resultado * (x - x_data[i]) + coefs[i]
    return resultado
```

### Ejemplo Completo

**Datos:** $(1, 0), (2, 1), (4, 2)$

**Tabla de diferencias divididas:**

| $x_i$ | $f[x_i]$ | $f[x_i, x_{i+1}]$ | $f[x_i, x_{i+1}, x_{i+2}]$ |
|-------|----------|-------------------|----------------------------|
| 1 | 0 | | |
| 2 | 1 | $\frac{1-0}{2-1} = 1$ | |
| 4 | 2 | $\frac{2-1}{4-2} = 0.5$ | $\frac{0.5-1}{4-1} = -\frac{1}{6}$ |

**Coeficientes:** $a_0 = 0$, $a_1 = 1$, $a_2 = -\frac{1}{6}$

**Polinomio:**
$$P(x) = 0 + 1(x-1) - \frac{1}{6}(x-1)(x-2)$$

---

## Método 3: Newton Progresivo (Datos Equiespaciados)

### Algoritmo Paso a Paso

**Entrada:** Puntos con $x_i = x_0 + ih$, valores $y_0, ..., y_n$

**Paso 1:** Calcular diferencias finitas progresivas:
$$\Delta y_i = y_{i+1} - y_i$$
$$\Delta^2 y_i = \Delta y_{i+1} - \Delta y_i$$

**Paso 2:** Calcular $s = \frac{x - x_0}{h}$

**Paso 3:** Evaluar:
$$P(x) = y_0 + \binom{s}{1}\Delta y_0 + \binom{s}{2}\Delta^2 y_0 + ...$$

### Ejemplo Completo

**Datos:** $h = 1$, puntos $(0, 1), (1, 2), (2, 5), (3, 10)$

**Tabla de diferencias:**

| $x$ | $y$ | $\Delta y$ | $\Delta^2 y$ | $\Delta^3 y$ |
|-----|-----|------------|--------------|--------------|
| 0 | 1 | | | |
| 1 | 2 | 1 | | |
| 2 | 5 | 3 | 2 | |
| 3 | 10 | 5 | 2 | 0 |

**Para $x = 1.5$:** $s = \frac{1.5 - 0}{1} = 1.5$

$$P(1.5) = 1 + 1.5(1) + \frac{1.5(0.5)}{2}(2) + \frac{1.5(0.5)(-0.5)}{6}(0)$$
$$= 1 + 1.5 + 0.75 = 3.25$$

---

## Método 4: Splines Cúbicos Naturales

### Algoritmo Paso a Paso

**Entrada:** Puntos $(x_0, y_0), ..., (x_n, y_n)$

**Paso 1:** Calcular $h_i = x_{i+1} - x_i$

**Paso 2:** Formar el sistema tridiagonal para $c_i$ (segunda derivada/2):

$$h_{i-1}c_{i-1} + 2(h_{i-1} + h_i)c_i + h_i c_{i+1} = 3\left(\frac{y_{i+1}-y_i}{h_i} - \frac{y_i - y_{i-1}}{h_{i-1}}\right)$$

Con $c_0 = c_n = 0$ (spline natural)

**Paso 3:** Resolver el sistema (Thomas algorithm)

**Paso 4:** Calcular los demás coeficientes:
$$a_i = y_i$$
$$b_i = \frac{y_{i+1} - y_i}{h_i} - \frac{h_i}{3}(2c_i + c_{i+1})$$
$$d_i = \frac{c_{i+1} - c_i}{3h_i}$$

**Paso 5:** El spline en $[x_i, x_{i+1}]$ es:
$$S_i(x) = a_i + b_i(x-x_i) + c_i(x-x_i)^2 + d_i(x-x_i)^3$$

### Pseudocódigo (Simplificado)

```python
def spline_cubico(x_data, y_data):
    n = len(x_data) - 1
    h = [x_data[i+1] - x_data[i] for i in range(n)]
    
    # Sistema tridiagonal
    # ... resolver para c[i] ...
    
    # Calcular coeficientes
    a = y_data[:-1]
    b = [(y_data[i+1]-y_data[i])/h[i] - h[i]*(2*c[i]+c[i+1])/3 
         for i in range(n)]
    d = [(c[i+1]-c[i])/(3*h[i]) for i in range(n)]
    
    return a, b, c[:-1], d
```

### Ejemplo Simplificado

**Datos:** $(0, 0), (1, 1), (2, 0)$ con $h = 1$

Sistema (con $c_0 = c_2 = 0$):
$$4c_1 = 3\left(\frac{0-1}{1} - \frac{1-0}{1}\right) = 3(-2) = -6$$
$$c_1 = -1.5$$

**Coeficientes para $[0, 1]$:**
- $a_0 = 0$
- $b_0 = \frac{1-0}{1} - \frac{1}{3}(0 + (-1.5)) = 1 + 0.5 = 1.5$
- $c_0 = 0$
- $d_0 = \frac{-1.5 - 0}{3} = -0.5$

$$S_0(x) = 1.5x - 0.5x^3$$

---

## Método 5: Interpolación de Hermite

### Algoritmo Paso a Paso

**Entrada:** Puntos $(x_i, y_i)$ y derivadas $y'_i$

**Paso 1:** Construir tabla de diferencias divididas ampliada (duplicando puntos)

**Paso 2:** Cuando aparecen $f[x_i, x_i]$, usar $f'(x_i)$

**Paso 3:** Construir polinomio de Newton con los coeficientes obtenidos

### Ejemplo

**Datos:** $(0, 0, 1), (1, 1, 0)$ (valor y derivada en cada punto)

Tabla ampliada con puntos: $0, 0, 1, 1$

| $z$ | $f[z]$ | 1er orden | 2do orden | 3er orden |
|-----|--------|-----------|-----------|-----------|
| 0 | 0 | | | |
| 0 | 0 | 1 (=f'(0)) | | |
| 1 | 1 | 1 | 0 | |
| 1 | 1 | 0 (=f'(1)) | -1 | -1 |

$$H(x) = 0 + 1 \cdot x + 0 \cdot x^2 + (-1) \cdot x^2(x-1) = x - x^2(x-1)$$
$$= x - x^3 + x^2 = -x^3 + x^2 + x$$

---

## Tabla de Comparación de Métodos

| Método | Complejidad | Ventaja | Desventaja |
|--------|-------------|---------|------------|
| Lagrange | $O(n^2)$ | Simple, directo | Recalcular todo al agregar punto |
| Newton DD | $O(n^2)$ | Fácil agregar puntos | Más pasos |
| Newton Prog. | $O(n^2)$ | Simple para equiespaciados | Solo equiespaciados |
| Splines | $O(n)$ | Suave, estable | Más complejo |
| Hermite | $O(n^2)$ | Usa derivadas | Requiere más datos |

---

## Diagrama de Decisión

```
INTERPOLACIÓN
     │
     ▼
¿Cuántos puntos?
     │
  ≤5─┴─>5
  │      │
  ▼      ▼
Lagrange  ¿Datos equiespaciados?
o Newton       │
          SÍ──┴──NO
          │       │
          ▼       ▼
       Newton   ¿Necesitas suavidad?
      Progresivo     │
                SÍ──┴──NO
                │       │
                ▼       ▼
             Splines  Newton DD
```
