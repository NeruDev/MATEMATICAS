<!--
::METADATA::
type: solution
status: active
-->

# Soluciones: Integración Numérica

---

## Solución 1.2: Trapecio Compuesto

**Problema:** Usar trapecio compuesto con $n = 4$ para $\int_1^3 \frac{1}{x}\,dx$.

**Solución:**

$h = \frac{3-1}{4} = 0.5$

Puntos: $x_0 = 1, x_1 = 1.5, x_2 = 2, x_3 = 2.5, x_4 = 3$

| $i$ | $x_i$ | $f(x_i) = 1/x_i$ | Coef. | Contribución |
|-----|-------|------------------|-------|--------------|
| 0 | 1.0 | 1.0000 | 1 | 1.0000 |
| 1 | 1.5 | 0.6667 | 2 | 1.3333 |
| 2 | 2.0 | 0.5000 | 2 | 1.0000 |
| 3 | 2.5 | 0.4000 | 2 | 0.8000 |
| 4 | 3.0 | 0.3333 | 1 | 0.3333 |

Suma = 4.4667

$$I = \frac{0.5}{2} \times 4.4667 = 1.1167$$

**Comparación:**
- Valor exacto: $\ln 3 = 1.0986$
- Error absoluto: $|1.1167 - 1.0986| = 0.0181$
- Error relativo: $1.65\%$

---

## Solución 2.2: Simpson para aproximar π

**Problema:** Usar Simpson compuesto con $n = 4$ para $\int_0^1 \frac{4}{1+x^2}\,dx$.

**Solución:**

Esta integral es $4\arctan(1) - 4\arctan(0) = \pi$.

$h = 0.25$

| $i$ | $x_i$ | $f(x_i) = \frac{4}{1+x_i^2}$ | Coef. | Contrib. |
|-----|-------|------------------------------|-------|----------|
| 0 | 0 | 4.0000 | 1 | 4.0000 |
| 1 | 0.25 | 3.7647 | 4 | 15.0588 |
| 2 | 0.5 | 3.2000 | 2 | 6.4000 |
| 3 | 0.75 | 2.5600 | 4 | 10.2400 |
| 4 | 1 | 2.0000 | 1 | 2.0000 |

Suma = 37.6988

$$I = \frac{0.25}{3} \times 37.6988 = 3.1416$$

**Aproximación de π:** $\pi \approx 3.1416$

Error: $|3.1416 - 3.14159...| \approx 0.00001$

---

## Solución 3.1: Tabla de Romberg

**Problema:** Construir tabla de Romberg para $\int_0^1 e^x\,dx$ hasta $R_{3,3}$.

**Solución:**

**Paso 1:** Calcular columna $R_{k,0}$ (trapecio):

$R_{0,0} = \frac{1}{2}(e^0 + e^1) = \frac{1}{2}(1 + 2.7183) = 1.8591$

$R_{1,0} = \frac{1}{2}R_{0,0} + \frac{1}{2}e^{0.5} = 0.9296 + 0.8244 = 1.7539$

$R_{2,0} = \frac{1}{2}R_{1,0} + \frac{1}{4}(e^{0.25} + e^{0.75}) = 0.8770 + 0.8502 = 1.7272$

$R_{3,0} = \frac{1}{2}R_{2,0} + \frac{1}{8}\sum e^{x_i} = 0.8636 + 0.8569 = 1.7205$

**Paso 2:** Extrapolación de Richardson:

$$R_{k,j} = \frac{4^j R_{k,j-1} - R_{k-1,j-1}}{4^j - 1}$$

$R_{1,1} = \frac{4(1.7539) - 1.8591}{3} = 1.7188$

$R_{2,1} = \frac{4(1.7272) - 1.7539}{3} = 1.7183$

$R_{2,2} = \frac{16(1.7183) - 1.7188}{15} = 1.7183$

$R_{3,1} = \frac{4(1.7205) - 1.7272}{3} = 1.7183$

$R_{3,2} = \frac{16(1.7183) - 1.7183}{15} = 1.7183$

