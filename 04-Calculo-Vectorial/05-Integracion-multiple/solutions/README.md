# Soluciones — Integración múltiple

---

## Nivel Básico

### Problema 1
**Contexto**: Para una integral doble sobre un rectángulo, integramos iteradamente en cualquier orden.

$$\int_0^1 \int_0^2 (x + y)\,dy\,dx = \int_0^1 \left[ xy + \frac{y^2}{2} \right]_0^2 dx = \int_0^1 (2x + 2)\,dx$$
$$= \left[ x^2 + 2x \right]_0^1 = 1 + 2 = 3$$

---

### Problema 2
**Contexto**: Aplicamos Fubini ya que el integrando se puede separar en producto de funciones.

$$\int_0^2 \int_0^1 xy^2\,dy\,dx = \int_0^2 x\,dx \cdot \int_0^1 y^2\,dy = \left[ \frac{x^2}{2} \right]_0^2 \cdot \left[ \frac{y^3}{3} \right]_0^1 = 2 \cdot \frac{1}{3} = \frac{2}{3}$$

---

### Problema 5
**Contexto**: Para cambiar el orden, dibujamos la región y reescribimos los límites.

Región: $0 \leq x \leq 1$, $0 \leq y \leq x$ (triángulo debajo de $y = x$)

Invirtiendo: $0 \leq y \leq 1$, $y \leq x \leq 1$

$$\int_0^1 \int_0^x f(x,y)\,dy\,dx = \int_0^1 \int_y^1 f(x,y)\,dx\,dy$$

---

### Problema 7
**Contexto**: El triángulo tiene $x \geq 0$, $y \geq 0$, $x + y \leq 1$. Usamos Tipo I.

$$\iint_R y\,dA = \int_0^1 \int_0^{1-x} y\,dy\,dx = \int_0^1 \left[ \frac{y^2}{2} \right]_0^{1-x} dx = \int_0^1 \frac{(1-x)^2}{2}\,dx$$
$$= \frac{1}{2} \left[ -\frac{(1-x)^3}{3} \right]_0^1 = \frac{1}{2} \cdot \frac{1}{3} = \frac{1}{6}$$

---

## Nivel Intermedio

### Problema 9
**Contexto**: La simetría circular del disco y el integrando sugieren coordenadas polares.

En polares: $x^2 + y^2 = r^2$, $dA = r\,dr\,d\theta$

$$\int_0^{2\pi} \int_0^1 r^2 \cdot r\,dr\,d\theta = \int_0^{2\pi} d\theta \int_0^1 r^3\,dr = 2\pi \cdot \left[ \frac{r^4}{4} \right]_0^1 = 2\pi \cdot \frac{1}{4} = \frac{\pi}{2}$$

---

### Problema 10
**Contexto**: El anillo y el integrando $\frac{1}{r}$ son ideales para polares.

$$\int_0^{2\pi} \int_1^2 \frac{1}{r} \cdot r\,dr\,d\theta = \int_0^{2\pi} d\theta \int_1^2 dr = 2\pi \cdot (2 - 1) = 2\pi$$

---

### Problema 11
**Contexto**: El área en polares se calcula con $\frac{1}{2}\int r^2\,d\theta$.

$$A = \frac{1}{2} \int_0^{2\pi} (1 + \cos\theta)^2\,d\theta = \frac{1}{2} \int_0^{2\pi} (1 + 2\cos\theta + \cos^2\theta)\,d\theta$$

$$= \frac{1}{2}\left[ 2\pi + 0 + \pi \right] = \frac{3\pi}{2}$$

---

### Problema 13
**Contexto**: El tetraedro estándar tiene volumen $\frac{1}{6}$ del paralelepípedo unitario.

$$V = \int_0^1 \int_0^{1-x} \int_0^{1-x-y} dz\,dy\,dx = \int_0^1 \int_0^{1-x} (1-x-y)\,dy\,dx$$
$$= \int_0^1 \frac{(1-x)^2}{2}\,dx = \frac{1}{2} \cdot \frac{1}{3} = \frac{1}{6}$$

---

### Problema 16
**Contexto**: El cilindro circular es ideal para coordenadas cilíndricas.

$$V = \int_0^{2\pi} \int_0^2 \int_0^3 r\,dz\,dr\,d\theta = \int_0^{2\pi} d\theta \int_0^2 r\,dr \int_0^3 dz$$
$$= 2\pi \cdot \left[ \frac{r^2}{2} \right]_0^2 \cdot 3 = 2\pi \cdot 2 \cdot 3 = 12\pi$$

**Verificación**: $V = \pi r^2 h = \pi(4)(3) = 12\pi$ ✓

---

### Problema 19
**Contexto**: La esfera tiene simetría esférica perfecta; usamos coordenadas esféricas.

$$V = \int_0^{2\pi} \int_0^{\pi} \int_0^3 \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$$
$$= 2\pi \cdot [-\cos\phi]_0^{\pi} \cdot \left[ \frac{\rho^3}{3} \right]_0^3 = 2\pi \cdot 2 \cdot 9 = 36\pi$$

**Verificación**: $V = \frac{4}{3}\pi r^3 = \frac{4}{3}\pi(27) = 36\pi$ ✓

---

### Problema 20
**Contexto**: En esféricas, $x^2 + y^2 + z^2 = \rho^2$, lo que simplifica enormemente el integrando.

$$\iiint_V \rho^2 \cdot \rho^2\sin\phi\,d\rho\,d\phi\,d\theta = \int_0^{2\pi} d\theta \int_0^{\pi} \sin\phi\,d\phi \int_0^a \rho^4\,d\rho$$
$$= 2\pi \cdot 2 \cdot \frac{a^5}{5} = \frac{4\pi a^5}{5}$$

