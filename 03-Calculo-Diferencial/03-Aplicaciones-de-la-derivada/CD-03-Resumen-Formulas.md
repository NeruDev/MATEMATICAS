<!--
::METADATA::
type: cheatsheet
topic_id: cd-03-aplicaciones
file_id: CD-03-Resumen-Formulas
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

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

Sea $c$ [tal que](../../glossary.md#tal-que) $f'(c) = 0$:

| Valor de $f''(c)$ | Conclusión |
|-------------------|------------|
| $f''(c) < 0$ | Máximo local |
| $f''(c) > 0$ | Mínimo local |
| $f''(c) = 0$ | Inconcluso |

## Concavidad y Puntos de Inflexión

| Signo de $f''(x)$ | [Concavidad](../../glossary.md#concavidad) |
|-------------------|------------|
| $f''(x) > 0$ | Cóncava hacia arriba (convexa) ∪ |
| $f''(x) < 0$ | Cóncava hacia abajo ∩ |

**[Punto de inflexión](../../glossary.md#punto-de-inflexion)**: Donde $f''(x) = 0$ o no existe, Y hay cambio de [concavidad](../../glossary.md#concavidad).

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
2. **Escribir** la [función](../../glossary.md#funcion) objetivo
3. **Establecer** restricciones
4. **Expresar** en una variable
5. **Derivar** e igualar a cero
6. **Verificar** que es máximo/mínimo
7. **Responder** la pregunta original

## Fórmulas de Geometría Útiles

| Figura | Perímetro/Área/Volumen |
|--------|------------------------|
| Rectángulo | $A = lw$, $P = 2l + 2w$ |
| Círculo | $A = \pi r^2$, $C = 2\pi r$ |
| Triángulo | $A = \frac{1}{2}bh$ |
| Esfera | $V = \frac{4}{3}\pi r^3$, $S = 4\pi r^2$ |
| Cilindro | $V = \pi r^2 h$, $S = 2\pi rh + 2\pi r^2$ |
| Cono | $V = \frac{1}{3}\pi r^2 h$ |

## Análisis Completo de Funciones

Para graficar $f(x)$, analizar:

1. **[Dominio](../../glossary.md#dominio)** y [continuidad](../../glossary.md#continuidad)
2. **Simetrías** (par, impar, periódica)
3. **Intersecciones** con ejes
4. **Asíntotas** (verticales, horizontales, oblicuas)
5. **Intervalos de crecimiento** ($f' > 0$ o $f' < 0$)
6. **Extremos locales** (puntos críticos)
7. **Concavidad** ($f'' > 0$ o $f'' < 0$)
8. **Puntos de inflexión**

---

> **Tip**: En problemas de optimización, siempre verifica que tu respuesta tenga sentido físico (dimensiones positivas, valores razonables).
