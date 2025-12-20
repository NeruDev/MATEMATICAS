<!--
HUMANO:
Métodos para evaluar límites.

IA:
Cada método tiene: cuándo usar, pasos, ejemplo.

---
content_type: methods
expected_output:
  default: markdown
audience: self-study
---
-->

# Métodos para Evaluar Límites

---

## Método 1: Sustitución Directa

### Cuándo Usar
- La función es continua en el punto
- No produce formas indeterminadas

### Pasos
1. Sustituir $x = a$ en $f(x)$
2. Calcular el valor numérico

### Ejemplo
$$\lim_{x \to 3} (x^2 + 2x - 1) = 3^2 + 2(3) - 1 = 9 + 6 - 1 = 14$$

---

## Método 2: Factorización

### Cuándo Usar
- Forma indeterminada $\frac{0}{0}$
- Numerador y denominador son polinomios

### Pasos
1. Factorizar numerador y denominador
2. Cancelar factor común $(x - a)$
3. Sustituir en la expresión simplificada

### Ejemplo
$$\lim_{x \to 3} \frac{x^2 - 9}{x - 3} = \lim_{x \to 3} \frac{(x-3)(x+3)}{x-3} = \lim_{x \to 3} (x+3) = 6$$

---

## Método 3: Racionalización

### Cuándo Usar
- Forma $\frac{0}{0}$ con radicales
- Expresiones con diferencia de raíces

### Pasos
1. Multiplicar por el conjugado arriba y abajo
2. Usar $(a-b)(a+b) = a^2 - b^2$
3. Simplificar y evaluar

### Ejemplo
$$\lim_{x \to 4} \frac{\sqrt{x} - 2}{x - 4} = \lim_{x \to 4} \frac{(\sqrt{x}-2)(\sqrt{x}+2)}{(x-4)(\sqrt{x}+2)} = \lim_{x \to 4} \frac{x-4}{(x-4)(\sqrt{x}+2)} = \frac{1}{4}$$

---

## Método 4: División entre Mayor Potencia

### Cuándo Usar
- Límites al infinito
- Funciones racionales

### Pasos
1. Identificar la mayor potencia de $x$ en el denominador
2. Dividir cada término entre esa potencia
3. Aplicar $\lim_{x \to \infty} \frac{1}{x^n} = 0$

### Ejemplo
$$\lim_{x \to \infty} \frac{3x^2 + 5x}{2x^2 - 1} = \lim_{x \to \infty} \frac{3 + \frac{5}{x}}{2 - \frac{1}{x^2}} = \frac{3 + 0}{2 - 0} = \frac{3}{2}$$

---

## Método 5: Límites Trigonométricos Fundamentales

### Cuándo Usar
- Expresiones con $\sin x$, $\cos x$ cuando $x \to 0$
- Formas que se pueden convertir a $\frac{\sin u}{u}$

### Fórmulas Base
$$\lim_{u \to 0} \frac{\sin u}{u} = 1 \qquad \lim_{u \to 0} \frac{1 - \cos u}{u} = 0$$

### Pasos
1. Manipular para obtener la forma $\frac{\sin u}{u}$
2. Usar sustitución si el argumento no es $x$
3. Aplicar la fórmula fundamental

### Ejemplo
$$\lim_{x \to 0} \frac{\sin 3x}{x} = \lim_{x \to 0} \frac{\sin 3x}{3x} \cdot 3 = 1 \cdot 3 = 3$$

---

## Método 6: Multiplicar por 1 en Forma Conveniente

### Cuándo Usar
- Límites trigonométricos compuestos
- Cuando se necesita introducir un factor

### Pasos
1. Identificar qué factor falta para usar una identidad
2. Multiplicar por $\frac{\text{factor}}{\text{factor}} = 1$
3. Reorganizar y evaluar

### Ejemplo
$$\lim_{x \to 0} \frac{\tan x}{x} = \lim_{x \to 0} \frac{\sin x}{x} \cdot \frac{1}{\cos x} = 1 \cdot 1 = 1$$

---

## Método 7: Teorema del Emparedado

