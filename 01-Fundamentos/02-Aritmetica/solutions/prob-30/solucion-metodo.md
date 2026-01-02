<!--
::METADATA::
type: solution
topic_id: fun-02-aritmetica
file_id: FUN-02-Prob-30-Solucion
status: stable
audience: student
problem_ref: "[Prob-30]"
methods: ["estimación por raíz cúbica", "[factorización](../../../../glossary.md#factorización) directa", "búsqueda sistemática"]
-->

# Solución [Prob-30]: Producto de primos consecutivos

> **Problema:** El producto de tres primos consecutivos es 2431. ¿Cuáles son?

---

## Método 1: Estimación por Raíz Cúbica

### Paso 1: Estimar el primo central

Si tres primos consecutivos $p_1, p_2, p_3$ tienen producto 2431, entonces los tres primos deben estar "cerca" de la raíz cúbica del producto.

Calculamos:
$$\sqrt[3]{2431} \approx 13.44$$

### Paso 2: Identificar primos cercanos a 13

Listamos los primos cercanos a 13:
- $..., 7, 11, \mathbf{13}, 17, 19, 23, ...$

Los candidatos más probables para el primo central son 11, 13 o 17.

### Paso 3: Probar con primos consecutivos centrados en 13

**Opción 1:** Primos consecutivos $11, 13, 17$

$$11 \times 13 \times 17 = ?$$

Calculamos paso a paso:
$$11 \times 13 = 143$$
$$143 \times 17 = 143 \times 17$$

Para $143 \times 17$:
$$143 \times 17 = 143 \times 10 + 143 \times 7$$
$$= 1430 + 1001$$
$$= 2431$$

¡Este es exactamente el valor buscado!

### Verificación

$$11 \times 13 \times 17 = 2431 \quad \checkmark$$

Confirmemos que 11, 13 y 17 son primos consecutivos:
- **11** es primo (divisible solo por 1 y 11)
- **13** es primo (divisible solo por 1 y 13)
- **17** es primo (divisible solo por 1 y 17)
- No hay primos entre 11 y 13 ✓
- No hay primos entre 13 y 17 ✓

Por lo tanto, 11, 13 y 17 son efectivamente **tres primos consecutivos**.

---

## Método 2: Factorización Directa de 2431

### Paso 1: Verificar divisibilidad por primos pequeños

**¿Es divisible por 2?** No, porque 2431 es impar.

**¿Es divisible por 3?** Suma de dígitos: $2 + 4 + 3 + 1 = 10$. Como 10 no es divisible por 3, 2431 tampoco lo es.

**¿Es divisible por 5?** No, porque no termina en 0 ni en 5.

**¿Es divisible por 7?**
$$2431 \div 7 = 347.28...$$
No es exacto.

**¿Es divisible por 11?**
$$2431 \div 11 = 221$$

¡Sí! Verificamos: $11 \times 221 = 2431$ ✓

### Paso 2: Factorizar 221

$$221 \div 11 = 20.09...$$ 
No es exacto.

$$221 \div 13 = 17$$

¡Sí! Verificamos: $13 \times 17 = 221$ ✓

### Paso 3: Factorización completa

$$2431 = 11 \times 221 = 11 \times 13 \times 17$$

### Paso 4: Verificar que son primos consecutivos

Secuencia de primos: $2, 3, 5, 7, 11, 13, 17, 19, 23, ...$

- 11 es el 5º primo
- 13 es el 6º primo
- 17 es el 7º primo

Efectivamente son **tres primos consecutivos**.

---

## Método 3: Búsqueda Sistemática

### Paso 1: Listar tripletas de primos consecutivos

| Tripleta | Producto |
|----------|----------|
| 3, 5, 7 | $3 \times 5 \times 7 = 105$ |
| 5, 7, 11 | $5 \times 7 \times 11 = 385$ |
| 7, 11, 13 | $7 \times 11 \times 13 = 1001$ |
| **11, 13, 17** | $11 \times 13 \times 17 = \mathbf{2431}$ ✓ |
| 13, 17, 19 | $13 \times 17 \times 19 = 4199$ |

### Paso 2: Identificar la tripleta correcta

La única tripleta cuyo producto es 2431 es $\{11, 13, 17\}$.

---

## Cálculo Detallado del Producto

Para mayor claridad, mostramos el cálculo completo:

$$11 \times 13 = 143$$

Desglose:
$$11 \times 13 = 11 \times (10 + 3) = 110 + 33 = 143$$

$$143 \times 17$$

Desglose:
$$143 \times 17 = 143 \times (20 - 3) = 143 \times 20 - 143 \times 3$$
$$= 2860 - 429 = 2431$$

O alternativamente:
$$143 \times 17 = (140 + 3) \times 17 = 140 \times 17 + 3 \times 17$$
$$= 2380 + 51 = 2431$$

---

## Respuesta Final

**Los tres primos consecutivos son: $\boxed{11, 13 \text{ y } 17}$**

---

> 📚 Volver a: [FUN-02-Problemas](../../problems/FUN-02-Problemas.md)
