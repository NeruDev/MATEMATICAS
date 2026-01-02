<!--
::METADATA::
type: method
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Métodos de Geometría

> Guía completa de métodos geométricos con algoritmos detallados, tablas de procedimientos y ejemplos paso a paso.

---

## Método 1: Calcular Ángulos en Figuras

**Cuándo Usar:** Para encontrar ángulos desconocidos usando propiedades geométricas.

### Propiedades Fundamentales

| Configuración | Suma de Ángulos |
|---------------|-----------------|
| Ángulos suplementarios | $\alpha + \beta = 180°$ |
| Ángulos complementarios | $\alpha + \beta = 90°$ |
| Triángulo | $\alpha + \beta + \gamma = 180°$ |
| Cuadrilátero | $\alpha + \beta + \gamma + \delta = 360°$ |
| Polígono de $n$ lados | $(n - 2) \times 180°$ |
| Ángulo exterior triángulo | $\alpha_{ext} = \beta + \gamma$ |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar configuración | Tipo de figura o relación angular |
| 2 | Aplicar propiedad | Según la configuración encontrada |
| 3 | Plantear ecuación | Con los ángulos conocidos y desconocidos |
| 4 | Resolver | Despejar el ángulo buscado |

### Ejemplo Detallado

**Problema:** En un triángulo, un ángulo mide $48°$, otro mide el doble del tercero. Hallar todos los ángulos.

---

**Paso 1: Definir variables**

Sea $x$ el tercer ángulo. Entonces:
- Primer ángulo: $48°$
- Segundo ángulo: $2x$
- Tercer ángulo: $x$

---

**Paso 2: Aplicar propiedad de suma**

$$48° + 2x + x = 180°$$

---

**Paso 3: Resolver**

$$48° + 3x = 180°$$
$$3x = 132°$$
$$x = 44°$$

---

**Paso 4: Calcular todos los ángulos**

- Primer ángulo: $48°$
- Segundo ángulo: $2(44°) = 88°$
- Tercer ángulo: $44°$

---

**Verificación:**

$$48° + 88° + 44° = 180° \checkmark$$

$$\boxed{48°, \quad 88°, \quad 44°}$$

---

## Método 2: Calcular Perímetro y Área de Polígonos

**Cuándo Usar:** Para cualquier polígono regular o irregular.

### Fórmulas de Perímetro

| Figura | Fórmula |
|--------|---------|
| Polígono | Suma de todos los lados |
| Polígono regular | $P = n \times s$ |
| Circunferencia | $C = 2\pi r = \pi d$ |

### Fórmulas de Área

| Figura | Fórmula |
|--------|---------|
| Triángulo | $A = \frac{bh}{2}$ |
| Rectángulo | $A = bh$ |
| Paralelogramo | $A = bh$ |
| Trapecio | $A = \frac{(B + b)h}{2}$ |
| Rombo | $A = \frac{d_1 \times d_2}{2}$ |
| Polígono regular | $A = \frac{P \times a}{2}$ (apotema) |
| Círculo | $A = \pi r^2$ |

### Ejemplo Detallado

**Problema:** Calcular el área de un trapecio con bases de 12 cm y 8 cm, y altura de 5 cm.

---

**Fórmula:**

$$A = \frac{(B + b) \times h}{2}$$

---

