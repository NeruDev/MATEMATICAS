<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: FUN-03-Prob-87-Solucion
status: stable
audience: student
problem_ref: "[Prob-87]"
methods: ["analisis-signos", "recta-real", "tabla-signos"]
-->

# Solución [Prob-87]: Desigualdad de grado 3 (análisis de signos)

> **Problema:** Resuelve: $(x - 1)(x + 2)(x - 3) > 0$

## Método 1: Análisis de signos con recta real

### Paso 1: Encontrar los puntos críticos (raíces)

Igualamos cada factor a cero:

$$x - 1 = 0 \quad \Rightarrow \quad x = 1$$

$$x + 2 = 0 \quad \Rightarrow \quad x = -2$$

$$x - 3 = 0 \quad \Rightarrow \quad x = 3$$

**Puntos críticos ordenados:** $x = -2, \; 1, \; 3$

### Paso 2: Dividir la recta real en intervalos

Los puntos críticos dividen la recta real en **4 intervalos**:

$$(-\infty, -2), \quad (-2, 1), \quad (1, 3), \quad (3, +\infty)$$

### Paso 3: Determinar el signo del producto en cada intervalo

Elegimos un **punto de prueba** en cada intervalo:

| Intervalo | Punto de prueba | $(x-1)$ | $(x+2)$ | $(x-3)$ | Producto |
|-----------|-----------------|---------|---------|---------|----------|
| $(-\infty, -2)$ | $x = -3$ | $(-)$ | $(-)$ | $(-)$ | $(-)$ |
| $(-2, 1)$ | $x = 0$ | $(-)$ | $(+)$ | $(-)$ | $(+)$ |
| $(1, 3)$ | $x = 2$ | $(+)$ | $(+)$ | $(-)$ | $(-)$ |
| $(3, +\infty)$ | $x = 4$ | $(+)$ | $(+)$ | $(+)$ | $(+)$ |

### Paso 4: Verificar cálculos de signos

**Para $x = -3$:**
$$(-3-1)(-3+2)(-3-3) = (-4)(-1)(-6) = -24 < 0 \quad \checkmark$$

**Para $x = 0$:**
$$(0-1)(0+2)(0-3) = (-1)(2)(-3) = 6 > 0 \quad \checkmark$$

**Para $x = 2$:**
$$(2-1)(2+2)(2-3) = (1)(4)(-1) = -4 < 0 \quad \checkmark$$

**Para $x = 4$:**
$$(4-1)(4+2)(4-3) = (3)(6)(1) = 18 > 0 \quad \checkmark$$

### Paso 5: Seleccionar intervalos donde el producto es positivo

Buscamos $(x - 1)(x + 2)(x - 3) > 0$, es decir, signo $(+)$:

- En $(-2, 1)$: signo $(+)$ ✓
- En $(3, +\infty)$: signo $(+)$ ✓

### Paso 6: Escribir la solución

Como la desigualdad es **estricta** $(> 0)$, no incluimos los puntos críticos:

$$\boxed{x \in (-2, 1) \cup (3, +\infty)}$$

**En notación de desigualdades:**

$$\boxed{-2 < x < 1 \quad \text{o} \quad x > 3}$$

---

## Método 2: Tabla de signos detallada

### Paso 1: Construir tabla de signos

Analizamos el signo de cada factor en cada intervalo:

```
          │  (-∞,-2)  │  (-2,1)  │  (1,3)   │  (3,+∞)
──────────┼───────────┼──────────┼──────────┼──────────
  (x-1)   │     −     │     −    │     +    │     +
──────────┼───────────┼──────────┼──────────┼──────────
  (x+2)   │     −     │     +    │     +    │     +
──────────┼───────────┼──────────┼──────────┼──────────
  (x-3)   │     −     │     −    │     −    │     +
══════════╪═══════════╪══════════╪══════════╪══════════
 Producto │  (−)(−)(−)│  (−)(+)(−)│  (+)(+)(−)│  (+)(+)(+)
          │    = −    │    = +   │    = −   │    = +
```

