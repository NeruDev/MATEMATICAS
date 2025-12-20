<!--
content_type: problems
topic: Integración Numérica
difficulty_range: básico a avanzado
total_problems: 30
---
-->

# Problemas: Integración Numérica

---

## Sección 1: Regla del Trapecio

### Problema 1.1
Aproxima $\int_0^2 x^2\,dx$ usando la regla del trapecio simple. Calcula el error relativo.

### Problema 1.2
Usa el trapecio compuesto con $n = 4$ para estimar $\int_1^3 \frac{1}{x}\,dx$. Compara con $\ln 3$.

### Problema 1.3
Determina el número de subintervalos necesarios para calcular $\int_0^1 e^{-x^2}\,dx$ con error menor a $10^{-4}$ usando trapecio compuesto.

### Problema 1.4
Con los datos tabulados:

| $x$ | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 |
|-----|-----|-----|-----|-----|-----|
| $f(x)$ | 2.3 | 3.1 | 3.8 | 4.2 | 4.5 |

Calcula $\int_1^3 f(x)\,dx$ usando trapecio compuesto.

### Problema 1.5
Para $\int_0^{\pi} \sin x\,dx$, calcula las aproximaciones con trapecio compuesto usando $n = 2, 4, 8$ y analiza la convergencia.

---

## Sección 2: Regla de Simpson

### Problema 2.1
Aproxima $\int_0^2 x^3\,dx$ usando Simpson 1/3 simple. ¿Es exacto? Justifica.

### Problema 2.2
Usa Simpson compuesto con $n = 4$ para calcular $\int_0^1 \frac{4}{1+x^2}\,dx$ y aproxima $\pi$.

### Problema 2.3
Calcula $\int_0^{0.8} e^{-x^2}\,dx$ con Simpson compuesto ($n = 4$).

### Problema 2.4
Demuestra que la regla de Simpson 3/8 con puntos $x_0, x_1, x_2, x_3$ equiespaciados da:
$$I \approx \frac{3h}{8}[f_0 + 3f_1 + 3f_2 + f_3]$$

### Problema 2.5
Con datos de velocidad:

| $t$ (s) | 0 | 0.5 | 1 | 1.5 | 2 |
|---------|---|-----|---|-----|---|
| $v$ (m/s) | 0 | 4.2 | 7.8 | 10.1 | 11.5 |

Calcula la distancia recorrida $\int_0^2 v\,dt$ usando Simpson compuesto.

### Problema 2.6
Compara trapecio y Simpson compuestos ($n = 6$) para $\int_1^4 \sqrt{x}\,dx$.

---

## Sección 3: Integración de Romberg

### Problema 3.1
Construye la tabla de Romberg para $\int_0^1 e^x\,dx$ hasta $R_{3,3}$.

### Problema 3.2
Usa integración de Romberg para calcular $\int_0^{\pi/2} \cos x\,dx$ con tolerancia $10^{-6}$.

### Problema 3.3
Calcula $\int_1^2 \frac{1}{x}\,dx$ usando Romberg. Llena la tabla hasta convergencia ($\varepsilon < 10^{-5}$).

### Problema 3.4
Verifica que $R_{1,1}$ es equivalente a Simpson simple aplicando la extrapolación:
$$R_{1,1} = \frac{4R_{1,0} - R_{0,0}}{3}$$

### Problema 3.5
Para $\int_0^2 x^4\,dx$, construye la tabla de Romberg y determina en qué nivel se obtiene el valor exacto.

---

## Sección 4: Cuadratura de Gauss

### Problema 4.1
Usa Gauss-Legendre con $n = 2$ para calcular $\int_0^1 e^{-x}\,dx$.

### Problema 4.2
Evalúa $\int_{-1}^{1} \frac{1}{1+x^2}\,dx$ usando Gauss-Legendre con $n = 2$ y $n = 3$.

### Problema 4.3
Calcula $\int_1^3 \ln x\,dx$ usando Gauss-Legendre con 3 puntos. Realiza el cambio de variable necesario.