**[Sustitución](../../../glossary.md#sustitucion):**

$$A = \frac{(12 + 8) \times 5}{2} = \frac{20 \times 5}{2} = \frac{100}{2} = 50$$

$$\boxed{A = 50 \text{ cm}^2}$$

---

## Método 3: Aplicar Criterios de Congruencia de Triángulos

**Cuándo Usar:** Para demostrar que dos triángulos son idénticos (misma forma y tamaño).

### Criterios de Congruencia

| Criterio | Significado | Condición |
|----------|-------------|-----------|
| LLL | Lado-Lado-Lado | Tres lados iguales |
| LAL | Lado-Ángulo-Lado | Dos lados y el ángulo entre ellos |
| ALA | Ángulo-Lado-Ángulo | Dos ángulos y el lado entre ellos |
| AAL | Ángulo-Ángulo-Lado | Dos ángulos y un lado correspondiente |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar elementos | Listar lados y ángulos conocidos |
| 2 | Buscar correspondencias | Elementos iguales en ambos triángulos |
| 3 | Verificar criterio | Determinar cuál criterio aplica |
| 4 | Concluir | Afirmar congruencia y consecuencias |

### Ejemplo Detallado

**Problema:** Demostrar que los triángulos $ABC$ y $DEF$ son congruentes si:
- $AB = DE = 7$ cm
- $AC = DF = 9$ cm
- $\angle A = \angle D = 52°$

---

**Paso 1: Identificar elementos**

| Triángulo ABC | Triángulo DEF |
|---------------|---------------|
| $AB = 7$ | $DE = 7$ |
| $AC = 9$ | $DF = 9$ |
| $\angle A = 52°$ | $\angle D = 52°$ |

---

**Paso 2: Verificar criterio LAL**

- Lado $AB = DE$ ✓
- Ángulo incluido $\angle A = \angle D$ ✓
- Lado $AC = DF$ ✓

---

**Paso 3: Conclusión**

Por el criterio **LAL**, los triángulos son congruentes:

$$\triangle ABC \cong \triangle DEF$$

Por lo tanto:
- $BC = EF$
- $\angle B = \angle E$
- $\angle C = \angle F$

$$\boxed{\triangle ABC \cong \triangle DEF \text{ por LAL}}$$

---

## Método 4: Aplicar el Teorema de Pitágoras

**Cuándo Usar:** En triángulos rectángulos para encontrar un lado desconocido.

### Fórmula

$$c^2 = a^2 + b^2$$

Donde $c$ es la hipotenusa (lado opuesto al ángulo recto).

### Formas Despejadas

| Buscar | Fórmula |
|--------|---------|
| Hipotenusa | $c = \sqrt{a^2 + b^2}$ |
| Cateto | $a = \sqrt{c^2 - b^2}$ |

### Ternas Pitagóricas Comunes

| Terna | Múltiplos |
|-------|-----------|
| (3, 4, 5) | (6, 8, 10), (9, 12, 15), ... |
| (5, 12, 13) | (10, 24, 26), ... |
| (8, 15, 17) | (16, 30, 34), ... |
| (7, 24, 25) | (14, 48, 50), ... |

### Ejemplo Detallado

**Problema:** Una escalera de 13 m se apoya contra una pared. Si la [base](../../../glossary.md#base) está a 5 m de la pared, ¿a qué altura llega?

---

**Paso 1: Identificar elementos**

- Hipotenusa: escalera = 13 m
- Cateto horizontal: distancia a la pared = 5 m
- Cateto vertical: altura = ?

---

**Paso 2: Aplicar Pitágoras**

$$13^2 = 5^2 + h^2$$
$$169 = 25 + h^2$$
$$h^2 = 144$$
$$h = 12$$

---

**Verificación:** $(5, 12, 13)$ es terna pitagórica ✓

$$\boxed{h = 12 \text{ m}}$$

---

## Método 5: Aplicar Criterios de Semejanza de Triángulos

**Cuándo Usar:** Cuando dos triángulos tienen la misma forma pero diferente tamaño.

### Criterios de Semejanza

| Criterio | Significado | Condición |
|----------|-------------|-----------|
| AA | Ángulo-Ángulo | Dos ángulos iguales |
| LAL | Lado-Ángulo-Lado | Dos lados proporcionales y ángulo incluido igual |
| LLL | Lado-Lado-Lado | Tres lados proporcionales |

### Propiedades de Triángulos Semejantes

| Elemento | Relación |
|----------|----------|
| Lados correspondientes | Proporcionales (razón $k$) |
| Ángulos correspondientes | Iguales |
| Perímetros | Razón $k$ |
| Áreas | Razón $k^2$ |

### Ejemplo Detallado

**Problema:** Los triángulos $ABC$ y $DEF$ son semejantes con razón $\frac{AB}{DE} = \frac{3}{2}$. Si $BC = 12$ cm, $AC = 15$ cm y el área de $DEF$ es 40 cm², hallar $EF$, $DF$ y el área de $ABC$.

---

**Paso 1: Identificar la razón de semejanza**

$$k = \frac{3}{2} = 1.5$$

---

**Paso 2: Calcular lados correspondientes**

$$\frac{BC}{EF} = k \Rightarrow EF = \frac{BC}{k} = \frac{12}{1.5} = 8 \text{ cm}$$

$$\frac{AC}{DF} = k \Rightarrow DF = \frac{AC}{k} = \frac{15}{1.5} = 10 \text{ cm}$$

---

**Paso 3: Calcular área**

$$\frac{A_{ABC}}{A_{DEF}} = k^2 = 2.25$$

$$A_{ABC} = A_{DEF} \times k^2 = 40 \times 2.25 = 90 \text{ cm}^2$$

$$\boxed{EF = 8 \text{ cm}, \quad DF = 10 \text{ cm}, \quad A_{ABC} = 90 \text{ cm}^2}$$

---

## Método 6: Calcular Área por Fórmula de Herón

**Cuándo Usar:** Para calcular el área de un triángulo conociendo solo sus tres lados.

### Fórmula

$$A = \sqrt{s(s-a)(s-b)(s-c)}$$

Donde $s = \frac{a + b + c}{2}$ es el semiperímetro.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Calcular semiperímetro | $s = \frac{a + b + c}{2}$ |
| 2 | Calcular diferencias | $(s - a)$, $(s - b)$, $(s - c)$ |
| 3 | Multiplicar | $s \times (s-a) \times (s-b) \times (s-c)$ |
| 4 | Extraer raíz | $A = \sqrt{\text{producto}}$ |

### Ejemplo Detallado

**Problema:** Calcular el área de un triángulo con lados $a = 13$, $b = 14$, $c = 15$.

---

**Paso 1: Semiperímetro**

$$s = \frac{13 + 14 + 15}{2} = \frac{42}{2} = 21$$

---

**Paso 2: Diferencias**

$$s - a = 21 - 13 = 8$$
$$s - b = 21 - 14 = 7$$
$$s - c = 21 - 15 = 6$$

---

**Paso 3: Producto**

$$s(s-a)(s-b)(s-c) = 21 \times 8 \times 7 \times 6 = 7056$$

---

**Paso 4: Raíz cuadrada**

$$A = \sqrt{7056} = 84$$

---

**Verificación alternativa:** Este es un triángulo que puede descomponerse:
- [Base](../../../glossary.md#base) 14, altura 12 → $A = \frac{14 \times 12}{2} = 84$ ✓

$$\boxed{A = 84 \text{ unidades}^2}$$

---

## Método 7: Calcular Elementos de Círculos

**Cuándo Usar:** Problemas que involucran circunferencia, arcos, sectores, cuerdas.

### Fórmulas Fundamentales

| Elemento | Fórmula |
|----------|---------|
| Circunferencia | $C = 2\pi r$ |
| Área del círculo | $A = \pi r^2$ |
| Longitud de arco | $L = \frac{\theta}{360°} \times 2\pi r = \frac{\theta}{180°} \times \pi r$ |
| Área de sector | $A_s = \frac{\theta}{360°} \times \pi r^2$ |
| Área de segmento | $A_{seg} = A_{sector} - A_{triángulo}$ |
| Ángulo central | Igual al arco que subtiende |
| Ángulo inscrito | Mitad del arco que subtiende |

### Ejemplo Detallado

**Problema:** Un círculo tiene radio 10 cm. Calcular la longitud del arco y el área del sector correspondiente a un ángulo central de 72°.

---

**Paso 1: Longitud del arco**

$$L = \frac{\theta}{360°} \times 2\pi r = \frac{72°}{360°} \times 2\pi(10)$$

$$L = \frac{1}{5} \times 20\pi = 4\pi \approx 12.57 \text{ cm}$$

---

**Paso 2: Área del sector**

$$A_s = \frac{\theta}{360°} \times \pi r^2 = \frac{72°}{360°} \times \pi(10)^2$$

$$A_s = \frac{1}{5} \times 100\pi = 20\pi \approx 62.83 \text{ cm}^2$$

---

**Verificación proporcional:**

$$\frac{72°}{360°} = \frac{1}{5} = 0.2$$

El arco es $\frac{1}{5}$ de la circunferencia total: $\frac{4\pi}{20\pi} = \frac{1}{5}$ ✓

El sector es $\frac{1}{5}$ del área total: $\frac{20\pi}{100\pi} = \frac{1}{5}$ ✓

$$\boxed{L = 4\pi \text{ cm} \approx 12.57 \text{ cm}, \quad A_s = 20\pi \text{ cm}^2 \approx 62.83 \text{ cm}^2}$$

---

## Método 8: Calcular Volumen y Área Superficial de Sólidos

**Cuándo Usar:** Problemas tridimensionales con prismas, pirámides, cilindros, conos, esferas.

### Fórmulas de Volumen

| Sólido | Fórmula |
|--------|---------|
| Prisma/Cilindro | $V = A_{base} \times h$ |
| Pirámide/Cono | $V = \frac{1}{3} A_{base} \times h$ |
| Esfera | $V = \frac{4}{3}\pi r^3$ |
| Cubo | $V = a^3$ |
| Caja rectangular | $V = lwh$ |

### Fórmulas de Área Superficial

| Sólido | Fórmula |
|--------|---------|
| Cubo | $A_s = 6a^2$ |
| Caja rectangular | $A_s = 2(lw + lh + wh)$ |
| Cilindro | $A_s = 2\pi r^2 + 2\pi rh$ |
| Cono | $A_s = \pi r^2 + \pi r g$ (g = generatriz) |
| Esfera | $A_s = 4\pi r^2$ |

### Ejemplo Detallado

**Problema:** Un cono tiene radio de base 6 cm y altura 8 cm. Calcular volumen y área superficial.

---

**Paso 1: Calcular generatriz**

$$g = \sqrt{r^2 + h^2} = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10 \text{ cm}$$

---

**Paso 2: Calcular volumen**

$$V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi(6)^2(8) = \frac{1}{3}\pi(36)(8) = 96\pi$$

$$V = 96\pi \approx 301.59 \text{ cm}^3$$

---

**Paso 3: Calcular área superficial**

$$A_s = \pi r^2 + \pi r g = \pi(6)^2 + \pi(6)(10) = 36\pi + 60\pi = 96\pi$$

$$A_s = 96\pi \approx 301.59 \text{ cm}^2$$

---

**Nota:** Es coincidencia que $V$ (en $\pi$ cm³) y $A_s$ (en $\pi$ cm²) sean numéricamente iguales.

$$\boxed{V = 96\pi \text{ cm}^3 \approx 301.59 \text{ cm}^3, \quad A_s = 96\pi \text{ cm}^2 \approx 301.59 \text{ cm}^2}$$

---

## Método 9: Aplicar el Teorema de Tales

**Cuándo Usar:** Cuando líneas paralelas cortan a transversales, o para dividir segmentos proporcionalmente.

### Teorema de Tales

Si una línea paralela a un lado del triángulo corta a los otros dos lados, los divide proporcionalmente:

$$\frac{AD}{DB} = \frac{AE}{EC}$$

### Proporcionalidad en Transversales

Si varias paralelas cortan a dos transversales:

$$\frac{AB}{BC} = \frac{A'B'}{B'C'}$$

### Ejemplo Detallado

**Problema:** En el triángulo $ABC$, $DE \parallel BC$ con $D$ en $AB$ y $E$ en $AC$. Si $AD = 4$, $DB = 6$, y $AE = 5$, hallar $EC$ y la razón $\frac{DE}{BC}$.

---

**Paso 1: Aplicar Tales para hallar EC**

$$\frac{AD}{DB} = \frac{AE}{EC}$$

$$\frac{4}{6} = \frac{5}{EC}$$

$$EC = \frac{6 \times 5}{4} = \frac{30}{4} = 7.5$$

---

**Paso 2: Razón de segmentos paralelos**

Por semejanza de triángulos $ADE$ y $ABC$:

$$\frac{DE}{BC} = \frac{AD}{AB} = \frac{AD}{AD + DB} = \frac{4}{4 + 6} = \frac{4}{10} = \frac{2}{5}$$

---

**Verificación:**

$$\frac{AE}{AC} = \frac{5}{5 + 7.5} = \frac{5}{12.5} = \frac{2}{5} = \frac{AD}{AB} \checkmark$$

$$\boxed{EC = 7.5, \quad \frac{DE}{BC} = \frac{2}{5}}$$

---

## Método 10: Calcular con Polígonos Regulares

**Cuándo Usar:** Triángulos equiláteros, cuadrados, pentágonos, hexágonos, etc.

### Fórmulas Generales (Polígono Regular de $n$ lados)

| Elemento | Fórmula |
|----------|---------|
| Suma de ángulos interiores | $(n - 2) \times 180°$ |
| Ángulo interior | $\frac{(n - 2) \times 180°}{n}$ |
| Ángulo exterior | $\frac{360°}{n}$ |
| Apotema | $a = \frac{s}{2\tan(\frac{180°}{n})}$ |
| Área | $A = \frac{P \times a}{2} = \frac{n \times s \times a}{2}$ |

### Tabla de Polígonos Comunes

| Polígono | $n$ | Ángulo Interior | Ángulo Exterior |
|----------|-----|-----------------|-----------------|
| Triángulo equilátero | 3 | 60° | 120° |
| Cuadrado | 4 | 90° | 90° |
| Pentágono | 5 | 108° | 72° |
| Hexágono | 6 | 120° | 60° |
| Octágono | 8 | 135° | 45° |
| Decágono | 10 | 144° | 36° |
| Dodecágono | 12 | 150° | 30° |

### Ejemplo Detallado

**Problema:** Calcular el área de un hexágono regular con lado de 8 cm.

---

**Paso 1: Calcular apotema**

Para hexágono regular: la apotema forma un triángulo 30-60-90 con el radio y medio lado.

$$a = \frac{s}{2\tan(30°)} = \frac{8}{2 \times \frac{1}{\sqrt{3}}} = \frac{8\sqrt{3}}{2} = 4\sqrt{3} \approx 6.93 \text{ cm}$$

---

**Paso 2: Calcular perímetro**

$$P = 6 \times 8 = 48 \text{ cm}$$

---

**Paso 3: Calcular área**

$$A = \frac{P \times a}{2} = \frac{48 \times 4\sqrt{3}}{2} = 96\sqrt{3} \approx 166.28 \text{ cm}^2$$

---

**Método alternativo:** El hexágono regular se divide en 6 triángulos equiláteros.

$$A_{tri.eq.} = \frac{s^2\sqrt{3}}{4} = \frac{64\sqrt{3}}{4} = 16\sqrt{3}$$

$$A_{hex} = 6 \times 16\sqrt{3} = 96\sqrt{3} \checkmark$$

$$\boxed{A = 96\sqrt{3} \text{ cm}^2 \approx 166.28 \text{ cm}^2}$$

---

## Método 11: Resolver con Coordenadas (Geometría Analítica Básica)

**Cuándo Usar:** Cuando se dan puntos en el plano cartesiano.

### Fórmulas Básicas

| Concepto | Fórmula |
|----------|---------|
| Distancia | $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ |
| Punto medio | $M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$ |
| Pendiente | $m = \frac{y_2 - y_1}{x_2 - x_1}$ |
| Área triángulo | $A = \frac{1}{2}\lvert x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2) \rvert$ |

### Ejemplo Detallado

**Problema:** Dados los puntos $A(1, 2)$, $B(7, 2)$ y $C(4, 8)$, calcular el perímetro y área del triángulo.

---

**Paso 1: Calcular longitudes de los lados**

$$AB = \sqrt{(7-1)^2 + (2-2)^2} = \sqrt{36 + 0} = 6$$

$$BC = \sqrt{(4-7)^2 + (8-2)^2} = \sqrt{9 + 36} = \sqrt{45} = 3\sqrt{5}$$

$$AC = \sqrt{(4-1)^2 + (8-2)^2} = \sqrt{9 + 36} = \sqrt{45} = 3\sqrt{5}$$

---

**Paso 2: Perímetro**

$$P = 6 + 3\sqrt{5} + 3\sqrt{5} = 6 + 6\sqrt{5} \approx 19.42$$

---

**Paso 3: Área (fórmula del [determinante](../../../glossary.md#determinante))**

$$A = \frac{1}{2}|x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|$$

$$A = \frac{1}{2}|1(2 - 8) + 7(8 - 2) + 4(2 - 2)|$$

$$A = \frac{1}{2}|1(-6) + 7(6) + 4(0)|$$

$$A = \frac{1}{2}|-6 + 42 + 0| = \frac{1}{2}(36) = 18$$

---

**Verificación:** Base $AB = 6$, altura $= 8 - 2 = 6$

$$A = \frac{6 \times 6}{2} = 18 \checkmark$$

$$\boxed{P = 6 + 6\sqrt{5} \approx 19.42, \quad A = 18 \text{ unidades}^2}$$

---

## Método 12: Aplicar Teoremas de Circunferencia

**Cuándo Usar:** Problemas con cuerdas, tangentes, secantes en círculos.

### Teoremas de Potencia

| Configuración | Fórmula |
|---------------|---------|
| Dos cuerdas | $PA \times PB = PC \times PD$ |
| Secante-[Tangente](../../../glossary.md#tangente) | $PT^2 = PA \times PB$ |
| Dos secantes | $PA \times PB = PC \times PD$ |

### Teoremas de Ángulos

| Ángulo | Fórmula |
|--------|---------|
| Central | Igual al arco |
| Inscrito | Mitad del arco |
| Interior (cuerdas) | $\frac{\text{arco}_1 + \text{arco}_2}{2}$ |
| Exterior (secantes) | $\frac{\text{arco mayor} - \text{arco [menor](../../../glossary.md#menor)}}{2}$ |

### Ejemplo Detallado

**Problema:** Desde un punto $P$ exterior a un círculo se [traza](../../../glossary.md#traza) una [tangente](../../../glossary.md#tangente) $PT = 12$ cm y una secante $PAB$ donde $PA = 8$ cm. Hallar $AB$.

---

**Paso 1: Aplicar teorema de potencia**

$$PT^2 = PA \times PB$$

$$12^2 = 8 \times PB$$

$$144 = 8 \times PB$$

$$PB = 18 \text{ cm}$$

---

**Paso 2: Calcular AB**

$$AB = PB - PA = 18 - 8 = 10 \text{ cm}$$

---

**Verificación:**

$$PT^2 = 144, \quad PA \times PB = 8 \times 18 = 144 \checkmark$$

$$\boxed{AB = 10 \text{ cm}}$$

---

## Resumen de Fórmulas

| Concepto | Fórmula |
|----------|---------|
| Suma ángulos triángulo | $\alpha + \beta + \gamma = 180°$ |
| Suma ángulos polígono | $(n - 2) \times 180°$ |
| Pitágoras | $c^2 = a^2 + b^2$ |
| Área triángulo | $A = \frac{bh}{2}$ |
| Herón | $A = \sqrt{s(s-a)(s-b)(s-c)}$ |
| Circunferencia | $C = 2\pi r$ |
| Área círculo | $A = \pi r^2$ |
| Volumen esfera | $V = \frac{4}{3}\pi r^3$ |
| Área esfera | $A = 4\pi r^2$ |
| Tales | $\frac{AD}{DB} = \frac{AE}{EC}$ |

---

## Errores Comunes

| Error | Corrección |
|-------|------------|
| Confundir radio y diámetro | $d = 2r$, usar el correcto en la fórmula |
| Olvidar elevar al cuadrado en Pitágoras | Es $c^2$, no $c$ |
| Usar fórmula de área incorrecta | Verificar qué altura corresponde a qué base |
| Confundir perímetro con área | Perímetro = longitud, Área = superficie |
| Error en ángulos exteriores | Exterior = $180°$ - interior |
| Confundir semejanza con congruencia | Semejanza: proporcional, Congruencia: igual |
| Olvidar factor $\frac{1}{3}$ en pirámides/conos | Volumen es un tercio del prisma/cilindro |