### Paso 2: Identificar dónde el producto es positivo

El producto es positivo $(+)$ en:
- $(-2, 1)$
- $(3, +\infty)$

### Paso 3: Conclusión

$$x \in (-2, 1) \cup (3, +\infty)$$

---

## Método 3: Regla de los signos alternados

### Paso 1: Observación para polinomios factorizados

Para un producto de factores lineales con coeficientes principales positivos:

$$P(x) = (x - a_1)(x - a_2)(x - a_3) \cdots (x - a_n)$$

donde $a_1 < a_2 < a_3 < \cdots < a_n$:

- El signo **alterna** entre intervalos consecutivos
- A la **derecha** del mayor punto crítico, el signo es $(+)$

### Paso 2: Aplicar al problema

Puntos críticos ordenados: $-2 < 1 < 3$

Comenzando desde la derecha de $x = 3$ (donde el signo es $+$):

```
    (−)      (+)      (−)      (+)
───────●─────────●─────────●─────────→
     -2         1         3
```

### Paso 3: Seleccionar intervalos positivos

$(x - 1)(x + 2)(x - 3) > 0$ en los intervalos con signo $(+)$:

$$x \in (-2, 1) \cup (3, +\infty)$$

---

## Representación gráfica

### Recta numérica con signos

```
        (−)         (+)         (−)         (+)
    ◄───────────○───────────○───────────○───────────►
              -2           1           3
                   │              │
                   └──────────────┴────────────────►
                        Solución: (-2,1) ∪ (3,+∞)
```

### Gráfica de $y = (x-1)(x+2)(x-3)$

```
        y
        │
        │     *
        │    * *              *
        │   *   *            *
   ─────┼──*─────*──────────*───────────► x
      -2│        *         *    3
        │         *       *
        │          *     *
        │           * * *
        │              1
```

El polinomio cruza el eje $x$ en $x = -2, 1, 3$ y es positivo ($y > 0$) en $(-2, 1) \cup (3, +\infty)$.

---

## Verificación

### Verificación de puntos dentro de la solución

**Para $x = 0$ (en $(-2, 1)$):**
$$(0-1)(0+2)(0-3) = (-1)(2)(-3) = 6 > 0 \quad \checkmark$$

**Para $x = 5$ (en $(3, +\infty)$):**
$$(5-1)(5+2)(5-3) = (4)(7)(2) = 56 > 0 \quad \checkmark$$

### Verificación de puntos fuera de la solución

**Para $x = -5$ (en $(-\infty, -2)$):**
$$(-5-1)(-5+2)(-5-3) = (-6)(-3)(-8) = -144 < 0 \quad \checkmark$$

**Para $x = 2$ (en $(1, 3)$):**
$$(2-1)(2+2)(2-3) = (1)(4)(-1) = -4 < 0 \quad \checkmark$$

### Verificación de puntos críticos

Para $x = -2, 1, 3$:
$$(x-1)(x+2)(x-3) = 0 \not> 0$$

Correcto: los puntos críticos **no** están en la solución (desigualdad estricta).

---

## Resumen

| Aspecto | Detalle |
|---------|---------|
| Puntos críticos | $x = -2, 1, 3$ |
| Intervalos donde $P(x) > 0$ | $(-2, 1)$ y $(3, +\infty)$ |
| **Solución** | $\boxed{-2 < x < 1 \;\text{ o }\; x > 3}$ |
| Notación de intervalos | $(-2, 1) \cup (3, +\infty)$ |

---

## Notas adicionales

### Si la desigualdad fuera $\geq 0$

$$\text{Solución: } x \in [-2, 1] \cup [3, +\infty)$$

### Si la desigualdad fuera $< 0$

$$\text{Solución: } x \in (-\infty, -2) \cup (1, 3)$$

### Si la desigualdad fuera $\leq 0$

$$\text{Solución: } x \in (-\infty, -2] \cup [1, 3]$$
