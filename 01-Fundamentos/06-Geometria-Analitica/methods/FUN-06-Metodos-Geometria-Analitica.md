# Métodos de Geometría Analítica

> Guía completa de métodos de geometría analítica con algoritmos detallados, tablas de procedimientos y ejemplos paso a paso.

---

## Método 1: Calcular Distancia entre Dos Puntos

**Cuándo Usar:** Para encontrar la longitud del segmento entre dos puntos dados.

### Fórmula

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar coordenadas | $(x_1, y_1)$ y $(x_2, y_2)$ |
| 2 | Calcular diferencias | $\Delta x = x_2 - x_1$, $\Delta y = y_2 - y_1$ |
| 3 | Elevar al cuadrado | $(\Delta x)^2$ y $(\Delta y)^2$ |
| 4 | Sumar y extraer raíz | $d = \sqrt{(\Delta x)^2 + (\Delta y)^2}$ |

### Ejemplo Detallado

**Problema:** Hallar la distancia entre $A(-3, 2)$ y $B(5, -4)$.

---

**Paso 1: Identificar coordenadas**

$$x_1 = -3, \quad y_1 = 2, \quad x_2 = 5, \quad y_2 = -4$$

---

**Paso 2: Calcular diferencias**

$$\Delta x = 5 - (-3) = 8$$
$$\Delta y = -4 - 2 = -6$$

---

**Paso 3: Aplicar fórmula**

$$d = \sqrt{8^2 + (-6)^2} = \sqrt{64 + 36} = \sqrt{100} = 10$$

---

**Verificación:** Los catetos forman una terna pitagórica $(6, 8, 10)$ ✓

$$\boxed{d(A, B) = 10}$$

---

## Método 2: Encontrar Punto Medio de un Segmento

**Cuándo Usar:** Para hallar el centro de un segmento o verificar bisectrices.

### Fórmula

$$M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$$

### División en Razón $m:n$

Para dividir el segmento $\overline{P_1P_2}$ en razón $m:n$:

$$P = \left(\frac{nx_1 + mx_2}{m + n}, \frac{ny_1 + my_2}{m + n}\right)$$

### Ejemplo Detallado

**Problema:** Hallar el punto que divide al segmento de $A(2, -1)$ a $B(8, 5)$ en razón $2:3$.

---

**Paso 1: Identificar datos**

$$P_1 = A(2, -1), \quad P_2 = B(8, 5), \quad m = 2, \quad n = 3$$

---

**Paso 2: Aplicar fórmula**

$$x = \frac{3(2) + 2(8)}{2 + 3} = \frac{6 + 16}{5} = \frac{22}{5} = 4.4$$

$$y = \frac{3(-1) + 2(5)}{2 + 3} = \frac{-3 + 10}{5} = \frac{7}{5} = 1.4$$

---

**Verificación:** El punto está más cerca de $A$ (a $\frac{2}{5}$ del camino)

$$AP = \sqrt{(4.4-2)^2 + (1.4-(-1))^2} = \sqrt{5.76 + 5.76} = \sqrt{11.52} \approx 3.39$$

$$PB = \sqrt{(8-4.4)^2 + (5-1.4)^2} = \sqrt{12.96 + 12.96} = \sqrt{25.92} \approx 5.09$$

$$\frac{AP}{PB} = \frac{3.39}{5.09} \approx \frac{2}{3} \checkmark$$

$$\boxed{P = \left(\frac{22}{5}, \frac{7}{5}\right) = (4.4, 1.4)}$$

---

## Método 3: Determinar la Ecuación de una Recta

**Cuándo Usar:** Cuando necesitas expresar algebraicamente una línea recta.

### Formas de la Ecuación

| Forma | Ecuación | Datos Necesarios |
|-------|----------|------------------|
| Pendiente-ordenada | $y = mx + b$ | Pendiente y ordenada al origen |
| Punto-pendiente | $y - y_1 = m(x - x_1)$ | Un punto y la pendiente |
| Dos puntos | $\frac{y - y_1}{y_2 - y_1} = \frac{x - x_1}{x_2 - x_1}$ | Dos puntos |
| General | $Ax + By + C = 0$ | Forma estándar |
| Simétrica | $\frac{x}{a} + \frac{y}{b} = 1$ | Intersecciones con ejes |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar datos | Puntos y/o pendiente |
| 2 | Calcular pendiente | $m = \frac{y_2 - y_1}{x_2 - x_1}$ si es necesario |
| 3 | Seleccionar forma | Según datos disponibles |
| 4 | Sustituir valores | En la ecuación elegida |
| 5 | Simplificar | A la forma deseada |

