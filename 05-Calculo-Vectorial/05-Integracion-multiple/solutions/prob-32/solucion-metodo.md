<!--
::METADATA::
type: solution
topic_id: cv-05-integrales-triples-cilindricas
file_id: prob-32-solucion
problem_ref: Prob-32
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Volumen con Coordenadas Cilíndricas

## Problema

Calcular el volumen del sólido acotado entre el paraboloide $z = x^2 + y^2$ y el plano $z = 4$.

---

## Conceptos clave

**Coordenadas cilíndricas:**
$$\begin{cases}
x = r\cos\theta \\
y = r\sin\theta \\
z = z
\end{cases}$$

**Relación fundamental:**
$$x^2 + y^2 = r^2$$

**Jacobiano (elemento de volumen):**
$$dV = r \, dr \, d\theta \, dz$$

**Fórmula del volumen:**
$$V = \iiint_E dV$$

---

## Solución

### Paso 1: Visualizar y describir el sólido

El sólido está limitado por:
- **Abajo:** El paraboloide $z = x^2 + y^2 = r^2$
- **Arriba:** El plano horizontal $z = 4$

La intersección ocurre cuando:
$$r^2 = 4 \Rightarrow r = 2$$

Esto forma un círculo de radio 2 en el plano $z = 4$.

---

### Paso 2: Determinar los límites de integración

**En coordenadas cilíndricas:**

- **$\theta$:** Da la vuelta completa → $0 \leq \theta \leq 2\pi$
- **$r$:** Desde el eje $z$ hasta la intersección → $0 \leq r \leq 2$
- **$z$:** Desde el paraboloide hasta el plano → $r^2 \leq z \leq 4$

---

### Paso 3: Plantear la integral triple

$$V = \int_0^{2\pi} \int_0^2 \int_{r^2}^{4} r \, dz \, dr \, d\theta$$

---

### Paso 4: Evaluar la integral interior (respecto a $z$)

$$\int_{r^2}^{4} r \, dz = r \int_{r^2}^{4} dz = r \cdot [z]_{r^2}^{4}$$

$$= r \cdot (4 - r^2)$$

$$= 4r - r^3$$

---

### Paso 5: Evaluar la integral media (respecto a $r$)

$$\int_0^2 (4r - r^3) \, dr = \int_0^2 4r \, dr - \int_0^2 r^3 \, dr$$

$$= 4 \cdot \left[ \frac{r^2}{2} \right]_0^2 - \left[ \frac{r^4}{4} \right]_0^2$$

$$= 4 \cdot \left( \frac{4}{2} - 0 \right) - \left( \frac{16}{4} - 0 \right)$$

$$= 4 \cdot 2 - 4$$

$$= 8 - 4$$

$$= 4$$

---

### Paso 6: Evaluar la integral exterior (respecto a $\theta$)

$$V = \int_0^{2\pi} 4 \, d\theta = 4 \cdot [\theta]_0^{2\pi}$$

$$= 4 \cdot (2\pi - 0)$$

$$= 8\pi$$

---

## Respuesta Final

$$\boxed{V = 8\pi}$$

---

## Verificación

**Método alternativo: Integral doble con altura**

El volumen también se puede calcular como:

$$V = \iint_D (z_{\text{sup}} - z_{\text{inf}}) \, dA = \iint_D (4 - r^2) \, dA$$

En polares, con $D$ siendo el disco $r \leq 2$:

$$V = \int_0^{2\pi} \int_0^2 (4 - r^2) \cdot r \, dr \, d\theta$$

$$= \int_0^{2\pi} \int_0^2 (4r - r^3) \, dr \, d\theta$$

$$= \int_0^{2\pi} 4 \, d\theta = 8\pi \quad \checkmark$$

---

**Verificación por comparación:**

El cilindro de radio 2 y altura 4 tiene volumen:
$$V_{\text{cilindro}} = \pi r^2 h = \pi \cdot 4 \cdot 4 = 16\pi$$

El paraboloide ocupa la mitad inferior del cilindro (aproximadamente). El volumen bajo el paraboloide hasta $z = 4$ es:

$$V_{\text{paraboloide}} = \int_0^{2\pi} \int_0^2 \int_0^{r^2} r \, dz \, dr \, d\theta = \int_0^{2\pi} \int_0^2 r^3 \, dr \, d\theta$$

$$= 2\pi \cdot \left[ \frac{r^4}{4} \right]_0^2 = 2\pi \cdot 4 = 8\pi$$

Por lo tanto:
$$V_{\text{sólido}} = V_{\text{cilindro}} - V_{\text{paraboloide}} = 16\pi - 8\pi = 8\pi \quad \checkmark$$

---

**Interpretación geométrica:**

El sólido es como un "tazón" invertido. Su volumen de $8\pi$ unidades cúbicas es exactamente la mitad del volumen del cilindro circunscrito, lo cual es una propiedad conocida de los paraboloides de revolución.
