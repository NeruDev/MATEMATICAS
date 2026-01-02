<!--
HUMANO:
Soluciones detalladas y contextualizadas para cada problema de geometría.

IA:
Antes de cada solución, incluye un breve contexto que conecte con la teoría.
Explica el razonamiento geométrico paso a paso.
Incluye diagramas conceptuales cuando sea posible.

---
content_type: solutions_set
expected_output:
  default: markdown
solution_format: context + development + verification
---
-->

# Soluciones de Geometría

> **Formato de cada solución:** Contexto teórico → Desarrollo paso a paso → Verificación

---

## 4.1 Conceptos Fundamentales

### Solución 4.1.1
**Contexto:** Los postulados básicos de la geometría establecen las relaciones fundamentales entre puntos, rectas y planos.

**Desarrollo:**
a) **VERDADERO.** Es el postulado de determinación de la recta: dos puntos distintos determinan una única recta.

b) **FALSO.** Tres puntos determinan un único plano solo si no son colineales. Si son colineales, infinitos planos contienen esa recta.

c) **FALSO.** Dos rectas en el espacio pueden ser:
   - Paralelas (no se intersecan)
   - Secantes (se intersecan en un punto)
   - Alabeadas (no coplanares, no se intersecan)

d) **FALSO.** Una semirrecta tiene exactamente un punto extremo (su origen).

---

### Solución 4.1.2
**Contexto:** Los puntos sobre una recta se pueden ordenar y las distancias se suman algebraicamente.

**Desarrollo:**
Como los puntos están en [orden](../../../glossary.md#orden) $A$, $B$, $C$, $D$:
$$AD = AB + BC + CD$$
$$12 = 3 + 5 + CD$$
$$CD = 12 - 8 = 4 \text{ cm}$$

**Verificación:** $AB + BC + CD = 3 + 5 + 4 = 12 = AD$ ✓

---

### Solución 4.1.3
**Contexto:** El punto medio de un segmento divide al segmento en dos partes congruentes.

**Desarrollo:**
Si $M$ es punto medio de $\overline{PQ}$:
$$PM = MQ$$
$$2x + 3 = 5x - 9$$
$$3 + 9 = 5x - 2x$$
$$12 = 3x$$
$$x = 4$$

Entonces: $PM = MQ = 2(4) + 3 = 11$ cm

Por tanto: $PQ = PM + MQ = 11 + 11 = 22$ cm

**Verificación:** $MQ = 5(4) - 9 = 20 - 9 = 11$ ✓

---

### Solución 4.1.4
**Contexto:** Para tres puntos colineales, uno de ellos debe estar entre los otros dos, y la distancia total es la suma de las distancias parciales.

**Desarrollo:**
Hay tres casos posibles: $B$ entre $A$ y $C$, $A$ entre $B$ y $C$, o $C$ entre $A$ y $B$.

**Caso 1:** $B$ está entre $A$ y $C$
$$AC = AB + BC$$
$$4x - 2 = (2x + 1) + (x + 5)$$
$$4x - 2 = 3x + 6$$
$$x = 8$$

Verificamos: $AB = 17$, $BC = 13$, $AC = 30$ → $17 + 13 = 30$ ✓

**Caso 2 y 3:** Llevan a contradicciones o valores negativos.

**Respuesta:** $B$ está entre $A$ y $C$, con $AB = 17$ cm, $BC = 13$ cm, $AC = 30$ cm.

---

### Solución 4.1.5
**Contexto:** Las propiedades de los puntos medios permiten establecer relaciones entre longitudes de segmentos.

**Desarrollo:**
Sea $AB = 2a$, entonces $AM = a$ (por ser $M$ punto medio).
Sea $BC = 2b$, entonces $BN = b$ (por ser $N$ punto medio).

$$MN = MB + BN = a + b$$

Por otro lado:
$$AC = AB + BC = 2a + 2b = 2(a + b)$$

Por tanto:
$$MN = a + b = \frac{2(a+b)}{2} = \frac{AC}{2}$$

**Conclusión:** $MN = \frac{1}{2}AC$ ∎

---

## 4.2 Ángulos

### Solución 4.2.1
**Contexto:** Los ángulos se clasifican según su medida en: agudo (0°-90°), recto (90°), obtuso (90°-180°), llano (180°), cóncavo (180°-360°) y completo (360°).

**Desarrollo:**
a) 47° → **Agudo** ([menor](../../../glossary.md#menor) que 90°)
b) 90° → **Recto** (exactamente 90°)
c) 123° → **Obtuso** (entre 90° y 180°)
d) 180° → **Llano** (exactamente 180°)
e) 215° → **Cóncavo/reflejo** (entre 180° y 360°)
f) 360° → **Completo/perigonal** (exactamente 360°)

