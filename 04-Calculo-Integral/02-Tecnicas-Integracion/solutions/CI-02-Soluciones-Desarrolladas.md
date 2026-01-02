<!--
HUMANO:
Soluciones de [técnicas de integración](../../../glossary.md#tecnicas-de-integracion).

IA:
Soluciones representativas con desarrollo completo.

---
content_type: solutions
expected_output:
  default: detailed steps
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Soluciones de Técnicas de Integración

---

## Problema 6 (Sustitución)
$$\int \frac{\ln x}{x} \, dx$$

**Desarrollo:**
Sea $u = \ln x$, entonces $du = \frac{1}{x} dx$

$$= \int u \, du = \frac{u^2}{2} + C = \frac{(\ln x)^2}{2} + C$$

---

## Problema 17 (Partes)
$$\int \ln x \, dx$$

**Desarrollo:**
$u = \ln x$, $dv = dx$
$du = \frac{1}{x} dx$, $v = x$

$$= x \ln x - \int x \cdot \frac{1}{x} dx = x \ln x - \int dx = x \ln x - x + C$$

---

## Problema 20 (Partes cíclicas)
$$\int e^x \cos x \, dx$$

**Desarrollo:**
Primera aplicación: $u = \cos x$, $dv = e^x dx$

$$I = e^x \cos x + \int e^x \sin x \, dx$$

Segunda aplicación: $u = \sin x$, $dv = e^x dx$

$$I = e^x \cos x + e^x \sin x - \int e^x \cos x \, dx$$
$$I = e^x(\cos x + \sin x) - I$$
$$2I = e^x(\cos x + \sin x)$$

$$\boxed{I = \frac{e^x(\cos x + \sin x)}{2} + C}$$

---

## Problema 27 (Trigonométrica)
$$\int \sin^3 x \, dx$$

**Desarrollo:**
Separamos un factor $\sin x$:
$$= \int \sin^2 x \cdot \sin x \, dx = \int (1 - \cos^2 x) \sin x \, dx$$

$u = \cos x$, $du = -\sin x \, dx$

$$= -\int (1 - u^2) du = -u + \frac{u^3}{3} + C = -\cos x + \frac{\cos^3 x}{3} + C$$

---

## Problema 42 (Sustitución trigonométrica)
$$\int \sqrt{4-x^2} \, dx$$

**Desarrollo:**
$x = 2\sin\theta$, $dx = 2\cos\theta \, d\theta$
$\sqrt{4-x^2} = 2\cos\theta$

$$= \int 4\cos^2\theta \, d\theta = 4 \cdot \frac{1}{2}\int (1 + \cos 2\theta) d\theta$$

$$= 2\left(\theta + \frac{\sin 2\theta}{2}\right) + C = 2\theta + \sin 2\theta + C$$

Regresando: $\theta = \arcsin\frac{x}{2}$, $\sin 2\theta = 2\sin\theta\cos\theta = 2 \cdot \frac{x}{2} \cdot \frac{\sqrt{4-x^2}}{2} = \frac{x\sqrt{4-x^2}}{2}$

$$= 2\arcsin\frac{x}{2} + \frac{x\sqrt{4-x^2}}{2} + C$$

---

## Problema 49 (Fracciones parciales)
$$\int \frac{1}{x^2-1} \, dx$$

**Desarrollo:**
$$\frac{1}{x^2-1} = \frac{1}{(x-1)(x+1)} = \frac{A}{x-1} + \frac{B}{x+1}$$

$1 = A(x+1) + B(x-1)$

$x = 1$: $1 = 2A \Rightarrow A = \frac{1}{2}$
$x = -1$: $1 = -2B \Rightarrow B = -\frac{1}{2}$

$$= \int \left(\frac{1/2}{x-1} - \frac{1/2}{x+1}\right) dx = \frac{1}{2}\ln\lvert x-1\rvert - \frac{1}{2}\ln\lvert x+1\rvert + C$$

$$= \frac{1}{2}\ln\left\lvert\frac{x-1}{x+1}\right\rvert + C$$

---

## Problema 54 (Factor repetido)
$$\int \frac{1}{x(x-1)^2} \, dx$$

**Desarrollo:**
$$\frac{1}{x(x-1)^2} = \frac{A}{x} + \frac{B}{x-1} + \frac{C}{(x-1)^2}$$

$1 = A(x-1)^2 + Bx(x-1) + Cx$

$x = 0$: $1 = A$
$x = 1$: $1 = C$
Coeficiente de $x^2$: $0 = A + B \Rightarrow B = -1$

$$= \int \left(\frac{1}{x} - \frac{1}{x-1} + \frac{1}{(x-1)^2}\right) dx$$

$$= \ln\lvert x\rvert - \ln\lvert x-1\rvert - \frac{1}{x-1} + C$$

---

## Problema 60 (Completar cuadrado)
$$\int \frac{dx}{x^2+4x+5}$$

**Desarrollo:**
Completamos: $x^2 + 4x + 5 = (x+2)^2 + 1$

$$= \int \frac{dx}{(x+2)^2 + 1}$$

$u = x + 2$, $du = dx$

$$= \int \frac{du}{u^2 + 1} = \arctan u + C = \arctan(x+2) + C$$

---

## Problema 62 (Numerador lineal + cuadrático)
$$\int \frac{x+1}{x^2+2x+5} \, dx$$

**Desarrollo:**
Completamos: $x^2 + 2x + 5 = (x+1)^2 + 4$

El numerador es exactamente la [derivada](../../../glossary.md#derivada) del interior del cuadrado (casi):

$$\frac{d}{dx}(x^2+2x+5) = 2x + 2 = 2(x+1)$$

Por tanto:
$$= \frac{1}{2}\int \frac{2(x+1)}{(x+1)^2 + 4} dx = \frac{1}{2}\ln[(x+1)^2 + 4] + C$$

$$= \frac{1}{2}\ln(x^2+2x+5) + C$$
