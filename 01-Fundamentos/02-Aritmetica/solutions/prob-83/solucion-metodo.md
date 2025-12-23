<!--
::METADATA::
type: solution
topic_id: fun-02-aritmetica
file_id: FUN-02-Prob-83-Solucion
status: stable
audience: student
problem_ref: "[Prob-83]"
methods: ["fórmula de tiempo-velocidad-distancia", "análisis porcentual", "comparación de tiempos"]
-->

# Solución [Prob-83]: Tiempo de viaje con cambio de velocidad

> **Problema:** Un tren recorre 240 km a 80 km/h. Si aumenta su velocidad en 25%, ¿cuánto tiempo ahorra?

---

## Método 1: Cálculo directo de tiempos

### Paso 1: Recordar la fórmula fundamental

$$\text{Tiempo} = \frac{\text{Distancia}}{\text{Velocidad}}$$

$$t = \frac{d}{v}$$

### Paso 2: Calcular el tiempo original

Con la velocidad original de 80 km/h:

$$t_1 = \frac{240 \text{ km}}{80 \text{ km/h}} = 3 \text{ horas}$$

### Paso 3: Calcular la nueva velocidad

Aumento del 25%:
$$v_2 = 80 + 0.25 \times 80 = 80 + 20 = 100 \text{ km/h}$$

O equivalentemente:
$$v_2 = 80 \times 1.25 = 100 \text{ km/h}$$

### Paso 4: Calcular el nuevo tiempo

Con la velocidad aumentada:

$$t_2 = \frac{240 \text{ km}}{100 \text{ km/h}} = 2.4 \text{ horas}$$

### Paso 5: Calcular el tiempo ahorrado

$$\text{Tiempo ahorrado} = t_1 - t_2 = 3 - 2.4 = 0.6 \text{ horas}$$

### Paso 6: Convertir a minutos

$$0.6 \text{ horas} = 0.6 \times 60 = 36 \text{ minutos}$$

---

## Método 2: Análisis mediante proporciones inversas

### Paso 1: Reconocer la relación inversa

A distancia constante, el tiempo es **inversamente proporcional** a la velocidad:

$$t \propto \frac{1}{v} \quad \Rightarrow \quad t_1 \cdot v_1 = t_2 \cdot v_2$$

### Paso 2: Establecer la proporción

$$\frac{t_2}{t_1} = \frac{v_1}{v_2}$$

### Paso 3: Calcular la razón de tiempos

Si la velocidad aumenta 25%, se multiplica por 1.25:
$$\frac{v_2}{v_1} = 1.25 = \frac{5}{4}$$

Por lo tanto:
$$\frac{t_2}{t_1} = \frac{v_1}{v_2} = \frac{4}{5}$$

### Paso 4: Calcular el nuevo tiempo

$$t_2 = t_1 \times \frac{4}{5} = 3 \times \frac{4}{5} = \frac{12}{5} = 2.4 \text{ horas}$$

### Paso 5: Calcular el ahorro

$$\text{Ahorro} = 3 - 2.4 = 0.6 \text{ horas} = 36 \text{ minutos}$$

---

## Método 3: Fórmula del porcentaje de ahorro

### Paso 1: Derivar la fórmula general

Si la velocidad se multiplica por un factor $k$ (donde $k > 1$):

$$t_2 = \frac{t_1}{k}$$

El ahorro de tiempo es:
$$\Delta t = t_1 - t_2 = t_1 - \frac{t_1}{k} = t_1 \left(1 - \frac{1}{k}\right) = t_1 \cdot \frac{k-1}{k}$$

### Paso 2: Aplicar al problema

Con $k = 1.25 = \frac{5}{4}$:

$$\frac{k-1}{k} = \frac{1.25 - 1}{1.25} = \frac{0.25}{1.25} = \frac{1}{5} = 0.2$$

### Paso 3: Calcular el ahorro

$$\Delta t = t_1 \times 0.2 = 3 \times 0.2 = 0.6 \text{ horas} = 36 \text{ minutos}$$

---

## Verificación

### Comprobación de distancias

- **Viaje original:** $80 \text{ km/h} \times 3 \text{ h} = 240 \text{ km}$ ✓
- **Viaje rápido:** $100 \text{ km/h} \times 2.4 \text{ h} = 240 \text{ km}$ ✓

Ambos recorridos cubren la misma distancia.

### Comprobación del porcentaje de ahorro

$$\frac{\text{Tiempo ahorrado}}{\text{Tiempo original}} = \frac{0.6}{3} = 0.2 = 20\%$$

Esto confirma que un aumento del 25% en velocidad produce un ahorro del 20% en tiempo (no el mismo porcentaje, debido a la relación inversa).

---

## Resumen de datos

| Concepto | Valor original | Valor nuevo |
|----------|----------------|-------------|
| Distancia | 240 km | 240 km |
| Velocidad | 80 km/h | 100 km/h (+25%) |
| Tiempo | 3 horas | 2.4 horas (−20%) |

---

## Nota importante

> ⚠️ Un error común es pensar que si la velocidad aumenta 25%, el tiempo disminuye 25%. **Esto es incorrecto** porque la relación es inversa, no lineal.

El porcentaje real de reducción de tiempo es:
$$\frac{0.6}{3} \times 100\% = 20\%$$

---

## Respuesta Final

**El tren ahorra 0.6 horas, es decir, 36 minutos.**

$$\boxed{36 \text{ minutos}} \quad \text{(o equivalentemente } 0.6 \text{ horas)}$$

> 📚 Volver a: [FUN-02-Problemas](../../problems/FUN-02-Problemas.md)
