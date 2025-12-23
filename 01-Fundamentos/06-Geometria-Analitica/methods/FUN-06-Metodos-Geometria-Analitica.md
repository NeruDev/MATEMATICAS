<!--
HUMANO:
Procedimientos sistemáticos para resolver problemas de geometría analítica.

IA:
Incluye fórmulas, pasos claros y ejemplos resueltos.
Cada método debe incluir verificación.

---
content_type: methods_comprehensive
expected_output:
  default: markdown
audience: self-study
---
-->

# Métodos de Geometría Analítica

---

## Método 1: Calcular Distancia y Punto Medio

### Objetivo
Encontrar la distancia entre dos puntos y el punto medio del segmento que los une.

### Procedimiento
1. Identifica las coordenadas: $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$
2. **Distancia:** $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$
3. **Punto medio:** $M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$

### Ejemplo
Encuentra la distancia y punto medio entre $A(3, -2)$ y $B(-1, 4)$.

**Distancia:**
$$d = \sqrt{(-1-3)^2 + (4-(-2))^2} = \sqrt{(-4)^2 + (6)^2} = \sqrt{16 + 36} = \sqrt{52} = 2\sqrt{13}$$

**Punto medio:**
$$M = \left(\frac{3+(-1)}{2}, \frac{-2+4}{2}\right) = \left(\frac{2}{2}, \frac{2}{2}\right) = (1, 1)$$

### Verificación
La distancia de $A$ a $M$ debe ser la mitad de $AB$:
$$AM = \sqrt{(1-3)^2 + (1-(-2))^2} = \sqrt{4+9} = \sqrt{13}$$
$\sqrt{13} = \frac{2\sqrt{13}}{2}$ ✓

---

## Método 2: Encontrar la Ecuación de una Recta

### Objetivo
Determinar la ecuación de una recta dados diferentes elementos.

### Caso 2.1: Punto y Pendiente
**Fórmula:** $y - y_1 = m(x - x_1)$

**Ejemplo:** Recta con pendiente $m = -3$ que pasa por $(2, 5)$.
$$y - 5 = -3(x - 2)$$
$$y = -3x + 6 + 5 = -3x + 11$$

### Caso 2.2: Dos Puntos
**Procedimiento:**
1. Calcula la pendiente: $m = \frac{y_2-y_1}{x_2-x_1}$
2. Usa forma punto-pendiente

**Ejemplo:** Recta por $A(1, 3)$ y $B(4, -6)$.
$$m = \frac{-6-3}{4-1} = \frac{-9}{3} = -3$$
$$y - 3 = -3(x - 1) \Rightarrow y = -3x + 6$$

### Caso 2.3: Paralela a otra recta
**Procedimiento:** Usa la misma pendiente que la recta dada.

**Ejemplo:** Recta paralela a $2x - 3y + 5 = 0$ que pasa por $(1, 4)$.

Pendiente de la recta dada: $m = \frac{2}{3}$
$$y - 4 = \frac{2}{3}(x - 1)$$
$$3y - 12 = 2x - 2 \Rightarrow 2x - 3y + 10 = 0$$

### Caso 2.4: Perpendicular a otra recta
**Procedimiento:** Usa pendiente negativa recíproca: $m_\perp = -\frac{1}{m}$

**Ejemplo:** Recta perpendicular a $y = 4x - 1$ que pasa por $(8, 2)$.

Pendiente original: $m = 4$, pendiente perpendicular: $m_\perp = -\frac{1}{4}$
$$y - 2 = -\frac{1}{4}(x - 8)$$
$$y = -\frac{x}{4} + 2 + 2 = -\frac{x}{4} + 4$$

---

## Método 3: Distancia de un Punto a una Recta

### Objetivo
Calcular la distancia perpendicular de un punto a una recta.

### Procedimiento
1. Escribe la recta en forma general: $Ax + By + C = 0$
2. Aplica: $d = \frac{\lvert Ax_0 + By_0 + C \rvert}{\sqrt{A^2 + B^2}}$

