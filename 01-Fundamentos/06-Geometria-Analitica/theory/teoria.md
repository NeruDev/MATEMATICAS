<!--
HUMANO:
Teoría completa de geometría analítica: plano cartesiano, recta y secciones cónicas.

IA:
No incluyas métodos de solución ni problemas aquí.
Presenta definiciones, fórmulas y propiedades fundamentales.

---
content_type: theory_comprehensive
expected_output:
  default: markdown
audience: self-study
maturity: complete
---
-->

# Teoría de Geometría Analítica

## 6.1 El Plano Cartesiano

### Sistema de Coordenadas Cartesianas
El **plano cartesiano** es un sistema de referencia formado por dos rectas perpendiculares (ejes) que se intersecan en el **origen** $O(0,0)$.

- **Eje $x$** (abscisas): recta horizontal
- **Eje $y$** (ordenadas): recta vertical

Cada punto $P$ del plano se identifica con un par ordenado $(x, y)$:
- $x$ = abscisa (distancia horizontal desde el eje $y$)
- $y$ = ordenada (distancia vertical desde el eje $x$)

### Cuadrantes

| Cuadrante | Signos | Posición |
|-----------|--------|----------|
| I | $(+, +)$ | Superior derecho |
| II | $(-, +)$ | Superior izquierdo |
| III | $(-, -)$ | Inferior izquierdo |
| IV | $(+, -)$ | Inferior derecho |

Los puntos sobre los ejes no pertenecen a ningún cuadrante.

---

## 6.2 Distancia y Punto Medio

### Fórmula de Distancia
La distancia entre dos puntos $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$ es:

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

**Casos especiales:**
- Distancia horizontal ($y_1 = y_2$): $d = \lvert x_2 - x_1 \rvert$
- Distancia vertical ($x_1 = x_2$): $d = \lvert y_2 - y_1 \rvert$

### Punto Medio
El punto medio $M$ del segmento que une $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$ es:

$$M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$$

### División de un Segmento en una Razón Dada
El punto $P$ que divide al segmento $\overline{P_1P_2}$ en la razón $m:n$ (desde $P_1$) tiene coordenadas:

$$P = \left(\frac{mx_2 + nx_1}{m + n}, \frac{my_2 + ny_1}{m + n}\right)$$

**Caso especial:** Si $m = n$ (razón 1:1), se obtiene el punto medio.

### Área de un Triángulo por Coordenadas
El área del triángulo con vértices $A(x_1, y_1)$, $B(x_2, y_2)$, $C(x_3, y_3)$ es:

$$A = \frac{1}{2}\lvert x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2) \rvert$$

O usando el determinante:
$$A = \frac{1}{2}\left|\det\begin{pmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{pmatrix}\right|$$

---

## 6.3 La Línea Recta

### Pendiente de una Recta
La **pendiente** $m$ de la recta que pasa por $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$ es:

$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x}$$

**Interpretación:**
- $m > 0$: recta creciente (sube de izquierda a derecha)
- $m < 0$: recta decreciente (baja de izquierda a derecha)
- $m = 0$: recta horizontal
- $m$ no definida: recta vertical

### Ángulo de Inclinación
El ángulo $\theta$ que forma la recta con el eje $x$ positivo satisface:
$$m = \tan\theta \quad (0° \leq \theta < 180°)$$

### Formas de la Ecuación de la Recta

#### Forma punto-pendiente
$$y - y_1 = m(x - x_1)$$

#### Forma pendiente-ordenada
$$y = mx + b$$
donde $b$ es la ordenada al origen (intersección con el eje $y$).

#### Forma general
$$Ax + By + C = 0$$
con $A$, $B$ no ambos cero. La pendiente es $m = -\frac{A}{B}$ (si $B \neq 0$).

#### Forma simétrica (interceptos)
$$\frac{x}{a} + \frac{y}{b} = 1$$
donde $a$ = intersección con eje $x$, $b$ = intersección con eje $y$.