$R_{3,3} = \frac{64(1.7183) - 1.7183}{63} = 1.7183$

**Tabla completa:**

| $k$ | $R_{k,0}$ | $R_{k,1}$ | $R_{k,2}$ | $R_{k,3}$ |
|-----|-----------|-----------|-----------|-----------|
| 0 | 1.8591 | | | |
| 1 | 1.7539 | 1.7188 | | |
| 2 | 1.7272 | 1.7183 | 1.7183 | |
| 3 | 1.7205 | 1.7183 | 1.7183 | 1.7183 |

**Valor exacto:** $e - 1 = 1.71828...$

---

## Solución 4.1: Gauss-Legendre

**Problema:** Usar Gauss-Legendre con $n = 2$ para $\int_0^1 e^{-x}\,dx$.

**Solución:**

**Paso 1:** Cambio de variable de $[0,1]$ a $[-1,1]$:
$$x = \frac{1-0}{2}t + \frac{1+0}{2} = \frac{t+1}{2}$$
$$dx = \frac{1}{2}dt$$

**Paso 2:** Transformar la integral:
$$\int_0^1 e^{-x}\,dx = \frac{1}{2}\int_{-1}^{1} e^{-(t+1)/2}\,dt$$

**Paso 3:** Nodos y pesos para $n = 2$:
- $t_1 = -\frac{1}{\sqrt{3}} = -0.5774$, $w_1 = 1$
- $t_2 = +\frac{1}{\sqrt{3}} = +0.5774$, $w_2 = 1$

**Paso 4:** Calcular $x_i$ en $[0,1]$:
- $x_1 = \frac{-0.5774 + 1}{2} = 0.2113$
- $x_2 = \frac{+0.5774 + 1}{2} = 0.7887$

**Paso 5:** Evaluar:
$$I = \frac{1}{2}[1 \cdot e^{-0.2113} + 1 \cdot e^{-0.7887}]$$
$$= \frac{1}{2}[0.8094 + 0.4546] = \frac{1}{2}(1.2640) = 0.6320$$

**Verificación:**
- Valor exacto: $1 - e^{-1} = 1 - 0.3679 = 0.6321$
- Error: $|0.6320 - 0.6321| = 0.0001$

---

## Solución 5.1: Estimación de Error

**Problema:** Para $f(x) = e^x$ en $[0, 1]$ con trapecio compuesto $n = 10$.

**Solución:**

**a) Cota teórica:**

Error del trapecio compuesto:
$$E_T = -\frac{(b-a)^3}{12n^2}f''(\xi), \quad \xi \in [a,b]$$

Para $f(x) = e^x$: $f''(x) = e^x$

Máximo en $[0,1]$: $f''(1) = e \approx 2.7183$

$$|E_T| \leq \frac{(1)^3}{12(10)^2} \cdot e = \frac{2.7183}{1200} = 0.00227$$

**b) Error real:**

$h = 0.1$

Cálculo directo con trapecio compuesto $n = 10$:
$$I_{10} = \frac{0.1}{2}[e^0 + 2(e^{0.1} + e^{0.2} + ... + e^{0.9}) + e^1]$$
$$= 0.05[1 + 2(8.0997) + 2.7183] = 0.05(19.9177) = 1.71745$$

Valor exacto: $e - 1 = 1.71828$

Error real: $|1.71745 - 1.71828| = 0.00083$

**Comparación:** Error real (0.00083) < Cota (0.00227) ✓

---

## Solución 7.1: AUC Farmacológico

**Problema:** Calcular el AUC con los datos de concentración usando Simpson compuesto.

**Datos:**
| $t$ (h) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---------|---|---|---|---|---|---|---|
| $C$ (mg/L) | 0 | 8.5 | 15.2 | 12.1 | 8.3 | 5.0 | 2.8 |

**Solución:**

$n = 6$ (par), $h = 1$ hora

Fórmula Simpson compuesto:
$$\text{AUC} = \frac{h}{3}[C_0 + 4(C_1 + C_3 + C_5) + 2(C_2 + C_4) + C_6]$$

