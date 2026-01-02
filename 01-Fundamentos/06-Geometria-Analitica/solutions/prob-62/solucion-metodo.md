<!--
::METADATA::
type: solution
topic_id: fun-06-geometria-analitica
file_id: FUN-06-Prob-62-Solucion
status: stable
audience: student
problem_ref: "[Prob-62]"
methods: ["completar-cuadrado", "identificacion-elementos-hiperbola", "asintotas"]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución [Prob-62]: Hipérbola - Conversión a forma estándar

> **Problema:** Convierte a forma estándar: $4y^2 - x^2 + 8y + 4x + 4 = 0$

## Identificación inicial

Los coeficientes de $x^2$ y $y^2$ tienen **signos opuestos** ($-1$ para $x^2$ y $+4$ para $y^2$), por lo tanto la cónica es una **hipérbola**.

Como el coeficiente de $y^2$ es positivo y el de $x^2$ es negativo, la hipérbola tendrá **eje transverso vertical**.

---

## Método: Completar el cuadrado

### Paso 1: Reordenar y agrupar términos

$$4y^2 + 8y - x^2 + 4x + 4 = 0$$

Movemos la constante al otro lado:
$$4y^2 + 8y - x^2 + 4x = -4$$

### Paso 2: Agrupar por variable

$$4y^2 + 8y - (x^2 - 4x) = -4$$

> **Nota:** Sacamos el signo negativo como factor del grupo de $x$.

### Paso 3: Factorizar los coeficientes cuadráticos

$$4(y^2 + 2y) - (x^2 - 4x) = -4$$

### Paso 4: Completar el cuadrado en $y$

Para $y^2 + 2y$:

1. Tomar la mitad del coeficiente de $y$: $\frac{2}{2} = 1$
2. Elevarlo al cuadrado: $(1)^2 = 1$

$$y^2 + 2y + 1 = (y + 1)^2$$

> **Importante:** Como el factor externo es 4, al añadir 1 dentro del paréntesis, añadimos $4 \times 1 = 4$ al lado izquierdo.

### Paso 5: Completar el cuadrado en $x$

Para $x^2 - 4x$:

1. Tomar la mitad del coeficiente de $x$: $\frac{-4}{2} = -2$
2. Elevarlo al cuadrado: $(-2)^2 = 4$

$$x^2 - 4x + 4 = (x - 2)^2$$

> **Importante:** Como el factor externo es $-1$, al añadir 4 dentro del paréntesis, añadimos $(-1) \times 4 = -4$ al lado izquierdo.

### Paso 6: Escribir la ecuación completada

$$4(y^2 + 2y + 1) - (x^2 - 4x + 4) = -4 + 4 + (-4)$$

$$4(y + 1)^2 - (x - 2)^2 = -4$$

### Paso 7: Dividir para obtener 1 en el lado derecho

Dividimos entre $-4$:

$$\frac{4(y + 1)^2}{-4} - \frac{(x - 2)^2}{-4} = 1$$

$$-\frac{(y + 1)^2}{1} + \frac{(x - 2)^2}{4} = 1$$

Reordenamos:
$$\frac{(x - 2)^2}{4} - \frac{(y + 1)^2}{1} = 1$$

### Paso 8: Forma estándar final

$$\boxed{\frac{(x - 2)^2}{4} - \frac{(y + 1)^2}{1} = 1}$$

**Alternativamente:**
$$\frac{(x - 2)^2}{4} - (y + 1)^2 = 1$$

---

## Identificación de elementos

### Paso 9: Determinar la orientación

La forma estándar de la hipérbola es:
- **Eje transverso horizontal:** $\displaystyle\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1$
- **Eje transverso vertical:** $\displaystyle\frac{(y-k)^2}{a^2} - \frac{(x-h)^2}{b^2} = 1$

Nuestra ecuación $\displaystyle\frac{(x - 2)^2}{4} - \frac{(y + 1)^2}{1} = 1$ tiene el término positivo en $x$, por lo tanto:

**El eje transverso es HORIZONTAL.**

### Paso 10: Extraer los parámetros

Comparando con $\displaystyle\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1$:

- $h = 2$, $k = -1$ → **Centro:** $(2, -1)$
- $a^2 = 4$ → $a = 2$ (semieje transverso)
- $b^2 = 1$ → $b = 1$ (semieje conjugado)

### Paso 11: Calcular la distancia focal $c$

Para la hipérbola: $c^2 = a^2 + b^2$

$$c^2 = 4 + 1 = 5$$
$$c = \sqrt{5}$$

### Paso 12: Calcular la excentricidad

$$e = \frac{c}{a} = \frac{\sqrt{5}}{2} \approx 1.118$$

> **Nota:** $e > 1$ confirma que es una hipérbola.

---

## Elementos de la hipérbola

### Centro
$$C(h, k) = \boxed{(2, -1)}$$

### Vértices (sobre el eje transverso)

Los vértices están a distancia $a = 2$ del centro, en dirección horizontal:

$$V_1 = (h + a, k) = (2 + 2, -1) = \boxed{(4, -1)}$$
$$V_2 = (h - a, k) = (2 - 2, -1) = \boxed{(0, -1)}$$

### Focos

Los focos están a distancia $c = \sqrt{5}$ del centro, sobre el eje transverso:

$$F_1 = (h + c, k) = (2 + \sqrt{5}, -1) = \boxed{(2 + \sqrt{5}, -1)}$$
$$F_2 = (h - c, k) = (2 - \sqrt{5}, -1) = \boxed{(2 - \sqrt{5}, -1)}$$

