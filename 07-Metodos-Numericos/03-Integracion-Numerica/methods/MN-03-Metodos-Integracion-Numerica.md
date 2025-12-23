<!--
content_type: methods
topic: Integración Numérica
---
-->

# Métodos: Integración Numérica

---

## Método 1: Regla del Trapecio Simple

### Fórmula

$$\int_a^b f(x)\,dx \approx \frac{b-a}{2}[f(a) + f(b)]$$

### Algoritmo

```python
def trapecio_simple(f, a, b):
    return (b - a) / 2 * (f(a) + f(b))
```

### Ejemplo

**Calcular $\int_0^1 e^x\,dx$**

$$I \approx \frac{1-0}{2}[e^0 + e^1] = \frac{1}{2}[1 + 2.7183] = 1.8591$$

Valor exacto: $e - 1 = 1.7183$

Error: $|1.8591 - 1.7183| = 0.1408$

---

## Método 2: Trapecio Compuesto

### Fórmula

Con $n$ subintervalos y $h = \frac{b-a}{n}$:

$$I \approx \frac{h}{2}\left[f(a) + 2\sum_{i=1}^{n-1} f(a + ih) + f(b)\right]$$

### Algoritmo

```python
def trapecio_compuesto(f, a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        suma += 2 * f(a + i * h)
    return h / 2 * suma
```

### Ejemplo Completo

**Calcular $\int_0^1 e^x\,dx$ con $n = 4$**

$h = 0.25$, puntos: $0, 0.25, 0.5, 0.75, 1$

| $x_i$ | $f(x_i) = e^{x_i}$ | Coef. | Contribución |
|-------|---------------------|-------|--------------|
| 0 | 1.0000 | 1 | 1.0000 |
| 0.25 | 1.2840 | 2 | 2.5681 |
| 0.5 | 1.6487 | 2 | 3.2974 |
| 0.75 | 2.1170 | 2 | 4.2340 |
| 1 | 2.7183 | 1 | 2.7183 |

Suma = 13.8178

$$I \approx \frac{0.25}{2} \times 13.8178 = 1.7272$$

Error: $|1.7272 - 1.7183| = 0.0089$

---

## Método 3: Simpson 1/3 Simple

### Fórmula

$$\int_a^b f(x)\,dx \approx \frac{h}{3}[f(a) + 4f(\frac{a+b}{2}) + f(b)]$$

donde $h = \frac{b-a}{2}$

### Algoritmo

```python
def simpson_simple(f, a, b):
    h = (b - a) / 2
    return h / 3 * (f(a) + 4 * f((a + b) / 2) + f(b))
```

### Ejemplo

**Calcular $\int_0^1 e^x\,dx$**

$h = 0.5$

$$I \approx \frac{0.5}{3}[e^0 + 4e^{0.5} + e^1] = \frac{0.5}{3}[1 + 6.5949 + 2.7183]$$
$$= \frac{0.5}{3} \times 10.3132 = 1.7189$$

Error: $|1.7189 - 1.7183| = 0.0006$

---

## Método 4: Simpson Compuesto

### Fórmula

Con $n$ par subintervalos y $h = \frac{b-a}{n}$:

$$I \approx \frac{h}{3}\left[f(a) + 4\sum_{i \text{ impar}} f(x_i) + 2\sum_{i \text{ par}} f(x_i) + f(b)\right]$$

### Algoritmo

```python
def simpson_compuesto(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n debe ser par")
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        coef = 4 if i % 2 == 1 else 2
        suma += coef * f(a + i * h)
    return h / 3 * suma
```

### Ejemplo Completo

**Calcular $\int_0^1 e^x\,dx$ con $n = 4$**

$h = 0.25$

| $x_i$ | $f(x_i)$ | Coef. | Contribución |
|-------|----------|-------|--------------|
| 0 | 1.0000 | 1 | 1.0000 |
| 0.25 | 1.2840 | 4 | 5.1361 |
| 0.5 | 1.6487 | 2 | 3.2974 |
| 0.75 | 2.1170 | 4 | 8.4681 |
| 1 | 2.7183 | 1 | 2.7183 |

Suma = 20.6199

$$I \approx \frac{0.25}{3} \times 20.6199 = 1.7183$$

Error: $\approx 0.00003$

---

## Método 5: Integración de Romberg

### Algoritmo Paso a Paso

**Paso 1:** Calcular columna de trapecio $R_{k,0}$:
$$R_{k,0} = T(h_k), \quad h_k = \frac{b-a}{2^k}$$

