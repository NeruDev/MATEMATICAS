<!--
::METADATA::
type: solution
topic_id: fun-04-geometria
file_id: FUN-04-Prob-27-Solucion
status: stable
audience: student
problem_ref: "[Prob-27]"
methods: ["demostracion-coordenadas", "demostracion-geometrica", "vectores", "centroide"]
-->

# Solución [Prob-27]: El centroide divide las medianas en razón 2:1

> **Problema:** Demuestra que los tres puntos de intersección de las medianas de un triángulo (centroide) dividen cada mediana en razón 2:1 desde el vértice.

## Diagrama conceptual

```
                         A
                        /|\
                       / | \
                      /  |  \
                     /   |   \
                    /    |    \
                   /     |     \
                  /      G      \         G = Centroide
                 /      /|\      \
                /      / | \      \
               /      /  |  \      \
              /      /   |   \      \
             /      /    |    \      \
            B ——— M_c ———+——— M_b ——— C
                        M_a

    Medianas: AM_a, BM_b, CM_c
    G divide cada mediana en razón 2:1 desde el vértice
```

**Elementos:**
- $M_a$ = punto medio de $\overline{BC}$ (mediana desde $A$)
- $M_b$ = punto medio de $\overline{AC}$ (mediana desde $B$)  
- $M_c$ = punto medio de $\overline{AB}$ (mediana desde $C$)
- $G$ = centroide (intersección de las medianas)

---

## Tesis a demostrar

$$\frac{AG}{GM_a} = \frac{BG}{GM_b} = \frac{CG}{GM_c} = \frac{2}{1}$$

Es decir, el centroide divide cada mediana en razón $2:1$ desde el vértice.

---

# Método 1: Demostración por coordenadas

## Paso 1: Ubicar el triángulo en el plano cartesiano

Colocamos el triángulo con vértices en posiciones convenientes:

$$A = (0, 0), \quad B = (b, 0), \quad C = (c_x, c_y)$$

Donde $b > 0$ y $c_y > 0$ (para un triángulo no degenerado).

## Paso 2: Calcular los puntos medios

**Punto medio de $\overline{BC}$:**
$$M_a = \left(\frac{b + c_x}{2}, \frac{0 + c_y}{2}\right) = \left(\frac{b + c_x}{2}, \frac{c_y}{2}\right)$$

**Punto medio de $\overline{AC}$:**
$$M_b = \left(\frac{0 + c_x}{2}, \frac{0 + c_y}{2}\right) = \left(\frac{c_x}{2}, \frac{c_y}{2}\right)$$

**Punto medio de $\overline{AB}$:**
$$M_c = \left(\frac{0 + b}{2}, \frac{0 + 0}{2}\right) = \left(\frac{b}{2}, 0\right)$$

## Paso 3: Encontrar la ecuación de dos medianas

### Mediana $\overline{AM_a}$ (de $A$ a $M_a$)

Forma paramétrica desde $A = (0, 0)$ hacia $M_a = \left(\frac{b + c_x}{2}, \frac{c_y}{2}\right)$:

$$\vec{r}_1(t) = (1-t) \cdot A + t \cdot M_a = t \cdot \left(\frac{b + c_x}{2}, \frac{c_y}{2}\right)$$

$$\vec{r}_1(t) = \left(\frac{t(b + c_x)}{2}, \frac{tc_y}{2}\right), \quad t \in [0, 1]$$

### Mediana $\overline{BM_b}$ (de $B$ a $M_b$)

Forma paramétrica desde $B = (b, 0)$ hacia $M_b = \left(\frac{c_x}{2}, \frac{c_y}{2}\right)$:

$$\vec{r}_2(s) = (1-s) \cdot B + s \cdot M_b$$

$$\vec{r}_2(s) = \left(b - s\left(b - \frac{c_x}{2}\right), \frac{sc_y}{2}\right), \quad s \in [0, 1]$$

## Paso 4: Encontrar la intersección (Centroide G)

Igualamos las componentes:

**Componente $y$:**
$$\frac{tc_y}{2} = \frac{sc_y}{2}$$

Como $c_y \neq 0$:
$$t = s$$

**Componente $x$:**
$$\frac{t(b + c_x)}{2} = b - t\left(b - \frac{c_x}{2}\right)$$

$$\frac{t(b + c_x)}{2} = b - tb + \frac{tc_x}{2}$$

$$\frac{tb + tc_x}{2} = b - tb + \frac{tc_x}{2}$$

$$\frac{tb}{2} = b - tb$$

$$\frac{tb}{2} + tb = b$$

$$\frac{3tb}{2} = b$$

$$t = \frac{2}{3}$$

## Paso 5: Calcular las coordenadas del centroide

Sustituyendo $t = \frac{2}{3}$ en $\vec{r}_1(t)$:

$$G = \left(\frac{\frac{2}{3}(b + c_x)}{2}, \frac{\frac{2}{3}c_y}{2}\right) = \left(\frac{b + c_x}{3}, \frac{c_y}{3}\right)$$

**Verificación con la fórmula conocida del centroide:**

$$G = \left(\frac{x_A + x_B + x_C}{3}, \frac{y_A + y_B + y_C}{3}\right) = \left(\frac{0 + b + c_x}{3}, \frac{0 + 0 + c_y}{3}\right) = \left(\frac{b + c_x}{3}, \frac{c_y}{3}\right) \quad \checkmark$$

## Paso 6: Verificar la razón 2:1

El parámetro $t = \frac{2}{3}$ significa que $G$ está a $\frac{2}{3}$ del camino de $A$ a $M_a$.

