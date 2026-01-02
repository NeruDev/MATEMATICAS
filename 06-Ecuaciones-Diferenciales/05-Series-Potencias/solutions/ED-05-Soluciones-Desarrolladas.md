<!--
::METADATA::
type: solution
status: active
-->

# Soluciones: Series de Potencias para EDO

*Soluciones seleccionadas que ilustran los métodos principales.*

---

## Solución Problema 1 (Radio de convergencia)

**a)** $\sum_{n=0}^{\infty} \frac{x^n}{n!}$

Usando el criterio del cociente:
$$\lim_{n\to\infty} \left|\frac{a_{n+1}}{a_n}\right| = \lim_{n\to\infty} \frac{|x|^{n+1}/(n+1)!}{|x|^n/n!} = \lim_{n\to\infty} \frac{|x|}{n+1} = 0$$

Como el [límite](../../../glossary.md#límite) es $0 < 1$ para todo $x$, el **radio de [convergencia](../../../glossary.md#convergencia) es $R = \infty$**.

**b)** $\sum_{n=0}^{\infty} n! x^n$

$$\lim_{n\to\infty} \left|\frac{(n+1)! x^{n+1}}{n! x^n}\right| = \lim_{n\to\infty} (n+1)|x| = \infty$$ para $x \neq 0$

**Radio de convergencia: $R = 0$** (solo converge en $x = 0$)

**c)** $\sum_{n=1}^{\infty} \frac{x^n}{n}$

$$\lim_{n\to\infty} \left|\frac{x^{n+1}/(n+1)}{x^n/n}\right| = \lim_{n\to\infty} \frac{n}{n+1}|x| = |x|$$

Converge si $|x| < 1$. **Radio de convergencia: $R = 1$**

**d)** $\sum_{n=0}^{\infty} \frac{(x-2)^n}{3^n}$

Esta es una serie geométrica con razón $\frac{x-2}{3}$.

Converge si $\left|\frac{x-2}{3}\right| < 1$, es decir, $|x-2| < 3$.

**Radio de convergencia: $R = 3$** (centrada en $x = 2$)

---

## Solución Problema 4a (Punto ordinario)

**Resolver:** $y'' + y = 0$

**Paso 1:** Proponer $y = \sum_{n=0}^{\infty} a_n x^n$

$$y' = \sum_{n=1}^{\infty} n a_n x^{n-1}$$
$$y'' = \sum_{n=2}^{\infty} n(n-1) a_n x^{n-2}$$

**Paso 2:** Sustituir:
$$\sum_{n=2}^{\infty} n(n-1) a_n x^{n-2} + \sum_{n=0}^{\infty} a_n x^n = 0$$

**Paso 3:** Reindexar la primera suma ($m = n-2$, $n = m+2$):
$$\sum_{m=0}^{\infty} (m+2)(m+1) a_{m+2} x^m + \sum_{n=0}^{\infty} a_n x^n = 0$$

**Paso 4:** Combinar:
$$\sum_{n=0}^{\infty} [(n+2)(n+1) a_{n+2} + a_n] x^n = 0$$

**Paso 5:** Relación de recurrencia:
$$a_{n+2} = -\frac{a_n}{(n+2)(n+1)}$$

**Paso 6:** Calcular coeficientes:

Para $n$ par ($a_0$ arbitrario):
- $a_2 = -\frac{a_0}{2!}$
- $a_4 = -\frac{a_2}{4 \cdot 3} = \frac{a_0}{4!}$
- $a_6 = -\frac{a_4}{6 \cdot 5} = -\frac{a_0}{6!}$

Para $n$ impar ($a_1$ arbitrario):
- $a_3 = -\frac{a_1}{3!}$
- $a_5 = \frac{a_1}{5!}$
- $a_7 = -\frac{a_1}{7!}$

**Solución:**
$$\boxed{y = a_0\left(1 - \frac{x^2}{2!} + \frac{x^4}{4!} - ...\right) + a_1\left(x - \frac{x^3}{3!} + \frac{x^5}{5!} - ...\right) = a_0\cos x + a_1\sin x}$$

---

## Solución Problema 5a (Ecuación de Airy)

**Resolver:** $y'' - xy = 0$ hasta $x^5$

**Paso 1:** Proponer $y = \sum_{n=0}^{\infty} a_n x^n$

$$y'' = \sum_{n=2}^{\infty} n(n-1)a_n x^{n-2}$$
$$xy = \sum_{n=0}^{\infty} a_n x^{n+1}$$