### Ejemplo
Encuentra la distancia de $P(3, -1)$ a la recta $4x - 3y + 2 = 0$.

$$d = \frac{\lvert 4(3) - 3(-1) + 2 \rvert}{\sqrt{4^2 + (-3)^2}} = \frac{\lvert 12 + 3 + 2 \rvert}{\sqrt{16 + 9}} = \frac{17}{5} = 3.4$$

### Verificación
Podemos encontrar el pie de la perpendicular y verificar la distancia directamente.

---

## Método 4: Identificar una Circunferencia desde su Ecuación General

### Objetivo
Convertir la ecuación general a forma estándar para identificar centro y radio.

### Procedimiento
1. Agrupa términos en $x$ y términos en $y$
2. Completa el cuadrado para cada variable
3. Identifica $(h, k)$ y $r$

### Ejemplo
Identifica el centro y radio de $x^2 + y^2 - 6x + 4y - 12 = 0$.

**Paso 1:** Agrupa y reorganiza
$$(x^2 - 6x) + (y^2 + 4y) = 12$$

**Paso 2:** Completa cuadrados
$$(x^2 - 6x + 9) + (y^2 + 4y + 4) = 12 + 9 + 4$$
$$(x - 3)^2 + (y + 2)^2 = 25$$

**Paso 3:** Identifica
- Centro: $(3, -2)$
- Radio: $r = 5$

### Verificación
Sustituye un punto de la circunferencia, por ejemplo $(8, -2)$:
$(8-3)^2 + (-2+2)^2 = 25 + 0 = 25$ ✓

---

## Método 5: Encontrar la Ecuación de una Circunferencia

### Caso 5.1: Centro y Radio conocidos
**Fórmula:** $(x - h)^2 + (y - k)^2 = r^2$

### Caso 5.2: Centro y un punto sobre la circunferencia
**Procedimiento:**
1. Calcula el radio como distancia del centro al punto
2. Escribe la ecuación

**Ejemplo:** Centro $C(2, -3)$ que pasa por $P(6, 0)$.
$$r = \sqrt{(6-2)^2 + (0-(-3))^2} = \sqrt{16 + 9} = 5$$
$$(x - 2)^2 + (y + 3)^2 = 25$$

### Caso 5.3: Tres puntos sobre la circunferencia
**Procedimiento:**
1. Sustituye cada punto en $x^2 + y^2 + Dx + Ey + F = 0$
2. Resuelve el sistema de 3 ecuaciones con 3 incógnitas

### Caso 5.4: Diámetro conocido (extremos)
**Procedimiento:**
1. Centro = punto medio del diámetro
2. Radio = mitad de la longitud del diámetro

---

## Método 6: Determinar Intersección Recta-Circunferencia

### Objetivo
Encontrar los puntos donde una recta corta a una circunferencia.

### Procedimiento
1. Despeja una variable de la ecuación de la recta
2. Sustituye en la ecuación de la circunferencia
3. Resuelve la ecuación cuadrática resultante
4. Encuentra las coordenadas de intersección

### Ejemplo
Encuentra la intersección de $y = x + 1$ con $x^2 + y^2 = 25$.

**Paso 1:** Sustituye $y = x + 1$:
$$x^2 + (x + 1)^2 = 25$$
$$x^2 + x^2 + 2x + 1 = 25$$
$$2x^2 + 2x - 24 = 0$$
$$x^2 + x - 12 = 0$$

**Paso 2:** Resuelve
$$(x + 4)(x - 3) = 0 \Rightarrow x = -4 \text{ o } x = 3$$

**Paso 3:** Encuentra $y$
- Si $x = -4$: $y = -4 + 1 = -3$ → Punto $(-4, -3)$
- Si $x = 3$: $y = 3 + 1 = 4$ → Punto $(3, 4)$

### Verificación
$(-4)^2 + (-3)^2 = 16 + 9 = 25$ ✓
$3^2 + 4^2 = 9 + 16 = 25$ ✓

