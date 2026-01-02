<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: FUN-03-Prob-49-Solucion
status: stable
audience: student
problem_ref: "[Prob-49]"
methods: ["fracciones-complejas", "[mcm](../../../../glossary.md#mcm)", "simplificacion-algebraica"]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../glossary.md)

---

# Solución [Prob-49]: Fracción compleja - simplificación

> **Problema:** Simplifica la fracción compleja: $\displaystyle\frac{\frac{1}{x} - \frac{1}{y}}{\frac{1}{x} + \frac{1}{y}}$

## Método 1: Multiplicar por el MCM

### Paso 1: Identificar la fracción compleja

$$\frac{\frac{1}{x} - \frac{1}{y}}{\frac{1}{x} + \frac{1}{y}}$$

Esta es una fracción donde tanto el numerador como el denominador contienen fracciones.

### Paso 2: Encontrar el MCM de los denominadores internos

Los denominadores internos son $x$ e $y$.

$$\text{[MCM](../../../../glossary.md#mcm)}(x, y) = xy$$

### Paso 3: Multiplicar numerador y denominador por el MCM

Multiplicamos toda la fracción compleja por $\displaystyle\frac{xy}{xy}$:

$$\frac{\frac{1}{x} - \frac{1}{y}}{\frac{1}{x} + \frac{1}{y}} \cdot \frac{xy}{xy} = \frac{\left(\frac{1}{x} - \frac{1}{y}\right) \cdot xy}{\left(\frac{1}{x} + \frac{1}{y}\right) \cdot xy}$$

### Paso 4: Distribuir $xy$ en el numerador

$$\left(\frac{1}{x} - \frac{1}{y}\right) \cdot xy = \frac{1}{x} \cdot xy - \frac{1}{y} \cdot xy$$

$$= \frac{xy}{x} - \frac{xy}{y}$$

$$= y - x$$

### Paso 5: Distribuir $xy$ en el denominador

$$\left(\frac{1}{x} + \frac{1}{y}\right) \cdot xy = \frac{1}{x} \cdot xy + \frac{1}{y} \cdot xy$$

$$= \frac{xy}{x} + \frac{xy}{y}$$

$$= y + x$$

### Paso 6: Escribir el resultado

$$\frac{y - x}{y + x}$$

O equivalentemente:

$$\frac{y - x}{x + y}$$

---

## Método 2: Simplificar numerador y denominador por separado

### Paso 1: Simplificar el numerador

$$\frac{1}{x} - \frac{1}{y}$$

Para restar fracciones, encontramos denominador común:

$$= \frac{1 \cdot y}{x \cdot y} - \frac{1 \cdot x}{y \cdot x}$$

$$= \frac{y}{xy} - \frac{x}{xy}$$

$$= \frac{y - x}{xy}$$

### Paso 2: Simplificar el denominador

$$\frac{1}{x} + \frac{1}{y}$$

$$= \frac{1 \cdot y}{x \cdot y} + \frac{1 \cdot x}{y \cdot x}$$

$$= \frac{y}{xy} + \frac{x}{xy}$$

$$= \frac{y + x}{xy}$$

### Paso 3: Formar la fracción de fracciones

$$\frac{\frac{y - x}{xy}}{\frac{y + x}{xy}}$$

### Paso 4: Dividir fracciones (multiplicar por el recíproco)

$$= \frac{y - x}{xy} \cdot \frac{xy}{y + x}$$

### Paso 5: Simplificar

$$= \frac{(y - x) \cdot xy}{xy \cdot (y + x)}$$

$$= \frac{(y - x) \cdot \cancel{xy}}{\cancel{xy} \cdot (y + x)}$$

$$= \frac{y - x}{y + x}$$

---

## Método 3: Sustitución de variables auxiliares

### Paso 1: Hacer sustituciones

Sea $u = \frac{1}{x}$ y $v = \frac{1}{y}$

La expresión se convierte en:

$$\frac{u - v}{u + v}$$

### Paso 2: Sustituir de vuelta

$$u = \frac{1}{x} \quad \Rightarrow \quad x = \frac{1}{u}$$

$$v = \frac{1}{y} \quad \Rightarrow \quad y = \frac{1}{v}$$

### Paso 3: Expresar en términos de $x$ e $y$

$$\frac{u - v}{u + v} = \frac{\frac{1}{x} - \frac{1}{y}}{\frac{1}{x} + \frac{1}{y}}$$

Siguiendo el Método 1 ó 2:

$$= \frac{y - x}{y + x}$$

---

## Formas equivalentes de la respuesta

La respuesta puede escribirse de varias formas equivalentes:

1. $$\frac{y - x}{y + x}$$

2. $$\frac{y - x}{x + y}$$

3. $$\frac{-(x - y)}{x + y} = -\frac{x - y}{x + y}$$

4. $$\frac{y - x}{x + y} = \frac{-(x - y)}{x + y}$$

---

## Verificación numérica

Probemos con $x = 2$ e $y = 6$:

**Expresión original:**

$$\frac{\frac{1}{2} - \frac{1}{6}}{\frac{1}{2} + \frac{1}{6}}$$

Calculando el numerador:
$$\frac{1}{2} - \frac{1}{6} = \frac{3}{6} - \frac{1}{6} = \frac{2}{6} = \frac{1}{3}$$

Calculando el denominador:
$$\frac{1}{2} + \frac{1}{6} = \frac{3}{6} + \frac{1}{6} = \frac{4}{6} = \frac{2}{3}$$

División:
$$\frac{\frac{1}{3}}{\frac{2}{3}} = \frac{1}{3} \cdot \frac{3}{2} = \frac{1}{2}$$

**Resultado simplificado:**

$$\frac{y - x}{y + x} = \frac{6 - 2}{6 + 2} = \frac{4}{8} = \frac{1}{2} \quad \checkmark$$

---

## Restricciones del dominio

La expresión está definida cuando:

1. $x \neq 0$ (para que exista $\frac{1}{x}$)
2. $y \neq 0$ (para que exista $\frac{1}{y}$)
3. $\frac{1}{x} + \frac{1}{y} \neq 0$, es decir, $x + y \neq 0$ o $y \neq -x$

**[Dominio](../../../../glossary.md#dominio):** $\{(x, y) \in \mathbb{R}^2 : x \neq 0, y \neq 0, x \neq -y\}$

---

## Respuesta Final

$$\frac{\frac{1}{x} - \frac{1}{y}}{\frac{1}{x} + \frac{1}{y}} = \boxed{\frac{y - x}{x + y}}$$

> 📚 Volver a: [FUN-03-Problemas](../../problems/FUN-03-Problemas.md)