### Problema 4.4
¿Cuál es el grado máximo de polinomio que integra exactamente Gauss-Legendre con $n = 4$ puntos?

### Problema 4.5
Demuestra que para $n = 2$, los nodos $t_i = \pm\frac{1}{\sqrt{3}}$ y pesos $w_i = 1$ integran exactamente polinomios de grado ≤ 3.

### Problema 4.6
Compara la precisión de Simpson compuesto ($n = 6$) vs Gauss-Legendre ($n = 3$) para $\int_0^1 \sin(\pi x)\,dx$.

---

## Sección 5: Estimación de Error

### Problema 5.1
Para $f(x) = e^x$ en $[0, 1]$:
a) Calcula la cota de error teórica del trapecio compuesto con $n = 10$
b) Compara con el error real

### Problema 5.2
Determina el número mínimo de subintervalos para Simpson compuesto que garantiza error menor a $10^{-6}$ en $\int_0^1 \frac{1}{1+x}\,dx$.

### Problema 5.3
Usa extrapolación de Richardson para mejorar la estimación de $\int_0^{\pi/4} \tan x\,dx$ si tienes:
- $T(h) = 0.4390$
- $T(h/2) = 0.4312$

### Problema 5.4
Si el trapecio con $n = 10$ da $I_{10} = 1.8521$ y con $n = 20$ da $I_{20} = 1.8478$, estima el valor exacto usando extrapolación.

---

## Sección 6: Integrales Dobles

### Problema 6.1
Aproxima $\iint_R xy\,dA$ donde $R = [0,1] \times [0,1]$ usando Simpson simple en ambas direcciones.

### Problema 6.2
Usa el trapecio compuesto ($n = 2$ en cada dirección) para calcular $\iint_R e^{x+y}\,dA$ con $R = [0,1] \times [0,1]$.

### Problema 6.3
Para $\int_0^1 \int_0^x e^{xy}\,dy\,dx$, aplica trapecio iterado con $n = 4$ en cada integral.

---

## Sección 7: Problemas Aplicados

### Problema 7.1 (Área bajo curva experimental)
Los datos de concentración de un fármaco son:

| $t$ (h) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---------|---|---|---|---|---|---|---|
| $C$ (mg/L) | 0 | 8.5 | 15.2 | 12.1 | 8.3 | 5.0 | 2.8 |

Calcula el AUC (área bajo la curva) usando Simpson compuesto.

### Problema 7.2 (Trabajo)
La fuerza aplicada a un resorte varía como:

| $x$ (m) | 0 | 0.1 | 0.2 | 0.3 | 0.4 |
|---------|---|-----|-----|-----|-----|
| $F$ (N) | 0 | 12 | 26 | 45 | 68 |

Calcula el trabajo $W = \int_0^{0.4} F\,dx$.

### Problema 7.3 (Probabilidad)
Calcula $P(X < 1)$ para $X \sim N(0,1)$ evaluando $\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{1} e^{-x^2/2}\,dx$ usando un método apropiado.

### Problema 7.4 (Longitud de arco)
Aproxima la longitud de la curva $y = x^2$ en $[0, 1]$ usando:
$$L = \int_0^1 \sqrt{1 + 4x^2}\,dx$$
con Simpson compuesto ($n = 4$).

### Problema 7.5 (Función error)
Calcula la función error $\text{erf}(1) = \frac{2}{\sqrt{\pi}}\int_0^1 e^{-t^2}\,dt$ con precisión de 4 decimales.

---

## Sección 8: Problemas de Diseño

### Problema 8.1
Diseña un programa que seleccione automáticamente entre trapecio, Simpson y Romberg según la precisión requerida.

### Problema 8.2
Implementa integración adaptativa que subdivida el intervalo solo donde el error local sea grande.

### Problema 8.3
Dada una función tabulada en puntos NO equiespaciados:

| $x$ | 0 | 0.2 | 0.5 | 0.8 | 1.0 |
|-----|---|-----|-----|-----|-----|
| $f(x)$ | 1 | 1.22 | 1.65 | 2.23 | 2.72 |

¿Cómo calcularías la integral? Propón y ejecuta un método.
