<!--
::METADATA::
type: solution
topic_id: fun-06-geometria-analitica
file_id: FUN-06-Prob-35-Solucion
status: stable
audience: student
problem_ref: "[Prob-35]"
methods: ["condicion-tangencia", "distancia-igual-radio", "analisis-geometrico"]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución [Prob-35]: Rectas tangentes a una circunferencia desde un punto externo

> **Problema:** Encuentra las ecuaciones de las rectas tangentes a la circunferencia $x^2 + y^2 = 9$ desde el punto externo $P(5, 0)$.

## Análisis previo

**Datos de la circunferencia:**
- Centro: $O(0, 0)$
- Radio: $r = 3$

**Verificación de que $P(5, 0)$ es exterior:**
$$d(O, P) = \sqrt{5^2 + 0^2} = 5 > 3 = r \quad \checkmark$$

Desde un punto exterior siempre se pueden trazar **dos rectas tangentes** a la circunferencia.

---

## Método 1: Por condición de tangencia (discriminante = 0)

### Paso 1: Plantear la ecuación de la recta que pasa por $P(5, 0)$

Usando la forma punto-pendiente:
$$y - 0 = m(x - 5)$$
$$y = m(x - 5)$$
$$y = mx - 5m$$

En forma general:
$$mx - y - 5m = 0$$

### Paso 2: Sustituir en la ecuación de la circunferencia

De $y = mx - 5m$, sustituimos en $x^2 + y^2 = 9$:

$$x^2 + (mx - 5m)^2 = 9$$
$$x^2 + m^2x^2 - 10m^2x + 25m^2 = 9$$
$$(1 + m^2)x^2 - 10m^2x + (25m^2 - 9) = 0$$

### Paso 3: Aplicar condición de tangencia