**[Sustitución](../../../glossary.md#sustitución):**
$$\text{AUC} = \frac{1}{3}[0 + 4(8.5 + 12.1 + 5.0) + 2(15.2 + 8.3) + 2.8]$$
$$= \frac{1}{3}[0 + 4(25.6) + 2(23.5) + 2.8]$$
$$= \frac{1}{3}[102.4 + 47.0 + 2.8]$$
$$= \frac{152.2}{3} = 50.73 \text{ mg·h/L}$$

**Interpretación:** El área bajo la curva de concentración-tiempo es aproximadamente 50.73 mg·h/L, medida importante en farmacocinética para determinar la biodisponibilidad del fármaco.

---

## Solución 7.4: Longitud de Arco

**Problema:** Aproximar longitud de $y = x^2$ en $[0, 1]$ con Simpson $n = 4$.

**Solución:**

$$L = \int_0^1 \sqrt{1 + (y')^2}\,dx = \int_0^1 \sqrt{1 + 4x^2}\,dx$$

$h = 0.25$

Sea $g(x) = \sqrt{1 + 4x^2}$:

| $i$ | $x_i$ | $g(x_i)$ | Coef. | Contrib. |
|-----|-------|----------|-------|----------|
| 0 | 0 | $\sqrt{1} = 1$ | 1 | 1.0000 |
| 1 | 0.25 | $\sqrt{1.25} = 1.118$ | 4 | 4.4721 |
| 2 | 0.5 | $\sqrt{2} = 1.414$ | 2 | 2.8284 |
| 3 | 0.75 | $\sqrt{3.25} = 1.803$ | 4 | 7.2111 |
| 4 | 1 | $\sqrt{5} = 2.236$ | 1 | 2.2361 |

Suma = 17.7477

$$L = \frac{0.25}{3} \times 17.7477 = 1.479$$

**Valor exacto (usando sustitución hiperbólica):**
$$L = \frac{1}{2}\left[\sqrt{5} + \frac{\sinh^{-1}(2)}{2}\right] = 1.4789$$

**Error:** $|1.479 - 1.4789| = 0.0001$ (0.007%)

---

## Solución 4.3: Gauss-Legendre con Cambio de Variable

**Problema:** Calcular $\int_1^3 \ln x\,dx$ usando Gauss-Legendre con 3 puntos.

**Solución:**

**Paso 1:** Cambio de variable de $[1,3]$ a $[-1,1]$:
$$x = \frac{3-1}{2}t + \frac{3+1}{2} = t + 2$$
$$dx = dt$$

$$\int_1^3 \ln x\,dx = \int_{-1}^{1} \ln(t+2)\,dt$$

**Paso 2:** Nodos y pesos para $n = 3$:

| $i$ | $t_i$ | $w_i$ |
|-----|-------|-------|
| 1 | $-\sqrt{0.6} = -0.7746$ | 5/9 = 0.5556 |
| 2 | 0 | 8/9 = 0.8889 |
| 3 | $+\sqrt{0.6} = +0.7746$ | 5/9 = 0.5556 |

**Paso 3:** Evaluar $f(t) = \ln(t+2)$:

| $i$ | $t_i$ | $x_i = t_i + 2$ | $\ln(x_i)$ | $w_i$ | $w_i \ln(x_i)$ |
|-----|-------|-----------------|------------|-------|----------------|
| 1 | -0.7746 | 1.2254 | 0.2035 | 0.5556 | 0.1131 |
| 2 | 0 | 2 | 0.6931 | 0.8889 | 0.6161 |
| 3 | 0.7746 | 2.7746 | 1.0205 | 0.5556 | 0.5670 |

**Paso 4:** Resultado:
$$I = \frac{3-1}{2} \sum w_i f(t_i) = 1 \times (0.1131 + 0.6161 + 0.5670) = 1.2962$$

**Verificación:**
$$\int_1^3 \ln x\,dx = [x\ln x - x]_1^3 = (3\ln 3 - 3) - (0 - 1) = 3\ln 3 - 2 = 1.2958$$

**Error:** $|1.2962 - 1.2958| = 0.0004$
