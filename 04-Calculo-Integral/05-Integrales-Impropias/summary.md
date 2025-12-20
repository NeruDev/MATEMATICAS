<!--
HUMANO:
Resumen de integrales impropias.

IA:
Definiciones y criterios principales.

---
content_type: summary
format: formula_sheet
---
-->

# Resumen: Integrales Impropias

---

## Tipo I: Límites Infinitos

$$\int_a^{\infty} f(x)\,dx = \lim_{t \to \infty} \int_a^t f(x)\,dx$$

$$\int_{-\infty}^{b} f(x)\,dx = \lim_{t \to -\infty} \int_t^b f(x)\,dx$$

$$\int_{-\infty}^{\infty} f(x)\,dx = \int_{-\infty}^{c} f(x)\,dx + \int_c^{\infty} f(x)\,dx$$

---

## Tipo II: Discontinuidades

Si $f$ tiene discontinuidad en $a$:
$$\int_a^b f(x)\,dx = \lim_{t \to a^+} \int_t^b f(x)\,dx$$

Si $f$ tiene discontinuidad en $b$:
$$\int_a^b f(x)\,dx = \lim_{t \to b^-} \int_a^t f(x)\,dx$$

---

## Integrales p

$$\int_1^{\infty} \frac{1}{x^p}\,dx \begin{cases} \text{converge} & \text{si } p > 1 \\ \text{diverge} & \text{si } p \leq 1 \end{cases}$$

$$\int_0^{1} \frac{1}{x^p}\,dx \begin{cases} \text{converge} & \text{si } p < 1 \\ \text{diverge} & \text{si } p \geq 1 \end{cases}$$

---

## Criterio de Comparación Directa

Si $0 \leq f(x) \leq g(x)$ para $x \geq a$:
- $\int_a^{\infty} g(x)\,dx$ converge $\Rightarrow$ $\int_a^{\infty} f(x)\,dx$ converge
- $\int_a^{\infty} f(x)\,dx$ diverge $\Rightarrow$ $\int_a^{\infty} g(x)\,dx$ diverge

---

## Criterio de Comparación por Límite

Si $\displaystyle\lim_{x \to \infty} \frac{f(x)}{g(x)} = L$ con $0 < L < \infty$:

Ambas integrales convergen o ambas divergen.

---

## Integrales Clásicas Convergentes

| Integral | Valor |
|----------|-------|
| $\int_0^{\infty} e^{-x}\,dx$ | $1$ |
| $\int_0^{\infty} e^{-x^2}\,dx$ | $\frac{\sqrt{\pi}}{2}$ |
| $\int_0^{\infty} \frac{\sin x}{x}\,dx$ | $\frac{\pi}{2}$ |
