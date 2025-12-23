<!--
::METADATA::
type: reference
topic_id: teoremas-fundamentales
file_id: _directives
status: stable
audience: ai_context
-->

# Directivas para Teoremas Fundamentales

## Clasificación del Contenido

| Carpeta/Archivo | Archivo Principal | Descripción |
|-----------------|-------------------|-------------|
| `theory/` | `CD-04-Teoria-Teoremas-Fundamentales.md` | Teoría de teoremas fundamentales |
| `methods/` | `CD-04-Metodos-Teoremas-Fundamentales.md` | Procedimientos paso a paso |
| `problems/` | `CD-04-Problemas.md` | Enunciados de problemas |
| `solutions/` | `CD-04-Respuestas.md`, `CD-04-Soluciones-Desarrolladas.md` | Soluciones desarrolladas |
| `CD-04-Teoremas-Fundamentales-Intro.md` | — | Entrada principal del tema |
| `CD-04-Resumen-Formulas.md` | — | Resumen de fórmulas |
| `manifest.json` | — | Metadatos y configuración |

---

## Series de Maclaurin Estándar

| Función | Serie | Radio de Convergencia |
|---------|-------|----------------------|
| $e^x$ | $\displaystyle\sum_{n=0}^{\infty} \frac{x^n}{n!}$ | $\infty$ |
| $\sin x$ | $\displaystyle\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}$ | $\infty$ |
| $\cos x$ | $\displaystyle\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}$ | $\infty$ |
| $\ln(1+x)$ | $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^{n+1} x^n}{n}$ | $1$ |
| $\frac{1}{1-x}$ | $\displaystyle\sum_{n=0}^{\infty} x^n$ | $1$ |
| $(1+x)^\alpha$ | $\displaystyle\sum_{n=0}^{\infty} \binom{\alpha}{n} x^n$ | $1$ |
| $\arctan x$ | $\displaystyle\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{2n+1}$ | $1$ |

## Formas Indeterminadas

| Forma | Método Principal |
|-------|------------------|
| $\frac{0}{0}$ | L'Hôpital directo |
| $\frac{\infty}{\infty}$ | L'Hôpital directo |
| $0 \cdot \infty$ | Convertir a cociente |
| $\infty - \infty$ | Fracción común o racionalización |
| $0^0$ | Logaritmo + L'Hôpital |
| $1^\infty$ | Logaritmo + L'Hôpital |
| $\infty^0$ | Logaritmo + L'Hôpital |

## Fórmula de Taylor

$$f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k + R_n(x)$$

## Residuo de Lagrange

$$R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$

donde $c$ está entre $a$ y $x$.

## Límites Útiles (referencia rápida)

- $\displaystyle\lim_{x \to 0} \frac{\sin x}{x} = 1$
- $\displaystyle\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$
- $\displaystyle\lim_{x \to 0} \frac{\tan x}{x} = 1$
- $\displaystyle\lim_{x \to 0} \frac{e^x - 1}{x} = 1$
- $\displaystyle\lim_{x \to 0} \frac{\ln(1+x)}{x} = 1$
- $\displaystyle\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e$

## Convenciones de Formato

- Usar $\displaystyle\lim$ en línea separada para límites complejos
- Indicar forma indeterminada antes de aplicar L'Hôpital
- Verificar hipótesis de teoremas antes de aplicarlos
- Mostrar desarrollo de Taylor término a término
