<!--
::METADATA::
type: cheatsheet
topic_id: ed-05-series-potencias
file_id: ED-05-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->

# Resumen rápido — Series de Potencias en EDO

## Serie de Potencias

$$y = \sum_{n=0}^{\infty} a_n (x - x_0)^n$$

**Radio de convergencia:** $R = \frac{1}{\limsup_{n\to\infty} |a_n|^{1/n}}$ o por cociente.

---

## Clasificación de Puntos Singulares

Para $y'' + P(x)y' + Q(x)y = 0$:

| Tipo | Condición en $x_0$ |
|------|-------------------|
| Ordinario | $P(x)$ y $Q(x)$ analíticas |
| Singular regular | $(x-x_0)P(x)$ y $(x-x_0)^2Q(x)$ analíticas |
| Singular irregular | No cumple lo anterior |

---

## Solución en Punto Ordinario

1. Proponer $y = \sum_{n=0}^{\infty} a_n x^n$
2. Calcular $y' = \sum_{n=1}^{\infty} n a_n x^{n-1}$
3. Calcular $y'' = \sum_{n=2}^{\infty} n(n-1) a_n x^{n-2}$
4. Sustituir en la [EDO](../../glossary.md#edo)
5. Igualar coeficientes de potencias iguales
6. Obtener **relación de recurrencia** para $a_n$

---

## Método de Frobenius

Para punto singular regular $x_0 = 0$:

$$y = x^r \sum_{n=0}^{\infty} a_n x^n = \sum_{n=0}^{\infty} a_n x^{n+r}$$

### Ecuación indicial

De $a_0 \neq 0$, el término de [menor](../../glossary.md#menor) potencia da:

$$r(r-1) + p_0 r + q_0 = 0$$

donde $p_0 = \lim_{x\to 0} xP(x)$ y $q_0 = \lim_{x\to 0} x^2Q(x)$

---

## Casos según Raíces de Ecuación Indicial

Sean $r_1 \geq r_2$ las raíces.

### Caso 1: $r_1 - r_2 \notin \mathbb{Z}$

Dos soluciones independientes de Frobenius:
$$y_1 = x^{r_1}\sum a_n x^n, \quad y_2 = x^{r_2}\sum b_n x^n$$

### Caso 2: $r_1 = r_2 = r$

$$y_1 = x^r \sum a_n x^n$$
$$y_2 = y_1 \ln x + x^r \sum b_n x^n$$

### Caso 3: $r_1 - r_2 = N$ (entero positivo)

$$y_1 = x^{r_1}\sum a_n x^n$$
$$y_2 = Cy_1 \ln x + x^{r_2}\sum b_n x^n$$

donde $C$ puede ser $0$.

---

## Ecuación de Bessel

$$x^2 y'' + xy' + (x^2 - \nu^2)y = 0$$

### Soluciones

| [Orden](../../glossary.md#orden) $\nu$ | Soluciones |
|-------------|------------|
| $\nu \notin \mathbb{Z}$ | $y = C_1 J_\nu(x) + C_2 J_{-\nu}(x)$ |
| $\nu = n \in \mathbb{Z}$ | $y = C_1 J_n(x) + C_2 Y_n(x)$ |

### Función de Bessel de primera especie
$$J_\nu(x) = \sum_{k=0}^{\infty} \frac{(-1)^k}{k!\,\Gamma(\nu+k+1)}\left(\frac{x}{2}\right)^{2k+\nu}$$

### Casos particulares
$$J_0(x) = 1 - \frac{x^2}{4} + \frac{x^4}{64} - \cdots$$

---

## Ecuación de Legendre

$$(1-x^2)y'' - 2xy' + n(n+1)y = 0$$

### Polinomios de Legendre

$$P_n(x) = \frac{1}{2^n n!}\frac{d^n}{dx^n}(x^2-1)^n$$

### Primeros polinomios
| $n$ | $P_n(x)$ |
|-----|----------|
| 0 | 1 |
| 1 | $x$ |
| 2 | $\frac{1}{2}(3x^2-1)$ |
| 3 | $\frac{1}{2}(5x^3-3x)$ |
| 4 | $\frac{1}{8}(35x^4-30x^2+3)$ |

### Ortogonalidad
$$\int_{-1}^{1} P_m(x)P_n(x)\,dx = \frac{2}{2n+1}\delta_{mn}$$

---

## Ecuación de Hermite

$$y'' - 2xy' + 2ny = 0$$

### Polinomios de Hermite
$$H_n(x) = (-1)^n e^{x^2} \frac{d^n}{dx^n}e^{-x^2}$$

### Primeros polinomios
| $n$ | $H_n(x)$ |
|-----|----------|
| 0 | 1 |
| 1 | $2x$ |
| 2 | $4x^2 - 2$ |
| 3 | $8x^3 - 12x$ |

---

## Ecuación de Laguerre

$$xy'' + (1-x)y' + ny = 0$$

### Polinomios de Laguerre
$$L_n(x) = \frac{e^x}{n!}\frac{d^n}{dx^n}(x^n e^{-x})$$

---

## Operaciones con Series

### Derivada
$$\frac{d}{dx}\sum a_n x^n = \sum n a_n x^{n-1}$$

### Re-indexación
$$\sum_{n=2}^{\infty} n(n-1)a_n x^{n-2} = \sum_{k=0}^{\infty}(k+2)(k+1)a_{k+2}x^k$$

### Producto de Cauchy
$$\left(\sum a_n x^n\right)\left(\sum b_n x^n\right) = \sum_{n=0}^{\infty}\left(\sum_{k=0}^{n}a_k b_{n-k}\right)x^n$$

---

<!--
IA: Hoja de referencia rápida para Series de Potencias en EDO.
Para desarrollo completo: theory/ED-05-Teoria-Series-EDO.md
file_id: ED-05-Resumen-Formulas
-->
