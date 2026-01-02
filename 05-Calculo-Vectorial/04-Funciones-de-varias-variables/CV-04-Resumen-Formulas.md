<!--
::METADATA::
type: cheatsheet
topic_id: cv-04-funciones-varias-variables
file_id: CV-04-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Resumen rápido — Funciones de varias variables

## Límites y continuidad

| Concepto | Fórmula / Criterio |
|----------|---------------------|
| **Límite** | $\lim_{(x,y) \to (a,b)} f(x,y) = L$ |
| **No existe si** | Diferentes trayectorias dan diferentes límites |
| **Continuidad** | $\lim_{(x,y) \to (a,b)} f(x,y) = f(a,b)$ |

## Derivadas parciales

| Notación | Definición |
|----------|------------|
| $f_x = \frac{\partial f}{\partial x}$ | $\lim_{h \to 0} \frac{f(x+h, y) - f(x,y)}{h}$ |
| $f_y = \frac{\partial f}{\partial y}$ | $\lim_{h \to 0} \frac{f(x, y+h) - f(x,y)}{h}$ |

## Derivadas de orden superior

| Notación | Significado |
|----------|-------------|
| $f_{xx}$ | $\frac{\partial^2 f}{\partial x^2}$ |
| $f_{yy}$ | $\frac{\partial^2 f}{\partial y^2}$ |
| $f_{xy} = f_{yx}$ | $\frac{\partial^2 f}{\partial y \partial x}$ (si son continuas) |

## Diferenciabilidad

| Concepto | Fórmula |
|----------|---------|
| **Diferencial total** | $df = f_x\,dx + f_y\,dy + f_z\,dz$ |
| **Aproximación lineal** | $f(x,y) \approx f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)$ |
| **Plano tangente** | $z - z_0 = f_x(x_0,y_0)(x-x_0) + f_y(x_0,y_0)(y-y_0)$ |

## Regla de la cadena

| Caso | Fórmula |
|------|---------|
| $z = f(x,y)$, $x = x(t)$, $y = y(t)$ | $\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}$ |
| $z = f(x,y)$, $x = x(s,t)$, $y = y(s,t)$ | $\frac{\partial z}{\partial s} = f_x \frac{\partial x}{\partial s} + f_y \frac{\partial y}{\partial s}$ |

## Gradiente

| Concepto | Fórmula |
|----------|---------|
| **Definición** | $\nabla f = \langle f_x, f_y \rangle$ o $\langle f_x, f_y, f_z \rangle$ |
| **Propiedad** | Apunta en dirección de máximo crecimiento |
| **Magnitud** | $\lVert \nabla f \rVert$ = tasa máxima de cambio |
| **Perpendicular** | $\nabla f \perp$ curvas/superficies de nivel |

## Derivada direccional

| Concepto | Fórmula |
|----------|---------|
| **Definición** | $D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}$ (donde $\lVert\mathbf{u}\rVert = 1$) |
| **Máximo** | En dirección de $\nabla f$, valor $= \lVert \nabla f \rVert$ |
| **Mínimo** | En dirección de $-\nabla f$, valor $= -\lVert \nabla f \rVert$ |
| **Cero** | Perpendicular a $\nabla f$ |

## Extremos locales

### Puntos críticos
$\nabla f = \mathbf{0}$ o $\nabla f$ no existe

### Criterio de la segunda derivada ($z = f(x,y)$)

Sea $D = f_{xx}f_{yy} - (f_{xy})^2$ en el [punto crítico](theory/CV-04-Teoria-Varias.md)
file_id: CV-04-Resumen-Formulas
-->
