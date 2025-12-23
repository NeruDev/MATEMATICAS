<!--
::METADATA::
type: solution
topic_id: fun-06-geometria-analitica
file_id: prob-25-solucion
problem_ref: Prob-25
status: stable
audience: student
-->

# Solución: Ángulo entre dos rectas

## Problema
Encuentra el ángulo agudo entre las rectas $y = 3x - 1$ y $y = -2x + 4$.

---

## Método: Fórmula de ángulo entre rectas

### Paso 1: Identificar las pendientes
De la forma $y = mx + b$:
- Recta 1: $m_1 = 3$
- Recta 2: $m_2 = -2$

### Paso 2: Fórmula del ángulo entre dos rectas
$$\tan\theta = \left|\frac{m_1 - m_2}{1 + m_1 m_2}\right|$$

**Nota:** El valor absoluto asegura que obtengamos el ángulo agudo.

### Paso 3: Sustituir valores
$$\tan\theta = \left|\frac{3 - (-2)}{1 + (3)(-2)}\right|$$

$$= \left|\frac{3 + 2}{1 - 6}\right|$$

$$= \left|\frac{5}{-5}\right|$$

$$= |-1|$$

$$= 1$$

### Paso 4: Encontrar el ángulo
$$\tan\theta = 1$$
$$\theta = \arctan(1) = 45°$$

---

## Verificación geométrica

### Ángulos de inclinación de cada recta
- Recta 1: $\alpha_1 = \arctan(3) \approx 71.57°$
- Recta 2: $\alpha_2 = \arctan(-2) \approx -63.43°$ (o $180° - 63.43° = 116.57°$)

### Diferencia de ángulos
La diferencia absoluta es aproximadamente:
$$|71.57° - 116.57°| = 45°$$ ✓

O considerando el ángulo suplementario:
$$180° - |71.57° - (-63.43°)| = 180° - 135° = 45°$$ ✓

---

## Respuesta Final
$$\boxed{\theta = 45°}$$

---

## Diagrama
```
     y ↑
       |     /  y = 3x - 1
       |    / 
       |   /   45°
       |  /____/____
       | /    /     y = -2x + 4
       |/____/______
     --+------------→ x
      /|
     / |
```

---

## Caso especial: Rectas perpendiculares
Si $m_1 \cdot m_2 = -1$, las rectas son perpendiculares (ángulo = 90°).

En nuestro caso: $3 \times (-2) = -6 \neq -1$, por lo que no son perpendiculares.

---

## Fórmula alternativa (con arcotangente)
$$\theta = \arctan\left(\left|\frac{m_1 - m_2}{1 + m_1 m_2}\right|\right)$$

Si el denominador es cero ($m_1 m_2 = -1$), las rectas son perpendiculares: $\theta = 90°$.
