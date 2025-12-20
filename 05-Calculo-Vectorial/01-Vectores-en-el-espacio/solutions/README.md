# Soluciones — Vectores en el espacio

<!--
IA: Cada solución incluye:
1. Breve contexto del concepto/método aplicado
2. Desarrollo paso a paso
3. Respuesta final destacada
Esto facilita el aprendizaje guiado.
-->

---

## Nivel básico

### Problema 1
**Contexto**: Usamos la fórmula de magnitud en $\mathbb{R}^3$ y la definición de vector unitario (dividir por la magnitud).

**Desarrollo**:
$$\lVert \mathbf{v} \rVert = \sqrt{3^2 + (-4)^2 + 12^2} = \sqrt{9 + 16 + 144} = \sqrt{169} = 13$$

$$\hat{\mathbf{v}} = \frac{\mathbf{v}}{\lVert \mathbf{v} \rVert} = \frac{1}{13}\langle 3, -4, 12 \rangle = \left\langle \frac{3}{13}, -\frac{4}{13}, \frac{12}{13} \right\rangle$$

**Respuesta**: $\lVert \mathbf{v} \rVert = 13$; $\hat{\mathbf{v}} = \langle 3/13, -4/13, 12/13 \rangle$

---

### Problema 2
**Contexto**: El vector entre dos puntos se obtiene restando coordenadas (punto final menos inicial).

**Desarrollo**:
$$\overrightarrow{AB} = B - A = \langle 4-1, 6-2, 3-3 \rangle = \langle 3, 4, 0 \rangle$$
$$\lVert \overrightarrow{AB} \rVert = \sqrt{9 + 16 + 0} = \sqrt{25} = 5$$

**Respuesta**: La distancia entre $A$ y $B$ es $5$.

---

### Problema 3
**Contexto**: Un vector es unitario si su magnitud es 1. Si no lo es, lo normalizamos.

**Desarrollo**:
$$\lVert \mathbf{u} \rVert = \sqrt{4 + 1 + 4} = \sqrt{9} = 3 \neq 1$$

No es unitario. Vector unitario:
$$\hat{\mathbf{u}} = \frac{1}{3}\langle 2, -1, 2 \rangle = \left\langle \frac{2}{3}, -\frac{1}{3}, \frac{2}{3} \right\rangle$$

**Respuesta**: No es unitario; $\hat{\mathbf{u}} = \langle 2/3, -1/3, 2/3 \rangle$

---

### Problema 4
**Contexto**: Las operaciones con vectores se realizan componente a componente.

**Desarrollo**:
- a) $\mathbf{a} + \mathbf{b} = \langle 1+4, -2+0, 3-1 \rangle = \langle 5, -2, 2 \rangle$
- b) $2\mathbf{a} - 3\mathbf{b} = \langle 2-12, -4-0, 6+3 \rangle = \langle -10, -4, 9 \rangle$
- c) $\mathbf{a} - \mathbf{b} = \langle -3, -2, 4 \rangle$; $\lVert \mathbf{a} - \mathbf{b} \rVert = \sqrt{9+4+16} = \sqrt{29}$

**Respuestas**: a) $\langle 5, -2, 2 \rangle$; b) $\langle -10, -4, 9 \rangle$; c) $\sqrt{29}$

---

### Problema 5
**Contexto**: Para obtener un vector de magnitud específica en una dirección dada, normalizamos y escalamos.

**Desarrollo**:
$$\lVert \mathbf{v} \rVert = \sqrt{1 + 4 + 4} = 3$$
$$\hat{\mathbf{v}} = \frac{1}{3}\langle 1, 2, 2 \rangle$$

Vector de magnitud 10:
$$10\hat{\mathbf{v}} = \frac{10}{3}\langle 1, 2, 2 \rangle = \left\langle \frac{10}{3}, \frac{20}{3}, \frac{20}{3} \right\rangle$$

**Respuesta**: $\langle 10/3, 20/3, 20/3 \rangle$

---

## Nivel intermedio

### Problema 6
**Contexto**: El ángulo entre vectores se obtiene con el producto escalar y la fórmula del coseno.

**Desarrollo**:
$$\mathbf{u} \cdot \mathbf{v} = 1(2) + 2(-1) + (-1)(2) = 2 - 2 - 2 = -2$$
$$\lVert \mathbf{u} \rVert = \sqrt{6}, \quad \lVert \mathbf{v} \rVert = 3$$
$$\cos\theta = \frac{-2}{3\sqrt{6}} = -\frac{\sqrt{6}}{9}$$
$$\theta = \arccos\left(-\frac{\sqrt{6}}{9}\right) \approx 99.6°$$

**Respuesta**: $\theta \approx 99.6°$ (ángulo obtuso)

---

### Problema 7
**Contexto**: Ortogonales si $\mathbf{a} \cdot \mathbf{b} = 0$; paralelos si uno es múltiplo escalar del otro.

