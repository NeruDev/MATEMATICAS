<!--
::METADATA::
type: solution
topic_id: fun-02-aritmetica
file_id: FUN-02-Prob-70-Solucion
status: stable
audience: student
problem_ref: "[Prob-70]"
methods: ["ecuación de punto fijo", "ecuación cuadrática", "análisis de [convergencia](../../../../glossary.md#convergencia)"]
-->

# Solución [Prob-70]: Radical anidado infinito

> **Problema:** Calcula: $\sqrt{12 + \sqrt{12 + \sqrt{12 + ...}}}$ (valor exacto).

---

## Método 1: Ecuación de punto fijo

### Paso 1: Definir la expresión como una variable

Sea $x$ el valor del radical anidado infinito:
$$x = \sqrt{12 + \sqrt{12 + \sqrt{12 + ...}}}$$

### Paso 2: Observar la estructura recursiva

Notemos que la expresión dentro de la primera raíz también es el mismo radical infinito:
$$x = \sqrt{12 + \underbrace{\sqrt{12 + \sqrt{12 + ...}}}_{= x}}$$

Por lo tanto:
$$x = \sqrt{12 + x}$$

### Paso 3: Elevar al cuadrado ambos lados

$$x^2 = 12 + x$$

### Paso 4: Resolver la ecuación cuadrática

Reordenamos:
$$x^2 - x - 12 = 0$$

Factorizamos buscando dos números que multipliquen $-12$ y sumen $-1$:
- Los números son $-4$ y $3$

$$(x - 4)(x + 3) = 0$$

### Paso 5: Encontrar las soluciones

$$x - 4 = 0 \quad \Rightarrow \quad x = 4$$
$$x + 3 = 0 \quad \Rightarrow \quad x = -3$$

### Paso 6: Seleccionar la solución válida

Como $x$ representa una raíz cuadrada, debe ser **no negativo**.

Por lo tanto, descartamos $x = -3$ y aceptamos:
$$x = 4$$

### Verificación

Comprobamos que $x = 4$ satisface la ecuación:
$$\sqrt{12 + 4} = \sqrt{16} = 4 \checkmark$$

También podemos verificar numéricamente calculando iteraciones:
- $a_1 = \sqrt{12} \approx 3.464$
- $a_2 = \sqrt{12 + 3.464} \approx 3.932$
- $a_3 = \sqrt{12 + 3.932} \approx 3.991$
- $a_4 = \sqrt{12 + 3.991} \approx 3.999$
- $a_n \to 4$

✓ La sucesión converge a 4.

---

## Método 2: Fórmula general usando la cuadrática

### Paso 1: Aplicar la fórmula cuadrática

Para $x^2 - x - 12 = 0$, con $a = 1$, $b = -1$, $c = -12$:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = \frac{1 \pm \sqrt{1 + 48}}{2} = \frac{1 \pm \sqrt{49}}{2} = \frac{1 \pm 7}{2}$$

### Paso 2: Calcular las soluciones

$$x_1 = \frac{1 + 7}{2} = \frac{8}{2} = 4$$
$$x_2 = \frac{1 - 7}{2} = \frac{-6}{2} = -3$$

### Paso 3: Seleccionar la solución válida

Como el radical debe ser positivo: $x = 4$

---

## Método 3: Análisis de convergencia (complementario)

### Paso 1: Definir la sucesión

Sea $a_1 = \sqrt{12}$ y $a_{n+1} = \sqrt{12 + a_n}$

### Paso 2: Demostrar que la sucesión está acotada

**Cota superior:** Si $a_n < 4$, entonces:
$$a_{n+1} = \sqrt{12 + a_n} < \sqrt{12 + 4} = \sqrt{16} = 4$$

Como $a_1 = \sqrt{12} \approx 3.46 < 4$, por inducción $a_n < 4$ para todo $n$.

**Cota inferior:** $a_n > 0$ para todo $n$ (por ser raíces cuadradas).

### Paso 3: Demostrar que la sucesión es creciente

$$a_{n+1}^2 - a_n^2 = (12 + a_n) - a_n^2 = 12 + a_n - a_n^2$$

Para $0 < a_n < 4$:
$$12 + a_n - a_n^2 = -(a_n^2 - a_n - 12) = -(a_n - 4)(a_n + 3) > 0$$

Por lo tanto, $a_{n+1} > a_n$ (sucesión creciente).

### Paso 4: Conclusión

Por el teorema de convergencia monótona:
- La sucesión es creciente y acotada superiormente
- Por lo tanto, converge
- El [límite](../../../../glossary.md#límite) satisface $L = \sqrt{12 + L}$, lo que da $L = 4$

---

## Nota: Forma general

Para radicales de la forma $\sqrt{n + \sqrt{n + \sqrt{n + ...}}}$, el valor es:
$$x = \frac{1 + \sqrt{1 + 4n}}{2}$$

Para $n = 12$:
$$x = \frac{1 + \sqrt{1 + 48}}{2} = \frac{1 + 7}{2} = 4$$

---

## Respuesta Final

$$\boxed{4}$$

> 📚 Volver a: [FUN-02-Problemas](../../problems/FUN-02-Problemas.md)
