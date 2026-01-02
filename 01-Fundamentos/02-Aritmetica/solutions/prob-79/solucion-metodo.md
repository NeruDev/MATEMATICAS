<!--
::METADATA::
type: solution
topic_id: fun-02-aritmetica
file_id: FUN-02-Prob-79-Solucion
status: stable
audience: student
problem_ref: "[Prob-79]"
methods: ["proporcionalidad compuesta", "regla de tres compuesta", "análisis dimensional"]
-->

# Solución [Prob-79]: Proporcionalidad compuesta

> **Problema:** Si 5 máquinas producen 200 artículos en 4 horas, ¿cuántos artículos producen 8 máquinas en 5 horas?

---

## Método 1: Proporcionalidad compuesta paso a paso

### Paso 1: Identificar las magnitudes y sus relaciones

| Magnitud | Valor inicial | Valor final | Relación con producción |
|----------|---------------|-------------|------------------------|
| Máquinas | 5 | 8 | **Directa** (más máquinas → más producción) |
| Tiempo | 4 horas | 5 horas | **Directa** (más tiempo → más producción) |
| Artículos | 200 | $x$ | (incógnita) |

### Paso 2: Establecer la proporción

Como ambas relaciones son **directas**, la producción aumenta proporcionalmente:

$$\frac{x}{200} = \frac{8}{5} \times \frac{5}{4}$$

### Paso 3: Calcular el resultado

$$x = 200 \times \frac{8}{5} \times \frac{5}{4}$$

$$x = 200 \times \frac{8 \times 5}{5 \times 4}$$

$$x = 200 \times \frac{40}{20}$$

$$x = 200 \times 2$$

$$x = 400$$

---

## Método 2: Regla de tres compuesta (formato tradicional)

### Paso 1: Organizar los datos en una tabla

| Máquinas | Horas | Artículos |
|----------|-------|-----------|
| 5 | 4 | 200 |
| 8 | 5 | $x$ |

### Paso 2: Determinar el tipo de proporcionalidad

**Máquinas vs Artículos:**
- Si aumentan las máquinas, aumentan los artículos
- Proporcionalidad **DIRECTA**

**Horas vs Artículos:**
- Si aumentan las horas, aumentan los artículos
- Proporcionalidad **DIRECTA**

### Paso 3: Construir la ecuación

Para proporcionalidad directa, las fracciones van "como están":

$$\frac{200}{x} = \frac{5}{8} \times \frac{4}{5}$$

### Paso 4: Resolver

$$\frac{200}{x} = \frac{5 \times 4}{8 \times 5} = \frac{20}{40} = \frac{1}{2}$$

$$x = 200 \times 2 = 400$$

---

## Método 3: Análisis dimensional (producción unitaria)

### Paso 1: Calcular la producción por máquina-hora

$$\text{Producción unitaria} = \frac{200 \text{ artículos}}{5 \text{ máquinas} \times 4 \text{ horas}}$$

$$= \frac{200}{20} = 10 \text{ artículos por [máquina](../../../../glossary.md#maquina)-hora}$$

### Paso 2: Calcular la producción total con los nuevos valores

$$\text{Producción} = 10 \frac{\text{artículos}}{\text{[máquina](../../../../glossary.md#maquina)-hora}} \times 8 \text{ máquinas} \times 5 \text{ horas}$$

$$= 10 \times 8 \times 5 = 400 \text{ artículos}$$

---

## Método 4: Análisis por etapas

### Paso 1: Cambiar solo el número de máquinas (de 5 a 8)

Manteniendo las 4 horas constantes:

$$\frac{5 \text{ máquinas}}{8 \text{ máquinas}} = \frac{200 \text{ artículos}}{x_1 \text{ artículos}}$$

Como es directa:
$$x_1 = 200 \times \frac{8}{5} = \frac{1600}{5} = 320 \text{ artículos}$$

### Paso 2: Cambiar el tiempo (de 4 a 5 horas)

Con 8 máquinas que producen 320 artículos en 4 horas:

$$\frac{4 \text{ horas}}{5 \text{ horas}} = \frac{320 \text{ artículos}}{x \text{ artículos}}$$

Como es directa:
$$x = 320 \times \frac{5}{4} = \frac{1600}{4} = 400 \text{ artículos}$$

---

## Verificación

### Comprobación con la producción unitaria

- **Situación original:** 5 máquinas × 4 horas = 20 máquinas-hora → 200 artículos
  - Tasa: $\frac{200}{20} = 10$ artículos/máquina-hora ✓

- **Situación nueva:** 8 máquinas × 5 horas = 40 máquinas-hora → 400 artículos
  - Tasa: $\frac{400}{40} = 10$ artículos/máquina-hora ✓

La tasa de producción por máquina-hora es la misma en ambos casos.

### Comprobación de proporciones

$$\frac{\text{Artículos nuevos}}{\text{Artículos originales}} = \frac{400}{200} = 2$$

$$\frac{\text{Máquinas nuevas}}{\text{Máquinas originales}} \times \frac{\text{Horas nuevas}}{\text{Horas originales}} = \frac{8}{5} \times \frac{5}{4} = 2 \checkmark$$

---

## Fórmula General

Para problemas de proporcionalidad compuesta:

$$\frac{x}{x_0} = \left(\frac{a_1}{a_0}\right)^{\pm 1} \times \left(\frac{b_1}{b_0}\right)^{\pm 1} \times ...$$

Donde el exponente es:
- $+1$ para proporcionalidad directa
- $-1$ para proporcionalidad inversa

---

## Respuesta Final

$$\boxed{400 \text{ artículos}}$$

> 📚 Volver a: [FUN-02-Problemas](../../problems/FUN-02-Problemas.md)
