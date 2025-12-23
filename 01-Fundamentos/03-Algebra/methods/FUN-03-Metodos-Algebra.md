# Métodos de Álgebra

---

## Método 1: Simplificación de expresiones con términos semejantes

**Contexto:** Reducir expresiones algebraicas combinando términos con las mismas variables y exponentes.

**Pasos:**
1. Identificar términos semejantes (mismas variables con mismos exponentes)
2. Sumar o restar los coeficientes de términos semejantes
3. Escribir el resultado en orden descendente de grado

**Ejemplo:** Simplificar $3x^2 + 5x - 2x^2 + 7 - 3x + 1$

| Paso | Proceso |
|------|---------|
| Agrupar | $(3x^2 - 2x^2) + (5x - 3x) + (7 + 1)$ |
| Combinar | $x^2 + 2x + 8$ |

**Verificación:** Evaluar en $x = 1$: Original = $3 + 5 - 2 + 7 - 3 + 1 = 11$; Simplificado = $1 + 2 + 8 = 11$ ✓

---

## Método 2: Multiplicación de polinomios (FOIL para binomios)

**Contexto:** Multiplicar dos binomios usando la regla FOIL (First, Outer, Inner, Last).

**Pasos:**
1. **F**irst: Multiplicar los primeros términos
2. **O**uter: Multiplicar los términos externos
3. **I**nner: Multiplicar los términos internos
4. **L**ast: Multiplicar los últimos términos
5. Combinar términos semejantes

**Ejemplo:** $(2x + 3)(x - 4)$

| Paso | Operación | Resultado |
|------|-----------|-----------|
| First | $2x \cdot x$ | $2x^2$ |
| Outer | $2x \cdot (-4)$ | $-8x$ |
| Inner | $3 \cdot x$ | $3x$ |
| Last | $3 \cdot (-4)$ | $-12$ |
| **Total** | $2x^2 - 8x + 3x - 12$ | $2x^2 - 5x - 12$ |

---

## Método 3: División sintética (Ruffini)

**Contexto:** Dividir un polinomio por $(x - a)$ de manera eficiente.

**Pasos:**
1. Escribir los coeficientes del dividendo (incluir 0 para términos faltantes)
2. Escribir $a$ a la izquierda (el valor que hace cero al divisor)
3. Bajar el primer coeficiente
4. Multiplicar por $a$, sumar al siguiente coeficiente
5. Repetir hasta terminar. El último número es el residuo.

**Ejemplo:** $(x^3 - 6x^2 + 11x - 6) \div (x - 2)$

| $a = 2$ | 1 | -6 | 11 | -6 |
|---------|---|----|----|-----|
| | | 2 | -8 | 6 |
| | 1 | -4 | 3 | **0** |

**Resultado:** Cociente = $x^2 - 4x + 3$, Residuo = $0$

**Verificación:** $(x - 2)(x^2 - 4x + 3) = x^3 - 4x^2 + 3x - 2x^2 + 8x - 6 = x^3 - 6x^2 + 11x - 6$ ✓

---

## Método 4: Factorización por factor común

**Contexto:** Extraer el mayor factor común de todos los términos.

**Pasos:**
1. Identificar el MCD de los coeficientes numéricos
2. Identificar el menor exponente de cada variable común
3. Extraer el factor común
4. Escribir en paréntesis lo que queda

**Ejemplo:** $12x^3y^2 - 8x^2y^3 + 4x^2y^2$

| Paso | Análisis |
|------|----------|
| MCD numérico | MCD(12, 8, 4) = 4 |
| Variable $x$ | Menor exponente: $x^2$ |
| Variable $y$ | Menor exponente: $y^2$ |
| Factor común | $4x^2y^2$ |

**Resultado:** $4x^2y^2(3x - 2y + 1)$

---

## Método 5: Factorización de trinomio $x^2 + bx + c$

**Contexto:** Factorizar cuando el coeficiente de $x^2$ es 1.

**Pasos:**
1. Buscar dos números $m$ y $n$ tales que:
   - $m + n = b$
   - $m \cdot n = c$
2. Escribir $(x + m)(x + n)$

**Ejemplo:** $x^2 - 7x + 12$

| Condición | Valor |
|-----------|-------|
| $m + n$ | $-7$ |
| $m \cdot n$ | $12$ |
| Solución | $m = -3$, $n = -4$ |

**Resultado:** $(x - 3)(x - 4)$

