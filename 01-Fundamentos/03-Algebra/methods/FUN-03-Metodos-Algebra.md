<!--
::METADATA::
type: method
status: active
-->

# Métodos de Álgebra

> Guía completa de métodos algebraicos con algoritmos detallados, tablas de procedimientos y ejemplos paso a paso.

---

## Método 1: Simplificar Expresiones Algebraicas

**Cuándo Usar:** Para reducir expresiones combinando términos semejantes y aplicando propiedades.

**Definición:** Términos semejantes tienen exactamente las mismas variables con los mismos exponentes.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar términos semejantes | Mismas variables con mismos exponentes |
| 2 | Agrupar | Colocar términos semejantes juntos |
| 3 | Combinar | Sumar/restar coeficientes |
| 4 | Ordenar | Por grado descendente (opcional) |

### Ejemplo Detallado

**Problema:** Simplificar $3x^2y - 5xy^2 + 7x^2y + 2xy^2 - 4x^2y + xy^2$

---

**Paso 1: Identificar términos semejantes**

- Términos con $x^2y$: $3x^2y$, $7x^2y$, $-4x^2y$
- Términos con $xy^2$: $-5xy^2$, $2xy^2$, $xy^2$

---

**Paso 2: Agrupar**

$$= (3x^2y + 7x^2y - 4x^2y) + (-5xy^2 + 2xy^2 + xy^2)$$

---

**Paso 3: Combinar coeficientes**

$$= (3 + 7 - 4)x^2y + (-5 + 2 + 1)xy^2$$

$$= 6x^2y + (-2)xy^2$$

$$\boxed{6x^2y - 2xy^2}$$

---

## Método 2: Multiplicar Binomios (FOIL)

**Cuándo Usar:** Para expandir el producto de dos binomios.

**FOIL:** First, Outer, Inner, Last

### Algoritmo de Resolución

| Paso | Acción | Producto |
|------|--------|----------|
| F | First (Primeros) | $a \times c$ |
| O | Outer (Externos) | $a \times d$ |
| I | Inner (Internos) | $b \times c$ |
| L | Last (Últimos) | $b \times d$ |

### Fórmula

$$(a + b)(c + d) = ac + ad + bc + bd$$

### Ejemplo Detallado

**Problema:** Expandir $(3x - 5)(2x + 7)$

---

| Paso | Operación | Resultado |
|------|-----------|-----------|
| F | $3x \times 2x$ | $6x^2$ |
| O | $3x \times 7$ | $21x$ |
| I | $-5 \times 2x$ | $-10x$ |
| L | $-5 \times 7$ | $-35$ |

---

**Suma:** $6x^2 + 21x - 10x - 35 = 6x^2 + 11x - 35$

$$\boxed{(3x - 5)(2x + 7) = 6x^2 + 11x - 35}$$

---

### Productos Notables

