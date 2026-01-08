<!--
::METADATA::
type: cheatsheet
topic_id: ed-04-transformada-laplace
file_id: ED-04-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Resumen rápido — Transformada de Laplace

## Definición

$$\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty e^{-st}f(t)\,dt$$

**Condición de existencia:** $f(t)$ de [orden](../../glossary.md#funcion) escalón unitario.

---

## Funciones Especiales

### Función escalón unitario (Heaviside)
$$u(t-a) = \begin{cases} 0, & t < a \\ 1, & t \geq a \end{cases}$$

$$\mathcal{L}\{u(t-a)\} = \frac{e^{-as}}{s}$$

### Delta de Dirac
$$\mathcal{L}\{\delta(t-a)\} = e^{-as}$$

### Función periódica
$$\mathcal{L}\{f(t)\} = \frac{1}{1-e^{-Ts}}\int_0^T e^{-st}f(t)\,dt$$

donde $T$ es el período.

---

## Convolución

$$(f * g)(t) = \int_0^t f(\tau)g(t-\tau)\,d\tau$$

$$\mathcal{L}\{f * g\} = F(s) \cdot G(s)$$

$$\mathcal{L}^{-1}\{F(s)G(s)\} = f * g$$

---

## Transformada Inversa por Fracciones Parciales

### Factores lineales simples
$$\frac{P(s)}{(s-a)(s-b)} = \frac{A}{s-a} + \frac{B}{s-b}$$

### Factores lineales repetidos
$$\frac{P(s)}{(s-a)^n} = \frac{A_1}{s-a} + \frac{A_2}{(s-a)^2} + \cdots + \frac{A_n}{(s-a)^n}$$

### Factores cuadráticos irreducibles
$$\frac{P(s)}{s^2+bs+c} = \frac{As+B}{s^2+bs+c}$$

---

## Resolución de PVI

### Método
1. Aplicar $\mathcal{L}$ a ambos lados de la [EDO](../../glossary.md#derivadas) con condiciones iniciales
3. Despejar $Y(s)$
4. Aplicar $\mathcal{L}^{-1}$ para obtener $y(t)$

### Ejemplo típico
$$y'' + ay' + by = g(t), \quad y(0)=y_0, \; y'(0)=y_1$$

$$s^2Y - sy_0 - y_1 + a(sY - y_0) + bY = G(s)$$

$$(s^2 + as + b)Y = G(s) + (s+a)y_0 + y_1$$

---

## Función de Transferencia

Para sistema $ay'' + by' + cy = f(t)$ con condiciones iniciales cero:

$$H(s) = \frac{Y(s)}{F(s)} = \frac{1}{as^2 + bs + c}$$

---

<!--
IA: Hoja de referencia rápida para [Transformada de Laplace](theory/ED-04-Teoria-Transformada-Laplace.md)
file_id: ED-04-Resumen-Formulas
-->