**Verificación:** $(x - 3)(x - 4) = x^2 - 4x - 3x + 12 = x^2 - 7x + 12$ ✓

---

## Método 6: Factorización por el método AC ($ax^2 + bx + c$)

**Contexto:** Factorizar trinomios donde $a \neq 1$.

**Pasos:**
1. Calcular $ac$
2. Buscar dos números que sumen $b$ y multipliquen $ac$
3. Reescribir el término medio usando esos números
4. Factorizar por agrupación

**Ejemplo:** $6x^2 + x - 12$

| Paso | Cálculo |
|------|---------|
| $ac$ | $6 \times (-12) = -72$ |
| Buscar | $m + n = 1$, $m \cdot n = -72$ → $m = 9$, $n = -8$ |
| Reescribir | $6x^2 + 9x - 8x - 12$ |
| Agrupar | $3x(2x + 3) - 4(2x + 3)$ |
| Factorizar | $(2x + 3)(3x - 4)$ |

---

## Método 7: Resolver ecuaciones lineales

**Contexto:** Encontrar el valor de $x$ en ecuaciones de primer grado.

**Pasos:**
1. Eliminar paréntesis (distribuir)
2. Eliminar fracciones (multiplicar por MCM de denominadores)
3. Mover términos con $x$ a un lado, constantes al otro
4. Combinar términos semejantes
5. Despejar $x$

**Ejemplo:** $\frac{2x - 1}{3} + \frac{x + 2}{4} = 2$

| Paso | Operación |
|------|-----------|
| MCM(3,4) = 12 | $12 \cdot \frac{2x-1}{3} + 12 \cdot \frac{x+2}{4} = 12 \cdot 2$ |
| Simplificar | $4(2x - 1) + 3(x + 2) = 24$ |
| Distribuir | $8x - 4 + 3x + 6 = 24$ |
| Combinar | $11x + 2 = 24$ |
| Despejar | $11x = 22$ → $x = 2$ |

**Verificación:** $\frac{3}{3} + \frac{4}{4} = 1 + 1 = 2$ ✓

---

## Método 8: Resolver ecuaciones cuadráticas por factorización

**Contexto:** Resolver $ax^2 + bx + c = 0$ cuando el trinomio es factorizable.

**Pasos:**
1. Llevar la ecuación a forma estándar ($= 0$)
2. Factorizar el lado izquierdo
3. Aplicar la propiedad del producto cero: si $AB = 0$, entonces $A = 0$ o $B = 0$
4. Resolver cada ecuación lineal

**Ejemplo:** $x^2 = 5x - 6$

| Paso | Operación |
|------|-----------|
| Forma estándar | $x^2 - 5x + 6 = 0$ |
| Factorizar | $(x - 2)(x - 3) = 0$ |
| Producto cero | $x - 2 = 0$ o $x - 3 = 0$ |
| Soluciones | $x = 2$ o $x = 3$ |

---

## Método 9: Fórmula cuadrática

**Contexto:** Resolver cualquier ecuación cuadrática $ax^2 + bx + c = 0$.

**Fórmula:**
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**Pasos:**
1. Identificar $a$, $b$, $c$
2. Calcular el discriminante $\Delta = b^2 - 4ac$
3. Sustituir en la fórmula
4. Simplificar

**Ejemplo:** $2x^2 + 5x - 3 = 0$

| Paso | Cálculo |
|------|---------|
| Coeficientes | $a = 2$, $b = 5$, $c = -3$ |
| Discriminante | $\Delta = 25 - 4(2)(-3) = 25 + 24 = 49$ |
| Fórmula | $x = \frac{-5 \pm 7}{4}$ |
| Soluciones | $x = \frac{2}{4} = \frac{1}{2}$ o $x = \frac{-12}{4} = -3$ |

---

## Método 10: Sistema 2×2 por sustitución

**Contexto:** Resolver sistemas donde es fácil despejar una variable.

**Pasos:**
1. Despejar una variable de la ecuación más sencilla
2. Sustituir en la otra ecuación
3. Resolver la ecuación resultante
4. Sustituir para hallar la otra variable

**Ejemplo:**
$$\begin{cases} x + 2y = 7 \\ 3x - y = 7 \end{cases}$$

| Paso | Operación |
|------|-----------|
| Despejar $x$ | $x = 7 - 2y$ |
| Sustituir | $3(7 - 2y) - y = 7$ |
| Resolver | $21 - 6y - y = 7$ → $-7y = -14$ → $y = 2$ |
| Hallar $x$ | $x = 7 - 4 = 3$ |

