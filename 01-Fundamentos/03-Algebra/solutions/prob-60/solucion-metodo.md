<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: FUN-03-Prob-60-Solucion
status: stable
audience: student
problem_ref: "[Prob-60]"
methods: ["valores-absolutos", "casos-por-signo", "ecuaciones-equivalentes"]
-->

# Solución [Prob-60]: Ecuación con dos valores absolutos

> **Problema:** Resuelve: $|3x + 1| = |x - 5|$

## Estrategia de solución

Cuando tenemos una ecuación de la forma $|A| = |B|$, se cumple si y solo si:

$$A = B \quad \text{o} \quad A = -B$$

Esto se debe a que dos números tienen el mismo valor absoluto si son iguales o si son opuestos.

---

## Método 1: Propiedad de valores absolutos iguales

### Paso 1: Establecer los dos casos

Dado que $|3x + 1| = |x - 5|$, entonces:

**Caso 1:** $3x + 1 = x - 5$

**Caso 2:** $3x + 1 = -(x - 5)$

### Paso 2: Resolver el Caso 1

$$3x + 1 = x - 5$$

Restamos $x$ de ambos lados:

$$3x - x + 1 = -5$$

$$2x + 1 = -5$$

Restamos 1 de ambos lados:

$$2x = -6$$

Dividimos entre 2:

$$x = -3$$

### Paso 3: Resolver el Caso 2

$$3x + 1 = -(x - 5)$$

Distribuimos el signo negativo:

$$3x + 1 = -x + 5$$

Sumamos $x$ a ambos lados:

$$3x + x + 1 = 5$$

$$4x + 1 = 5$$

Restamos 1 de ambos lados:

$$4x = 4$$

Dividimos entre 4:

$$x = 1$$

### Paso 4: Verificar ambas soluciones

**Verificación de $x = -3$:**

$$|3(-3) + 1| = |(-3) - 5|$$

$$|-9 + 1| = |-8|$$

$$|-8| = |-8|$$

$$8 = 8 \quad \checkmark$$

**Verificación de $x = 1$:**

$$|3(1) + 1| = |(1) - 5|$$

$$|3 + 1| = |-4|$$

$$|4| = |-4|$$

$$4 = 4 \quad \checkmark$$

---

## Método 2: Análisis por intervalos (regiones críticas)

### Paso 1: Encontrar los puntos críticos

Los valores absolutos cambian de comportamiento cuando su argumento es cero:

- $3x + 1 = 0 \Rightarrow x = -\frac{1}{3}$
- $x - 5 = 0 \Rightarrow x = 5$

Estos puntos dividen la recta real en tres regiones:

```
         -1/3            5
    ──────┼─────────────┼──────▶ x
   Región I   Región II   Región III
```

### Paso 2: Analizar Región I: $x < -\frac{1}{3}$

En esta región:
- $3x + 1 < 0 \Rightarrow |3x + 1| = -(3x + 1)$
- $x - 5 < 0 \Rightarrow |x - 5| = -(x - 5)$

La ecuación se convierte en:

$$-(3x + 1) = -(x - 5)$$

$$-3x - 1 = -x + 5$$

$$-3x + x = 5 + 1$$

$$-2x = 6$$

$$x = -3$$

¿Está $x = -3$ en la Región I? Sí, porque $-3 < -\frac{1}{3}$ ✓

### Paso 3: Analizar Región II: $-\frac{1}{3} \leq x < 5$

En esta región:
- $3x + 1 \geq 0 \Rightarrow |3x + 1| = 3x + 1$
- $x - 5 < 0 \Rightarrow |x - 5| = -(x - 5)$

La ecuación se convierte en:

$$3x + 1 = -(x - 5)$$

$$3x + 1 = -x + 5$$

$$4x = 4$$

$$x = 1$$

¿Está $x = 1$ en la Región II? Sí, porque $-\frac{1}{3} \leq 1 < 5$ ✓

### Paso 4: Analizar Región III: $x \geq 5$

En esta región:
- $3x + 1 > 0 \Rightarrow |3x + 1| = 3x + 1$
- $x - 5 \geq 0 \Rightarrow |x - 5| = x - 5$

La ecuación se convierte en:

$$3x + 1 = x - 5$$

$$2x = -6$$

$$x = -3$$

¿Está $x = -3$ en la Región III? No, porque $-3 < 5$ ✗

Esta solución no es válida en esta región.

---

## Interpretación geométrica

La ecuación $|3x + 1| = |x - 5|$ pregunta: ¿para qué valores de $x$ la distancia de $3x + 1$ al origen es igual a la distancia de $x - 5$ al origen?

```
Gráficamente: y = |3x + 1| intersecta a y = |x - 5|

        y
        │       /
        │      /   \
        │     /     \        /
        │    /       \      /
        │   /         \    /
        │  /           \  /
        │ /             \/
        │/               
   ─────┼───────────────────────▶ x
       -3    -1/3   1       5
```

Las intersecciones ocurren en $x = -3$ y $x = 1$.

---

## Diagrama de análisis por casos

```
                    |3x + 1| = |x - 5|
                          │
          ┌───────────────┴───────────────┐
          │                               │
    Caso: A = B                     Caso: A = -B
    3x + 1 = x - 5                  3x + 1 = -(x - 5)
          │                               │
       2x = -6                         4x = 4
          │                               │
       x = -3                           x = 1
          │                               │
          └───────────────┬───────────────┘
                          │
              Verificar ambas soluciones
                          │
           Conjunto solución: {-3, 1}
```

---

## Errores comunes a evitar

⚠️ **Error 1:** Elevar al cuadrado directamente sin considerar los casos.

Aunque funciona matemáticamente:
$$|3x + 1|^2 = |x - 5|^2$$
$$(3x + 1)^2 = (x - 5)^2$$

Es más propenso a errores algebraicos que el método de casos.

⚠️ **Error 2:** Olvidar verificar que las soluciones están en la región correcta cuando se usa el método de intervalos.

⚠️ **Error 3:** Pensar que $|A| = |B|$ implica solo $A = B$.

---

## Respuesta Final

$$\boxed{x = -3 \quad \text{o} \quad x = 1}$$

**Conjunto solución:** $\{-3, 1\}$

> 📚 Volver a: [FUN-03-Problemas](../../problems/FUN-03-Problemas.md)