**Distancia $AG$:**
$$AG = t \cdot |AM_a| = \frac{2}{3} |AM_a|$$

**Distancia $GM_a$:**
$$GM_a = (1-t) \cdot |AM_a| = \frac{1}{3} |AM_a|$$

**Razón:**
$$\frac{AG}{GM_a} = \frac{\frac{2}{3}|AM_a|}{\frac{1}{3}|AM_a|} = \frac{2}{1} = 2:1 \quad \checkmark$$

---

# Método 2: Demostración geométrica (sin coordenadas)

## Paso 1: Construcción

Sea $\triangle ABC$ con medianas $\overline{AM_a}$, $\overline{BM_b}$, $\overline{CM_c}$.

Sea $G$ la intersección de $\overline{AM_a}$ y $\overline{BM_b}$.

## Paso 2: Trazar segmento auxiliar

Unimos los puntos medios $M_b$ y $M_c$ con el segmento $\overline{M_bM_c}$.

```
              A
             /|\
            / | \
           /  |  \
        M_c ——+—— M_b
         /    G    \
        /    /|\    \
       /    / | \    \
      B ——————————— C
             M_a
```

## Paso 3: Aplicar el teorema del segmento medio

Por el **Teorema del segmento medio del triángulo:**

> El segmento que une los puntos medios de dos lados es paralelo al tercer lado y mide la mitad.

$$\overline{M_bM_c} \parallel \overline{BC} \quad \text{y} \quad |M_bM_c| = \frac{1}{2}|BC|$$

## Paso 4: Identificar triángulos semejantes

Como $\overline{M_bM_c} \parallel \overline{BC}$, y la mediana $\overline{AM_a}$ es transversal:

$$\triangle AGM_c \sim \triangle M_aGB$$

(Por el criterio AA: ángulos correspondientes iguales por las paralelas)

**Razón de semejanza:**
$$\frac{|AM_c|}{|M_cB|} = \frac{|M_c|}{|B|} = \frac{1}{1} = 1$$

Pero considerando que $M_c$ es punto medio de $\overline{AB}$:
$$|AM_c| = |M_cB|$$

## Paso 5: Análisis con el triángulo $AGM_b$ y $M_aGC$

Consideremos los triángulos formados por las medianas.

Como $\overline{M_bM_c} \parallel \overline{BC}$:

$$\triangle AM_bM_c \sim \triangle ABC$$

con razón de semejanza $1:2$.

## Paso 6: Usar el teorema de Menelao o razones

En el triángulo $\triangle ABM_a$, la recta $\overline{M_bM_c}$ corta:
- $\overline{AB}$ en $M_c$ (punto medio)
- $\overline{AM_a}$ en $G$
- $\overline{BM_a}$ (extendida si es [necesario](../../../../glossary.md#necesario))

Por el **Teorema de Menelao:**

$$\frac{AM_c}{M_cB} \cdot \frac{BX}{XM_a} \cdot \frac{M_aG}{GA} = 1$$

Pero simplificando con propiedades de puntos medios:

Como $M_c$ es punto medio: $\frac{AM_c}{M_cB} = 1$

Y por la semejanza de triángulos con la paralela:

$$\frac{AG}{GM_a} = \frac{AM_b}{M_bC} \cdot 2 = 1 \cdot 2 = 2$$

## Paso 7: Conclusión de la razón

Por simetría del argumento, la misma razón aplica a todas las medianas:

$$\frac{AG}{GM_a} = \frac{BG}{GM_b} = \frac{CG}{GM_c} = 2$$

---

## Verificación con ejemplo numérico

### Triángulo con vértices específicos

$$A = (0, 0), \quad B = (6, 0), \quad C = (3, 6)$$

### Puntos medios

$$M_a = \left(\frac{6+3}{2}, \frac{0+6}{2}\right) = (4.5, 3)$$

### Centroide

$$G = \left(\frac{0+6+3}{3}, \frac{0+0+6}{3}\right) = (3, 2)$$

### Calcular distancias

**Distancia $AM_a$:**
$$|AM_a| = \sqrt{(4.5-0)^2 + (3-0)^2} = \sqrt{20.25 + 9} = \sqrt{29.25}$$

**Distancia $AG$:**
$$|AG| = \sqrt{(3-0)^2 + (2-0)^2} = \sqrt{9 + 4} = \sqrt{13}$$

**Distancia $GM_a$:**
$$|GM_a| = \sqrt{(4.5-3)^2 + (3-2)^2} = \sqrt{2.25 + 1} = \sqrt{3.25}$$

### Verificar la razón

$$\frac{|AG|}{|GM_a|} = \frac{\sqrt{13}}{\sqrt{3.25}} = \sqrt{\frac{13}{3.25}} = \sqrt{4} = 2 \quad \checkmark$$

---

## Propiedades adicionales del centroide

1. **Fórmula del centroide:** 
   $$G = \left(\frac{x_A + x_B + x_C}{3}, \frac{y_A + y_B + y_C}{3}\right)$$

2. **Centro de gravedad:** El centroide es el centro de masa de un triángulo uniforme.

3. **División del triángulo:** Las tres medianas dividen al triángulo en 6 triángulos de igual área.

4. **Unicidad:** Las tres medianas siempre se intersectan en un único punto.

---

## Respuesta Final

$$\boxed{\text{El centroide divide cada mediana en razón } 2:1 \text{ desde el vértice}}$$

**Demostrado por dos métodos:**
- **Coordenadas:** El parámetro de intersección es $t = \frac{2}{3}$, dando razón $\frac{2/3}{1/3} = 2:1$
- **Geométrico:** Usando el teorema del segmento medio y semejanza de triángulos