| Nombre | Fórmula |
|--------|---------|
| Cuadrado de suma | $(a + b)^2 = a^2 + 2ab + b^2$ |
| Cuadrado de diferencia | $(a - b)^2 = a^2 - 2ab + b^2$ |
| Diferencia de cuadrados | $(a + b)(a - b) = a^2 - b^2$ |
| Cubo de suma | $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$ |
| Cubo de diferencia | $(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$ |
| Suma de cubos | $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$ |
| Diferencia de cubos | $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$ |

---

## Método 3: División Sintética (Ruffini)

**Cuándo Usar:** Para dividir un [polinomio](../../../glossary.md#polinomio) entre $(x - c)$ de manera eficiente.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Escribir coeficientes | En [orden](../../../glossary.md#orden) descendente de grados |
| 2 | Colocar raíz | $c$ si dividimos entre $(x - c)$ |
| 3 | Bajar primer coeficiente | Directamente |
| 4 | Multiplicar y sumar | $c \times$ resultado, sumar al siguiente |
| 5 | Repetir | Hasta terminar |
| 6 | Interpretar | Últimos valores son cociente y residuo |

### Ejemplo Detallado

**Problema:** Dividir $2x^4 - 3x^3 + 0x^2 - 5x + 7$ entre $(x - 2)$

---

**Paso 1:** Coeficientes: $[2, -3, 0, -5, 7]$, raíz $c = 2$

---

**Paso 2:** Aplicar Ruffini

```
    2  |  2   -3    0   -5    7
       |      4    2    4   -2
       |-------------------------
          2    1    2   -1    5
```

Proceso:
- Bajar $2$
- $2 \times 2 = 4$, luego $-3 + 4 = 1$
- $2 \times 1 = 2$, luego $0 + 2 = 2$
- $2 \times 2 = 4$, luego $-5 + 4 = -1$
- $2 \times (-1) = -2$, luego $7 + (-2) = 5$

---

**Paso 3:** Interpretar resultado

- Cociente: $2x^3 + x^2 + 2x - 1$
- Residuo: $5$

$$\frac{2x^4 - 3x^3 - 5x + 7}{x - 2} = 2x^3 + x^2 + 2x - 1 + \frac{5}{x - 2}$$

---

**Verificación:** Por el Teorema del Residuo, $P(2) = 5$

$$P(2) = 2(16) - 3(8) + 0 - 5(2) + 7 = 32 - 24 - 10 + 7 = 5 \checkmark$$

$$\boxed{\text{Cociente: } 2x^3 + x^2 + 2x - 1, \quad \text{Residuo: } 5}$$

---

## Método 4: Factorizar por Factor Común

**Cuándo Usar:** Cuando todos los términos comparten un factor común.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar [MCD](../../../glossary.md#mcd) | De coeficientes numéricos |
| 2 | Identificar factor variable | [Menor](../../../glossary.md#menor) exponente de cada variable |
| 3 | Extraer factor común | Escribir fuera del paréntesis |
| 4 | Dividir cada término | Lo que queda dentro del paréntesis |

### Ejemplo Detallado

**Problema:** [Factorizar](../../../glossary.md#factorizar) $18x^4y^3 - 24x^3y^5 + 30x^5y^2$

---

**Paso 1: MCD de coeficientes**

$$\text{MCD}(18, 24, 30) = 6$$

---

**Paso 2: Factor variable común**

- Para $x$: exponentes son 4, 3, 5 → mínimo es 3 → $x^3$
- Para $y$: exponentes son 3, 5, 2 → mínimo es 2 → $y^2$

---

**Paso 3: Factor común completo**

$$\text{Factor común} = 6x^3y^2$$

---

**Paso 4: Dividir cada término**

$$\frac{18x^4y^3}{6x^3y^2} = 3xy$$

$$\frac{-24x^3y^5}{6x^3y^2} = -4y^3$$

$$\frac{30x^5y^2}{6x^3y^2} = 5x^2$$

---

**Resultado:**

$$18x^4y^3 - 24x^3y^5 + 30x^5y^2 = 6x^3y^2(3xy - 4y^3 + 5x^2)$$

$$\boxed{6x^3y^2(3xy - 4y^3 + 5x^2)}$$

---

## Método 5: Factorizar Trinomio Cuadrado Perfecto

**Cuándo Usar:** Cuando el trinomio tiene la forma $a^2 \pm 2ab + b^2$.

### Criterio de Identificación

| Verificar | Condición |
|-----------|-----------|
| Primer término | Es cuadrado perfecto |
| Último término | Es cuadrado perfecto |
| Término medio | Es $2 \times \sqrt{\text{primero}} \times \sqrt{\text{último}}$ |

### Fórmulas

$$a^2 + 2ab + b^2 = (a + b)^2$$
$$a^2 - 2ab + b^2 = (a - b)^2$$

### Ejemplo Detallado

**Problema:** Factorizar $9x^2 - 30xy + 25y^2$

---

**Paso 1: Verificar primer término**

$$9x^2 = (3x)^2 \checkmark$$

---

**Paso 2: Verificar último término**

$$25y^2 = (5y)^2 \checkmark$$

---

**Paso 3: Verificar término medio**

$$2 \times 3x \times 5y = 30xy$$

El término medio es $-30xy$ (negativo) → usar $(a - b)^2$

---

**Resultado:**

$$9x^2 - 30xy + 25y^2 = (3x - 5y)^2$$

$$\boxed{(3x - 5y)^2}$$

---

## Método 6: Factorizar Trinomio $x^2 + bx + c$

**Cuándo Usar:** Trinomio cuadrático con coeficiente principal 1.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar | $b$ = suma, $c$ = producto |
| 2 | Buscar dos números | $p + q = b$ y $p \times q = c$ |
| 3 | Factorizar | $(x + p)(x + q)$ |

### Ejemplo Detallado

**Problema:** Factorizar $x^2 - 7x + 12$

---

**Paso 1: Identificar**

- $b = -7$ (suma de los números)
- $c = 12$ (producto de los números)

---

**Paso 2: Buscar $p$ y $q$**

| $p$ | $q$ | $p + q$ | $p \times q$ |
|-----|-----|---------|--------------|
| -1 | -12 | -13 | 12 |
| -2 | -6 | -8 | 12 |
| -3 | -4 | -7 ✓ | 12 ✓ |

---

**Paso 3: Factorizar**

$$x^2 - 7x + 12 = (x - 3)(x - 4)$$

---

**Verificación:**

$$(x - 3)(x - 4) = x^2 - 4x - 3x + 12 = x^2 - 7x + 12 \checkmark$$

$$\boxed{(x - 3)(x - 4)}$$

---

## Método 7: Factorizar Trinomio $ax^2 + bx + c$ (Método AC)

**Cuándo Usar:** Trinomio cuadrático con $a \neq 1$.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Calcular producto | $a \times c$ |
| 2 | Buscar factores | Dos números que sumen $b$ y multipliquen $ac$ |
| 3 | Reescribir | Descomponer término medio |
| 4 | Agrupar | Factor común en pares |
| 5 | Extraer | Factor común binomial |

### Ejemplo Detallado

**Problema:** Factorizar $6x^2 + 11x - 10$

---

**Paso 1: Producto $ac$**

$$a \times c = 6 \times (-10) = -60$$

---

**Paso 2: Buscar factores**

Necesitamos $p + q = 11$ y $p \times q = -60$

| $p$ | $q$ | $p + q$ | $p \times q$ |
|-----|-----|---------|--------------|
| 15 | -4 | 11 ✓ | -60 ✓ |

---

**Paso 3: Reescribir el término medio**

$$6x^2 + 11x - 10 = 6x^2 + 15x - 4x - 10$$

---

**Paso 4: Agrupar y factorizar**

$$= (6x^2 + 15x) + (-4x - 10)$$
$$= 3x(2x + 5) - 2(2x + 5)$$

---

**Paso 5: Extraer factor común**

$$= (2x + 5)(3x - 2)$$

---

**Verificación:**

$$(2x + 5)(3x - 2) = 6x^2 - 4x + 15x - 10 = 6x^2 + 11x - 10 \checkmark$$

$$\boxed{(2x + 5)(3x - 2)}$$

---

## Método 8: Factorizar Diferencia de Cuadrados

**Cuándo Usar:** Expresión de la forma $a^2 - b^2$.

### Fórmula

$$a^2 - b^2 = (a + b)(a - b)$$

### Ejemplo Detallado

**Problema:** Factorizar $16x^4 - 81y^4$

---

**Paso 1: Reconocer como diferencia de cuadrados**

$$16x^4 - 81y^4 = (4x^2)^2 - (9y^2)^2$$

---

**Paso 2: Aplicar fórmula**

$$= (4x^2 + 9y^2)(4x^2 - 9y^2)$$

---

**Paso 3: Factorizar nuevamente (si es posible)**

$4x^2 + 9y^2$ no es factorizable en reales (suma de cuadrados)

$4x^2 - 9y^2 = (2x)^2 - (3y)^2 = (2x + 3y)(2x - 3y)$

---

**Resultado final:**

$$\boxed{(4x^2 + 9y^2)(2x + 3y)(2x - 3y)}$$

---

## Método 9: Factorizar Suma y Diferencia de Cubos

**Cuándo Usar:** Expresiones de la forma $a^3 \pm b^3$.

### Fórmulas

$$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$$
$$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$$

### Regla Mnemónica

- **SOAP:** Same (mismo signo), Opposite (opuesto), Always Positive (siempre positivo)
- Primer factor: $(a \pm b)$ con el mismo signo
- Segundo factor: $a^2 \mp ab + b^2$ (signo opuesto en $ab$, siempre $+b^2$)

### Ejemplo Detallado

**Problema:** Factorizar $27x^3 + 125y^6$

---

**Paso 1: Expresar como cubos**

$$27x^3 = (3x)^3, \quad 125y^6 = (5y^2)^3$$

---

**Paso 2: Identificar $a = 3x$, $b = 5y^2$**

---

**Paso 3: Aplicar fórmula de suma de cubos**

$$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$$

$$= (3x + 5y^2)((3x)^2 - (3x)(5y^2) + (5y^2)^2)$$

$$= (3x + 5y^2)(9x^2 - 15xy^2 + 25y^4)$$

$$\boxed{(3x + 5y^2)(9x^2 - 15xy^2 + 25y^4)}$$

---

## Método 10: Resolver Ecuaciones Lineales

**Cuándo Usar:** Ecuaciones de primer grado con una incógnita.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Eliminar paréntesis | Distribuir si es [necesario](../../../glossary.md#necesario) |
| 2 | Eliminar fracciones | Multiplicar por [MCM](../../../glossary.md#mcm) |
| 3 | Agrupar términos | Variables a un lado, constantes al otro |
| 4 | Combinar | Términos semejantes |
| 5 | Despejar | Dividir por coeficiente |
| 6 | Verificar | Sustituir en ecuación original |

### Ejemplo Detallado

**Problema:** Resolver $\frac{2x - 1}{3} - \frac{x + 2}{4} = \frac{x - 5}{6} + 1$

---

**Paso 1: Calcular MCM de denominadores**

$$\text{MCM}(3, 4, 6) = 12$$

---

**Paso 2: Multiplicar toda la ecuación por 12**

$$12 \cdot \frac{2x - 1}{3} - 12 \cdot \frac{x + 2}{4} = 12 \cdot \frac{x - 5}{6} + 12 \cdot 1$$

$$4(2x - 1) - 3(x + 2) = 2(x - 5) + 12$$

---

**Paso 3: Distribuir**

$$8x - 4 - 3x - 6 = 2x - 10 + 12$$

---

**Paso 4: Simplificar cada lado**

$$5x - 10 = 2x + 2$$

---

**Paso 5: Agrupar variables y constantes**

$$5x - 2x = 2 + 10$$
$$3x = 12$$

---

**Paso 6: Despejar**

$$x = 4$$

---

**Verificación:**

$$\frac{2(4) - 1}{3} - \frac{4 + 2}{4} = \frac{4 - 5}{6} + 1$$

$$\frac{7}{3} - \frac{6}{4} = \frac{-1}{6} + 1$$

$$\frac{28}{12} - \frac{18}{12} = \frac{-2}{12} + \frac{12}{12}$$

$$\frac{10}{12} = \frac{10}{12} \checkmark$$

$$\boxed{x = 4}$$

---

## Método 11: Resolver Ecuaciones Cuadráticas

**Cuándo Usar:** Ecuaciones de la forma $ax^2 + bx + c = 0$.

### Métodos Disponibles

| Método | Cuándo Usar |
|--------|-------------|
| [Factorización](../../../glossary.md#factorización) | Si es fácilmente factorizable |
| Completar cuadrado | Para derivar fórmula general |
| Fórmula general | Siempre funciona |

### Fórmula General (Bhaskara)

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

### Discriminante

| Valor de $\Delta = b^2 - 4ac$ | Naturaleza de las raíces |
|-------------------------------|--------------------------|
| $\Delta > 0$ | Dos raíces reales distintas |
| $\Delta = 0$ | Una raíz real doble |
| $\Delta < 0$ | Dos raíces complejas conjugadas |

### Ejemplo Detallado

**Problema:** Resolver $3x^2 - 10x + 3 = 0$

---

**Paso 1: Identificar coeficientes**

$$a = 3, \quad b = -10, \quad c = 3$$

---

**Paso 2: Calcular discriminante**

$$\Delta = b^2 - 4ac = (-10)^2 - 4(3)(3) = 100 - 36 = 64$$

Como $\Delta > 0$, hay dos raíces reales distintas.

---

**Paso 3: Aplicar fórmula**

$$x = \frac{-(-10) \pm \sqrt{64}}{2(3)} = \frac{10 \pm 8}{6}$$

---

**Paso 4: Calcular raíces**

$$x_1 = \frac{10 + 8}{6} = \frac{18}{6} = 3$$

$$x_2 = \frac{10 - 8}{6} = \frac{2}{6} = \frac{1}{3}$$

---

**Verificación con relaciones de Vieta:**

- Suma: $x_1 + x_2 = 3 + \frac{1}{3} = \frac{10}{3} = -\frac{b}{a} = \frac{10}{3}$ ✓
- Producto: $x_1 \cdot x_2 = 3 \cdot \frac{1}{3} = 1 = \frac{c}{a} = \frac{3}{3} = 1$ ✓

$$\boxed{x_1 = 3, \quad x_2 = \frac{1}{3}}$$

---

## Método 12: Completar el Cuadrado

**Cuándo Usar:** Para resolver cuadráticas, derivar fórmula del vértice, o simplificar expresiones.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Asegurar $a = 1$ | Dividir toda la ecuación por $a$ |
| 2 | Mover constante | Al lado derecho |
| 3 | Calcular $\left(\frac{b}{2}\right)^2$ | Mitad del coeficiente lineal, al cuadrado |
| 4 | Sumar a ambos lados | Para mantener igualdad |
| 5 | Factorizar | Como cuadrado perfecto |
| 6 | Resolver | Aplicar raíz cuadrada |

### Ejemplo Detallado

**Problema:** Resolver $2x^2 + 12x - 7 = 0$ completando el cuadrado.

---

**Paso 1: Dividir por $a = 2$**

$$x^2 + 6x - \frac{7}{2} = 0$$

---

**Paso 2: Mover constante**

$$x^2 + 6x = \frac{7}{2}$$

---

**Paso 3: Calcular $\left(\frac{b}{2}\right)^2$**

$$\left(\frac{6}{2}\right)^2 = 3^2 = 9$$

---

**Paso 4: Sumar 9 a ambos lados**

$$x^2 + 6x + 9 = \frac{7}{2} + 9 = \frac{7}{2} + \frac{18}{2} = \frac{25}{2}$$

---

**Paso 5: Factorizar**

$$(x + 3)^2 = \frac{25}{2}$$

---

**Paso 6: Aplicar raíz cuadrada**

$$x + 3 = \pm\sqrt{\frac{25}{2}} = \pm\frac{5}{\sqrt{2}} = \pm\frac{5\sqrt{2}}{2}$$

$$x = -3 \pm \frac{5\sqrt{2}}{2}$$

$$\boxed{x = -3 + \frac{5\sqrt{2}}{2} \approx 0.536, \quad x = -3 - \frac{5\sqrt{2}}{2} \approx -6.536}$$

---

## Método 13: Resolver Sistemas de Ecuaciones Lineales 2×2

**Cuándo Usar:** Dos ecuaciones con dos incógnitas.

### Métodos Disponibles

| Método | Cuándo Usar |
|--------|-------------|
| [Sustitución](../../../glossary.md#sustitución) | Una variable fácil de despejar |
| Eliminación | Coeficientes permiten fácil eliminación |
| Igualación | Cuando ambas ecuaciones despejan la misma variable |

### Método de Eliminación

**Problema:** Resolver el sistema:
$$\begin{cases} 3x + 4y = 18 \\ 5x - 2y = 4 \end{cases}$$

---

**Paso 1: Preparar para eliminar $y$**

Multiplicar la segunda ecuación por 2:

$$\begin{cases} 3x + 4y = 18 \\ 10x - 4y = 8 \end{cases}$$

---

**Paso 2: Sumar las ecuaciones**

$$3x + 10x + 4y - 4y = 18 + 8$$
$$13x = 26$$
$$x = 2$$

---

**Paso 3: Sustituir en la primera ecuación**

$$3(2) + 4y = 18$$
$$6 + 4y = 18$$
$$4y = 12$$
$$y = 3$$

---

**Verificación:**

Primera: $3(2) + 4(3) = 6 + 12 = 18$ ✓
Segunda: $5(2) - 2(3) = 10 - 6 = 4$ ✓

$$\boxed{(x, y) = (2, 3)}$$

---

## Método 14: Resolver Sistemas 3×3 (Método de Gauss)

**Cuándo Usar:** Tres ecuaciones con tres incógnitas.

### Ejemplo Detallado

**Problema:** Resolver:
$$\begin{cases} x + y + z = 6 \\ 2x - y + z = 3 \\ x + 2y - z = 2 \end{cases}$$

---

**Paso 1: [Matriz](../../../glossary.md#matriz) aumentada**

$$\left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 2 & -1 & 1 & 3 \\ 1 & 2 & -1 & 2 \end{array}\right]$$

---

**Paso 2: $F_2 \to F_2 - 2F_1$ y $F_3 \to F_3 - F_1$**

$$\left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & -3 & -1 & -9 \\ 0 & 1 & -2 & -4 \end{array}\right]$$

---

**Paso 3: $F_3 \to 3F_3 + F_2$**

$$\left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & -3 & -1 & -9 \\ 0 & 0 & -7 & -21 \end{array}\right]$$

---

**Paso 4: Sustitución hacia atrás**

De la tercera fila: $-7z = -21 \Rightarrow z = 3$

De la segunda fila: $-3y - 1(3) = -9 \Rightarrow -3y = -6 \Rightarrow y = 2$

De la primera fila: $x + 2 + 3 = 6 \Rightarrow x = 1$

---

**Verificación:**

- $1 + 2 + 3 = 6$ ✓
- $2(1) - 2 + 3 = 3$ ✓
- $1 + 2(2) - 3 = 2$ ✓

$$\boxed{(x, y, z) = (1, 2, 3)}$$

---

## Método 15: Descomponer en Fracciones Parciales

**Cuándo Usar:** Para integración de funciones racionales o transformadas de Laplace.

### Casos

| Tipo de Factor | Forma de Descomposición |
|----------------|------------------------|
| Lineal simple $(ax + b)$ | $\frac{A}{ax + b}$ |
| Lineal repetido $(ax + b)^n$ | $\frac{A_1}{ax + b} + \frac{A_2}{(ax + b)^2} + \cdots$ |
| Cuadrático irreducible | $\frac{Ax + B}{ax^2 + bx + c}$ |

### Ejemplo Detallado

**Problema:** Descomponer $\frac{5x^2 - 4x + 7}{(x - 1)(x^2 + 2)}$

---

**Paso 1: Plantear la forma**

$$\frac{5x^2 - 4x + 7}{(x - 1)(x^2 + 2)} = \frac{A}{x - 1} + \frac{Bx + C}{x^2 + 2}$$

---

**Paso 2: Multiplicar por el denominador común**

$$5x^2 - 4x + 7 = A(x^2 + 2) + (Bx + C)(x - 1)$$

---

**Paso 3: Método de valores convenientes**

Para $x = 1$:
$$5(1) - 4(1) + 7 = A(1 + 2) + 0$$
$$8 = 3A \Rightarrow A = \frac{8}{3}$$

---

**Paso 4: Expandir y comparar coeficientes**

$$5x^2 - 4x + 7 = Ax^2 + 2A + Bx^2 - Bx + Cx - C$$
$$= (A + B)x^2 + (-B + C)x + (2A - C)$$

Comparando:
- $x^2$: $A + B = 5 \Rightarrow B = 5 - \frac{8}{3} = \frac{7}{3}$
- $x^0$: $2A - C = 7 \Rightarrow C = 2(\frac{8}{3}) - 7 = \frac{16 - 21}{3} = -\frac{5}{3}$

Verificación con $x^1$: $-B + C = -\frac{7}{3} - \frac{5}{3} = -4$ ✓

---

**Resultado:**

$$\boxed{\frac{5x^2 - 4x + 7}{(x - 1)(x^2 + 2)} = \frac{8/3}{x - 1} + \frac{\frac{7}{3}x - \frac{5}{3}}{x^2 + 2}}$$

---

## Resumen de Fórmulas

| Concepto | Fórmula |
|----------|---------|
| FOIL | $(a+b)(c+d) = ac + ad + bc + bd$ |
| Cuadrado de binomio | $(a \pm b)^2 = a^2 \pm 2ab + b^2$ |
| Diferencia de cuadrados | $a^2 - b^2 = (a+b)(a-b)$ |
| Suma de cubos | $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$ |
| Diferencia de cubos | $a^3 - b^3 = (a-b)(a^2 + ab + b^2)$ |
| Fórmula cuadrática | $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ |
| Vieta (suma) | $x_1 + x_2 = -\frac{b}{a}$ |
| Vieta (producto) | $x_1 \cdot x_2 = \frac{c}{a}$ |

---

## Errores Comunes

| Error | Corrección |
|-------|------------|
| $(a + b)^2 = a^2 + b^2$ | $(a + b)^2 = a^2 + 2ab + b^2$ |
| $\sqrt{a^2 + b^2} = a + b$ | No se puede simplificar así |
| $\frac{a + b}{c + d} = \frac{a}{c} + \frac{b}{d}$ | No es válido |
| Olvidar $\pm$ en la fórmula cuadrática | Siempre hay dos soluciones (pueden coincidir) |
| División por cero al simplificar | Verificar que el factor cancelado no sea cero |
| Signo incorrecto en Ruffini | Si dividimos entre $(x - c)$, usar $c$ positivo |
