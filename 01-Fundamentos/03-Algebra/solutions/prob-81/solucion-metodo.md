<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: FUN-03-Prob-81-Solucion
status: stable
audience: student
problem_ref: "[Prob-81]"
methods: ["sistema-ecuaciones", "problema-verbal", "representacion-digitos"]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución [Prob-81]: Problema de dígitos

> **Problema:** Invirtiendo los dígitos de un número de dos cifras, se obtiene un número 27 unidades mayor. Si la suma de los dígitos es 9, ¿cuál es el número original?

## Análisis del problema

### Paso 1: Definir las variables

Sea el número original de dos cifras con:
- **Dígito de las decenas:** $d$
- **Dígito de las unidades:** $u$

Entonces el número original es: $10d + u$

### Paso 2: Expresar el número invertido

Al invertir los dígitos:
- El dígito $u$ pasa a las decenas
- El dígito $d$ pasa a las unidades

El número invertido es: $10u + d$

### Paso 3: Traducir las condiciones a ecuaciones

**Condición 1:** "El número invertido es 27 unidades mayor que el original"

$$\text{Invertido} = \text{Original} + 27$$

$$10u + d = (10d + u) + 27$$

**Condición 2:** "La suma de los dígitos es 9"

$$d + u = 9$$

---

## Resolución del sistema

### Paso 1: Simplificar la primera ecuación

$$10u + d = 10d + u + 27$$

Agrupamos términos:

$$10u - u = 10d - d + 27$$

$$9u = 9d + 27$$

Dividimos entre 9:

$$u = d + 3 \quad \text{...(1)}$$

### Paso 2: Sustituir en la segunda ecuación

De la condición 2: $d + u = 9$

Sustituimos $u = d + 3$:

$$d + (d + 3) = 9$$

$$2d + 3 = 9$$

$$2d = 6$$

$$d = 3$$

### Paso 3: Encontrar el otro dígito

$$u = d + 3 = 3 + 3 = 6$$

### Paso 4: Formar el número original

$$\text{Número original} = 10d + u = 10(3) + 6 = 36$$

---

## Verificación

### Verificación de las condiciones

**Número original:** $36$
**Número invertido:** $63$

**Condición 1:** ¿El invertido es 27 más que el original?

$$63 - 36 = 27 \quad \checkmark$$

**Condición 2:** ¿La suma de dígitos es 9?

$$3 + 6 = 9 \quad \checkmark$$

---

## Análisis: ¿Por qué la diferencia es múltiplo de 9?

Este es un resultado general: cuando invertimos los dígitos de un número de dos cifras, la diferencia siempre es múltiplo de 9.

**Demostración:**

Sea el número original $10d + u$ y el invertido $10u + d$.

La diferencia es:

$$(10u + d) - (10d + u) = 10u + d - 10d - u = 9u - 9d = 9(u - d)$$

Por lo tanto, la diferencia siempre es $9$ veces la diferencia entre los dígitos.

En nuestro problema: $27 = 9 \times 3$, así que $u - d = 3$.

---

## Método alternativo: Razonamiento directo

### Usando la propiedad de la diferencia

Sabemos que:
1. $u - d = \frac{27}{9} = 3$ (de la diferencia)
2. $u + d = 9$ (dado en el problema)

Sumando estas ecuaciones:

$$(u - d) + (u + d) = 3 + 9$$

$$2u = 12$$

$$u = 6$$

Restando las ecuaciones:

$$(u + d) - (u - d) = 9 - 3$$

$$2d = 6$$

$$d = 3$$

---

## Diagrama del problema

```
     Número Original                Número Invertido
     
     ┌─────┬─────┐                  ┌─────┬─────┐
     │  d  │  u  │      ───▶       │  u  │  d  │
     │ (3) │ (6) │   invertir      │ (6) │ (3) │
     └─────┴─────┘                  └─────┴─────┘
          │                              │
          │                              │
       10d + u                        10u + d
          │                              │
       10(3)+6 = 36                   10(6)+3 = 63
          │                              │
          └──────────────┬───────────────┘
                         │
                    63 - 36 = 27 ✓
```

---

## Representación tabular de la solución

| Concepto | Expresión algebraica | Valor numérico |
|----------|---------------------|----------------|
| Dígito decenas | $d$ | $3$ |
| Dígito unidades | $u$ | $6$ |
| Número original | $10d + u$ | $36$ |
| Número invertido | $10u + d$ | $63$ |
| Diferencia | $9(u - d)$ | $27$ |
| Suma de dígitos | $d + u$ | $9$ |

---

## Problemas similares: Casos posibles

Si la suma de dígitos es 9 y queremos que la diferencia al invertir sea positiva (el invertido mayor), los casos posibles son:

| $(d, u)$ | Original | Invertido | Diferencia |
|----------|----------|-----------|------------|
| $(0, 9)$ | $09$ | $90$ | $81 = 9 \times 9$ |
| $(1, 8)$ | $18$ | $81$ | $63 = 9 \times 7$ |
| $(2, 7)$ | $27$ | $72$ | $45 = 9 \times 5$ |
| $(3, 6)$ | $36$ | $63$ | $27 = 9 \times 3$ ✓ |
| $(4, 5)$ | $45$ | $54$ | $9 = 9 \times 1$ |

El único caso donde la diferencia es 27 es cuando el número es **36**.

---

## Errores comunes a evitar

⚠️ **Error 1:** Escribir el número como $du$ en lugar de $10d + u$.

El número 36 **no** es $3 \times 6 = 18$, sino $10(3) + 6 = 36$.

⚠️ **Error 2:** Confundir cuál número es mayor.

Si $u > d$, entonces el número invertido es mayor. Verificar el signo de la diferencia.

⚠️ **Error 3:** Olvidar que los dígitos deben ser enteros entre 0 y 9.

Además, el dígito de las decenas no puede ser 0 (sería un número de una cifra).

---

## Respuesta Final

$$\boxed{\text{El número original es } 36}$$

**Verificación:** 
- Número invertido: $63$
- Diferencia: $63 - 36 = 27$ ✓
- Suma de dígitos: $3 + 6 = 9$ ✓

> 📚 Volver a: [FUN-03-Problemas](../../problems/FUN-03-Problemas.md)