#### Forma normal
$$x\cos\omega + y\sin\omega = p$$
donde $p$ es la distancia del origen a la recta y $\omega$ es el ángulo de la normal.

### Casos Especiales
| Tipo de recta | Ecuación | Pendiente |
|---------------|----------|-----------|
| Horizontal | $y = k$ | $m = 0$ |
| Vertical | $x = k$ | No definida |
| Pasa por el origen | $y = mx$ | $m$ |

### Rectas Paralelas y Perpendiculares

**Paralelas:** Dos rectas son paralelas si y solo si tienen la misma pendiente:
$$m_1 = m_2$$

**Perpendiculares:** Dos rectas son perpendiculares si y solo si el producto de sus pendientes es $-1$:
$$m_1 \cdot m_2 = -1 \quad \text{o} \quad m_2 = -\frac{1}{m_1}$$

### Distancia de un Punto a una Recta
La distancia del punto $P(x_0, y_0)$ a la recta $Ax + By + C = 0$ es:

$$d = \frac{\lvert Ax_0 + By_0 + C \rvert}{\sqrt{A^2 + B^2}}$$

### Ángulo entre Dos Rectas
Si dos rectas tienen pendientes $m_1$ y $m_2$, el ángulo agudo $\theta$ entre ellas es:

$$\tan\theta = \left|\frac{m_1 - m_2}{1 + m_1 m_2}\right|$$

---

## 6.4 La Circunferencia

### Definición
Una **circunferencia** es el lugar geométrico de los puntos del plano que equidistan de un punto fijo llamado **centro**.

### Ecuación Canónica (Estándar)
Circunferencia con centro $C(h, k)$ y radio $r$:

$$(x - h)^2 + (y - k)^2 = r^2$$

**Caso especial:** Centro en el origen:
$$x^2 + y^2 = r^2$$

### Ecuación General
$$x^2 + y^2 + Dx + Ey + F = 0$$

Para convertir a forma estándar, completamos cuadrados:
- Centro: $\left(-\frac{D}{2}, -\frac{E}{2}\right)$
- Radio: $r = \sqrt{\frac{D^2}{4} + \frac{E^2}{4} - F}$

**Condición de existencia:** $\frac{D^2 + E^2}{4} > F$

### Posiciones Relativas de Punto y Circunferencia
Para $P(x_0, y_0)$ y circunferencia $(x-h)^2 + (y-k)^2 = r^2$:

Sea $d = \sqrt{(x_0-h)^2 + (y_0-k)^2}$ la distancia del punto al centro.

| Condición | Posición |
|-----------|----------|
| $d < r$ | Interior |
| $d = r$ | Sobre la circunferencia |
| $d > r$ | Exterior |

### Posiciones Relativas de Recta y Circunferencia
Para una recta $\ell$ y circunferencia de centro $C$ y radio $r$:

Sea $d$ la distancia de $C$ a $\ell$.

| Condición | Posición | Intersecciones |
|-----------|----------|----------------|
| $d > r$ | Externa | 0 |
| $d = r$ | Tangente | 1 |
| $d < r$ | Secante | 2 |

### Ecuación de la Tangente
La tangente a la circunferencia $x^2 + y^2 = r^2$ en el punto $P(x_0, y_0)$ es:
$$x \cdot x_0 + y \cdot y_0 = r^2$$

---

## 6.5 La Parábola

### Definición
Una **parábola** es el lugar geométrico de los puntos que equidistan de un punto fijo (**foco** $F$) y una recta fija (**directriz** $\ell$).

### Elementos
- **Vértice** $V$: punto medio entre el foco y la directriz
- **Eje de simetría**: recta perpendicular a la directriz que pasa por el foco
- **Parámetro** $p$: distancia del vértice al foco (= distancia del vértice a la directriz)
- **Lado recto**: cuerda perpendicular al eje que pasa por el foco (longitud = $4p$)

### Ecuaciones Canónicas (vértice en el origen)

