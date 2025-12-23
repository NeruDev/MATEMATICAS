<!--
::METADATA::
type: solution
topic_id: fun-06-geometria-analitica
file_id: FUN-06-Prob-34-Solucion
status: stable
audience: student
problem_ref: "[Prob-34]"
methods: ["sistema-ecuaciones-3x3", "completar-cuadrado", "verificacion"]
-->

# Solución [Prob-34]: Circunferencia que pasa por tres puntos

> **Problema:** Encuentra la ecuación de la circunferencia que pasa por los puntos $A(1, 0)$, $B(5, 0)$ y $C(3, 4)$.

## Estrategia de solución

Usaremos la ecuación general de la circunferencia:
$$x^2 + y^2 + Dx + Ey + F = 0$$

Sustituiremos las coordenadas de los tres puntos para obtener un sistema de 3 ecuaciones con 3 incógnitas ($D$, $E$, $F$).

---

## Método: Sistema de ecuaciones lineales

### Paso 1: Plantear la ecuación general

La ecuación general de la circunferencia es:
$$x^2 + y^2 + Dx + Ey + F = 0$$

Donde:
- Centro: $\left(-\frac{D}{2}, -\frac{E}{2}\right)$
- Radio: $r = \frac{1}{2}\sqrt{D^2 + E^2 - 4F}$

### Paso 2: Sustituir el punto $A(1, 0)$

$$1^2 + 0^2 + D(1) + E(0) + F = 0$$
$$1 + D + F = 0$$

**Ecuación (1):** $D + F = -1$

### Paso 3: Sustituir el punto $B(5, 0)$

$$5^2 + 0^2 + D(5) + E(0) + F = 0$$
$$25 + 5D + F = 0$$

**Ecuación (2):** $5D + F = -25$

### Paso 4: Sustituir el punto $C(3, 4)$

$$3^2 + 4^2 + D(3) + E(4) + F = 0$$
$$9 + 16 + 3D + 4E + F = 0$$
$$25 + 3D + 4E + F = 0$$

**Ecuación (3):** $3D + 4E + F = -25$

### Paso 5: Resolver el sistema de ecuaciones

El sistema es:
$$\begin{cases}
D + F = -1 & \text{(1)} \\
5D + F = -25 & \text{(2)} \\
3D + 4E + F = -25 & \text{(3)}
\end{cases}$$

**Paso 5a: Encontrar $D$**

Restamos (1) de (2):
$$(5D + F) - (D + F) = -25 - (-1)$$
$$4D = -24$$
$$D = -6$$

**Paso 5b: Encontrar $F$**

Sustituimos $D = -6$ en (1):
$$-6 + F = -1$$
$$F = 5$$

**Paso 5c: Encontrar $E$**

Sustituimos $D = -6$ y $F = 5$ en (3):
$$3(-6) + 4E + 5 = -25$$
$$-18 + 4E + 5 = -25$$
$$4E - 13 = -25$$
$$4E = -12$$
$$E = -3$$

### Paso 6: Escribir la ecuación general

Con $D = -6$, $E = -3$, $F = 5$:

$$\boxed{x^2 + y^2 - 6x - 3y + 5 = 0}$$

---

## Conversión a forma estándar (Completar cuadrado)

### Paso 7: Agrupar términos

$$x^2 - 6x + y^2 - 3y = -5$$

### Paso 8: Completar el cuadrado en $x$

$$x^2 - 6x$$

Tomamos la mitad del coeficiente de $x$: $\frac{-6}{2} = -3$

Lo elevamos al cuadrado: $(-3)^2 = 9$

$$x^2 - 6x + 9 = (x - 3)^2$$

### Paso 9: Completar el cuadrado en $y$

$$y^2 - 3y$$

Tomamos la mitad del coeficiente de $y$: $\frac{-3}{2}$

Lo elevamos al cuadrado: $\left(\frac{-3}{2}\right)^2 = \frac{9}{4}$

$$y^2 - 3y + \frac{9}{4} = \left(y - \frac{3}{2}\right)^2$$

### Paso 10: Completar la ecuación

Sumamos lo que añadimos a ambos lados:
$$x^2 - 6x + 9 + y^2 - 3y + \frac{9}{4} = -5 + 9 + \frac{9}{4}$$

$$(x - 3)^2 + \left(y - \frac{3}{2}\right)^2 = 4 + \frac{9}{4}$$

$$(x - 3)^2 + \left(y - \frac{3}{2}\right)^2 = \frac{16}{4} + \frac{9}{4}$$

$$(x - 3)^2 + \left(y - \frac{3}{2}\right)^2 = \frac{25}{4}$$

### Paso 11: Identificar centro y radio

**Forma estándar:**
$$\boxed{(x - 3)^2 + \left(y - \frac{3}{2}\right)^2 = \frac{25}{4}}$$

- **Centro:** $C\left(3, \frac{3}{2}\right)$
- **Radio:** $r = \frac{5}{2}$

---

## Verificación de los tres puntos

### Verificación del punto $A(1, 0)$

$$(1 - 3)^2 + \left(0 - \frac{3}{2}\right)^2 = (-2)^2 + \left(-\frac{3}{2}\right)^2$$
$$= 4 + \frac{9}{4} = \frac{16}{4} + \frac{9}{4} = \frac{25}{4} \quad \checkmark$$

### Verificación del punto $B(5, 0)$

$$(5 - 3)^2 + \left(0 - \frac{3}{2}\right)^2 = (2)^2 + \left(-\frac{3}{2}\right)^2$$
$$= 4 + \frac{9}{4} = \frac{16}{4} + \frac{9}{4} = \frac{25}{4} \quad \checkmark$$

### Verificación del punto $C(3, 4)$

$$(3 - 3)^2 + \left(4 - \frac{3}{2}\right)^2 = (0)^2 + \left(\frac{5}{2}\right)^2$$
$$= 0 + \frac{25}{4} = \frac{25}{4} \quad \checkmark$$

---

## Resumen de resultados

| Elemento | Valor |
|:---------|:------|
| Ecuación general | $x^2 + y^2 - 6x - 3y + 5 = 0$ |
| Ecuación estándar | $(x - 3)^2 + \left(y - \frac{3}{2}\right)^2 = \frac{25}{4}$ |
| Centro | $\left(3, \frac{3}{2}\right)$ |
| Radio | $\frac{5}{2} = 2.5$ |

---

## Diagrama

```
      y
      │
    4 ┤       ● C(3,4)
      │      /│\
    3 ┤     / │ \
      │    /  │  \
  3/2 ┤   /   ●Centro(3, 3/2)
      │  /    │   \
    1 ┤ /     │    \
      │/      │     \
    0 ●───────┼──────● B(5,0)
      A(1,0)  │     
   ───┼───┬───┬───┬───┬───► x
      0   1   2   3   4   5
```

**Observación geométrica:** Los puntos $A$ y $B$ están sobre el eje $x$ (simétricos respecto a $x = 3$), lo cual implica que el centro tiene coordenada $x = 3$.
