<!--
HUMANO:
Métodos para calcular derivadas.

IA:
Cada método tiene: cuándo usar, pasos, ejemplo.

---
content_type: methods
expected_output:
  default: markdown
audience: self-study
---
-->

# Métodos de Diferenciación

---

## Método 1: Derivación Directa (Fórmulas Básicas)

### Cuándo Usar
- Funciones elementales o combinaciones simples

### Pasos
1. Identificar el tipo de función
2. Aplicar la fórmula correspondiente
3. Simplificar

### Ejemplo
$$\frac{d}{dx}[3x^4 - 2x^2 + 5x - 7] = 12x^3 - 4x + 5$$

---

## Método 2: Regla del Producto

### Cuándo Usar
- Producto de dos funciones $f(x) \cdot g(x)$

### Fórmula
$(fg)' = f'g + fg'$

### Pasos
1. Identificar $f$ y $g$
2. Calcular $f'$ y $g'$
3. Aplicar: $f'g + fg'$

### Ejemplo
$$\frac{d}{dx}[x^2 \sin x] = 2x \sin x + x^2 \cos x$$

---

## Método 3: Regla del Cociente

### Cuándo Usar
- Cociente de funciones $\frac{f(x)}{g(x)}$

### Fórmula
$$\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$$

### Mnemónico
"Lo de abajo por la derivada de arriba, menos lo de arriba por la derivada de abajo, todo sobre lo de abajo al cuadrado"

### Ejemplo
$$\frac{d}{dx}\left[\frac{x^2}{x+1}\right] = \frac{2x(x+1) - x^2(1)}{(x+1)^2} = \frac{x^2 + 2x}{(x+1)^2}$$

---

## Método 4: Regla de la Cadena

### Cuándo Usar
- Funciones compuestas $f(g(x))$
- Funciones "de algo"

### Fórmula
$$[f(g(x))]' = f'(g(x)) \cdot g'(x)$$

### Pasos
1. Identificar la función exterior e interior
2. Derivar la exterior, manteniendo la interior
3. Multiplicar por la derivada de la interior

### Ejemplo
$$\frac{d}{dx}[\sin(x^2)] = \cos(x^2) \cdot 2x = 2x\cos(x^2)$$

---

## Método 5: Derivación Implícita

### Cuándo Usar
- La variable $y$ no está despejada
- Ecuaciones que relacionan $x$ e $y$

### Pasos
1. Derivar término por término respecto a $x$
2. Usar la regla de la cadena: $\frac{d}{dx}[y^n] = ny^{n-1}\frac{dy}{dx}$
3. Reunir términos con $\frac{dy}{dx}$ a un lado
4. Factorizar y despejar $\frac{dy}{dx}$

### Ejemplo
Para $x^2 + xy + y^3 = 7$:
$$2x + y + x\frac{dy}{dx} + 3y^2\frac{dy}{dx} = 0$$
$$\frac{dy}{dx}(x + 3y^2) = -2x - y$$
$$\frac{dy}{dx} = \frac{-2x - y}{x + 3y^2}$$

---

## Método 6: Derivación Logarítmica

### Cuándo Usar
- Productos/cocientes complicados
- Potencias variables: $[f(x)]^{g(x)}$

### Pasos
1. Tomar $\ln$ de ambos lados
2. Usar propiedades de logaritmos para simplificar
3. Derivar implícitamente
4. Despejar $\frac{dy}{dx}$ y sustituir $y$

### Ejemplo
Para $y = \frac{x^2\sqrt{x+1}}{(x-1)^3}$:

$$\ln y = 2\ln x + \frac{1}{2}\ln(x+1) - 3\ln(x-1)$$

$$\frac{1}{y}\frac{dy}{dx} = \frac{2}{x} + \frac{1}{2(x+1)} - \frac{3}{x-1}$$

$$\frac{dy}{dx} = y\left[\frac{2}{x} + \frac{1}{2(x+1)} - \frac{3}{x-1}\right]$$

---

## Método 7: Derivadas de Funciones Inversas

### Cuándo Usar
- Funciones trigonométricas inversas
- Cualquier función inversa

### Fórmula
Si $y = f^{-1}(x)$, entonces $\frac{dy}{dx} = \frac{1}{f'(y)}$

### Ejemplo
Para $y = \arcsin x$:
$$\sin y = x$$
$$\cos y \cdot \frac{dy}{dx} = 1$$
$$\frac{dy}{dx} = \frac{1}{\cos y} = \frac{1}{\sqrt{1-\sin^2 y}} = \frac{1}{\sqrt{1-x^2}}$$

---

## Método 8: Derivada por Definición

### Cuándo Usar
- Demostrar fórmulas
- Funciones especiales no cubiertas por reglas

### Fórmula
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

### Ejemplo
Para $f(x) = \sqrt{x}$:
$$f'(x) = \lim_{h \to 0} \frac{\sqrt{x+h} - \sqrt{x}}{h} = \lim_{h \to 0} \frac{(x+h) - x}{h(\sqrt{x+h} + \sqrt{x})} = \frac{1}{2\sqrt{x}}$$

---

## Método 9: Cadena Múltiple

### Cuándo Usar
- Composiciones de tres o más funciones

### Fórmula
$$[f(g(h(x)))]' = f'(g(h(x))) \cdot g'(h(x)) \cdot h'(x)$$

### Ejemplo
$$\frac{d}{dx}[\sin(\cos(x^2))] = \cos(\cos(x^2)) \cdot (-\sin(x^2)) \cdot 2x$$

---

## Método 10: Derivadas Paramétricas

### Cuándo Usar
- Curvas definidas por $x = f(t)$, $y = g(t)$

### Fórmula
$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{g'(t)}{f'(t)}$$

### Segunda Derivada
$$\frac{d^2y}{dx^2} = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{dx/dt}$$

### Ejemplo
Si $x = t^2$, $y = t^3$:
$$\frac{dy}{dx} = \frac{3t^2}{2t} = \frac{3t}{2}$$

---

## Método 11: Derivación de Funciones Definidas por Partes

### Cuándo Usar
- Funciones con diferentes expresiones en distintos intervalos

### Pasos
1. Derivar cada pieza en su intervalo
2. Verificar continuidad en los puntos de unión
3. Verificar si los límites laterales de la derivada coinciden

### Ejemplo
$f(x) = \begin{cases} x^2 & x \leq 1 \\ 2x-1 & x > 1 \end{cases}$

$f'(x) = \begin{cases} 2x & x < 1 \\ 2 & x > 1 \end{cases}$

En $x = 1$: $\lim_{x \to 1^-} f'(x) = 2 = \lim_{x \to 1^+} f'(x)$, así que $f'(1) = 2$.

---

## Método 12: Derivadas Sucesivas

### Cuándo Usar
- Se necesita $f''$, $f'''$, etc.
- Análisis de concavidad
- Expansiones de Taylor

### Pasos
1. Calcular $f'$
2. Derivar $f'$ para obtener $f''$
3. Repetir según se necesite

### Ejemplo
$f(x) = x^4 - 3x^2 + 2$
$f'(x) = 4x^3 - 6x$
$f''(x) = 12x^2 - 6$
$f'''(x) = 24x$
$f^{(4)}(x) = 24$
$f^{(n)}(x) = 0$ para $n \geq 5$
