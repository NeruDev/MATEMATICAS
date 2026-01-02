<!--
::METADATA::
type: cheatsheet
topic_id: cd-03-aplicaciones
file_id: CD-03-Resumen-Formulas
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Resumen de Fórmulas: Aplicaciones de la Derivada

## Puntos Críticos

Un punto $c$ es **crítico** si:
- $f'(c) = 0$, o
- $f'(c)$ no existe

## Extremos Absolutos (Teorema de Valores Extremos)

Si $f$ es continua en $[a, b]$, entonces $f$ alcanza un máximo y un mínimo absolutos en:
- Los puntos críticos en $(a, b)$
- Los extremos del intervalo: $a$ y $b$

## Criterio de la Primera Derivada

| Cambio de signo de $f'$ | Conclusión |
|-------------------------|------------|
| $(+) \to (-)$ | Máximo local en $c$ |
| $(-) \to (+)$ | Mínimo local en $c$ |
| Sin cambio | No hay extremo |

## Criterio de la Segunda Derivada

Sea $c$ [tal que](../../glossary.md#concavidad) |
|-------------------|------------|
| $f''(x) > 0$ | Cóncava hacia arriba (convexa) ∪ |
| $f''(x) < 0$ | Cóncava hacia abajo ∩ |

**[Punto de inflexión](../../glossary.md#concavidad).

## Razón de Cambio

$$\text{Tasa instantánea de cambio} = f'(x) = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}$$

### Razones Relacionadas

Si $x$ e $y$ son funciones del tiempo $t$:

$$\frac{dy}{dt} = \frac{dy}{dx} \cdot \frac{dx}{dt}$$

## Aproximación Lineal

La **aproximación lineal** de $f$ en $x = a$:

$$L(x) = f(a) + f'(a)(x - a)$$

**Error de aproximación**:
$$f(x) \approx L(x) \quad \text{cuando } x \approx a$$

## Diferenciales

$$dy = f'(x) \, dx$$

$$\Delta y \approx dy = f'(x) \, \Delta x$$

## Método de Newton-Raphson

Para encontrar raíces de $f(x) = 0$:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

## Movimiento Rectilíneo

Si $s(t)$ es la posición:

| Concepto | Fórmula |
|----------|---------|
| Velocidad | $v(t) = s'(t)$ |
| Rapidez | $\lvert v(t) \rvert$ |
| Aceleración | $a(t) = v'(t) = s''(t)$ |

## Optimización: Proceso Sistemático

1. **Identificar** la cantidad a optimizar
2. **Escribir** la [función](../../glossary.md#dominio)** y [continuidad](../../glossary.md#continuidad)
2. **Simetrías** (par, impar, periódica)
3. **Intersecciones** con ejes
4. **Asíntotas** (verticales, horizontales, oblicuas)
5. **Intervalos de crecimiento** ($f' > 0$ o $f' < 0$)
6. **Extremos locales** (puntos críticos)
7. **Concavidad** ($f'' > 0$ o $f'' < 0$)
8. **Puntos de inflexión**

---

> **Tip**: En problemas de optimización, siempre verifica que tu respuesta tenga sentido físico (dimensiones positivas, valores razonables).
