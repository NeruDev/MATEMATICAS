<!--
::METADATA::
type: method
topic_id: cv-01-vectores-espacio
file_id: CV-01-Metodos-Vectores
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Métodos para Vectores en el Espacio

> **Objetivo:** Dominar las operaciones con vectores en $\mathbb{R}^3$ con explicaciones detalladas, cálculos intermedios y ejemplos clásicos paso a paso.

---

## Método 1: Magnitud de un Vector

### Cuándo Usar
- Calcular la "longitud" o norma de un [vector](../../../glossary.md#vector)
- Normalizar vectores (crear unitarios)

### Fórmula
$$\lVert\mathbf{v}\rVert = \sqrt{v_x^2 + v_y^2 + v_z^2}$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Identificar las componentes | $v_x$, $v_y$, $v_z$ |
| 2 | Elevar al cuadrado cada componente | $v_x^2$, $v_y^2$, $v_z^2$ |
| 3 | Sumar los cuadrados | $v_x^2 + v_y^2 + v_z^2$ |
| 4 | Sacar raíz cuadrada | $\sqrt{\text{suma}}$ |

### Ejemplo Detallado

**Problema:** Calcular la magnitud de $\mathbf{v} = \langle 3, -4, 12 \rangle$

**Paso 1:** Identificamos las componentes:
$$v_x = 3, \quad v_y = -4, \quad v_z = 12$$

**Paso 2:** Elevamos al cuadrado:
$$v_x^2 = 9, \quad v_y^2 = 16, \quad v_z^2 = 144$$

**Paso 3:** Sumamos:
$$9 + 16 + 144 = 169$$

**Paso 4:** Sacamos raíz cuadrada:
$$\lVert\mathbf{v}\rVert = \sqrt{169} = 13$$

**Resultado:** $\lVert\mathbf{v}\rVert = \boxed{13}$

---

## Método 2: Vector Unitario

### Cuándo Usar
- Obtener un [vector](../../../glossary.md#vector) de magnitud 1 en la misma dirección
- Normalizar para cálculos de proyección

### Fórmula
$$\hat{\mathbf{v}} = \frac{\mathbf{v}}{\lVert\mathbf{v}\rVert} = \left\langle \frac{v_x}{\lVert\mathbf{v}\rVert}, \frac{v_y}{\lVert\mathbf{v}\rVert}, \frac{v_z}{\lVert\mathbf{v}\rVert} \right\rangle$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Calcular $\lVert\mathbf{v}\rVert$ | Método 1 |
| 2 | Dividir cada componente por la magnitud | $\frac{v_i}{\lVert\mathbf{v}\rVert}$ |
| 3 | Verificar que $\lVert\hat{\mathbf{v}}\rVert = 1$ | Opcional |

### Ejemplo Detallado

**Problema:** Encontrar el vector unitario en la dirección de $\mathbf{v} = \langle 1, 2, 2 \rangle$

**Paso 1:** Calculamos la magnitud:
$$\lVert\mathbf{v}\rVert = \sqrt{1^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$$

**Paso 2:** Dividimos cada componente:
$$\hat{\mathbf{v}} = \frac{1}{3}\langle 1, 2, 2 \rangle = \left\langle \frac{1}{3}, \frac{2}{3}, \frac{2}{3} \right\rangle$$

**Verificación:**
$$\lVert\hat{\mathbf{v}}\rVert = \sqrt{\frac{1}{9} + \frac{4}{9} + \frac{4}{9}} = \sqrt{\frac{9}{9}} = 1 \checkmark$$

**Resultado:** $\hat{\mathbf{v}} = \boxed{\left\langle \frac{1}{3}, \frac{2}{3}, \frac{2}{3} \right\rangle}$

---

## Método 3: Producto Escalar (Punto)

### Cuándo Usar
- Calcular el ángulo entre vectores
- Determinar ortogonalidad
- Calcular trabajo

### Fórmulas
**Algebraica:** $\mathbf{u} \cdot \mathbf{v} = u_x v_x + u_y v_y + u_z v_z$

**Geométrica:** $\mathbf{u} \cdot \mathbf{v} = \lVert\mathbf{u}\rVert \lVert\mathbf{v}\rVert \cos\theta$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Multiplicar componentes correspondientes | $u_x v_x$, $u_y v_y$, $u_z v_z$ |
| 2 | Sumar los productos | $u_x v_x + u_y v_y + u_z v_z$ |

### Propiedades Importantes

| Condición | Significado |
|-----------|-------------|
| $\mathbf{u} \cdot \mathbf{v} = 0$ | Vectores **ortogonales** (perpendiculares) |
| $\mathbf{u} \cdot \mathbf{v} > 0$ | Ángulo agudo entre ellos |
| $\mathbf{u} \cdot \mathbf{v} < 0$ | Ángulo obtuso entre ellos |

### Ejemplo Detallado

**Problema:** Calcular $\mathbf{u} \cdot \mathbf{v}$ donde $\mathbf{u} = \langle 2, -1, 3 \rangle$ y $\mathbf{v} = \langle 4, 5, -2 \rangle$

**Paso 1:** Multiplicamos componentes correspondientes:
$$u_x v_x = 2 \cdot 4 = 8$$
$$u_y v_y = (-1) \cdot 5 = -5$$
$$u_z v_z = 3 \cdot (-2) = -6$$

**Paso 2:** Sumamos:
$$\mathbf{u} \cdot \mathbf{v} = 8 + (-5) + (-6) = 8 - 5 - 6 = -3$$

**Resultado:** $\mathbf{u} \cdot \mathbf{v} = \boxed{-3}$

**Interpretación:** Como el producto es negativo, el ángulo entre los vectores es obtuso (mayor que 90°).

---

## Método 4: Ángulo entre Vectores

### Cuándo Usar
- Encontrar el ángulo $\theta$ entre dos vectores
- Verificar perpendicularidad o paralelismo

### Fórmula
$$\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert\mathbf{u}\rVert \lVert\mathbf{v}\rVert}$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Calcular $\mathbf{u} \cdot \mathbf{v}$ | Método 3 |
| 2 | Calcular $\lVert\mathbf{u}\rVert$ | Método 1 |
| 3 | Calcular $\lVert\mathbf{v}\rVert$ | Método 1 |
| 4 | Dividir | $\frac{\mathbf{u} \cdot \mathbf{v}}{\lVert\mathbf{u}\rVert \lVert\mathbf{v}\rVert}$ |
| 5 | Aplicar $\arccos$ | $\theta = \arccos(\text{resultado})$ |

### Ejemplo Detallado

**Problema:** Encontrar el ángulo entre $\mathbf{u} = \langle 1, 0, 1 \rangle$ y $\mathbf{v} = \langle 0, 1, 1 \rangle$

**Paso 1:** Calculamos el producto escalar:
$$\mathbf{u} \cdot \mathbf{v} = (1)(0) + (0)(1) + (1)(1) = 0 + 0 + 1 = 1$$

**Paso 2:** Calculamos $\lVert\mathbf{u}\rVert$:
$$\lVert\mathbf{u}\rVert = \sqrt{1 + 0 + 1} = \sqrt{2}$$

**Paso 3:** Calculamos $\lVert\mathbf{v}\rVert$:
$$\lVert\mathbf{v}\rVert = \sqrt{0 + 1 + 1} = \sqrt{2}$$

**Paso 4:** Calculamos $\cos\theta$:
$$\cos\theta = \frac{1}{\sqrt{2} \cdot \sqrt{2}} = \frac{1}{2}$$

**Paso 5:** Encontramos $\theta$:
$$\theta = \arccos\left(\frac{1}{2}\right) = \frac{\pi}{3} = 60°$$

**Resultado:** El ángulo es $\boxed{60°}$ o $\boxed{\frac{\pi}{3}}$ radianes.

---

## Método 5: Producto Vectorial (Cruz)

### Cuándo Usar
- Encontrar un vector perpendicular a otros dos
- Calcular el área de un paralelogramo
- Calcular torque

### Fórmula (Determinante)
$$\mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_x & u_y & u_z \\ v_x & v_y & v_z \end{vmatrix}$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Componente $\mathbf{i}$ | $u_y v_z - u_z v_y$ |
| 2 | Componente $\mathbf{j}$ | $-(u_x v_z - u_z v_x)$ |
| 3 | Componente $\mathbf{k}$ | $u_x v_y - u_y v_x$ |
| 4 | Formar el vector | $\langle \text{paso 1}, \text{paso 2}, \text{paso 3} \rangle$ |

### Regla Mnemotécnica
```
     | i    j    k  |
u×v= | u_x  u_y  u_z |
     | v_x  v_y  v_z |

i: "cubro i, hago u_y·v_z - u_z·v_y"
j: "cubro j, hago -(u_x·v_z - u_z·v_x)"  ← ¡signo negativo!
k: "cubro k, hago u_x·v_y - u_y·v_x"
```

### Ejemplo Detallado

**Problema:** Calcular $\mathbf{u} \times \mathbf{v}$ donde $\mathbf{u} = \langle 1, 2, 3 \rangle$ y $\mathbf{v} = \langle 4, 5, 6 \rangle$

**Paso 1:** Componente $\mathbf{i}$:
$$u_y v_z - u_z v_y = (2)(6) - (3)(5) = 12 - 15 = -3$$

**Paso 2:** Componente $\mathbf{j}$:
$$-(u_x v_z - u_z v_x) = -[(1)(6) - (3)(4)] = -[6 - 12] = -(-6) = 6$$

**Paso 3:** Componente $\mathbf{k}$:
$$u_x v_y - u_y v_x = (1)(5) - (2)(4) = 5 - 8 = -3$$

**Paso 4:** Formamos el vector:
$$\mathbf{u} \times \mathbf{v} = \langle -3, 6, -3 \rangle$$

**Verificación de perpendicularidad:**
$$(\mathbf{u} \times \mathbf{v}) \cdot \mathbf{u} = (-3)(1) + (6)(2) + (-3)(3) = -3 + 12 - 9 = 0 \checkmark$$

**Resultado:** $\mathbf{u} \times \mathbf{v} = \boxed{\langle -3, 6, -3 \rangle}$

---

## Método 6: Área del Paralelogramo

### Cuándo Usar
- Calcular el área del paralelogramo formado por dos vectores

### Fórmula
$$\text{Área} = \lVert\mathbf{u} \times \mathbf{v}\rVert$$

### Algoritmo de Resolución

| Paso | Acción | Método |
|------|--------|--------|
| 1 | Calcular $\mathbf{u} \times \mathbf{v}$ | Método 5 |
| 2 | Calcular la magnitud del resultado | Método 1 |

### Ejemplo Detallado

**Problema:** Encontrar el área del paralelogramo con lados $\mathbf{u} = \langle 3, 0, 0 \rangle$ y $\mathbf{v} = \langle 0, 4, 0 \rangle$

**Paso 1:** Calculamos $\mathbf{u} \times \mathbf{v}$:
$$\mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 3 & 0 & 0 \\ 0 & 4 & 0 \end{vmatrix}$$

- Componente $\mathbf{i}$: $(0)(0) - (0)(4) = 0$
- Componente $\mathbf{j}$: $-[(3)(0) - (0)(0)] = 0$
- Componente $\mathbf{k}$: $(3)(4) - (0)(0) = 12$

$$\mathbf{u} \times \mathbf{v} = \langle 0, 0, 12 \rangle$$

**Paso 2:** Calculamos la magnitud:
$$\lVert\mathbf{u} \times \mathbf{v}\rVert = \sqrt{0 + 0 + 144} = 12$$

**Resultado:** El área es $\boxed{12}$ unidades cuadradas.

> **Nota:** Como esperábamos, el área del rectángulo $3 \times 4 = 12$ ✓

---

## Método 7: Proyección de un Vector sobre Otro

### Cuándo Usar
- Descomponer un vector en componentes paralela y perpendicular
- Calcular trabajo en física

### Fórmulas

**Componente escalar (longitud con signo):**
$$\text{comp}_{\mathbf{v}}\mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert\mathbf{v}\rVert}$$

**Proyección vectorial:**
$$\text{proy}_{\mathbf{v}}\mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert\mathbf{v}\rVert^2}\mathbf{v}$$

