<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: FUN-03-Prob-108-Solucion
status: stable
audience: student
problem_ref: "[Prob-108]"
methods: ["ecuacion-racional", "trabajo-conjunto", "tasas-de-trabajo"]
-->

# Solución [Prob-108]: Problema de grifos (trabajo conjunto)

> **Problema:** Dos grifos llenan un tanque. El primero tarda $x$ horas y el segundo $x + 2$ horas. Juntos tardan 2.4 horas. ¿Cuánto tarda cada uno por separado?

## Concepto clave: Tasas de trabajo

Si un grifo llena un tanque en $t$ horas, entonces:
- **Tasa de llenado** = $\frac{1}{t}$ del tanque por hora

---

## Método 1: Ecuación de tasas de trabajo

### Paso 1: Definir variables y tasas

| Grifo | Tiempo individual | Tasa (tanque/hora) |
|-------|-------------------|-------------------|
| Primero | $x$ horas | $\frac{1}{x}$ |
| Segundo | $x + 2$ horas | $\frac{1}{x+2}$ |
| **Juntos** | $2.4$ horas | $\frac{1}{2.4}$ |

### Paso 2: Plantear la ecuación

**Principio:** Las tasas se suman cuando trabajan juntos.

$$\text{Tasa}_1 + \text{Tasa}_2 = \text{Tasa conjunta}$$

$$\frac{1}{x} + \frac{1}{x+2} = \frac{1}{2.4}$$

### Paso 3: Simplificar $\frac{1}{2.4}$

$$2.4 = \frac{24}{10} = \frac{12}{5}$$

$$\frac{1}{2.4} = \frac{5}{12}$$

**Ecuación:**
$$\frac{1}{x} + \frac{1}{x+2} = \frac{5}{12}$$

### Paso 4: Encontrar el MCM y eliminar denominadores

MCM de $x$, $(x+2)$ y $12$ es $12x(x+2)$.

Multiplicamos toda la ecuación por $12x(x+2)$:

$$12x(x+2) \cdot \frac{1}{x} + 12x(x+2) \cdot \frac{1}{x+2} = 12x(x+2) \cdot \frac{5}{12}$$

### Paso 5: Simplificar cada término

**Término 1:**
$$12x(x+2) \cdot \frac{1}{x} = 12(x+2) = 12x + 24$$

**Término 2:**
$$12x(x+2) \cdot \frac{1}{x+2} = 12x$$

**Término 3:**
$$12x(x+2) \cdot \frac{5}{12} = 5x(x+2) = 5x^2 + 10x$$

### Paso 6: Formar la ecuación

$$12x + 24 + 12x = 5x^2 + 10x$$

$$24x + 24 = 5x^2 + 10x$$

### Paso 7: Reordenar en forma estándar

$$0 = 5x^2 + 10x - 24x - 24$$

$$5x^2 - 14x - 24 = 0$$

### Paso 8: Resolver la ecuación cuadrática

**Usando la fórmula general:**

$$a = 5, \quad b = -14, \quad c = -24$$

$$\Delta = b^2 - 4ac = (-14)^2 - 4(5)(-24)$$

$$\Delta = 196 + 480 = 676$$

$$\sqrt{\Delta} = \sqrt{676} = 26$$

$$x = \frac{-(-14) \pm 26}{2(5)} = \frac{14 \pm 26}{10}$$

**Solución 1:**
$$x_1 = \frac{14 + 26}{10} = \frac{40}{10} = 4$$

**Solución 2:**
$$x_2 = \frac{14 - 26}{10} = \frac{-12}{10} = -1.2$$

### Paso 9: Analizar las soluciones

- $x = 4$ ✓ (tiempo positivo, válido)
- $x = -1.2$ ✗ (tiempo negativo, no tiene sentido físico)

### Paso 10: Calcular tiempos individuales

$$\text{Grifo 1: } x = 4 \text{ horas}$$

$$\text{Grifo 2: } x + 2 = 4 + 2 = 6 \text{ horas}$$

### Conclusión

$$\boxed{\text{Primer grifo: } 4 \text{ horas}, \quad \text{Segundo grifo: } 6 \text{ horas}}$$

---

## Método 2: Trabajo completado

### Paso 1: Concepto de trabajo completado

En $t$ horas, cada grifo completa una fracción del trabajo:

| Grifo | En $t$ horas completa |
|-------|----------------------|
| Primero | $\frac{t}{x}$ del tanque |
| Segundo | $\frac{t}{x+2}$ del tanque |

### Paso 2: En 2.4 horas, juntos completan 1 tanque

$$\frac{2.4}{x} + \frac{2.4}{x+2} = 1$$

### Paso 3: Multiplicar por $\frac{1}{2.4} = \frac{5}{12}$

