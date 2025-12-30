<!--
content_type: methods
topic: Integración Numérica
version: 2.0
last_updated: 2025-01-14
---
-->

# Métodos: Integración Numérica

> **Referencia rápida:** Esta guía presenta 12 métodos de integración numérica (cuadratura) con algoritmos detallados, análisis de error y ejemplos completos.

---

## Índice de Métodos

| # | Método | Orden de Error | Complejidad |
|---|--------|----------------|-------------|
| 1 | [Trapecio Simple](#método-1-regla-del-trapecio-simple) | $O(h^3)$ | ⭐ |
| 2 | [Trapecio Compuesto](#método-2-trapecio-compuesto) | $O(h^2)$ | ⭐ |
| 3 | [Simpson 1/3 Simple](#método-3-simpson-13-simple) | $O(h^5)$ | ⭐ |
| 4 | [Simpson Compuesto](#método-4-simpson-compuesto) | $O(h^4)$ | ⭐⭐ |
| 5 | [Simpson 3/8](#método-5-simpson-38) | $O(h^5)$ | ⭐⭐ |
| 6 | [Romberg](#método-6-integración-de-romberg) | $O(h^{2k})$ | ⭐⭐⭐ |
| 7 | [Gauss-Legendre](#método-7-cuadratura-de-gauss-legendre) | Exacto grado $2n-1$ | ⭐⭐⭐ |
| 8 | [Gauss-Laguerre](#método-8-gauss-laguerre) | Integrales impropias | ⭐⭐⭐ |
| 9 | [Gauss-Hermite](#método-9-gauss-hermite) | Integrales $(-\infty, \infty)$ | ⭐⭐⭐ |
| 10 | [Cuadratura Adaptativa](#método-10-cuadratura-adaptativa) | Variable | ⭐⭐⭐⭐ |
| 11 | [Monte Carlo](#método-11-monte-carlo) | $O(1/\sqrt{n})$ | ⭐⭐ |
| 12 | [Doble/Triple](#método-12-integrales-múltiples) | Variable | ⭐⭐⭐ |

---

## Conceptos Fundamentales

### Idea General

Aproximar $\int_a^b f(x)\,dx$ por una suma ponderada:

$$\int_a^b f(x)\,dx \approx \sum_{i=0}^{n} w_i f(x_i)$$

### Fórmulas de Newton-Cotes

Basadas en interpolación polinomial con **nodos equiespaciados**.

### Cuadratura de Gauss

Elige nodos **óptimamente** para maximizar precisión con $n$ evaluaciones.

### Error de Truncamiento

Para una regla con grado de precisión $p$:
- Exacta para polinomios de grado $\leq p$
- Error $\propto f^{(p+1)}(\xi) \cdot h^{p+2}$

---

## Método 1: Regla del Trapecio Simple

### Cuándo Usar

- Aproximación rápida y sencilla
- Punto de partida para métodos más precisos
- Funciones lineales (exacto)

### Fórmula

$$\int_a^b f(x)\,dx \approx \frac{b-a}{2}[f(a) + f(b)]$$

### Error

$$E = -\frac{(b-a)^3}{12}f''(\xi), \quad \xi \in (a,b)$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Evaluar** | $f(a)$ y $f(b)$ |
| 2 | **Calcular** | $I = \frac{b-a}{2}[f(a) + f(b)]$ |

### Pseudocódigo

```python
def trapecio_simple(f, a, b):
    return (b - a) / 2 * (f(a) + f(b))
```

### Ejemplo Detallado

**Problema:** Aproximar $\int_0^1 e^x\,dx$

---

**Paso 1: Evaluar**

$f(0) = e^0 = 1$

$f(1) = e^1 = 2.7183$

---

**Paso 2: Calcular**

$$I \approx \frac{1-0}{2}[1 + 2.7183] = \frac{3.7183}{2} = 1.8591$$

---

**Valor exacto:** $\int_0^1 e^x\,dx = e - 1 = 1.7183$

**Error:** $|1.8591 - 1.7183| = 0.1408$

$$\boxed{I \approx 1.8591}$$

---

## Método 2: Trapecio Compuesto

### Cuándo Usar

- Mejor precisión que trapecio simple
- Datos tabulados equiespaciados
- Base para Romberg

### Fórmula

Con $n$ subintervalos, $h = \frac{b-a}{n}$, $x_i = a + ih$:

$$I \approx \frac{h}{2}\left[f(x_0) + 2\sum_{i=1}^{n-1} f(x_i) + f(x_n)\right]$$

### Error Global

$$E = -\frac{(b-a)h^2}{12}f''(\xi) = -\frac{(b-a)^3}{12n^2}f''(\xi)$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Calcular** | $h = (b-a)/n$ |
| 2 | **Evaluar** | $f(x_i)$ para $i = 0, \ldots, n$ |
| 3 | **Sumar** | $f(a) + 2\sum f(x_i) + f(b)$ |
| 4 | **Multiplicar** | por $h/2$ |

### Pseudocódigo

```python
def trapecio_compuesto(f, a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n):
        suma += 2 * f(a + i * h)
    
    return h / 2 * suma
```

### Ejemplo Detallado

**Problema:** Aproximar $\int_0^1 e^x\,dx$ con $n = 4$

---

**Paso 1:** $h = (1-0)/4 = 0.25$

**Paso 2: Tabla de valores**

| $i$ | $x_i$ | $f(x_i) = e^{x_i}$ | Coef. | Contribución |
|:---:|:-----:|:------------------:|:-----:|:------------:|
| 0 | 0.00 | 1.0000 | 1 | 1.0000 |
| 1 | 0.25 | 1.2840 | 2 | 2.5681 |
| 2 | 0.50 | 1.6487 | 2 | 3.2974 |
| 3 | 0.75 | 2.1170 | 2 | 4.2340 |
| 4 | 1.00 | 2.7183 | 1 | 2.7183 |
| | | **Suma** | | **13.8178** |

---

**Paso 3-4:** 

$$I \approx \frac{0.25}{2} \times 13.8178 = 0.125 \times 13.8178 = 1.7272$$

**Error:** $|1.7272 - 1.7183| = 0.0089$

$$\boxed{I \approx 1.7272}$$

---

## Método 3: Simpson 1/3 Simple

### Cuándo Usar

- Funciones suaves
- Mayor precisión con 3 puntos
- Exacto para polinomios cúbicos

### Fórmula

$$\int_a^b f(x)\,dx \approx \frac{h}{3}[f(a) + 4f(m) + f(b)]$$

donde $m = \frac{a+b}{2}$ y $h = \frac{b-a}{2}$

### Error

$$E = -\frac{h^5}{90}f^{(4)}(\xi) = -\frac{(b-a)^5}{2880}f^{(4)}(\xi)$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Calcular** | $m = (a+b)/2$, $h = (b-a)/2$ |
| 2 | **Evaluar** | $f(a)$, $f(m)$, $f(b)$ |
| 3 | **Aplicar** | $I = \frac{h}{3}[f(a) + 4f(m) + f(b)]$ |

### Pseudocódigo

```python
def simpson_simple(f, a, b):
    m = (a + b) / 2
    h = (b - a) / 2
    return h / 3 * (f(a) + 4 * f(m) + f(b))
```

### Ejemplo Detallado

**Problema:** Aproximar $\int_0^1 e^x\,dx$

---

**Paso 1:** $m = 0.5$, $h = 0.5$

**Paso 2:** 
- $f(0) = 1$
- $f(0.5) = e^{0.5} = 1.6487$
- $f(1) = e = 2.7183$

**Paso 3:**

$$I \approx \frac{0.5}{3}[1 + 4(1.6487) + 2.7183]$$

$$= \frac{0.5}{3}[1 + 6.5949 + 2.7183] = \frac{0.5}{3}[10.3132]$$

$$= \frac{5.1566}{3} = 1.7189$$

**Error:** $|1.7189 - 1.7183| = 0.0006$

$$\boxed{I \approx 1.7189}$$

---

## Método 4: Simpson Compuesto

### Cuándo Usar

- Precisión alta para funciones suaves
- $n$ **par** de subintervalos
- Método estándar en la práctica

### Fórmula

Con $n$ par, $h = \frac{b-a}{n}$:

$$I \approx \frac{h}{3}\left[f(x_0) + 4\sum_{i \text{ impar}} f(x_i) + 2\sum_{i \text{ par}}^{n-2} f(x_i) + f(x_n)\right]$$

**Coeficientes:** $1, 4, 2, 4, 2, \ldots, 4, 2, 4, 1$

### Error Global

$$E = -\frac{(b-a)h^4}{180}f^{(4)}(\xi)$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Verificar** | $n$ es par |
| 2 | **Calcular** | $h = (b-a)/n$ |
| 3 | **Evaluar** | Todos los $f(x_i)$ |
| 4 | **Sumar** | Con coeficientes $1, 4, 2, 4, \ldots$ |
| 5 | **Multiplicar** | por $h/3$ |

### Pseudocódigo

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

### Ejemplo Detallado

**Problema:** Aproximar $\int_0^1 e^x\,dx$ con $n = 4$

---

$h = 0.25$

| $i$ | $x_i$ | $f(x_i)$ | Coef. | Contribución |
|:---:|:-----:|:--------:|:-----:|:------------:|
| 0 | 0.00 | 1.0000 | 1 | 1.0000 |
| 1 | 0.25 | 1.2840 | 4 | 5.1361 |
| 2 | 0.50 | 1.6487 | 2 | 3.2974 |
| 3 | 0.75 | 2.1170 | 4 | 8.4681 |
| 4 | 1.00 | 2.7183 | 1 | 2.7183 |
| | | **Suma** | | **20.6199** |

$$I \approx \frac{0.25}{3} \times 20.6199 = \frac{5.1550}{3} = 1.71833$$

**Error:** $|1.71833 - 1.71828| \approx 0.00005$

$$\boxed{I \approx 1.71833}$$

---

## Método 5: Simpson 3/8

### Cuándo Usar

- $n$ es múltiplo de 3
- Alternativa a Simpson 1/3
- Combinación con 1/3 para $n$ impar

### Fórmula Simple

$$\int_a^b f(x)\,dx \approx \frac{3h}{8}[f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)]$$

donde $h = \frac{b-a}{3}$

### Fórmula Compuesta

$$I \approx \frac{3h}{8}\left[f_0 + 3f_1 + 3f_2 + 2f_3 + 3f_4 + 3f_5 + 2f_6 + \cdots + f_n\right]$$

**Coeficientes:** $1, 3, 3, 2, 3, 3, 2, \ldots, 3, 3, 1$

### Ejemplo

**Problema:** $\int_0^3 e^x\,dx$ con Simpson 3/8 simple

$h = 1$

$$I \approx \frac{3(1)}{8}[e^0 + 3e^1 + 3e^2 + e^3]$$

$$= \frac{3}{8}[1 + 8.155 + 22.167 + 20.086] = \frac{3}{8}(51.408) = 19.278$$

Valor exacto: $e^3 - 1 = 19.086$

---

## Método 6: Integración de Romberg

### Cuándo Usar

- Alta precisión requerida
- Función suave
- Costo computacional aceptable

### Idea

Combinar extrapolación de Richardson con trapecio compuesto.

### Fórmulas

**Primera columna** (trapecio):

$$R_{k,0} = T(h_k), \quad h_k = \frac{b-a}{2^k}$$

**Extrapolación:**

$$R_{k,j} = \frac{4^j R_{k,j-1} - R_{k-1,j-1}}{4^j - 1}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Inicializar** | $R_{0,0} = \frac{b-a}{2}[f(a)+f(b)]$ |
| 2 | **Para** $k = 1, 2, \ldots$ | |
| 3 | → **Trapecio** | $R_{k,0}$ con $2^k$ intervalos |
| 4 | → **Extrapolar** | $R_{k,j}$ para $j = 1, \ldots, k$ |
| 5 | → **Verificar** | Si $|R_{k,k} - R_{k-1,k-1}| < \varepsilon$: terminar |

### Pseudocódigo

```python
def romberg(f, a, b, tol=1e-10, max_k=10):
    R = [[0.0] * (max_k + 1) for _ in range(max_k + 1)]
    
    h = b - a
    R[0][0] = h / 2 * (f(a) + f(b))
    
    for k in range(1, max_k + 1):
        h = h / 2
        
        # Nuevos puntos para trapecio
        suma = sum(f(a + (2*i - 1) * h) for i in range(1, 2**(k-1) + 1))
        R[k][0] = R[k-1][0] / 2 + h * suma
        
        # Extrapolación de Richardson
        for j in range(1, k + 1):
            R[k][j] = (4**j * R[k][j-1] - R[k-1][j-1]) / (4**j - 1)
        
        # Convergencia
        if k > 1 and abs(R[k][k] - R[k-1][k-1]) < tol:
            return R[k][k], k
    
    return R[max_k][max_k], max_k
```

### Ejemplo Detallado

**Problema:** Aproximar $\int_0^1 e^x\,dx$ con Romberg

---

**Tabla de Romberg:**

| $k$ | $h_k$ | $R_{k,0}$ | $R_{k,1}$ | $R_{k,2}$ | $R_{k,3}$ |
|:---:|:-----:|:---------:|:---------:|:---------:|:---------:|
| 0 | 1 | 1.8591409 | | | |
| 1 | 0.5 | 1.7539312 | 1.7188846 | | |
| 2 | 0.25 | 1.7272219 | 1.7183249 | 1.7182876 | |
| 3 | 0.125 | 1.7205059 | 1.7182839 | 1.7182819 | 1.7182818 |

---

**Cálculos de ejemplo:**

$R_{1,1} = \frac{4 \cdot R_{1,0} - R_{0,0}}{3} = \frac{4(1.7539) - 1.8591}{3} = \frac{5.1564}{3} = 1.7188$

$R_{2,1} = \frac{4 \cdot R_{2,0} - R_{1,0}}{3} = \frac{4(1.7272) - 1.7539}{3} = 1.7183$

$R_{2,2} = \frac{16 \cdot R_{2,1} - R_{1,1}}{15} = \frac{16(1.7183) - 1.7189}{15} = 1.71828$

---

**Valor exacto:** $e - 1 = 1.7182818...$

$$\boxed{I \approx 1.7182818 \text{ (Romberg con } k=3 \text{)}}$$

---

## Método 7: Cuadratura de Gauss-Legendre

### Cuándo Usar

- Función conocida analíticamente
- Alta precisión con pocas evaluaciones
- Nodos no necesitan ser equiespaciados

### Idea

Elegir nodos $t_i$ y pesos $w_i$ óptimamente en $[-1, 1]$:

$$\int_{-1}^{1} g(t)\,dt \approx \sum_{i=1}^{n} w_i g(t_i)$$

Exacto para polinomios de grado $\leq 2n - 1$.

### Cambio de Variable

De $[a, b]$ a $[-1, 1]$:

$$x = \frac{b-a}{2}t + \frac{a+b}{2}, \quad dx = \frac{b-a}{2}dt$$

$$\int_a^b f(x)\,dx = \frac{b-a}{2}\int_{-1}^{1} f\left(\frac{b-a}{2}t + \frac{a+b}{2}\right)dt$$

### Tabla de Nodos y Pesos

**n = 2:**
| $t_i$ | $w_i$ |
|:-----:|:-----:|
| $-1/\sqrt{3} \approx -0.5773503$ | 1 |
| $+1/\sqrt{3} \approx +0.5773503$ | 1 |

**n = 3:**
| $t_i$ | $w_i$ |
|:-----:|:-----:|
| $-\sqrt{0.6} \approx -0.7745967$ | $5/9 \approx 0.5556$ |
| $0$ | $8/9 \approx 0.8889$ |
| $+\sqrt{0.6} \approx +0.7745967$ | $5/9 \approx 0.5556$ |

**n = 4:**
| $t_i$ | $w_i$ |
|:-----:|:-----:|
| $\pm 0.8611363$ | $0.3478548$ |
| $\pm 0.3399810$ | $0.6521452$ |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Elegir** $n$ | Número de puntos |
| 2 | **Obtener** | Nodos $t_i$ y pesos $w_i$ (tabla) |
| 3 | **Transformar** | $x_i = \frac{b-a}{2}t_i + \frac{a+b}{2}$ |
| 4 | **Evaluar** | $f(x_i)$ |
| 5 | **Calcular** | $I = \frac{b-a}{2}\sum w_i f(x_i)$ |

### Pseudocódigo

```python
def gauss_legendre(f, a, b, n=3):
    # Nodos y pesos para n puntos (precalculados)
    nodos_pesos = {
        2: ([0.5773503, -0.5773503], [1.0, 1.0]),
        3: ([0.0, 0.7745967, -0.7745967], [0.8888889, 0.5555556, 0.5555556]),
        4: ([0.3399810, -0.3399810, 0.8611363, -0.8611363],
            [0.6521452, 0.6521452, 0.3478548, 0.3478548])
    }
    
    t, w = nodos_pesos[n]
    c1 = (b - a) / 2
    c2 = (a + b) / 2
    
    suma = sum(w[i] * f(c1 * t[i] + c2) for i in range(n))
    
    return c1 * suma
```

### Ejemplo Detallado

**Problema:** Aproximar $\int_0^1 e^x\,dx$ con Gauss-Legendre $n = 2$

---

**Paso 1-2:** Nodos y pesos

$t_1 = -1/\sqrt{3} \approx -0.5774$, $w_1 = 1$

$t_2 = +1/\sqrt{3} \approx +0.5774$, $w_2 = 1$

---

**Paso 3:** Transformar a $[0, 1]$

$c_1 = \frac{1-0}{2} = 0.5$, $c_2 = \frac{0+1}{2} = 0.5$

$x_1 = 0.5(-0.5774) + 0.5 = 0.2113$

$x_2 = 0.5(+0.5774) + 0.5 = 0.7887$

---

**Paso 4:** Evaluar

$f(x_1) = e^{0.2113} = 1.2354$

$f(x_2) = e^{0.7887} = 2.2007$

---

**Paso 5:** Calcular

$$I = 0.5[1 \cdot 1.2354 + 1 \cdot 2.2007] = 0.5 \times 3.4361 = 1.7181$$

**Error:** $|1.7181 - 1.7183| = 0.0002$

$$\boxed{I \approx 1.7181 \text{ (solo 2 evaluaciones)}}$$

---

## Método 8: Gauss-Laguerre

### Cuándo Usar

- Integrales de la forma $\int_0^\infty e^{-x} g(x)\,dx$
- Integrales impropias $[0, \infty)$

### Fórmula

$$\int_0^\infty e^{-x} g(x)\,dx \approx \sum_{i=1}^{n} w_i g(x_i)$$

### Nodos y Pesos (n = 3)

| $x_i$ | $w_i$ |
|:-----:|:-----:|
| 0.4158 | 0.7110 |
| 2.2943 | 0.2785 |
| 6.2900 | 0.0104 |

### Ejemplo

**Problema:** $\int_0^\infty e^{-x}\cos x\,dx$

$g(x) = \cos x$

$$I \approx 0.7110 \cos(0.4158) + 0.2785 \cos(2.2943) + 0.0104 \cos(6.2900)$$

$$\approx 0.7110(0.916) + 0.2785(-0.665) + 0.0104(0.999)$$

$$\approx 0.651 - 0.185 + 0.010 = 0.476$$

Valor exacto: $\frac{1}{2}$

---

## Método 9: Gauss-Hermite

### Cuándo Usar

- Integrales de la forma $\int_{-\infty}^{\infty} e^{-x^2} g(x)\,dx$
- Distribuciones normales
- Mecánica cuántica

### Fórmula

$$\int_{-\infty}^{\infty} e^{-x^2} g(x)\,dx \approx \sum_{i=1}^{n} w_i g(x_i)$$

### Nodos y Pesos (n = 3)

| $x_i$ | $w_i$ |
|:-----:|:-----:|
| 0 | 1.1816 |
| $\pm 1.2247$ | 0.2954 |

---

## Método 10: Cuadratura Adaptativa

### Cuándo Usar

- Función con variación irregular
- Precisión uniforme requerida
- Picos o regiones difíciles

### Idea

1. Aplicar regla a todo $[a, b]$
2. Dividir y aplicar a cada mitad
3. Si diferencia > tolerancia, subdividir más
4. Recursivamente hasta convergencia

### Pseudocódigo

```python
def adaptativa(f, a, b, tol=1e-6, metodo=simpson_simple):
    S_ab = metodo(f, a, b)
    m = (a + b) / 2
    S_am = metodo(f, a, m)
    S_mb = metodo(f, m, b)
    
    if abs(S_ab - S_am - S_mb) < 15 * tol:
        return S_am + S_mb + (S_am + S_mb - S_ab) / 15
    else:
        return adaptativa(f, a, m, tol/2) + adaptativa(f, m, b, tol/2)
```

### Ventaja

Concentra el esfuerzo donde la función es más difícil de integrar.

---

## Método 11: Monte Carlo

### Cuándo Usar

- Dimensiones altas (integrales múltiples)
- Dominios irregulares
- Estimación probabilística suficiente

### Fórmula Básica

$$\int_a^b f(x)\,dx \approx (b-a) \cdot \frac{1}{N}\sum_{i=1}^{N} f(x_i)$$

donde $x_i$ son puntos aleatorios uniformes en $[a, b]$.

### Error

$$\text{Error} \sim \frac{\sigma}{\sqrt{N}}$$

donde $\sigma$ es la desviación estándar de $f$.

### Pseudocódigo

```python
import random

def monte_carlo(f, a, b, N=10000):
    suma = sum(f(random.uniform(a, b)) for _ in range(N))
    return (b - a) * suma / N
```

### Ejemplo

**Problema:** Estimar $\int_0^1 e^x\,dx$ con $N = 10000$ puntos

```python
>>> monte_carlo(lambda x: math.exp(x), 0, 1, 10000)
1.7192  # ± 0.01 aproximadamente
```

---

## Método 12: Integrales Múltiples

### Cuándo Usar

- Integrales dobles $\iint$
- Integrales triples $\iiint$
- Volúmenes, centros de masa

### Integral Doble con Producto de Cuadraturas

$$\int_a^b \int_c^d f(x,y)\,dy\,dx \approx \sum_{i=1}^{n}\sum_{j=1}^{m} w_i v_j f(x_i, y_j)$$

### Pseudocódigo

```python
def simpson_doble(f, a, b, c, d, n=4, m=4):
    # Simpson 2D con n x m puntos
    hx = (b - a) / n
    hy = (d - c) / m
    
    resultado = 0
    for i in range(n + 1):
        xi = a + i * hx
        ci = 1 if i == 0 or i == n else (4 if i % 2 == 1 else 2)
        
        for j in range(m + 1):
            yj = c + j * hy
            cj = 1 if j == 0 or j == m else (4 if j % 2 == 1 else 2)
            
            resultado += ci * cj * f(xi, yj)
    
    return resultado * hx * hy / 9
```

### Ejemplo

**Problema:** $\int_0^1 \int_0^1 e^{x+y}\,dy\,dx$

Valor exacto: $(e-1)^2 \approx 2.952$

Con Simpson $4 \times 4$: $\approx 2.9524$

---

## Diagrama de Decisión

```
┌──────────────────────────────────────────────┐
│        INTEGRACIÓN NUMÉRICA                  │
└──────────────────────────────────────────────┘
                    │
                    ▼
         ┌─────────────────────┐
         │ ¿Tipo de integral?  │
         └─────────────────────┘
                    │
    ┌───────────────┼───────────────┐
    ▼               ▼               ▼
 Definida       Impropia        Múltiple
 [a,b]          [0,∞) etc.      ∬, ∭
    │               │               │
    ▼               ▼               ▼
 ¿Precisión?    Gauss-         Monte Carlo
    │           Laguerre        o producto
    │           Hermite         de reglas
 ┌──┴──┐
Baja  Alta
 │      │
 ▼      ▼
Trapecio Romberg
Simpson  Gauss
```

---

## Tabla Comparativa

| Método | Evaluaciones | Grado exacto | Error Global |
|--------|:------------:|:------------:|:------------:|
| Trapecio simple | 2 | 1 | $O(h^3)$ |
| Trapecio compuesto | $n+1$ | 1 | $O(h^2)$ |
| Simpson 1/3 | 3 | 3 | $O(h^5)$ |
| Simpson compuesto | $n+1$ | 3 | $O(h^4)$ |
| Gauss-$n$ | $n$ | $2n-1$ | Depende de $f$ |
| Romberg | Variable | Alto | $O(h^{2k})$ |
| Monte Carlo | $N$ | — | $O(1/\sqrt{N})$ |

---

## Errores Comunes a Evitar

| Error | Consecuencia | Prevención |
|-------|--------------|------------|
| $n$ impar en Simpson | Error grande | Verificar paridad |
| Ignorar singularidades | Resultado incorrecto | Dividir en $x$ singular |
| Demasiados subintervalos | Acumulación de redondeo | Usar métodos adaptativos |
| Monte Carlo con pocas muestras | Alta varianza | Aumentar $N$ |

---

## Problemas de Práctica Sugeridos

1. **Trapecio:** $\int_0^{\pi/2} \sin x\,dx$ con $n = 4$

2. **Simpson:** $\int_1^2 \frac{1}{x}\,dx$ con $n = 4$

3. **Romberg:** $\int_0^1 \frac{4}{1+x^2}\,dx$ (debe dar $\pi$)

4. **Gauss-2:** $\int_0^1 x^3\,dx$ (exacto)

5. **Doble:** $\int_0^1\int_0^x xy\,dy\,dx$

6. **Adaptativo:** $\int_0^1 \frac{1}{\sqrt{x}}\,dx$ (singularidad en 0)

---

*Documento actualizado con formato expandido para estudio detallado.*