### Ejemplo Detallado

**Problema:** Hallar la ecuación de la recta que pasa por $A(3, -2)$ y $B(-1, 6)$ en todas sus formas.

---

**Paso 1: Calcular pendiente**

$$m = \frac{6 - (-2)}{-1 - 3} = \frac{8}{-4} = -2$$

---

**Paso 2: Forma punto-pendiente** (usando punto $A$)

$$y - (-2) = -2(x - 3)$$
$$y + 2 = -2x + 6$$

---

**Paso 3: Forma pendiente-ordenada**

$$y = -2x + 4$$

---

**Paso 4: Forma general**

$$2x + y - 4 = 0$$

---

**Paso 5: Forma simétrica**

De $y = -2x + 4$:
- Intersección con eje $x$: $0 = -2x + 4 \Rightarrow x = 2$
- Intersección con eje $y$: $y = 4$

$$\frac{x}{2} + \frac{y}{4} = 1$$

---

**Verificación:** Sustituir ambos puntos

- $A(3, -2)$: $2(3) + (-2) - 4 = 6 - 2 - 4 = 0$ ✓
- $B(-1, 6)$: $2(-1) + 6 - 4 = -2 + 6 - 4 = 0$ ✓

$$\boxed{y = -2x + 4 \text{ o } 2x + y - 4 = 0}$$

---

## Método 4: Calcular Distancia de un Punto a una Recta

**Cuándo Usar:** Para encontrar la perpendicular más corta desde un punto a una línea.

### Fórmula

Para la recta $Ax + By + C = 0$ y el punto $P(x_0, y_0)$:

$$d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Llevar a forma general | $Ax + By + C = 0$ |
| 2 | Identificar coeficientes | $A$, $B$, $C$ |
| 3 | Sustituir punto | En el numerador |
| 4 | Calcular denominador | $\sqrt{A^2 + B^2}$ |
| 5 | Aplicar valor absoluto | Y dividir |

### Ejemplo Detallado

**Problema:** Hallar la distancia del punto $P(4, -1)$ a la recta $3x - 4y + 5 = 0$.

---

**Paso 1: Identificar coeficientes**

$$A = 3, \quad B = -4, \quad C = 5$$

---

**Paso 2: Sustituir en fórmula**

$$d = \frac{|3(4) + (-4)(-1) + 5|}{\sqrt{3^2 + (-4)^2}}$$

$$d = \frac{|12 + 4 + 5|}{\sqrt{9 + 16}}$$

$$d = \frac{|21|}{\sqrt{25}} = \frac{21}{5} = 4.2$$

---

**Verificación geométrica:**

Encontrar el pie de la perpendicular y calcular distancia directamente.

La perpendicular tiene pendiente $m_\perp = -\frac{1}{m} = -\frac{4}{3}$ (la recta original tiene $m = \frac{3}{4}$)

Ecuación de la perpendicular por $P(4, -1)$:
$$y + 1 = -\frac{4}{3}(x - 4)$$
$$3y + 3 = -4x + 16$$
$$4x + 3y - 13 = 0$$

Intersección con $3x - 4y + 5 = 0$:

Multiplicando y sumando para eliminar:
$$16x + 12y - 52 = 0$$
$$9x - 12y + 15 = 0$$
$$25x - 37 = 0 \Rightarrow x = \frac{37}{25}$$

$$y = \frac{3(\frac{37}{25}) + 5}{4} = \frac{\frac{111 + 125}{25}}{4} = \frac{236}{100} = 2.36$$

Distancia: $d = \sqrt{(4 - 1.48)^2 + (-1 - 2.36)^2} \approx 4.2$ ✓

$$\boxed{d = \frac{21}{5} = 4.2}$$

---

## Método 5: Determinar Rectas Paralelas y Perpendiculares

**Cuándo Usar:** Para construir o verificar relaciones entre rectas.

### Condiciones

