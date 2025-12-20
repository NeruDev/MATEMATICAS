<!--
IA:
Directivas para Aplicaciones de la Derivada.
-->

# Directivas: Aplicaciones de la Derivada

## Clasificación del Tema

| Campo | Valor |
|-------|-------|
| **Módulo** | 02-Calculo-Diferencial |
| **Código** | 03 |
| **Nombre** | Aplicaciones de la Derivada |
| **Prerequisitos** | Derivadas |
| **Nivel** | Intermedio-Avanzado |

---

## Subtemas

| Código | Subtema | Tipo |
|--------|---------|------|
| 3.1 | Recta tangente y normal | procedimental |
| 3.2 | Razones relacionadas | aplicado |
| 3.3 | Valores extremos | procedimental |
| 3.4 | Criterio primera derivada | analítico |
| 3.5 | Criterio segunda derivada | analítico |
| 3.6 | Optimización | aplicado |
| 3.7 | Aproximaciones y diferenciales | aplicado |
| 3.8 | Análisis completo | analítico |
| 3.9 | Newton-Raphson | numérico |

---

## Fórmulas de Referencia

### Rectas
- **Tangente:** $y - f(a) = f'(a)(x - a)$
- **Normal:** $y - f(a) = -\frac{1}{f'(a)}(x - a)$

### Criterios
| Condición | Interpretación |
|-----------|----------------|
| $f'(x) > 0$ | Creciente |
| $f'(x) < 0$ | Decreciente |
| $f''(x) > 0$ | Cóncava arriba |
| $f''(x) < 0$ | Cóncava abajo |

### Newton-Raphson
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

### Aproximación Lineal
$$f(x) \approx f(a) + f'(a)(x - a)$$

---

## Preferencias de Formato

1. **Optimización:** Siempre verificar con segunda derivada o criterio
2. **Razones relacionadas:** Incluir diagrama conceptual
3. **Unidades:** Siempre incluir unidades en problemas aplicados
4. **Valor absoluto:** Usar `$\lvert x \rvert$` en tablas
