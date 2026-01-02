<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: FUN-03-Prob-101-Solucion
status: stable
audience: student
problem_ref: "[Prob-101]"
methods: ["aislamiento-radical", "doble-elevacion", "sustitucion"]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución [Prob-101]: Ecuación radical (II) - Dos radicales

> **Problema:** Resuelve: $\sqrt{x + 5} + \sqrt{x} = 5$

## ⚠️ Advertencia importante

En ecuaciones con radicales, al elevar al cuadrado **pueden aparecer soluciones extrañas**. Es **obligatorio verificar** todas las soluciones candidatas en la ecuación original.

---

## Método 1: Aislar un radical y elevar al cuadrado (dos veces)

### Paso 1: Establecer restricciones de dominio

Para que ambos radicales estén definidos:

$$x + 5 \geq 0 \quad \Rightarrow \quad x \geq -5$$

$$x \geq 0$$

**[Dominio](../../../..](../../../../glossary.md)#dominio) válido:** $x \geq 0$

### Paso 2: Aislar un radical

$$\sqrt{x + 5} = 5 - \sqrt{x}$$

### Paso 3: Primera elevación al cuadrado

$$\left(\sqrt{x + 5}\right)^2 = \left(5 - \sqrt{x}\right)^2$$

**Lado izquierdo:**
$$x + 5$$

**Lado derecho:** (usando $(a - b)^2 = a^2 - 2ab + b^2$)
$$(5)^2 - 2(5)(\sqrt{x}) + (\sqrt{x})^2$$
$$= 25 - 10\sqrt{x} + x$$

**Ecuación resultante:**
$$x + 5 = 25 - 10\sqrt{x} + x$$

### Paso 4: Simplificar y aislar el radical restante

$$x + 5 = 25 - 10\sqrt{x} + x$$

Cancelamos $x$ de ambos lados:
$$5 = 25 - 10\sqrt{x}$$

Despejamos el término con radical:
$$10\sqrt{x} = 25 - 5$$

$$10\sqrt{x} = 20$$

$$\sqrt{x} = 2$$

### Paso 5: Segunda elevación al cuadrado

$$(\sqrt{x})^2 = 2^2$$

$$x = 4$$

### Paso 6: Verificación obligatoria ⚠️

Sustituimos $x = 4$ en la ecuación original:

$$\sqrt{4 + 5} + \sqrt{4} \stackrel{?}{=} 5$$

$$\sqrt{9} + \sqrt{4} = 3 + 2 = 5 \quad \checkmark$$

**¡$x = 4$ es solución válida!**

### Paso 7: Conclusión

$$\boxed{x = 4}$$

---

## Método 2: Sustitución $u = \sqrt{x}$

### Paso 1: Realizar la sustitución

Sea $u = \sqrt{x}$, entonces $u \geq 0$ y $x = u^2$.

$$\sqrt{x + 5} + \sqrt{x} = 5$$

$$\sqrt{u^2 + 5} + u = 5$$

### Paso 2: Aislar el radical

$$\sqrt{u^2 + 5} = 5 - u$$

**Restricción adicional:** $5 - u \geq 0 \Rightarrow u \leq 5$

### Paso 3: Elevar al cuadrado

$$u^2 + 5 = (5 - u)^2$$

$$u^2 + 5 = 25 - 10u + u^2$$

### Paso 4: Simplificar

$$u^2 + 5 = 25 - 10u + u^2$$

Restamos $u^2$ de ambos lados:
$$5 = 25 - 10u$$

$$10u = 20$$

$$u = 2$$

### Paso 5: Regresar a la variable original

$$\sqrt{x} = 2$$

$$x = 4$$

### Paso 6: Verificar

$$\sqrt{4 + 5} + \sqrt{4} = 3 + 2 = 5 \quad \checkmark$$

---

## Método 3: Conjugado (racionalización)

### Paso 1: Escribir la ecuación y su conjugada

**Ecuación original:**
$$\sqrt{x + 5} + \sqrt{x} = 5 \quad \text{...(1)}$$

**Identidad algebraica:**
$$(\sqrt{x + 5} + \sqrt{x})(\sqrt{x + 5} - \sqrt{x}) = (x + 5) - x = 5$$

### Paso 2: Usar la identidad

Dividimos la identidad por la ecuación (1):

$$\sqrt{x + 5} - \sqrt{x} = \frac{5}{\sqrt{x + 5} + \sqrt{x}} = \frac{5}{5} = 1$$