| Relación | Condición (pendientes) | Condición (general) |
|----------|------------------------|---------------------|
| Paralelas | $m_1 = m_2$ | $\frac{A_1}{A_2} = \frac{B_1}{B_2}$ |
| Perpendiculares | $m_1 \cdot m_2 = -1$ | $A_1A_2 + B_1B_2 = 0$ |

### Ejemplo Detallado

**Problema:** Hallar la ecuación de la recta que pasa por $P(2, 3)$ y es:
a) Paralela a $4x - 2y + 7 = 0$
b) Perpendicular a $4x - 2y + 7 = 0$

---

**Paso 1: Hallar pendiente de la recta dada**

$$4x - 2y + 7 = 0 \Rightarrow y = 2x + \frac{7}{2}$$

$$m = 2$$

---

**a) Recta paralela:**

$$m_{\parallel} = 2$$

Por $P(2, 3)$:
$$y - 3 = 2(x - 2)$$
$$y = 2x - 1$$
$$\boxed{2x - y - 1 = 0}$$

---

**b) Recta perpendicular:**

$$m_{\perp} = -\frac{1}{m} = -\frac{1}{2}$$

Por $P(2, 3)$:
$$y - 3 = -\frac{1}{2}(x - 2)$$
$$2y - 6 = -x + 2$$
$$\boxed{x + 2y - 8 = 0}$$

---

**Verificación:**

- Paralela: $m = 2$ y recta original $m = 2$ ✓
- Perpendicular: $2 \times (-\frac{1}{2}) = -1$ ✓
- Ambas pasan por $(2, 3)$: 
  - $2(2) - 3 - 1 = 0$ ✓
  - $2 + 2(3) - 8 = 0$ ✓

---

## Método 6: Ecuación de la Circunferencia

**Cuándo Usar:** Para representar o analizar círculos en el plano.

### Formas de la Ecuación

| Forma | Ecuación | Información Directa |
|-------|----------|---------------------|
| Canónica | $(x - h)^2 + (y - k)^2 = r^2$ | Centro $(h, k)$, radio $r$ |
| General | $x^2 + y^2 + Dx + Ey + F = 0$ | Expandida |

### Relación entre Formas

$$h = -\frac{D}{2}, \quad k = -\frac{E}{2}, \quad r = \sqrt{h^2 + k^2 - F}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar forma | Canónica o general |
| 2 | Si general → canónica | Completar el cuadrado |
| 3 | Extraer elementos | Centro y radio |
| 4 | Verificar existencia | $r^2 > 0$ para circunferencia real |

### Ejemplo Detallado

**Problema:** Hallar centro y radio de $x^2 + y^2 - 6x + 4y - 12 = 0$.

---

**Paso 1: Agrupar términos**

$$(x^2 - 6x) + (y^2 + 4y) = 12$$

---

**Paso 2: Completar cuadrados**

Para $x$: $\left(\frac{-6}{2}\right)^2 = 9$

Para $y$: $\left(\frac{4}{2}\right)^2 = 4$

$$(x^2 - 6x + 9) + (y^2 + 4y + 4) = 12 + 9 + 4$$

$$(x - 3)^2 + (y + 2)^2 = 25$$

---

**Paso 3: Identificar elementos**

- Centro: $C(3, -2)$
- Radio: $r = \sqrt{25} = 5$

---

**Verificación:** Sustituir el centro en la ecuación general:

$$3^2 + (-2)^2 - 6(3) + 4(-2) - 12 = 9 + 4 - 18 - 8 - 12 = -25$$

Distancia del centro a cualquier punto de la circunferencia = 5 ✓

$$\boxed{C(3, -2), \quad r = 5}$$

---

### Ejemplo: Ecuación dados tres puntos

**Problema:** Hallar la circunferencia que pasa por $A(0, 0)$, $B(6, 0)$ y $C(0, 8)$.

---

**Método:** Usar forma general $x^2 + y^2 + Dx + Ey + F = 0$

**Sustituir cada punto:**

- $A(0,0)$: $0 + 0 + 0 + 0 + F = 0 \Rightarrow F = 0$
- $B(6,0)$: $36 + 0 + 6D + 0 + 0 = 0 \Rightarrow D = -6$
- $C(0,8)$: $0 + 64 + 0 + 8E + 0 = 0 \Rightarrow E = -8$

**Ecuación:**

$$x^2 + y^2 - 6x - 8y = 0$$

**Centro y radio:**

