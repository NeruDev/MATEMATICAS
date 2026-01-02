<!--
::METADATA::
type: answer-key
topic_id: mn-02-interpolacion
file_id: MN-02-Respuestas
status: stable
audience: student
total_problems: 30
solved_detailed: 0
-->

# Respuestas Rápidas - Interpolación

> **Leyenda:** ✅ Solución desarrollada | ➖ Solo respuesta

## Tabla de Respuestas

### Sección 1: Interpolación de Lagrange

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-01] | $P(x) = x^2 - 2x + 1 = (x-1)^2$ | ➖ |
| [Prob-02] | a) $P(x) = x^2 + 1$; b) $P(0.5) = 1.25$ | ➖ |
| [Prob-03] | $P_2(x)$ interpolante; $\ln(3) \approx 1.0986$; estimación $\approx 1.0397$ | ➖ |
| [Prob-04] | $\sum_{i=0}^{n} L_i(x) = 1$ pues interpola $f(x) = 1$ exactamente | ➖ |

### Sección 2: Diferencias Divididas

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-05] | $P(x) = -1 + 2x + 0(x)(x-1) + 0 = -1 + 2x$; [polinomio](../../../glossary.md#polinomio) lineal | ➖ |
| [Prob-06] | a) $f[0,1] = 1$; b) $f[0,1,2] = 3$; c) $f[0,1,2,3] = 1$ | ➖ |
| [Prob-07] | Demostración por inducción sobre definición recursiva | ➖ |
| [Prob-08] | $f[x_0, \ldots, x_n] = a_n$ (coeficiente líder del [polinomio](../../../glossary.md#polinomio)) | ➖ |

### Sección 3: Datos Equiespaciados

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-09] | $\Delta^0: 1,1,2,6,24$; $\Delta^1: 0,1,4,18$; $\Delta^2: 1,3,14$; $\Delta^3: 2,11$; $\Delta^4: 9$ | ➖ |
| [Prob-10] | $y(1.25) \approx 0.949$ usando Newton regresivo | ➖ |
| [Prob-11] | $\sin(0.15) \approx 0.1494$ (valor exacto: $0.14944$) | ➖ |

### Sección 4: Error de Interpolación

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-12] | $\|E(x)\| \leq \frac{e}{8} \approx 0.3398$ (cota superior) | ➖ |
| [Prob-13] | a) $P_2(x)$ por Lagrange; b) $\|E(x)\| \leq \frac{1}{6}\left(\frac{\pi}{4}\right)^3 \approx 0.0323$ | ➖ |
| [Prob-14] | [Fenómeno de Runge](../../../glossary.md#fenomeno-de-runge): oscilaciones cerca de extremos; $\|f^{(n+1)}\| \to \infty$ | ➖ |
| [Prob-15] | Chebyshev $n=3$: $x_k = \cos\left(\frac{2k+1}{8}\pi\right)$; $x \approx \pm 0.924, \pm 0.383$ | ➖ |

### Sección 5: Splines Cúbicos

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-16] | $S_0(x) = x - x^3/2$; $S_1(x) = 1 - (x-1) - \frac{3}{2}(x-1)^2 + \frac{1}{2}(x-1)^3$ | ➖ |
| [Prob-17] | a) Sistema $4 \times 4$ para coeficientes; b) $S(1.5) \approx 2.5$ | ➖ |
| [Prob-18] | Spline: suave sin oscilaciones; Polinomio grado 4: posibles oscilaciones | ➖ |
| [Prob-19] | Splines: grado 3 local evita acumulación de error; nodos no afectan globalmente | ➖ |

### Sección 6: Interpolación de Hermite

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-20] | $H(x) = 1 + 2x - 2x^2 + x^3$ (polinomio de grado 3) | ➖ |
| [Prob-21] | $H(x) = 1 + x + \frac{1}{2}x^2 + \frac{e-2}{2}x^2(x-1)$ | ➖ |

### Sección 7: Problemas Aplicados

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-22] | a) Lagrange grado 2: $\rho(50) \approx 0.988$ g/cm³; b) Spline: $\approx 0.9881$ g/cm³ | ➖ |
| [Prob-23] | a) $P_3(t)$; b) $x(1.5) \approx 11.0$ m; c) $v(1.5) = P_3'(1.5) \approx 5.5$ m/s | ➖ |
| [Prob-24] | Spline sujeto con $S'(0) = S'(200) = 0$; curva suave con pendiente cero en extremos | ➖ |

### Sección 8: Problemas de Implementación

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-25] | Algoritmo: tabla triangular de [diferencias divididas](../../../glossary.md#diferencias-divididas) $O(n^2)$ | ➖ |
| [Prob-26] | Sistema tridiagonal $Ax = b$ para segundas [derivadas](../../../glossary.md#derivadas); $O(n)$ con Thomas | ➖ |
| [Prob-27] | Mismo resultado; Newton más eficiente para agregar puntos | ➖ |

### Sección 9: Problemas Teóricos

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-28] | Unicidad del polinomio interpolante de grado $\leq n$ | ➖ |
| [Prob-29] | Usar teorema de Rolle $n+1$ veces sobre $E(x) = f(x) - P_n(x)$ | ➖ |
| [Prob-30] | Minimiza energía de flexión; spline = "regla flexible" | ➖ |

---

> 📚 **Archivo de problemas:** [`problems/MN-02-Problemas.md`](../problems/MN-02-Problemas.md)