### Algoritmo de Resolución

| Paso | Acción | Para escalar | Para vectorial |
|------|--------|--------------|----------------|
| 1 | Calcular $\mathbf{u} \cdot \mathbf{v}$ | ✓ | ✓ |
| 2 | Calcular $\lVert\mathbf{v}\rVert$ | ✓ | ✓ |
| 3 | Dividir | $\frac{\mathbf{u} \cdot \mathbf{v}}{\lVert\mathbf{v}\rVert}$ | $\frac{\mathbf{u} \cdot \mathbf{v}}{\lVert\mathbf{v}\rVert^2}$ |
| 4 | Multiplicar por $\mathbf{v}$ | — | ✓ |

### Ejemplo Detallado

**Problema:** Proyectar $\mathbf{u} = \langle 3, 4, 0 \rangle$ sobre $\mathbf{v} = \langle 1, 0, 0 \rangle$

**Paso 1:** Calculamos $\mathbf{u} \cdot \mathbf{v}$:
$$\mathbf{u} \cdot \mathbf{v} = (3)(1) + (4)(0) + (0)(0) = 3$$

**Paso 2:** Calculamos $\lVert\mathbf{v}\rVert$:
$$\lVert\mathbf{v}\rVert = \sqrt{1 + 0 + 0} = 1$$

