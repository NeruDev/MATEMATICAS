<!--
IA:
Este archivo contiene directivas específicas para el tema de Geometría Analítica.
-->

# Directivas: Geometría Analítica

## Clasificación del Tema

| Campo | Valor |
|-------|-------|
| **Módulo** | 01-Fundamentos |
| **Código** | 06 |
| **Nombre** | Geometría Analítica |
| **Prerequisitos** | Álgebra, Geometría Euclidiana |
| **Nivel** | Intermedio-Avanzado |

---

## Subtemas

| Código | Subtema | Tipo |
|--------|---------|------|
| 6.1 | El Plano Cartesiano | conceptual |
| 6.2 | Distancia y Punto Medio | procedimental |
| 6.3 | La Línea Recta | procedimental |
| 6.4 | La Circunferencia | procedimental |
| 6.5 | La Parábola | procedimental |
| 6.6 | La Elipse | procedimental |
| 6.7 | La Hipérbola | procedimental |
| 6.8 | Ecuación General de Segundo Grado | analítico |
| 6.9 | Transformaciones en el Plano | procedimental |
| 6.10 | Aplicaciones | aplicado |

---

## Convenciones de Notación

### Puntos y Coordenadas
- Puntos: letras mayúsculas $P$, $Q$, $A$, $B$
- Coordenadas: $(x, y)$, $(x_1, y_1)$, $(h, k)$
- Origen: $O(0, 0)$

### Parámetros de Cónicas
| Símbolo | Significado |
|---------|-------------|
| $(h, k)$ | Centro o vértice |
| $a$ | Semieje mayor (elipse), semieje transverso (hipérbola) |
| $b$ | Semieje menor (elipse), semieje conjugado (hipérbola) |
| $c$ | Distancia focal (del centro al foco) |
| $p$ | Parámetro de la parábola (distancia vértice-foco) |
| $e$ | Excentricidad |
| $r$ | Radio (circunferencia) |

### Relaciones Fundamentales
- **Elipse:** $c^2 = a^2 - b^2$, $e = \frac{c}{a} < 1$
- **Hipérbola:** $c^2 = a^2 + b^2$, $e = \frac{c}{a} > 1$
- **Parábola:** $e = 1$

---

## Ecuaciones de Referencia Rápida

### Distancia y Punto Medio
$$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$$
$$M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$$

### Línea Recta
| Forma | Ecuación |
|-------|----------|
| Pendiente-ordenada | $y = mx + b$ |
| Punto-pendiente | $y - y_1 = m(x - x_1)$ |
| General | $Ax + By + C = 0$ |
| Simétrica | $\frac{x}{a} + \frac{y}{b} = 1$ |

**Pendiente:** $m = \frac{y_2 - y_1}{x_2 - x_1} = \tan\theta$

**Distancia punto-recta:** $d = \frac{\lvert Ax_0 + By_0 + C \rvert}{\sqrt{A^2 + B^2}}$

### Circunferencia
- **Estándar:** $(x-h)^2 + (y-k)^2 = r^2$
- **General:** $x^2 + y^2 + Dx + Ey + F = 0$

### Parábola (vértice en origen)
| Orientación | Ecuación | Foco | Directriz |
|-------------|----------|------|-----------|
| Derecha | $y^2 = 4px$ | $(p, 0)$ | $x = -p$ |
| Izquierda | $y^2 = -4px$ | $(-p, 0)$ | $x = p$ |
| Arriba | $x^2 = 4py$ | $(0, p)$ | $y = -p$ |
| Abajo | $x^2 = -4py$ | $(0, -p)$ | $y = p$ |

### Elipse (centro en origen)
| Eje mayor | Ecuación | Focos | Vértices |
|-----------|----------|-------|----------|
| Horizontal | $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ | $(\pm c, 0)$ | $(\pm a, 0)$ |
| Vertical | $\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1$ | $(0, \pm c)$ | $(0, \pm a)$ |

### Hipérbola (centro en origen)
| Eje transverso | Ecuación | Asíntotas |
|----------------|----------|-----------|
| Horizontal | $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ | $y = \pm\frac{b}{a}x$ |
| Vertical | $\frac{y^2}{a^2} - \frac{x^2}{b^2} = 1$ | $y = \pm\frac{a}{b}x$ |

---

## Clasificación de Cónicas

Para $Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$:

| Discriminante $B^2 - 4AC$ | Cónica |
|---------------------------|--------|
| $< 0$ (y $A = C$, $B = 0$) | Circunferencia |
| $< 0$ (otros casos) | Elipse |
| $= 0$ | Parábola |
| $> 0$ | Hipérbola |

---

## Preferencias de Formato

1. **Respuestas exactas:** Usar radicales, no decimales
2. **Ecuaciones:** Preferir forma estándar sobre general
3. **Verificación:** Confirmar sustituyendo puntos conocidos
4. **Gráficas:** Identificar siempre centro/vértice, focos, orientación
5. **Valor absoluto en tablas:** Usar `$\lvert x \rvert$`