---

## Nivel Avanzado

### Problema 22
**Contexto**: Parametrizamos el segmento de recta y calculamos el producto punto.

Parametrización: $\mathbf{r}(t) = \langle t, 2t \rangle$, $t \in [0, 1]$, $\mathbf{r}'(t) = \langle 1, 2 \rangle$

$\mathbf{F}(\mathbf{r}(t)) = \langle 2t, t \rangle$

$$\int_0^1 \langle 2t, t \rangle \cdot \langle 1, 2 \rangle\,dt = \int_0^1 (2t + 2t)\,dt = 4 \int_0^1 t\,dt = 4 \cdot \frac{1}{2} = 2$$

---

### Problema 23
**Contexto**: Esta es una integral de línea respecto a longitud de arco ($ds$), no de trabajo.

Parametrización: $\mathbf{r}(t) = \langle 2\cos t, 2\sin t \rangle$, $t \in [0, 2\pi]$

$ds = \|\mathbf{r}'(t)\|\,dt = 2\,dt$, $x^2 + y^2 = 4$

$$\int_C 4\,ds = \int_0^{2\pi} 4 \cdot 2\,dt = 8 \cdot 2\pi = 16\pi$$

---

### Problema 25
**Contexto**: Verificamos si el campo es conservativo comprobando $\nabla \times \mathbf{F} = \mathbf{0}$.

$\mathbf{F} = \langle 2xy, x^2 + z, y \rangle$

$$\nabla \times \mathbf{F} = \langle \frac{\partial}{\partial y}(y) - \frac{\partial}{\partial z}(x^2+z), \frac{\partial}{\partial z}(2xy) - \frac{\partial}{\partial x}(y), \frac{\partial}{\partial x}(x^2+z) - \frac{\partial}{\partial y}(2xy) \rangle$$
$$= \langle 1 - 1, 0 - 0, 2x - 2x \rangle = \langle 0, 0, 0 \rangle$$

**Es conservativo**. Potencial: $f_x = 2xy \Rightarrow f = x^2y + g(y,z)$
$f_y = x^2 + g_y = x^2 + z \Rightarrow g_y = z \Rightarrow g = yz + h(z)$
$f_z = y + h'(z) = y \Rightarrow h'(z) = 0 \Rightarrow h = C$

**Potencial**: $f(x,y,z) = x^2y + yz + C$

---

### Problema 26
**Contexto**: Green convierte la integral de línea cerrada en una integral doble.

$P = x^2 - y$, $Q = y^2 + x$

$Q_x - P_y = 1 - (-1) = 2$

$$\oint_C = \iint_R 2\,dA = 2 \cdot \pi(1)^2 = 2\pi$$

---

### Problema 27
**Contexto**: El área se puede calcular con la fórmula de Green: $A = \frac{1}{2}\oint_C (x\,dy - y\,dx)$.

Parametrizamos la elipse: $x = 2\cos t$, $y = \sin t$, $t \in [0, 2\pi]$

$dx = -2\sin t\,dt$, $dy = \cos t\,dt$

$$A = \frac{1}{2}\int_0^{2\pi} (2\cos t \cdot \cos t - \sin t \cdot (-2\sin t))\,dt$$
$$= \frac{1}{2}\int_0^{2\pi} (2\cos^2 t + 2\sin^2 t)\,dt = \frac{1}{2} \cdot 2 \cdot 2\pi = 2\pi$$

---

### Problema 29
**Contexto**: Gauss convierte el flujo en una integral de volumen de la divergencia.

$\nabla \cdot \mathbf{F} = 1 + 1 + 1 = 3$

Volumen de la esfera de radio 2: $V = \frac{4}{3}\pi(8) = \frac{32\pi}{3}$

$$\oiint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_V 3\,dV = 3 \cdot \frac{32\pi}{3} = 32\pi$$

---

### Problema 32
**Contexto**: Stokes relaciona circulación con flujo del rotacional. Es más fácil usar el rotacional.

$$\nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \partial_x & \partial_y & \partial_z \\ -y & x & 0 \end{vmatrix} = \langle 0, 0, 1+1 \rangle = \langle 0, 0, 2 \rangle$$

Superficie: disco en $z = 0$, $\mathbf{n} = \mathbf{k}$

$$\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_S \langle 0, 0, 2 \rangle \cdot \langle 0, 0, 1 \rangle\,dA = 2 \cdot \pi(1)^2 = 2\pi$$

---

### Problema 35
**Contexto**: La masa es la integral doble de la densidad sobre la región.

$$M = \iint_R xy\,dA = \int_0^2 \int_0^{2-x} xy\,dy\,dx = \int_0^2 x \cdot \frac{(2-x)^2}{2}\,dx$$

$$= \frac{1}{2}\int_0^2 x(4 - 4x + x^2)\,dx = \frac{1}{2}\int_0^2 (4x - 4x^2 + x^3)\,dx$$

$$= \frac{1}{2}\left[ 2x^2 - \frac{4x^3}{3} + \frac{x^4}{4} \right]_0^2 = \frac{1}{2}\left( 8 - \frac{32}{3} + 4 \right) = \frac{1}{2} \cdot \frac{4}{3} = \frac{2}{3}$$

---

### Problema 39
**Contexto**: El trabajo en una trayectoria cerrada no nula indica que el campo no es conservativo.

$\mathbf{F} = \langle -y, x \rangle$, $Q_x - P_y = 1 - (-1) = 2$

Por Green:
$$W = \oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_R 2\,dA = 2 \cdot \text{Área de elipse} = 2 \cdot 2\pi = 4\pi$$

(Área de la elipse $\frac{x^2}{4} + y^2 = 1$ es $\pi \cdot 2 \cdot 1 = 2\pi$)