| Orientación | Ecuación | Foco | Directriz |
|-------------|----------|------|-----------|
| Abre a la derecha | $y^2 = 4px$ | $(p, 0)$ | $x = -p$ |
| Abre a la izquierda | $y^2 = -4px$ | $(-p, 0)$ | $x = p$ |
| Abre hacia arriba | $x^2 = 4py$ | $(0, p)$ | $y = -p$ |
| Abre hacia abajo | $x^2 = -4py$ | $(0, -p)$ | $y = p$ |

### Ecuaciones con Vértice en $(h, k)$
- Eje horizontal: $(y - k)^2 = 4p(x - h)$
- Eje vertical: $(x - h)^2 = 4p(y - k)$

### Ecuación General
$$Ax^2 + Dx + Ey + F = 0$$ (eje vertical)
$$Cy^2 + Dx + Ey + F = 0$$ (eje horizontal)

---

## 6.6 La Elipse

### Definición
Una **elipse** es el lugar geométrico de los puntos cuya suma de distancias a dos puntos fijos (**focos**) es constante.

$$d(P, F_1) + d(P, F_2) = 2a$$

### Elementos
- **Centro**: punto medio entre los focos
- **Focos** $F_1$ y $F_2$: puntos fijos a distancia $c$ del centro
- **Semieje mayor** $a$: distancia del centro a un vértice mayor
- **Semieje menor** $b$: distancia del centro a un vértice menor
- **Vértices**: puntos donde la elipse corta a los ejes

### Relación Fundamental
$$a^2 = b^2 + c^2 \quad \text{o} \quad c^2 = a^2 - b^2$$

Siempre $a > b > 0$ y $c < a$.

### Excentricidad
$$e = \frac{c}{a} \quad (0 < e < 1)$$

- Si $e \approx 0$: elipse casi circular
- Si $e \approx 1$: elipse muy alargada

### Ecuaciones Canónicas (centro en el origen)

| Eje mayor | Ecuación | Focos | Vértices |
|-----------|----------|-------|----------|
| Horizontal | $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ | $(\pm c, 0)$ | $(\pm a, 0)$ |
| Vertical | $\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1$ | $(0, \pm c)$ | $(0, \pm a)$ |

### Ecuaciones con Centro en $(h, k)$
$$\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1$$

### Directrices
Las directrices están a distancia $\frac{a}{e} = \frac{a^2}{c}$ del centro, perpendiculares al eje mayor.

---

## 6.7 La Hipérbola

### Definición
Una **hipérbola** es el lugar geométrico de los puntos cuya diferencia absoluta de distancias a dos puntos fijos (**focos**) es constante.

$$\lvert d(P, F_1) - d(P, F_2) \rvert = 2a$$

### Elementos
- **Centro**: punto medio entre los focos
- **Focos** $F_1$ y $F_2$: puntos fijos a distancia $c$ del centro
- **Semieje real** (o transverso) $a$: distancia del centro a un vértice
- **Semieje imaginario** (o conjugado) $b$
- **Vértices**: puntos más cercanos de cada rama al centro

### Relación Fundamental
$$c^2 = a^2 + b^2$$

Siempre $c > a$.

### Excentricidad
$$e = \frac{c}{a} \quad (e > 1)$$

### Asíntotas
Las **asíntotas** son rectas a las que la hipérbola se aproxima pero nunca toca.

Para hipérbola centrada en el origen:
- Eje real horizontal: $y = \pm\frac{b}{a}x$
- Eje real vertical: $y = \pm\frac{a}{b}x$

### Ecuaciones Canónicas (centro en el origen)

| Eje real | Ecuación | Focos | Vértices | Asíntotas |
|----------|----------|-------|----------|-----------|
| Horizontal | $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ | $(\pm c, 0)$ | $(\pm a, 0)$ | $y = \pm\frac{b}{a}x$ |
| Vertical | $\frac{y^2}{a^2} - \frac{x^2}{b^2} = 1$ | $(0, \pm c)$ | $(0, \pm a)$ | $y = \pm\frac{a}{b}x$ |

### Ecuaciones con Centro en $(h, k)$
$$\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1$$

