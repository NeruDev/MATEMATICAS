<!--
HUMANO:
Soluciones con contexto teórico y desarrollo paso a paso.

IA:
Cada solución incluye: contexto → desarrollo → verificación.

---
content_type: solutions
expected_output:
  default: markdown
audience: self-study
---
-->

# Soluciones de Geometría Analítica

> **Formato:** Contexto teórico → Desarrollo paso a paso → Verificación

---

## 6.1 El Plano Cartesiano

### Solución 6.1.1
**Contexto:** Los cuadrantes se numeran I, II, III, IV en sentido antihorario desde (+,+). Los ejes tienen coordenadas con uno de los valores igual a cero.

**Desarrollo:**
- a) $A(3, -5)$: $x > 0$, $y < 0$ → **Cuadrante IV**
- b) $B(-2, 4)$: $x < 0$, $y > 0$ → **Cuadrante II**
- c) $C(0, -3)$: $x = 0$ → **Eje Y** (parte negativa)
- d) $D(-4, 0)$: $y = 0$ → **Eje X** (parte negativa)
- e) $E(-1, -7)$: $x < 0$, $y < 0$ → **Cuadrante III**

### Solución 6.1.4
**Contexto:** En un rectángulo con lados paralelos a los ejes, los vértices opuestos comparten una coordenada con cada vértice adyacente.

**Desarrollo:**
Si $A(1, 2)$ y $C(7, 6)$ son opuestos:
- $B$ comparte $x$ con $C$ y $y$ con $A$: $B(7, 2)$
- $D$ comparte $x$ con $A$ y $y$ con $C$: $D(1, 6)$

**Verificación:** Las diagonales $\overline{AC}$ y $\overline{BD}$ tienen el mismo punto medio: $M = \left(\frac{1+7}{2}, \frac{2+6}{2}\right) = (4, 4)$ ✓

### Solución 6.1.5
**Contexto:** Un punto en el eje $y$ tiene forma $(0, y)$. La equidistancia implica igualar distancias.

**Desarrollo:**
Sea $P(0, y)$. Condición: $d(P,A) = d(P,B)$

$$\sqrt{(0-(-3))^2 + (y-2)^2} = \sqrt{(0-5)^2 + (y-4)^2}$$

Elevando al cuadrado:
$$9 + (y-2)^2 = 25 + (y-4)^2$$
$$9 + y^2 - 4y + 4 = 25 + y^2 - 8y + 16$$
$$13 - 4y = 41 - 8y$$
$$4y = 28$$
$$y = 7$$

**Respuesta:** $P(0, 7)$

---

## 6.2 Distancia y Punto Medio

### Solución 6.2.1
**Contexto:** $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$

**Desarrollo:**
a) $d(A,B) = \sqrt{(-1-3)^2 + (4-7)^2} = \sqrt{16 + 9} = \sqrt{25} = 5$

b) $d(P,Q) = \sqrt{(3-(-5))^2 + (-4-2)^2} = \sqrt{64 + 36} = \sqrt{100} = 10$

### Solución 6.2.3
**Contexto:** Un triángulo es isósceles si tiene al menos dos lados iguales.

**Desarrollo:**
- $\lvert AB \rvert = \sqrt{(4-1)^2 + (5-1)^2} = \sqrt{9 + 16} = 5$
- $\lvert BC \rvert = \sqrt{(7-4)^2 + (1-5)^2} = \sqrt{9 + 16} = 5$
- $\lvert AC \rvert = \sqrt{(7-1)^2 + (1-1)^2} = \sqrt{36} = 6$

Como $\lvert AB \rvert = \lvert BC \rvert = 5$, el triángulo es **isósceles**. ✓

### Solución 6.2.4
**Contexto:** Si $M$ es punto medio de $\overline{AB}$, entonces $M = \left(\frac{x_A + x_B}{2}, \frac{y_A + y_B}{2}\right)$.

**Desarrollo:**
$$3 = \frac{7 + x_B}{2} \Rightarrow x_B = 6 - 7 = -1$$
$$-2 = \frac{4 + y_B}{2} \Rightarrow y_B = -4 - 4 = -8$$

**Respuesta:** $B(-1, -8)$

