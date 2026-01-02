<!--
::METADATA::
type: answer-key
topic_id: mn-03-integracion-numerica
file_id: MN-03-Respuestas
status: stable
audience: student
total_problems: 37
solved_detailed: 0
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Respuestas Rápidas - Integración Numérica

> **Leyenda:** ✅ Solución desarrollada | ➖ Solo respuesta

## Tabla de Respuestas

### Sección 1: Regla del Trapecio

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-01] | $T = 4$; exacto $= 8/3 \approx 2.667$; error relativo $\approx 50\%$ | ➖ |
| [Prob-02] | $T_4 \approx 1.1167$; $\ln 3 \approx 1.0986$; error $\approx 1.6\%$ | ➖ |
| [Prob-03] | $n \geq 408$ subintervalos (usando cota $\|f''\| \leq 2$) | ➖ |
| [Prob-04] | $\int_1^3 f(x)\,dx \approx 7.1$ (trapecio compuesto) | ➖ |
| [Prob-05] | $T_2 = 1.5708$, $T_4 = 1.8961$, $T_8 = 1.9742$; exacto $= 2$ | ➖ |

### Sección 2: Regla de Simpson

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-06] | $S = 4$; exacto $= 4$; ¡Es exacto! Simpson integra cúbicas exactamente | ➖ |
| [Prob-07] | $S_4 \approx 3.1416$; $\pi \approx 3.14159$; error $< 0.001\%$ | ➖ |
| [Prob-08] | $S_4 \approx 0.7421$ | ➖ |
| [Prob-09] | Demostración: interpolar con Lagrange cúbico e integrar | ➖ |
| [Prob-10] | Distancia $\approx 14.9$ m (Simpson compuesto) | ➖ |
| [Prob-11] | $\int_1^4 \sqrt{x}\,dx = \frac{14}{3} \approx 4.667$; Trapecio $\approx 4.646$; Simpson $\approx 4.666$ | ➖ |

### Sección 3: Integración de Romberg

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-12] | $R_{3,3} \approx 1.71828$ (exacto $e - 1 = 1.71828...$) | ➖ |
| [Prob-13] | $R_{k,k} \to 1.000000$ con $k \approx 3-4$ iteraciones | ➖ |
| [Prob-14] | $\ln 2 \approx 0.693147$; Romberg converge en $R_{4,4}$ | ➖ |
| [Prob-15] | $R_{1,1} = \frac{4R_{1,0} - R_{0,0}}{3}$ equivale a Simpson simple | ➖ |
| [Prob-16] | Exacto $= 6.4$; Romberg exacto en nivel $R_{2,2}$ (grado 5) | ➖ |

### Sección 4: Cuadratura de Gauss

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-17] | $G_2 \approx 0.6321$ (exacto $= 1 - e^{-1} \approx 0.6321$) | ➖ |
| [Prob-18] | $G_2 \approx 1.5708$; $G_3 \approx 1.5708$; exacto $= \pi/2$ | ➖ |
| [Prob-19] | Cambio: $x = 2 + t$, $t \in [-1,1]$; $G_3 \approx 1.2958$ (exacto $\approx 1.2958$) | ➖ |
| [Prob-20] | Grado máximo $= 2n - 1 = 7$ para $n = 4$ puntos | ➖ |
| [Prob-21] | Verificación directa: $\int_{-1}^{1} x^k dx$ para $k = 0,1,2,3$ | ➖ |
| [Prob-22] | $\int_0^1 \sin(\pi x)\,dx = 2/\pi \approx 0.6366$; Gauss-3: $\approx 0.6366$; Simpson-6: $\approx 0.6366$ | ➖ |

### Sección 5: Estimación de Error

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-23] | a) Cota: $\frac{e}{1200} \approx 0.00227$; b) Error real $\approx 0.00166$ | ➖ |
| [Prob-24] | $n \geq 6$ subintervalos (pares para Simpson) | ➖ |
| [Prob-25] | Richardson: $I \approx 4T_{h/2}/3 - T_h/3 \approx 0.4286$ | ➖ |
| [Prob-26] | $I_{exacto} \approx I_{20} + \frac{I_{20} - I_{10}}{3} \approx 1.8464$ | ➖ |

### Sección 6: Integrales Dobles

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-27] | $\iint xy\,dA = 1/4 = 0.25$; Simpson simple da exacto | ➖ |
| [Prob-28] | $T_{2,2} \approx (e^2 - 1)^2/4 \approx 2.952$ (exacto $\approx 2.952$) | ➖ |
| [Prob-29] | Trapecio iterado: $\approx 0.2642$ | ➖ |

### Sección 7: Problemas Aplicados

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-30] | AUC $\approx 45.3$ mg·h/L | ➖ |
| [Prob-31] | Trabajo $W \approx 11.9$ J (Simpson compuesto) | ➖ |
| [Prob-32] | $P(X < 1) \approx 0.8413$ (usar Romberg + transformación) | ➖ |
| [Prob-33] | $L \approx 1.4789$ unidades | ➖ |
| [Prob-34] | $\text{erf}(1) \approx 0.8427$ | ➖ |

### Sección 8: Problemas de Diseño

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-35] | Selector: Romberg para alta precisión; Simpson para datos tabulados | ➖ |
| [Prob-36] | Adaptativo: subdividir donde $\|S_{2h} - S_h\| > \text{tol}$ | ➖ |
| [Prob-37] | Usar splines o Lagrange local + integrar; $\approx 1.68$ | ➖ |

---

> 📚 **Archivo de problemas:** [`problems/MN-03-Problemas.md`](../problems/MN-03-Problemas.md)
