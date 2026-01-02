<!--
::METADATA::
type: answer-key
topic_id: mn-01-raices-ecuaciones
file_id: MN-01-Respuestas
status: stable
audience: student
total_problems: 32
solved_detailed: 0
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Respuestas Rápidas - Raíces de Ecuaciones

> **Leyenda:** ✅ Solución desarrollada | ➖ Solo respuesta

## Tabla de Respuestas

### Sección 1: Método de Bisección

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-01] | $x \approx 1.3247$ (raíz de $x^3 - x - 1 = 0$) | ➖ |
| [Prob-02] | $n = 23$ iteraciones ($n \geq \log_2\left(\frac{4-0}{10^{-6}}\right)$) | ➖ |
| [Prob-03] | $x \approx 0.7391$ (punto fijo de $\cos(x) = x$) | ➖ |
| [Prob-04] | $x \approx 0.5671$ (punto de Lambert) | ➖ |

### Sección 2: Método de Newton-Raphson

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-05] | $\sqrt{5} \approx 2.2361$ (en 4 iteraciones desde $x_0=2$) | ➖ |
| [Prob-06] | $x \approx 2.0946$ (raíz de $x^3 - 2x - 5 = 0$) | ➖ |
| [Prob-07] | $x = e \approx 2.7183$ (solución exacta de $\ln(x) = 1$) | ➖ |
| [Prob-08] | Falla: $f'(x) = \frac{1}{3x^{2/3}} \to \infty$ cerca de 0, iterados divergen | ➖ |
| [Prob-09] | Newton estándar: [convergencia](../../../glossary.md#convergencia) lineal; Newton modificado ($m=2$): convergencia cuadrática restaurada | ➖ |

### Sección 3: Método de la Secante

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-10] | $x \approx 0.6824$ (raíz de $x^3 + x - 1 = 0$) | ➖ |
| [Prob-11] | Newton: 4-5 iteraciones; Secante: 6-7 iteraciones; ambos convergen a $x \approx 0.5671$ | ➖ |
| [Prob-12] | $x \approx 4.4934$ (primera raíz positiva no [trivial](../../../glossary.md#trivial) de $\tan(x) = x$) | ➖ |

### Sección 4: Método de Punto Fijo

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-13] | $g_1(x) = \sqrt[3]{x+1}$ converge; otras pueden diverger según $\lvert g'(x) \rvert$ | ➖ |
| [Prob-14] | $x \approx 1.8955$ (solución de $x = 2\sin(x)$) | ➖ |
| [Prob-15] | $\lvert g'(x) \rvert = e^{-x} < 1$ en $[0,1]$, por Teorema del Punto Fijo converge a $x \approx 0.5671$ | ➖ |
| [Prob-16] | $g_2$: diverge ($\lvert g'_2(x) \rvert > 1$); $g_3$: converge cuadráticamente a $\sqrt[3]{2} \approx 1.2599$ | ➖ |

### Sección 5: Análisis de Convergencia

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-17] | Newton: $x_{n+1} = \frac{1}{2}\left(x_n + \frac{a}{x_n}\right)$; [convergencia](../../../glossary.md#convergencia) cuadrática: $e_{n+1} \approx \frac{e_n^2}{2\sqrt{a}}$ | ➖ |
| [Prob-18] | Bisección: [orden](../../../glossary.md#orden) 1 (lineal); $\lvert e_{n+1} \rvert \approx 0.5\lvert e_n \rvert$ | ➖ |
| [Prob-19] | Newton: $IE = 2^{1/2} \approx 1.414$; Secante: $IE = \phi^{1/1} \approx 1.618$; Secante más eficiente | ➖ |

### Sección 6: Problemas Aplicados

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-20] | $x \approx 1.3797$ (punto de deflexión cero en viga) | ➖ |
| [Prob-21] | TIR $\approx 22.3\%$ ($r \approx 0.223$) | ➖ |
| [Prob-22] | $t = 1$ y $t = 4$ segundos (posiciones donde partícula cruza origen) | ➖ |
| [Prob-23] | $x \approx 0.7639$ (concentración de equilibrio) | ➖ |
| [Prob-24] | $\omega \approx 2.0946$ rad/s (frecuencia de [resonancia](../../../glossary.md#resonancia)) | ➖ |

### Sección 7: Problemas de Implementación

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-25] | $x \approx 1.8955$ (raíz de $\sin(x) - x/2 = 0$ en $[\pi/2, \pi]$) | ➖ |
| [Prob-26] | Implementación con `max_iter` y detección de $\|x_{n+1} - x_n\| > M$ | ➖ |
| [Prob-27] | Selector: usar Newton si $f'$ disponible; bisección como respaldo | ➖ |
| [Prob-28] | Steffensen: convergencia cuadrática sin necesitar $f'$ | ➖ |

### Sección 8: Problemas Teóricos

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-29] | $e_{n+1} \approx \frac{f''(x^*)}{2f'(x^*)}e_n^2$ implica [orden](../../../glossary.md#orden) 2 | ➖ |
| [Prob-30] | Orden $= \phi = \frac{1+\sqrt{5}}{2} \approx 1.618$ (número áureo) | ➖ |
| [Prob-31] | Teorema de Banach: contracción en espacio completo tiene punto fijo único | ➖ |
| [Prob-32] | Ciclo: $0 \to 1 \to 0 \to 1 \to \ldots$ (comportamiento periódico) | ➖ |

---

> 📚 **Archivo de problemas:** [problems/MN-01-Problemas.md](../problems/MN-01-Problemas.md)