### Solución 6.2.8
**Contexto:** Área con [determinante](../../../glossary.md#determinante): $\text{Área} = \frac{1}{2}\lvert x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2) \rvert$

**Desarrollo:**
$$\text{Área} = \frac{1}{2}\lvert 2(-1-(-3)) + 6(-3-3) + (-2)(3-(-1)) \rvert$$
$$= \frac{1}{2}\lvert 2(2) + 6(-6) + (-2)(4) \rvert$$
$$= \frac{1}{2}\lvert 4 - 36 - 8 \rvert = \frac{1}{2}\lvert -40 \rvert = 20$$

**Respuesta:** Área $= 20$ unidades²

### Solución 6.2.10
**Contexto:** El circuncentro es equidistante de los tres vértices. En un triángulo rectángulo, el circuncentro está en el punto medio de la hipotenusa.

**Desarrollo:**
El triángulo es rectángulo (ángulo recto en $A(0,0)$, pues está en el origen con catetos sobre los ejes).

La hipotenusa va de $B(8, 0)$ a $C(0, 6)$.
Centro = punto medio de $\overline{BC}$: $O = \left(\frac{8+0}{2}, \frac{0+6}{2}\right) = (4, 3)$

Radio = distancia al vértice:
$r = \sqrt{(4-0)^2 + (3-0)^2} = \sqrt{16 + 9} = 5$

**Respuesta:** Centro $(4, 3)$, radio $5$

---

## 6.3 La Línea Recta

### Solución 6.3.1
**Contexto:** $m = \frac{y_2 - y_1}{x_2 - x_1}$

**Desarrollo:**
a) $m = \frac{6-(-2)}{7-3} = \frac{8}{4} = 2$

b) $m = \frac{5-5}{2-(-4)} = \frac{0}{6} = 0$ (recta horizontal)

### Solución 6.3.4
**Contexto:** Rectas paralelas tienen igual pendiente. Rectas perpendiculares tienen pendientes con producto $-1$.

**Desarrollo:**
La recta $3x - 2y + 5 = 0$ tiene pendiente $m = \frac{3}{2}$.

a) **Paralela:** misma pendiente $m = \frac{3}{2}$
$$y - (-2) = \frac{3}{2}(x - 4)$$
$$y + 2 = \frac{3}{2}x - 6$$
$$3x - 2y - 16 = 0$$

b) **Perpendicular:** $m_\perp = -\frac{2}{3}$
$$y + 2 = -\frac{2}{3}(x - 4)$$
$$3y + 6 = -2x + 8$$
$$2x + 3y - 2 = 0$$

### Solución 6.3.5
**Contexto:** Distancia punto-recta: $d = \frac{\lvert Ax_0 + By_0 + C \rvert}{\sqrt{A^2 + B^2}}$

**Desarrollo:**
Recta: $5x - 12y + 10 = 0$, Punto: $P(3, -4)$

$$d = \frac{\lvert 5(3) - 12(-4) + 10 \rvert}{\sqrt{25 + 144}} = \frac{\lvert 15 + 48 + 10 \rvert}{\sqrt{169}} = \frac{73}{13}$$

**Respuesta:** $d = \frac{73}{13} \approx 5.62$ unidades

### Solución 6.3.8
**Contexto:** La mediatriz pasa por el punto medio y es perpendicular al segmento.

**Desarrollo:**
Punto medio: $M = \left(\frac{-1+5}{2}, \frac{4+(-2)}{2}\right) = (2, 1)$

Pendiente de $\overline{AB}$: $m_{AB} = \frac{-2-4}{5-(-1)} = \frac{-6}{6} = -1$

Pendiente de la mediatriz: $m_\perp = 1$

Ecuación: $y - 1 = 1(x - 2)$ → $\boxed{x - y - 1 = 0}$

### Solución 6.3.10
**Contexto:** El ángulo entre rectas: $\tan\theta = \left\lvert\frac{m_1 - m_2}{1 + m_1 m_2}\right\rvert$

**Desarrollo:**
$m_1 = 3$, $m_2 = -2$

$$\tan\theta = \left\lvert\frac{3 - (-2)}{1 + (3)(-2)}\right\rvert = \left\lvert\frac{5}{-5}\right\rvert = 1$$

$$\theta = \arctan(1) = 45°$$

---

## 6.4 La Circunferencia

### Solución 6.4.2
**Contexto:** Completar cuadrados para convertir forma general a estándar.

**Desarrollo:**
$x^2 + y^2 - 6x + 4y - 12 = 0$

$(x^2 - 6x + 9) + (y^2 + 4y + 4) = 12 + 9 + 4$

$(x - 3)^2 + (y + 2)^2 = 25$

**Respuesta:** Centro $(3, -2)$, radio $5$

### Solución 6.4.6
**Contexto:** Sustituir la ecuación de la recta en la circunferencia y resolver.

**Desarrollo:**
Sustituyendo $y = x + 1$ en $x^2 + y^2 = 25$:
$$x^2 + (x+1)^2 = 25$$
$$x^2 + x^2 + 2x + 1 = 25$$
$$2x^2 + 2x - 24 = 0$$
$$x^2 + x - 12 = 0$$
$$(x+4)(x-3) = 0$$

