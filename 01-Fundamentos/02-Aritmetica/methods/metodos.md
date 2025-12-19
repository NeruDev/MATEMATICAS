# Métodos de Aritmética

---

## Método 1: Aplicar jerarquía de operaciones (PEMDAS)

### Contexto
La jerarquía evita ambigüedad al evaluar expresiones con múltiples operaciones.

### Pasos
1. Resuelve lo que está dentro de **P**aréntesis (de adentro hacia afuera).
2. Evalúa **E**xponentes (potencias y raíces).
3. Realiza **M**ultiplicación y **D**ivisión de izquierda a derecha.
4. Realiza **A**dición y **S**ustracción de izquierda a derecha.

### Ejemplo práctico
**Problema**: Evalúa $2 + 3 \times (4^2 - 6) \div 5$

**Solución**:
1. Paréntesis: $4^2 - 6 = 16 - 6 = 10$
2. Expresión: $2 + 3 \times 10 \div 5$
3. Multiplicación/División (izq. a der.): $3 \times 10 = 30$, luego $30 \div 5 = 6$
4. Suma: $2 + 6 = 8$

**Resultado**: $8$

### Verificación
Usa calculadora ingresando la expresión completa.

---

## Método 2: Descomponer en factores primos

### Contexto
La factorización prima es base para calcular MCD, MCM y simplificar fracciones.

### Pasos
1. Divide el número por el menor primo que lo divida.
2. Continúa dividiendo el cociente por primos.
3. Repite hasta llegar a 1.
4. Escribe el número como producto de los primos usados.

### Ejemplo práctico
**Problema**: Factoriza 360.

**Solución**:
| Número | Primo |
|--------|-------|
| 360 | 2 |
| 180 | 2 |
| 90 | 2 |
| 45 | 3 |
| 15 | 3 |
| 5 | 5 |
| 1 | — |

$$360 = 2^3 \times 3^2 \times 5$$

### Verificación
$2^3 \times 3^2 \times 5 = 8 \times 9 \times 5 = 360$ ✓

---

## Método 3: Calcular MCD por factorización

### Contexto
El MCD es esencial para simplificar fracciones al máximo.

### Pasos
1. Descompón ambos números en factores primos.
2. Identifica los factores **comunes**.
3. Toma cada factor común con el **menor** exponente.
4. Multiplica los factores seleccionados.

### Ejemplo práctico
**Problema**: Encuentra $\text{MCD}(48, 180)$.

**Solución**:
- $48 = 2^4 \times 3$
- $180 = 2^2 \times 3^2 \times 5$
- Factores comunes: $2$ (menor exp: 2), $3$ (menor exp: 1)
- $\text{MCD} = 2^2 \times 3 = 12$

### Verificación
$48 \div 12 = 4$ ✓, $180 \div 12 = 15$ ✓

---

## Método 4: Calcular MCD por algoritmo de Euclides

### Contexto
Más eficiente que factorización para números grandes.

### Pasos
1. Divide el mayor entre el menor; anota el residuo.
2. Reemplaza: (mayor, menor) → (menor, residuo).
3. Repite hasta que el residuo sea 0.
4. El último divisor no nulo es el MCD.

### Ejemplo práctico
**Problema**: Encuentra $\text{MCD}(462, 1071)$ por Euclides.

**Solución**:
- $1071 = 462 \times 2 + 147$
- $462 = 147 \times 3 + 21$
- $147 = 21 \times 7 + 0$

**MCD** = 21

### Verificación
$462 = 21 \times 22$ ✓, $1071 = 21 \times 51$ ✓

---

## Método 5: Calcular MCM por factorización

### Contexto
El MCM se usa para encontrar denominadores comunes en sumas de fracciones.

### Pasos
1. Descompón ambos números en factores primos.
2. Lista **todos** los factores que aparecen.
3. Toma cada factor con el **mayor** exponente.
4. Multiplica los factores seleccionados.

### Ejemplo práctico
**Problema**: Encuentra $\text{MCM}(48, 180)$.

**Solución**:
- $48 = 2^4 \times 3$
- $180 = 2^2 \times 3^2 \times 5$
- Todos los factores: $2^4$, $3^2$, $5^1$
- $\text{MCM} = 2^4 \times 3^2 \times 5 = 16 \times 9 \times 5 = 720$

### Verificación
Usando la relación: $\text{MCD} \times \text{MCM} = 48 \times 180$
$12 \times 720 = 8640 = 48 \times 180$ ✓

---

## Método 6: Sumar fracciones con distinto denominador

### Contexto
Las fracciones solo se suman directamente si tienen el mismo denominador.

### Pasos
1. Encuentra el MCM de los denominadores.
2. Convierte cada fracción al denominador común.
3. Suma los numeradores.
4. Simplifica si es posible.

### Ejemplo práctico
**Problema**: Calcula $\frac{5}{12} + \frac{7}{18}$.

**Solución**:
- $\text{MCM}(12, 18) = 36$
- $\frac{5}{12} = \frac{5 \times 3}{36} = \frac{15}{36}$
- $\frac{7}{18} = \frac{7 \times 2}{36} = \frac{14}{36}$
- $\frac{15}{36} + \frac{14}{36} = \frac{29}{36}$

**Resultado**: $\frac{29}{36}$

### Verificación
$\frac{5}{12} \approx 0.417$, $\frac{7}{18} \approx 0.389$, suma $\approx 0.806$
$\frac{29}{36} \approx 0.806$ ✓

---

## Método 7: Dividir fracciones