### Cuándo Usar
- Funciones difíciles de evaluar directamente
- Se pueden encontrar cotas superior e inferior

### Pasos
1. Encontrar $g(x) \leq f(x) \leq h(x)$ cerca del punto
2. Calcular $\lim g(x)$ y $\lim h(x)$
3. Si ambos límites son iguales a $L$, entonces $\lim f(x) = L$

### Ejemplo
$$\lim_{x \to 0} x^2 \sin\frac{1}{x}$$

Como $-1 \leq \sin\frac{1}{x} \leq 1$, entonces $-x^2 \leq x^2\sin\frac{1}{x} \leq x^2$

Como $\lim_{x \to 0} (-x^2) = \lim_{x \to 0} x^2 = 0$, entonces el límite es $0$.

---

## Método 8: Cambio de Variable

### Cuándo Usar
- Simplificar expresiones complicadas
- Límites con composición de funciones

### Pasos
1. Hacer $u = g(x)$ para alguna parte de la expresión
2. Determinar $u \to ?$ cuando $x \to a$
3. Reescribir el límite en términos de $u$
4. Evaluar

### Ejemplo
$$\lim_{x \to 0} \frac{\sin(x^2)}{x^2}$$

Sea $u = x^2$. Cuando $x \to 0$, $u \to 0$.

$$\lim_{u \to 0} \frac{\sin u}{u} = 1$$

---

## Método 9: Límites Laterales

### Cuándo Usar
- Funciones definidas por partes
- Funciones con valor absoluto
- Verificar existencia del límite

### Pasos
1. Calcular $\lim_{x \to a^-} f(x)$
2. Calcular $\lim_{x \to a^+} f(x)$
3. Si son iguales, ese es el límite; si no, el límite no existe

### Ejemplo
Para $f(x) = \frac{\lvert x \rvert}{x}$:

$\lim_{x \to 0^+} \frac{\lvert x \rvert}{x} = \frac{x}{x} = 1$

$\lim_{x \to 0^-} \frac{\lvert x \rvert}{x} = \frac{-x}{x} = -1$

Como $1 \neq -1$, el límite no existe.

---

## Método 10: Análisis de Asíntotas

### Cuándo Usar
- Encontrar comportamiento asintótico
- Límites infinitos o al infinito

### Pasos para Asíntota Vertical
1. Encontrar donde el denominador es cero
2. Evaluar límites laterales en ese punto
3. Si alguno es $\pm\infty$, hay asíntota vertical

### Pasos para Asíntota Horizontal
1. Calcular $\lim_{x \to \infty} f(x)$
2. Calcular $\lim_{x \to -\infty} f(x)$
3. Si el límite es $L$ finito, $y = L$ es asíntota horizontal

### Ejemplo
$f(x) = \frac{1}{x-2}$

Asíntota vertical: $x = 2$ (el denominador es 0)
Asíntota horizontal: $y = 0$ (porque $\lim_{x \to \pm\infty} \frac{1}{x-2} = 0$)

---

## Método 11: Factorización de Diferencia de Potencias

### Cuándo Usar
- Expresiones como $x^n - a^n$

### Fórmulas
$$x^n - a^n = (x-a)(x^{n-1} + x^{n-2}a + \cdots + xa^{n-2} + a^{n-1})$$

### Ejemplo
$$\lim_{x \to 2} \frac{x^3 - 8}{x - 2} = \lim_{x \to 2} \frac{(x-2)(x^2+2x+4)}{x-2} = 4 + 4 + 4 = 12$$

---

## Método 12: Fracciones Complejas

### Cuándo Usar
- Límites con fracciones dentro de fracciones

### Pasos
1. Encontrar el común denominador de las fracciones internas
2. Simplificar a una sola fracción
3. Evaluar el límite

### Ejemplo
$$\lim_{h \to 0} \frac{\frac{1}{x+h} - \frac{1}{x}}{h} = \lim_{h \to 0} \frac{\frac{x - (x+h)}{x(x+h)}}{h} = \lim_{h \to 0} \frac{-h}{hx(x+h)} = \frac{-1}{x^2}$$
