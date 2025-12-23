<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: prob-16-solucion
problem_ref: Prob-16
status: stable
audience: student
-->

# Solución: División sintética (Ruffini)

## Problema
Usa división sintética para dividir $(2x^4 - 3x^3 + x - 5)$ entre $(x + 1)$.

---

## Método: División sintética (Regla de Ruffini)

### Paso 1: Identificar el valor de c
Para dividir entre $(x - c)$, necesitamos $c$.

$(x + 1) = (x - (-1))$, por lo tanto $c = -1$.

### Paso 2: Escribir los coeficientes
Del polinomio $2x^4 - 3x^3 + 0x^2 + x - 5$:

**¡Importante!** El término $x^2$ falta, así que usamos coeficiente $0$.

Coeficientes: $[2, -3, 0, 1, -5]$

### Paso 3: Preparar el esquema de Ruffini
```
-1 |  2    -3     0     1    -5
   |
   |________________________________
```

### Paso 4: Ejecutar el algoritmo

**Bajar el primer coeficiente:**
```
-1 |  2    -3     0     1    -5
   |
   |________________________________
      2
```

**Primera multiplicación y suma:**
$2 \times (-1) = -2$, luego $-3 + (-2) = -5$
```
-1 |  2    -3     0     1    -5
   |       -2
   |________________________________
      2    -5
```

**Segunda multiplicación y suma:**
$(-5) \times (-1) = 5$, luego $0 + 5 = 5$
```
-1 |  2    -3     0     1    -5
   |       -2     5
   |________________________________
      2    -5     5
```

**Tercera multiplicación y suma:**
$5 \times (-1) = -5$, luego $1 + (-5) = -4$
```
-1 |  2    -3     0     1    -5
   |       -2     5    -5
   |________________________________
      2    -5     5    -4
```

**Cuarta multiplicación y suma:**
$(-4) \times (-1) = 4$, luego $-5 + 4 = -1$
```
-1 |  2    -3     0     1    -5
   |       -2     5    -5     4
   |________________________________
      2    -5     5    -4    -1
                             ↑
                          Residuo
```

### Paso 5: Interpretar el resultado
Los números en la última fila son los coeficientes del cociente (grado reducido en 1) y el residuo.

**Cociente:** $2x^3 - 5x^2 + 5x - 4$
**Residuo:** $-1$

---

## Respuesta Final
$$\frac{2x^4 - 3x^3 + x - 5}{x + 1} = \boxed{2x^3 - 5x^2 + 5x - 4 + \frac{-1}{x+1}}$$

O equivalentemente:
$$2x^4 - 3x^3 + x - 5 = (x + 1)(2x^3 - 5x^2 + 5x - 4) - 1$$

---

## Verificación por Teorema del Residuo
$P(x) = 2x^4 - 3x^3 + x - 5$

$P(-1) = 2(-1)^4 - 3(-1)^3 + (-1) - 5$
$= 2(1) - 3(-1) - 1 - 5$
$= 2 + 3 - 1 - 5$
$= -1$ ✓

El residuo coincide con $P(-1)$.

---

## Verificación expandiendo
$(x + 1)(2x^3 - 5x^2 + 5x - 4) - 1$
$= 2x^4 - 5x^3 + 5x^2 - 4x + 2x^3 - 5x^2 + 5x - 4 - 1$
$= 2x^4 + (-5+2)x^3 + (5-5)x^2 + (-4+5)x + (-4-1)$
$= 2x^4 - 3x^3 + 0x^2 + x - 5$ ✓
