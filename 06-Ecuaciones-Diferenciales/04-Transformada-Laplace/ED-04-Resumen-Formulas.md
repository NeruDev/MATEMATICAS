<!--
::METADATA::
type: cheatsheet
topic_id: ed-04-transformada-laplace
file_id: ED-04-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

---

# Resumen rápido — Transformada de Laplace

## Definición

$$\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty e^{-st}f(t)\,dt$$

**Condición de existencia:** $f(t)$ de [orden](../..](../../glossary.md)#orden) exponencial y seccionalmente continua.

---

## Tabla de Transformadas Básicas

| $f(t)$ | $F(s) = \mathcal{L}\{f(t)\}$ | Restricción |
|--------|------------------------------|-------------|
| $1$ | $\dfrac{1}{s}$ | $s > 0$ |
| $t$ | $\dfrac{1}{s^2}$ | $s > 0$ |
| $t^n$ | $\dfrac{n!}{s^{n+1}}$ | $s > 0$ |
| $e^{at}$ | $\dfrac{1}{s-a}$ | $s > a$ |
| $t^n e^{at}$ | $\dfrac{n!}{(s-a)^{n+1}}$ | $s > a$ |
| $\sin(bt)$ | $\dfrac{b}{s^2+b^2}$ | $s > 0$ |
| $\cos(bt)$ | $\dfrac{s}{s^2+b^2}$ | $s > 0$ |
| $\sinh(bt)$ | $\dfrac{b}{s^2-b^2}$ | $s > \lvert b \rvert$ |
| $\cosh(bt)$ | $\dfrac{s}{s^2-b^2}$ | $s > \lvert b \rvert$ |
| $e^{at}\sin(bt)$ | $\dfrac{b}{(s-a)^2+b^2}$ | $s > a$ |
| $e^{at}\cos(bt)$ | $\dfrac{s-a}{(s-a)^2+b^2}$ | $s > a$ |
| $t\sin(bt)$ | $\dfrac{2bs}{(s^2+b^2)^2}$ | $s > 0$ |
| $t\cos(bt)$ | $\dfrac{s^2-b^2}{(s^2+b^2)^2}$ | $s > 0$ |

---

## Propiedades Fundamentales

### Linealidad
$$\mathcal{L}\{af(t) + bg(t)\} = aF(s) + bG(s)$$

### Derivadas
$$\mathcal{L}\{f'(t)\} = sF(s) - f(0)$$
$$\mathcal{L}\{f''(t)\} = s^2F(s) - sf(0) - f'(0)$$
$$\mathcal{L}\{f^{(n)}(t)\} = s^nF(s) - s^{n-1}f(0) - \cdots - f^{(n-1)}(0)$$

### Integral
$$\mathcal{L}\left\{\int_0^t f(\tau)\,d\tau\right\} = \frac{F(s)}{s}$$

### Multiplicación por $t$
$$\mathcal{L}\{t^n f(t)\} = (-1)^n \frac{d^n F(s)}{ds^n}$$

### División por $t$
$$\mathcal{L}\left\{\frac{f(t)}{t}\right\} = \int_s^\infty F(\sigma)\,d\sigma$$

---

## Teoremas de Traslación

### Primera traslación (en $s$)
$$\mathcal{L}\{e^{at}f(t)\} = F(s-a)$$

### Segunda traslación (en $t$)
$$\mathcal{L}\{u(t-a)f(t-a)\} = e^{-as}F(s)$$

donde $u(t-a)$ es la [función](../..](../../glossary.md)#funcion) escalón unitario.

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
1. Aplicar $\mathcal{L}$ a ambos lados de la [EDO](../..](../../glossary.md)#edo)
2. Usar propiedades de [derivadas](../..](../../glossary.md)#derivadas) con condiciones iniciales
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
IA: Hoja de referencia rápida para [Transformada de Laplace](../..](../../glossary.md)#transformada-de-laplace).
Para desarrollo completo: [theory/ED-04-Teoria-Laplace.md](theory/ED-04-Teoria-Laplace.md)
file_id: ED-04-Resumen-Formulas
-->