$$\frac{1}{x} + \frac{1}{x+2} = \frac{1}{2.4} = \frac{5}{12}$$

(Misma ecuación que en el Método 1)

### Paso 4: Resolver

$$5x^2 - 14x - 24 = 0$$

$$x = 4 \text{ (descartando el negativo)}$$

**Resultado:** Primero 4 h, Segundo 6 h.

---

## Método 3: Factorización de la cuadrática

### Partiendo de $5x^2 - 14x - 24 = 0$

Buscamos factorizar $5x^2 - 14x - 24$.

**Producto:** $a \cdot c = 5 \cdot (-24) = -120$

**Suma:** $b = -14$

Necesitamos dos números que:
- Multiplicados den $-120$
- Sumados den $-14$

Los números son $-20$ y $6$:
- $(-20)(6) = -120$ ✓
- $(-20) + 6 = -14$ ✓

### Reescribir el término medio

$$5x^2 - 20x + 6x - 24 = 0$$

### Factorizar por agrupación

$$5x(x - 4) + 6(x - 4) = 0$$

$$(5x + 6)(x - 4) = 0$$

### Resolver

$$5x + 6 = 0 \quad \Rightarrow \quad x = -\frac{6}{5} = -1.2 \quad \text{(rechazado)}$$

$$x - 4 = 0 \quad \Rightarrow \quad x = 4 \quad \checkmark$$

---

## Verificación completa

### Datos obtenidos

- Grifo 1: 4 horas (tasa: $\frac{1}{4}$ tanque/hora)
- Grifo 2: 6 horas (tasa: $\frac{1}{6}$ tanque/hora)

### Verificación de la tasa conjunta

$$\frac{1}{4} + \frac{1}{6} = \frac{3}{12} + \frac{2}{12} = \frac{5}{12}$$

### Verificación del tiempo conjunto

$$\text{Tiempo conjunto} = \frac{1}{\frac{5}{12}} = \frac{12}{5} = 2.4 \text{ horas} \quad \checkmark$$

### Verificación del trabajo en 2.4 horas

**Grifo 1 en 2.4 h:**
$$\frac{2.4}{4} = 0.6 = \frac{3}{5} \text{ del tanque}$$

**Grifo 2 en 2.4 h:**
$$\frac{2.4}{6} = 0.4 = \frac{2}{5} \text{ del tanque}$$

**Total:**
$$\frac{3}{5} + \frac{2}{5} = \frac{5}{5} = 1 \text{ tanque completo} \quad \checkmark$$

---

## Diagrama visual

```
Trabajo realizado en 2.4 horas:

Grifo 1 (4 h individual):
████████████████████░░░░░░░░░░  60% = 3/5
|←────── 2.4 h ──────→|

Grifo 2 (6 h individual):
████████████████░░░░░░░░░░░░░░  40% = 2/5
|←────── 2.4 h ──────→|

Juntos:
████████████████████████████████  100%
|←────── 2.4 h ──────→|
```

---

## Tabla resumen de la fórmula de trabajo conjunto

Para $n$ trabajadores/dispositivos:

$$\frac{1}{t_1} + \frac{1}{t_2} + \cdots + \frac{1}{t_n} = \frac{1}{T}$$

donde:
- $t_i$: tiempo que tarda el $i$-ésimo en completar el trabajo solo
- $T$: tiempo que tardan todos juntos

### Caso especial: dos trabajadores

$$\frac{1}{t_1} + \frac{1}{t_2} = \frac{1}{T}$$

$$T = \frac{t_1 \cdot t_2}{t_1 + t_2}$$

**Verificación con nuestros valores:**

$$T = \frac{4 \cdot 6}{4 + 6} = \frac{24}{10} = 2.4 \text{ horas} \quad \checkmark$$

---

## Resumen

| Aspecto | Valor |
|---------|-------|
| Variable | $x$ = tiempo del primer grifo |
| Ecuación planteada | $\frac{1}{x} + \frac{1}{x+2} = \frac{5}{12}$ |
| Ecuación cuadrática | $5x^2 - 14x - 24 = 0$ |
| Soluciones | $x = 4$ (válida), $x = -1.2$ (rechazada) |
| **Primer grifo** | $\boxed{4 \text{ horas}}$ |
| **Segundo grifo** | $\boxed{6 \text{ horas}}$ |

---

## Extensión: Problemas similares

Este tipo de problemas de "trabajo conjunto" aparece en:

- **Grifos/tuberías:** Llenar o vaciar tanques
- **Trabajadores:** Completar un proyecto
- **Máquinas:** Producir cierta cantidad de piezas
- **Velocidades:** Encuentro de móviles

La fórmula clave siempre es:
$$\text{Tasa}_1 + \text{Tasa}_2 + \cdots = \text{Tasa total}$$