**Aproximación decimal:**
- $F_1 \approx (4.236, -1)$
- $F_2 \approx (-0.236, -1)$

### Covértices (extremos del eje conjugado)

Los covértices están a distancia $b = 1$ del centro, en dirección vertical:

$$B_1 = (h, k + b) = (2, -1 + 1) = \boxed{(2, 0)}$$
$$B_2 = (h, k - b) = (2, -1 - 1) = \boxed{(2, -2)}$$

---

## Asíntotas

### Paso 13: Ecuaciones de las asíntotas

Para una hipérbola con eje transverso horizontal y centro $(h, k)$:

$$y - k = \pm\frac{b}{a}(x - h)$$

Sustituyendo $h = 2$, $k = -1$, $a = 2$, $b = 1$:

$$y - (-1) = \pm\frac{1}{2}(x - 2)$$

$$y + 1 = \pm\frac{1}{2}(x - 2)$$

**[Asíntota](../../../..](../../../../glossary.md)#asintota) 1:**
$$y + 1 = \frac{1}{2}(x - 2)$$
$$y = \frac{1}{2}x - 1 - 1$$
$$\boxed{y = \frac{1}{2}x - 2}$$

En forma general: $x - 2y - 4 = 0$

**[Asíntota](../../../..](../../../../glossary.md)#asintota) 2:**
$$y + 1 = -\frac{1}{2}(x - 2)$$
$$y = -\frac{1}{2}x + 1 - 1$$
$$\boxed{y = -\frac{1}{2}x}$$

En forma general: $x + 2y = 0$

### Observación sobre las asíntotas

Las asíntotas pasan por el centro $(2, -1)$ y tienen pendientes $m = \pm\frac{1}{2}$.

**Verificación:** En $x = 2$:
- Asíntota 1: $y = \frac{1}{2}(2) - 2 = -1$ ✓
- Asíntota 2: $y = -\frac{1}{2}(2) = -1$ ✓

Ambas pasan por $(2, -1)$.

---

## Elementos adicionales

### Lado recto (latus rectum)

$$LR = \frac{2b^2}{a} = \frac{2(1)}{2} = \boxed{1}$$

### Longitudes de los ejes

- **Eje transverso:** $2a = 2(2) = \boxed{4}$
- **Eje conjugado:** $2b = 2(1) = \boxed{2}$

### Distancia entre focos

$$2c = 2\sqrt{5} \approx 4.472$$

---

## Resumen de resultados

| Elemento | Valor |
|:---------|:------|
| **Ecuación estándar** | $\displaystyle\frac{(x-2)^2}{4} - \frac{(y+1)^2}{1} = 1$ |
| **Centro** | $(2, -1)$ |
| **Orientación** | Eje transverso horizontal |
| **Semieje transverso** | $a = 2$ |
| **Semieje conjugado** | $b = 1$ |
| **Distancia focal** | $c = \sqrt{5} \approx 2.236$ |
| **Excentricidad** | $e = \frac{\sqrt{5}}{2} \approx 1.118$ |
| **Vértices** | $(4, -1)$ y $(0, -1)$ |
| **Focos** | $(2 \pm \sqrt{5}, -1)$ |
| **Covértices** | $(2, 0)$ y $(2, -2)$ |
| **Asíntotas** | $y = \frac{1}{2}x - 2$ y $y = -\frac{1}{2}x$ |
| **Lado recto** | $1$ |

---

## Diagrama

```
           y│       
            │      /
            │     /  Asíntota: y = ½x - 2
          0 ●────/───B₁(2,0)
            │   /  / \
            │  /  /   \
   ─────────●─/──●─────●──────────────► x
         V₂(0,-1)C(2,-1) V₁(4,-1)
            │  \      /
            │   \    /
         -2 ●────\──/ B₂(2,-2)
            │     \/
            │      \  Asíntota: y = -½x
            │
```

---

## Verificación

### Verificar el vértice $(4, -1)$ en la ecuación original

En $4y^2 - x^2 + 8y + 4x + 4 = 0$:

$$4(-1)^2 - (4)^2 + 8(-1) + 4(4) + 4$$
$$= 4(1) - 16 - 8 + 16 + 4$$
$$= 4 - 16 - 8 + 16 + 4 = 0 \quad \checkmark$$

### Verificar el vértice $(0, -1)$

$$4(-1)^2 - (0)^2 + 8(-1) + 4(0) + 4$$
$$= 4 - 0 - 8 + 0 + 4 = 0 \quad \checkmark$$

### Verificar el covértice $(2, 0)$

$$4(0)^2 - (2)^2 + 8(0) + 4(2) + 4$$
$$= 0 - 4 + 0 + 8 + 4 = 8 \neq 0$$

> **Nota:** Los covértices **no** pertenecen a la hipérbola (son puntos auxiliares del rectángulo fundamental). Esto es correcto.

### Verificar que las asíntotas no intersectan la hipérbola

Sustituyendo $y = \frac{1}{2}x - 2$ en la ecuación estándar:

$$\frac{(x-2)^2}{4} - \left(\frac{1}{2}x - 2 + 1\right)^2 = 1$$

$$\frac{(x-2)^2}{4} - \left(\frac{1}{2}x - 1\right)^2 = 1$$

$$\frac{(x-2)^2}{4} - \frac{(x-2)^2}{4} = 1$$

$$0 = 1 \quad \text{(Contradicción)}$$

Esto confirma que las asíntotas nunca tocan la hipérbola. ✓
