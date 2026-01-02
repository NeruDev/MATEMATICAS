<!--
::METADATA::
type: solution
topic_id: cd-01-limites
file_id: prob-43-solucion
problem_ref: Prob-43
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Definición del número e

## Problema
Evalúa $\displaystyle\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x$

---

## Resultado fundamental
Este [límite](../../../..](../../../../glossary.md)#limite) define el **número de Euler** $e$:
$$e = \lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x$$

---

## Demostración de la convergencia

### Paso 1: Definir la sucesión
Sea $a_n = \left(1 + \frac{1}{n}\right)^n$ para $n \in \mathbb{N}$.

### Paso 2: Demostrar que es creciente
Usando la desigualdad AM-GM (media aritmética ≥ media geométrica):

Para $n+1$ números: uno igual a 1 y $n$ iguales a $1 + \frac{1}{n}$:

$$\frac{1 + n\left(1 + \frac{1}{n}\right)}{n+1} \geq \sqrt[n+1]{1 \cdot \left(1 + \frac{1}{n}\right)^n}$$

$$\frac{n + 2}{n+1} = 1 + \frac{1}{n+1} \geq \sqrt[n+1]{\left(1 + \frac{1}{n}\right)^n}$$

$$\left(1 + \frac{1}{n+1}\right)^{n+1} \geq \left(1 + \frac{1}{n}\right)^n$$

Por lo tanto, $a_{n+1} \geq a_n$. La sucesión es **creciente**.

### Paso 3: Demostrar que está acotada
Usando el binomio de Newton:
$$\left(1 + \frac{1}{n}\right)^n = \sum_{k=0}^{n} \binom{n}{k} \frac{1}{n^k}$$

$$= 1 + 1 + \frac{n(n-1)}{2!n^2} + \frac{n(n-1)(n-2)}{3!n^3} + \cdots$$

Cada término es [menor](../../../..](../../../../glossary.md)#menor) que $\frac{1}{k!}$, entonces:
$$\left(1 + \frac{1}{n}\right)^n < 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \cdots = e < 3$$

### Paso 4: Conclusión
Por el teorema de [convergencia](../../../..](../../../../glossary.md)#convergencia) monótona, la sucesión convergente a un número que llamamos $e$.

---

## Valor de e
$$e = 2.718281828459045...$$

---

## Respuesta Final
$$\boxed{\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e \approx 2.71828}$$

---

## Verificación numérica

| $x$ | $\left(1 + \frac{1}{x}\right)^x$ |
|:---:|:--------------------------------:|
| 1 | 2 |
| 10 | 2.59374... |
| 100 | 2.70481... |
| 1000 | 2.71692... |
| 10000 | 2.71815... |
| 100000 | 2.71827... |

El valor converge a $e \approx 2.71828$. ✓

---

## Formas equivalentes del límite

$$e = \lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = \lim_{x \to 0} (1 + x)^{1/x} = \sum_{n=0}^{\infty} \frac{1}{n!}$$

---

## Aplicaciones
- [Base](../../../..](../../../../glossary.md)#base) del logaritmo natural: $\ln x = \log_e x$
- [Función](../../../..](../../../../glossary.md)#funcion) exponencial: $e^x$
- Crecimiento/decrecimiento continuo
- Fórmula de Euler: $e^{i\pi} + 1 = 0$