### Hipérbola Equilátera
Si $a = b$, las asíntotas son perpendiculares ($y = \pm x$) y la excentricidad es $e = \sqrt{2}$.

---

## 6.8 Ecuación General de Segundo Grado

### Forma General
$$Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$$

### Clasificación por el Discriminante
El discriminante $\Delta = B^2 - 4AC$ determina el tipo de cónica:

| Discriminante | Cónica |
|---------------|--------|
| $\Delta < 0$ | Elipse (o circunferencia si $A = C$ y $B = 0$) |
| $\Delta = 0$ | Parábola |
| $\Delta > 0$ | Hipérbola |

### Casos Degenerados
La ecuación puede representar:
- Un punto (elipse degenerada)
- Dos rectas (hipérbola degenerada)
- Una recta (parábola degenerada)
- Conjunto vacío

### Invariantes
Bajo rotación de ejes, se conservan:
- $A + C$ (traza)
- $B^2 - 4AC$ (discriminante)
- $\det\begin{pmatrix} A & B/2 & D/2 \\ B/2 & C & E/2 \\ D/2 & E/2 & F \end{pmatrix}$

---

## 6.9 Transformaciones en el Plano

### Traslación
Mover el origen a $(h, k)$:
$$x = x' + h, \quad y = y' + k$$

Equivalentemente: $x' = x - h$, $y' = y - k$

### Rotación
Rotar los ejes un ángulo $\theta$:
$$x = x'\cos\theta - y'\sin\theta$$
$$y = x'\sin\theta + y'\cos\theta$$

Para eliminar el término $xy$ de la ecuación general, se rota un ángulo:
$$\tan(2\theta) = \frac{B}{A - C}$$

### Reflexión
- Respecto al eje $x$: $(x, y) \to (x, -y)$
- Respecto al eje $y$: $(x, y) \to (-x, y)$
- Respecto al origen: $(x, y) \to (-x, -y)$
- Respecto a $y = x$: $(x, y) \to (y, x)$

### Homotecia
Transformación con centro $O$ y razón $k$:
$$(x, y) \to (kx, ky)$$

---

## 6.10 Aplicaciones

### Propiedad Reflectiva de la Parábola
Los rayos paralelos al eje que inciden en una parábola se reflejan hacia el foco. Aplicaciones: antenas parabólicas, faros, telescopios.

### Propiedad Reflectiva de la Elipse
Un rayo desde un foco se refleja hacia el otro foco. Aplicaciones: salas de susurros, litotricia.

### Propiedad Reflectiva de la Hipérbola
Un rayo dirigido hacia un foco se refleja como si viniera del otro foco. Aplicaciones: telescopios Cassegrain.

### Órbitas Planetarias
Las órbitas de los planetas son elipses con el Sol en un foco (primera ley de Kepler).

---

## Resumen de Fórmulas Principales

### Distancia y Punto Medio
| Fórmula | Expresión |
|---------|-----------|
| Distancia | $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ |
| Punto medio | $M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$ |
| Pendiente | $m = \frac{y_2-y_1}{x_2-x_1}$ |

### Ecuaciones de la Recta
| Forma | Ecuación |
|-------|----------|
| Punto-pendiente | $y - y_1 = m(x - x_1)$ |
| Pendiente-ordenada | $y = mx + b$ |
| General | $Ax + By + C = 0$ |

### Cónicas (centradas en el origen)
| Cónica | Ecuación |
|--------|----------|
| Circunferencia | $x^2 + y^2 = r^2$ |
| Elipse | $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ |
| Hipérbola | $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ |
| Parábola | $y^2 = 4px$ o $x^2 = 4py$ |

### Relaciones en Cónicas
| Cónica | Relación | Excentricidad |
|--------|----------|---------------|
| Elipse | $c^2 = a^2 - b^2$ | $e = c/a < 1$ |
| Hipérbola | $c^2 = a^2 + b^2$ | $e = c/a > 1$ |
| Parábola | — | $e = 1$ |