---

## Método 7: Identificar una Parábola y sus Elementos

### Objetivo
Dado una ecuación de parábola, identificar vértice, foco, directriz y eje.

### Procedimiento
1. Identifica la orientación según la forma de la ecuación
2. Completa el cuadrado si es necesario
3. Extrae $p$ de la forma $4p$
4. Calcula los elementos

### Ejemplo
Identifica los elementos de $y^2 - 8y - 4x + 28 = 0$.

**Paso 1:** Completa el cuadrado en $y$
$$y^2 - 8y = 4x - 28$$
$$y^2 - 8y + 16 = 4x - 28 + 16$$
$$(y - 4)^2 = 4x - 12 = 4(x - 3)$$

**Paso 2:** Identifica
Forma $(y - k)^2 = 4p(x - h)$ con $4p = 4 \Rightarrow p = 1$

**Paso 3:** Elementos
- Vértice: $V(3, 4)$
- Abre hacia: derecha ($p > 0$)
- Foco: $F(3 + 1, 4) = (4, 4)$
- Directriz: $x = 3 - 1 = 2$
- Eje: $y = 4$

---

## Método 8: Identificar una Elipse y sus Elementos

### Objetivo
Convertir la ecuación a forma estándar y extraer los elementos.

### Procedimiento
1. Completa cuadrados en $x$ e $y$ si es necesario
2. Divide para obtener 1 en el lado derecho
3. Identifica $a^2$ y $b^2$ (el mayor es $a^2$)
4. Calcula $c = \sqrt{a^2 - b^2}$
5. Determina la orientación del eje mayor

### Ejemplo
Analiza $9x^2 + 25y^2 - 36x + 50y - 164 = 0$.

**Paso 1:** Agrupa y completa cuadrados
$$9(x^2 - 4x) + 25(y^2 + 2y) = 164$$
$$9(x^2 - 4x + 4) + 25(y^2 + 2y + 1) = 164 + 36 + 25$$
$$9(x - 2)^2 + 25(y + 1)^2 = 225$$

**Paso 2:** Divide entre 225
$$\frac{(x-2)^2}{25} + \frac{(y+1)^2}{9} = 1$$

**Paso 3:** Identifica
- $a^2 = 25 \Rightarrow a = 5$
- $b^2 = 9 \Rightarrow b = 3$
- Centro: $(2, -1)$
- Eje mayor: horizontal (porque $a^2$ está bajo $(x-2)^2$)
- $c = \sqrt{25 - 9} = 4$

**Elementos:**
- Vértices: $(2 \pm 5, -1) = (-3, -1)$ y $(7, -1)$
- Focos: $(2 \pm 4, -1) = (-2, -1)$ y $(6, -1)$
- Excentricidad: $e = \frac{4}{5} = 0.8$

---

## Método 9: Identificar una Hipérbola y sus Elementos

### Objetivo
Convertir la ecuación a forma estándar y encontrar los elementos.

### Procedimiento
1. Completa cuadrados
2. Observa cuál término es positivo (ese determina el eje real)
3. Identifica $a^2$ y $b^2$
4. Calcula $c = \sqrt{a^2 + b^2}$
5. Encuentra asíntotas

### Ejemplo
Analiza $4x^2 - 9y^2 - 16x - 18y - 29 = 0$.

**Paso 1:** Agrupa
$$4(x^2 - 4x) - 9(y^2 + 2y) = 29$$
$$4(x^2 - 4x + 4) - 9(y^2 + 2y + 1) = 29 + 16 - 9$$
$$4(x - 2)^2 - 9(y + 1)^2 = 36$$

**Paso 2:** Divide entre 36
$$\frac{(x-2)^2}{9} - \frac{(y+1)^2}{4} = 1$$

