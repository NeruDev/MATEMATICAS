<!--
::METADATA::
type: solution
topic_id: fun-02-aritmetica
file_id: prob-45-solucion
problem_ref: Prob-45
status: stable
audience: student
-->

# Solución: Serie de fracciones parciales (telescópica)

## Problema
Calcula: $\frac{1}{1 \times 2} + \frac{1}{2 \times 3} + \frac{1}{3 \times 4} + \frac{1}{4 \times 5}$

---

## Método 1: Suma directa

### Paso 1: Calcular cada término
$$\frac{1}{1 \times 2} = \frac{1}{2}$$
$$\frac{1}{2 \times 3} = \frac{1}{6}$$
$$\frac{1}{3 \times 4} = \frac{1}{12}$$
$$\frac{1}{4 \times 5} = \frac{1}{20}$$

### Paso 2: Encontrar denominador común
$$\text{[MCM](../../../../glossary.md#mcm)}(2, 6, 12, 20) = 60$$

### Paso 3: Convertir fracciones
$$\frac{1}{2} = \frac{30}{60}, \quad \frac{1}{6} = \frac{10}{60}, \quad \frac{1}{12} = \frac{5}{60}, \quad \frac{1}{20} = \frac{3}{60}$$

### Paso 4: Sumar
$$\frac{30 + 10 + 5 + 3}{60} = \frac{48}{60} = \frac{4}{5}$$

---

## Método 2: Fracciones parciales (Telescópica)

### Paso 1: Descomponer cada término
Observamos que:
$$\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$$

**Verificación de la identidad:**
$$\frac{1}{n} - \frac{1}{n+1} = \frac{(n+1) - n}{n(n+1)} = \frac{1}{n(n+1)} \checkmark$$

### Paso 2: Aplicar a cada término
$$\frac{1}{1 \times 2} = \frac{1}{1} - \frac{1}{2} = 1 - \frac{1}{2}$$
$$\frac{1}{2 \times 3} = \frac{1}{2} - \frac{1}{3}$$
$$\frac{1}{3 \times 4} = \frac{1}{3} - \frac{1}{4}$$
$$\frac{1}{4 \times 5} = \frac{1}{4} - \frac{1}{5}$$

### Paso 3: Sumar (efecto telescópico)
$$\left(1 - \cancel{\frac{1}{2}}\right) + \left(\cancel{\frac{1}{2}} - \cancel{\frac{1}{3}}\right) + \left(\cancel{\frac{1}{3}} - \cancel{\frac{1}{4}}\right) + \left(\cancel{\frac{1}{4}} - \frac{1}{5}\right)$$

Los términos intermedios se cancelan:
$$= 1 - \frac{1}{5} = \frac{5-1}{5} = \frac{4}{5}$$

---

## Respuesta Final
$$\frac{1}{1 \times 2} + \frac{1}{2 \times 3} + \frac{1}{3 \times 4} + \frac{1}{4 \times 5} = \boxed{\frac{4}{5}}$$

---

## Generalización
Para la suma $\displaystyle\sum_{k=1}^{n} \frac{1}{k(k+1)}$:

$$\sum_{k=1}^{n} \frac{1}{k(k+1)} = \sum_{k=1}^{n} \left(\frac{1}{k} - \frac{1}{k+1}\right) = 1 - \frac{1}{n+1} = \frac{n}{n+1}$$

En nuestro caso, $n = 4$: $\frac{4}{4+1} = \frac{4}{5}$ ✓
