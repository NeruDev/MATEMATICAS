<!--
::METADATA::
type: answer-key
topic_id: ed-05-series-potencias
file_id: ED-05-Respuestas
status: stable
audience: student
total_problems: 20
solved_detailed: 0
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Respuestas Rápidas - Series de Potencias para EDO

> **Leyenda:** ✅ Solución desarrollada | ➖ Solo respuesta

## Tabla de Respuestas

| ID | Respuesta | Solución |
|:---|:----------|:--------:|
| [Prob-01] | a) $R = \infty$; b) $R = 0$; c) $R = 1$; d) $R = 3$ | ➖ |
| [Prob-02] | a) $\sum_{n=0}^{\infty}(-1)^n x^n$; b) $\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n}}{n!}$; c) $\sum_{n=1}^{\infty}\frac{(-1)^{n+1}x^n}{n}$ | ➖ |
| [Prob-03] | a) Ordinario; b) Singular; c) Ordinario; d) Singular regular | ➖ |
| [Prob-04] | a) $y = a_0\cos x + a_1\sin x$; b) $y = a_0\cosh x + a_1\sinh x$; c) $y = a_0 e^x$ | ➖ |
| [Prob-05] | a) Airy: $y = a_0\left(1 + \frac{x^3}{6} + \cdots\right) + a_1\left(x + \frac{x^4}{12} + \cdots\right)$; b) Hermite: $y = a_0(1 - x^2 + \cdots) + a_1(x - \frac{x^3}{3} + \cdots)$; c) Legendre: $y = x$ ([polinomio](../../../glossary.md#polinomio)) | ➖ |
| [Prob-06] | a) $y = 1 - \frac{x^2}{2} + \frac{x^4}{8} + \cdots$; b) $y = x + \frac{x^5}{20} + \cdots$ | ➖ |
| [Prob-07] | a) $a_{n+4} = -\frac{a_n}{(n+3)(n+4)}$; b) $a_{n+2} = \frac{2(n-1)a_n - (n-1)na_{n-2}}{(n+1)(n+2)}$ | ➖ |
| [Prob-08] | a) Singular regular; b) Singular irregular; c) Singular regular; d) Singular regular | ➖ |
| [Prob-09] | a) $r(2r-1) = 0 \Rightarrow r = 0, \frac{1}{2}$; b) $r^2 - \frac{1}{4} = 0 \Rightarrow r = \pm\frac{1}{2}$; c) $r(r-1) = 0 \Rightarrow r = 0, 1$; d) $r^2 - 2r + 1 = 0 \Rightarrow r = 1$ (doble) | ➖ |
| [Prob-10] | a) Caso 3 (raíces iguales); b) Caso 1 (diferencia entera no nula); c) Caso 1 (diferencia no entera) | ➖ |
| [Prob-11] | a) $y = x^{1/2}\sum_{n=0}^{\infty}\frac{(-1)^n x^n}{n!(2n+1)!!}$; b) $y = \sum_{n=0}^{\infty}\frac{x^n}{(n!)^2}$; c) $y = x J_1(x) = x\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+1}}{n!(n+1)!2^{2n+1}}$ | ➖ |
| [Prob-12] | a) $y_1 = x(1 - x + \frac{x^2}{2} - \cdots)$, $y_2 = x^2(1 - x + \cdots)$; b) $y = 1 + x + x^2 + \frac{2x^3}{3} + \cdots$ | ➖ |
| [Prob-13] | a) $y = x^{-1}\sin x = 1 - \frac{x^2}{6} + \frac{x^4}{120} - \cdots$; b) $y = x(1 + x + \frac{x^2}{2} + \cdots)$ | ➖ |
| [Prob-14] | a) Verificado: $J_0$ satisface la ecuación de Bessel con $\nu = 0$; b) Verificado: $P_2$ satisface Legendre con $n = 2$ | ➖ |
| [Prob-15] | a) $r^2 - \nu^2 = 0 \Rightarrow r = \pm\nu$; b) $J_0(x) = 1 - \frac{x^2}{4} + \frac{x^4}{64} - \frac{x^6}{2304} + \cdots$; c) $J_1(x) = \frac{x}{2} - \frac{x^3}{16} + \frac{x^5}{384} + \cdots$ | ➖ |
| [Prob-16] | a) Punto ordinario (coeficientes analíticos en $x=0$); b) $P_2(x) = \frac{1}{2}(3x^2 - 1)$; c) $\int_{-1}^{1} x \cdot \frac{1}{2}(3x^2-1)\,dx = 0$ ✓ | ➖ |
| [Prob-17] | a) Ordinario ($P(x)=1$, $Q(x)=-x$ analíticos); b) $\text{Ai}(x) = 1 + \frac{x^3}{6} + \frac{x^6}{180} + \cdots$; c) Coeficientes determinados por recurrencia | ➖ |
| [Prob-18] | a) $\psi = 1 - \frac{x^2}{2} + \frac{x^4}{8} - \cdots$; b) Verificación: $\psi'' = (x^2 - 1)e^{-x^2/2}$, satisface la ecuación | ➖ |
| [Prob-19] | a) Ecuación de Bessel con $\nu = 0$: $x^2T'' + xT' + \lambda^2 x^2 T = 0$; b) $T(r) = J_0(\lambda r)$ (acotada en $r=0$) | ➖ |
| [Prob-20] | a) Ecuación de Legendre con parámetro $n$; b) $P_3(x) = \frac{1}{2}(5x^3 - 3x)$ | ➖ |

---

## Fórmulas Clave

### Radio de Convergencia
$$R = \lim_{n\to\infty}\left|\frac{a_n}{a_{n+1}}\right| \quad\text{o}\quad R = \frac{1}{\limsup\sqrt[n]{|a_n|}}$$

### Punto Ordinario vs Singular
- **Ordinario:** $P(x)$ y $Q(x)$ analíticos en $x_0$
- **Singular Regular:** $\lim_{x\to x_0}(x-x_0)P(x)$ y $\lim_{x\to x_0}(x-x_0)^2 Q(x)$ finitos
- **Singular Irregular:** No es regular

### Método de Frobenius
$$y = \sum_{n=0}^{\infty}a_n x^{n+r}$$

### Ecuación Indicial
$$r(r-1) + p_0 r + q_0 = 0$$

### Funciones Especiales

| Ecuación | Forma | Soluciones |
|:---------|:------|:-----------|
| Bessel | $x^2y'' + xy' + (x^2 - \nu^2)y = 0$ | $J_\nu(x)$, $Y_\nu(x)$ |
| Legendre | $(1-x^2)y'' - 2xy' + n(n+1)y = 0$ | $P_n(x)$, $Q_n(x)$ |
| Airy | $y'' - xy = 0$ | $\text{Ai}(x)$, $\text{Bi}(x)$ |
| Hermite | $y'' - 2xy' + 2ny = 0$ | $H_n(x)$ |

### Primeros Polinomios de Legendre
$$P_0(x) = 1, \quad P_1(x) = x, \quad P_2(x) = \frac{3x^2-1}{2}, \quad P_3(x) = \frac{5x^3-3x}{2}$$

### Primeras Funciones de Bessel
$$J_0(x) = 1 - \frac{x^2}{4} + \frac{x^4}{64} - \cdots, \quad J_1(x) = \frac{x}{2} - \frac{x^3}{16} + \cdots$$

---

> 📚 **Archivo de problemas:** [problems/ED-05-Problemas.md](../problems/ED-05-Problemas.md)