$$h = 3, \quad k = 4, \quad r = \sqrt{9 + 16 - 0} = 5$$

$$\boxed{(x-3)^2 + (y-4)^2 = 25}$$

---

## Método 7: Ecuación de la Parábola

**Cuándo Usar:** Para representar parábolas con vértice y eje conocidos.

### Formas Canónicas

| Orientación | Ecuación | Foco | Directriz |
|-------------|----------|------|-----------|
| Abre derecha | $(y - k)^2 = 4p(x - h)$ | $(h + p, k)$ | $x = h - p$ |
| Abre izquierda | $(y - k)^2 = -4p(x - h)$ | $(h - p, k)$ | $x = h + p$ |
| Abre arriba | $(x - h)^2 = 4p(y - k)$ | $(h, k + p)$ | $y = k - p$ |
| Abre abajo | $(x - h)^2 = -4p(y - k)$ | $(h, k - p)$ | $y = k + p$ |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar forma | Por la variable al cuadrado |
| 2 | Completar cuadrado | Si es necesario |
| 3 | Determinar $4p$ | Del coeficiente |
| 4 | Calcular elementos | Vértice, foco, directriz, eje |

### Ejemplo Detallado

**Problema:** Analizar la parábola $y^2 - 4y - 8x + 20 = 0$.

---

**Paso 1: Agrupar y completar el cuadrado en $y$**

$$y^2 - 4y = 8x - 20$$
$$(y^2 - 4y + 4) = 8x - 20 + 4$$
$$(y - 2)^2 = 8x - 16$$
$$(y - 2)^2 = 8(x - 2)$$

---

**Paso 2: Identificar forma canónica**

$$(y - k)^2 = 4p(x - h)$$

Con $h = 2$, $k = 2$, $4p = 8 \Rightarrow p = 2$

---

**Paso 3: Calcular elementos**

- **Vértice:** $V(2, 2)$
- **Foco:** $F(h + p, k) = F(4, 2)$
- **Directriz:** $x = h - p = 0$
- **Eje de simetría:** $y = 2$
- **Lado recto:** $|LR| = |4p| = 8$

---

**Verificación:** La distancia del vértice al foco = distancia del vértice a la directriz = $p = 2$ ✓

$$\boxed{V(2, 2), \quad F(4, 2), \quad \text{Directriz: } x = 0}$$

---

## Método 8: Ecuación de la Elipse

**Cuándo Usar:** Para representar óvalos con dos focos.

### Formas Canónicas (centro en origen)

| Eje mayor | Ecuación | Relación |
|-----------|----------|----------|
| Horizontal | $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ | $a > b$ |
| Vertical | $\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1$ | $a > b$ |

### Elementos de la Elipse

| Elemento | Descripción | Fórmula |
|----------|-------------|---------|
| Semieje mayor | $a$ | Mayor denominador bajo raíz |
| Semieje menor | $b$ | Menor denominador bajo raíz |
| Distancia focal | $c$ | $c^2 = a^2 - b^2$ |
| Excentricidad | $e$ | $e = \frac{c}{a}$ (siempre $0 < e < 1$) |
| Vértices | | $(\pm a, 0)$ o $(0, \pm a)$ |
| Focos | | $(\pm c, 0)$ o $(0, \pm c)$ |

### Ejemplo Detallado

**Problema:** Hallar los elementos de $\frac{x^2}{25} + \frac{y^2}{9} = 1$.

---

**Paso 1: Identificar $a^2$ y $b^2$**

$$a^2 = 25 \Rightarrow a = 5$$
$$b^2 = 9 \Rightarrow b = 3$$

Como $a^2$ está bajo $x^2$, el eje mayor es horizontal.

---

**Paso 2: Calcular $c$**

$$c^2 = a^2 - b^2 = 25 - 9 = 16$$
$$c = 4$$

---

**Paso 3: Identificar elementos**

- **Centro:** $C(0, 0)$
- **Vértices:** $V_1(-5, 0)$, $V_2(5, 0)$
- **Focos:** $F_1(-4, 0)$, $F_2(4, 0)$
- **Extremos eje menor:** $(0, -3)$, $(0, 3)$
- **Excentricidad:** $e = \frac{4}{5} = 0.8$

---

**Verificación:** Para cualquier punto $P$ de la elipse: $PF_1 + PF_2 = 2a = 10$

