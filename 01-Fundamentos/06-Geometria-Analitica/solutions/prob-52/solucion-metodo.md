<!--
::METADATA::
type: solution
topic_id: fun-06-geometria-analitica
file_id: FUN-06-Prob-52-Solucion
status: stable
audience: student
problem_ref: "[Prob-52]"
methods: ["completar-cuadrado", "identificacion-elementos-elipse", "excentricidad"]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución [Prob-52]: Elipse - Conversión a forma estándar

> **Problema:** Convierte a forma estándar: $4x^2 + 9y^2 - 16x + 18y - 11 = 0$

## Identificación inicial

Los coeficientes de $x^2$ y $y^2$ son **positivos y diferentes** ($4 \neq 9$), por lo tanto la cónica es una **elipse**.

---

## Método: Completar el cuadrado

### Paso 1: Agrupar términos por variable

$$4x^2 - 16x + 9y^2 + 18y = 11$$

### Paso 2: Factorizar los coeficientes cuadráticos

$$4(x^2 - 4x) + 9(y^2 + 2y) = 11$$

### Paso 3: Completar el cuadrado en $x$

Para $x^2 - 4x$:

1. Tomar la mitad del coeficiente de $x$: $\frac{-4}{2} = -2$
2. Elevarlo al cuadrado: $(-2)^2 = 4$
3. Sumar y restar 4 dentro del paréntesis

$$x^2 - 4x + 4 = (x - 2)^2$$

> **Importante:** Como el factor es 4, al añadir 4 dentro del paréntesis, realmente añadimos $4 \times 4 = 16$ al lado izquierdo.

### Paso 4: Completar el cuadrado en $y$

Para $y^2 + 2y$:

1. Tomar la mitad del coeficiente de $y$: $\frac{2}{2} = 1$
2. Elevarlo al cuadrado: $(1)^2 = 1$
3. Sumar y restar 1 dentro del paréntesis

$$y^2 + 2y + 1 = (y + 1)^2$$

> **Importante:** Como el factor es 9, al añadir 1 dentro del paréntesis, realmente añadimos $9 \times 1 = 9$ al lado izquierdo.

### Paso 5: Escribir la ecuación completada

$$4(x^2 - 4x + 4) + 9(y^2 + 2y + 1) = 11 + 16 + 9$$

$$4(x - 2)^2 + 9(y + 1)^2 = 36$$

### Paso 6: Dividir entre 36 para obtener 1 en el lado derecho

$$\frac{4(x - 2)^2}{36} + \frac{9(y + 1)^2}{36} = 1$$

$$\frac{(x - 2)^2}{9} + \frac{(y + 1)^2}{4} = 1$$

### Paso 7: Forma estándar final

$$\boxed{\frac{(x - 2)^2}{9} + \frac{(y + 1)^2}{4} = 1}$$

---

## Identificación de elementos

### Paso 8: Extraer los parámetros

Comparando con la forma estándar de la elipse con centro $(h, k)$:
$$\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1 \quad (a > b)$$

