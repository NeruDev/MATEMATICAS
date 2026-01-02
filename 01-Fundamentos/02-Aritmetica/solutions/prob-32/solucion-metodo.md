<!--
::METADATA::
type: solution
topic_id: fun-02-aritmetica
file_id: prob-32-solucion
problem_ref: Prob-32
status: stable
audience: student
-->

# Solución: MCD por algoritmo de Euclides

## Problema
Calcula $\text{[MCD](../../../../glossary.md#mcd)}(252, 198)$ usando el algoritmo de Euclides.

---

## Método: Algoritmo de Euclides

### Fundamento teórico
El algoritmo de Euclides se basa en que $\text{MCD}(a, b) = \text{MCD}(b, r)$, donde $r$ es el residuo de dividir $a$ entre $b$.

### Paso 1: Primera división
$$252 = 198 \times 1 + 54$$
- Dividendo: 252
- Divisor: 198
- Cociente: $\lfloor 252/198 \rfloor = 1$
- **Residuo: 54**

### Paso 2: Segunda división
$$198 = 54 \times 3 + 36$$
- Dividendo: 198
- Divisor: 54
- Cociente: $\lfloor 198/54 \rfloor = 3$
- **Residuo: 36**

### Paso 3: Tercera división
$$54 = 36 \times 1 + 18$$
- Dividendo: 54
- Divisor: 36
- Cociente: $\lfloor 54/36 \rfloor = 1$
- **Residuo: 18**

### Paso 4: Cuarta división
$$36 = 18 \times 2 + 0$$
- Dividendo: 36
- Divisor: 18
- Cociente: $\lfloor 36/18 \rfloor = 2$
- **Residuo: 0** ← El algoritmo termina

### Paso 5: Conclusión
El **último divisor no nulo** es el MCD.

---

## Respuesta Final
$$\text{MCD}(252, 198) = \boxed{18}$$

---

## Verificación por factorización
$$252 = 2^2 \times 3^2 \times 7$$
$$198 = 2 \times 3^2 \times 11$$

$$\text{MCD} = 2^{\min(2,1)} \times 3^{\min(2,2)} = 2^1 \times 3^2 = 2 \times 9 = 18 \checkmark$$

---

## Resumen del algoritmo
| Paso | División | Residuo |
|:----:|:---------|:-------:|
| 1 | $252 = 198(1) + 54$ | 54 |
| 2 | $198 = 54(3) + 36$ | 36 |
| 3 | $54 = 36(1) + 18$ | 18 |
| 4 | $36 = 18(2) + 0$ | **0** |

**MCD = 18**
