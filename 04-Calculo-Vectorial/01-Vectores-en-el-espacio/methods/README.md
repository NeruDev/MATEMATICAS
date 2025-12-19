# Métodos — Vectores en el espacio

<!--
IA: Al presentar métodos, incluye siempre:
1. Cuándo usar este método (contexto)
2. Pasos detallados
3. Un ejemplo resuelto completo
4. Verificación del resultado
-->

---

## Método 1: Calcular magnitud y vector unitario

### ¿Cuándo usarlo?
Cuando necesitas conocer la "longitud" de un vector o normalizarlo para trabajar solo con su dirección.

### Pasos detallados
1. **Identifica las componentes** del vector $\mathbf{v} = \langle v_x, v_y, v_z \rangle$.
2. **Calcula la magnitud** aplicando:
   $$\lVert \mathbf{v} \rVert = \sqrt{v_x^2 + v_y^2 + v_z^2}$$
3. **Obtén el vector unitario** dividiendo cada componente entre la magnitud:
   $$\hat{\mathbf{v}} = \frac{\mathbf{v}}{\lVert \mathbf{v} \rVert} = \left\langle \frac{v_x}{\lVert \mathbf{v} \rVert}, \frac{v_y}{\lVert \mathbf{v} \rVert}, \frac{v_z}{\lVert \mathbf{v} \rVert} \right\rangle$$

### Ejemplo práctico
**Problema**: Dado $\mathbf{v} = \langle 3, -4, 12 \rangle$, encuentra su magnitud y su vector unitario.

**Solución**:
1. Componentes: $v_x = 3$, $v_y = -4$, $v_z = 12$.
2. Magnitud:
   $$\lVert \mathbf{v} \rVert = \sqrt{3^2 + (-4)^2 + 12^2} = \sqrt{9 + 16 + 144} = \sqrt{169} = 13$$
3. Vector unitario:
   $$\hat{\mathbf{v}} = \frac{1}{13}\langle 3, -4, 12 \rangle = \left\langle \frac{3}{13}, -\frac{4}{13}, \frac{12}{13} \right\rangle$$

**Verificación**: $\lVert \hat{\mathbf{v}} \rVert = \sqrt{(3/13)^2 + (-4/13)^2 + (12/13)^2} = \sqrt{169/169} = 1$ ✓

---

## Método 2: Calcular el ángulo entre dos vectores

### ¿Cuándo usarlo?
Para determinar si dos vectores son perpendiculares, paralelos, o calcular el ángulo exacto entre ellos.

### Pasos detallados
1. **Calcula el producto escalar** $\mathbf{u} \cdot \mathbf{v}$.
2. **Calcula las magnitudes** $\lVert \mathbf{u} \rVert$ y $\lVert \mathbf{v} \rVert$.
3. **Aplica la fórmula**:
   $$\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert}$$
4. **Despeja** $\theta = \arccos(\cdots)$.

**Casos especiales rápidos**:
- Si $\mathbf{u} \cdot \mathbf{v} = 0 \Rightarrow \theta = 90°$ (perpendiculares).
- Si $\mathbf{u} \cdot \mathbf{v} = \lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert \Rightarrow \theta = 0°$ (paralelos, mismo sentido).

### Ejemplo práctico
**Problema**: Encuentra el ángulo entre $\mathbf{u} = \langle 1, 2, -1 \rangle$ y $\mathbf{v} = \langle 2, -1, 2 \rangle$.

**Solución**:
1. Producto escalar:
   $$\mathbf{u} \cdot \mathbf{v} = (1)(2) + (2)(-1) + (-1)(2) = 2 - 2 - 2 = -2$$
2. Magnitudes:
   $$\lVert \mathbf{u} \rVert = \sqrt{1 + 4 + 1} = \sqrt{6}$$
   $$\lVert \mathbf{v} \rVert = \sqrt{4 + 1 + 4} = \sqrt{9} = 3$$
3. Coseno del ángulo:
   $$\cos\theta = \frac{-2}{\sqrt{6} \cdot 3} = \frac{-2}{3\sqrt{6}} = -\frac{2\sqrt{6}}{18} = -\frac{\sqrt{6}}{9}$$
4. Ángulo:
   $$\theta = \arccos\left(-\frac{\sqrt{6}}{9}\right) \approx 99.6°$$

**Verificación**: El coseno es negativo, así que el ángulo es obtuso (entre 90° y 180°), lo cual es consistente.

---

## Método 3: Calcular la proyección de un vector sobre otro

### ¿Cuándo usarlo?
Para descomponer un vector en una componente paralela y otra perpendicular a una dirección dada. Útil en física (trabajo, fuerzas).