Identificamos:
- $h = 2$, $k = -1$ → **Centro:** $(2, -1)$
- El denominador mayor está bajo $(x-2)^2$: $a^2 = 9$ → $a = 3$
- El denominador [menor](../../../../glossary.md#menor): $b^2 = 4$ → $b = 2$

Como $a^2 = 9$ está asociado a $x$, el **eje mayor es horizontal**.

### Paso 9: Calcular la distancia focal $c$

Para la elipse: $c^2 = a^2 - b^2$

$$c^2 = 9 - 4 = 5$$
$$c = \sqrt{5}$$

### Paso 10: Calcular la excentricidad

$$e = \frac{c}{a} = \frac{\sqrt{5}}{3} \approx 0.745$$

> **Nota:** $0 < e < 1$ confirma que es una elipse.

---

## Elementos de la elipse

### Centro
$$C(h, k) = \boxed{(2, -1)}$$

### Vértices (sobre el eje mayor)

Los vértices están a distancia $a = 3$ del centro, en dirección horizontal:

$$V_1 = (h + a, k) = (2 + 3, -1) = \boxed{(5, -1)}$$
$$V_2 = (h - a, k) = (2 - 3, -1) = \boxed{(-1, -1)}$$

### Covértices (sobre el eje menor)

Los covértices están a distancia $b = 2$ del centro, en dirección vertical:

$$B_1 = (h, k + b) = (2, -1 + 2) = \boxed{(2, 1)}$$
$$B_2 = (h, k - b) = (2, -1 - 2) = \boxed{(2, -3)}$$

### Focos

Los focos están a distancia $c = \sqrt{5}$ del centro, sobre el eje mayor (horizontal):

$$F_1 = (h + c, k) = (2 + \sqrt{5}, -1) = \boxed{(2 + \sqrt{5}, -1)}$$
$$F_2 = (h - c, k) = (2 - \sqrt{5}, -1) = \boxed{(2 - \sqrt{5}, -1)}$$

**Aproximación decimal:**
- $F_1 \approx (4.236, -1)$
- $F_2 \approx (-0.236, -1)$

### Longitud de los ejes

- **Eje mayor:** $2a = 2(3) = \boxed{6}$
- **Eje [menor](../../../../glossary.md#menor):** $2b = 2(2) = \boxed{4}$

### Lado recto (latus rectum)

$$LR = \frac{2b^2}{a} = \frac{2(4)}{3} = \boxed{\frac{8}{3}}$$

---

## Resumen de resultados

| Elemento | Valor |
|:---------|:------|
| **Ecuación estándar** | $\displaystyle\frac{(x-2)^2}{9} + \frac{(y+1)^2}{4} = 1$ |
| **Centro** | $(2, -1)$ |
| **Semieje mayor** | $a = 3$ |
| **Semieje menor** | $b = 2$ |
| **Distancia focal** | $c = \sqrt{5} \approx 2.236$ |
| **Excentricidad** | $e = \frac{\sqrt{5}}{3} \approx 0.745$ |
| **Orientación** | Eje mayor horizontal |
| **Vértices** | $(5, -1)$ y $(-1, -1)$ |
| **Covértices** | $(2, 1)$ y $(2, -3)$ |
| **Focos** | $(2 \pm \sqrt{5}, -1)$ |
| **Longitud eje mayor** | $6$ |
| **Longitud eje menor** | $4$ |
| **Lado recto** | $\frac{8}{3}$ |

---

## Diagrama

```
           y
           │
         1 ┤         ● B₁(2,1)
           │        /│\
           │       / │ \
           │      /  │  \
   ────●───┼─────●───●───●─────●────► x
    V₂(-1,-1)  F₂  C(2,-1)  F₁  V₁(5,-1)
           │      \  │  /
           │       \ │ /
        -3 ┤        \│/
           │         ● B₂(2,-3)
           │
```

---

## Verificación

### Verificar el centro $(2, -1)$ en la ecuación original

El centro $(2, -1)$ **no** satisface la ecuación original (los centros de las cónicas no pertenecen a la curva).

### Verificar el vértice $(5, -1)$

En la ecuación original $4x^2 + 9y^2 - 16x + 18y - 11 = 0$:

$$4(5)^2 + 9(-1)^2 - 16(5) + 18(-1) - 11$$
$$= 4(25) + 9(1) - 80 - 18 - 11$$
$$= 100 + 9 - 80 - 18 - 11$$
$$= 109 - 109 = 0 \quad \checkmark$$

### Verificar el covértice $(2, 1)$

$$4(2)^2 + 9(1)^2 - 16(2) + 18(1) - 11$$
$$= 16 + 9 - 32 + 18 - 11$$
$$= 43 - 43 = 0 \quad \checkmark$$