### Contexto
Dividir por una fracción equivale a multiplicar por su recíproco.

### Pasos
1. Escribe el recíproco (invertir) del divisor.
2. Cambia la división por multiplicación.
3. Multiplica numeradores entre sí y denominadores entre sí.
4. Simplifica el resultado.

### Ejemplo práctico
**Problema**: Calcula $\frac{8}{15} \div \frac{4}{9}$.

**Solución**:
$$\frac{8}{15} \div \frac{4}{9} = \frac{8}{15} \times \frac{9}{4} = \frac{8 \times 9}{15 \times 4} = \frac{72}{60}$$

Simplificando: $\text{MCD}(72, 60) = 12$
$$\frac{72}{60} = \frac{6}{5} = 1\frac{1}{5}$$

### Verificación
$\frac{6}{5} \times \frac{4}{9} = \frac{24}{45} = \frac{8}{15}$ ✓

---

## Método 8: Convertir decimal periódico a fracción

### Contexto
Todo decimal periódico es racional y puede expresarse como fracción.

### Pasos
1. Sea $x$ el decimal periódico.
2. Multiplica por $10^n$ donde $n$ = longitud del período.
3. Resta la ecuación original.
4. Despeja $x$.

### Ejemplo práctico
**Problema**: Convierte $0.\overline{27}$ a fracción.

**Solución**:
- Sea $x = 0.272727...$
- $100x = 27.272727...$
- $100x - x = 27$
- $99x = 27$
- $x = \frac{27}{99} = \frac{3}{11}$

### Verificación
$3 \div 11 = 0.272727...$ ✓

---

## Método 9: Calcular porcentaje de incremento/decremento

### Contexto
Mide el cambio relativo entre un valor inicial y uno final.

### Pasos
1. Calcula la diferencia: $\Delta = V_f - V_i$
2. Divide por el valor inicial: $\frac{\Delta}{V_i}$
3. Multiplica por 100 para expresar como porcentaje.

### Fórmula
$$\text{Cambio \%} = \frac{V_f - V_i}{V_i} \times 100\%$$

### Ejemplo práctico
**Problema**: Un producto costaba \$80 y ahora cuesta \$92. ¿Cuál fue el incremento porcentual?

**Solución**:
$$\text{Incremento} = \frac{92 - 80}{80} \times 100\% = \frac{12}{80} \times 100\% = 15\%$$

### Verificación
$80 \times 1.15 = 92$ ✓

---

## Método 10: Simplificar expresiones con exponentes

### Contexto
Las leyes de exponentes permiten combinar y simplificar potencias.

### Pasos
1. Agrupa términos con la misma base.
2. Aplica las leyes de exponentes:
   - $a^m \cdot a^n = a^{m+n}$
   - $\frac{a^m}{a^n} = a^{m-n}$
   - $(a^m)^n = a^{mn}$
3. Convierte exponentes negativos si se desea.

### Ejemplo práctico
**Problema**: Simplifica $\frac{2^5 \cdot 3^{-2} \cdot 2^{-3}}{3^{-4}}$.

**Solución**:
$$= \frac{2^{5+(-3)} \cdot 3^{-2}}{3^{-4}} = \frac{2^2 \cdot 3^{-2}}{3^{-4}} = 2^2 \cdot 3^{-2-(-4)} = 4 \cdot 3^2 = 4 \cdot 9 = 36$$

### Verificación
Calculando directamente: $\frac{32 \cdot \frac{1}{9} \cdot \frac{1}{8}}{\frac{1}{81}} = \frac{32}{72} \cdot 81 = \frac{32 \cdot 81}{72} = 36$ ✓

---

## Método 11: Racionalizar denominadores

### Contexto
Eliminar raíces del denominador facilita operaciones posteriores.

### Pasos
**Caso 1**: Denominador $\sqrt{a}$
- Multiplica numerador y denominador por $\sqrt{a}$.

**Caso 2**: Denominador $\sqrt{a} + \sqrt{b}$
- Multiplica por el conjugado $\sqrt{a} - \sqrt{b}$.

### Ejemplo práctico
**Problema**: Racionaliza $\frac{5}{2 + \sqrt{3}}$.

**Solución**:
$$\frac{5}{2 + \sqrt{3}} \cdot \frac{2 - \sqrt{3}}{2 - \sqrt{3}} = \frac{5(2 - \sqrt{3})}{4 - 3} = \frac{10 - 5\sqrt{3}}{1} = 10 - 5\sqrt{3}$$

### Verificación
$(10 - 5\sqrt{3})(2 + \sqrt{3}) = 20 + 10\sqrt{3} - 10\sqrt{3} - 15 = 5$ ✓

---

## Método 12: Resolver problemas de proporcionalidad

### Contexto
La regla de tres resuelve problemas donde las cantidades varían proporcionalmente.

### Pasos
1. Identifica si es proporcionalidad directa o inversa.
2. Plantea la proporción.
3. Aplica la propiedad fundamental ($ad = bc$).
4. Despeja la incógnita.

### Ejemplo práctico
**Problema**: Si 8 trabajadores terminan una obra en 15 días, ¿cuántos días tardarán 12 trabajadores?

**Solución**:
Es proporcionalidad **inversa** (más trabajadores = menos días).

$$8 \times 15 = 12 \times x$$
$$x = \frac{8 \times 15}{12} = \frac{120}{12} = 10 \text{ días}$$

### Verificación
Trabajo total = $8 \times 15 = 120$ "trabajador-días"
Con 12 trabajadores: $120 \div 12 = 10$ días ✓