### Pasos detallados
1. **Calcula** $\mathbf{u} \cdot \mathbf{v}$ y $\lVert \mathbf{v} \rVert^2 = \mathbf{v} \cdot \mathbf{v}$.
2. **Proyección escalar** (componente):
   $$\text{comp}_{\mathbf{v}}\mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{v} \rVert}$$
3. **Proyección vectorial**:
   $$\text{proy}_{\mathbf{v}}\mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{v} \rVert^2}\mathbf{v}$$

### Ejemplo práctico
**Problema**: Proyecta $\mathbf{u} = \langle 4, 2, 0 \rangle$ sobre $\mathbf{v} = \langle 1, 1, 1 \rangle$.

**Solución**:
1. $\mathbf{u} \cdot \mathbf{v} = 4 + 2 + 0 = 6$
2. $\lVert \mathbf{v} \rVert^2 = 1 + 1 + 1 = 3$
3. Proyección vectorial:
   $$\text{proy}_{\mathbf{v}}\mathbf{u} = \frac{6}{3}\langle 1, 1, 1 \rangle = 2\langle 1, 1, 1 \rangle = \langle 2, 2, 2 \rangle$$

**Verificación**: La proyección debe ser paralela a $\mathbf{v}$: $\langle 2, 2, 2 \rangle = 2\langle 1, 1, 1 \rangle$ ✓

---

## Método 4: Calcular el producto vectorial

### ¿Cuándo usarlo?
- Para encontrar un vector perpendicular a otros dos.
- Para calcular el área de un paralelogramo.
- Para obtener la normal de un plano.

### Pasos detallados
1. **Organiza en determinante**:
   $$\mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_x & u_y & u_z \\ v_x & v_y & v_z \end{vmatrix}$$
2. **Expande por cofactores** de la primera fila:
   - Componente $\mathbf{i}$: $(u_y v_z - u_z v_y)$
   - Componente $\mathbf{j}$: $-(u_x v_z - u_z v_x) = (u_z v_x - u_x v_z)$
   - Componente $\mathbf{k}$: $(u_x v_y - u_y v_x)$
3. **Resultado**:
   $$\mathbf{u} \times \mathbf{v} = \langle u_y v_z - u_z v_y, \; u_z v_x - u_x v_z, \; u_x v_y - u_y v_x \rangle$$

### Ejemplo práctico
**Problema**: Calcula $\mathbf{u} \times \mathbf{v}$ para $\mathbf{u} = \langle 1, 2, -1 \rangle$ y $\mathbf{v} = \langle 2, -1, 2 \rangle$.

**Solución**:
$$\mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & -1 \\ 2 & -1 & 2 \end{vmatrix}$$

- $\mathbf{i}$: $(2)(2) - (-1)(-1) = 4 - 1 = 3$
- $\mathbf{j}$: $-[(1)(2) - (-1)(2)] = -[2 + 2] = -4$
- $\mathbf{k}$: $(1)(-1) - (2)(2) = -1 - 4 = -5$

$$\mathbf{u} \times \mathbf{v} = \langle 3, -4, -5 \rangle$$

**Verificación**: Comprueba ortogonalidad:
- $\mathbf{u} \cdot (\mathbf{u} \times \mathbf{v}) = (1)(3) + (2)(-4) + (-1)(-5) = 3 - 8 + 5 = 0$ ✓
- $\mathbf{v} \cdot (\mathbf{u} \times \mathbf{v}) = (2)(3) + (-1)(-4) + (2)(-5) = 6 + 4 - 10 = 0$ ✓

---

## Método 5: Ecuación de la recta en el espacio

### ¿Cuándo usarlo?
Para describir una recta dados un punto y una dirección, o dos puntos.

### Pasos detallados
1. **Identifica el punto** $P_0 = (x_0, y_0, z_0)$.
2. **Identifica la dirección** $\mathbf{v} = \langle a, b, c \rangle$.
   - Si tienes dos puntos $A$ y $B$: $\mathbf{v} = \overrightarrow{AB}$.
3. **Escribe la forma vectorial**: $\mathbf{r}(t) = \mathbf{r}_0 + t\mathbf{v}$.
4. **Forma paramétrica**: separa componentes.
5. **Forma simétrica** (si $a, b, c \neq 0$): despeja $t$ de cada ecuación.

### Ejemplo práctico
**Problema**: Encuentra las ecuaciones de la recta que pasa por $A = (1, 0, 2)$ y $B = (3, 1, 1)$.

**Solución**:
1. Punto: $P_0 = A = (1, 0, 2)$
2. Dirección: $\mathbf{v} = \overrightarrow{AB} = \langle 3-1, 1-0, 1-2 \rangle = \langle 2, 1, -1 \rangle$
3. **Forma vectorial**:
   $$\mathbf{r}(t) = \langle 1, 0, 2 \rangle + t\langle 2, 1, -1 \rangle$$
4. **Forma paramétrica**:
   $$x = 1 + 2t, \quad y = t, \quad z = 2 - t$$