**Paso 3a:** Componente escalar:
$$\text{comp}_{\mathbf{v}}\mathbf{u} = \frac{3}{1} = 3$$

**Paso 3b:** Proyección vectorial:
$$\text{proy}_{\mathbf{v}}\mathbf{u} = \frac{3}{1^2}\langle 1, 0, 0 \rangle = 3\langle 1, 0, 0 \rangle = \langle 3, 0, 0 \rangle$$

**Resultado:** 
- Componente escalar: $\boxed{3}$
- Proyección vectorial: $\boxed{\langle 3, 0, 0 \rangle}$

**Interpretación:** La "sombra" de $\mathbf{u}$ sobre el eje $x$ tiene longitud 3.

---

## Método 8: Ecuación de una Recta en el Espacio

### Cuándo Usar
- Encontrar la recta que pasa por un punto con dirección dada
- Encontrar la recta que pasa por dos puntos

### Formas de la Ecuación

| Forma | Ecuación |
|-------|----------|
| Vectorial | $\mathbf{r}(t) = \mathbf{r}_0 + t\mathbf{v}$ |
| Paramétrica | $x = x_0 + at$, $y = y_0 + bt$, $z = z_0 + ct$ |
| Simétrica | $\frac{x-x_0}{a} = \frac{y-y_0}{b} = \frac{z-z_0}{c}$ |

