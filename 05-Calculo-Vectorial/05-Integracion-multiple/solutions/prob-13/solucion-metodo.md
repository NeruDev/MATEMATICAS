<!--
::METADATA::
type: solution
topic_id: cv-05-integrales-dobles-polares
file_id: prob-13-solucion
problem_ref: Prob-13
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Integral Doble en Coordenadas Polares

## Problema

Evaluar la integral doble:

$$\iint_D (x^2 + y^2) \, dA$$

donde $D$ es el disco $x^2 + y^2 \leq 4$.

---

## Conceptos clave

**Transformación a coordenadas polares:**
$$\begin{cases}
x = r\cos\theta \\
y = r\sin\theta
\end{cases}$$

**Identidad fundamental:**
$$x^2 + y^2 = r^2$$

**Jacobiano de la transformación:**
$$dA = dx\,dy = r\,dr\,d\theta$$

**[Límites](../../../../glossary.md#limites) para un disco de radio $R$ centrado en el origen:**
$$0 \leq r \leq R, \quad 0 \leq \theta \leq 2\pi$$

---

## Solución

### Paso 1: Identificar la región de integración

El disco $D: x^2 + y^2 \leq 4$ tiene:
- Centro: $(0, 0)$
- Radio: $R = 2$ (ya que $x^2 + y^2 \leq 2^2$)

---

### Paso 2: Convertir a coordenadas polares

**El integrando:**
$$x^2 + y^2 = r^2$$

**El elemento de área:**
$$dA = r \, dr \, d\theta$$

**Los [límites](../../../../glossary.md#limites) de integración:**
- $r$: desde $0$ hasta $2$
- $\theta$: desde $0$ hasta $2\pi$

---

### Paso 3: Escribir la integral en polares

$$\iint_D (x^2 + y^2) \, dA = \int_0^{2\pi} \int_0^2 r^2 \cdot r \, dr \, d\theta$$

$$= \int_0^{2\pi} \int_0^2 r^3 \, dr \, d\theta$$

---

### Paso 4: Evaluar la integral interior (respecto a $r$)

$$\int_0^2 r^3 \, dr = \left[ \frac{r^4}{4} \right]_0^2$$

$$= \frac{2^4}{4} - \frac{0^4}{4}$$

$$= \frac{16}{4} - 0$$

$$= 4$$

---

### Paso 5: Evaluar la integral exterior (respecto a $\theta$)

$$\int_0^{2\pi} 4 \, d\theta = 4 \int_0^{2\pi} d\theta$$

$$= 4 \cdot \left[ \theta \right]_0^{2\pi}$$

$$= 4 \cdot (2\pi - 0)$$

$$= 8\pi$$

---

### Paso 6: Resultado final

$$\iint_D (x^2 + y^2) \, dA = 8\pi$$

---

## Respuesta Final

$$\boxed{\iint_D (x^2 + y^2) \, dA = 8\pi}$$

---

## Verificación

**Verificación dimensional:**
- El integrando $x^2 + y^2$ tiene [dimensión](../../../../glossary.md#dimension) $[\text{longitud}]^2$
- El área $dA$ tiene [dimensión](../../../../glossary.md#dimension) $[\text{longitud}]^2$
- La integral tiene dimensión $[\text{longitud}]^4$ ✓

**Verificación por estimación:**
- Área del disco: $\pi R^2 = 4\pi$
- [Valor promedio](../../../../glossary.md#valor-promedio) de $r^2$ en el disco: entre $0$ y $4$
- El promedio ponderado de $r^2$ con densidad $r$ es $\frac{\int_0^2 r^3 \, dr}{\int_0^2 r \, dr} = \frac{4}{2} = 2$
- Estimación: $\text{promedio} \times \text{área} = 2 \times 4\pi = 8\pi$ ✓

**Verificación usando fórmula de momentos de inercia:**

La integral $\iint_D r^2 \, dA$ representa el momento de inercia polar de un disco uniforme. Para un disco de radio $R$:

$$I_0 = \int_0^{2\pi} \int_0^R r^2 \cdot r \, dr \, d\theta = 2\pi \cdot \frac{R^4}{4} = \frac{\pi R^4}{2}$$

Con $R = 2$:
$$I_0 = \frac{\pi \cdot 16}{2} = 8\pi \quad \checkmark$$