Para $P(5, 0)$:
$$PF_1 = |5 - (-4)| = 9, \quad PF_2 = |5 - 4| = 1$$
$$PF_1 + PF_2 = 10 \checkmark$$

$$\boxed{a = 5, \quad b = 3, \quad c = 4, \quad e = 0.8}$$

---

## Método 9: Ecuación de la Hipérbola

**Cuándo Usar:** Para representar curvas con dos ramas y dos focos.

### Formas Canónicas (centro en origen)

| Eje transverso | Ecuación | Asíntotas |
|----------------|----------|-----------|
| Horizontal | $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ | $y = \pm\frac{b}{a}x$ |
| Vertical | $\frac{y^2}{a^2} - \frac{x^2}{b^2} = 1$ | $y = \pm\frac{a}{b}x$ |

### Elementos de la Hipérbola

| Elemento | Descripción | Fórmula |
|----------|-------------|---------|
| Semieje transverso | $a$ | Bajo el término positivo |
| Semieje conjugado | $b$ | Bajo el término negativo |
| Distancia focal | $c$ | $c^2 = a^2 + b^2$ |
| Excentricidad | $e$ | $e = \frac{c}{a}$ (siempre $e > 1$) |

### Ejemplo Detallado

**Problema:** Analizar la hipérbola $\frac{x^2}{16} - \frac{y^2}{9} = 1$.

---

**Paso 1: Identificar $a^2$ y $b^2$**

$$a^2 = 16 \Rightarrow a = 4$$ (término positivo)
$$b^2 = 9 \Rightarrow b = 3$$

Eje transverso horizontal (el término con $x^2$ es positivo).

---

**Paso 2: Calcular $c$**

$$c^2 = a^2 + b^2 = 16 + 9 = 25$$
$$c = 5$$

---

**Paso 3: Identificar elementos**

- **Centro:** $C(0, 0)$
- **Vértices:** $V_1(-4, 0)$, $V_2(4, 0)$
- **Focos:** $F_1(-5, 0)$, $F_2(5, 0)$
- **Asíntotas:** $y = \pm\frac{3}{4}x$
- **Excentricidad:** $e = \frac{5}{4} = 1.25$

---

**Verificación:** Para cualquier punto $P$ de la hipérbola: $|PF_1 - PF_2| = 2a = 8$

Para $P(4, 0)$ (vértice):
$$PF_1 = |4 - (-5)| = 9, \quad PF_2 = |4 - 5| = 1$$
$$|PF_1 - PF_2| = |9 - 1| = 8 \checkmark$$

$$\boxed{a = 4, \quad b = 3, \quad c = 5, \quad e = 1.25}$$

---

## Método 10: Identificar Cónicas por la Ecuación General

**Cuándo Usar:** Cuando se da una ecuación de segundo grado y hay que clasificarla.

### Ecuación General

$$Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$$

### Clasificación por Discriminante

| Discriminante | Cónica |
|---------------|--------|
| $B^2 - 4AC < 0$ | Elipse (o circunferencia si $A = C$ y $B = 0$) |
| $B^2 - 4AC = 0$ | Parábola |
| $B^2 - 4AC > 0$ | Hipérbola |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar coeficientes | $A$, $B$, $C$ de los términos cuadráticos |
| 2 | Calcular discriminante | $\Delta = B^2 - 4AC$ |
| 3 | Clasificar | Según signo del discriminante |
| 4 | Transformar a forma canónica | Rotación si $B \neq 0$, completar cuadrado |

### Ejemplo Detallado

**Problema:** Clasificar y analizar $9x^2 - 16y^2 - 36x - 32y - 124 = 0$.

---

**Paso 1: Identificar coeficientes**

$$A = 9, \quad B = 0, \quad C = -16$$

---

**Paso 2: Calcular discriminante**

$$\Delta = B^2 - 4AC = 0 - 4(9)(-16) = 576 > 0$$

Es una **hipérbola**.

---

**Paso 3: Llevar a forma canónica**

Agrupar:
$$(9x^2 - 36x) + (-16y^2 - 32y) = 124$$

Factorizar:
$$9(x^2 - 4x) - 16(y^2 + 2y) = 124$$