**Solución:** $(3, 2)$

---

## Método 11: Sistema 2×2 por eliminación

**Contexto:** Resolver sistemas multiplicando ecuaciones para eliminar una variable.

**Pasos:**
1. Elegir la variable a eliminar
2. Multiplicar ecuaciones para que los coeficientes sean opuestos
3. Sumar las ecuaciones
4. Resolver y sustituir

**Ejemplo:**
$$\begin{cases} 2x + 3y = 12 \\ 5x - 2y = 1 \end{cases}$$

| Paso | Operación |
|------|-----------|
| Eliminar $y$ | Multiplicar 1ª por 2, 2ª por 3 |
| Nuevas ecuaciones | $4x + 6y = 24$, $15x - 6y = 3$ |
| Sumar | $19x = 27$ → $x = \frac{27}{19}$ |
| Sustituir | $y = \frac{12 - 2(\frac{27}{19})}{3} = \frac{12 - \frac{54}{19}}{3} = \frac{174}{57} = \frac{58}{19}$ |

**Solución:** $\left(\frac{27}{19}, \frac{58}{19}\right)$

---

## Método 12: Resolver inecuaciones lineales

**Contexto:** Encontrar el conjunto solución de desigualdades de primer grado.

**Pasos:**
1. Aplicar las mismas operaciones que en ecuaciones
2. **IMPORTANTE:** Al multiplicar/dividir por negativo, invertir el signo
3. Expresar la solución en notación de intervalo

**Ejemplo:** $-2x + 5 > 3x - 10$

| Paso | Operación |
|------|-----------|
| Mover términos | $-2x - 3x > -10 - 5$ |
| Combinar | $-5x > -15$ |
| Dividir por $-5$ | $x < 3$ (se invierte el signo) |

**Solución:** $(-\infty, 3)$

---

## Método 13: Resolver inecuaciones cuadráticas

**Contexto:** Encontrar valores donde un trinomio es positivo o negativo.

**Pasos:**
1. Factorizar la expresión cuadrática
2. Encontrar las raíces (puntos críticos)
3. Construir tabla de signos
4. Seleccionar intervalos según la desigualdad

**Ejemplo:** $x^2 - 2x - 8 \leq 0$

| Paso | Cálculo |
|------|---------|
| Factorizar | $(x - 4)(x + 2) \leq 0$ |
| Raíces | $x = 4$, $x = -2$ |
| Tabla de signos | |

| Intervalo | $(x-4)$ | $(x+2)$ | Producto |
|-----------|---------|---------|----------|
| $x < -2$ | $-$ | $-$ | $+$ |
| $-2 < x < 4$ | $-$ | $+$ | $-$ ✓ |
| $x > 4$ | $+$ | $+$ | $+$ |

**Solución:** $[-2, 4]$

---

## Método 14: Simplificar fracciones algebraicas

**Contexto:** Reducir expresiones racionales a su forma más simple.

**Pasos:**
1. Factorizar numerador y denominador completamente
2. Cancelar factores comunes
3. Indicar restricciones del dominio

**Ejemplo:** $\frac{x^2 - 4x + 3}{x^2 - 1}$

| Paso | Operación |
|------|-----------|
| Factorizar numerador | $(x - 1)(x - 3)$ |
| Factorizar denominador | $(x - 1)(x + 1)$ |
| Cancelar | $\frac{(x-1)(x-3)}{(x-1)(x+1)} = \frac{x-3}{x+1}$ |
| Restricciones | $x \neq 1$, $x \neq -1$ |

---

## Método 15: Racionalizar denominadores con radicales

**Contexto:** Eliminar radicales del denominador de una fracción.

**Caso binomio:**
1. Multiplicar por el conjugado: $(a + \sqrt{b})(a - \sqrt{b}) = a^2 - b$

**Ejemplo:** $\frac{5}{3 + \sqrt{2}}$

| Paso | Operación |
|------|-----------|
| Conjugado | $3 - \sqrt{2}$ |
| Multiplicar | $\frac{5(3 - \sqrt{2})}{(3 + \sqrt{2})(3 - \sqrt{2})}$ |
| Simplificar | $\frac{15 - 5\sqrt{2}}{9 - 2} = \frac{15 - 5\sqrt{2}}{7}$ |
