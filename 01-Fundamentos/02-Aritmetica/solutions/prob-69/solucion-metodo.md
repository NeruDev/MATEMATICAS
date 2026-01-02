<!--
::METADATA::
type: solution
topic_id: fun-02-aritmetica
file_id: FUN-02-Prob-69-Solucion
status: stable
audience: student
problem_ref: "[Prob-69]"
methods: ["leyes de exponentes", "simplificación algebraica"]
-->

# Solución [Prob-69]: Exponentes algebraicos

> **Problema:** Simplifica: $(a^2 b^{-3})^{-2} \times (a^{-1} b^2)^3$

---

## Método 1: Aplicación directa de leyes de exponentes

### Paso 1: Identificar las leyes de exponentes necesarias

Las leyes que aplicaremos son:
- **Potencia de una potencia:** $(x^m)^n = x^{m \cdot n}$
- **Potencia de un producto:** $(xy)^n = x^n \cdot y^n$
- **Producto de potencias con la misma [base](../../../../glossary.md#base):** $x^m \cdot x^n = x^{m+n}$

### Paso 2: Aplicar la potencia de un producto a cada factor

**Primer factor:** $(a^2 b^{-3})^{-2}$

Aplicamos $(xy)^n = x^n \cdot y^n$:
$$(a^2 b^{-3})^{-2} = (a^2)^{-2} \cdot (b^{-3})^{-2}$$

**Segundo factor:** $(a^{-1} b^2)^3$

$$(a^{-1} b^2)^3 = (a^{-1})^3 \cdot (b^2)^3$$

### Paso 3: Aplicar la potencia de una potencia

**Primer factor:**
$$(a^2)^{-2} \cdot (b^{-3})^{-2} = a^{2 \cdot (-2)} \cdot b^{(-3) \cdot (-2)} = a^{-4} \cdot b^{6}$$

**Segundo factor:**
$$(a^{-1})^3 \cdot (b^2)^3 = a^{(-1) \cdot 3} \cdot b^{2 \cdot 3} = a^{-3} \cdot b^{6}$$

### Paso 4: Multiplicar ambos factores

Ahora multiplicamos los resultados:
$$(a^{-4} \cdot b^{6}) \times (a^{-3} \cdot b^{6})$$

Agrupamos las potencias con la misma [base](../../../../glossary.md#base):
$$= a^{-4} \cdot a^{-3} \cdot b^{6} \cdot b^{6}$$

### Paso 5: Aplicar producto de potencias con la misma base

$$= a^{-4 + (-3)} \cdot b^{6 + 6}$$
$$= a^{-7} \cdot b^{12}$$

### Paso 6: Expresar con exponentes positivos (forma estándar)

Como $a^{-7} = \frac{1}{a^7}$, la expresión final es:

$$a^{-7} b^{12} = \frac{b^{12}}{a^7}$$

### Verificación

Verificamos con valores numéricos. Sea $a = 2$ y $b = 1$:

**Expresión original:**
$$(2^2 \cdot 1^{-3})^{-2} \times (2^{-1} \cdot 1^2)^3 = (4 \cdot 1)^{-2} \times (0.5 \cdot 1)^3$$
$$= 4^{-2} \times 0.5^3 = \frac{1}{16} \times \frac{1}{8} = \frac{1}{128}$$

**Resultado simplificado:**
$$\frac{1^{12}}{2^7} = \frac{1}{128}$$

✓ Los resultados coinciden.

---

## Método 2: Trabajar con los exponentes directamente

### Paso 1: Expresar cada base con su exponente total

Para la base $a$:
- Del primer factor: $2 \times (-2) = -4$
- Del segundo factor: $(-1) \times 3 = -3$
- **Total:** $-4 + (-3) = -7$

Para la base $b$:
- Del primer factor: $(-3) \times (-2) = 6$
- Del segundo factor: $2 \times 3 = 6$
- **Total:** $6 + 6 = 12$

### Paso 2: Escribir el resultado

$$a^{-7} \cdot b^{12} = \frac{b^{12}}{a^7}$$

---

## Respuesta Final

$$\boxed{\frac{b^{12}}{a^7}} \quad \text{o equivalentemente} \quad \boxed{a^{-7}b^{12}}$$

> 📚 Volver a: [FUN-02-Problemas](../../problems/FUN-02-Problemas.md)
