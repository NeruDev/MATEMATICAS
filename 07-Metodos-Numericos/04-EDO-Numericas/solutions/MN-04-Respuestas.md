<!--
::METADATA::
type: answer-key
topic_id: mn-04-[edo](../../../glossary.md#edo)-numericas
file_id: MN-04-Respuestas
status: stable
audience: student
total_problems: 34
solved_detailed: 0
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Respuestas Rápidas - Solución Numérica de EDO

> **Leyenda:** ✅ Solución desarrollada | ➖ Solo respuesta

## Tabla de Respuestas

### Sección 1: Método de Euler

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-01] | Euler: $y(0.5) \approx 1.2840$; exacto $e^{0.25} \approx 1.2840$; error $\approx 0.5\%$ | ➖ |
| [Prob-02] | $y(1) \approx 3.4146$ (Euler); exacto $\approx 3.4366$; errores crecientes | ➖ |
| [Prob-03] | a) $h=0.5$: inestable; $h=0.25$: estable; c) condición: $h < 1$ | ➖ |
| [Prob-04] | $y(30) \approx 2.03$ kg de sal | ➖ |
| [Prob-05] | Euler implícito estable para $h \leq 0.3$; explícito requiere $h < 0.2$ | ➖ |

### Sección 2: Método de Heun

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-06] | Heun: $y(0.4) \approx 1.5948$; Euler: $\approx 1.5456$; Heun más preciso | ➖ |
| [Prob-07] | $y(2) \approx 4.4817$ | ➖ |
| [Prob-08] | $v(2) \approx 13.8$ m/s (velocidad descendiendo) | ➖ |
| [Prob-09] | Razón errores $\approx 4:1$ (Heun [orden](../../../glossary.md#orden) 2, Euler orden 1) | ➖ |

### Sección 3: Runge-Kutta

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-10] | RK4: $y(1) \approx 2.6402$; exacto $= 2.6409$; error $< 0.03\%$ | ➖ |
| [Prob-11] | $y(0.5) \approx 5.7396$ | ➖ |
| [Prob-12] | RK4: $y(1) \approx 1.5574$; RK2: $y(1) \approx 1.5502$; RK4 más preciso | ➖ |
| [Prob-13] | $i(1) \approx 2.528$ A (corriente estacionaria $= 3$ A) | ➖ |
| [Prob-14] | RK4 exacto para polinomios grado $\leq 4$ pues error $O(h^5)$ | ➖ |

### Sección 4: Métodos Multipaso

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-15] | $y_4 \approx 2.1832$; $y_5 \approx 2.2961$ | ➖ |
| [Prob-16] | Predictor-Corrector: $y(0.5) \approx 1.7958$ | ➖ |
| [Prob-17] | RK4: $4n$ evaluaciones; AB4: $n$ evaluaciones (después de arranque) | ➖ |

### Sección 5: Sistemas de EDO

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-18] | Sistema: $y_1' = y_2$, $y_2' = -y_1$; $y(0.3) \approx 0.9553$; $\cos(0.3) = 0.9553$ | ➖ |
| [Prob-19] | $(x(0.4), y(0.4)) \approx (1.1756, 0.7052)$ | ➖ |
| [Prob-20] | Oscilaciones: presas y depredadores oscilan desfasados; período $\approx 15$ unidades | ➖ |
| [Prob-21] | Péndulo oscila: $\theta(2) \approx -0.48$ rad (cuasi-periódico) | ➖ |
| [Prob-22] | Van der Pol: ciclo [límite](../../../glossary.md#limite); oscilaciones no armónicas | ➖ |

### Sección 6: Análisis de Error y Estabilidad

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-23] | a) $h_{max} = 0.4$; b) $h=0.3$: estable; $h=0.5$: inestable (oscila) | ➖ |
| [Prob-24] | Richardson: $y_{exacto} \approx 2y_{h/2} - y_h = 2(2.6408) - 2.5937 \approx 2.6879$ | ➖ |
| [Prob-25] | a) $y_h(1) \approx 2.6887$; $y_{h/2}(1) \approx 2.7169$; b) Error $\approx 0.0019$ | ➖ |
| [Prob-26] | Rigidez: $\lambda = -1000$; Euler explícito requiere $h < 0.002$ | ➖ |

### Sección 7: Problemas Aplicados

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-27] | $T = 50°C$ en $t \approx 6.93$ min (exacto: $t = 10\ln 2$) | ➖ |
| [Prob-28] | $P = 500$ en $t \approx 16.1$ unidades de tiempo | ➖ |
| [Prob-29] | a) $v(10) \approx 43.8$ m/s; b) $v_{terminal} \approx 44.3$ m/s | ➖ |
| [Prob-30] | $c(5) \approx 0.444$ mol/L (exacto: $c = 2/(1+5t)$) | ➖ |
| [Prob-31] | Oscilación amortiguada; amplitud decrece exponencialmente | ➖ |

### Sección 8: Problemas de Diseño

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-32] | RK adaptativo: comparar RK4 vs RK5; ajustar $h$ si error $>$ tol | ➖ |
| [Prob-33] | Comparador: tabla con errores, evaluaciones de $f$, tiempo CPU | ➖ |
| [Prob-34] | RKF45: $y(1) \approx e$ con error $< 10^{-8}$; $h$ adaptativo | ➖ |

---

> 📚 **Archivo de problemas:** [problems/MN-04-Problemas.md](../problems/MN-04-Problemas.md)
