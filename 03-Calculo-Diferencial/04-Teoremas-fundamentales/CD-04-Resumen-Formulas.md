<!--
::METADATA::
type: cheatsheet
topic_id: cd-04-teoremas
file_id: CD-04-Resumen-Formulas
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

---

# Resumen de Fórmulas: Teoremas Fundamentales

## Teorema de Rolle

**Hipótesis:**
1. $f$ es continua en $[a, b]$
2. $f$ es derivable en $(a, b)$
3. $f(a) = f(b)$

**Conclusión:** Existe al menos un $c \in (a, b)$ [tal que](../..](../../glossary.md)#tal-que):

$$f'(c) = 0$$

## Teorema del Valor Medio (Lagrange)

**Hipótesis:**
1. $f$ es continua en $[a, b]$
2. $f$ es derivable en $(a, b)$

**Conclusión:** Existe al menos un $c \in (a, b)$ [tal que](../..](../../glossary.md)#tal-que):

$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

### Interpretación Geométrica

La pendiente de la recta [tangente](../..](../../glossary.md)#tangente) en $c$ es igual a la pendiente de la recta secante que une $(a, f(a))$ y $(b, f(b))$.

## Teorema del Valor Medio de Cauchy

**Hipótesis:**
1. $f$ y $g$ son continuas en $[a, b]$
2. $f$ y $g$ son derivables en $(a, b)$
3. $g'(x) \neq 0$ para todo $x \in (a, b)$

**Conclusión:** Existe al menos un $c \in (a, b)$ tal que:

$$\frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}$$

## Corolarios del Teorema del Valor Medio

### Funciones con Derivada Cero

Si $f'(x) = 0$ para todo $x$ en un intervalo, entonces $f$ es **constante**.

### Funciones con Derivadas Iguales

Si $f'(x) = g'(x)$ para todo $x$ en un intervalo, entonces:
$$f(x) = g(x) + C$$

### Signo de la Derivada

- $f'(x) > 0$ en $(a,b)$ $\Rightarrow$ $f$ es creciente en $(a,b)$
- $f'(x) < 0$ en $(a,b)$ $\Rightarrow$ $f$ es decreciente en $(a,b)$

## Serie de Taylor

La serie de Taylor de $f(x)$ centrada en $x = a$:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$$

**Forma expandida:**

$$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots$$

## Serie de Maclaurin

Serie de Taylor centrada en $x = 0$:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^n$$

## Series de Maclaurin Importantes

### Exponencial

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

### Seno

$$\sin x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$$

### Coseno

$$\cos x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$$

### Logaritmo Natural

$$\ln(1+x) = \sum_{n=1}^{\infty} \frac{(-1)^{n+1} x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots, \quad |x| \leq 1$$

### Serie Geométrica

$$\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n = 1 + x + x^2 + x^3 + \cdots, \quad |x| < 1$$

### Binomial

$$(1+x)^k = \sum_{n=0}^{\infty} \binom{k}{n} x^n = 1 + kx + \frac{k(k-1)}{2!}x^2 + \cdots$$

## Polinomio de Taylor de Grado $n$

$$P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k$$

## Residuo (Error) de Taylor

### Forma de Lagrange

$$R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$$

donde $\xi$ está entre $a$ y $x$.

### Cota del Error

$$|R_n(x)| \leq \frac{M}{(n+1)!}|x-a|^{n+1}$$

donde $M = \max |f^{(n+1)}(t)|$ para $t$ entre $a$ y $x$.

## Aplicaciones de Taylor

1. **Aproximación de funciones**: $f(x) \approx P_n(x)$
2. **Cálculo de [límites](../..](../../glossary.md)#limites)**: Expandir y simplificar
3. **Evaluación de integrales**: Integrar término a término
4. **Análisis numérico**: [Base](../..](../../glossary.md)#base) de muchos algoritmos

---

> **Tip**: Las series de Taylor son herramientas poderosas para aproximar funciones. Memoriza las series más comunes ($e^x$, $\sin x$, $\cos x$, $\ln(1+x)$).
