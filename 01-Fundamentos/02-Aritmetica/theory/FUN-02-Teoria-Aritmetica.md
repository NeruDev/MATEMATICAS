<!--
::METADATA::
type: theory
topic_id: fun-02-aritmetica
file_id: FUN-02-Teoria-Aritmetica
status: stable
audience: student
requires: []
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Teoría de Aritmética

La aritmética es la rama más antigua de las matemáticas, fundamental para todas las demás áreas. Dominar sus conceptos es esencial para el éxito en álgebra, cálculo y matemáticas superiores.

---

## 2.1 Sistemas numéricos

### Números naturales $\mathbb{N}$

$$\mathbb{N} = \{1, 2, 3, 4, 5, \ldots\}$$

- Usados para contar.
- Cerrados bajo suma y multiplicación.
- **No cerrados** bajo resta ni división.

> **Nota**: Algunos autores incluyen el 0 en $\mathbb{N}$. Escribimos $\mathbb{N}_0 = \{0, 1, 2, 3, \ldots\}$.

### Números enteros $\mathbb{Z}$

$$\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}$$

- Incluyen negativos y el cero.
- Cerrados bajo suma, resta y multiplicación.
- **No cerrados** bajo división.

### Números racionales $\mathbb{Q}$

$$\mathbb{Q} = \left\{ \frac{p}{q} : p, q \in \mathbb{Z}, q \neq 0 \right\}$$

- Todo número que puede expresarse como fracción de enteros.
- Incluyen decimales finitos y periódicos.
- Cerrados bajo las cuatro operaciones (excepto división por cero).

**Ejemplos**: $\frac{3}{4} = 0.75$, $\frac{1}{3} = 0.\overline{3}$, $-\frac{7}{2} = -3.5$

### Números irracionales $\mathbb{I}$

Números que **no pueden** expresarse como fracción de enteros.

- Decimales infinitos no periódicos.
- Ejemplos: $\sqrt{2} \approx 1.41421356...$, $\pi \approx 3.14159265...$, $e \approx 2.71828...$

**Demostración clásica**: $\sqrt{2}$ es irracional (por contradicción).

### Números reales $\mathbb{R}$

$$\mathbb{R} = \mathbb{Q} \cup \mathbb{I}$$

- Todos los puntos de la recta numérica.
- Cerrados bajo las cuatro operaciones básicas (excepto división por cero).

### Jerarquía de conjuntos

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$$

| Conjunto | Símbolo | Ejemplo | No pertenece |
|----------|---------|---------|--------------|
| Naturales | $\mathbb{N}$ | 5, 17, 1000 | -3, 0, 0.5 |
| Enteros | $\mathbb{Z}$ | -7, 0, 42 | 0.5, $\sqrt{2}$ |
| Racionales | $\mathbb{Q}$ | $\frac{2}{3}$, -4, 0.25 | $\pi$, $\sqrt{3}$ |
| Reales | $\mathbb{R}$ | Todo lo anterior + irracionales | $\sqrt{-1}$ |

---

## 2.2 Operaciones fundamentales y sus propiedades

### Las cuatro operaciones básicas

| Operación | Símbolo | Términos | Resultado |
|-----------|---------|----------|-----------|
| Suma | $+$ | Sumandos | Suma |
| Resta | $-$ | Minuendo, sustraendo | Diferencia |
| Multiplicación | $\times$ o $\cdot$ | Factores | Producto |
| División | $\div$ o $/$ | Dividendo, divisor | Cociente |

### Propiedades de la suma y multiplicación

| Propiedad | Suma | Multiplicación |
|-----------|------|----------------|
| **Conmutativa** | $a + b = b + a$ | $a \cdot b = b \cdot a$ |
| **Asociativa** | $(a + b) + c = a + (b + c)$ | $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ |
| **Elemento neutro** | $a + 0 = a$ | $a \cdot 1 = a$ |
| **Elemento inverso** | $a + (-a) = 0$ | $a \cdot \frac{1}{a} = 1$ (si $a \neq 0$) |

**Propiedad Distributiva** (conecta suma y multiplicación):
$$a \cdot (b + c) = a \cdot b + a \cdot c$$

### Jerarquía de operaciones (PEMDAS)