**Paso 2:** Reindexar:
- Primera suma: $m = n-2 \Rightarrow \sum_{m=0}^{\infty} (m+2)(m+1)a_{m+2}x^m$
- Segunda suma: $m = n+1 \Rightarrow \sum_{m=1}^{\infty} a_{m-1}x^m$

**Paso 3:** Ecuación combinada:
$$2a_2 + \sum_{n=1}^{\infty} [(n+2)(n+1)a_{n+2} - a_{n-1}]x^n = 0$$

**Paso 4:** De los coeficientes:
- $x^0$: $2a_2 = 0 \Rightarrow a_2 = 0$
- $x^n$ ($n \geq 1$): $a_{n+2} = \frac{a_{n-1}}{(n+2)(n+1)}$

**Paso 5:** Calcular:

Comenzando con $a_0$:
- $a_3 = \frac{a_0}{3 \cdot 2} = \frac{a_0}{6}$
- $a_6 = \frac{a_3}{6 \cdot 5} = \frac{a_0}{180}$

Comenzando con $a_1$:
- $a_4 = \frac{a_1}{4 \cdot 3} = \frac{a_1}{12}$

**Solución hasta $x^6$:**
$$\boxed{y = a_0\left(1 + \frac{x^3}{6} + \frac{x^6}{180} + ...\right) + a_1\left(x + \frac{x^4}{12} + ...\right)}$$

---

## Solución Problema 9a (Ecuación indicial)

**Para:** $2xy'' + y' - y = 0$

**Paso 1:** Forma estándar $y'' + P(x)y' + Q(x)y = 0$:
$$y'' + \frac{1}{2x}y' - \frac{1}{2x}y = 0$$

$$P(x) = \frac{1}{2x}, \quad Q(x) = -\frac{1}{2x}$$

