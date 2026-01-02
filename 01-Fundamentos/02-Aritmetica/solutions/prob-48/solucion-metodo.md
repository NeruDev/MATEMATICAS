<!--
::METADATA::
type: solution
topic_id: fun-02-aritmetica
file_id: prob-48-solucion
problem_ref: Prob-48
status: stable
audience: student
-->

# Solución: Fracción compleja

## Problema
Simplifica: $\frac{\frac{3}{4} - \frac{2}{3}}{\frac{5}{6} + \frac{1}{4}}$

---

## Método: Simplificación por partes

### Paso 1: Simplificar el numerador
$$\frac{3}{4} - \frac{2}{3}$$

**Encontrar [MCM](../../../../glossary.md#mcm)(4, 3):**
- $4 = 2^2$
- $3 = 3$
- $\text{[MCM](../../../../glossary.md#mcm)} = 2^2 \times 3 = 12$

**Convertir fracciones:**
$$\frac{3}{4} = \frac{3 \times 3}{4 \times 3} = \frac{9}{12}$$
$$\frac{2}{3} = \frac{2 \times 4}{3 \times 4} = \frac{8}{12}$$

**Restar:**
$$\frac{9}{12} - \frac{8}{12} = \frac{1}{12}$$

### Paso 2: Simplificar el denominador
$$\frac{5}{6} + \frac{1}{4}$$

**Encontrar MCM(6, 4):**
- $6 = 2 \times 3$
- $4 = 2^2$
- $\text{MCM} = 2^2 \times 3 = 12$

**Convertir fracciones:**
$$\frac{5}{6} = \frac{5 \times 2}{6 \times 2} = \frac{10}{12}$$
$$\frac{1}{4} = \frac{1 \times 3}{4 \times 3} = \frac{3}{12}$$

**Sumar:**
$$\frac{10}{12} + \frac{3}{12} = \frac{13}{12}$$

### Paso 3: Dividir las fracciones resultantes
$$\frac{\frac{1}{12}}{\frac{13}{12}} = \frac{1}{12} \times \frac{12}{13}$$

### Paso 4: Simplificar
$$= \frac{1 \times 12}{12 \times 13} = \frac{12}{156}$$

Simplificando (dividiendo entre 12):
$$= \frac{1}{13}$$

---

## Respuesta Final
$$\frac{\frac{3}{4} - \frac{2}{3}}{\frac{5}{6} + \frac{1}{4}} = \boxed{\frac{1}{13}}$$

---

## Verificación
- Numerador: $\frac{3}{4} - \frac{2}{3} = 0.75 - 0.666... = 0.0833...$
- Denominador: $\frac{5}{6} + \frac{1}{4} = 0.833... + 0.25 = 1.0833...$
- División: $\frac{0.0833...}{1.0833...} = \frac{1/12}{13/12} = \frac{1}{13} = 0.076923...$ ✓
