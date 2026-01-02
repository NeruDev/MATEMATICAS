<!--
::METADATA::
type: solution
topic_id: fun-02-aritmetica
file_id: FUN-02-Prob-40-Solucion
status: stable
audience: student
problem_ref: "[Prob-40]"
methods: ["relación [MCD](../../../../glossary.md#mcd)-[MCM](../../../../glossary.md#mcm)-producto", "[factorización](../../../../glossary.md#factorizacion) prima", "análisis de divisores"]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../glossary.md)

---

# Solución [Prob-40]: Encontrar n dado MCD y MCM

> **Problema:** Si $\text{[MCD](../../../../glossary.md#mcd)}(n, 12) = 4$ y $\text{[MCM](../../../../glossary.md#mcm)}(n, 12) = 60$, encuentra $n$.

---

## Método 1: Relación MCD · MCM = a · b

### Paso 1: Recordar la propiedad fundamental

Para cualesquiera dos números positivos $a$ y $b$:

$$\text{MCD}(a, b) \times \text{MCM}(a, b) = a \times b$$

### Paso 2: Aplicar la fórmula

En nuestro caso, $a = n$ y $b = 12$:

$$\text{MCD}(n, 12) \times \text{MCM}(n, 12) = n \times 12$$

Sustituyendo los valores dados:
$$4 \times 60 = n \times 12$$

### Paso 3: Resolver para n

$$240 = 12n$$

$$n = \frac{240}{12}$$

$$n = 20$$

### Verificación

Comprobemos que $n = 20$ satisface las condiciones:

**Verificar MCD(20, 12) = 4:**
- Divisores de 20: $\{1, 2, 4, 5, 10, 20\}$
- Divisores de 12: $\{1, 2, 3, 4, 6, 12\}$
- Divisores comunes: $\{1, 2, 4\}$
- MCD(20, 12) = 4 ✓

**Verificar MCM(20, 12) = 60:**

Usando la fórmula: $\text{MCM}(20, 12) = \frac{20 \times 12}{\text{MCD}(20, 12)} = \frac{240}{4} = 60$ ✓

---

## Método 2: Factorización Prima

### Paso 1: Factorizar 12

$$12 = 2^2 \times 3^1$$

### Paso 2: Expresar n en términos de factores primos

Sea $n = 2^a \times 3^b \times k$, donde $k$ es un entero sin factores 2 ni 3.

### Paso 3: Usar la condición MCD(n, 12) = 4

$$\text{MCD}(n, 12) = 2^{\min(a, 2)} \times 3^{\min(b, 1)} = 4 = 2^2$$

Esto implica:
- $\min(a, 2) = 2 \Rightarrow a \geq 2$
- $\min(b, 1) = 0 \Rightarrow b = 0$

### Paso 4: Usar la condición MCM(n, 12) = 60

Primero, factoricemos 60:
$$60 = 2^2 \times 3^1 \times 5^1$$

$$\text{MCM}(n, 12) = 2^{\max(a, 2)} \times 3^{\max(b, 1)} \times (\text{otros factores de } n)$$

Igualando a 60:
$$2^{\max(a, 2)} \times 3^{\max(0, 1)} \times k = 2^2 \times 3^1 \times 5^1$$

Esto nos da:
- $\max(a, 2) = 2 \Rightarrow a \leq 2$

Combinando con $a \geq 2$ del paso anterior: $a = 2$

- $\max(0, 1) = 1$ ✓ (se cumple automáticamente)
- $k = 5^1 = 5$ (los factores restantes)

### Paso 5: Construir n

$$n = 2^2 \times 3^0 \times 5^1 = 4 \times 1 \times 5 = 20$$

---

## Método 3: Análisis de Divisores

### Paso 1: Usar que MCD(n, 12) = 4

Esto significa que:
- $4 \mid n$ (4 divide a n)
- $4 \mid 12$ ✓ (esto es cierto)
- No hay divisor común mayor que 4

Entonces $n$ es múltiplo de 4: $n \in \{4, 8, 12, 16, 20, 24, ...\}$

Pero $\text{MCD}(n, 12) = 4$, no puede ser mayor. Esto excluye valores donde el MCD sería mayor:
- $n = 12$: MCD(12, 12) = 12 ✗
- $n = 24$: MCD(24, 12) = 12 ✗
- $n = 36$: MCD(36, 12) = 12 ✗

Candidatos restantes que son múltiplos de 4 pero no de 3 (para evitar MCD > 4):
$$n \in \{4, 8, 16, 20, 28, 32, 40, 44, 52, 56, ...\}$$

### Paso 2: Usar que MCM(n, 12) = 60

El MCM de n y 12 debe ser 60.

Probemos candidatos:

| $n$ | $\text{MCD}(n, 12)$ | $\text{MCM}(n, 12) = \frac{n \times 12}{\text{MCD}}$ |
|-----|---------------------|------------------------------------------------------|
| 4 | 4 | $\frac{48}{4} = 12$ ✗ |
| 8 | 4 | $\frac{96}{4} = 24$ ✗ |
| 16 | 4 | $\frac{192}{4} = 48$ ✗ |
| **20** | **4** | $\frac{240}{4} = 60$ ✓ |
| 28 | 4 | $\frac{336}{4} = 84$ ✗ |

### Paso 3: Confirmar la solución

$n = 20$ es el único valor que satisface ambas condiciones.

---

## Demostración de la Fórmula MCD × MCM = a × b

Para completar la comprensión, demostremos por qué funciona esta fórmula:

Sean $a = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdots p_k^{\alpha_k}$ y $b = p_1^{\beta_1} \cdot p_2^{\beta_2} \cdots p_k^{\beta_k}$

Entonces:
- $\text{MCD}(a,b) = p_1^{\min(\alpha_1, \beta_1)} \cdot p_2^{\min(\alpha_2, \beta_2)} \cdots$
- $\text{MCM}(a,b) = p_1^{\max(\alpha_1, \beta_1)} \cdot p_2^{\max(\alpha_2, \beta_2)} \cdots$

Como $\min(x, y) + \max(x, y) = x + y$ para cualesquiera $x, y$:

$$\text{MCD} \times \text{MCM} = \prod_{i} p_i^{\min(\alpha_i, \beta_i) + \max(\alpha_i, \beta_i)} = \prod_{i} p_i^{\alpha_i + \beta_i} = a \times b$$

---

## Respuesta Final

$$\boxed{n = 20}$$

**Verificación completa:**
- $\text{MCD}(20, 12) = 4$ ✓
- $\text{MCM}(20, 12) = 60$ ✓
- $\text{MCD} \times \text{MCM} = 4 \times 60 = 240 = 20 \times 12$ ✓

---

> 📚 Volver a: [FUN-02-Problemas](../../problems/FUN-02-Problemas.md)