---

### Solución 4.2.2
**Contexto:** Dos ángulos complementarios suman 90°.

**Desarrollo:**
Sea $x$ el ángulo [menor](../../../glossary.md#menor). El otro ángulo es $3x$.
$$x + 3x = 90°$$
$$4x = 90°$$
$$x = 22.5°$$

**Respuesta:** Los ángulos son **22.5°** y **67.5°**.

**Verificación:** $22.5° + 67.5° = 90°$ ✓ y $67.5° = 3 \times 22.5°$ ✓

---

### Solución 4.2.3
**Contexto:** Dos ángulos suplementarios suman 180°.

**Desarrollo:**
Sea $x$ el ángulo menor. El otro ángulo es $x + 36°$.
$$x + (x + 36°) = 180°$$
$$2x = 144°$$
$$x = 72°$$

**Respuesta:** Los ángulos son **72°** y **108°**.

**Verificación:** $72° + 108° = 180°$ ✓ y $108° - 72° = 36°$ ✓

---

### Solución 4.2.5
**Contexto:** Cuando dos rectas paralelas son cortadas por una transversal, los ángulos alternos internos son iguales y los correspondientes también.

**Desarrollo:**
Si son ángulos alternos internos, deben ser iguales:
$$3x + 15 = 5x - 25$$

Pero si uno es alterno interno y el otro correspondiente al primero, están en lados opuestos...

En realidad, un ángulo alterno interno y su correspondiente no son iguales entre sí (están en posiciones diferentes).

Analicemos: si $\alpha$ es un ángulo alterno interno, su correspondiente está del mismo lado de la transversal pero en otra intersección.

Para ángulos alternos internos: son iguales entre sí.
El correspondiente de un alterno interno es suplementario al otro alterno interno.

El problema tiene una inconsistencia en el enunciado. Si interpretamos que son ángulos que deberían ser iguales:
$$3x + 15 = 5x - 25 \Rightarrow x = 20$$

Los ángulos medirían $3(20)+15 = 75°$ y $5(20)-25 = 75°$ ✓

---

### Solución 4.2.6
**Contexto:** En paralelas cortadas por transversales, usamos propiedades de ángulos alternos, correspondientes y covertinales.

**Desarrollo:**
En el diagrama, $\angle 1$ y $\angle 2$ están en las paralelas, y $\angle 3$ está entre ellas.

Por ángulos alternos internos y la propiedad del triángulo formado:
$$\angle 3 = 180° - \angle 1 - \angle 2 = 180° - 65° - 40° = 75°$$

(O usando que $\angle 3$ es el ángulo entre las transversales que forman $\angle 1$ y $\angle 2$)

**Respuesta:** $\angle 3 = 75°$

---

## 4.3 Triángulos

### Solución 4.3.1
**Contexto:** La suma de los ángulos interiores de un triángulo es 180°.

**Desarrollo:**
$$\angle C = 180° - 45° - 72° = 63°$$

**Clasificación:** Como todos los ángulos son menores que 90°, es un **triángulo acutángulo**.

---

### Solución 4.3.2
**Contexto:** En un triángulo isósceles, los ángulos de la [base](../../../glossary.md#base) (opuestos a los lados iguales) son iguales.

**Desarrollo:**
El ángulo de 100° debe ser el ángulo del vértice (no puede ser de la [base](../../../glossary.md#base), pues $2 \times 100° = 200° > 180°$).

Sea $x$ el ángulo de cada ángulo de la base:
$$100° + x + x = 180°$$
$$2x = 80°$$
$$x = 40°$$

**Respuesta:** Los otros dos ángulos miden **40°** cada uno.

---

### Solución 4.3.3
**Contexto:** Un triángulo se clasifica según sus lados (escaleno, isósceles, equilátero) y según sus ángulos (rectángulo si cumple el teorema de Pitágoras).

**Desarrollo:**
**Por lados:** 5 ≠ 12 ≠ 13, todos diferentes → **escaleno**.

**Por ángulos:** Verificamos si es rectángulo:
$$5^2 + 12^2 = 25 + 144 = 169 = 13^2$$

Cumple el teorema de Pitágoras → **triángulo rectángulo**.

**Respuesta:** Triángulo escaleno rectángulo (5, 12, 13 es una terna pitagórica).

---

### Solución 4.3.4
**Contexto:** El ángulo exterior de un triángulo es igual a la suma de los dos ángulos interiores no adyacentes.

**Desarrollo:**
El ángulo exterior en $C$ es: $\angle A + \angle B = 140°$

Dado que $\angle A = 3\angle B$:
$$3\angle B + \angle B = 140°$$
$$4\angle B = 140°$$
$$\angle B = 35°$$
$$\angle A = 3(35°) = 105°$$
$$\angle C = 180° - 140° = 40°$$

**Verificación:** $35° + 105° + 40° = 180°$ ✓

---

### Solución 4.3.5
**Contexto:** Si los ángulos están en razón $a:b:c$, podemos expresarlos como $ax$, $bx$, $cx$ donde su suma es 180°.

**Desarrollo:**
$$2x + 3x + 4x = 180°$$
$$9x = 180°$$
$$x = 20°$$

**Respuesta:** Los ángulos son **40°**, **60°** y **80°**.

**Verificación:** $40° + 60° + 80° = 180°$ ✓ y $40:60:80 = 2:3:4$ ✓

---

### Solución 4.3.6
**Contexto:** La desigualdad triangular establece que la suma de dos lados cualesquiera debe ser mayor que el tercero.

**Desarrollo:**
Verificamos las tres desigualdades:
- $3 + 4 = 7 > 8$? → **NO**, $7 < 8$

**Respuesta:** **No es posible** construir el triángulo porque $3 + 4 = 7 < 8$, violando la desigualdad triangular.

---

### Solución 4.3.7
**Contexto:** En un triángulo equilátero de lado $a$: altura $h = \frac{a\sqrt{3}}{2}$, área $A = \frac{a^2\sqrt{3}}{4}$, radio inscrito $r = \frac{a\sqrt{3}}{6}$.

**Desarrollo:**
Con $a = 6$ cm:

**Altura:**
$$h = \frac{6\sqrt{3}}{2} = 3\sqrt{3} \approx 5.196 \text{ cm}$$

**Área:**
$$A = \frac{36\sqrt{3}}{4} = 9\sqrt{3} \approx 15.59 \text{ cm}^2$$

**Radio inscrito:**
$$r = \frac{6\sqrt{3}}{6} = \sqrt{3} \approx 1.732 \text{ cm}$$

---

### Solución 4.3.8
**Contexto:** En un triángulo isósceles, la altura a la base biseca a la base, formando dos triángulos rectángulos congruentes.

**Desarrollo:**
La altura divide la base en dos segmentos de 5 cm cada uno.
Por Pitágoras en el triángulo rectángulo formado:
$$h^2 + 5^2 = 13^2$$
$$h^2 = 169 - 25 = 144$$
$$h = 12 \text{ cm}$$

**Verificación:** $5^2 + 12^2 = 25 + 144 = 169 = 13^2$ ✓

---

## 4.4 Cuadriláteros

### Solución 4.4.1
**Contexto:** La suma de los ángulos interiores de cualquier cuadrilátero es 360°.

**Desarrollo:**
$$\angle_4 = 360° - 85° - 110° - 95° = 70°$$

---

### Solución 4.4.2
**Contexto:** En un paralelogramo, los ángulos consecutivos son suplementarios y los opuestos son iguales.

**Desarrollo:**
- El ángulo opuesto a 65° también mide **65°**.
- Los ángulos consecutivos miden $180° - 65° = 115°$.

**Respuesta:** Los cuatro ángulos son **65°**, **115°**, **65°** y **115°**.

---

### Solución 4.4.3
**Contexto:** En un rectángulo, las diagonales son congruentes y se bisecan mutuamente.

**Desarrollo:**
Sea $b$ el otro lado del rectángulo. Por Pitágoras:
$$6^2 + b^2 = 10^2$$
$$b^2 = 100 - 36 = 64$$
$$b = 8 \text{ cm}$$

---

### Solución 4.4.4
**Contexto:** En un rombo, las diagonales se bisecan perpendicularmente. El área es la mitad del producto de las diagonales.

**Desarrollo:**
Las semidiagonales miden 3 cm y 4 cm.

**Lado del rombo** (por Pitágoras):
$$\ell = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5 \text{ cm}$$

**Perímetro:** $P = 4 \times 5 = 20$ cm

**Área:** $A = \frac{d_1 \times d_2}{2} = \frac{6 \times 8}{2} = 24$ cm²

---

### Solución 4.4.5
**Contexto:** En un trapecio isósceles, los lados no paralelos son congruentes y forman triángulos rectángulos con la altura.

**Desarrollo:**
**Área:**
$$A = \frac{(B + b) \times h}{2} = \frac{(14 + 8) \times 4}{2} = \frac{22 \times 4}{2} = 44 \text{ cm}^2$$

**Lados no paralelos:**
La diferencia de bases es $14 - 8 = 6$ cm, repartida en 3 cm a cada lado.
$$\ell = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5 \text{ cm}$$

---

### Solución 4.4.7
**Contexto:** En un cuadrado, la diagonal $d$ y el lado $\ell$ se relacionan por $d = \ell\sqrt{2}$.

**Desarrollo:**
$$d = \ell\sqrt{2}$$
$$6\sqrt{2} = \ell\sqrt{2}$$
$$\ell = 6 \text{ cm}$$

**Perímetro:** $P = 4 \times 6 = 24$ cm

**Área:** $A = 6^2 = 36$ cm²

**Verificación alternativa:** $A = \frac{d^2}{2} = \frac{(6\sqrt{2})^2}{2} = \frac{72}{2} = 36$ cm² ✓

---

## 4.5 Polígonos

### Solución 4.5.1
**Contexto:** La suma de ángulos interiores de un polígono de $n$ lados es $(n-2) \times 180°$.

**Desarrollo:**
Para un octógono ($n = 8$):
$$S = (8 - 2) \times 180° = 6 \times 180° = 1080°$$

---

### Solución 4.5.2
**Contexto:** El número de diagonales de un polígono de $n$ lados es $\frac{n(n-3)}{2}$.

**Desarrollo:**
Para un decágono ($n = 10$):
$$D = \frac{10(10-3)}{2} = \frac{10 \times 7}{2} = 35 \text{ diagonales}$$

---

### Solución 4.5.3
**Contexto:** En un polígono regular, cada ángulo interior mide $\frac{(n-2) \times 180°}{n}$.

**Desarrollo:**
$$140° = \frac{(n-2) \times 180°}{n}$$
$$140n = 180n - 360$$
$$360 = 40n$$
$$n = 9$$

**Respuesta:** El polígono tiene **9 lados** (nonágono regular).

**Verificación:** $\frac{7 \times 180°}{9} = \frac{1260°}{9} = 140°$ ✓

---

### Solución 4.5.4
**Contexto:** Despejamos $n$ de la fórmula de suma de ángulos interiores.

**Desarrollo:**
$$(n - 2) \times 180° = 2340°$$
$$n - 2 = 13$$
$$n = 15$$

**Respuesta:** El polígono tiene **15 lados**.

---

### Solución 4.5.5
**Contexto:** Para un pentágono regular: apotema $a = \frac{\ell}{2\tan(36°)}$, área $A = \frac{P \times a}{2}$.

**Desarrollo:**
Con $\ell = 6$ cm:

**Apotema:**
$$a = \frac{6}{2\tan(36°)} = \frac{6}{2 \times 0.7265} \approx \frac{6}{1.453} \approx 4.13 \text{ cm}$$

**Área:**
$$A = \frac{5 \times 6 \times 4.13}{2} = \frac{123.9}{2} \approx 61.94 \text{ cm}^2$$

---

### Solución 4.5.7
**Contexto:** El ángulo exterior de un polígono regular es $\frac{360°}{n}$.

**Desarrollo:**
$$30° = \frac{360°}{n}$$
$$n = \frac{360°}{30°} = 12$$

**Respuesta:** Es un **dodecágono** (polígono de 12 lados).

---

## 4.6 Circunferencia y Círculo

### Solución 4.6.1
**Contexto:** Longitud de circunferencia: $C = 2\pi r$. Área del círculo: $A = \pi r^2$.

**Desarrollo:**
Con $r = 7$ cm:
$$C = 2\pi(7) = 14\pi \approx 43.98 \text{ cm}$$
$$A = \pi(7)^2 = 49\pi \approx 153.94 \text{ cm}^2$$

---

### Solución 4.6.3
**Contexto:** La longitud de un arco es proporcional al ángulo central: $L = \frac{\theta}{360°} \times 2\pi r$.

**Desarrollo:**
$$L = \frac{60°}{360°} \times 2\pi(9) = \frac{1}{6} \times 18\pi = 3\pi \approx 9.42 \text{ cm}$$

---

### Solución 4.6.4
**Contexto:** La distancia del centro a una cuerda y la semicuerda forman un triángulo rectángulo con el radio.

**Desarrollo:**
La cuerda de 8 cm tiene semicuerda de 4 cm.
Por Pitágoras:
$$r^2 = 4^2 + 3^2 = 16 + 9 = 25$$
$$r = 5 \text{ cm}$$

---

### Solución 4.6.5
**Contexto:** Un ángulo inscrito es la mitad del ángulo central que subtiende el mismo arco.

**Desarrollo:**
El arco que subtiende un ángulo inscrito de 35° mide:
$$\text{arco} = 2 \times 35° = 70°$$

---

### Solución 4.6.6
**Contexto:** El área de un sector circular es $A = \frac{\theta}{360°} \times \pi r^2$.

**Desarrollo:**
$$A = \frac{120°}{360°} \times \pi(6)^2 = \frac{1}{3} \times 36\pi = 12\pi \approx 37.70 \text{ cm}^2$$

---

### Solución 4.6.8
**Contexto:** La [tangente](../../../glossary.md#tangente) desde un punto exterior es perpendicular al radio en el punto de tangencia, formando un triángulo rectángulo.

**Desarrollo:**
Sea $T$ la longitud de la [tangente](../../../glossary.md#tangente):
$$T^2 + 5^2 = 13^2$$
$$T^2 = 169 - 25 = 144$$
$$T = 12 \text{ cm}$$

---

### Solución 4.6.11
**Contexto:** En un cuadrilátero inscrito en una circunferencia, los ángulos opuestos son suplementarios.

**Desarrollo:**
$$\alpha + \gamma = 180°$$
$$75° + \gamma = 180°$$
$$\gamma = 105°$$

**Justificación:** Los ángulos opuestos de un cuadrilátero inscrito suman 180° porque cada uno subtiende un arco, y los dos arcos juntos forman la circunferencia completa.

---

## 4.7 Áreas de Figuras Planas

### Solución 4.7.1
**Contexto:** Área de triángulo: $A = \frac{bh}{2}$.

$$A = \frac{12 \times 8}{2} = 48 \text{ cm}^2$$

---

### Solución 4.7.2
**Contexto:** En un rectángulo, el perímetro es $P = 2(l + a)$ y el área es $A = l \times a$.

**Desarrollo:**
$$34 = 2(12 + a) \Rightarrow 17 = 12 + a \Rightarrow a = 5 \text{ cm}$$
$$A = 12 \times 5 = 60 \text{ cm}^2$$

---

### Solución 4.7.4
**Contexto:** La fórmula de Herón: $A = \sqrt{s(s-a)(s-b)(s-c)}$ donde $s = \frac{a+b+c}{2}$.

**Desarrollo:**
$$s = \frac{13 + 14 + 15}{2} = 21$$
$$A = \sqrt{21(21-13)(21-14)(21-15)} = \sqrt{21 \times 8 \times 7 \times 6}$$
$$A = \sqrt{7056} = 84 \text{ cm}^2$$

---

### Solución 4.7.5
**Contexto:** Área del rombo: $A = \frac{d_1 \times d_2}{2}$. El lado se calcula con Pitágoras usando las semidiagonales.

**Desarrollo:**
$$A = \frac{10 \times 24}{2} = 120 \text{ cm}^2$$

**Lado:** $\ell = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13$ cm

**Perímetro:** $P = 4 \times 13 = 52$ cm

---

### Solución 4.7.6
**Contexto:** Para figuras compuestas, sumamos las áreas de las partes.

**Desarrollo:**
- Área del rectángulo: $8 \times 6 = 48$ cm²
- Área del semicírculo: $\frac{\pi(3)^2}{2} = \frac{9\pi}{2} \approx 14.14$ cm²

**Área total:** $48 + \frac{9\pi}{2} \approx 62.14$ cm²

---

### Solución 4.7.8
**Contexto:** Comparamos áreas de figuras con el mismo perímetro.

**Desarrollo:**
**Triángulo equilátero:** lado $= \frac{24}{3} = 8$ cm
$$A_{\triangle} = \frac{8^2\sqrt{3}}{4} = 16\sqrt{3} \approx 27.71 \text{ cm}^2$$

**Cuadrado:** lado $= \frac{24}{4} = 6$ cm
$$A_{\square} = 6^2 = 36 \text{ cm}^2$$

**Respuesta:** El **cuadrado** tiene mayor área.

---

## 4.8 Semejanza

### Solución 4.8.1
**Contexto:** Dos triángulos son semejantes si sus lados son proporcionales (criterio LLL).

**Desarrollo:**
Verificamos proporcionalidad:
$$\frac{6}{3} = \frac{8}{4} = \frac{10}{5} = 2$$

Todos los cocientes son iguales.

**Respuesta:** **Sí, son semejantes** con razón de semejanza 2:1.

---

### Solución 4.8.3
**Contexto:** El Teorema de Thales establece que una paralela a un lado de un triángulo divide a los otros dos lados proporcionalmente.

**Desarrollo:**
Por Thales:
$$\frac{AD}{AB} = \frac{DE}{BC}$$
$$\frac{4}{4+6} = \frac{5}{BC}$$
$$\frac{4}{10} = \frac{5}{BC}$$
$$BC = \frac{5 \times 10}{4} = 12.5 \text{ cm}$$

---

### Solución 4.8.4
**Contexto:** A la misma hora, los rayos del sol forman ángulos iguales, creando triángulos semejantes.

**Desarrollo:**
$$\frac{\text{altura poste}}{\text{sombra poste}} = \frac{\text{altura edificio}}{\text{sombra edificio}}$$
$$\frac{8}{6} = \frac{h}{45}$$
$$h = \frac{8 \times 45}{6} = 60 \text{ m}$$

---

### Solución 4.8.5
**Contexto:** La razón de áreas es el cuadrado de la razón de semejanza.

**Desarrollo:**
$$\frac{A_1}{A_2} = k^2$$
$$\frac{25}{100} = \frac{1}{4} = k^2$$
$$k = \frac{1}{2}$$

El triángulo menor tiene razón 1:2 respecto al mayor.

Si $\ell_1 = 6$ cm corresponde a $\ell_2$:
$$\frac{\ell_1}{\ell_2} = \frac{1}{2} \Rightarrow \ell_2 = 12 \text{ cm}$$

---

### Solución 4.8.6
**Contexto:** Las relaciones métricas en el triángulo rectángulo establecen que la altura a la hipotenusa es media geométrica de las proyecciones.

**Desarrollo:**
$$CH = \sqrt{AH \times HB} = \sqrt{4 \times 9} = \sqrt{36} = 6 \text{ cm}$$
$$AC = \sqrt{AH \times AB} = \sqrt{4 \times 13} = \sqrt{52} = 2\sqrt{13} \text{ cm}$$
$$BC = \sqrt{HB \times AB} = \sqrt{9 \times 13} = \sqrt{117} = 3\sqrt{13} \text{ cm}$$

**Verificación:** $AC^2 + BC^2 = 52 + 117 = 169 = 13^2 = AB^2$ ✓

---

## 4.9 Teorema de Pitágoras

### Solución 4.9.1
**Contexto:** En un triángulo rectángulo: $c^2 = a^2 + b^2$ donde $c$ es la hipotenusa.

$$c = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10 \text{ cm}$$

---

### Solución 4.9.2
$$b = \sqrt{17^2 - 8^2} = \sqrt{289 - 64} = \sqrt{225} = 15 \text{ cm}$$

---

### Solución 4.9.3
**Desarrollo:**
Verificamos: $7^2 + 24^2 = 49 + 576 = 625 = 25^2$ ✓

**Respuesta:** **Sí es rectángulo** (7, 24, 25 es una terna pitagórica).

---

### Solución 4.9.4
**Desarrollo:**
$$h = \sqrt{5^2 - 3^2} = \sqrt{25 - 9} = \sqrt{16} = 4 \text{ m}$$

---

### Solución 4.9.6
**Contexto:** La diagonal de un cuadrado de lado $\ell$ es $d = \ell\sqrt{2}$.

$$d = 8\sqrt{2} \approx 11.31 \text{ cm}$$

---

### Solución 4.9.7
**Desarrollo:**
Las semidiagonales miden 15 cm y 20 cm.
$$\ell = \sqrt{15^2 + 20^2} = \sqrt{225 + 400} = \sqrt{625} = 25 \text{ cm}$$

---

### Solución 4.9.9
**Desarrollo:**
La altura biseca la base: cada mitad mide 8 cm.
$$h = \sqrt{17^2 - 8^2} = \sqrt{289 - 64} = \sqrt{225} = 15 \text{ cm}$$
$$A = \frac{16 \times 15}{2} = 120 \text{ cm}^2$$

---

### Solución 4.9.11
**Contexto:** La diagonal espacial de un cubo de arista $a$ es $d = a\sqrt{3}$.

$$d = 6\sqrt{3} \approx 10.39 \text{ cm}$$

**Demostración:** Primero la diagonal de una cara: $d_1 = 6\sqrt{2}$.
Luego: $d = \sqrt{d_1^2 + 6^2} = \sqrt{72 + 36} = \sqrt{108} = 6\sqrt{3}$ ✓

---

### Solución 4.9.12
**Desarrollo:**
$$x^2 + (x+7)^2 = (x+8)^2$$
$$x^2 + x^2 + 14x + 49 = x^2 + 16x + 64$$
$$x^2 - 2x - 15 = 0$$
$$(x-5)(x+3) = 0$$
$$x = 5 \text{ (descartamos } x = -3)$$

**Respuesta:** Los lados miden **5 cm**, **12 cm** y **13 cm**.

**Verificación:** $5^2 + 12^2 = 25 + 144 = 169 = 13^2$ ✓

---

## 4.10 Geometría del Espacio

### Solución 4.10.1
**Contexto:** Prisma rectangular: $V = abc$, $A_T = 2(ab + bc + ac)$.

$$V = 3 \times 4 \times 5 = 60 \text{ cm}^3$$
$$A_T = 2(12 + 20 + 15) = 2(47) = 94 \text{ cm}^2$$

---

### Solución 4.10.2
**Contexto:** Cubo de arista $a$: $V = a^3$, $A_T = 6a^2$, diagonal $= a\sqrt{3}$.

$$V = 7^3 = 343 \text{ cm}^3$$
$$A_T = 6(7)^2 = 294 \text{ cm}^2$$
$$d = 7\sqrt{3} \approx 12.12 \text{ cm}$$

---

### Solución 4.10.3
**Contexto:** Volumen de pirámide: $V = \frac{1}{3} A_b \times h$.

$$V = \frac{1}{3}(10)^2 \times 12 = \frac{1200}{3} = 400 \text{ cm}^3$$

---

### Solución 4.10.4
**Contexto:** Cilindro: $V = \pi r^2 h$, $A_L = 2\pi rh$, $A_T = 2\pi r(r + h)$.

$$V = \pi(5)^2(10) = 250\pi \approx 785.4 \text{ cm}^3$$
$$A_L = 2\pi(5)(10) = 100\pi \approx 314.2 \text{ cm}^2$$
$$A_T = 2\pi(5)(5 + 10) = 150\pi \approx 471.2 \text{ cm}^2$$

---

### Solución 4.10.5
**Contexto:** Cono: generatriz $g = \sqrt{r^2 + h^2}$, $V = \frac{1}{3}\pi r^2 h$, $A_T = \pi r(r + g)$.

**Generatriz:**
$$g = \sqrt{6^2 + 8^2} = \sqrt{100} = 10 \text{ cm}$$

**Volumen:**
$$V = \frac{1}{3}\pi(6)^2(8) = 96\pi \approx 301.6 \text{ cm}^3$$

**Área total:**
$$A_T = \pi(6)(6 + 10) = 96\pi \approx 301.6 \text{ cm}^2$$

---

### Solución 4.10.6
**Contexto:** Esfera: $V = \frac{4}{3}\pi r^3$, $A = 4\pi r^2$.

$$V = \frac{4}{3}\pi(9)^3 = 972\pi \approx 3053.6 \text{ cm}^3$$
$$A = 4\pi(9)^2 = 324\pi \approx 1017.9 \text{ cm}^2$$

---

### Solución 4.10.8
**Contexto:** El volumen del cono es un tercio del volumen del cilindro con misma base y altura.

$$V_{cono} = \frac{1}{3} V_{cilindro} = \frac{450}{3} = 150 \text{ cm}^3$$

---

### Solución 4.10.9
**Desarrollo:**
$$V_{cilindro} = \pi(6)^2(10) = 360\pi$$
$$V_{semiesfera} = \frac{1}{2} \times \frac{4}{3}\pi(6)^3 = 144\pi$$
$$V_{total} = 360\pi + 144\pi = 504\pi \approx 1583.4 \text{ cm}^3$$

---

### Solución 4.10.12
**Contexto:** Volumen del tronco de cono: $V = \frac{1}{3}\pi h(R^2 + Rr + r^2)$.

$$V = \frac{1}{3}\pi(4)(36 + 18 + 9) = \frac{4\pi(63)}{3} = 84\pi \approx 263.9 \text{ cm}^3$$

---

## Soluciones de Síntesis

### Solución 4.S.1
**Contexto:** Ley de cosenos: $c^2 = a^2 + b^2 - 2ab\cos C$.

**Desarrollo:**
$$BC^2 = AB^2 + AC^2 - 2(AB)(AC)\cos A$$
$$BC^2 = 64 + 100 - 2(8)(10)\cos 60°$$
$$BC^2 = 164 - 160(0.5) = 164 - 80 = 84$$
$$BC = \sqrt{84} = 2\sqrt{21} \approx 9.17 \text{ cm}$$

---

### Solución 4.S.3
**Contexto:** Descomponemos la figura en rectángulo y semicírculo.

**Desarrollo:**
- Ancho = 2 m (también diámetro del semicírculo)
- Radio del semicírculo = 1 m
- Altura del rectángulo = $3 - 1 = 2$ m

$$A_{rect} = 2 \times 2 = 4 \text{ m}^2$$
$$A_{semi} = \frac{\pi(1)^2}{2} = \frac{\pi}{2} \approx 1.57 \text{ m}^2$$
$$A_{total} = 4 + \frac{\pi}{2} \approx 5.57 \text{ m}^2$$
