<!--
::METADATA::
type: method
status: active
-->

# Métodos de Aritmética

> Guía completa de métodos con algoritmos detallados, tablas de procedimientos y ejemplos paso a paso.

---

## Método 1: Aplicar Jerarquía de Operaciones (PEMDAS/BODMAS)

**Cuándo Usar:** Para evaluar correctamente cualquier expresión aritmética que contenga múltiples operaciones.

**Regla:** La jerarquía evita ambigüedad en el orden de las operaciones.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | **P**aréntesis | Resolver de adentro hacia afuera |
| 2 | **E**xponentes | Potencias y raíces |
| 3 | **M**ultiplicación/**D**ivisión | De izquierda a derecha |
| 4 | **A**dición/**S**ustracción | De izquierda a derecha |

### Ejemplo Detallado

**Problema:** Evaluar $48 \div 2(9 + 3) - 5^2 + 18 \div 3 \times 2$

---

**Paso 1: Resolver paréntesis**

$$48 \div 2(9 + 3) - 5^2 + 18 \div 3 \times 2$$
$$= 48 \div 2(12) - 5^2 + 18 \div 3 \times 2$$

---

**Paso 2: Resolver exponentes**

$$= 48 \div 2(12) - 25 + 18 \div 3 \times 2$$

---

**Paso 3: Multiplicación y División (izquierda a derecha)**

$$= 24(12) - 25 + 6 \times 2$$
$$= 288 - 25 + 12$$

---

**Paso 4: Suma y Resta (izquierda a derecha)**

$$= 263 + 12 = 275$$

$$\boxed{275}$$

---

### Ejemplo con Fracciones y Paréntesis Anidados

**Problema:** Evaluar $\frac{3 + [4 \times (6 - 2)]}{2^3 - 1} + 5$

---

**Paso 1: Paréntesis más internos**

$$= \frac{3 + [4 \times 4]}{2^3 - 1} + 5$$

---

**Paso 2: Corchetes**

$$= \frac{3 + 16}{2^3 - 1} + 5 = \frac{19}{2^3 - 1} + 5$$

---

**Paso 3: Exponentes**

$$= \frac{19}{8 - 1} + 5 = \frac{19}{7} + 5$$

---

**Paso 4: División y suma**

$$= \frac{19}{7} + \frac{35}{7} = \frac{54}{7}$$

$$\boxed{\frac{54}{7} \approx 7.71}$$

---

## Método 2: Descomponer en Factores Primos

**Cuándo Usar:** Base fundamental para calcular MCD, MCM, simplificar fracciones y raíces.

**Definición:** Todo número entero mayor que 1 puede expresarse como producto de números primos de manera única (Teorema Fundamental de la Aritmética).

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Dividir por el menor primo | Comenzar por 2 |
| 2 | Continuar dividiendo | Usar el mismo primo mientras sea posible |
| 3 | Cambiar de primo | Cuando no divida, probar el siguiente primo |
| 4 | Terminar | Cuando el cociente sea 1 |
| 5 | Escribir factorización | Producto de primos con exponentes |

### Ejemplo Detallado

**Problema:** Factorizar 2520 en primos.

---

| Cociente | Primo Divisor | Proceso |
|----------|---------------|---------|
| 2520 | 2 | $2520 \div 2 = 1260$ |
| 1260 | 2 | $1260 \div 2 = 630$ |
| 630 | 2 | $630 \div 2 = 315$ |
| 315 | 3 | $315 \div 3 = 105$ |
| 105 | 3 | $105 \div 3 = 35$ |
| 35 | 5 | $35 \div 5 = 7$ |
| 7 | 7 | $7 \div 7 = 1$ |

---

**Resultado:**

$$2520 = 2^3 \times 3^2 \times 5 \times 7$$

---

**Verificación:**

$$2^3 \times 3^2 \times 5 \times 7 = 8 \times 9 \times 5 \times 7 = 72 \times 35 = 2520 \checkmark$$

$$\boxed{2520 = 2^3 \times 3^2 \times 5 \times 7}$$

---

## Método 3: Calcular MCD por Factorización

**Cuándo Usar:** Para simplificar fracciones al máximo o encontrar el mayor divisor común de varios números.

**Definición:** El MCD es el mayor número que divide exactamente a todos los números dados.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Factorizar | Descomponer cada número en primos |
| 2 | Identificar comunes | Listar factores que aparecen en TODOS |
| 3 | Tomar menor exponente | Para cada factor común |
| 4 | Multiplicar | Producto de factores seleccionados |

### Ejemplo Detallado

**Problema:** Calcular $\text{MCD}(168, 252, 420)$

---

**Paso 1: Factorizar cada número**

| Número | Factorización |
|--------|---------------|
| 168 | $2^3 \times 3 \times 7$ |
| 252 | $2^2 \times 3^2 \times 7$ |
| 420 | $2^2 \times 3 \times 5 \times 7$ |

---

**Paso 2: Identificar factores comunes**

Aparecen en los tres: $2$, $3$, $7$

---

**Paso 3: Tomar menor exponente de cada uno**

| Factor | Exponentes | Menor |
|--------|------------|-------|
| 2 | 3, 2, 2 | 2 |
| 3 | 1, 2, 1 | 1 |
| 7 | 1, 1, 1 | 1 |

---

**Paso 4: Multiplicar**

$$\text{MCD} = 2^2 \times 3^1 \times 7^1 = 4 \times 3 \times 7 = 84$$

---

**Verificación:**

$$168 \div 84 = 2, \quad 252 \div 84 = 3, \quad 420 \div 84 = 5 \checkmark$$

$$\boxed{\text{MCD}(168, 252, 420) = 84}$$

---

## Método 4: Calcular MCD por Algoritmo de Euclides

**Cuándo Usar:** Más eficiente que factorización para números grandes.

**Fundamento:** $\text{MCD}(a, b) = \text{MCD}(b, a \mod b)$ hasta que el residuo sea 0.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Ordenar | Colocar mayor primero |
| 2 | Dividir | $a = bq + r$ |
| 3 | Reemplazar | $(a, b) \to (b, r)$ |
| 4 | Repetir | Hasta que $r = 0$ |
| 5 | Concluir | MCD = último divisor no nulo |

### Ejemplo Detallado

**Problema:** Calcular $\text{MCD}(1071, 462)$ por Euclides.

---

| División | Cálculo | Residuo |
|----------|---------|---------|
| $1071 \div 462$ | $1071 = 462 \times 2 + 147$ | $r = 147$ |
| $462 \div 147$ | $462 = 147 \times 3 + 21$ | $r = 21$ |
| $147 \div 21$ | $147 = 21 \times 7 + 0$ | $r = 0$ |

---

El último divisor no nulo es **21**.

---

**Verificación:**

$$1071 = 21 \times 51, \quad 462 = 21 \times 22 \checkmark$$

$$\boxed{\text{MCD}(1071, 462) = 21}$$

---

### Euclides Extendido (Identidad de Bézout)

**Objetivo:** Encontrar $x, y$ tales que $ax + by = \text{MCD}(a, b)$

**Problema:** Expresar $\text{MCD}(1071, 462) = 21$ como combinación lineal.

**Método de sustitución hacia atrás:**

De la tabla:
- $21 = 462 - 147 \times 3$
- $147 = 1071 - 462 \times 2$

Sustituyendo:
$$21 = 462 - (1071 - 462 \times 2) \times 3$$
$$= 462 - 1071 \times 3 + 462 \times 6$$
$$= 462 \times 7 - 1071 \times 3$$

$$\boxed{21 = 462(7) + 1071(-3)}$$

---

## Método 5: Calcular MCM por Factorización

**Cuándo Usar:** Para encontrar denominadores comunes en sumas de fracciones, problemas de ciclos.

**Definición:** El MCM es el menor número que es múltiplo de todos los números dados.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Factorizar | Descomponer cada número en primos |
| 2 | Listar todos los factores | Los que aparecen en CUALQUIERA |
| 3 | Tomar mayor exponente | Para cada factor |
| 4 | Multiplicar | Producto de factores seleccionados |

### Relación MCD-MCM

$$\text{MCD}(a, b) \times \text{MCM}(a, b) = a \times b$$

### Ejemplo Detallado

**Problema:** Calcular $\text{MCM}(24, 36, 54)$

---

**Paso 1: Factorizar**

| Número | Factorización |
|--------|---------------|
| 24 | $2^3 \times 3$ |
| 36 | $2^2 \times 3^2$ |
| 54 | $2 \times 3^3$ |

---

**Paso 2: Listar todos los factores**

Factores presentes: $2$, $3$

---

**Paso 3: Tomar mayor exponente**

| Factor | Exponentes | Mayor |
|--------|------------|-------|
| 2 | 3, 2, 1 | 3 |
| 3 | 1, 2, 3 | 3 |

---

**Paso 4: Multiplicar**

$$\text{MCM} = 2^3 \times 3^3 = 8 \times 27 = 216$$

---

**Verificación:**

$$216 \div 24 = 9, \quad 216 \div 36 = 6, \quad 216 \div 54 = 4 \checkmark$$

$$\boxed{\text{MCM}(24, 36, 54) = 216}$$

---

## Método 6: Sumar y Restar Fracciones

**Cuándo Usar:** Cuando las fracciones tienen denominadores diferentes.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Calcular MCM | De los denominadores |
| 2 | Amplificar | Cada fracción al denominador común |
| 3 | Operar | Sumar o restar numeradores |
| 4 | Simplificar | Dividir por MCD si es posible |

### Ejemplo Detallado

**Problema:** Calcular $\frac{5}{12} + \frac{7}{18} - \frac{1}{8}$

---

**Paso 1: Calcular MCM de denominadores**

$$12 = 2^2 \times 3, \quad 18 = 2 \times 3^2, \quad 8 = 2^3$$

$$\text{MCM} = 2^3 \times 3^2 = 8 \times 9 = 72$$

---

**Paso 2: Amplificar cada fracción**

$$\frac{5}{12} = \frac{5 \times 6}{72} = \frac{30}{72}$$

$$\frac{7}{18} = \frac{7 \times 4}{72} = \frac{28}{72}$$

$$\frac{1}{8} = \frac{1 \times 9}{72} = \frac{9}{72}$$

---

**Paso 3: Operar**

$$\frac{30}{72} + \frac{28}{72} - \frac{9}{72} = \frac{30 + 28 - 9}{72} = \frac{49}{72}$$

---

**Paso 4: Verificar si se puede simplificar**

$\text{MCD}(49, 72) = 1$ (49 = 7², 72 = 2³×3²), no se simplifica.

$$\boxed{\frac{5}{12} + \frac{7}{18} - \frac{1}{8} = \frac{49}{72}}$$

---

**Verificación decimal:**

$$\frac{5}{12} \approx 0.417, \quad \frac{7}{18} \approx 0.389, \quad \frac{1}{8} = 0.125$$

$$0.417 + 0.389 - 0.125 = 0.681$$

$$\frac{49}{72} \approx 0.681 \checkmark$$

---

## Método 7: Multiplicar y Dividir Fracciones

**Cuándo Usar:** Operaciones directas con fracciones.

### Fórmulas

**Multiplicación:**
$$\frac{a}{b} \times \frac{c}{d} = \frac{a \times c}{b \times d}$$

**División:**
$$\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c} = \frac{a \times d}{b \times c}$$

### Algoritmo con Simplificación Cruzada

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Simplificar cruzado | Dividir numerador de una con denominador de otra |
| 2 | Multiplicar | Numeradores y denominadores |
| 3 | Simplificar | Si aún es posible |

### Ejemplo Detallado

**Problema:** Calcular $\frac{15}{28} \times \frac{21}{45}$

---

**Paso 1: Simplificación cruzada**

- $\text{MCD}(15, 45) = 15$: dividimos $15 \div 15 = 1$, $45 \div 15 = 3$
- $\text{MCD}(21, 28) = 7$: dividimos $21 \div 7 = 3$, $28 \div 7 = 4$

$$\frac{15}{28} \times \frac{21}{45} = \frac{1}{4} \times \frac{3}{3} = \frac{1 \times 3}{4 \times 3} = \frac{3}{12} = \frac{1}{4}$$

---

**Verificación directa:**

$$\frac{15 \times 21}{28 \times 45} = \frac{315}{1260} = \frac{315 \div 315}{1260 \div 315} = \frac{1}{4} \checkmark$$

$$\boxed{\frac{15}{28} \times \frac{21}{45} = \frac{1}{4}}$$

---

### Ejemplo de División

**Problema:** Calcular $\frac{8}{15} \div \frac{12}{25}$

---

**Paso 1: Invertir y multiplicar**

$$\frac{8}{15} \div \frac{12}{25} = \frac{8}{15} \times \frac{25}{12}$$

---

**Paso 2: Simplificación cruzada**

- $\text{MCD}(8, 12) = 4$: $8 \div 4 = 2$, $12 \div 4 = 3$
- $\text{MCD}(25, 15) = 5$: $25 \div 5 = 5$, $15 \div 5 = 3$

$$= \frac{2}{3} \times \frac{5}{3} = \frac{10}{9}$$

$$\boxed{\frac{8}{15} \div \frac{12}{25} = \frac{10}{9} = 1\frac{1}{9}}$$

---

## Método 8: Convertir Decimal Periódico a Fracción

**Cuándo Usar:** Para expresar decimales repetitivos como fracciones exactas.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Definir variable | $x =$ decimal periódico |
| 2 | Multiplicar | Por $10^n$ donde $n$ = longitud del período |
| 3 | Restar | Ecuación multiplicada menos original |
| 4 | Despejar | Resolver para $x$ |
| 5 | Simplificar | Reducir la fracción |

### Ejemplo 1: Período Puro

**Problema:** Convertir $0.\overline{142857}$ a fracción.

---

**Paso 1:** Sea $x = 0.142857142857...$

**Paso 2:** Período tiene 6 dígitos, multiplicar por $10^6$:
$$1000000x = 142857.142857...$$

**Paso 3:** Restar:
$$1000000x - x = 142857$$
$$999999x = 142857$$

**Paso 4:** Despejar:
$$x = \frac{142857}{999999}$$

**Paso 5:** Simplificar (MCD = 142857):
$$x = \frac{142857 \div 142857}{999999 \div 142857} = \frac{1}{7}$$

$$\boxed{0.\overline{142857} = \frac{1}{7}}$$

---

### Ejemplo 2: Período Mixto (Anteperíodo + Período)

**Problema:** Convertir $0.8\overline{3}$ a fracción.

---

**Paso 1:** $x = 0.8333...$

**Paso 2:** Multiplicar por 10 (para mover anteperíodo):
$$10x = 8.333...$$

Multiplicar por 100:
$$100x = 83.333...$$

**Paso 3:** Restar:
$$100x - 10x = 83.333... - 8.333...$$
$$90x = 75$$

**Paso 4:** Despejar:
$$x = \frac{75}{90} = \frac{5}{6}$$

$$\boxed{0.8\overline{3} = \frac{5}{6}}$$

---

### Fórmula General

Para $0.\underbrace{a_1a_2...a_k}_{\text{anteperíodo}}\overline{\underbrace{b_1b_2...b_n}_{\text{período}}}$:

$$x = \frac{(\text{todo}) - (\text{anteperíodo})}{\underbrace{99...9}_{n}\underbrace{00...0}_{k}}$$

---

## Método 9: Calcular Porcentajes

**Cuándo Usar:** Incrementos, descuentos, comparaciones porcentuales.

### Fórmulas Esenciales

| Concepto | Fórmula |
|----------|---------|
| Porcentaje de un número | $\frac{p}{100} \times N$ |
| Incremento porcentual | $V_f = V_i \times (1 + \frac{p}{100})$ |
| Decremento porcentual | $V_f = V_i \times (1 - \frac{p}{100})$ |
| Cambio porcentual | $\frac{V_f - V_i}{V_i} \times 100\%$ |
| Hallar el total | $V_i = \frac{V_f}{1 \pm \frac{p}{100}}$ |

### Ejemplo 1: Incrementos Sucesivos

**Problema:** Un artículo de \$200 aumenta 15% y luego 20%. ¿Precio final?

---

**Paso 1:** Primer incremento
$$V_1 = 200 \times 1.15 = 230$$

**Paso 2:** Segundo incremento
$$V_f = 230 \times 1.20 = 276$$

---

**Método alternativo (factor combinado):**
$$V_f = 200 \times 1.15 \times 1.20 = 200 \times 1.38 = 276$$

**Nota:** El incremento total NO es 35%, sino:
$$\frac{276 - 200}{200} \times 100\% = 38\%$$

$$\boxed{V_f = \$276 \text{ (incremento real: 38\%)}}$$

---

### Ejemplo 2: Descuento sobre Descuento

**Problema:** Un producto de \$500 tiene 20% de descuento y luego 10% adicional. ¿Precio final?

---

$$V_f = 500 \times 0.80 \times 0.90 = 500 \times 0.72 = 360$$

**Descuento total:**
$$\frac{500 - 360}{500} \times 100\% = 28\%$$

$$\boxed{V_f = \$360 \text{ (descuento real: 28\%)}}$$

---

### Ejemplo 3: Encontrar el Valor Original

**Problema:** Después de un aumento del 25%, un artículo cuesta \$150. ¿Cuál era el precio original?

---

$$V_i = \frac{V_f}{1.25} = \frac{150}{1.25} = 120$$

**Verificación:** $120 \times 1.25 = 150$ ✓

$$\boxed{V_i = \$120}$$

---

## Método 10: Simplificar Expresiones con Exponentes

**Cuándo Usar:** Para combinar y reducir expresiones con potencias.

### Leyes de Exponentes

| Ley | Fórmula |
|-----|---------|
| Producto de potencias | $a^m \times a^n = a^{m+n}$ |
| Cociente de potencias | $\frac{a^m}{a^n} = a^{m-n}$ |
| Potencia de potencia | $(a^m)^n = a^{mn}$ |
| Potencia de producto | $(ab)^n = a^n b^n$ |
| Potencia de cociente | $\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$ |
| Exponente cero | $a^0 = 1$ (si $a \neq 0$) |
| Exponente negativo | $a^{-n} = \frac{1}{a^n}$ |
| Exponente fraccionario | $a^{m/n} = \sqrt[n]{a^m}$ |

### Ejemplo Detallado

**Problema:** Simplificar $\frac{12x^5 y^{-2} z^3}{4x^{-1} y^4 z^3} \times \frac{2x^2 y^3}{6x^4 y^{-3}}$

---

**Paso 1: Simplificar primera fracción**

$$\frac{12x^5 y^{-2} z^3}{4x^{-1} y^4 z^3} = \frac{12}{4} \cdot x^{5-(-1)} \cdot y^{-2-4} \cdot z^{3-3}$$

$$= 3 \cdot x^6 \cdot y^{-6} \cdot z^0 = 3x^6 y^{-6}$$

---

**Paso 2: Simplificar segunda fracción**

$$\frac{2x^2 y^3}{6x^4 y^{-3}} = \frac{2}{6} \cdot x^{2-4} \cdot y^{3-(-3)}$$

$$= \frac{1}{3} \cdot x^{-2} \cdot y^6$$

---

**Paso 3: Multiplicar resultados**

$$3x^6 y^{-6} \times \frac{1}{3} x^{-2} y^6 = \frac{3}{3} \cdot x^{6-2} \cdot y^{-6+6}$$

$$= 1 \cdot x^4 \cdot y^0 = x^4$$

$$\boxed{\frac{12x^5 y^{-2} z^3}{4x^{-1} y^4 z^3} \times \frac{2x^2 y^3}{6x^4 y^{-3}} = x^4}$$

---

## Método 11: Simplificar Radicales

**Cuándo Usar:** Para expresar raíces en su forma más simple.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Factorizar | El radicando en factores primos |
| 2 | Identificar | Grupos del tamaño del índice |
| 3 | Extraer | Un factor por cada grupo completo |
| 4 | Dejar dentro | Factores que no forman grupo |

### Ejemplo Detallado

**Problema:** Simplificar $\sqrt{288}$

---

**Paso 1: Factorizar**

$$288 = 2^5 \times 3^2$$

---

**Paso 2: Identificar grupos de 2 (índice de la raíz)**

$$288 = 2^4 \times 2 \times 3^2 = (2^2)^2 \times 2 \times (3)^2$$

---

**Paso 3: Extraer**

$$\sqrt{288} = \sqrt{(2^2)^2 \times (3)^2 \times 2} = 2^2 \times 3 \times \sqrt{2} = 12\sqrt{2}$$

$$\boxed{\sqrt{288} = 12\sqrt{2}}$$

---

### Ejemplo con Raíz Cúbica

**Problema:** Simplificar $\sqrt[3]{432}$

---

**Paso 1: Factorizar**

$$432 = 2^4 \times 3^3$$

---

**Paso 2: Identificar grupos de 3**

$$432 = 2^3 \times 2 \times 3^3$$

---

**Paso 3: Extraer**

$$\sqrt[3]{432} = \sqrt[3]{2^3 \times 3^3 \times 2} = 2 \times 3 \times \sqrt[3]{2} = 6\sqrt[3]{2}$$

$$\boxed{\sqrt[3]{432} = 6\sqrt[3]{2}}$$

---

## Método 12: Racionalizar Denominadores

**Cuándo Usar:** Eliminar radicales del denominador de una fracción.

### Algoritmo de Resolución

| Tipo | Multiplicar por | Resultado |
|------|-----------------|-----------|
| $\frac{a}{\sqrt{b}}$ | $\frac{\sqrt{b}}{\sqrt{b}}$ | $\frac{a\sqrt{b}}{b}$ |
| $\frac{a}{\sqrt[n]{b^m}}$ | $\frac{\sqrt[n]{b^{n-m}}}{\sqrt[n]{b^{n-m}}}$ | $\frac{a\sqrt[n]{b^{n-m}}}{b}$ |
| $\frac{a}{b + \sqrt{c}}$ | $\frac{b - \sqrt{c}}{b - \sqrt{c}}$ | Usar conjugado |

### Ejemplo 1: Raíz Simple

**Problema:** Racionalizar $\frac{5}{\sqrt{8}}$

---

$$\frac{5}{\sqrt{8}} = \frac{5}{\sqrt{8}} \times \frac{\sqrt{8}}{\sqrt{8}} = \frac{5\sqrt{8}}{8}$$

Simplificar $\sqrt{8} = 2\sqrt{2}$:

$$= \frac{5 \times 2\sqrt{2}}{8} = \frac{10\sqrt{2}}{8} = \frac{5\sqrt{2}}{4}$$

$$\boxed{\frac{5}{\sqrt{8}} = \frac{5\sqrt{2}}{4}}$$

---

### Ejemplo 2: Conjugado

**Problema:** Racionalizar $\frac{6}{3 + \sqrt{5}}$

---

**Multiplicar por el conjugado:**

$$\frac{6}{3 + \sqrt{5}} \times \frac{3 - \sqrt{5}}{3 - \sqrt{5}} = \frac{6(3 - \sqrt{5})}{(3)^2 - (\sqrt{5})^2}$$

$$= \frac{18 - 6\sqrt{5}}{9 - 5} = \frac{18 - 6\sqrt{5}}{4} = \frac{9 - 3\sqrt{5}}{2}$$

$$\boxed{\frac{6}{3 + \sqrt{5}} = \frac{9 - 3\sqrt{5}}{2}}$$

---

## Resumen de Fórmulas

| Concepto | Fórmula |
|----------|---------|
| MCD por Euclides | $\text{MCD}(a, b) = \text{MCD}(b, a \mod b)$ |
| Relación MCD-MCM | $\text{MCD} \times \text{MCM} = a \times b$ |
| Suma de fracciones | $\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$ |
| División de fracciones | $\frac{a}{b} \div \frac{c}{d} = \frac{ad}{bc}$ |
| Decimal periódico | $0.\overline{abc} = \frac{abc}{999}$ |
| Incremento porcentual | $V_f = V_i(1 + r)$ |
| Cambio porcentual | $\Delta\% = \frac{V_f - V_i}{V_i} \times 100$ |
| Raíz de producto | $\sqrt{ab} = \sqrt{a} \times \sqrt{b}$ |
| Racionalización | $\frac{1}{\sqrt{a}} = \frac{\sqrt{a}}{a}$ |

---

## Errores Comunes

| Error | Corrección |
|-------|------------|
| $(a + b)^2 = a^2 + b^2$ | $(a + b)^2 = a^2 + 2ab + b^2$ |
| $\sqrt{a + b} = \sqrt{a} + \sqrt{b}$ | No se puede separar suma bajo raíz |
| $\frac{a}{b + c} = \frac{a}{b} + \frac{a}{c}$ | Solo si es $\frac{a + b}{c} = \frac{a}{c} + \frac{b}{c}$ |
| $a^m \times b^m = (ab)^{2m}$ | $a^m \times b^m = (ab)^m$ |
| 20% + 30% = 50% en incrementos | Incrementos sucesivos: $(1.2)(1.3) = 1.56$ → 56% |
| Olvidar simplificar fracciones | Siempre verificar MCD del resultado |
