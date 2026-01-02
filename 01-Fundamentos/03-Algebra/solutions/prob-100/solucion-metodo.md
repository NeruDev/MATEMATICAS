<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: FUN-03-Prob-100-Solucion
status: stable
audience: student
problem_ref: "[Prob-100]"
methods: ["elevar-al-cuadrado", "verificacion-soluciones", "analisis-[dominio](../../../../glossary.md#dominio)"]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución [Prob-100]: Ecuación radical (I)

> **Problema:** Resuelve: $\sqrt{2x + 3} = x$

## ⚠️ Advertencia importante

En ecuaciones con radicales, al elevar al cuadrado **pueden aparecer soluciones extrañas** (soluciones de la ecuación cuadrática que no satisfacen la ecuación original). Es **obligatorio verificar** todas las soluciones candidatas.

---

## Método 1: Elevar al cuadrado y verificar

### Paso 1: Establecer restricciones de dominio

Para que la ecuación tenga sentido:

**Restricción 1:** El radicando debe ser no negativo:
$$2x + 3 \geq 0 \quad \Rightarrow \quad x \geq -\frac{3}{2}$$

**Restricción 2:** El lado derecho debe ser no negativo (pues $\sqrt{\cdot} \geq 0$):
$$x \geq 0$$

**[Dominio](../../../../glossary.md#dominio) válido:** $x \geq 0$

### Paso 2: Elevar ambos lados al cuadrado

$$\left(\sqrt{2x + 3}\right)^2 = x^2$$

$$2x + 3 = x^2$$

### Paso 3: Reordenar como ecuación cuadrática

$$x^2 - 2x - 3 = 0$$

### Paso 4: Resolver la ecuación cuadrática

**Opción A: [Factorización](../../../../glossary.md#factorizacion)**

Buscamos dos números que multiplicados den $-3$ y sumados den $-2$:
- Los números son $-3$ y $1$

$$x^2 - 2x - 3 = (x - 3)(x + 1) = 0$$

**Soluciones candidatas:**
$$x - 3 = 0 \quad \Rightarrow \quad x = 3$$
$$x + 1 = 0 \quad \Rightarrow \quad x = -1$$

**Opción B: Fórmula general**

$$x = \frac{-(-2) \pm \sqrt{(-2)^2 - 4(1)(-3)}}{2(1)}$$

$$x = \frac{2 \pm \sqrt{4 + 12}}{2} = \frac{2 \pm \sqrt{16}}{2} = \frac{2 \pm 4}{2}$$

$$x_1 = \frac{2 + 4}{2} = 3 \qquad x_2 = \frac{2 - 4}{2} = -1$$

### Paso 5: Verificar cada solución candidata ⚠️

**Verificación de $x = 3$:**

$$\sqrt{2(3) + 3} \stackrel{?}{=} 3$$

$$\sqrt{6 + 3} = \sqrt{9} = 3 \quad \checkmark$$

**¡$x = 3$ es solución válida!**

---

**Verificación de $x = -1$:**

$$\sqrt{2(-1) + 3} \stackrel{?}{=} -1$$

$$\sqrt{-2 + 3} = \sqrt{1} = 1 \neq -1 \quad ✗$$

**¡$x = -1$ es solución EXTRAÑA!**

Además, $x = -1 < 0$ viola la restricción de dominio.

### Paso 6: Conclusión

$$\boxed{x = 3}$$

---

## Método 2: Análisis gráfico

### Paso 1: Definir las funciones

Sea:
$$f(x) = \sqrt{2x + 3}$$
$$g(x) = x$$

Buscamos los puntos donde $f(x) = g(x)$.

### Paso 2: Características de cada función

**$f(x) = \sqrt{2x + 3}$:**
- Dominio: $x \geq -\frac{3}{2}$
- Siempre positiva o cero
- Creciente
- Cóncava hacia abajo

**$g(x) = x$:**
- Dominio: todos los reales
- Recta con pendiente 1

### Paso 3: Intersección

Las funciones se intersectan donde ambas son iguales y no negativas:

```
    y│
     │        *****  
     │      **    ***     y = x
     │     *        ****     /
     │    *            **   /
   3 │   *                ●/
     │  *                / (3, 3)
     │ *               /
   1 │●              /
     │ (-1,1)      /
     └─────────────────────────► x
    -3/2    0      3
```

Solo hay **un punto de intersección** en el primer cuadrante: $(3, 3)$.

El punto $(-1, 1)$ está en la gráfica de $f$ pero **no** en la recta $y = x$.

### Paso 4: Conclusión

$$x = 3$$

---

## Método 3: Sustitución y verificación sistemática

### Paso 1: Sea $u = \sqrt{2x + 3}$

Entonces $u = x$ y $u^2 = 2x + 3$.

Sustituyendo $x = u$:
$$u^2 = 2u + 3$$

$$u^2 - 2u - 3 = 0$$

$$(u - 3)(u + 1) = 0$$

$$u = 3 \quad \text{o} \quad u = -1$$

### Paso 2: Recordar que $u = \sqrt{2x + 3} \geq 0$

$$u = -1 < 0 \quad \text{es imposible}$$

Solo $u = 3$ es válido.

### Paso 3: Encontrar $x$

$$\sqrt{2x + 3} = 3$$

$$2x + 3 = 9$$

$$2x = 6$$

$$x = 3$$

### Paso 4: Verificar

$$\sqrt{2(3) + 3} = \sqrt{9} = 3 = x \quad \checkmark$$

---

## ¿Por qué aparecen soluciones extrañas?

### Explicación algebraica

Al elevar al cuadrado la ecuación:

$$\sqrt{2x + 3} = x$$

Obtenemos:

$$2x + 3 = x^2$$

Pero esta ecuación cuadrática es equivalente a:

$$(\sqrt{2x + 3})^2 = x^2$$

Lo cual incluye tanto $\sqrt{2x + 3} = x$ como $\sqrt{2x + 3} = -x$.

Para $x = -1$:
$$\sqrt{2(-1) + 3} = \sqrt{1} = 1 = -(-1) = -x$$

Así, $x = -1$ satisface $\sqrt{2x + 3} = -x$, pero **no** la ecuación original $\sqrt{2x + 3} = x$.

### Diagrama de equivalencias

```
┌─────────────────────────────┐
│   √(2x + 3) = x             │  ← Ecuación original
└──────────────┬──────────────┘
               │ elevar al cuadrado
               ▼
┌─────────────────────────────┐
│   2x + 3 = x²               │  ← Ecuación cuadrática
│   (soluciones: x = 3, -1)   │
└──────────────┬──────────────┘
               │ incluye soluciones de:
     ┌─────────┴─────────┐
     ▼                   ▼
┌────────────┐     ┌────────────┐
│ √(2x+3)=x  │     │ √(2x+3)=-x │
│  x = 3 ✓   │     │  x = -1 ✗  │
└────────────┘     └────────────┘
```

---

## Resumen del proceso

| Paso | Acción | Resultado |
|------|--------|-----------|
| 1 | Determinar dominio | $x \geq 0$ |
| 2 | Elevar al cuadrado | $x^2 - 2x - 3 = 0$ |
| 3 | Resolver cuadrática | $x = 3$ o $x = -1$ |
| 4 | Verificar $x = 3$ | $\sqrt{9} = 3$ ✓ Válida |
| 5 | Verificar $x = -1$ | $\sqrt{1} = 1 \neq -1$ ✗ Extraña |
| **6** | **Solución final** | $\boxed{x = 3}$ |

---

## Verificación final

$$\sqrt{2(3) + 3} = \sqrt{9} = 3 \quad \checkmark$$

**La única solución es $x = 3$.**
