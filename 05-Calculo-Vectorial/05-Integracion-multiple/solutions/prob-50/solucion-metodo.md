<!--
::METADATA::
type: solution
topic_id: cv-05-integral-gaussiana
file_id: prob-50-solucion
problem_ref: Prob-50
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: La Integral Gaussiana

## Problema

Calcular la [integral impropia](../../../..](../../../../glossary.md)#integral-impropia):

$$I = \int_0^{\infty} e^{-x^2} \, dx$$

utilizando una integral doble en $\mathbb{R}^2$ y coordenadas polares.

---

## Conceptos clave

**Técnica de Poisson:** Calcular $I^2$ como integral doble y luego tomar raíz cuadrada.

**Coordenadas polares:**
$$\begin{cases}
x = r\cos\theta \\
y = r\sin\theta \\
x^2 + y^2 = r^2
\end{cases}$$

**Jacobiano:** $dA = r \, dr \, d\theta$

**Integral exponencial fundamental:**
$$\int e^{-ar^2} \cdot r \, dr = -\frac{1}{2a} e^{-ar^2} + C$$

---

## Solución

### Paso 1: Definir $I$ y plantear $I^2$

Sea:
$$I = \int_0^{\infty} e^{-x^2} \, dx$$

Consideramos también la integral equivalente en variable $y$:
$$I = \int_0^{\infty} e^{-y^2} \, dy$$

Multiplicamos ambas integrales:

$$I^2 = \left( \int_0^{\infty} e^{-x^2} \, dx \right) \cdot \left( \int_0^{\infty} e^{-y^2} \, dy \right)$$

---

### Paso 2: Convertir el producto en integral doble

Por el teorema de Fubini, el producto de integrales se convierte en una integral doble:

$$I^2 = \int_0^{\infty} \int_0^{\infty} e^{-x^2} \cdot e^{-y^2} \, dx \, dy$$

$$I^2 = \int_0^{\infty} \int_0^{\infty} e^{-(x^2 + y^2)} \, dx \, dy$$

Esta integral doble se extiende sobre el primer cuadrante del plano $xy$.

---

### Paso 3: Cambiar a coordenadas polares

**[Sustitución](../../../..](../../../../glossary.md)#sustitucion):**
- $x^2 + y^2 = r^2$
- $dx \, dy = r \, dr \, d\theta$

**Región de integración:**
- El primer cuadrante corresponde a $0 \leq \theta \leq \frac{\pi}{2}$
- La distancia al origen va de $0$ a $\infty$: $0 \leq r < \infty$

La integral se transforma en:

$$I^2 = \int_0^{\pi/2} \int_0^{\infty} e^{-r^2} \cdot r \, dr \, d\theta$$

---

### Paso 4: Separar las integrales

Como el integrando se factoriza:

$$I^2 = \int_0^{\pi/2} d\theta \cdot \int_0^{\infty} r \, e^{-r^2} \, dr$$

---

### Paso 5: Evaluar la integral angular

$$\int_0^{\pi/2} d\theta = \left[ \theta \right]_0^{\pi/2} = \frac{\pi}{2} - 0 = \frac{\pi}{2}$$

---

### Paso 6: Evaluar la integral radial

Para $\int_0^{\infty} r \, e^{-r^2} \, dr$, usamos [sustitución](../../../..](../../../../glossary.md)#sustitucion):

Sea $u = r^2$, entonces $du = 2r \, dr$, por lo tanto $r \, dr = \frac{1}{2} du$

**Cambio de [límites](../../../..](../../../../glossary.md)#limites):**
- Cuando $r = 0$: $u = 0$
- Cuando $r \to \infty$: $u \to \infty$

$$\int_0^{\infty} r \, e^{-r^2} \, dr = \int_0^{\infty} e^{-u} \cdot \frac{1}{2} \, du$$

$$= \frac{1}{2} \int_0^{\infty} e^{-u} \, du$$

$$= \frac{1}{2} \left[ -e^{-u} \right]_0^{\infty}$$

$$= \frac{1}{2} \left( \lim_{u \to \infty} (-e^{-u}) - (-e^{0}) \right)$$

$$= \frac{1}{2} \left( 0 - (-1) \right)$$

$$= \frac{1}{2} \cdot 1 = \frac{1}{2}$$

---

### Paso 7: Calcular $I^2$

$$I^2 = \frac{\pi}{2} \cdot \frac{1}{2} = \frac{\pi}{4}$$

---

### Paso 8: Obtener $I$

Como $I > 0$ (el integrando es positivo):

$$I = \sqrt{I^2} = \sqrt{\frac{\pi}{4}} = \frac{\sqrt{\pi}}{2}$$

---

## Respuesta Final

$$\boxed{\int_0^{\infty} e^{-x^2} \, dx = \frac{\sqrt{\pi}}{2}}$$

**Forma alternativa (integral sobre toda la recta):**

$$\boxed{\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}}$$

---

## Verificación

**Verificación numérica:**

El valor numérico es:
$$\frac{\sqrt{\pi}}{2} \approx \frac{1.7724...}{2} \approx 0.8862...$$

Esto coincide con tablas de la [función](../../../..](../../../../glossary.md)#funcion) error y valores computados numéricamente.

---

**Relación con la [función](../../../..](../../../../glossary.md)#funcion) error:**

La función error se define como:
$$\text{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2} \, dt$$

Cuando $x \to \infty$:
$$\text{erf}(\infty) = \frac{2}{\sqrt{\pi}} \cdot \frac{\sqrt{\pi}}{2} = 1 \quad \checkmark$$

---

**[Generalización](../../../..](../../../../glossary.md)#generalizacion) (Integral Gaussiana general):**

Para $a > 0$:
$$\int_0^{\infty} e^{-ax^2} \, dx = \frac{1}{2}\sqrt{\frac{\pi}{a}}$$

Con $a = 1$, recuperamos nuestro resultado:
$$\int_0^{\infty} e^{-x^2} \, dx = \frac{1}{2}\sqrt{\pi} = \frac{\sqrt{\pi}}{2} \quad \checkmark$$

---

**Importancia histórica:**

Esta integral, conocida como la **integral de Gauss** o **integral gaussiana**, fue calculada por primera vez por Laplace en 1774 usando este mismo método de la integral doble. Es fundamental en:

- Teoría de probabilidad (distribución normal)
- Física cuántica (funciones de onda)
- Teoría del calor
- Procesamiento de señales