5. **Forma simétrica**:
   $$\frac{x - 1}{2} = \frac{y - 0}{1} = \frac{z - 2}{-1}$$

**Verificación**: En $t = 0$, obtenemos $A = (1, 0, 2)$; en $t = 1$, obtenemos $B = (3, 1, 1)$ ✓

---

## Método 6: Intersección de recta con plano

### ¿Cuándo usarlo?
Para encontrar el punto donde una recta atraviesa un plano.

### Pasos detallados
1. **Escribe la recta en forma paramétrica**: $x = x_0 + at$, etc.
2. **Sustituye** en la ecuación del plano $ax + by + cz = d$.
3. **Resuelve para $t$**.
4. **Sustituye $t$** en las ecuaciones paramétricas para obtener el punto.

### Ejemplo práctico
**Problema**: Encuentra la intersección de la recta $\mathbf{r}(t) = \langle 1+2t, t, 2-t \rangle$ con el plano $2x - y + 2z = 5$.

**Solución**:
1. Sustituye en el plano:
   $$2(1 + 2t) - (t) + 2(2 - t) = 5$$
2. Simplifica:
   $$2 + 4t - t + 4 - 2t = 5$$
   $$6 + t = 5$$
   $$t = -1$$
3. Punto de intersección:
   $$x = 1 + 2(-1) = -1, \quad y = -1, \quad z = 2 - (-1) = 3$$
   
**Punto**: $(-1, -1, 3)$

**Verificación**: Sustituye en el plano: $2(-1) - (-1) + 2(3) = -2 + 1 + 6 = 5$ ✓

---

## Método 7: Ecuación del plano

### ¿Cuándo usarlo?
Para describir un plano dado un punto y un vector normal, o tres puntos.

### Pasos detallados (con punto y normal)
1. **Identifica** punto $P_0 = (x_0, y_0, z_0)$ y normal $\mathbf{n} = \langle a, b, c \rangle$.
2. **Forma vectorial**: $\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0$.
3. **Expande** a forma escalar: $a(x - x_0) + b(y - y_0) + c(z - z_0) = 0$.
4. **Simplifica**: $ax + by + cz = d$ donde $d = ax_0 + by_0 + cz_0$.

### Pasos detallados (con tres puntos)
1. **Calcula** $\overrightarrow{AB}$ y $\overrightarrow{AC}$.
2. **Normal**: $\mathbf{n} = \overrightarrow{AB} \times \overrightarrow{AC}$.
3. Usa el método anterior con cualquiera de los tres puntos.

### Ejemplo práctico
**Problema**: Encuentra el plano que pasa por $A = (1, 0, 0)$, $B = (0, 2, 0)$, $C = (0, 0, 3)$.

**Solución**:
1. Vectores:
   - $\overrightarrow{AB} = \langle -1, 2, 0 \rangle$
   - $\overrightarrow{AC} = \langle -1, 0, 3 \rangle$
2. Normal:
   $$\mathbf{n} = \overrightarrow{AB} \times \overrightarrow{AC} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -1 & 2 & 0 \\ -1 & 0 & 3 \end{vmatrix} = \langle 6, 3, 2 \rangle$$
3. Ecuación usando $A = (1, 0, 0)$:
   $$6(x - 1) + 3(y - 0) + 2(z - 0) = 0$$
   $$6x + 3y + 2z = 6$$

**Verificación**: Sustituye cada punto en la ecuación ✓

---

## Método 8: Distancia de un punto a un plano

### ¿Cuándo usarlo?
Para medir la distancia perpendicular desde un punto al plano más cercano.

### Pasos detallados
1. **Escribe el plano** en forma $ax + by + cz = d$.
2. **Identifica** el punto $Q = (x_1, y_1, z_1)$.
3. **Aplica la fórmula**:
   $$D = \frac{|ax_1 + by_1 + cz_1 - d|}{\sqrt{a^2 + b^2 + c^2}}$$

### Ejemplo práctico
**Problema**: Distancia de $Q = (3, -1, 4)$ al plano $x + 2y - 2z = 7$.

**Solución**:
1. Coeficientes: $a = 1$, $b = 2$, $c = -2$, $d = 7$.
2. Numerador: $|1(3) + 2(-1) + (-2)(4) - 7| = |3 - 2 - 8 - 7| = |-14| = 14$
3. Denominador: $\sqrt{1 + 4 + 4} = \sqrt{9} = 3$
4. Distancia:
   $$D = \frac{14}{3} \approx 4.67$$

**Verificación**: El denominador es la norma del vector normal $\langle 1, 2, -2 \rangle$, que efectivamente es 3.

---

<!--
IA: Al explicar métodos, sigue este formato:
- Contexto de uso
- Pasos numerados
- Ejemplo completo con verificación
Esto facilita el aprendizaje autónomo.
-->