### Algoritmo de Resolución

| Paso | Acción | Información necesaria |
|------|--------|----------------------|
| 1 | Identificar un punto $P_0(x_0, y_0, z_0)$ | Punto en la recta |
| 2 | Encontrar vector dirección $\mathbf{v} = \langle a, b, c \rangle$ | Si hay 2 puntos: $\mathbf{v} = P_1 - P_0$ |
| 3 | Escribir en la forma deseada | Sustituir valores |

### Ejemplo Detallado

**Problema:** Encontrar la ecuación de la recta que pasa por $P(1, 2, 3)$ y $Q(4, -1, 2)$

**Paso 1:** Tomamos $P_0 = P = (1, 2, 3)$

**Paso 2:** Calculamos el vector dirección:
$$\mathbf{v} = Q - P = \langle 4-1, -1-2, 2-3 \rangle = \langle 3, -3, -1 \rangle$$

**Paso 3:** Escribimos las ecuaciones:

**Forma vectorial:**
$$\mathbf{r}(t) = \langle 1, 2, 3 \rangle + t\langle 3, -3, -1 \rangle$$

**Forma paramétrica:**
$$x = 1 + 3t, \quad y = 2 - 3t, \quad z = 3 - t$$

**Forma simétrica:**
$$\frac{x-1}{3} = \frac{y-2}{-3} = \frac{z-3}{-1}$$

---

## Método 9: Ecuación de un Plano

### Cuándo Usar
- Encontrar el plano con vector normal dado que pasa por un punto
- Encontrar el plano que contiene tres puntos

### Formas de la Ecuación

| Forma | Ecuación |
|-------|----------|
| Normal | $\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0$ |
| General | $ax + by + cz = d$ donde $\mathbf{n} = \langle a, b, c \rangle$ |

### Algoritmo de Resolución (dado vector normal y punto)

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Identificar $\mathbf{n} = \langle a, b, c \rangle$ | Vector normal |
| 2 | Identificar $P_0(x_0, y_0, z_0)$ | Punto en el plano |
| 3 | Calcular $d = ax_0 + by_0 + cz_0$ | Constante |
| 4 | Escribir $ax + by + cz = d$ | Ecuación final |

### Ejemplo Detallado

**Problema:** Encontrar el plano con normal $\mathbf{n} = \langle 2, -1, 3 \rangle$ que pasa por $P(1, 4, -2)$