**Ecuación conjugada:**
$$\sqrt{x + 5} - \sqrt{x} = 1 \quad \text{...(2)}$$

### Paso 3: Resolver el sistema de ecuaciones

Sumamos (1) y (2):
$$(\sqrt{x + 5} + \sqrt{x}) + (\sqrt{x + 5} - \sqrt{x}) = 5 + 1$$

$$2\sqrt{x + 5} = 6$$

$$\sqrt{x + 5} = 3$$

$$x + 5 = 9$$

$$x = 4$$

### Paso 4: Verificación alternativa

Restamos (2) de (1):
$$(\sqrt{x + 5} + \sqrt{x}) - (\sqrt{x + 5} - \sqrt{x}) = 5 - 1$$

$$2\sqrt{x} = 4$$

$$\sqrt{x} = 2$$

$$x = 4 \quad \checkmark$$

---

## Análisis gráfico

### Funciones a graficar

$$f(x) = \sqrt{x + 5} + \sqrt{x}$$
$$g(x) = 5$$

### Comportamiento de $f(x)$

- **[Dominio](../../../..](../../../../glossary.md)#dominio):** $x \geq 0$
- **En $x = 0$:** $f(0) = \sqrt{5} + 0 = \sqrt{5} \approx 2.24$
- **[Función](../../../..](../../../../glossary.md)#funcion) creciente:** la suma de dos funciones crecientes
- **En $x = 4$:** $f(4) = 3 + 2 = 5$

### Gráfica

```
    y│
     │
   6 │                    ****
     │                 ***
   5 │─ ─ ─ ─ ─ ─ ─ ─●─ ─ ─ ─ ─ ─  y = 5
     │            ***  (4, 5)
   4 │          **
     │        **
   3 │      **
√5≈2.2│    ●
     │   * (0, √5)
     │
     └──────────────────────────► x
         0    4         
```

**Único punto de intersección:** $(4, 5)$

---

## Verificación de que no hay soluciones extrañas

### ¿Por qué en este caso solo hay una solución?

1. **Dominio restringido:** $x \geq 0$

2. **$f(x) = \sqrt{x + 5} + \sqrt{x}$ es estrictamente creciente** para $x \geq 0$

3. **$f(0) = \sqrt{5} \approx 2.24 < 5$**

4. **$\lim_{x \to \infty} f(x) = \infty$**

Por el teorema del valor intermedio, existe exactamente **un** valor de $x$ donde $f(x) = 5$.

### Tabla de valores

| $x$ | $\sqrt{x+5}$ | $\sqrt{x}$ | Suma |
|-----|--------------|------------|------|
| $0$ | $\sqrt{5} \approx 2.24$ | $0$ | $\approx 2.24$ |
| $1$ | $\sqrt{6} \approx 2.45$ | $1$ | $\approx 3.45$ |
| $4$ | $3$ | $2$ | $5$ ✓ |
| $9$ | $\sqrt{14} \approx 3.74$ | $3$ | $\approx 6.74$ |

---

## Resumen del proceso

| Paso | Método 1 | Resultado |
|------|----------|-----------|
| 1 | Dominio | $x \geq 0$ |
| 2 | Aislar radical | $\sqrt{x+5} = 5 - \sqrt{x}$ |
| 3 | Elevar al cuadrado | $x + 5 = 25 - 10\sqrt{x} + x$ |
| 4 | Simplificar | $\sqrt{x} = 2$ |
| 5 | Resolver | $x = 4$ |
| 6 | Verificar | $\sqrt{9} + \sqrt{4} = 5$ ✓ |
| **7** | **Solución** | $\boxed{x = 4}$ |

---

## Errores comunes a evitar

### ❌ Error 1: Elevar al cuadrado sin aislar

$$(\sqrt{x + 5} + \sqrt{x})^2 \neq (x + 5) + x$$

**Correcto:**
$$(\sqrt{x + 5} + \sqrt{x})^2 = (x + 5) + 2\sqrt{x(x+5)} + x$$

### ❌ Error 2: Olvidar verificar

Aunque en este problema la solución $x = 4$ resulta válida, siempre hay que verificar porque al elevar al cuadrado se pueden introducir soluciones espurias.

### ❌ Error 3: Ignorar restricciones de dominio

Si hubiéramos obtenido una solución negativa, habría que descartarla porque el dominio es $x \geq 0$.

---

## Verificación final

$$\sqrt{4 + 5} + \sqrt{4} = \sqrt{9} + \sqrt{4} = 3 + 2 = 5 \quad \checkmark$$

**La única solución es $\boxed{x = 4}$**
