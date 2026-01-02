<!--
::METADATA::
type: solution
topic_id: fun-02-aritmetica
file_id: FUN-02-Prob-78-Solucion
status: stable
audience: student
problem_ref: "[Prob-78]"
methods: ["sistema de ecuaciones", "[sustitución](../../../../glossary.md#sustitucion)", "razones equivalentes"]
-->

# Solución [Prob-78]: Problema de edades con razones

> **Problema:** La edad de Ana y Beto están en razón 3:5. En 10 años estarán en razón 5:7. ¿Cuántos años tiene cada uno?

---

## Método 1: Sistema de ecuaciones con sustitución

### Paso 1: Definir las variables

Sea:
- $A$ = edad actual de Ana
- $B$ = edad actual de Beto

### Paso 2: Traducir las condiciones a ecuaciones

**Condición 1:** Las edades actuales están en razón 3:5
$$\frac{A}{B} = \frac{3}{5}$$

Esto implica:
$$5A = 3B \quad \Rightarrow \quad A = \frac{3B}{5} \quad \text{...(1)}$$

**Condición 2:** En 10 años estarán en razón 5:7
$$\frac{A + 10}{B + 10} = \frac{5}{7}$$

Esto implica:
$$7(A + 10) = 5(B + 10) \quad \text{...(2)}$$

### Paso 3: Desarrollar la ecuación (2)

$$7A + 70 = 5B + 50$$
$$7A = 5B - 20 \quad \text{...(2')}$$

### Paso 4: Sustituir (1) en (2')

Sustituyendo $A = \frac{3B}{5}$:

$$7 \cdot \frac{3B}{5} = 5B - 20$$

$$\frac{21B}{5} = 5B - 20$$

### Paso 5: Resolver para B

Multiplicamos por 5 para eliminar el denominador:
$$21B = 25B - 100$$

$$21B - 25B = -100$$

$$-4B = -100$$

$$B = 25$$

### Paso 6: Encontrar A

Sustituyendo en (1):
$$A = \frac{3 \cdot 25}{5} = \frac{75}{5} = 15$$

### Verificación

**Verificar razón actual:**
$$\frac{A}{B} = \frac{15}{25} = \frac{3}{5} \checkmark$$

**Verificar razón en 10 años:**
$$\frac{A + 10}{B + 10} = \frac{15 + 10}{25 + 10} = \frac{25}{35} = \frac{5}{7} \checkmark$$

---

## Método 2: Usando constante de proporcionalidad

### Paso 1: Expresar las edades con una constante

Si las edades están en razón 3:5, podemos escribir:
- Edad de Ana: $A = 3k$
- Edad de Beto: $B = 5k$

donde $k$ es una constante positiva.

### Paso 2: Aplicar la segunda condición

En 10 años:
- Edad de Ana: $3k + 10$
- Edad de Beto: $5k + 10$

La razón será 5:7:
$$\frac{3k + 10}{5k + 10} = \frac{5}{7}$$

### Paso 3: Resolver para k

Multiplicando en cruz:
$$7(3k + 10) = 5(5k + 10)$$

$$21k + 70 = 25k + 50$$

$$70 - 50 = 25k - 21k$$

$$20 = 4k$$

$$k = 5$$

### Paso 4: Calcular las edades

- **Edad de Ana:** $A = 3k = 3(5) = 15$ años
- **Edad de Beto:** $B = 5k = 5(5) = 25$ años

### Verificación

Igual que en el Método 1: ✓

---

## Método 3: Análisis algebraico directo

### Paso 1: Establecer la diferencia de edades

De la razón 3:5, si Ana tiene 3 partes, Beto tiene 5 partes.
La diferencia es 5 - 3 = 2 partes.

### Paso 2: Analizar cómo cambian las razones

| Tiempo | Ana | Beto | Diferencia |
|--------|-----|------|------------|
| Actual | $3k$ | $5k$ | $2k$ |
| En 10 años | $3k+10$ | $5k+10$ | $2k$ |

La diferencia de edades **siempre es la misma**: $2k$.

### Paso 3: Usar la razón futura

En 10 años, la razón es 5:7. La diferencia en esa razón es:
$$7 - 5 = 2 \text{ partes (de la nueva razón)}$$

Entonces:
$$2k = 2 \cdot \frac{(5k + 10)}{7}$$

Pero es más directo: si la diferencia $2k$ corresponde a 2 partes de la razón 5:7:

Una parte de la razón futura = $\frac{2k}{2} = k$

La edad de Ana en 10 años = 5 partes = $5 \cdot \text{(una parte)} = \frac{5 \cdot 2k}{2} = 5k$

Pero también sabemos que en 10 años Ana tendrá $3k + 10$.

$$3k + 10 = \frac{5 \cdot 2k}{2} = 5k$$

Esto no es correcto directamente. Mejor usar:

Si en 10 años las partes son 5 y 7, y la diferencia sigue siendo $2k$:
$$7 \text{ partes} - 5 \text{ partes} = 2 \text{ partes (futura)}$$

Una parte futura = $\frac{2k}{2} = k$... 

Mejor continuar con los métodos anteriores que son más directos.

---

## Resumen de la solución

| Persona | Edad actual | Edad en 10 años |
|---------|-------------|-----------------|
| Ana | 15 años | 25 años |
| Beto | 25 años | 35 años |

- Razón actual: $15:25 = 3:5$ ✓
- Razón futura: $25:35 = 5:7$ ✓

---

## Respuesta Final

**Ana tiene 15 años y Beto tiene 25 años.**

$$\boxed{A = 15 \text{ años}, \quad B = 25 \text{ años}}$$

> 📚 Volver a: [FUN-02-Problemas](../../problems/FUN-02-Problemas.md)
