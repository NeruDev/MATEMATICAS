<!--
::METADATA::
type: problem_set
topic_id: mn-03-integracion-numerica
file_id: MN-03-Problemas
status: stable
audience: student
total_problems: 30
difficulty_distribution:
  basico: 10
  intermedio: 13
  avanzado: 7
-->

# Problemas: Integración Numérica

---

## Sección 1: Regla del Trapecio

### [Prob-01] Trapecio simple para función cuadrática ⭐
Aproxima $\int_0^2 x^2\,dx$ usando la [regla del trapecio](../../../glossary.md#regla-del-trapecio) simple. Calcula el error relativo.

> 📁 Solución: `solutions/prob-01/`

### [Prob-02] Trapecio compuesto para logaritmo natural ⭐⭐
Usa el trapecio compuesto con $n = 4$ para estimar $\int_1^3 \frac{1}{x}\,dx$. Compara con $\ln 3$.

> 📁 Solución: `solutions/prob-02/`

### [Prob-03] Estimación de subintervalos para precisión dada ⭐⭐
Determina el número de subintervalos necesarios para calcular $\int_0^1 e^{-x^2}\,dx$ con error [menor](../../../glossary.md#menor) a $10^{-4}$ usando trapecio compuesto.

> 📁 Solución: `solutions/prob-03/`

### [Prob-04] Integración de datos tabulados ⭐
Con los datos tabulados:

| $x$ | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 |
|-----|-----|-----|-----|-----|-----|
| $f(x)$ | 2.3 | 3.1 | 3.8 | 4.2 | 4.5 |

Calcula $\int_1^3 f(x)\,dx$ usando trapecio compuesto.

> 📁 Solución: `solutions/prob-04/`

### [Prob-05] Análisis de convergencia del trapecio ⭐⭐
Para $\int_0^{\pi} \sin x\,dx$, calcula las aproximaciones con trapecio compuesto usando $n = 2, 4, 8$ y analiza la [convergencia](../../../glossary.md#convergencia).

> 📁 Solución: `solutions/prob-05/`

---

## Sección 2: Regla de Simpson

### [Prob-06] Simpson 1/3 para función cúbica ⭐
Aproxima $\int_0^2 x^3\,dx$ usando Simpson 1/3 simple. ¿Es exacto? Justifica.

> 📁 Solución: `solutions/prob-06/`

### [Prob-07] Aproximación de π con Simpson ⭐⭐
Usa Simpson compuesto con $n = 4$ para calcular $\int_0^1 \frac{4}{1+x^2}\,dx$ y aproxima $\pi$.

> 📁 Solución: `solutions/prob-07/`

### [Prob-08] Simpson compuesto para integral gaussiana ⭐
Calcula $\int_0^{0.8} e^{-x^2}\,dx$ con Simpson compuesto ($n = 4$).

> 📁 Solución: `solutions/prob-08/`

### [Prob-09] Demostración de la regla de Simpson 3/8 ⭐⭐⭐
Demuestra que la [regla de Simpson](../../../glossary.md#regla-de-simpson) 3/8 con puntos $x_0, x_1, x_2, x_3$ equiespaciados da:
$$I \approx \frac{3h}{8}[f_0 + 3f_1 + 3f_2 + f_3]$$

> 📁 Solución: `solutions/prob-09/`

### [Prob-10] Cálculo de distancia con datos de velocidad ⭐
Con datos de velocidad:

| $t$ (s) | 0 | 0.5 | 1 | 1.5 | 2 |
|---------|---|-----|---|-----|---|
| $v$ (m/s) | 0 | 4.2 | 7.8 | 10.1 | 11.5 |

Calcula la distancia recorrida $\int_0^2 v\,dt$ usando Simpson compuesto.

> 📁 Solución: `solutions/prob-10/`

### [Prob-11] Comparación trapecio vs Simpson ⭐⭐
Compara trapecio y Simpson compuestos ($n = 6$) para $\int_1^4 \sqrt{x}\,dx$.

> 📁 Solución: `solutions/prob-11/`

---

## Sección 3: Integración de Romberg

### [Prob-12] Construcción de tabla de Romberg ⭐⭐
Construye la tabla de Romberg para $\int_0^1 e^x\,dx$ hasta $R_{3,3}$.

> 📁 Solución: `solutions/prob-12/`

### [Prob-13] Romberg con tolerancia específica ⭐⭐
Usa integración de Romberg para calcular $\int_0^{\pi/2} \cos x\,dx$ con tolerancia $10^{-6}$.

> 📁 Solución: `solutions/prob-13/`

### [Prob-14] Romberg para logaritmo natural ⭐⭐
Calcula $\int_1^2 \frac{1}{x}\,dx$ usando Romberg. Llena la tabla hasta [convergencia](../../../glossary.md#convergencia) ($\varepsilon < 10^{-5}$).

> 📁 Solución: `solutions/prob-14/`

### [Prob-15] Verificación de equivalencia Simpson-Romberg ⭐⭐⭐
Verifica que $R_{1,1}$ es equivalente a Simpson simple aplicando la extrapolación:
$$R_{1,1} = \frac{4R_{1,0} - R_{0,0}}{3}$$

> 📁 Solución: `solutions/prob-15/`

### [Prob-16] Romberg para potencias y exactitud ⭐⭐
Para $\int_0^2 x^4\,dx$, construye la tabla de Romberg y determina en qué nivel se obtiene el valor exacto.

> 📁 Solución: `solutions/prob-16/`

---

## Sección 4: Cuadratura de Gauss

### [Prob-17] Gauss-Legendre para exponencial ⭐⭐
Usa Gauss-Legendre con $n = 2$ para calcular $\int_0^1 e^{-x}\,dx$.

> 📁 Solución: `solutions/prob-17/`

### [Prob-18] Gauss-Legendre con distintos nodos ⭐⭐
Evalúa $\int_{-1}^{1} \frac{1}{1+x^2}\,dx$ usando Gauss-Legendre con $n = 2$ y $n = 3$.

> 📁 Solución: `solutions/prob-18/`

### [Prob-19] Gauss-Legendre con cambio de variable ⭐⭐
Calcula $\int_1^3 \ln x\,dx$ usando Gauss-Legendre con 3 puntos. Realiza el cambio de variable [necesario](../../../glossary.md#necesario).

> 📁 Solución: `solutions/prob-19/`

### [Prob-20] Grado de exactitud de Gauss-Legendre ⭐
¿Cuál es el grado máximo de [polinomio](../../../glossary.md#polinomio) que integra exactamente Gauss-Legendre con $n = 4$ puntos?

> 📁 Solución: `solutions/prob-20/`

### [Prob-21] Demostración de nodos y pesos para n=2 ⭐⭐⭐
Demuestra que para $n = 2$, los nodos $t_i = \pm\frac{1}{\sqrt{3}}$ y pesos $w_i = 1$ integran exactamente polinomios de grado ≤ 3.

> 📁 Solución: `solutions/prob-21/`

### [Prob-22] Comparación Simpson vs Gauss-Legendre ⭐⭐
Compara la precisión de Simpson compuesto ($n = 6$) vs Gauss-Legendre ($n = 3$) para $\int_0^1 \sin(\pi x)\,dx$.

> 📁 Solución: `solutions/prob-22/`

---

## Sección 5: Estimación de Error

### [Prob-23] Cota de error teórica del trapecio ⭐⭐
Para $f(x) = e^x$ en $[0, 1]$:
a) Calcula la cota de error teórica del trapecio compuesto con $n = 10$
b) Compara con el error real

> 📁 Solución: `solutions/prob-23/`

### [Prob-24] Subintervalos mínimos para Simpson ⭐⭐
Determina el número mínimo de subintervalos para Simpson compuesto que garantiza error [menor](../../../glossary.md#menor) a $10^{-6}$ en $\int_0^1 \frac{1}{1+x}\,dx$.

> 📁 Solución: `solutions/prob-24/`

### [Prob-25] Extrapolación de Richardson ⭐⭐
Usa extrapolación de Richardson para mejorar la estimación de $\int_0^{\pi/4} \tan x\,dx$ si tienes:
- $T(h) = 0.4390$
- $T(h/2) = 0.4312$

> 📁 Solución: `solutions/prob-25/`

### [Prob-26] Estimación del valor exacto por extrapolación ⭐⭐
Si el trapecio con $n = 10$ da $I_{10} = 1.8521$ y con $n = 20$ da $I_{20} = 1.8478$, estima el valor exacto usando extrapolación.

> 📁 Solución: `solutions/prob-26/`

---

## Sección 6: Integrales Dobles

### [Prob-27] Simpson doble para función bilineal ⭐⭐
Aproxima $\iint_R xy\,dA$ donde $R = [0,1] \times [0,1]$ usando Simpson simple en ambas direcciones.

> 📁 Solución: `solutions/prob-27/`

### [Prob-28] Trapecio doble para exponencial ⭐⭐
Usa el trapecio compuesto ($n = 2$ en cada dirección) para calcular $\iint_R e^{x+y}\,dA$ con $R = [0,1] \times [0,1]$.

> 📁 Solución: `solutions/prob-28/`

### [Prob-29] Integral iterada con límites variables ⭐⭐⭐
Para $\int_0^1 \int_0^x e^{xy}\,dy\,dx$, aplica trapecio iterado con $n = 4$ en cada integral.

> 📁 Solución: `solutions/prob-29/`

---

## Sección 7: Problemas Aplicados

### [Prob-30] Área bajo curva de concentración farmacológica ⭐
Los datos de concentración de un fármaco son:

| $t$ (h) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---------|---|---|---|---|---|---|---|
| $C$ (mg/L) | 0 | 8.5 | 15.2 | 12.1 | 8.3 | 5.0 | 2.8 |

Calcula el AUC (área bajo la curva) usando Simpson compuesto.

> 📁 Solución: `solutions/prob-30/`

### [Prob-31] Trabajo de fuerza variable en resorte ⭐
La fuerza aplicada a un resorte varía como:

| $x$ (m) | 0 | 0.1 | 0.2 | 0.3 | 0.4 |
|---------|---|-----|-----|-----|-----|
| $F$ (N) | 0 | 12 | 26 | 45 | 68 |

Calcula el trabajo $W = \int_0^{0.4} F\,dx$.

> 📁 Solución: `solutions/prob-31/`

### [Prob-32] Probabilidad de distribución normal estándar ⭐⭐⭐
Calcula $P(X < 1)$ para $X \sim N(0,1)$ evaluando $\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{1} e^{-x^2/2}\,dx$ usando un método apropiado.

> 📁 Solución: `solutions/prob-32/`

### [Prob-33] Longitud de arco de parábola ⭐⭐
Aproxima la longitud de la curva $y = x^2$ en $[0, 1]$ usando:
$$L = \int_0^1 \sqrt{1 + 4x^2}\,dx$$
con Simpson compuesto ($n = 4$).

> 📁 Solución: `solutions/prob-33/`

### [Prob-34] Cálculo de la función error ⭐⭐
Calcula la [función](../../../glossary.md#funcion) error $\text{erf}(1) = \frac{2}{\sqrt{\pi}}\int_0^1 e^{-t^2}\,dt$ con precisión de 4 decimales.

> 📁 Solución: `solutions/prob-34/`

---

## Sección 8: Problemas de Diseño

### [Prob-35] Diseño de selector automático de método ⭐⭐⭐
Diseña un programa que seleccione automáticamente entre trapecio, Simpson y Romberg según la precisión requerida.

> 📁 Solución: `solutions/prob-35/`

### [Prob-36] Implementación de integración adaptativa ⭐⭐⭐
Implementa integración adaptativa que subdivida el intervalo solo donde el error local sea grande.

> 📁 Solución: `solutions/prob-36/`

### [Prob-37] Integración con puntos no equiespaciados ⭐⭐⭐
Dada una [función](../../../glossary.md#funcion) tabulada en puntos NO equiespaciados:

| $x$ | 0 | 0.2 | 0.5 | 0.8 | 1.0 |
|-----|---|-----|-----|-----|-----|
| $f(x)$ | 1 | 1.22 | 1.65 | 2.23 | 2.72 |

¿Cómo calcularías la integral? Propón y ejecuta un método.

> 📁 Solución: `solutions/prob-37/`