Completar cuadrados:
$$9(x^2 - 4x + 4) - 16(y^2 + 2y + 1) = 124 + 36 - 16$$
$$9(x - 2)^2 - 16(y + 1)^2 = 144$$

Dividir por 144:
$$\frac{(x - 2)^2}{16} - \frac{(y + 1)^2}{9} = 1$$

---

**Paso 4: Elementos**

- Centro: $C(2, -1)$
- $a^2 = 16 \Rightarrow a = 4$
- $b^2 = 9 \Rightarrow b = 3$
- $c = \sqrt{16 + 9} = 5$
- Focos: $(2 \pm 5, -1) = (-3, -1)$ y $(7, -1)$
- Vértices: $(2 \pm 4, -1) = (-2, -1)$ y $(6, -1)$

$$\boxed{\text{Hipérbola con centro } (2, -1), \quad a = 4, \quad b = 3}$$

---

## Método 11: Transformar Cónicas (Traslación y Rotación)

**Cuándo Usar:** Cuando la cónica no está centrada en el origen o tiene término $xy$.

### Traslación

Para mover el centro de $(h, k)$ al origen:
$$x' = x - h, \quad y' = y - k$$

### Rotación (eliminar término $xy$)

Ángulo de rotación:
$$\tan 2\theta = \frac{B}{A - C}$$

Transformación:
$$x = x'\cos\theta - y'\sin\theta$$
$$y = x'\sin\theta + y'\cos\theta$$

### Ejemplo Detallado

**Problema:** Identificar la cónica $xy = 4$.

---

**Paso 1: Identificar coeficientes**

$$A = 0, \quad B = 1, \quad C = 0$$

Discriminante: $B^2 - 4AC = 1 > 0$ → Hipérbola

---

**Paso 2: Calcular ángulo de rotación**

$$\tan 2\theta = \frac{1}{0 - 0}$$ → indefinido → $2\theta = 90°$ → $\theta = 45°$

---

**Paso 3: Aplicar rotación**

Con $\theta = 45°$: $\cos 45° = \sin 45° = \frac{\sqrt{2}}{2}$

$$x = \frac{\sqrt{2}}{2}(x' - y'), \quad y = \frac{\sqrt{2}}{2}(x' + y')$$

Sustituyendo en $xy = 4$:

$$\frac{\sqrt{2}}{2}(x' - y') \cdot \frac{\sqrt{2}}{2}(x' + y') = 4$$

$$\frac{1}{2}(x'^2 - y'^2) = 4$$

$$\frac{x'^2}{8} - \frac{y'^2}{8} = 1$$

---

**Paso 4: Identificar elementos**

Hipérbola equilátera con $a = b = 2\sqrt{2}$

Las asíntotas originales $y = 0$ y $x = 0$ se transforman en los ejes de la hipérbola rotada.

$$\boxed{\text{Hipérbola equilátera: } \frac{x'^2}{8} - \frac{y'^2}{8} = 1}$$

---

## Resumen de Fórmulas

| Concepto | Fórmula |
|----------|---------|
| Distancia entre puntos | $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ |
| Punto medio | $M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$ |
| Pendiente | $m = \frac{y_2 - y_1}{x_2 - x_1}$ |
| Distancia punto-recta | $d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}$ |
| Circunferencia | $(x-h)^2 + (y-k)^2 = r^2$ |
| Elipse | $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, $c^2 = a^2 - b^2$ |
| Hipérbola | $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$, $c^2 = a^2 + b^2$ |
| Parábola | $(y-k)^2 = 4p(x-h)$ |
| Discriminante | $\Delta = B^2 - 4AC$ |

---

## Errores Comunes

| Error | Corrección |
|-------|------------|
| Confundir $a$ y $b$ en elipse/hipérbola | En elipse: $a$ es siempre el mayor; en hipérbola: $a$ está bajo el término positivo |
| Olvidar $c^2 = a^2 - b^2$ vs $c^2 = a^2 + b^2$ | Elipse: resta; Hipérbola: suma |
| Error de signo al completar el cuadrado | Sumar el mismo valor a ambos lados |
| Confundir vértice con foco | Vértice está más cerca del centro que el foco (en hipérbola/elipse) |
| Asíntotas incorrectas | Hipérbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$: asíntotas $y = \pm\frac{b}{a}x$ |
| Ignorar la orientación de la parábola | Signo de $4p$ determina hacia dónde abre |