**Desarrollo**:
$$\mathbf{a} \cdot \mathbf{b} = 3(1) + (-1)(1) + 2(-1) = 3 - 1 - 2 = 0$$

**Respuesta**: Son ortogonales (perpendiculares).

---

### Problema 8
**Contexto**: Dos vectores son perpendiculares cuando su producto escalar es cero.

**Desarrollo**:
$$\mathbf{u} \cdot \mathbf{v} = 2(1) + k(-3) + (-1)(2) = 2 - 3k - 2 = -3k = 0$$
$$k = 0$$

**Respuesta**: $k = 0$

---

### Problema 9
**Contexto**: La proyección vectorial usa la fórmula $\text{proy}_{\mathbf{v}}\mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{v} \rVert^2}\mathbf{v}$.

**Desarrollo**:
$$\mathbf{u} \cdot \mathbf{v} = 12 + 3 + 4 = 19$$
$$\lVert \mathbf{v} \rVert^2 = 4 + 1 + 4 = 9$$
$$\text{proy}_{\mathbf{v}}\mathbf{u} = \frac{19}{9}\langle 2, 1, 2 \rangle = \left\langle \frac{38}{9}, \frac{19}{9}, \frac{38}{9} \right\rangle$$

**Respuesta**: $\langle 38/9, 19/9, 38/9 \rangle$

---

### Problema 10
**Contexto**: La componente de fuerza en una dirección es la proyección escalar.

**Desarrollo**:
$$\text{comp}_{\mathbf{d}}\mathbf{F} = \frac{\mathbf{F} \cdot \mathbf{d}}{\lVert \mathbf{d} \rVert} = \frac{4(1) + 3(0) + 0(0)}{1} = 4 \text{ N}$$

**Respuesta**: $4$ N en la dirección $x$.

---

### Problema 11
**Contexto**: El producto vectorial se calcula mediante el determinante 3×3 con los vectores canónicos.

**Desarrollo**:
$$\mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & -1 \\ 2 & -1 & 2 \end{vmatrix}$$
- $\mathbf{i}$: $(2)(2) - (-1)(-1) = 4 - 1 = 3$
- $\mathbf{j}$: $-[(1)(2) - (-1)(2)] = -(2 + 2) = -4$
- $\mathbf{k}$: $(1)(-1) - (2)(2) = -1 - 4 = -5$

**Respuesta**: $\mathbf{u} \times \mathbf{v} = \langle 3, -4, -5 \rangle$

---

### Problema 12
**Contexto**: El área del triángulo es la mitad de la magnitud del producto vectorial de dos lados.

**Desarrollo**:
$$\overrightarrow{AB} = \langle -1, 2, 0 \rangle, \quad \overrightarrow{AC} = \langle -1, 0, 3 \rangle$$
$$\overrightarrow{AB} \times \overrightarrow{AC} = \langle 6, 3, 2 \rangle$$
$$\lVert \overrightarrow{AB} \times \overrightarrow{AC} \rVert = \sqrt{36 + 9 + 4} = 7$$
$$\text{Área} = \frac{7}{2} = 3.5$$

**Respuesta**: Área $= 3.5$ unidades cuadradas.

---

### Problema 13
**Contexto**: Un vector perpendicular a dos vectores es su producto vectorial; normalizamos para hacerlo unitario.

**Desarrollo**:
$$\mathbf{a} \times \mathbf{b} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{vmatrix} = \langle 1, -1, 1 \rangle$$
$$\lVert \mathbf{a} \times \mathbf{b} \rVert = \sqrt{3}$$
$$\hat{\mathbf{n}} = \frac{1}{\sqrt{3}}\langle 1, -1, 1 \rangle = \left\langle \frac{1}{\sqrt{3}}, -\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}} \right\rangle$$

**Respuesta**: $\hat{\mathbf{n}} = \langle 1/\sqrt{3}, -1/\sqrt{3}, 1/\sqrt{3} \rangle$ (o su opuesto)

---

## Nivel avanzado

### Problema 14
**Contexto**: La recta se escribe en forma vectorial, luego se separan las componentes para la paramétrica y se despeja $t$ para la simétrica.

**Desarrollo**:
- Forma paramétrica: $x = 1 + 2t$, $y = t$, $z = 2 - t$
- Forma simétrica: $\frac{x-1}{2} = \frac{y}{1} = \frac{z-2}{-1}$

**Respuesta**: Paramétrica: $(x, y, z) = (1+2t, t, 2-t)$; Simétrica: $\frac{x-1}{2} = y = \frac{z-2}{-1}$

---

### Problema 15
**Contexto**: Comparamos direcciones (paralelas si proporcionales) y verificamos si comparten puntos.

**Desarrollo**:
$\mathbf{v}_2 = \langle 2, -2, 4 \rangle = 2\langle 1, -1, 2 \rangle = 2\mathbf{v}_1$

Las direcciones son proporcionales → rectas paralelas o coincidentes.