**Paso 2:** Calcular [límites](../../../glossary.md#límites):
$$p_0 = \lim_{x \to 0} xP(x) = \lim_{x \to 0} x \cdot \frac{1}{2x} = \frac{1}{2}$$
$$q_0 = \lim_{x \to 0} x^2 Q(x) = \lim_{x \to 0} x^2 \cdot \left(-\frac{1}{2x}\right) = 0$$

**Paso 3:** Ecuación indicial:
$$r(r-1) + p_0 r + q_0 = 0$$
$$r(r-1) + \frac{1}{2}r = 0$$
$$r^2 - r + \frac{1}{2}r = 0$$
$$r^2 - \frac{1}{2}r = 0$$
$$r\left(r - \frac{1}{2}\right) = 0$$

**Raíces:** $\boxed{r_1 = \frac{1}{2}, \quad r_2 = 0}$

Diferencia: $r_1 - r_2 = \frac{1}{2}$ (no entero) → **Caso 1 de Frobenius**

---

## Solución Problema 11a (Método de Frobenius)

**Resolver:** $2xy'' + y' + y = 0$

**Paso 1:** Verificar singularidad regular en $x = 0$:
- $P(x) = \frac{1}{2x}$, $Q(x) = \frac{1}{2x}$
- $xP(x) = \frac{1}{2}$ (analítico)
- $x^2Q(x) = \frac{x}{2}$ (analítico)
- $\checkmark$ Singular regular

**Paso 2:** Ecuación indicial:
$$r(r-1) + \frac{1}{2}r + 0 = 0$$
$$r^2 - \frac{r}{2} = 0 \Rightarrow r = 0, \frac{1}{2}$$

**Paso 3:** Para $r = \frac{1}{2}$, proponer $y = x^{1/2}\sum_{n=0}^{\infty} a_n x^n$:

$$y = \sum_{n=0}^{\infty} a_n x^{n+1/2}$$
$$y' = \sum_{n=0}^{\infty} \left(n+\frac{1}{2}\right) a_n x^{n-1/2}$$
$$y'' = \sum_{n=0}^{\infty} \left(n+\frac{1}{2}\right)\left(n-\frac{1}{2}\right) a_n x^{n-3/2}$$

**Paso 4:** Sustituir en $2xy'' + y' + y = 0$:
$$2\sum_{n=0}^{\infty} \left(n+\frac{1}{2}\right)\left(n-\frac{1}{2}\right) a_n x^{n-1/2} + \sum_{n=0}^{\infty} \left(n+\frac{1}{2}\right) a_n x^{n-1/2} + \sum_{n=0}^{\infty} a_n x^{n+1/2} = 0$$

**Paso 5:** Reindexar el último término y combinar:

Coeficiente de $x^{n-1/2}$:
$$2\left(n+\frac{1}{2}\right)\left(n-\frac{1}{2}\right)a_n + \left(n+\frac{1}{2}\right)a_n + a_{n-1} = 0$$

$$a_n(2n^2 + n) + a_{n-1} = 0$$

$$a_n = -\frac{a_{n-1}}{n(2n+1)}$$

**Paso 6:** Calcular coeficientes ($a_0 = 1$):
- $a_1 = -\frac{1}{1 \cdot 3} = -\frac{1}{3}$
- $a_2 = -\frac{a_1}{2 \cdot 5} = \frac{1}{30}$
- $a_3 = -\frac{a_2}{3 \cdot 7} = -\frac{1}{630}$

**Primera solución:**
$$\boxed{y_1 = x^{1/2}\left(1 - \frac{x}{3} + \frac{x^2}{30} - \frac{x^3}{630} + ...\right)}$$

---

## Solución Problema 15b (Bessel $J_0$)

**Ecuación de Bessel con $\nu = 0$:** $x^2y'' + xy' + x^2y = 0$

La ecuación indicial da $r = 0$ (raíz doble).

**Paso 1:** Proponer $y = \sum_{n=0}^{\infty} a_n x^n$

**Paso 2:** Sustituir en la ecuación:
$$\sum_{n=2}^{\infty} n(n-1)a_n x^n + \sum_{n=1}^{\infty} na_n x^n + \sum_{n=0}^{\infty} a_n x^{n+2} = 0$$

**Paso 3:** Reindexar y combinar:

- $n = 0$: $0 = 0$ ✓
- $n = 1$: $a_1 = 0$
- $n \geq 2$: $n^2 a_n + a_{n-2} = 0$

**Paso 4:** Relación de recurrencia:
$$a_n = -\frac{a_{n-2}}{n^2}$$

Como $a_1 = 0$, todos los coeficientes impares son cero.

**Paso 5:** Coeficientes pares ($a_0 = 1$):
- $a_2 = -\frac{1}{4}$
- $a_4 = -\frac{a_2}{16} = \frac{1}{64}$
- $a_6 = -\frac{a_4}{36} = -\frac{1}{2304}$

**[Función](../../../glossary.md#función) de Bessel $J_0$:**
$$\boxed{J_0(x) = 1 - \frac{x^2}{4} + \frac{x^4}{64} - \frac{x^6}{2304} + ... = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{2^{2n}(n!)^2}}$$

---

## Solución Problema 16b (Legendre $P_2$)

**Ecuación de Legendre con $n = 2$:**
$$(1-x^2)y'' - 2xy' + 6y = 0$$

**Paso 1:** Proponer $y = \sum_{k=0}^{\infty} a_k x^k$ y sustituir.

**Paso 2:** Relación de recurrencia:
$$a_{k+2} = \frac{k(k+1) - 6}{(k+2)(k+1)} a_k = \frac{(k-2)(k+3)}{(k+2)(k+1)} a_k$$

**Paso 3:** Serie par ($a_0 = 1$, $a_1 = 0$):
- $a_2 = \frac{(0-2)(0+3)}{(2)(1)} a_0 = \frac{-6}{2} = -3$
- $a_4 = \frac{(2-2)(2+3)}{(4)(3)} a_2 = 0$

Como $a_4 = 0$, la serie termina.

$$y_1 = 1 - 3x^2$$

**Paso 4:** Normalización: $P_n(1) = 1$

$$y_1(1) = 1 - 3 = -2$$

$$P_2(x) = \frac{y_1}{-2} = \frac{3x^2 - 1}{2}$$

$$\boxed{P_2(x) = \frac{1}{2}(3x^2 - 1)}$$

---

## Solución Problema 17 (Ecuación de Airy - Aplicación)

**Ecuación:** $y'' - xy = 0$, con $y(0) = 1$, $y'(0) = 0$

De la solución del Problema 5a:
$$y = a_0\left(1 + \frac{x^3}{6} + \frac{x^6}{180} + ...\right) + a_1\left(x + \frac{x^4}{12} + ...\right)$$

**Aplicando condiciones iniciales:**
- $y(0) = a_0 = 1$
- $y'(0) = a_1 = 0$

**Función de Airy $\text{Ai}(x)$:**
$$\boxed{\text{Ai}(x) = c\left(1 + \frac{x^3}{6} + \frac{x^6}{180} + \frac{x^9}{12960} + ...\right)}$$

donde $c = 3^{-2/3}/\Gamma(2/3) \approx 0.355$ es la constante de normalización.

**Patrón general:**
$$\text{Ai}(x) = c \sum_{n=0}^{\infty} \frac{x^{3n}}{3^{2n}(3n)!/n!}$$