**Paso 3:** Identifica
- $a^2 = 9 \Rightarrow a = 3$ (bajo el término positivo)
- $b^2 = 4 \Rightarrow b = 2$
- Centro: $(2, -1)$
- Eje real: horizontal
- $c = \sqrt{9 + 4} = \sqrt{13}$

**Elementos:**
- Vértices: $(2 \pm 3, -1) = (-1, -1)$ y $(5, -1)$
- Focos: $(2 \pm \sqrt{13}, -1)$
- Asíntotas: $y + 1 = \pm\frac{2}{3}(x - 2)$
- Excentricidad: $e = \frac{\sqrt{13}}{3} \approx 1.20$

---

## Método 10: Clasificar una Cónica por su Ecuación General

### Objetivo
Determinar qué tipo de cónica representa $Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$.

### Procedimiento
1. Calcula el discriminante: $\Delta = B^2 - 4AC$
2. Clasifica según el signo de $\Delta$:
   - $\Delta < 0$: Elipse (o circunferencia si $A = C$ y $B = 0$)
   - $\Delta = 0$: Parábola
   - $\Delta > 0$: Hipérbola
3. Verifica casos degenerados

### Ejemplo 1
Clasifica $3x^2 + 2xy + 3y^2 - 8x + 2y + 1 = 0$.

$A = 3$, $B = 2$, $C = 3$
$$\Delta = 2^2 - 4(3)(3) = 4 - 36 = -32 < 0$$

Es una **elipse** (rotada, por tener término $xy$).

### Ejemplo 2
Clasifica $x^2 - 4xy + 4y^2 + x - 2y - 6 = 0$.

$A = 1$, $B = -4$, $C = 4$
$$\Delta = (-4)^2 - 4(1)(4) = 16 - 16 = 0$$

Es una **parábola** (o caso degenerado).

---

## Método 11: Encontrar la Tangente a una Cónica en un Punto

### Para Circunferencia $x^2 + y^2 = r^2$ en $P(x_0, y_0)$:
$$x \cdot x_0 + y \cdot y_0 = r^2$$

### Para Elipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ en $P(x_0, y_0)$:
$$\frac{x \cdot x_0}{a^2} + \frac{y \cdot y_0}{b^2} = 1$$

### Para Hipérbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ en $P(x_0, y_0)$:
$$\frac{x \cdot x_0}{a^2} - \frac{y \cdot y_0}{b^2} = 1$$

### Para Parábola $y^2 = 4px$ en $P(x_0, y_0)$:
$$y \cdot y_0 = 2p(x + x_0)$$

### Ejemplo
Encuentra la tangente a $x^2 + y^2 = 25$ en $(3, 4)$.

$$x(3) + y(4) = 25$$
$$3x + 4y = 25$$

**Verificación:** El punto $(3, 4)$ satisface: $3(3) + 4(4) = 9 + 16 = 25$ ✓

---

## Método 12: Resolver Problemas de Aplicación con Geometría Analítica

### Procedimiento General
1. Define un sistema de coordenadas conveniente
2. Traduce las condiciones geométricas a ecuaciones
3. Resuelve el sistema
4. Interpreta geométricamente la solución

### Ejemplo: Encontrar el lugar geométrico
Encuentra el lugar geométrico de los puntos que equidistan de $A(0, 4)$ y la recta $y = -4$.

**Paso 1:** Sea $P(x, y)$ un punto del lugar geométrico.

**Paso 2:** Distancia de $P$ a $A$: $\sqrt{x^2 + (y-4)^2}$

Distancia de $P$ a la recta $y = -4$: $\lvert y + 4 \rvert$

**Paso 3:** Igualamos:
$$\sqrt{x^2 + (y-4)^2} = \lvert y + 4 \rvert$$
$$x^2 + (y-4)^2 = (y+4)^2$$
$$x^2 + y^2 - 8y + 16 = y^2 + 8y + 16$$
$$x^2 = 16y$$

**Conclusión:** Es una parábola con vértice en el origen, $4p = 16$, $p = 4$, foco en $(0, 4)$ y directriz $y = -4$. ✓