**Paso 1:** Tenemos $\mathbf{n} = \langle 2, -1, 3 \rangle$

**Paso 2:** Tenemos $P_0 = (1, 4, -2)$

**Paso 3:** Calculamos $d$:
$$d = (2)(1) + (-1)(4) + (3)(-2) = 2 - 4 - 6 = -8$$

**Paso 4:** Escribimos la ecuación:
$$2x - y + 3z = -8$$

**Verificación:** Sustituimos $P(1, 4, -2)$:
$$2(1) - 4 + 3(-2) = 2 - 4 - 6 = -8 \checkmark$$

**Resultado:** $\boxed{2x - y + 3z = -8}$

---

## Método 10: Distancia de un Punto a un Plano

### Cuándo Usar
- Calcular la distancia perpendicular de un punto a un plano

### Fórmula
$$D = \frac{|ax_1 + by_1 + cz_1 - d|}{\sqrt{a^2 + b^2 + c^2}}$$

donde el plano es $ax + by + cz = d$ y el punto es $(x_1, y_1, z_1)$.

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Identificar coeficientes del plano | $a$, $b$, $c$, $d$ |
| 2 | Sustituir el punto en $ax + by + cz - d$ | Valor con signo |
| 3 | Tomar valor absoluto | $\vert ax_1 + by_1 + cz_1 - d\vert$ |
| 4 | Calcular $\sqrt{a^2 + b^2 + c^2}$ | Magnitud del normal |
| 5 | Dividir | Distancia final |

### Ejemplo Detallado

**Problema:** Encontrar la distancia del punto $P(2, 3, 1)$ al plano $2x - 2y + z = 5$

**Paso 1:** Identificamos: $a = 2$, $b = -2$, $c = 1$, $d = 5$

**Paso 2:** Sustituimos el punto:
$$ax_1 + by_1 + cz_1 - d = 2(2) + (-2)(3) + 1(1) - 5$$
$$= 4 - 6 + 1 - 5 = -6$$

**Paso 3:** Tomamos valor absoluto:
$$|-6| = 6$$

**Paso 4:** Calculamos la magnitud del normal:
$$\sqrt{2^2 + (-2)^2 + 1^2} = \sqrt{4 + 4 + 1} = \sqrt{9} = 3$$

**Paso 5:** Dividimos:
$$D = \frac{6}{3} = 2$$

**Resultado:** La distancia es $\boxed{2}$ unidades.

---

## Método 11: Triple Producto Escalar (Volumen)

### Cuándo Usar
- Calcular el volumen de un paralelepípedo
- Determinar si tres vectores son coplanares

### Fórmula
$$\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = \begin{vmatrix} u_x & u_y & u_z \\ v_x & v_y & v_z \\ w_x & w_y & w_z \end{vmatrix}$$

### Propiedades

| Valor | Significado |
|-------|-------------|
| $\neq 0$ | Vectores **no coplanares** |
| $= 0$ | Vectores **coplanares** |
| $\vert\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})\vert$ | Volumen del paralelepípedo |

### Algoritmo de Resolución

| Paso | Acción | Método |
|------|--------|--------|
| 1 | Calcular $\mathbf{v} \times \mathbf{w}$ | Método 5 |
| 2 | Calcular $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})$ | Método 3 |
| 3 | Si se pide volumen, tomar valor absoluto | $\lvert \text{resultado} \rvert$ |

### Ejemplo Detallado

**Problema:** Calcular el volumen del paralelepípedo formado por:
$\mathbf{u} = \langle 1, 0, 0 \rangle$, $\mathbf{v} = \langle 0, 2, 0 \rangle$, $\mathbf{w} = \langle 0, 0, 3 \rangle$

**Paso 1:** Calculamos $\mathbf{v} \times \mathbf{w}$:
$$\mathbf{v} \times \mathbf{w} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{vmatrix} = \langle 6, 0, 0 \rangle$$

**Paso 2:** Calculamos el triple producto:
$$\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = \langle 1, 0, 0 \rangle \cdot \langle 6, 0, 0 \rangle = 6$$

**Paso 3:** El volumen es:
$$V = |6| = 6$$

**Resultado:** El volumen es $\boxed{6}$ unidades cúbicas.

> **Verificación:** Es el paralelepípedo con aristas $1 \times 2 \times 3 = 6$ ✓