$x = -4 \Rightarrow y = -3$ → $(-4, -3)$
$x = 3 \Rightarrow y = 4$ → $(3, 4)$

**Verificación:** $(-4)^2 + (-3)^2 = 16 + 9 = 25$ ✓

### Solución 6.4.9
**Contexto:** Una recta es [tangente](../../../glossary.md#tangente) a una circunferencia si la distancia del centro a la recta es igual al radio.

**Desarrollo:**
Centro: $(0, 0)$, Radio: $2$
Recta: $3x + 4y = k$ o $3x + 4y - k = 0$

Distancia del centro a la recta:
$$d = \frac{\lvert 3(0) + 4(0) - k \rvert}{\sqrt{9 + 16}} = \frac{\lvert k \rvert}{5}$$

Para tangencia: $d = r$
$$\frac{\lvert k \rvert}{5} = 2 \Rightarrow \lvert k \rvert = 10$$

**Respuesta:** $k = 10$ o $k = -10$

---

## 6.5 La Parábola

### Solución 6.5.1
**Contexto:** Para $y^2 = 4px$: vértice en origen, foco en $(p, 0)$, directriz $x = -p$.

**Desarrollo:**
$y^2 = 12x$ → $4p = 12$ → $p = 3$

- **Vértice:** $(0, 0)$
- **Foco:** $(3, 0)$
- **Directriz:** $x = -3$
- **Eje:** $y = 0$ (eje x)
- **Abre:** hacia la derecha

### Solución 6.5.5
**Contexto:** Completar cuadrados para identificar vértice y parámetro.

**Desarrollo:**
$y^2 + 6y + 8x + 1 = 0$

$(y^2 + 6y + 9) + 8x + 1 - 9 = 0$

$(y + 3)^2 = -8x + 8 = -8(x - 1)$

Forma estándar: $(y + 3)^2 = -8(x - 1)$

$4p = 8$ → $p = 2$ (abre a la izquierda)

- **Vértice:** $(1, -3)$
- **Foco:** $(1-2, -3) = (-1, -3)$
- **Directriz:** $x = 1 + 2 = 3$

### Solución 6.5.6
**Contexto:** El foco de un reflector parabólico está donde convergen los rayos reflejados.

**Desarrollo:**
Sistema con vértice en origen, parábola $y^2 = 4px$ (abre a la derecha).

El borde del reflector está en $(5, 10)$ (profundidad 5 cm, radio 10 cm).

$10^2 = 4p(5)$
$100 = 20p$
$p = 5$

**Respuesta:** La fuente de luz debe colocarse a **5 cm del vértice**.

---

## 6.6 La Elipse

### Solución 6.6.1
**Contexto:** Para $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ con $a > b$: focos en $(\pm c, 0)$ donde $c^2 = a^2 - b^2$.

**Desarrollo:**
$\frac{x^2}{25} + \frac{y^2}{9} = 1$ → $a^2 = 25$, $b^2 = 9$

$a = 5$, $b = 3$, $c = \sqrt{25-9} = 4$

- **Vértices:** $(\pm 5, 0)$ y $(0, \pm 3)$
- **Focos:** $(\pm 4, 0)$
- **Excentricidad:** $e = \frac{c}{a} = \frac{4}{5} = 0.8$

### Solución 6.6.7
**Contexto:** La excentricidad mide qué tan "estirada" es la elipse.

**Desarrollo:**
- Perihelio: $a - c = 147$ millones km
- Afelio: $a + c = 152$ millones km

Sumando: $2a = 299$ → $a = 149.5$
Restando: $2c = 5$ → $c = 2.5$

$$e = \frac{c}{a} = \frac{2.5}{149.5} \approx 0.0167$$

**Verificación:** La órbita terrestre es casi circular (baja excentricidad).

### Solución 6.6.9
**Contexto:** Semielipse: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ con $y \geq 0$.

**Desarrollo:**
$a = 5$ m (semiancho), $b = 4$ m (altura central)

$$\frac{x^2}{25} + \frac{y^2}{16} = 1$$

En $x = 3$:
$$\frac{9}{25} + \frac{y^2}{16} = 1$$
$$\frac{y^2}{16} = \frac{16}{25}$$
$$y^2 = \frac{256}{25}$$
$$y = \frac{16}{5} = 3.2 \text{ m}$$

---

## 6.7 La Hipérbola

### Solución 6.7.1
**Contexto:** Para $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$: focos en $(\pm c, 0)$ con $c^2 = a^2 + b^2$.

**Desarrollo:**
$a^2 = 16$, $b^2 = 9$ → $a = 4$, $b = 3$, $c = \sqrt{16+9} = 5$

- **Vértices:** $(\pm 4, 0)$
- **Focos:** $(\pm 5, 0)$
- **Asíntotas:** $y = \pm\frac{b}{a}x = \pm\frac{3}{4}x$

### Solución 6.7.9
**Contexto:** LORAN usa la diferencia de distancias a dos puntos (definición de hipérbola).

**Desarrollo:**
Estaciones en $(\pm 150, 0)$ (a 300 km de distancia).
$2a = 160$ → $a = 80$, $c = 150$

$b^2 = c^2 - a^2 = 22500 - 6400 = 16100$

**Ecuación:** $\frac{x^2}{6400} - \frac{y^2}{16100} = 1$

---

## 6.8 Ecuación General de Segundo Grado

### Solución 6.8.1
**Contexto:** Discriminante $B^2 - 4AC$: negativo = elipse, cero = parábola, positivo = hipérbola.

**Desarrollo:**
a) $x^2 + 4y^2 - 4x + 8y + 4 = 0$ → $A = 1$, $B = 0$, $C = 4$
   $\Delta = 0 - 4(1)(4) = -16 < 0$ → **Elipse**