**Paso 2:** Extrapolación de Richardson:
$$R_{k,j} = \frac{4^j R_{k,j-1} - R_{k-1,j-1}}{4^j - 1}$$

**Paso 3:** Repetir hasta convergencia.

### Pseudocódigo

```python
def romberg(f, a, b, tol=1e-6, max_iter=10):
    R = [[0] * (max_iter + 1) for _ in range(max_iter + 1)]
    
    # Primera columna: trapecio
    h = b - a
    R[0][0] = h / 2 * (f(a) + f(b))
    
    for k in range(1, max_iter + 1):
        h = h / 2
        # Trapecio con nuevos puntos
        suma = sum(f(a + (2*i - 1) * h) for i in range(1, 2**(k-1) + 1))
        R[k][0] = R[k-1][0] / 2 + h * suma
        
        # Extrapolación
        for j in range(1, k + 1):
            R[k][j] = (4**j * R[k][j-1] - R[k-1][j-1]) / (4**j - 1)
        
        if abs(R[k][k] - R[k-1][k-1]) < tol:
            return R[k][k]
    
    return R[max_iter][max_iter]
```

### Ejemplo

**Calcular $\int_0^1 e^x\,dx$**

| $k$ | $h_k$ | $R_{k,0}$ | $R_{k,1}$ | $R_{k,2}$ |
|-----|-------|-----------|-----------|-----------|
| 0 | 1 | 1.85914 | | |
| 1 | 0.5 | 1.75393 | 1.71886 | |
| 2 | 0.25 | 1.72722 | 1.71832 | 1.71828 |

$R_{2,2} = 1.71828$ (valor exacto: $e - 1 = 1.71828...$)

---

## Método 6: Cuadratura de Gauss-Legendre

### Algoritmo Paso a Paso

**Paso 1:** Cambiar variable de $[a,b]$ a $[-1,1]$:
$$x = \frac{b-a}{2}t + \frac{a+b}{2}$$

**Paso 2:** Aplicar cuadratura con nodos y pesos tabulados:
$$I = \frac{b-a}{2}\sum_{i=1}^{n} w_i f(x_i)$$

donde $x_i = \frac{b-a}{2}t_i + \frac{a+b}{2}$

### Tabla de Nodos y Pesos

**$n = 2$:**
| $t_i$ | $w_i$ |
|-------|-------|
| $-1/\sqrt{3} \approx -0.5774$ | 1 |
| $+1/\sqrt{3} \approx +0.5774$ | 1 |

**$n = 3$:**
| $t_i$ | $w_i$ |
|-------|-------|
| $-\sqrt{3/5} \approx -0.7746$ | 5/9 |
| 0 | 8/9 |
| $+\sqrt{3/5} \approx +0.7746$ | 5/9 |

### Ejemplo Completo

**Calcular $\int_0^1 e^x\,dx$ con Gauss-2**

Cambio: $x = \frac{1}{2}t + \frac{1}{2}$

Nodos en $[0,1]$:
- $x_1 = \frac{1}{2}(-0.5774) + 0.5 = 0.2113$
- $x_2 = \frac{1}{2}(+0.5774) + 0.5 = 0.7887$

$$I = \frac{1}{2}[1 \cdot f(0.2113) + 1 \cdot f(0.7887)]$$
$$= \frac{1}{2}[e^{0.2113} + e^{0.7887}]$$
$$= \frac{1}{2}[1.2354 + 2.2007] = 1.7181$$

Error: $|1.7181 - 1.7183| = 0.0002$

---

## Tabla Comparativa

| Método | Evaluaciones de $f$ | Orden | Mejor para |
|--------|---------------------|-------|------------|
| Trapecio | $n+1$ | $O(h^2)$ | Datos tabulados |
| Simpson | $n+1$ | $O(h^4)$ | Funciones suaves |
| Romberg | Variable | $O(h^{2k})$ | Alta precisión |
| Gauss-$n$ | $n$ | Exacto grado $2n-1$ | Funciones conocidas |

---

## Diagrama de Decisión

```
¿Cómo tienes la función?
│
├── ANALÍTICA → ¿Precisión requerida?
│                 │
│              Baja─┴─Alta
│              │       │
│              ▼       ▼
│           Simpson  Romberg o Gauss
│
└── TABULADA → ¿Datos equiespaciados?
                │
             SÍ─┴─NO
             │     │
             ▼     ▼
          Trapecio Ajustar puntos
          /Simpson  primero
```
