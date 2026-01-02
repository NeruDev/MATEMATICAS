<!--
HUMANO:
Soluciones de aplicaciones de la integral.

IA:
Desarrollo detallado de problemas representativos.

---
content_type: solutions
format: step_by_step
---
-->

# Soluciones de Aplicaciones de la Integral

---

## Problema 5
**Enunciado:** Área encerrada entre $y = x^2$ y $y = 2x + 3$.

**Solución:**
Intersecciones: $x^2 = 2x + 3 \Rightarrow x^2 - 2x - 3 = 0 \Rightarrow (x-3)(x+1) = 0$

$x = -1, 3$

En el intervalo, $2x + 3 \geq x^2$ (la recta está arriba).

$$A = \int_{-1}^{3} [(2x+3) - x^2]\,dx = \left[x^2 + 3x - \frac{x^3}{3}\right]_{-1}^{3}$$

$$= \left(9 + 9 - 9\right) - \left(1 - 3 + \frac{1}{3}\right) = 9 - \left(-\frac{5}{3}\right) = \frac{32}{3}$$

---

## Problema 8
**Enunciado:** Área entre $x = y^2$ y $x = y + 2$.

**Solución:**
Intersecciones: $y^2 = y + 2 \Rightarrow y^2 - y - 2 = 0 \Rightarrow (y-2)(y+1) = 0$

$y = -1, 2$

La recta $x = y + 2$ está a la derecha.

$$A = \int_{-1}^{2} [(y+2) - y^2]\,dy = \left[\frac{y^2}{2} + 2y - \frac{y^3}{3}\right]_{-1}^{2}$$

$$= \left(2 + 4 - \frac{8}{3}\right) - \left(\frac{1}{2} - 2 + \frac{1}{3}\right) = \frac{10}{3} - \left(-\frac{7}{6}\right) = \frac{27}{6} = \frac{9}{2}$$

---

## Problema 11
**Enunciado:** Volumen de una esfera de radio $r$.

**Solución:**
Rotamos el semicírculo $y = \sqrt{r^2 - x^2}$ alrededor del eje $x$.

$$V = \pi\int_{-r}^{r} (\sqrt{r^2 - x^2})^2\,dx = \pi\int_{-r}^{r} (r^2 - x^2)\,dx$$

$$= \pi\left[r^2 x - \frac{x^3}{3}\right]_{-r}^{r} = \pi\left[\left(r^3 - \frac{r^3}{3}\right) - \left(-r^3 + \frac{r^3}{3}\right)\right]$$

$$= \pi\left[\frac{2r^3}{3} + \frac{2r^3}{3}\right] = \frac{4\pi r^3}{3}$$

---

## Problema 17
**Enunciado:** Volumen al rotar $y = x^2$, $0 \leq x \leq 2$, alrededor del eje $y$ (capas cilíndricas).

**Solución:**
Usando capas cilíndricas:
- Radio: $x$
- Altura: $x^2$

$$V = 2\pi\int_0^2 x \cdot x^2\,dx = 2\pi\int_0^2 x^3\,dx = 2\pi\left[\frac{x^4}{4}\right]_0^2 = 2\pi \cdot 4 = 8\pi$$

---

## Problema 23
**Enunciado:** Longitud de $y = \frac{2}{3}x^{3/2}$ desde $x = 0$ hasta $x = 3$.

**Solución:**
$$\frac{dy}{dx} = \frac{2}{3} \cdot \frac{3}{2}x^{1/2} = x^{1/2}$$

$$1 + \left(\frac{dy}{dx}\right)^2 = 1 + x$$

$$L = \int_0^3 \sqrt{1 + x}\,dx = \frac{2}{3}(1+x)^{3/2}\Big|_0^3 = \frac{2}{3}(8 - 1) = \frac{14}{3}$$

---

## Problema 30
**Enunciado:** Superficie de una esfera de radio $r$.

**Solución:**
Rotamos $y = \sqrt{r^2 - x^2}$ alrededor del eje $x$.

$$\frac{dy}{dx} = \frac{-x}{\sqrt{r^2 - x^2}}$$

$$\sqrt{1 + \left(\frac{dy}{dx}\right)^2} = \sqrt{1 + \frac{x^2}{r^2 - x^2}} = \sqrt{\frac{r^2}{r^2 - x^2}} = \frac{r}{\sqrt{r^2 - x^2}}$$

$$S = 2\pi\int_{-r}^{r} \sqrt{r^2 - x^2} \cdot \frac{r}{\sqrt{r^2 - x^2}}\,dx = 2\pi r\int_{-r}^{r} dx = 2\pi r \cdot 2r = 4\pi r^2$$

---

## Problema 36
**Enunciado:** Tanque cilíndrico vertical de radio 2 m y altura 6 m lleno de agua. Trabajo para bombear toda el agua hasta el borde.

**Solución:**
Coordenada $y$ desde el fondo. Una rebanada a altura $y$:
- Volumen: $\pi(2)^2 \, dy = 4\pi\,dy$
- Peso: $\rho g \cdot 4\pi\,dy$ (con $\rho g \approx 9800$ N/m³)
- Distancia a elevar: $6 - y$

$$W = \int_0^6 9800 \cdot 4\pi (6 - y)\,dy = 39200\pi\left[6y - \frac{y^2}{2}\right]_0^6$$

$$= 39200\pi(36 - 18) = 39200\pi \cdot 18 = 705600\pi \approx 2.22 \times 10^6 \text{ J}$$

---

## Problema 37
**Enunciado:** Un resorte tiene longitud natural de 1 m. Una fuerza de 30 N lo estira a 1.2 m. Trabajo para estirarlo de 1.1 m a 1.5 m.

**Solución:**
De la ley de Hooke: $F = kx$ donde $x$ es el desplazamiento desde la posición natural.

$30 = k(0.2) \Rightarrow k = 150$ N/m

Para ir de 1.1 m a 1.5 m (desplazamientos 0.1 m a 0.5 m):

$$W = \int_{0.1}^{0.5} 150x\,dx = 150\left[\frac{x^2}{2}\right]_{0.1}^{0.5} = 75(0.25 - 0.01) = 18 \text{ J}$$

---

## Problema 42
**Enunciado:** [Valor promedio](../../../glossary.md#valor-promedio) de $f(x) = \sin x$ en $[0, \pi]$.

**Solución:**
$$f_{\text{prom}} = \frac{1}{\pi - 0}\int_0^{\pi} \sin x\,dx = \frac{1}{\pi}[-\cos x]_0^{\pi}$$

$$= \frac{1}{\pi}(-\cos\pi + \cos 0) = \frac{1}{\pi}(1 + 1) = \frac{2}{\pi}$$

---

## Problema 45
**Enunciado:** Velocidad $v(t) = 3t^2 + 2t$ m/s. Velocidad promedio en $[0, 4]$ s.

**Solución:**
$$v_{\text{prom}} = \frac{1}{4-0}\int_0^4 (3t^2 + 2t)\,dt = \frac{1}{4}\left[t^3 + t^2\right]_0^4$$

$$= \frac{1}{4}(64 + 16) = \frac{80}{4} = 20 \text{ m/s}$$
