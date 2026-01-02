<!--
::METADATA::
type: solution
topic_id: cv-01-vectores-espacio
file_id: prob-16-solucion
problem_ref: Prob-16
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Descomposición de un Vector en Componentes Paralela y Perpendicular

## Problema

Descomponer el [vector](../../../../glossary.md#vector) $\mathbf{F} = \langle 5, 8, -1 \rangle$ en componentes paralela y perpendicular al vector $\mathbf{d} = \langle 1, 2, 2 \rangle$.

---

## Conceptos clave

**Proyección vectorial (componente paralela):**
$$\text{proy}_{\mathbf{d}}\mathbf{F} = \frac{\mathbf{F} \cdot \mathbf{d}}{|\mathbf{d}|^2}\mathbf{d}$$

**Componente perpendicular:**
$$\mathbf{F}_{\perp} = \mathbf{F} - \text{proy}_{\mathbf{d}}\mathbf{F}$$

**Verificación de ortogonalidad:**
$$\mathbf{F}_{\perp} \cdot \mathbf{d} = 0$$

---

## Solución

### Paso 1: Calcular el producto punto $\mathbf{F} \cdot \mathbf{d}$

$$\mathbf{F} \cdot \mathbf{d} = \langle 5, 8, -1 \rangle \cdot \langle 1, 2, 2 \rangle$$

$$= (5)(1) + (8)(2) + (-1)(2)$$

$$= 5 + 16 - 2$$

$$= 19$$

### Paso 2: Calcular $|\mathbf{d}|^2$

$$|\mathbf{d}|^2 = 1^2 + 2^2 + 2^2 = 1 + 4 + 4 = 9$$

### Paso 3: Calcular la componente paralela (proyección)

$$\mathbf{F}_{\parallel} = \text{proy}_{\mathbf{d}}\mathbf{F} = \frac{\mathbf{F} \cdot \mathbf{d}}{|\mathbf{d}|^2}\mathbf{d}$$

$$= \frac{19}{9}\langle 1, 2, 2 \rangle$$

$$= \left\langle \frac{19}{9}, \frac{38}{9}, \frac{38}{9} \right\rangle$$

### Paso 4: Calcular la componente perpendicular

$$\mathbf{F}_{\perp} = \mathbf{F} - \mathbf{F}_{\parallel}$$

$$= \langle 5, 8, -1 \rangle - \left\langle \frac{19}{9}, \frac{38}{9}, \frac{38}{9} \right\rangle$$

$$= \left\langle 5 - \frac{19}{9}, 8 - \frac{38}{9}, -1 - \frac{38}{9} \right\rangle$$

$$= \left\langle \frac{45 - 19}{9}, \frac{72 - 38}{9}, \frac{-9 - 38}{9} \right\rangle$$

$$= \left\langle \frac{26}{9}, \frac{34}{9}, \frac{-47}{9} \right\rangle$$

---

## Respuesta Final

$$\boxed{\mathbf{F}_{\parallel} = \left\langle \frac{19}{9}, \frac{38}{9}, \frac{38}{9} \right\rangle}$$

$$\boxed{\mathbf{F}_{\perp} = \left\langle \frac{26}{9}, \frac{34}{9}, -\frac{47}{9} \right\rangle}$$

---

## Verificación

### Verificación 1: Ortogonalidad de $\mathbf{F}_{\perp}$ y $\mathbf{d}$

$$\mathbf{F}_{\perp} \cdot \mathbf{d} = \left\langle \frac{26}{9}, \frac{34}{9}, -\frac{47}{9} \right\rangle \cdot \langle 1, 2, 2 \rangle$$

$$= \frac{26}{9}(1) + \frac{34}{9}(2) + \left(-\frac{47}{9}\right)(2)$$

$$= \frac{26 + 68 - 94}{9} = \frac{0}{9} = 0 \checkmark$$

### Verificación 2: Suma de componentes igual al vector original

$$\mathbf{F}_{\parallel} + \mathbf{F}_{\perp} = \left\langle \frac{19}{9}, \frac{38}{9}, \frac{38}{9} \right\rangle + \left\langle \frac{26}{9}, \frac{34}{9}, -\frac{47}{9} \right\rangle$$

$$= \left\langle \frac{19+26}{9}, \frac{38+34}{9}, \frac{38-47}{9} \right\rangle$$

$$= \left\langle \frac{45}{9}, \frac{72}{9}, \frac{-9}{9} \right\rangle = \langle 5, 8, -1 \rangle = \mathbf{F} \checkmark$$

### Verificación 3: $\mathbf{F}_{\parallel}$ es paralelo a $\mathbf{d}$

$$\mathbf{F}_{\parallel} = \frac{19}{9}\mathbf{d}$$

Efectivamente $\mathbf{F}_{\parallel}$ es un múltiplo escalar de $\mathbf{d}$. $\checkmark$