[Orden](../../../glossary.md#orden) de evaluación:
1. **P**aréntesis (y otros agrupadores)
2. **E**xponentes (potencias y raíces)
3. **M**ultiplicación y **D**ivisión (izquierda a derecha)
4. **A**dición (suma) y **S**ustracción (izquierda a derecha)

**Ejemplo**: $3 + 4 \times 2^2 = 3 + 4 \times 4 = 3 + 16 = 19$

### Operaciones con números negativos

| Operación | Regla | Ejemplo |
|-----------|-------|---------|
| $(-a) + (-b)$ | $-(a + b)$ | $(-3) + (-5) = -8$ |
| $(-a) - (-b)$ | $-a + b$ | $(-3) - (-5) = 2$ |
| $(-a) \times (-b)$ | $+(a \times b)$ | $(-3) \times (-5) = 15$ |
| $(-a) \times b$ | $-(a \times b)$ | $(-3) \times 5 = -15$ |
| $\frac{-a}{-b}$ | $+\frac{a}{b}$ | $\frac{-6}{-2} = 3$ |

---

## 2.3 Divisibilidad y números primos

### Divisibilidad

**Definición**: Decimos que $a$ **divide** a $b$ (escrito $a \mid b$) si existe un entero $k$ [tal que](../../../glossary.md#tal-que) $b = a \cdot k$.

**Ejemplos**: $3 \mid 12$ porque $12 = 3 \times 4$. Pero $3 \nmid 10$.

### Criterios de divisibilidad

| Divisor | Criterio | Ejemplo |
|---------|----------|---------|
| 2 | Último dígito par (0, 2, 4, 6, 8) | 1234 ✓ |
| 3 | Suma de dígitos divisible por 3 | 123 → 1+2+3=6 ✓ |
| 4 | Últimos dos dígitos divisibles por 4 | 1324 → 24÷4=6 ✓ |
| 5 | Termina en 0 o 5 | 1235 ✓ |
| 6 | Divisible por 2 y por 3 | 126 ✓ |
| 8 | Últimos tres dígitos divisibles por 8 | 1024 → 024÷8=3 ✓ |
| 9 | Suma de dígitos divisible por 9 | 729 → 7+2+9=18 ✓ |
| 10 | Termina en 0 | 1230 ✓ |
| 11 | Suma alternada de dígitos divisible por 11 | 121 → 1-2+1=0 ✓ |

### Números primos

**Definición**: Un número natural $p > 1$ es **primo** si sus únicos divisores positivos son 1 y $p$.

**Primeros primos**: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, ...

> **Nota**: 2 es el único primo par. El 1 no se considera primo.

**Número compuesto**: Un número natural $n > 1$ que no es primo.

### Teorema fundamental de la aritmética

> Todo entero $n > 1$ puede expresarse de manera **única** como producto de primos (salvo el [orden](../../../glossary.md#orden) de los factores).

$$n = p_1^{a_1} \cdot p_2^{a_2} \cdot \ldots \cdot p_k^{a_k}$$

**Ejemplos**:
- $60 = 2^2 \cdot 3 \cdot 5$
- $84 = 2^2 \cdot 3 \cdot 7$
- $100 = 2^2 \cdot 5^2$

---

## 2.4 Máximo Común Divisor (MCD) y Mínimo Común Múltiplo (MCM)

### Máximo Común Divisor

**Definición**: El [MCD](../../../glossary.md#mcd) de dos números es el mayor número que divide a ambos.

$$\text{[MCD](../../../glossary.md#mcd)}(a, b) = \max\{d : d \mid a \text{ y } d \mid b\}$$

**Método por [factorización](../../../glossary.md#factorizacion)**:
1. Descomponer ambos números en factores primos.
2. Tomar los factores comunes con el **[menor](../../../glossary.md#menor)** exponente.

**Ejemplo**: $\text{MCD}(60, 84)$
- $60 = 2^2 \cdot 3 \cdot 5$
- $84 = 2^2 \cdot 3 \cdot 7$
- Comunes: $2^2 \cdot 3 = 12$

### Algoritmo de Euclides

Método eficiente para calcular el MCD:

$$\text{MCD}(a, b) = \text{MCD}(b, a \mod b)$$

Repetir hasta que el residuo sea 0.

**Ejemplo**: $\text{MCD}(252, 105)$
- $252 = 105 \times 2 + 42$
- $105 = 42 \times 2 + 21$
- $42 = 21 \times 2 + 0$
- **MCD** = 21

### Mínimo Común Múltiplo

**Definición**: El [MCM](../../../glossary.md#mcm) de dos números es el [menor](../../../glossary.md#menor) número positivo divisible por ambos.

$$\text{[MCM](../../../glossary.md#mcm)}(a, b) = \min\{m > 0 : a \mid m \text{ y } b \mid m\}$$

**Método por [factorización](../../../glossary.md#factorizacion)**:
1. Descomponer ambos números en factores primos.
2. Tomar todos los factores con el **mayor** exponente.

**Ejemplo**: $\text{MCM}(60, 84)$
- $60 = 2^2 \cdot 3 \cdot 5$
- $84 = 2^2 \cdot 3 \cdot 7$
- Todos: $2^2 \cdot 3 \cdot 5 \cdot 7 = 420$

### Relación MCD-MCM

$$\text{MCD}(a, b) \times \text{MCM}(a, b) = a \times b$$

---

## 2.5 Fracciones

### Definición y terminología

Una **fracción** $\frac{a}{b}$ representa $a$ partes de un todo dividido en $b$ partes iguales.

- **Numerador** ($a$): número de partes tomadas.
- **Denominador** ($b$): número de partes en que se divide el todo.

### Tipos de fracciones

| Tipo | Condición | Ejemplo |
|------|-----------|---------|
| Propia | $\lvert a \rvert < \lvert b \rvert$ | $\frac{3}{5}$ |
| Impropia | $\lvert a \rvert \geq \lvert b \rvert$ | $\frac{7}{4}$ |
| Mixta | Entero + fracción propia | $1\frac{3}{4}$ |
| Equivalentes | $\frac{a}{b} = \frac{ka}{kb}$ | $\frac{2}{3} = \frac{4}{6}$ |

### Operaciones con fracciones

**Suma y resta** (mismo denominador):
$$\frac{a}{c} \pm \frac{b}{c} = \frac{a \pm b}{c}$$

**Suma y resta** (diferente denominador):
$$\frac{a}{b} \pm \frac{c}{d} = \frac{ad \pm bc}{bd}$$

> **Mejor práctica**: Usar el MCM de los denominadores.

**Multiplicación**:
$$\frac{a}{b} \times \frac{c}{d} = \frac{a \cdot c}{b \cdot d}$$

**División**:
$$\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c} = \frac{ad}{bc}$$

### Simplificación

Dividir numerador y denominador por su MCD:
$$\frac{a}{b} = \frac{a/\text{MCD}(a,b)}{b/\text{MCD}(a,b)}$$

**Ejemplo**: $\frac{24}{36} = \frac{24/12}{36/12} = \frac{2}{3}$

---

## 2.6 Decimales y porcentajes

### Conversiones

| De | A | Método | Ejemplo |
|----|---|--------|---------|
| Fracción | Decimal | Dividir | $\frac{3}{4} = 0.75$ |
| Decimal | Fracción | Usar potencia de 10 | $0.125 = \frac{125}{1000} = \frac{1}{8}$ |
| Decimal | Porcentaje | Multiplicar por 100 | $0.75 = 75\%$ |
| Porcentaje | Decimal | Dividir por 100 | $45\% = 0.45$ |
| Fracción | Porcentaje | $\frac{a}{b} \times 100\%$ | $\frac{3}{5} = 60\%$ |

### Decimales periódicos

Todo racional tiene representación decimal finita o periódica.

- **Finito**: $\frac{3}{8} = 0.375$
- **Periódico puro**: $\frac{1}{3} = 0.\overline{3}$
- **Periódico mixto**: $\frac{1}{6} = 0.1\overline{6}$

**Conversión de periódico a fracción**:
$$0.\overline{ab} = \frac{ab}{99}, \quad 0.\overline{abc} = \frac{abc}{999}$$

**Ejemplo**: $0.\overline{36} = \frac{36}{99} = \frac{4}{11}$

### Cálculos con porcentajes

- **Porcentaje de una cantidad**: $x\% \text{ de } n = \frac{x}{100} \times n$
- **Incremento porcentual**: $n_{\text{nuevo}} = n \times (1 + \frac{x}{100})$
- **Descuento porcentual**: $n_{\text{nuevo}} = n \times (1 - \frac{x}{100})$

---

## 2.7 Potencias y raíces

### Definición de potencia

$$a^n = \underbrace{a \times a \times \cdots \times a}_{n \text{ veces}}$$

### Leyes de los exponentes

| Ley | Fórmula | Ejemplo |
|-----|---------|---------|
| Producto | $a^m \cdot a^n = a^{m+n}$ | $2^3 \cdot 2^4 = 2^7$ |
| Cociente | $\frac{a^m}{a^n} = a^{m-n}$ | $\frac{5^6}{5^2} = 5^4$ |
| Potencia de potencia | $(a^m)^n = a^{mn}$ | $(3^2)^4 = 3^8$ |
| Producto a una potencia | $(ab)^n = a^n b^n$ | $(2 \cdot 3)^4 = 2^4 \cdot 3^4$ |
| Cociente a una potencia | $\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$ | $\left(\frac{2}{5}\right)^3 = \frac{8}{125}$ |
| Exponente cero | $a^0 = 1$ (si $a \neq 0$) | $7^0 = 1$ |
| Exponente negativo | $a^{-n} = \frac{1}{a^n}$ | $2^{-3} = \frac{1}{8}$ |

### Raíces

**Definición**: $\sqrt[n]{a} = b$ si y solo si $b^n = a$.

$$\sqrt[n]{a} = a^{1/n}$$

### Propiedades de las raíces

| Propiedad | Fórmula |
|-----------|---------|
| Producto | $\sqrt[n]{ab} = \sqrt[n]{a} \cdot \sqrt[n]{b}$ |
| Cociente | $\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}$ |
| Potencia | $\sqrt[n]{a^m} = a^{m/n}$ |
| Raíz de raíz | $\sqrt[m]{\sqrt[n]{a}} = \sqrt[mn]{a}$ |

### Racionalización

Eliminar raíces del denominador:

$$\frac{1}{\sqrt{a}} = \frac{\sqrt{a}}{a}$$

$$\frac{1}{\sqrt{a} + \sqrt{b}} = \frac{\sqrt{a} - \sqrt{b}}{a - b}$$

---

## 2.8 Razones y proporciones

### Razón

Una **razón** compara dos cantidades: $a : b$ o $\frac{a}{b}$.

**Ejemplo**: En una clase con 12 hombres y 18 mujeres, la razón hombres:mujeres es $12:18 = 2:3$.

### Proporción

Una **proporción** es la igualdad de dos razones:

$$\frac{a}{b} = \frac{c}{d} \quad \text{o} \quad a : b = c : d$$

**Propiedad fundamental**:
$$\frac{a}{b} = \frac{c}{d} \iff a \cdot d = b \cdot c$$

### Regla de tres simple

Para resolver proporciones con una incógnita:

$$\frac{a}{b} = \frac{c}{x} \implies x = \frac{b \cdot c}{a}$$

### Proporcionalidad directa

$y$ es **directamente proporcional** a $x$ si:
$$y = kx \quad \text{(}k \text{ constante de proporcionalidad)}$$

**Característica**: Si $x$ aumenta, $y$ aumenta en la misma proporción.

### Proporcionalidad inversa

$y$ es **inversamente proporcional** a $x$ si:
$$y = \frac{k}{x} \quad \text{o equivalentemente} \quad xy = k$$

**Característica**: Si $x$ aumenta, $y$ disminuye.

---

## 2.9 Fundamentos de Aritmética Superior

### Rol de la aritmética en aplicaciones avanzadas

La aritmética sustenta estructuras de mayor complejidad en:
- Diseño de algoritmos discretos y análisis de complejidad.
- Criptografía y codificación (factorización y congruencias).
- Análisis de señales y discretización del continuo.

### Fundamentación axiomática de $\mathbb{N}$ (Axiomas de Peano)

Sea $N$ un conjunto y $S: N \to N$ la [función](../../../glossary.md#funcion) sucesor. Existe un elemento distinguido $1 \in N$ [tal que](../../../glossary.md#tal-que):

1. **Existencia del elemento inicial:** $1 \in N$.
2. **Clausura bajo sucesión:** $\forall n \in N,\ S(n) \in N$.
3. **Inyectividad:** $S(n)=S(m) \Rightarrow n=m$.
4. **Elemento no sucesor:** $\nexists n \in N$ tal que $S(n)=1$.
5. **Inducción:** Si $A \subseteq N$ cumple $1 \in A$ y $n \in A \Rightarrow S(n) \in A$, entonces $A=N$.

### Principios fundamentales

- **Principio de inducción:** si $P(1)$ es verdadero y $P(k)\Rightarrow P(k+1)$ para todo $k\in N$, entonces $P(n)$ es verdadero para todo $n\in N$.
- **Principio de buen orden:** todo subconjunto no vacío de $N$ tiene elemento mínimo. Es equivalente al principio de inducción.

### Teorema Fundamental de la Aritmética (TFA) - Formal

> Todo entero $n > 1$ puede expresarse de manera **única** como producto de primos (salvo el orden de los factores).

**Forma canónica:** Todo $n>1$ puede escribirse como:
$$n=\prod_{i=1}^r p_i^{\alpha_i}$$
con $p_i$ primos distintos y $\alpha_i\in \mathbb{N}$.

**Esbozo de prueba:**
- *Existencia:* Por buen orden, si hubiera un $n>1$ sin factorización prima, el mínimo tal $n$ no sería primo y se escribiría $n=ab$ con $1<a,b<n$, contradiciendo la minimalidad.
- *Unicidad:* Por el Lema de Euclides (si $p\mid ab$ entonces $p\mid a$ o $p\mid b$), cancelando primos por inducción se obtiene igualdad.

### Propiedades formales de divisibilidad

Para $a,b \in \mathbb{N}$, $a$ divide a $b$ ($a\mid b$) si $\exists k \in \mathbb{N}$ tal que $b=a\,k$.

| Propiedad | Descripción |
|-----------|-------------|
| Reflexividad | $a\mid a$ |
| Transitividad | $a\mid b$ y $b\mid c \Rightarrow a\mid c$ |
| Antisimetría | $a\mid b$ y $b\mid a \Rightarrow a=b$ |
| Comparabilidad | Si $a\mid b$ y $a\neq b$, entonces $a<b$ |

### Definiciones formales de MCD y MCM

Dados $a,b>0$ con descomposiciones $a=\prod p_i^{\alpha_i}$, $b=\prod p_i^{\beta_i}$:

$$\gcd(a,b)=\prod p_i^{\min(\alpha_i,\beta_i)}$$

$$\text{mcm}(a,b)=\prod p_i^{\max(\alpha_i,\beta_i)}$$

**Criterio de divisibilidad por exponentes:** $a\mid b \iff \alpha_i \le \beta_i\ \forall i$.

---

## 2.10 Ejemplos Avanzados: Factorización, MCD y MCM

### Ejemplo 1: Factorización prima

- $84 = 2^2 \cdot 3 \cdot 7$ (dividir sucesivamente entre primos crecientes)
- $231 = 3 \cdot 7 \cdot 11$

### Ejemplo 2: Cálculo de MCD y MCM por exponentes

Para $a=84=2^2\cdot 3^1\cdot 7^1$ y $b=231=3^1\cdot 7^1\cdot 11^1$:

**MCD:** Tomar mínimos exponentes (completando con 0 donde no aparece el primo):
$$\gcd(84,231)=2^{\min(2,0)} \cdot 3^{\min(1,1)} \cdot 7^{\min(1,1)} \cdot 11^{\min(0,1)}=2^0 \cdot 3^1 \cdot 7^1 \cdot 11^0=21$$

**MCM:** Tomar máximos exponentes:
$$\text{mcm}(84,231)=2^{\max(2,0)} \cdot 3^{\max(1,1)} \cdot 7^{\max(1,1)} \cdot 11^{\max(0,1)}=2^2\cdot 3\cdot 7\cdot 11=924$$

**Verificación:** $84\cdot 231 = 19404$ y $21\cdot 924 = 19404$ ✓

### Ejemplo 3: Ilustración del Lema de Euclides

Si $p=7$ y queremos verificar si $7 \mid (84\cdot 25)$:
- Como $84=7\cdot 12$, entonces $7\mid 84$
- Se cumple: "si un primo divide a un producto, divide a al menos un factor"

---

## Resumen de fórmulas clave

| Concepto | Fórmula |
|----------|---------|
| Factorización prima | $n = p_1^{a_1} \cdot p_2^{a_2} \cdots p_k^{a_k}$ |
| Relación MCD-MCM | $\text{MCD}(a,b) \cdot \text{MCM}(a,b) = a \cdot b$ |
| Suma de fracciones | $\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$ |
| División de fracciones | $\frac{a}{b} \div \frac{c}{d} = \frac{ad}{bc}$ |
| Porcentaje | $x\% \text{ de } n = \frac{xn}{100}$ |
| Leyes de exponentes | $a^m \cdot a^n = a^{m+n}$, $(a^m)^n = a^{mn}$ |
| Raíz como potencia | $\sqrt[n]{a} = a^{1/n}$ |
| Proporción | $\frac{a}{b} = \frac{c}{d} \Leftrightarrow ad = bc$ |

---

<!--
IA: Teoría completa de aritmética.
Incluye [fundamentos](../../../glossary.md#fundamentos) axiomáticos (Peano) y TFA formal.
file_id: FUN-02-Teoria-Aritmetica
-->
