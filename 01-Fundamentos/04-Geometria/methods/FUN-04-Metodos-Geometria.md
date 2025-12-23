# Métodos de Geometría

---

## Método 1: Encontrar ángulos usando paralelas y transversal

**Contexto:** Cuando una transversal corta dos rectas paralelas, se forman ángulos con relaciones específicas.

**Pasos:**
1. Identificar las rectas paralelas y la transversal
2. Clasificar los ángulos (correspondientes, alternos internos, etc.)
3. Aplicar la relación correspondiente (iguales o suplementarios)
4. Plantear ecuación si hay incógnitas

**Ejemplo:** Si dos rectas paralelas son cortadas por una transversal y un ángulo mide $3x + 10°$ y su alterno interno mide $5x - 20°$, encuentra $x$.

| Paso | Operación |
|------|-----------|
| Relación | Alternos internos son iguales |
| Ecuación | $3x + 10 = 5x - 20$ |
| Resolver | $30 = 2x$ → $x = 15°$ |

**Verificación:** $3(15) + 10 = 55°$ y $5(15) - 20 = 55°$ ✓

---

## Método 2: Calcular ángulos interiores de polígonos

**Contexto:** Usar la fórmula de suma de ángulos interiores para polígonos regulares o irregulares.

**Pasos:**
1. Contar el número de lados $n$
2. Aplicar $S = (n-2) \times 180°$
3. Para polígonos regulares: dividir entre $n$

**Ejemplo:** ¿Cuánto mide cada ángulo interior de un octágono regular?

| Paso | Cálculo |
|------|---------|
| Suma de ángulos | $(8-2) \times 180° = 1080°$ |
| Cada ángulo | $1080° \div 8 = 135°$ |

---

## Método 3: Aplicar criterios de congruencia de triángulos

**Contexto:** Demostrar que dos triángulos son iguales para deducir propiedades.

**Pasos:**
1. Identificar los elementos conocidos de ambos triángulos
2. Verificar si cumplen algún criterio (LLL, LAL, ALA, AAL)
3. Concluir la congruencia y deducir elementos correspondientes

**Ejemplo:** En el triángulo $ABC$, $M$ es punto medio de $BC$. Si $AM$ es mediana y $AB = AC$, demostrar que $\angle AMB = \angle AMC = 90°$.

| Paso | Justificación |
|------|---------------|
| En $\triangle ABM$ y $\triangle ACM$ | |
| $AB = AC$ | Dato (isósceles) |
| $BM = MC$ | $M$ es punto medio |
| $AM = AM$ | Lado común |
| Conclusión | $\triangle ABM \cong \triangle ACM$ (LLL) |
| Por tanto | $\angle AMB = \angle AMC$ y suman 180°, así que cada uno = 90° |

---

## Método 4: Calcular área por descomposición

**Contexto:** Dividir figuras complejas en figuras simples para calcular el área total.

**Pasos:**
1. Identificar las figuras simples que componen la figura
2. Calcular el área de cada figura simple
3. Sumar (o restar si hay huecos) las áreas

**Ejemplo:** Calcular el área de una figura en forma de "L" con dimensiones: base inferior 8 cm × 3 cm, y parte superior 4 cm × 5 cm.

| Figura | Área |
|--------|------|
| Rectángulo inferior | $8 \times 3 = 24$ cm² |
| Rectángulo superior | $4 \times 5 = 20$ cm² |
| **Total** | $24 + 20 = 44$ cm² |

---

## Método 5: Aplicar el teorema de Pitágoras

**Contexto:** Encontrar un lado de un triángulo rectángulo conociendo los otros dos.

**Pasos:**
1. Identificar la hipotenusa (lado opuesto al ángulo recto)
2. Aplicar $c^2 = a^2 + b^2$ o despejar según el caso
3. Calcular la raíz cuadrada

**Ejemplo:** En un triángulo rectángulo, los catetos miden 5 y 12. Encuentra la hipotenusa.

| Paso | Cálculo |
|------|---------|
| Fórmula | $c^2 = 5^2 + 12^2$ |
| Calcular | $c^2 = 25 + 144 = 169$ |
| Resultado | $c = \sqrt{169} = 13$ |

**Verificación:** $(5, 12, 13)$ es una terna pitagórica conocida ✓

---

## Método 6: Usar semejanza para encontrar longitudes

**Contexto:** Cuando dos figuras son semejantes, sus lados correspondientes son proporcionales.

**Pasos:**
1. Verificar que las figuras son semejantes (criterios AA, LAL, LLL)
2. Establecer la proporción entre lados correspondientes
3. Resolver para la incógnita

