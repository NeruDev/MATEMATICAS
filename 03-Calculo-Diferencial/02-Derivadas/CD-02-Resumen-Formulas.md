<!--
::METADATA::
type: cheatsheet
topic_id: cd-02-[derivadas](../../glossary.md#derivadas)
file_id: CD-02-Resumen-Formulas
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

---

# Resumen de Fórmulas: Derivadas

## Definición de Derivada

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

## Reglas Básicas de Derivación

| Regla | [Función](../../glossary.md#funcion) | [Derivada](../../glossary.md#derivada) |
|-------|---------|----------|
| Constante | $c$ | $0$ |
| Potencia | $x^n$ | $nx^{n-1}$ |
| Múltiplo | $cf(x)$ | $cf'(x)$ |
| Suma | $f(x) + g(x)$ | $f'(x) + g'(x)$ |
| Producto | $f(x) \cdot g(x)$ | $f'(x)g(x) + f(x)g'(x)$ |
| Cociente | $\frac{f(x)}{g(x)}$ | $\frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$ |
| Cadena | $f(g(x))$ | $f'(g(x)) \cdot g'(x)$ |

## Derivadas de Funciones Trigonométricas

| [Función](../../glossary.md#funcion) | [Derivada](../../glossary.md#derivada) |
|---------|----------|
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |
| $\cot x$ | $-\csc^2 x$ |
| $\sec x$ | $\sec x \tan x$ |
| $\csc x$ | $-\csc x \cot x$ |

## Derivadas de Funciones Trigonométricas Inversas

| Función | Derivada |
|---------|----------|
| $\arcsin x$ | $\frac{1}{\sqrt{1-x^2}}$ |
| $\arccos x$ | $-\frac{1}{\sqrt{1-x^2}}$ |
| $\arctan x$ | $\frac{1}{1+x^2}$ |
| $\text{arccot } x$ | $-\frac{1}{1+x^2}$ |
| $\text{arcsec } x$ | $\frac{1}{|x|\sqrt{x^2-1}}$ |
| $\text{arccsc } x$ | $-\frac{1}{|x|\sqrt{x^2-1}}$ |

## Derivadas de Funciones Exponenciales y Logarítmicas

| Función | Derivada |
|---------|----------|
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ | $\frac{1}{x}$ |
| $\log_a x$ | $\frac{1}{x \ln a}$ |
| $e^{u(x)}$ | $e^{u(x)} \cdot u'(x)$ |
| $\ln u(x)$ | $\frac{u'(x)}{u(x)}$ |

## Derivadas de Funciones Hiperbólicas

| Función | Derivada |
|---------|----------|
| $\sinh x$ | $\cosh x$ |
| $\cosh x$ | $\sinh x$ |
| $\tanh x$ | $\text{sech}^2 x$ |

## Regla de la Cadena (Generalizada)

Si $y = f(u)$ y $u = g(x)$:

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

Para composiciones múltiples:

$$\frac{d}{dx}[f(g(h(x)))] = f'(g(h(x))) \cdot g'(h(x)) \cdot h'(x)$$

## Derivación Implícita

Si $F(x, y) = 0$, derivar ambos lados respecto a $x$, tratando $y$ como función de $x$:

$$\frac{dy}{dx} = -\frac{F_x}{F_y}$$

## Derivación Logarítmica

Para $y = f(x)^{g(x)}$:

1. Tomar logaritmo: $\ln y = g(x) \ln f(x)$
2. Derivar implícitamente: $\frac{y'}{y} = g'(x)\ln f(x) + g(x)\frac{f'(x)}{f(x)}$
3. Despejar: $y' = y \left[ g'(x)\ln f(x) + \frac{g(x)f'(x)}{f(x)} \right]$

## Derivadas de Orden Superior

$$f''(x) = \frac{d^2f}{dx^2}, \quad f'''(x) = \frac{d^3f}{dx^3}, \quad f^{(n)}(x) = \frac{d^nf}{dx^n}$$

### Ejemplos Importantes

| Función | $n$-ésima derivada |
|---------|-------------------|
| $e^{ax}$ | $a^n e^{ax}$ |
| $\sin x$ | $\sin\left(x + \frac{n\pi}{2}\right)$ |
| $\cos x$ | $\cos\left(x + \frac{n\pi}{2}\right)$ |
| $x^m$ | $\frac{m!}{(m-n)!}x^{m-n}$ (si $n \leq m$) |

---

> **Tip**: Memoriza las [derivadas](../../glossary.md#derivadas) básicas y practica la [regla de la cadena](../../glossary.md#regla-de-la-cadena) hasta que sea automática.