Para que la recta sea [tangente](../../../../glossary.md#tangente), debe tocar la circunferencia en **exactamente un punto**, lo que significa que la ecuación cuadrática tiene **una sola solución**.

**Condición:** Discriminante $= 0$

$$\Delta = b^2 - 4ac = 0$$

Donde:
- $a = 1 + m^2$
- $b = -10m^2$
- $c = 25m^2 - 9$

### Paso 4: Calcular el discriminante

$$\Delta = (-10m^2)^2 - 4(1 + m^2)(25m^2 - 9) = 0$$

$$100m^4 - 4(25m^2 - 9 + 25m^4 - 9m^2) = 0$$

$$100m^4 - 4(25m^4 + 16m^2 - 9) = 0$$

$$100m^4 - 100m^4 - 64m^2 + 36 = 0$$

$$-64m^2 + 36 = 0$$

$$m^2 = \frac{36}{64} = \frac{9}{16}$$

$$m = \pm\frac{3}{4}$$

### Paso 5: Escribir las ecuaciones de las tangentes

**[Tangente](../../../../glossary.md#tangente) 1:** Con $m = \frac{3}{4}$:
$$y = \frac{3}{4}(x - 5)$$
$$y = \frac{3}{4}x - \frac{15}{4}$$
$$4y = 3x - 15$$
$$\boxed{3x - 4y - 15 = 0}$$

**Tangente 2:** Con $m = -\frac{3}{4}$:
$$y = -\frac{3}{4}(x - 5)$$
$$y = -\frac{3}{4}x + \frac{15}{4}$$
$$4y = -3x + 15$$
$$\boxed{3x + 4y - 15 = 0}$$

---

## Método 2: Por distancia del centro a la recta = radio

### Paso 1: Ecuación general de la recta por $P(5, 0)$

$$y - 0 = m(x - 5) \quad \Rightarrow \quad mx - y - 5m = 0$$

### Paso 2: Condición de tangencia por distancia

La distancia del centro $O(0, 0)$ a la recta debe ser igual al radio:

$$d(O, \text{recta}) = r$$

$$\frac{|m(0) - (0) - 5m|}{\sqrt{m^2 + 1}} = 3$$

$$\frac{|-5m|}{\sqrt{m^2 + 1}} = 3$$

$$\frac{5|m|}{\sqrt{m^2 + 1}} = 3$$

### Paso 3: Resolver para $m$

Elevamos al cuadrado:
$$\frac{25m^2}{m^2 + 1} = 9$$

$$25m^2 = 9(m^2 + 1)$$
$$25m^2 = 9m^2 + 9$$
$$16m^2 = 9$$
$$m^2 = \frac{9}{16}$$
$$m = \pm\frac{3}{4}$$

### Paso 4: Ecuaciones de las tangentes

Mismo resultado que el Método 1:
$$\boxed{3x - 4y - 15 = 0} \quad \text{y} \quad \boxed{3x + 4y - 15 = 0}$$

---

## Método 3: Análisis geométrico

### Paso 1: Configuración geométrica

```
                 y
                 │    T₁
                 │   /│
                 │  / │
               3 ┤ /  │ r = 3
                 │/   │
     ────────────●────┼────────● P(5,0)──► x
                O│    │       (punto externo)
                 │\   │
                 │ \  │
                 │  \ │
                 │   \│
                 │    T₂
```

### Paso 2: Triángulo rectángulo $OT_1P$

El radio al punto de tangencia es perpendicular a la tangente.

- $|OP| = 5$ (distancia del centro al punto externo)
- $|OT_1| = 3$ (radio)
- $|PT_1| = ?$ (longitud de la tangente)

Por Pitágoras:
$$|PT_1|^2 + |OT_1|^2 = |OP|^2$$
$$|PT_1|^2 + 9 = 25$$
$$|PT_1| = 4$$

### Paso 3: Encontrar los puntos de tangencia

Sea $T_1 = (x_1, y_1)$ un punto de tangencia.

**Condiciones:**
1. $T_1$ está en la circunferencia: $x_1^2 + y_1^2 = 9$
2. $\overrightarrow{OT_1} \perp \overrightarrow{T_1P}$

El [vector](../../../../glossary.md#vector) $\overrightarrow{OT_1} = (x_1, y_1)$

El [vector](../../../../glossary.md#vector) $\overrightarrow{T_1P} = (5 - x_1, -y_1)$

Para perpendicularidad:
$$\overrightarrow{OT_1} \cdot \overrightarrow{T_1P} = 0$$
$$x_1(5 - x_1) + y_1(-y_1) = 0$$
$$5x_1 - x_1^2 - y_1^2 = 0$$
$$5x_1 - (x_1^2 + y_1^2) = 0$$
$$5x_1 - 9 = 0$$
$$x_1 = \frac{9}{5}$$

### Paso 4: Encontrar $y_1$

De $x_1^2 + y_1^2 = 9$:
$$\left(\frac{9}{5}\right)^2 + y_1^2 = 9$$
$$\frac{81}{25} + y_1^2 = \frac{225}{25}$$
$$y_1^2 = \frac{144}{25}$$
$$y_1 = \pm\frac{12}{5}$$

**Puntos de tangencia:**
$$T_1 = \left(\frac{9}{5}, \frac{12}{5}\right) \quad \text{y} \quad T_2 = \left(\frac{9}{5}, -\frac{12}{5}\right)$$

### Paso 5: Ecuaciones de las rectas $PT_1$ y $PT_2$

**Recta $PT_1$:** Pasa por $P(5, 0)$ y $T_1\left(\frac{9}{5}, \frac{12}{5}\right)$

Pendiente:
$$m_1 = \frac{\frac{12}{5} - 0}{\frac{9}{5} - 5} = \frac{\frac{12}{5}}{-\frac{16}{5}} = -\frac{12}{16} = -\frac{3}{4}$$

Ecuación:
$$y - 0 = -\frac{3}{4}(x - 5)$$
$$4y = -3x + 15$$
$$3x + 4y - 15 = 0$$

**Recta $PT_2$:** Pasa por $P(5, 0)$ y $T_2\left(\frac{9}{5}, -\frac{12}{5}\right)$

Pendiente:
$$m_2 = \frac{-\frac{12}{5} - 0}{\frac{9}{5} - 5} = \frac{-\frac{12}{5}}{-\frac{16}{5}} = \frac{12}{16} = \frac{3}{4}$$

Ecuación:
$$y - 0 = \frac{3}{4}(x - 5)$$
$$4y = 3x - 15$$
$$3x - 4y - 15 = 0$$

---

## Verificación

### Verificar que las rectas pasan por $P(5, 0)$

**Recta $3x - 4y - 15 = 0$:**
$$3(5) - 4(0) - 15 = 15 - 15 = 0 \quad \checkmark$$

**Recta $3x + 4y - 15 = 0$:**
$$3(5) + 4(0) - 15 = 15 - 15 = 0 \quad \checkmark$$

### Verificar la distancia del centro a cada recta

**Distancia a $3x - 4y - 15 = 0$:**
$$d = \frac{|3(0) - 4(0) - 15|}{\sqrt{3^2 + 4^2}} = \frac{15}{5} = 3 = r \quad \checkmark$$

**Distancia a $3x + 4y - 15 = 0$:**
$$d = \frac{|3(0) + 4(0) - 15|}{\sqrt{3^2 + 4^2}} = \frac{15}{5} = 3 = r \quad \checkmark$$

---

## Respuesta final

$$\boxed{3x - 4y - 15 = 0 \quad \text{y} \quad 3x + 4y - 15 = 0}$$

**Equivalentemente:**
$$y = \frac{3}{4}(x - 5) \quad \text{y} \quad y = -\frac{3}{4}(x - 5)$$

---

## Resumen de elementos

| Elemento | Valor |
|:---------|:------|
| Longitud de cada tangente | $4$ |
| Puntos de tangencia | $T_1\left(\frac{9}{5}, \frac{12}{5}\right)$, $T_2\left(\frac{9}{5}, -\frac{12}{5}\right)$ |
| Pendientes | $m = \pm\frac{3}{4}$ |
| Ángulo entre tangentes | $2\arctan\left(\frac{3}{4}\right) \approx 73.74°$ |
