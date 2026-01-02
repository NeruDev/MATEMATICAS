<!--
::METADATA::
type: method
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Métodos para Evaluar Límites

> Guía completa de métodos con algoritmos detallados, tablas de procedimientos y ejemplos paso a paso.

---

## Método 1: Sustitución Directa

**Cuándo Usar:** Cuando la [función](../../../glossary.md#funcion) es continua en el punto de evaluación y no produce formas indeterminadas.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Sustituir directamente | Reemplazar $x = a$ en $f(x)$ |
| 2 | Calcular | Realizar las operaciones |
| 3 | Verificar | Confirmar que el resultado es un número definido |

### Funciones donde aplica directamente

| Tipo de [Función](../../../glossary.md#funcion) | Condición |
|-----------------|-----------|
| Polinomios | Siempre continuas |
| Racionales | Si $x = a$ no anula el denominador |
| Trigonométricas | En puntos de su [dominio](../../../glossary.md#dominio) |
| Exponenciales | Siempre continuas |
| Logarítmicas | Si el argumento es positivo |

### Ejemplo Detallado

**Problema:** Calcular $\displaystyle\lim_{x \to 2} (x^3 - 3x^2 + 5x - 7)$

---

**Paso 1: Verificar [continuidad](../../../glossary.md#continuidad)**

Los polinomios son continuos en todo $\mathbb{R}$, por lo tanto podemos sustituir directamente.

---

**Paso 2: Sustituir $x = 2$**

$$f(2) = (2)^3 - 3(2)^2 + 5(2) - 7$$
$$= 8 - 12 + 10 - 7$$
$$= -1$$

$$\boxed{\lim_{x \to 2} (x^3 - 3x^2 + 5x - 7) = -1}$$

---

## Método 2: Factorización

**Cuándo Usar:** [Forma indeterminada](../../../glossary.md#forma-indeterminada) $\frac{0}{0}$ donde numerador y denominador son polinomios o expresiones factorizables.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar forma | Sustituir para confirmar $\frac{0}{0}$ |
| 2 | [Factorizar](../../../glossary.md#factorizar) | Numerador y denominador |
| 3 | Cancelar | El factor común $(x - a)$ |
| 4 | Sustituir | En la expresión simplificada |

### Técnicas de Factorización Útiles

| Expresión | [Factorización](../../../glossary.md#factorizacion) |
|-----------|---------------|
| $x^2 - a^2$ | $(x-a)(x+a)$ |
| $x^3 - a^3$ | $(x-a)(x^2 + ax + a^2)$ |
| $x^3 + a^3$ | $(x+a)(x^2 - ax + a^2)$ |
| $x^n - a^n$ | $(x-a)(x^{n-1} + x^{n-2}a + \cdots + a^{n-1})$ |

### Ejemplo Detallado

**Problema:** Calcular $\displaystyle\lim_{x \to 3} \frac{x^3 - 27}{x^2 - 9}$

---

**Paso 1: Verificar [forma indeterminada](../../../glossary.md#forma-indeterminada)**

$$\frac{(3)^3 - 27}{(3)^2 - 9} = \frac{27 - 27}{9 - 9} = \frac{0}{0}$$

---

**Paso 2: [Factorizar](../../../glossary.md#factorizar) numerador (diferencia de cubos)**

$$x^3 - 27 = x^3 - 3^3 = (x - 3)(x^2 + 3x + 9)$$

---

**Paso 3: Factorizar denominador (diferencia de cuadrados)**

$$x^2 - 9 = (x - 3)(x + 3)$$

---

**Paso 4: Cancelar y sustituir**

$$\lim_{x \to 3} \frac{(x-3)(x^2 + 3x + 9)}{(x-3)(x+3)} = \lim_{x \to 3} \frac{x^2 + 3x + 9}{x + 3}$$

$$= \frac{9 + 9 + 9}{6} = \frac{27}{6} = \frac{9}{2}$$

$$\boxed{\lim_{x \to 3} \frac{x^3 - 27}{x^2 - 9} = \frac{9}{2}}$$

---

## Método 3: Racionalización

**Cuándo Usar:** Forma $\frac{0}{0}$ con expresiones que contienen radicales.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar radicales | En numerador o denominador |
| 2 | Multiplicar por conjugado | $\frac{\sqrt{a} - \sqrt{b}}{1} \times \frac{\sqrt{a} + \sqrt{b}}{\sqrt{a} + \sqrt{b}}$ |
| 3 | Aplicar diferencia de cuadrados | $(\sqrt{a})^2 - (\sqrt{b})^2 = a - b$ |
| 4 | Simplificar y evaluar | Cancelar factores comunes |

### Conjugados Comunes

| Expresión | Conjugado |
|-----------|-----------|
| $\sqrt{a} - b$ | $\sqrt{a} + b$ |
| $\sqrt{a} + \sqrt{b}$ | $\sqrt{a} - \sqrt{b}$ |
| $\sqrt[3]{a} - b$ | $\sqrt[3]{a^2} + b\sqrt[3]{a} + b^2$ |

### Ejemplo Detallado

**Problema:** Calcular $\displaystyle\lim_{x \to 0} \frac{\sqrt{1 + x} - 1}{x}$

---

**Paso 1: Verificar forma indeterminada**

$$\frac{\sqrt{1 + 0} - 1}{0} = \frac{1 - 1}{0} = \frac{0}{0}$$

---

**Paso 2: Multiplicar por el conjugado**

$$\frac{\sqrt{1 + x} - 1}{x} \times \frac{\sqrt{1 + x} + 1}{\sqrt{1 + x} + 1}$$

---

**Paso 3: Aplicar diferencia de cuadrados en numerador**

$$= \frac{(\sqrt{1+x})^2 - 1^2}{x(\sqrt{1+x} + 1)} = \frac{(1 + x) - 1}{x(\sqrt{1+x} + 1)}$$

$$= \frac{x}{x(\sqrt{1+x} + 1)} = \frac{1}{\sqrt{1+x} + 1}$$

---

**Paso 4: Evaluar el [límite](../../../glossary.md#limite)**

$$\lim_{x \to 0} \frac{1}{\sqrt{1+x} + 1} = \frac{1}{\sqrt{1} + 1} = \frac{1}{2}$$

$$\boxed{\lim_{x \to 0} \frac{\sqrt{1 + x} - 1}{x} = \frac{1}{2}}$$

---

### Ejemplo con Raíces en Denominador

**Problema:** Calcular $\displaystyle\lim_{x \to 4} \frac{x - 4}{\sqrt{x} - 2}$

---

**Paso 1: Verificar forma $\frac{0}{0}$**

$$\frac{4 - 4}{\sqrt{4} - 2} = \frac{0}{0}$$

---

**Paso 2: Racionalizar el denominador**

$$\frac{x - 4}{\sqrt{x} - 2} \times \frac{\sqrt{x} + 2}{\sqrt{x} + 2} = \frac{(x-4)(\sqrt{x} + 2)}{x - 4}$$

---

**Paso 3: Simplificar**

$$= \sqrt{x} + 2$$

---

**Paso 4: Evaluar**

$$\lim_{x \to 4} (\sqrt{x} + 2) = 2 + 2 = 4$$

$$\boxed{\lim_{x \to 4} \frac{x - 4}{\sqrt{x} - 2} = 4}$$

---

## Método 4: División entre Mayor Potencia (Límites al Infinito)

**Cuándo Usar:** [Límites](../../../glossary.md#limites) cuando $x \to \pm\infty$ en funciones racionales.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar grados | $n$ = grado numerador, $m$ = grado denominador |
| 2 | Dividir todo | Por $x^m$ (mayor potencia del denominador) |
| 3 | Aplicar [límites](../../../glossary.md#limites) | $\lim_{x \to \infty} \frac{1}{x^k} = 0$ para $k > 0$ |
| 4 | Evaluar | Los términos restantes |

### Regla Rápida

| Comparación de Grados | Resultado |
|----------------------|-----------|
| $n < m$ | $\lim = 0$ |
| $n = m$ | $\lim = \frac{\text{coef. principal num.}}{\text{coef. principal den.}}$ |
| $n > m$ | $\lim = \pm\infty$ |

### Ejemplo Detallado

**Problema:** Calcular $\displaystyle\lim_{x \to \infty} \frac{5x^3 - 2x^2 + 7}{3x^3 + 4x - 1}$

---

**Paso 1: Identificar grados**

Numerador: grado 3, Denominador: grado 3 (iguales)

---

**Paso 2: Dividir todo entre $x^3$**

$$\frac{5x^3 - 2x^2 + 7}{3x^3 + 4x - 1} = \frac{\frac{5x^3}{x^3} - \frac{2x^2}{x^3} + \frac{7}{x^3}}{\frac{3x^3}{x^3} + \frac{4x}{x^3} - \frac{1}{x^3}}$$

$$= \frac{5 - \frac{2}{x} + \frac{7}{x^3}}{3 + \frac{4}{x^2} - \frac{1}{x^3}}$$

---

**Paso 3: Aplicar límites**

Cuando $x \to \infty$: $\frac{1}{x}, \frac{1}{x^2}, \frac{1}{x^3} \to 0$

$$\lim_{x \to \infty} \frac{5 - 0 + 0}{3 + 0 - 0} = \frac{5}{3}$$

$$\boxed{\lim_{x \to \infty} \frac{5x^3 - 2x^2 + 7}{3x^3 + 4x - 1} = \frac{5}{3}}$$

---

### Ejemplo cuando $n > m$

**Problema:** Calcular $\displaystyle\lim_{x \to \infty} \frac{2x^4 - x}{x^2 + 3}$

---

**Grado numerador (4) > Grado denominador (2)**

$$= \lim_{x \to \infty} \frac{x^2(2x^2 - \frac{1}{x})}{x^2(1 + \frac{3}{x^2})} = \lim_{x \to \infty} \frac{2x^2 - \frac{1}{x}}{1 + \frac{3}{x^2}} = \frac{\infty}{1} = +\infty$$

$$\boxed{\lim_{x \to \infty} \frac{2x^4 - x}{x^2 + 3} = +\infty}$$

---

## Método 5: Límites Trigonométricos Fundamentales

**Cuándo Usar:** Expresiones con funciones trigonométricas cuando $x \to 0$.

### Límites Fundamentales

| [Límite](../../../glossary.md#limite) | Valor |
|--------|-------|
| $\displaystyle\lim_{u \to 0} \frac{\sin u}{u}$ | $1$ |
| $\displaystyle\lim_{u \to 0} \frac{u}{\sin u}$ | $1$ |
| $\displaystyle\lim_{u \to 0} \frac{\tan u}{u}$ | $1$ |
| $\displaystyle\lim_{u \to 0} \frac{1 - \cos u}{u}$ | $0$ |
| $\displaystyle\lim_{u \to 0} \frac{1 - \cos u}{u^2}$ | $\frac{1}{2}$ |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar argumento | $u = $ expresión dentro de la función trig |
| 2 | Manipular algebraicamente | Para obtener forma $\frac{\sin u}{u}$ |
| 3 | Multiplicar por factores | $\frac{u}{u}$ para introducir/cancelar |
| 4 | Aplicar límites conocidos | Sustituir los límites fundamentales |

### Ejemplo Detallado

**Problema:** Calcular $\displaystyle\lim_{x \to 0} \frac{\sin 5x}{3x}$

---

**Paso 1: Identificar el argumento**

El argumento del [seno](../../../glossary.md#seno) es $5x$, pero el denominador tiene $3x$.

---

**Paso 2: Introducir el factor [necesario](../../../glossary.md#necesario)**

$$\frac{\sin 5x}{3x} = \frac{\sin 5x}{5x} \cdot \frac{5x}{3x} = \frac{\sin 5x}{5x} \cdot \frac{5}{3}$$

---

**Paso 3: Aplicar el límite fundamental**

$$\lim_{x \to 0} \frac{\sin 5x}{5x} = 1 \quad \text{(con } u = 5x \to 0\text{)}$$

---

**Paso 4: Calcular**

$$\lim_{x \to 0} \frac{\sin 5x}{3x} = 1 \cdot \frac{5}{3} = \frac{5}{3}$$

$$\boxed{\lim_{x \to 0} \frac{\sin 5x}{3x} = \frac{5}{3}}$$

---

### Ejemplo Compuesto

**Problema:** Calcular $\displaystyle\lim_{x \to 0} \frac{\tan 2x}{\sin 5x}$

---

**Paso 1: Descomponer usando identidades**

$$\frac{\tan 2x}{\sin 5x} = \frac{\sin 2x}{\cos 2x \cdot \sin 5x}$$

---

**Paso 2: Introducir factores auxiliares**

$$= \frac{\sin 2x}{2x} \cdot \frac{5x}{\sin 5x} \cdot \frac{2x}{5x} \cdot \frac{1}{\cos 2x}$$

$$= \frac{\sin 2x}{2x} \cdot \frac{5x}{\sin 5x} \cdot \frac{2}{5} \cdot \frac{1}{\cos 2x}$$

---

**Paso 3: Aplicar límites**

$$\lim_{x \to 0} \frac{\sin 2x}{2x} = 1, \quad \lim_{x \to 0} \frac{5x}{\sin 5x} = 1, \quad \lim_{x \to 0} \cos 2x = 1$$

$$= 1 \cdot 1 \cdot \frac{2}{5} \cdot 1 = \frac{2}{5}$$

$$\boxed{\lim_{x \to 0} \frac{\tan 2x}{\sin 5x} = \frac{2}{5}}$$

---

## Método 6: Teorema del Emparedado (Sandwich)

**Cuándo Usar:** Cuando la función es difícil de evaluar directamente pero se pueden encontrar cotas.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Acotar la función | Encontrar $g(x) \leq f(x) \leq h(x)$ |
| 2 | Calcular límites de cotas | $\lim g(x)$ y $\lim h(x)$ |
| 3 | Verificar igualdad | Si ambos límites son $L$ |
| 4 | Concluir | $\lim f(x) = L$ |

### Cotas Útiles

| Función | Acotación |
|---------|-----------|
| $\sin u$ | $-1 \leq \sin u \leq 1$ |
| $\cos u$ | $-1 \leq \cos u \leq 1$ |
| $\lvert \sin u \rvert$ | $0 \leq \lvert \sin u \rvert \leq 1$ |

### Ejemplo Detallado

**Problema:** Calcular $\displaystyle\lim_{x \to 0} x^2 \cos\left(\frac{1}{x}\right)$

---

**Paso 1: Acotar la función problemática**

Sabemos que $-1 \leq \cos\left(\frac{1}{x}\right) \leq 1$ para todo $x \neq 0$

---

**Paso 2: Multiplicar por $x^2$ (positivo para $x \neq 0$)**

$$-x^2 \leq x^2 \cos\left(\frac{1}{x}\right) \leq x^2$$

---

**Paso 3: Calcular límites de las cotas**

$$\lim_{x \to 0} (-x^2) = 0$$
$$\lim_{x \to 0} x^2 = 0$$

---

**Paso 4: Aplicar el teorema**

Como ambas cotas tienden a 0:

$$\lim_{x \to 0} x^2 \cos\left(\frac{1}{x}\right) = 0$$

$$\boxed{\lim_{x \to 0} x^2 \cos\left(\frac{1}{x}\right) = 0}$$

---

## Método 7: Cambio de Variable (Sustitución)

**Cuándo Usar:** Para simplificar expresiones complicadas mediante una [sustitución](../../../glossary.md#sustitucion) apropiada.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar [sustitución](../../../glossary.md#sustitucion) | $u = g(x)$ para simplificar |
| 2 | Determinar nuevo límite | Si $x \to a$, entonces $u \to g(a)$ |
| 3 | Reescribir | El límite en términos de $u$ |
| 4 | Evaluar | El nuevo límite más simple |

### Sustituciones Comunes

| Situación | Sustitución |
|-----------|-------------|
| $\sin(g(x))$ con $g(x) \to 0$ | $u = g(x)$ |
| $\sqrt[n]{x} - a$ | $u = \sqrt[n]{x}$, entonces $x = u^n$ |
| $e^{g(x)} - 1$ con $g(x) \to 0$ | $u = g(x)$ |

### Ejemplo Detallado

**Problema:** Calcular $\displaystyle\lim_{x \to 1} \frac{\sin(x - 1)}{x^2 - 1}$

---

**Paso 1: Identificar sustitución**

Sea $u = x - 1$. Cuando $x \to 1$, entonces $u \to 0$.

---

**Paso 2: Expresar en términos de $u$**

$$x = u + 1$$
$$x^2 - 1 = (u + 1)^2 - 1 = u^2 + 2u + 1 - 1 = u^2 + 2u = u(u + 2)$$

---

**Paso 3: Reescribir el límite**

$$\lim_{u \to 0} \frac{\sin u}{u(u + 2)} = \lim_{u \to 0} \frac{\sin u}{u} \cdot \frac{1}{u + 2}$$

---

**Paso 4: Evaluar**

$$= 1 \cdot \frac{1}{0 + 2} = \frac{1}{2}$$

$$\boxed{\lim_{x \to 1} \frac{\sin(x - 1)}{x^2 - 1} = \frac{1}{2}}$$

---

### Ejemplo con Raíces

**Problema:** Calcular $\displaystyle\lim_{x \to 8} \frac{\sqrt[3]{x} - 2}{x - 8}$

---

**Paso 1: Sustitución**

Sea $u = \sqrt[3]{x}$, entonces $x = u^3$

Cuando $x \to 8$: $u = \sqrt[3]{8} = 2$, así que $u \to 2$

---

**Paso 2: Reescribir**

$$\lim_{u \to 2} \frac{u - 2}{u^3 - 8}$$

---

**Paso 3: Factorizar denominador**

$$u^3 - 8 = (u - 2)(u^2 + 2u + 4)$$

$$\lim_{u \to 2} \frac{u - 2}{(u - 2)(u^2 + 2u + 4)} = \lim_{u \to 2} \frac{1}{u^2 + 2u + 4}$$

---

**Paso 4: Evaluar**

$$= \frac{1}{4 + 4 + 4} = \frac{1}{12}$$

$$\boxed{\lim_{x \to 8} \frac{\sqrt[3]{x} - 2}{x - 8} = \frac{1}{12}}$$

---

## Método 8: Límites Laterales

**Cuándo Usar:** Funciones definidas por partes, valor absoluto, o verificar existencia del límite.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Calcular límite por izquierda | $\lim_{x \to a^-} f(x)$ |
| 2 | Calcular límite por derecha | $\lim_{x \to a^+} f(x)$ |
| 3 | Comparar | Si son iguales, el límite existe |
| 4 | Concluir | Límite = valor común, o no existe |

### Ejemplo Detallado

**Problema:** Calcular $\displaystyle\lim_{x \to 2} \frac{|x - 2|}{x - 2}$

---

**Paso 1: Analizar el valor absoluto**

$$|x - 2| = \begin{cases} x - 2 & \text{si } x \geq 2 \\ -(x - 2) & \text{si } x < 2 \end{cases}$$

---

**Paso 2: Límite por la derecha ($x \to 2^+$)**

Cuando $x > 2$: $|x - 2| = x - 2$

$$\lim_{x \to 2^+} \frac{x - 2}{x - 2} = \lim_{x \to 2^+} 1 = 1$$

---

**Paso 3: Límite por la izquierda ($x \to 2^-$)**

Cuando $x < 2$: $|x - 2| = -(x - 2)$

$$\lim_{x \to 2^-} \frac{-(x - 2)}{x - 2} = \lim_{x \to 2^-} (-1) = -1$$

---

**Paso 4: Conclusión**

Como $1 \neq -1$, el límite no existe.

$$\boxed{\lim_{x \to 2} \frac{|x - 2|}{x - 2} \text{ no existe}}$$

---

## Método 9: Límite de la Forma Exponencial $e$

**Cuándo Usar:** Expresiones de la forma $(1 + \text{algo})^{\text{algo grande}}$ cuando algo $\to 0$.

### Límites Fundamentales

| Forma | Resultado |
|-------|-----------|
| $\displaystyle\lim_{x \to 0} (1 + x)^{1/x}$ | $e$ |
| $\displaystyle\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x$ | $e$ |
| $\displaystyle\lim_{x \to 0} \frac{e^x - 1}{x}$ | $1$ |
| $\displaystyle\lim_{x \to 0} \frac{\ln(1 + x)}{x}$ | $1$ |
| $\displaystyle\lim_{x \to 0} \frac{a^x - 1}{x}$ | $\ln a$ |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar forma | $(1 + u)^{v}$ donde $u \to 0$ y $v \to \infty$ |
| 2 | Reescribir | Como $[(1 + u)^{1/u}]^{uv}$ |
| 3 | Aplicar límite | $(1 + u)^{1/u} \to e$ |
| 4 | Evaluar exponente | $\lim(uv)$ |

### Ejemplo Detallado

**Problema:** Calcular $\displaystyle\lim_{x \to \infty} \left(1 + \frac{3}{x}\right)^{2x}$

---

**Paso 1: Identificar la forma**

[Base](../../../glossary.md#base): $1 + \frac{3}{x} \to 1$ cuando $x \to \infty$
Exponente: $2x \to \infty$

Forma indeterminada $1^\infty$.

---

**Paso 2: Reescribir usando la forma estándar**

$$\left(1 + \frac{3}{x}\right)^{2x} = \left[\left(1 + \frac{3}{x}\right)^{x/3}\right]^{6}$$

Sea $u = \frac{3}{x}$, entonces $\frac{1}{u} = \frac{x}{3}$

$$= \left[(1 + u)^{1/u}\right]^6$$

---

**Paso 3: Aplicar el límite fundamental**

Cuando $x \to \infty$, $u = \frac{3}{x} \to 0$

$$\lim_{u \to 0} (1 + u)^{1/u} = e$$

---

**Paso 4: Resultado**

$$\lim_{x \to \infty} \left(1 + \frac{3}{x}\right)^{2x} = e^6$$

$$\boxed{\lim_{x \to \infty} \left(1 + \frac{3}{x}\right)^{2x} = e^6}$$

---

## Método 10: Análisis de Asíntotas

**Cuándo Usar:** Para determinar el comportamiento de funciones en los extremos o cerca de discontinuidades.

### Tipos de Asíntotas

| Tipo | Definición | Cómo encontrar |
|------|------------|----------------|
| Vertical | $x = a$ donde $f(x) \to \pm\infty$ | Resolver denominador $= 0$ |
| Horizontal | $y = L$ cuando $x \to \pm\infty$ | $\lim_{x \to \pm\infty} f(x) = L$ |
| Oblicua | $y = mx + b$ cuando $x \to \pm\infty$ | $m = \lim \frac{f(x)}{x}$, $b = \lim[f(x) - mx]$ |

### Algoritmo para Asíntotas Verticales

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Encontrar candidatos | Donde el denominador es 0 |
| 2 | Evaluar límites laterales | $\lim_{x \to a^+}$ y $\lim_{x \to a^-}$ |
| 3 | Determinar signo | Analizar signos de num. y den. |
| 4 | Concluir | $+\infty$ o $-\infty$ en cada lado |

### Ejemplo Detallado

**Problema:** Encontrar las asíntotas de $f(x) = \frac{2x^2 - 1}{x^2 - 4}$

---

**Asíntotas Verticales:**

Denominador $= 0$: $x^2 - 4 = 0 \Rightarrow x = \pm 2$

Para $x = 2$:
- $\lim_{x \to 2^+} \frac{2(4) - 1}{(x-2)(x+2)} = \frac{7}{0^+ \cdot 4} = +\infty$
- $\lim_{x \to 2^-} \frac{7}{0^- \cdot 4} = -\infty$

Asíntotas verticales: $x = 2$ y $x = -2$

---

**[Asíntota](../../../glossary.md#asintota) Horizontal:**

$$\lim_{x \to \infty} \frac{2x^2 - 1}{x^2 - 4} = \lim_{x \to \infty} \frac{2 - \frac{1}{x^2}}{1 - \frac{4}{x^2}} = \frac{2}{1} = 2$$

[Asíntota](../../../glossary.md#asintota) horizontal: $y = 2$

$$\boxed{\text{AV: } x = 2, x = -2; \quad \text{AH: } y = 2}$$

---

## Método 11: Multiplicación por la Unidad Conveniente

**Cuándo Usar:** Cuando necesitas introducir un factor para aplicar un límite conocido.

### Ejemplo Detallado

**Problema:** Calcular $\displaystyle\lim_{x \to 0} \frac{1 - \cos x}{x^2}$

---

**Paso 1: Multiplicar por [identidad trigonométrica](../../../glossary.md#identidad-trigonometrica)**

Usamos: $1 - \cos x = 2\sin^2\left(\frac{x}{2}\right)$

$$\frac{1 - \cos x}{x^2} = \frac{2\sin^2(x/2)}{x^2}$$

---

**Paso 2: Reescribir**

$$= 2 \cdot \frac{\sin^2(x/2)}{x^2} = 2 \cdot \left(\frac{\sin(x/2)}{x}\right)^2$$

$$= 2 \cdot \left(\frac{\sin(x/2)}{x/2} \cdot \frac{1}{2}\right)^2 = 2 \cdot \frac{1}{4} \cdot \left(\frac{\sin(x/2)}{x/2}\right)^2$$

---

**Paso 3: Aplicar límite fundamental**

$$\lim_{x \to 0} \frac{\sin(x/2)}{x/2} = 1$$

$$\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{2}{4} \cdot 1^2 = \frac{1}{2}$$

$$\boxed{\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}}$$

---

## Método 12: Fracciones Complejas

**Cuándo Usar:** Límites con fracciones anidadas (fracciones dentro de fracciones).

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Encontrar LCD | De las fracciones internas |
| 2 | Multiplicar | Numerador y denominador por LCD |
| 3 | Simplificar | La expresión resultante |
| 4 | Evaluar | El límite de la expresión simplificada |

### Ejemplo Detallado

**Problema:** Calcular $\displaystyle\lim_{h \to 0} \frac{\frac{1}{(x+h)^2} - \frac{1}{x^2}}{h}$

---

**Paso 1: Simplificar el numerador**

$$\frac{1}{(x+h)^2} - \frac{1}{x^2} = \frac{x^2 - (x+h)^2}{x^2(x+h)^2}$$

---

**Paso 2: Expandir y simplificar**

$$x^2 - (x+h)^2 = x^2 - x^2 - 2xh - h^2 = -2xh - h^2 = -h(2x + h)$$

$$= \frac{-h(2x + h)}{x^2(x+h)^2}$$

---

**Paso 3: Sustituir en la expresión original**

$$\frac{\frac{-h(2x + h)}{x^2(x+h)^2}}{h} = \frac{-h(2x + h)}{h \cdot x^2(x+h)^2} = \frac{-(2x + h)}{x^2(x+h)^2}$$

---

**Paso 4: Evaluar el límite**

$$\lim_{h \to 0} \frac{-(2x + h)}{x^2(x+h)^2} = \frac{-(2x + 0)}{x^2 \cdot x^2} = \frac{-2x}{x^4} = \frac{-2}{x^3}$$

$$\boxed{\lim_{h \to 0} \frac{\frac{1}{(x+h)^2} - \frac{1}{x^2}}{h} = -\frac{2}{x^3}}$$

---

## Resumen de Formas Indeterminadas

| Forma | Métodos Recomendados |
|-------|---------------------|
| $\frac{0}{0}$ | [Factorización](../../../glossary.md#factorizacion), Racionalización, L'Hôpital |
| $\frac{\infty}{\infty}$ | División por mayor potencia, L'Hôpital |
| $0 \cdot \infty$ | Reescribir como $\frac{0}{0}$ o $\frac{\infty}{\infty}$ |
| $\infty - \infty$ | Racionalizar, factor común |
| $0^0$, $1^\infty$, $\infty^0$ | Logaritmo, forma exponencial |

---

## Tabla de Límites Notables

| Límite | Valor |
|--------|-------|
| $\displaystyle\lim_{x \to 0} \frac{\sin x}{x}$ | $1$ |
| $\displaystyle\lim_{x \to 0} \frac{\tan x}{x}$ | $1$ |
| $\displaystyle\lim_{x \to 0} \frac{1 - \cos x}{x^2}$ | $\frac{1}{2}$ |
| $\displaystyle\lim_{x \to 0} \frac{e^x - 1}{x}$ | $1$ |
| $\displaystyle\lim_{x \to 0} \frac{\ln(1+x)}{x}$ | $1$ |
| $\displaystyle\lim_{x \to 0} (1+x)^{1/x}$ | $e$ |
| $\displaystyle\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x$ | $e$ |
| $\displaystyle\lim_{x \to 0} \frac{a^x - 1}{x}$ | $\ln a$ |

---

## Errores Comunes

| Error | Corrección |
|-------|------------|
| Aplicar L'Hôpital sin verificar forma | Solo usar si es $\frac{0}{0}$ o $\frac{\infty}{\infty}$ |
| $\lim \frac{\sin x}{x} = 1$ para cualquier $x$ | Solo cuando $x \to 0$ |
| Cancelar factores que no son comunes | Verificar que el factor aparece en ambos |
| $\lim(f \cdot g) = \lim f \cdot \lim g$ siempre | Solo si ambos límites existen y son finitos |
| Ignorar límites laterales | Verificar cuando hay discontinuidades |
| $\lim_{x \to a} \frac{0}{f(x)} = 0$ siempre | Falso si $f(x) \to 0$ también |