**Ejemplo:** Dos triángulos semejantes tienen razón 2:3. Si un lado del menor mide 8 cm, ¿cuánto mide el lado correspondiente del mayor?

| Paso | Cálculo |
|------|---------|
| Proporción | $\frac{8}{x} = \frac{2}{3}$ |
| Resolver | $x = \frac{8 \times 3}{2} = 12$ cm |

---

## Método 7: Calcular área usando la fórmula de Herón

**Contexto:** Cuando conocemos los tres lados de un triángulo pero no la altura.

**Pasos:**
1. Calcular el semiperímetro: $s = \frac{a + b + c}{2}$
2. Aplicar: $A = \sqrt{s(s-a)(s-b)(s-c)}$

**Ejemplo:** Triángulo con lados 7, 8 y 9.

| Paso | Cálculo |
|------|---------|
| Semiperímetro | $s = \frac{7 + 8 + 9}{2} = 12$ |
| Fórmula | $A = \sqrt{12 \times 5 \times 4 \times 3}$ |
| Resultado | $A = \sqrt{720} = 12\sqrt{5} \approx 26.83$ |

---

## Método 8: Resolver problemas con ángulos en circunferencia

**Contexto:** Usar las relaciones entre ángulos centrales, inscritos y arcos.

**Pasos:**
1. Identificar el tipo de ángulo (central, inscrito, etc.)
2. Aplicar la relación correspondiente
3. Resolver para la incógnita

**Ejemplo:** Un ángulo inscrito subtiende un arco de 80°. ¿Cuánto mide el ángulo?

| Paso | Cálculo |
|------|---------|
| Relación | Ángulo inscrito = Arco / 2 |
| Resultado | $\alpha = 80° / 2 = 40°$ |

---

## Método 9: Calcular volumen de sólidos compuestos

**Contexto:** Descomponer sólidos complejos en sólidos básicos.

**Pasos:**
1. Identificar los sólidos básicos que componen la figura
2. Calcular el volumen de cada uno
3. Sumar (o restar) según corresponda

**Ejemplo:** Un silo tiene forma de cilindro con tapa hemisférica. Radio = 3 m, altura del cilindro = 10 m.

| Sólido | Volumen |
|--------|---------|
| Cilindro | $\pi (3)^2 (10) = 90\pi$ m³ |
| Hemisferio | $\frac{1}{2} \cdot \frac{4}{3}\pi (3)^3 = 18\pi$ m³ |
| **Total** | $108\pi \approx 339.3$ m³ |

---

## Método 10: Aplicar el teorema de Tales

**Contexto:** Encontrar longitudes en triángulos cortados por rectas paralelas a un lado.

**Pasos:**
1. Verificar que existe una recta paralela a uno de los lados
2. Establecer la proporción de los segmentos
3. Resolver la proporción

**Ejemplo:** En el triángulo $ABC$, $DE \parallel BC$ con $D$ en $AB$ y $E$ en $AC$. Si $AD = 4$, $DB = 6$ y $AE = 5$, encuentra $EC$.

| Paso | Cálculo |
|------|---------|
| Proporción | $\frac{AD}{DB} = \frac{AE}{EC}$ |
| Sustituir | $\frac{4}{6} = \frac{5}{EC}$ |
| Resolver | $EC = \frac{5 \times 6}{4} = 7.5$ |

---

## Método 11: Calcular el apotema de un polígono regular

**Contexto:** El apotema es necesario para calcular el área de polígonos regulares.

**Pasos:**
1. Determinar el número de lados $n$ y la longitud del lado $l$
2. Calcular el ángulo central: $\theta = \frac{360°}{n}$
3. Usar: $a = \frac{l}{2 \tan(\theta/2)}$

**Ejemplo:** Hexágono regular con lado 6 cm.

| Paso | Cálculo |
|------|---------|
| Ángulo central | $\theta = 60°$ |
| Apotema | $a = \frac{6}{2 \tan(30°)} = \frac{6}{2 \cdot \frac{\sqrt{3}}{3}} = 3\sqrt{3}$ cm |

---

## Método 12: Encontrar la generatriz de un cono

**Contexto:** La generatriz relaciona el radio y la altura del cono.

**Pasos:**
1. Identificar radio $r$ y altura $h$
2. Aplicar teorema de Pitágoras: $g = \sqrt{r^2 + h^2}$

**Ejemplo:** Cono con radio 3 cm y altura 4 cm.

| Paso | Cálculo |
|------|---------|
| Fórmula | $g = \sqrt{3^2 + 4^2}$ |
| Resultado | $g = \sqrt{9 + 16} = 5$ cm |
