<!--
::METADATA::
type: cheatsheet
topic_id: ci-01-integral-indefinida
file_id: CI-01-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->

# Resumen rápido — Integral Indefinida

## Definición fundamental

$$\int f(x)\,dx = F(x) + C \quad \text{donde} \quad F'(x) = f(x)$$

## Propiedades básicas

| Propiedad | Fórmula |
|-----------|---------|
| Constante | $\int k\,dx = kx + C$ |
| [Linealidad](../../glossary.md#linealidad) | $\int kf(x)\,dx = k\int f(x)\,dx$ |
| Suma | $\int [f(x) \pm g(x)]\,dx = \int f(x)\,dx \pm \int g(x)\,dx$ |

## Tabla de integrales básicas

### Funciones algebraicas

| [Función](../../glossary.md#función) | Integral |
|---------|----------|
| $x^n$ $(n \neq -1)$ | $\dfrac{x^{n+1}}{n+1} + C$ |
| $\dfrac{1}{x}$ | $\ln\|x\| + C$ |
| $\dfrac{1}{\sqrt{x}}$ | $2\sqrt{x} + C$ |

### Funciones exponenciales y logarítmicas

| Función | Integral |
|---------|----------|
| $e^x$ | $e^x + C$ |
| $a^x$ | $\dfrac{a^x}{\ln a} + C$ |
| $e^{kx}$ | $\dfrac{e^{kx}}{k} + C$ |

### Funciones trigonométricas

| Función | Integral |
|---------|----------|
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |
| $\sec^2 x$ | $\tan x + C$ |
| $\csc^2 x$ | $-\cot x + C$ |
| $\sec x \tan x$ | $\sec x + C$ |
| $\csc x \cot x$ | $-\csc x + C$ |
| $\tan x$ | $-\ln\|\cos x\| + C = \ln\|\sec x\| + C$ |
| $\cot x$ | $\ln\|\sin x\| + C$ |
| $\sec x$ | $\ln\|\sec x + \tan x\| + C$ |
| $\csc x$ | $-\ln\|\csc x + \cot x\| + C$ |

### Integrales que producen funciones inversas

| Función | Integral |
|---------|----------|
| $\dfrac{1}{\sqrt{1-x^2}}$ | $\arcsin x + C$ |
| $\dfrac{1}{1+x^2}$ | $\arctan x + C$ |
| $\dfrac{1}{x\sqrt{x^2-1}}$ | $\text{arcsec}\|x\| + C$ |
| $\dfrac{1}{\sqrt{a^2-x^2}}$ | $\arcsin\dfrac{x}{a} + C$ |
| $\dfrac{1}{a^2+x^2}$ | $\dfrac{1}{a}\arctan\dfrac{x}{a} + C$ |
| $\dfrac{1}{x\sqrt{x^2-a^2}}$ | $\dfrac{1}{a}\text{arcsec}\dfrac{\|x\|}{a} + C$ |

### Funciones hiperbólicas

| Función | Integral |
|---------|----------|
| $\sinh x$ | $\cosh x + C$ |
| $\cosh x$ | $\sinh x + C$ |
| $\text{sech}^2 x$ | $\tanh x + C$ |
| $\text{csch}^2 x$ | $-\coth x + C$ |

## Fórmula de potencia generalizada

$$\int [f(x)]^n \cdot f'(x)\,dx = \frac{[f(x)]^{n+1}}{n+1} + C \quad (n \neq -1)$$

$$\int \frac{f'(x)}{f(x)}\,dx = \ln|f(x)| + C$$

## Verificación de resultados

**Regla de oro:** Derivar la respuesta siempre debe dar el integrando original.

$$\frac{d}{dx}\left[\int f(x)\,dx\right] = f(x)$$

---

<!--
IA: Hoja de referencia rápida para [integral indefinida](../../glossary.md#integral-indefinida).
Para desarrollo completo: theory/CI-01-Teoria-Integral-Indefinida.md
file_id: CI-01-Resumen-Formulas
-->