b) $x^2 - y^2 + 6x - 4y = 0$ → $A = 1$, $B = 0$, $C = -1$
   $\Delta = 0 - 4(1)(-1) = 4 > 0$ → **Hipérbola**

c) $x^2 - 4x + y + 3 = 0$ → $A = 1$, $B = 0$, $C = 0$
   $\Delta = 0 - 4(1)(0) = 0$ → **Parábola**

### Solución 6.8.5
**Contexto:** El ángulo de rotación $\theta$ que elimina $xy$ satisface $\cot(2\theta) = \frac{A-C}{B}$.

**Desarrollo:**
$A = 1$, $B = 2\sqrt{3}$, $C = 3$

$$\cot(2\theta) = \frac{1-3}{2\sqrt{3}} = \frac{-2}{2\sqrt{3}} = -\frac{1}{\sqrt{3}}$$

$\cot(2\theta) = -\frac{\sqrt{3}}{3}$ → $2\theta = 120°$ → $\theta = 60°$

---

## 6.10 Aplicaciones

### Solución 6.10.2
**Contexto:** El receptor debe estar en el foco de la parábola.

**Desarrollo:**
Diámetro = 3 m → radio = 1.5 m, profundidad = 0.5 m

Parábola: $x^2 = 4py$ con punto $(1.5, 0.5)$ en el borde:
$(1.5)^2 = 4p(0.5)$
$2.25 = 2p$
$p = 1.125$ m

**Respuesta:** El receptor debe colocarse a **1.125 m = 112.5 cm** del vértice.

### Solución 6.10.4
**Contexto:** Órbita elíptica con la Tierra en un foco.

**Desarrollo:**
- Perigeo: $a - c = 6371 + 500 = 6871$ km
- Apogeo: $a + c = 6371 + 4000 = 10371$ km

Sumando: $2a = 17242$ → $a = 8621$
Restando: $2c = 3500$ → $c = 1750$

$$e = \frac{c}{a} = \frac{1750}{8621} \approx 0.203$$

---

## Problemas de Síntesis

### Solución 6.S.1
**Contexto:** Lugar geométrico = conjunto de puntos que satisfacen una condición.

**Desarrollo:**
Sea $P(x, y)$. Condición: $d(P, A) = 2 \cdot d(P, \text{eje } y)$

$$\sqrt{(x-4)^2 + y^2} = 2\lvert x \rvert$$

Elevando al cuadrado:
$(x-4)^2 + y^2 = 4x^2$
$x^2 - 8x + 16 + y^2 = 4x^2$
$y^2 = 3x^2 + 8x - 16$
$y^2 = 3\left(x^2 + \frac{8}{3}x\right) - 16$

**Respuesta:** $3x^2 - y^2 + 8x - 16 = 0$ (hipérbola)

### Solución 6.S.2
**Contexto:** Suma de cuadrados de distancias define una circunferencia.

**Desarrollo:**
$$[x-3]^2 + y^2 + [x+3]^2 + y^2 = 50$$
$$(x^2 - 6x + 9) + y^2 + (x^2 + 6x + 9) + y^2 = 50$$
$$2x^2 + 2y^2 + 18 = 50$$
$$x^2 + y^2 = 16$$

**Respuesta:** Circunferencia con centro en el origen y radio 4.