¿Está $(3, 0, 1)$ en $L_1$? Sustituimos en $L_1$:
- $3 = 1 + t \Rightarrow t = 2$
- $0 = 2 - t \Rightarrow t = 2$ ✓
- $1 = 3 + 2t \Rightarrow t = -1$ ✗

**Respuesta**: Las rectas son paralelas (no coincidentes).

---

### Problema 16
**Contexto**: Sustituimos las ecuaciones paramétricas en el plano y resolvemos para $t$.

**Desarrollo**:
$$2(1+2t) - t + 2(2-t) = 5$$
$$2 + 4t - t + 4 - 2t = 5$$
$$6 + t = 5 \Rightarrow t = -1$$

Punto: $(1-2, -1, 2+1) = (-1, -1, 3)$

**Respuesta**: Punto de intersección $(-1, -1, 3)$

---

### Problema 17
**Contexto**: El plano por tres puntos tiene normal igual al producto vectorial de dos vectores en el plano.

**Desarrollo**:
$$\overrightarrow{AB} = \langle 1, -1, 0 \rangle, \quad \overrightarrow{AC} = \langle 0, 1, -1 \rangle$$
$$\mathbf{n} = \overrightarrow{AB} \times \overrightarrow{AC} = \langle 1, 1, 1 \rangle$$

Usando $A = (1, 1, 1)$:
$$1(x-1) + 1(y-1) + 1(z-1) = 0$$
$$x + y + z = 3$$

**Respuesta**: $x + y + z = 3$

---

### Problema 18
**Contexto**: Aplicamos la fórmula de distancia punto-plano.

**Desarrollo**:
$$D = \frac{|1(3) + 2(-1) + (-2)(4) - 7|}{\sqrt{1 + 4 + 4}} = \frac{|3 - 2 - 8 - 7|}{3} = \frac{|-14|}{3} = \frac{14}{3}$$

**Respuesta**: $D = 14/3 \approx 4.67$

---

### Problema 19
**Contexto**: El ángulo entre planos es el ángulo entre sus vectores normales.

**Desarrollo**:
$$\mathbf{n}_1 = \langle 2, -1, 1 \rangle, \quad \mathbf{n}_2 = \langle 1, 1, 2 \rangle$$
$$\mathbf{n}_1 \cdot \mathbf{n}_2 = 2 - 1 + 2 = 3$$
$$\lVert \mathbf{n}_1 \rVert = \sqrt{6}, \quad \lVert \mathbf{n}_2 \rVert = \sqrt{6}$$
$$\cos\theta = \frac{3}{6} = \frac{1}{2} \Rightarrow \theta = 60°$$

**Respuesta**: El ángulo entre los planos es $60°$.

---

### Problema 20
**Contexto**: Planos paralelos tienen la misma normal; solo cambia el término independiente.

**Desarrollo**:
El plano buscado tiene normal $\mathbf{n} = \langle 3, -2, 1 \rangle$ y pasa por $(2, 1, -1)$:
$$3(x-2) - 2(y-1) + 1(z+1) = 0$$
$$3x - 2y + z = 6 - 2 - 1 = 3$$

**Respuesta**: $3x - 2y + z = 3$

---

### Problema 21 (Aplicación: Volumen)
**Contexto**: El volumen del paralelepípedo es el valor absoluto del producto triple escalar.

**Desarrollo**:
$$V = |\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})| = \left| \det \begin{pmatrix} 1 & 0 & 2 \\ 0 & 3 & 1 \\ 2 & 1 & 0 \end{pmatrix} \right|$$

Expandiendo por la primera fila:
$$= |1(0-1) - 0 + 2(0-6)| = |-1 - 12| = 13$$

**Respuesta**: Volumen $= 13$ unidades cúbicas.

---

### Problema 22 (Aplicación: Trabajo)
**Contexto**: El trabajo es el producto escalar de la fuerza por el desplazamiento.

**Desarrollo**:
$$\mathbf{d} = \overrightarrow{AB} = \langle 3, 2, -2 \rangle$$
$$W = \mathbf{F} \cdot \mathbf{d} = 3(3) + 4(2) + (-2)(-2) = 9 + 8 + 4 = 21 \text{ J}$$

**Respuesta**: Trabajo $= 21$ Joules.

---

### Problema 23 (Aplicación: Torque)
**Contexto**: El torque es el producto vectorial del vector posición por la fuerza.

**Desarrollo**:
$$\mathbf{r} = \langle 3, 0, 0 \rangle, \quad \mathbf{F} = \langle 0, 5, 0 \rangle$$
$$\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 3 & 0 & 0 \\ 0 & 5 & 0 \end{vmatrix} = \langle 0, 0, 15 \rangle$$

**Respuesta**: $\boldsymbol{\tau} = \langle 0, 0, 15 \rangle$ N·m (torque en dirección $z$).

---

<!--
IA: Sigue este formato al generar soluciones:
1. Contexto breve (qué método/concepto se usa)
2. Desarrollo paso a paso
3. Respuesta final claramente marcada
-->
