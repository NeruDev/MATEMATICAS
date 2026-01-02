<!--
::METADATA::
type: cheatsheet
topic_id: fun-04-geometria
file_id: FUN-04-Resumen-Formulas
status: stable
audience: student
requires: [fun-04-geometria-intro]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Geometría — Resumen de Fórmulas

## Ángulos

| Tipo | Medida |
|------|--------|
| Agudo | $0° < \alpha < 90°$ |
| Recto | $\alpha = 90°$ |
| Obtuso | $90° < \alpha < 180°$ |
| Llano | $\alpha = 180°$ |

**Complementarios:** $\alpha + \beta = 90°$  
**Suplementarios:** $\alpha + \beta = 180°$

---

## Polígonos (n lados)

| Propiedad | Fórmula |
|-----------|---------|
| Suma de ángulos interiores | $(n-2) \cdot 180°$ |
| Cada ángulo interior (regular) | $\frac{(n-2) \cdot 180°}{n}$ |
| Suma de ángulos exteriores | $360°$ |
| Cada ángulo exterior (regular) | $\frac{360°}{n}$ |
| Número de diagonales | $\frac{n(n-3)}{2}$ |

---

## Triángulos

### Propiedades
- Suma de ángulos interiores: $\alpha + \beta + \gamma = 180°$
- Desigualdad triangular: $a + b > c$

### Líneas notables

| Línea | Punto de concurrencia |
|-------|----------------------|
| Mediana | Centroide (G) |
| Altura | Ortocentro (H) |
| Mediatriz | Circuncentro (O) |
| Bisectriz | Incentro (I) |

### Criterios de congruencia
**LLL** · **LAL** · **ALA** · **AAL**

### Criterios de semejanza
**AA** · **LAL** · **LLL**

---

## Teorema de Pitágoras

$$c^2 = a^2 + b^2$$

| Condición | Tipo de triángulo |
|-----------|-------------------|
| $c^2 = a^2 + b^2$ | Rectángulo |
| $c^2 < a^2 + b^2$ | Acutángulo |
| $c^2 > a^2 + b^2$ | Obtusángulo |

**Ternas pitagóricas:** $(3,4,5)$, $(5,12,13)$, $(8,15,17)$, $(7,24,25)$

---

## Áreas de Figuras Planas

| Figura | Fórmula |
|--------|---------|
| Cuadrado | $A = l^2$ |
| Rectángulo | $A = b \cdot h$ |
| Triángulo | $A = \frac{b \cdot h}{2}$ |
| Paralelogramo | $A = b \cdot h$ |
| Rombo | $A = \frac{D \cdot d}{2}$ |
| Trapecio | $A = \frac{(B + b) \cdot h}{2}$ |
| Polígono regular | $A = \frac{P \cdot a}{2}$ |
| Círculo | $A = \pi r^2$ |
| Sector circular | $A = \frac{\theta}{360°} \pi r^2$ |

### Fórmula de Herón
$$A = \sqrt{s(s-a)(s-b)(s-c)}, \quad s = \frac{a+b+c}{2}$$

---

## Perímetros

| Figura | Perímetro |
|--------|-----------|
| Cuadrado | $P = 4l$ |
| Rectángulo | $P = 2(b + h)$ |
| Triángulo | $P = a + b + c$ |
| Circunferencia | $C = 2\pi r = \pi d$ |

---

## Circunferencia

| Tipo de ángulo | Medida |
|----------------|--------|
| Central | Igual al arco |
| Inscrito | $\frac{\text{Arco}}{2}$ |
| Interior | Semisuma de arcos |
| Exterior | Semidiferencia de arcos |

---

## Semejanza

Si razón de semejanza = $k$:
- Lados: $\frac{a'}{a} = k$
- Áreas: $\frac{A'}{A} = k^2$
- Volúmenes: $\frac{V'}{V} = k^3$

---

## Volúmenes de Sólidos

| Sólido | Volumen | Área lateral |
|--------|---------|--------------|
| Prisma | $V = A_b \cdot h$ | $A_L = P_b \cdot h$ |
| Pirámide | $V = \frac{1}{3} A_b \cdot h$ | $A_L = \frac{1}{2} P_b \cdot a_p$ |
| Cilindro | $V = \pi r^2 h$ | $A_L = 2\pi r h$ |
| Cono | $V = \frac{1}{3} \pi r^2 h$ | $A_L = \pi r g$ |
| Esfera | $V = \frac{4}{3} \pi r^3$ | $A = 4\pi r^2$ |
