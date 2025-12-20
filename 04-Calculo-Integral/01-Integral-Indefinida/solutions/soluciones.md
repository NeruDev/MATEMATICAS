<!--
HUMANO:
Soluciones de integral indefinida.

IA:
Soluciones representativas con desarrollo.

---
content_type: solutions
expected_output:
  default: detailed steps
---
-->

# Soluciones de Integral Indefinida

---

## Problema 6
$$\int \sqrt{x} \, dx$$

**Desarrollo:**
Reescribimos como potencia:
$$\int x^{1/2} \, dx$$

Aplicamos regla de potencia con $n = 1/2$:
$$= \frac{x^{1/2+1}}{1/2+1} + C = \frac{x^{3/2}}{3/2} + C = \frac{2x^{3/2}}{3} + C$$

**Verificación:** $\frac{d}{dx}\left(\frac{2x^{3/2}}{3}\right) = \frac{2 \cdot \frac{3}{2}x^{1/2}}{3} = x^{1/2} = \sqrt{x}$ ✓

---

## Problema 10
$$\int \frac{x^2 - 1}{x} \, dx$$

**Desarrollo:**
Separamos la fracción:
$$= \int \left(\frac{x^2}{x} - \frac{1}{x}\right) dx = \int \left(x - \frac{1}{x}\right) dx$$

Integramos término a término:
$$= \frac{x^2}{2} - \ln\lvert x \rvert + C$$

---

## Problema 14
$$\int \left(\sqrt{x} + \frac{1}{\sqrt{x}}\right)^2 \, dx$$

**Desarrollo:**
Expandimos el cuadrado:
$$\left(\sqrt{x} + \frac{1}{\sqrt{x}}\right)^2 = x + 2 + \frac{1}{x}$$

Integramos:
$$\int \left(x + 2 + \frac{1}{x}\right) dx = \frac{x^2}{2} + 2x + \ln\lvert x \rvert + C$$

---

## Problema 23
$$\int \frac{e^{2x} - 1}{e^x} \, dx$$

**Desarrollo:**
Separamos:
$$= \int \left(\frac{e^{2x}}{e^x} - \frac{1}{e^x}\right) dx = \int (e^x - e^{-x}) \, dx$$

Integramos:
$$= e^x - (-e^{-x}) + C = e^x + e^{-x} + C$$

---

## Problema 41
$$\int (\sin^2 x + \cos^2 x) \, dx$$

**Desarrollo:**
Por identidad pitagórica: $\sin^2 x + \cos^2 x = 1$

$$\int 1 \, dx = x + C$$

---

## Problema 48
$$\int \frac{1}{9+x^2} \, dx$$

**Desarrollo:**
Identificamos la forma $\frac{1}{a^2 + x^2}$ con $a = 3$:

$$\int \frac{1}{a^2+x^2} \, dx = \frac{1}{a}\arctan\frac{x}{a} + C$$

Sustituyendo $a = 3$:
$$= \frac{1}{3}\arctan\frac{x}{3} + C$$

---

## Problema 51
$$\int \frac{1}{\sqrt{1-4x^2}} \, dx$$

**Desarrollo:**
Reescribimos: $1 - 4x^2 = 1 - (2x)^2$

Sea $u = 2x$, entonces $du = 2dx$, por lo que $dx = \frac{du}{2}$.

$$= \int \frac{1}{\sqrt{1-u^2}} \cdot \frac{du}{2} = \frac{1}{2}\arcsin u + C = \frac{1}{2}\arcsin(2x) + C$$

---

## Problema 58
$$\int \left(e^x + \sec^2 x + \frac{1}{\sqrt{1-x^2}}\right) \, dx$$

**Desarrollo:**
Integramos cada término:
- $\int e^x \, dx = e^x$
- $\int \sec^2 x \, dx = \tan x$
- $\int \frac{1}{\sqrt{1-x^2}} \, dx = \arcsin x$

Resultado:
$$= e^x + \tan x + \arcsin x + C$$

---

## Problema 60
$$\int \left(\frac{1}{x} + \frac{1}{1+x^2} + \frac{1}{\sqrt{1-x^2}}\right) \, dx$$

**Desarrollo:**
Cada término corresponde a una fórmula básica:
- $\int \frac{1}{x} \, dx = \ln\lvert x \rvert$
- $\int \frac{1}{1+x^2} \, dx = \arctan x$
- $\int \frac{1}{\sqrt{1-x^2}} \, dx = \arcsin x$

Resultado:
$$= \ln\lvert x \rvert + \arctan x + \arcsin x + C$$
